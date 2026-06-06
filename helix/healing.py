"""Self-healing controller.

When the monitor flags a failure/loop, the healer does not blindly retry. It:
  1. recalls how a *similar error* was handled before (knowledge reuse),
  2. asks an LLM to diagnose the root cause and propose distinct candidate fixes,
  3. has the world-model score those candidate fixes and picks the best,
  4. returns concrete guidance that is injected into the agent's next turn.

The chosen fix is recorded as a recovery decision in the trajectory, with a
``recovers`` edge from the failed outcome, so healing is visible in the graph.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .config import CONFIG
from .llm import ClaudeLLM
from .util import extract_json, trim


@dataclass
class Recovery:
    diagnosis: str = ""
    guidance: str = ""
    candidates: list[str] = field(default_factory=list)
    chosen: str = ""
    predicted_success: float | None = None
    memory_hits: list = field(default_factory=list)
    lessons_text: str = ""


_SYS = (
    "You are a self-healing controller for an autonomous AppWorld coding agent. "
    "The agent's last action failed or the run is stuck. Diagnose the ROOT CAUSE "
    "and propose 2-3 DISTINCT candidate fixes (different APIs/paths, not the same "
    "code retried). Prefer: verifying the exact API signature via "
    "apis.api_docs.show_api_doc, fixing argument names/types, correct login/token "
    "use, and pagination. Return ONLY JSON: "
    "{\"diagnosis\":\"...\",\"candidates\":[\"fix 1\",\"fix 2\"],\"guidance\":\"one concrete instruction for the next step\"}."
)


class SelfHealer:
    def __init__(self, memory=None, world_model=None, model: str | None = None):
        self.memory = memory
        self.world_model = world_model
        self._llm = None
        self._model = model or CONFIG.agent_model

    @property
    def llm(self) -> ClaudeLLM:
        if self._llm is None:
            self._llm = ClaudeLLM(model=self._model, max_tokens=900, temperature=0.0)
        return self._llm

    def plan_recovery(self, instruction: str, observation, recent_history: str,
                      tried_fixes: list | None = None) -> Recovery:
        rec = Recovery()

        # 1. knowledge reuse from past recoveries
        if self.memory is not None:
            try:
                rec.memory_hits = self.memory.recall_for_error(
                    instruction, observation.error_type, observation.error_message,
                    observation.code, k=3)
                rec.lessons_text = self.memory.error_lessons(rec.memory_hits)
            except Exception:
                rec.memory_hits, rec.lessons_text = [], ""

        # repair memory: fixes already tried THIS task that did NOT work
        tried_block = ""
        if tried_fixes:
            seen = "\n".join(f"- (after {t.get('error_type')}) {trim(str(t.get('fix','')), 200)}"
                             for t in tried_fixes[-6:])
            tried_block = ("\n\nALREADY TRIED THIS TASK AND STILL FAILING - do NOT repeat "
                           f"any of these; propose a DIFFERENT root-cause fix:\n{seen}")

        # 2. diagnose + propose candidate fixes
        user = (
            f"TASK: {instruction}\n\nRECENT STEPS:\n{trim(recent_history, 1500)}\n\n"
            f"FAILED CODE:\n{trim(observation.code, 600)}\n\n"
            f"ERROR ({observation.error_type}): {trim(observation.raw, 800)}\n\n"
            f"{rec.lessons_text}{tried_block}\n\nDiagnose the ROOT cause and propose distinct fixes."
        )
        try:
            res = self.llm.complete(_SYS, [{"role": "user", "content": user}],
                                    cache_system=True)
            data = extract_json(res.text) or {}
            rec.diagnosis = str(data.get("diagnosis", ""))[:600]
            rec.candidates = [str(c)[:400] for c in data.get("candidates", []) if str(c).strip()]
            rec.guidance = str(data.get("guidance", ""))[:600]
        except Exception:
            rec.candidates = []

        # 3. world-model scores the candidate fixes; pick best
        if self.world_model is not None and rec.candidates:
            try:
                assessment = self.world_model.assess(
                    instruction, recent_history, rec.candidates)
                best = assessment.best
                if best is not None:
                    rec.chosen = best.plan
                    rec.predicted_success = best.p_success
                    if not rec.guidance:
                        rec.guidance = best.plan
            except Exception:
                pass
        if not rec.chosen and rec.candidates:
            rec.chosen = rec.candidates[0]
        if not rec.guidance:
            rec.guidance = ("Diagnose the exact failing API with "
                            "apis.api_docs.show_api_doc and correct the call.")
        return rec
