"""World-model branch simulator - model-based planning.

Instead of committing to one plan, the agent proposes a few candidate branches
at key junctions (initial plan + recovery). The world-model scores each branch's
probability of success by combining:
  * a memory prior  - of similar past tasks, how many were solved
  * an LLM estimate - a fast model rates each branch in context

The agent then chooses the highest-probability branch. We record the prediction
and later the actual outcome, which yields a Trajectory Prediction Accuracy metric.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .config import CONFIG
from .llm import ClaudeLLM
from .util import extract_json, trim


@dataclass
class Branch:
    plan: str
    p_success: float = 0.5
    rationale: str = ""
    source: str = "uniform"


@dataclass
class Assessment:
    branches: list[Branch] = field(default_factory=list)
    prior: float | None = None

    @property
    def best(self) -> Branch | None:
        return max(self.branches, key=lambda b: b.p_success) if self.branches else None


_SYS = (
    "You are a world-model for an autonomous coding agent operating AppWorld "
    "(apps like spotify, gmail, venmo, amazon, todoist via python APIs). "
    "Given a task and candidate next-step plans, estimate each plan's probability "
    "of leading to overall task success. Reward plans that verify assumptions via "
    "apis.api_docs, handle pagination, and avoid irreversible mistakes. "
    "Return ONLY JSON: {\"branches\":[{\"index\":int,\"p_success\":0..1,\"rationale\":\"<=15 words\"}]}."
)


class WorldModel:
    def __init__(self, memory=None, model: str | None = None):
        self.memory = memory
        self._llm = None
        self._model = model or CONFIG.world_model_model

    @property
    def llm(self) -> ClaudeLLM:
        if self._llm is None:
            self._llm = ClaudeLLM(model=self._model, max_tokens=600, temperature=0.0)
        return self._llm

    def assess(self, instruction: str, context: str, plans: list[str]) -> Assessment:
        prior = None
        if self.memory is not None:
            try:
                prior = self.memory.success_prior(instruction)
            except Exception:
                prior = None

        llm_scores = self._llm_scores(instruction, context, plans)
        branches: list[Branch] = []
        for i, plan in enumerate(plans):
            llm_p = llm_scores.get(i, {}).get("p", 0.5)
            rationale = llm_scores.get(i, {}).get("r", "")
            if prior is not None:
                p = round(0.7 * llm_p + 0.3 * prior, 3)
                source = "llm+memory"
            else:
                p = round(llm_p, 3)
                source = "llm"
            branches.append(Branch(plan=plan, p_success=p, rationale=rationale, source=source))
        return Assessment(branches=branches, prior=prior)

    def _llm_scores(self, instruction: str, context: str, plans: list[str]) -> dict:
        listing = "\n".join(f"[{i}] {trim(p, 280)}" for i, p in enumerate(plans))
        user = (f"TASK: {instruction}\n\nCURRENT CONTEXT:\n{trim(context, 800)}\n\n"
                f"CANDIDATE PLANS:\n{listing}\n\nScore each plan.")
        try:
            res = self.llm.complete(_SYS, [{"role": "user", "content": user}],
                                    cache_system=True)
            data = extract_json(res.text) or {}
            out = {}
            for row in data.get("branches", []):
                idx = int(row.get("index"))
                out[idx] = {"p": float(row.get("p_success", 0.5)),
                            "r": str(row.get("rationale", ""))[:120]}
            return out
        except Exception:
            return {}
