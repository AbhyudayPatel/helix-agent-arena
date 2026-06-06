"""Trajectory graph - the unit of observability in HELIX.

We do not log requests/tokens. We record *trajectories*: a typed graph of

    State -> Decision -> Action -> Outcome -> State -> ...

with side-edges for self-healing recoveries, world-model predictions, and the
memories that informed a decision. The graph is the source of truth that the
monitor reads in real time, the memory indexes, and the visualizer renders.

Node kinds:
    state       what the agent knows / env digest at step k
    decision    the agent's reasoning + chosen plan (+ predicted P(success))
    action      the python code executed against AppWorld
    outcome     the observation + status (ok/error/empty) + cost/latency
    prediction  a world-model simulated future branch (counterfactual)
    memory      a retrieved past trajectory that informed a decision

Edge relations:
    decides     state    -> decision
    acts        decision -> action
    yields      action   -> outcome
    transitions outcome   -> state
    recovers    outcome   -> decision   (self-heal: error -> revised plan)
    predicts    decision  -> prediction (world model lookahead)
    informs     memory    -> decision   (retrieval-augmented decision)
"""
from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .util import real_clock

# ---- visual styling per node status -------------------------------------- #
STATUS_COLOR = {
    "ok": "#bbf7d0",        # green
    "error": "#fecaca",     # red
    "empty": "#fde68a",     # amber
    "recovery": "#fdba74",  # orange
    "predicted": "#e9d5ff", # purple
    "neutral": "#e2e8f0",   # slate
    "start": "#bfdbfe",     # blue
    "final": "#a7f3d0",     # teal
}
KIND_SHAPE = {
    "state": "box",
    "decision": "ellipse",
    "action": "note",
    "outcome": "box",
    "prediction": "diamond",
    "memory": "cylinder",
}


@dataclass
class Node:
    id: str
    kind: str
    step: int
    label: str
    data: dict = field(default_factory=dict)
    status: str = "neutral"
    ts: float = 0.0


@dataclass
class Edge:
    src: str
    dst: str
    relation: str
    data: dict = field(default_factory=dict)


class Trajectory:
    """One task attempt, recorded as a graph."""

    def __init__(self, task_id: str, instruction: str, split: str = "",
                 experiment: str = "", supervisor: str = "",
                 allowed_apps: list[str] | None = None):
        self.task_id = task_id
        self.instruction = instruction
        self.split = split
        self.experiment = experiment
        self.supervisor = supervisor
        self.allowed_apps = allowed_apps or []
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self._counts: dict[str, int] = {}
        self.created_at = time.time()
        self.finished_at: float | None = None
        # AppWorld freezes time.time() via freezegun during a task, so durations
        # are measured with perf_counter (which is not frozen).
        self._perf_start = real_clock()
        self._wall_time: float | None = None
        # outcome bookkeeping
        self.evaluation: dict | None = None
        self.solved: bool | None = None
        self.usage: dict = {}
        self.last_state_id: str | None = None

    # -- node construction ------------------------------------------------- #
    def _new_id(self, kind: str) -> str:
        i = self._counts.get(kind, 0)
        self._counts[kind] = i + 1
        return f"{kind[0]}{i}"

    def _add(self, kind: str, label: str, *, step: int, status: str = "neutral",
             **data: Any) -> str:
        nid = self._new_id(kind)
        self.nodes.append(Node(nid, kind, step, label, dict(data), status, time.time()))
        return nid

    def add_state(self, label: str, step: int, *, status: str = "neutral",
                  **data: Any) -> str:
        nid = self._add("state", label, step=step, status=status, **data)
        if self.last_state_id is not None:
            # transitions edge is added when the previous outcome links forward;
            # here we just remember the latest state.
            pass
        self.last_state_id = nid
        return nid

    def add_decision(self, label: str, step: int, **data: Any) -> str:
        return self._add("decision", label, step=step, status="neutral", **data)

    def add_action(self, code: str, step: int, *, label: str | None = None,
                   **data: Any) -> str:
        return self._add("action", label or _first_line(code), step=step,
                          status="neutral", code=code, **data)

    def add_outcome(self, label: str, step: int, *, status: str = "ok",
                    **data: Any) -> str:
        return self._add("outcome", label, step=step, status=status, **data)

    def add_prediction(self, label: str, step: int, **data: Any) -> str:
        return self._add("prediction", label, step=step, status="predicted", **data)

    def add_memory(self, label: str, step: int, **data: Any) -> str:
        return self._add("memory", label, step=step, status="neutral", **data)

    def link(self, src: str, dst: str, relation: str, **data: Any) -> None:
        self.edges.append(Edge(src, dst, relation, dict(data)))

    # -- analysis ---------------------------------------------------------- #
    def node(self, nid: str) -> Node | None:
        for n in self.nodes:
            if n.id == nid:
                return n
        return None

    def nodes_of(self, kind: str) -> list[Node]:
        return [n for n in self.nodes if n.kind == kind]

    @property
    def num_steps(self) -> int:
        return len(self.nodes_of("action"))

    @property
    def num_errors(self) -> int:
        return len([n for n in self.nodes_of("outcome") if n.status == "error"])

    @property
    def num_recoveries(self) -> int:
        return len([e for e in self.edges if e.relation == "recovers"])

    @property
    def total_cost(self) -> float:
        return round(sum(n.data.get("cost_usd", 0.0) for n in self.nodes), 4)

    @property
    def total_latency(self) -> float:
        return round(sum(n.data.get("latency_s", 0.0) for n in self.nodes_of("outcome")), 2)

    @property
    def wall_time(self) -> float:
        if self._wall_time is not None:
            return self._wall_time
        return round(real_clock() - self._perf_start, 2)

    def world_model_accuracy(self) -> float | None:
        """Mean |predicted - actual| accuracy over decisions that carried a
        world-model prediction. actual=1 if the resulting outcome made progress."""
        preds = [n for n in self.nodes_of("decision") if "predicted_success" in n.data
                 and "actual_success" in n.data]
        if not preds:
            return None
        correct = 0
        for n in preds:
            p = n.data["predicted_success"] >= 0.5
            a = bool(n.data["actual_success"])
            correct += int(p == a)
        return round(correct / len(preds), 3)

    def recovery_rate(self) -> float | None:
        """Fraction of error outcomes that were followed by a recovery that
        eventually produced a non-error outcome."""
        errs = [n for n in self.nodes_of("outcome") if n.status == "error"]
        if not errs:
            return None
        recovered_sources = {e.src for e in self.edges if e.relation == "recovers"}
        return round(len([n for n in errs if n.id in recovered_sources]) / len(errs), 3)

    # -- finalize ---------------------------------------------------------- #
    def finalize(self, evaluation: dict | None, usage: dict | None = None,
                 solved: bool | None = None) -> None:
        self.finished_at = time.time()
        self._wall_time = round(real_clock() - self._perf_start, 2)
        self.evaluation = evaluation
        self.usage = usage or {}
        if solved is None and evaluation is not None:
            solved = bool(evaluation.get("success"))
        self.solved = solved
        if self.nodes:
            final = self.nodes[-1]
            if final.kind == "state":
                final.status = "final" if solved else final.status

    def summary(self) -> dict:
        return {
            "task_id": self.task_id,
            "split": self.split,
            "instruction": self.instruction,
            "solved": self.solved,
            "num_steps": self.num_steps,
            "num_errors": self.num_errors,
            "num_recoveries": self.num_recoveries,
            "recovery_rate": self.recovery_rate(),
            "world_model_accuracy": self.world_model_accuracy(),
            "total_cost_usd": self.total_cost,
            "total_latency_s": self.total_latency,
            "wall_time_s": self.wall_time,
            "evaluation": self.evaluation,
        }

    def compact_graph(self) -> dict:
        """Lightweight node/edge view for storing the graph itself (e.g. in HydraDB)."""
        return {
            "nodes": [{"id": n.id, "kind": n.kind, "step": n.step,
                       "status": n.status, "label": n.label} for n in self.nodes],
            "edges": [{"src": e.src, "dst": e.dst, "rel": e.relation} for e in self.edges],
        }

    # -- (de)serialization ------------------------------------------------- #
    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "instruction": self.instruction,
            "split": self.split,
            "experiment": self.experiment,
            "supervisor": self.supervisor,
            "allowed_apps": self.allowed_apps,
            "created_at": self.created_at,
            "finished_at": self.finished_at,
            "evaluation": self.evaluation,
            "solved": self.solved,
            "usage": self.usage,
            "summary": self.summary(),
            "nodes": [asdict(n) for n in self.nodes],
            "edges": [asdict(e) for e in self.edges],
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Trajectory":
        t = cls(d["task_id"], d["instruction"], d.get("split", ""),
                d.get("experiment", ""), d.get("supervisor", ""),
                d.get("allowed_apps", []))
        t.created_at = d.get("created_at", t.created_at)
        t.finished_at = d.get("finished_at")
        t.evaluation = d.get("evaluation")
        t.solved = d.get("solved")
        t.usage = d.get("usage", {})
        t.nodes = [Node(**n) for n in d.get("nodes", [])]
        t.edges = [Edge(**e) for e in d.get("edges", [])]
        t._wall_time = d.get("summary", {}).get("wall_time_s")
        return t

    def save(self, directory: str | Path) -> Path:
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{self.task_id}.trajectory.json"
        path.write_text(json.dumps(self.to_dict(), indent=2, default=str), encoding="utf-8")
        return path

    @classmethod
    def load(cls, path: str | Path) -> "Trajectory":
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))


def _first_line(text: str, n: int = 60) -> str:
    line = text.strip().splitlines()[0] if text.strip() else ""
    return (line[:n] + "...") if len(line) > n else line
