"""LLM + embedding layer.

- ClaudeLLM: Anthropic chat with prompt-caching on the (large, static) system
  prompt, exponential-backoff retries, and global token/cost accounting.
- Embedder: OpenAI text-embedding-3 with a disk cache; falls back to a
  deterministic hashing embedding if no OpenAI key is available so the memory
  subsystem never hard-fails.
"""
from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field

import numpy as np

from .config import CACHE_DIR, CONFIG, PRICING

try:
    import anthropic
except Exception:  # pragma: no cover
    anthropic = None

try:
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None


# --------------------------------------------------------------------------- #
# Token / cost accounting
# --------------------------------------------------------------------------- #
@dataclass
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    calls: int = 0
    cost_usd: float = 0.0

    def snapshot(self) -> dict:
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cache_read_tokens": self.cache_read_tokens,
            "cache_write_tokens": self.cache_write_tokens,
            "calls": self.calls,
            "cost_usd": round(self.cost_usd, 4),
        }

    def reset(self) -> None:
        self.__init__()


GLOBAL_USAGE = Usage()


def _cost(model: str, billable_input: int, output: int) -> float:
    if model in PRICING:
        pin, pout = PRICING[model]
        return billable_input / 1e6 * pin + output / 1e6 * pout
    return 0.0


@dataclass
class LLMResult:
    text: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    model: str
    raw: object = field(default=None, repr=False)


class ClaudeLLM:
    """Thin Anthropic wrapper with caching + retries + accounting."""

    def __init__(self, model: str | None = None, max_tokens: int | None = None,
                 temperature: float = 0.0):
        self.model = model or CONFIG.agent_model
        self.max_tokens = max_tokens or CONFIG.max_tokens_per_call
        self.temperature = temperature
        # newest models (e.g. opus-4-8) deprecate the temperature param
        self._no_temp = self.model.startswith("claude-opus-4-8")
        # provider routing: claude-* -> Anthropic, anything else -> Groq (OpenAI-compatible)
        self.provider = "anthropic" if self.model.startswith("claude") else "groq"
        if self.provider == "anthropic":
            if anthropic is None:
                raise RuntimeError("anthropic package not installed in this environment")
            self.client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
        else:
            from openai import OpenAI
            self.client = OpenAI(base_url=CONFIG.groq_base_url, api_key=CONFIG.groq_api_key)

    def _system_blocks(self, system, cache: bool):
        if isinstance(system, str):
            block = {"type": "text", "text": system}
            if cache:
                block["cache_control"] = {"type": "ephemeral"}
            return [block]
        return system

    def complete(self, system, messages, *, max_tokens: int | None = None,
                 temperature: float | None = None, cache_system: bool = True,
                 stop: list[str] | None = None) -> LLMResult:
        if self.provider != "anthropic":
            return self._complete_openai(system, messages, max_tokens, temperature, stop)
        sys_blocks = self._system_blocks(system, cache_system)
        last_err = None
        for attempt in range(6):
            try:
                kwargs = dict(
                    model=self.model,
                    max_tokens=max_tokens or self.max_tokens,
                    system=sys_blocks,
                    messages=messages,
                    stop_sequences=stop or None,
                )
                if not self._no_temp:
                    kwargs["temperature"] = (self.temperature if temperature is None
                                             else temperature)
                resp = self.client.messages.create(**kwargs)
                text = "".join(
                    b.text for b in resp.content if getattr(b, "type", "") == "text"
                )
                u = resp.usage
                inp = u.input_tokens
                out = u.output_tokens
                cr = getattr(u, "cache_read_input_tokens", 0) or 0
                cw = getattr(u, "cache_creation_input_tokens", 0) or 0
                cost = _cost(self.model, inp + cr + cw, out)
                GLOBAL_USAGE.input_tokens += inp + cr + cw
                GLOBAL_USAGE.output_tokens += out
                GLOBAL_USAGE.cache_read_tokens += cr
                GLOBAL_USAGE.cache_write_tokens += cw
                GLOBAL_USAGE.calls += 1
                GLOBAL_USAGE.cost_usd += cost
                return LLMResult(text, inp, out, cost, self.model, resp)
            except Exception as e:  # noqa: BLE001 - retry on any transient API error
                if "temperature" in str(e).lower() and not self._no_temp:
                    self._no_temp = True  # model rejects temperature; drop it and retry
                    continue
                last_err = e
                time.sleep(min(2 ** attempt, 30))
        raise RuntimeError(f"Claude call failed after retries: {last_err}")

    def _complete_openai(self, system, messages, max_tokens, temperature, stop) -> LLMResult:
        """Groq / any OpenAI-compatible chat endpoint (system folded into a message)."""
        sys_text = system if isinstance(system, str) else " ".join(
            b.get("text", "") for b in system)
        msgs = [{"role": "system", "content": sys_text}] + list(messages)
        last_err = None
        for attempt in range(6):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model, messages=msgs,
                    max_tokens=max_tokens or self.max_tokens,
                    temperature=self.temperature if temperature is None else temperature,
                    stop=stop or None,
                )
                text = resp.choices[0].message.content or ""
                u = getattr(resp, "usage", None)
                inp = getattr(u, "prompt_tokens", 0) or 0
                out = getattr(u, "completion_tokens", 0) or 0
                cost = _cost(self.model, inp, out)
                GLOBAL_USAGE.input_tokens += inp
                GLOBAL_USAGE.output_tokens += out
                GLOBAL_USAGE.calls += 1
                GLOBAL_USAGE.cost_usd += cost
                return LLMResult(text, inp, out, cost, self.model, resp)
            except Exception as e:  # noqa: BLE001
                last_err = e
                time.sleep(min(2 ** attempt, 30))
        raise RuntimeError(f"Groq call failed after retries: {last_err}")


class Embedder:
    """OpenAI embeddings with a disk cache and a deterministic fallback."""

    def __init__(self, model: str | None = None):
        self.model = model or CONFIG.embedding_model
        self.dim = CONFIG.embedding_dim
        self._mem: dict[str, np.ndarray] = {}
        self.cache_dir = CACHE_DIR / "embeddings"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.client = OpenAI() if (OpenAI is not None and CONFIG.openai_api_key) else None
        self.fallback = self.client is None

    def _key(self, text: str) -> str:
        return hashlib.sha256(f"{self.model}::{text}".encode("utf-8")).hexdigest()

    def _hash_embed(self, text: str) -> np.ndarray:
        """Deterministic bag-of-hashed-tokens embedding (cosine-meaningful)."""
        v = np.zeros(self.dim, dtype=np.float32)
        for tok in text.lower().split():
            h = int(hashlib.md5(tok.encode()).hexdigest(), 16)
            v[h % self.dim] += 1.0
        n = np.linalg.norm(v)
        return v / n if n > 0 else v

    def embed(self, texts):
        single = isinstance(texts, str)
        items = [texts] if single else list(texts)
        out: list[np.ndarray | None] = [None] * len(items)
        todo: list[tuple[int, str, str]] = []
        for i, t in enumerate(items):
            k = self._key(t)
            if k in self._mem:
                out[i] = self._mem[k]
                continue
            f = self.cache_dir / f"{k}.npy"
            if f.exists():
                v = np.load(f)
                self._mem[k] = v
                out[i] = v
                continue
            todo.append((i, t, k))

        if todo:
            if self.fallback:
                for i, t, k in todo:
                    v = self._hash_embed(t)
                    self._mem[k] = v
                    out[i] = v
            else:
                resp = self.client.embeddings.create(
                    model=self.model, input=[t for _, t, _ in todo]
                )
                for (i, t, k), d in zip(todo, resp.data):
                    v = np.array(d.embedding, dtype=np.float32)
                    self._mem[k] = v
                    np.save(self.cache_dir / f"{k}.npy", v)
                    out[i] = v

        arr = np.vstack([o for o in out])
        return arr[0] if single else arr
