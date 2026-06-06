"""Trajectory memory - retrieval-augmented decisions + knowledge reuse.

Indexes finished trajectories at two granularities:
  * task-level   : instruction -> the approach (winning code steps) that solved it
  * step-level   : (situation, action) -> outcome, so we can retrieve what fixed a
                   similar error before (the self-healing knowledge base)

Before a task we recall similar *solved* approaches; on a failure we recall how a
similar error was recovered. This is how a later task benefits from earlier ones
- the "trajectories instead of tokens" idea, made concrete.
"""
from __future__ import annotations

import json

from ..config import CONFIG
from ..llm import Embedder
from .store import Hit, VectorStore, get_vector_store


def situation_text(instruction: str, context: str, intent: str) -> str:
    return (f"TASK: {instruction.strip()}\n"
            f"CONTEXT: {context.strip()[:400]}\n"
            f"INTENT: {intent.strip()[:300]}")


def _trim(s: str, n: int) -> str:
    s = (s or "").strip()
    return (s[:n] + "...") if len(s) > n else s


class TrajectoryMemory:
    def __init__(self, store: VectorStore | None = None, embedder: Embedder | None = None):
        self.store = store or get_vector_store(CONFIG.hydra_collection)
        self.embedder = embedder or Embedder()

    @property
    def backend(self) -> str:
        return self.store.backend

    def __len__(self) -> int:
        return len(self.store)

    # -- indexing ---------------------------------------------------------- #
    def index_trajectory(self, traj) -> int:
        """Store task- and step-level records from a finished trajectory."""
        solved = bool(traj.solved)
        # build action -> (decision, outcome) maps from edges
        a2d, a2o = {}, {}
        for e in traj.edges:
            if e.relation == "acts":
                a2d[e.dst] = e.src
            elif e.relation == "yields":
                a2o[e.src] = e.dst

        records: list[tuple[str, str, dict]] = []
        approach_steps: list[str] = []
        for action in traj.nodes_of("action"):
            dec = traj.node(a2d.get(action.id))
            out = traj.node(a2o.get(action.id))
            thought = (dec.data.get("thought", "") if dec else "")
            context = (dec.data.get("context", "") if dec else "")
            code = action.data.get("code", "")
            status = out.status if out else "ok"
            etype = (out.data.get("error_type") if out else None)
            approach_steps.append(_trim(code, 240))
            text = situation_text(traj.instruction, context, thought or code)
            payload = {
                "type": "step",
                "task_id": traj.task_id,
                "split": traj.split,
                "instruction": _trim(traj.instruction, 300),
                "thought": _trim(thought, 240),
                "code": _trim(code, 400),
                "status": status,
                "error_type": etype,
                "solved": solved,
                "step": action.step,
            }
            records.append((f"{traj.task_id}:step:{action.id}", text, payload))

        if solved and approach_steps:
            approach = "\n".join(f"{i + 1}. {s}" for i, s in enumerate(approach_steps))
            records.append((
                f"{traj.task_id}:task",
                f"TASK: {traj.instruction.strip()}",
                {
                    "type": "task",
                    "task_id": traj.task_id,
                    "split": traj.split,
                    "instruction": _trim(traj.instruction, 400),
                    "solved": True,
                    "approach": _trim(approach, 2000),
                    "num_steps": traj.num_steps,
                    "apps": ",".join(traj.allowed_apps),
                    # store the trajectory GRAPH itself (nodes+edges), not just the vector
                    "graph": json.dumps(traj.compact_graph()),
                },
            ))

        if not records:
            return 0
        vecs = self.embedder.embed([t for _, t, _ in records])
        self.store.add_many((rid, vecs[i], payload)
                            for i, (rid, _, payload) in enumerate(records))
        self.store.save()

        # also feed the trajectory into HydraDB's managed knowledge graph
        # (LLM entity/relation extraction -> token usage + a queryable graph)
        if hasattr(self.store, "ingest_knowledge"):
            try:
                self.store.ingest_knowledge(
                    traj.task_id, self._knowledge_text(traj, solved, approach_steps),
                    {"title": _trim(traj.instruction, 80),
                     "apps": ",".join(traj.allowed_apps[:6]),
                     "solved": solved, "steps": traj.num_steps,
                     "recoveries": traj.num_recoveries})
            except Exception:
                pass
        return len(records)

    @staticmethod
    def _knowledge_text(traj, solved: bool, approach_steps: list[str]) -> str:
        parts = [
            f"AppWorld task {traj.task_id}: {traj.instruction}",
            f"Apps available: {', '.join(traj.allowed_apps)}",
            f"Outcome: {'SOLVED' if solved else 'FAILED'} in {traj.num_steps} steps, "
            f"{traj.num_errors} errors, {traj.num_recoveries} self-healing recoveries.",
        ]
        if solved and approach_steps:
            parts.append("Approach that worked:\n" + "\n".join(approach_steps[:12]))
        else:
            errs = sorted({o.data.get("error_type") for o in traj.nodes_of("outcome")
                           if o.status == "error" and o.data.get("error_type")})
            if errs:
                parts.append("Errors encountered: " + ", ".join(errs))
        return "\n".join(parts)

    # -- recall ------------------------------------------------------------ #
    def recall_for_task(self, instruction: str, k: int = 3) -> list[Hit]:
        if len(self.store) == 0:
            return []
        q = self.embedder.embed(f"TASK: {instruction.strip()}")
        hits = self.store.search(q, k=k * 4, where={"type": "task"})
        return [h for h in hits if h.payload.get("solved")][:k]

    def recall_for_error(self, instruction: str, error_type: str | None,
                         error_message: str, code: str, k: int = 3) -> list[Hit]:
        if len(self.store) == 0:
            return []
        ctx = f"ERROR {error_type}: {error_message}"
        q = self.embedder.embed(situation_text(instruction, ctx, code))
        hits = self.store.search(q, k=k * 6, where={"type": "step"})
        # prefer steps that ultimately came from solved trajectories
        ranked = sorted(hits, key=lambda h: (not h.payload.get("solved"), -h.score))
        return ranked[:k]

    def recall_for_step(self, instruction: str, context: str, k: int = 2) -> list[Hit]:
        """Procedural recall: the (situation -> action) patterns that worked in a
        similar spot, even when the overall trajectory differs."""
        if len(self.store) == 0:
            return []
        q = self.embedder.embed(situation_text(instruction, context, ""))
        hits = self.store.search(q, k=k * 6, where={"type": "step"})
        ranked = sorted(hits, key=lambda h: (
            h.payload.get("status") == "error",       # successful steps first
            not h.payload.get("solved"),               # from solved trajectories first
            -h.score))
        return [h for h in ranked if h.payload.get("status") != "error"][:k]

    def success_prior(self, instruction: str, k: int = 8) -> float | None:
        if len(self.store) == 0:
            return None
        q = self.embedder.embed(f"TASK: {instruction.strip()}")
        hits = self.store.search(q, k=k, where={"type": "task"})
        if not hits:
            return None
        return round(sum(1 for h in hits if h.payload.get("solved")) / len(hits), 3)

    # -- prompt formatting ------------------------------------------------- #
    @staticmethod
    def task_lessons(hits: list[Hit]) -> str:
        if not hits:
            return ""
        parts = ["PRIOR EXPERIENCE - approaches that solved similar tasks:"]
        for i, h in enumerate(hits, 1):
            p = h.payload
            parts.append(f"\n[Similar solved task {i} | sim={h.score:.2f}] "
                         f"\"{p.get('instruction', '')}\"\nApproach that worked:\n{p.get('approach', '')}")
        parts.append("\nReuse the *pattern* above (apps/APIs/order), but always "
                     "re-check the current task's specifics with apis.api_docs.")
        return "\n".join(parts)

    @staticmethod
    def step_hints(hits: list[Hit]) -> str:
        if not hits:
            return ""
        parts = ["PROCEDURAL HINTS - code patterns that worked in a similar situation "
                 "(adapt to the current ids/values, do not copy verbatim):"]
        for h in hits:
            parts.append(f"# (sim={h.score:.2f})\n{h.payload.get('code', '')}")
        return "\n".join(parts)

    @staticmethod
    def error_lessons(hits: list[Hit]) -> str:
        if not hits:
            return ""
        parts = ["PRIOR RECOVERIES - how a similar situation was handled before:"]
        for i, h in enumerate(hits, 1):
            p = h.payload
            tag = "OK" if p.get("status") != "error" else f"FAILED ({p.get('error_type')})"
            parts.append(f"\n[{i} | sim={h.score:.2f} | {tag}] code:\n{p.get('code', '')}")
        return "\n".join(parts)

    def save(self) -> None:
        self.store.save()

    def reset(self) -> None:
        self.store.clear()
