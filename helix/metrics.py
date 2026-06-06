"""Trajectory Intelligence Benchmark.

We do not only report the AppWorld score. We benchmark the *intelligence* of the
trajectory layer:

  * task_goal_completion  - fraction of tasks fully solved (the AppWorld score)
  * recovery_rate         - of failed steps, how many were healed back to progress
  * planning_efficiency    - useful (non-error) actions / total actions
  * world_model_accuracy   - did predicted P(success) match the realized outcome
  * knowledge_reuse_rate   - fraction of tasks where recalled trajectories informed
                             the agent, and the solve-rate among those
"""
from __future__ import annotations

from .trajectory import Trajectory


def _safe_div(a, b):
    return round(a / b, 4) if b else None


def aggregate(trajs: list[Trajectory]) -> dict:
    n = len(trajs)
    if n == 0:
        return {"num_tasks": 0}

    solved = sum(1 for t in trajs if t.solved)
    total_steps = sum(t.num_steps for t in trajs)
    total_errors = sum(t.num_errors for t in trajs)

    # recovery: error outcomes that have a `recovers` edge originating from them
    recovered, error_outcomes = 0, 0
    for t in trajs:
        recover_srcs = {e.src for e in t.edges if e.relation == "recovers"}
        for o in t.nodes_of("outcome"):
            if o.status == "error":
                error_outcomes += 1
                if o.id in recover_srcs:
                    recovered += 1

    # world-model accuracy across all predicting decisions
    wm_correct, wm_n, brier = 0, 0, 0.0
    for t in trajs:
        for d in t.nodes_of("decision"):
            if "predicted_success" in d.data and "actual_success" in d.data:
                p = float(d.data["predicted_success"])
                a = int(d.data["actual_success"])
                wm_correct += int((p >= 0.5) == bool(a))
                brier += (p - a) ** 2
                wm_n += 1

    # knowledge reuse: tasks where a memory node informed a decision
    informed = [t for t in trajs if any(e.relation == "informs" for e in t.edges)]
    informed_solved = sum(1 for t in informed if t.solved)

    by_diff: dict = {}
    for t in trajs:
        d = (t.evaluation or {}).get("difficulty", "?")
        by_diff.setdefault(d, {"n": 0, "solved": 0})
        by_diff[d]["n"] += 1
        by_diff[d]["solved"] += int(bool(t.solved))
    for d in by_diff.values():
        d["tgc"] = _safe_div(d["solved"], d["n"])

    return {
        "num_tasks": n,
        "solved": solved,
        "task_goal_completion": _safe_div(solved, n),
        "avg_steps": _safe_div(total_steps, n),
        "avg_errors": _safe_div(total_errors, n),
        "error_rate": _safe_div(total_errors, total_steps),
        "planning_efficiency": _safe_div(total_steps - total_errors, total_steps),
        "total_errors": total_errors,
        "recovered_errors": recovered,
        "recovery_rate": _safe_div(recovered, error_outcomes),
        "world_model_accuracy": _safe_div(wm_correct, wm_n),
        "world_model_brier": round(brier / wm_n, 4) if wm_n else None,
        "world_model_n": wm_n,
        "knowledge_reuse_rate": _safe_div(len(informed), n),
        "memory_assisted_solve_rate": _safe_div(informed_solved, len(informed)),
        "total_cost_usd": round(sum(t.total_cost for t in trajs), 4),
        "avg_cost_usd": _safe_div(sum(t.total_cost for t in trajs), n),
        "avg_wall_time_s": _safe_div(sum(t.wall_time for t in trajs), n),
        "by_difficulty": by_diff,
    }


def format_report(metrics: dict) -> str:
    if metrics.get("num_tasks", 0) == 0:
        return "No tasks."
    m = metrics
    lines = [
        "=" * 56,
        " TRAJECTORY INTELLIGENCE BENCHMARK",
        "=" * 56,
        f" Tasks                 : {m['num_tasks']}",
        f" Task Goal Completion  : {m['task_goal_completion']}  ({m['solved']}/{m['num_tasks']})",
        f" Avg steps / task      : {m['avg_steps']}",
        f" Planning efficiency   : {m['planning_efficiency']}  (non-error actions)",
        f" Errors (rate)         : {m['total_errors']} ({m['error_rate']})",
        f" Recovery rate         : {m['recovery_rate']}  ({m['recovered_errors']}/{m['total_errors']} healed)",
        f" World-model accuracy  : {m['world_model_accuracy']}  (Brier {m['world_model_brier']}, n={m['world_model_n']})",
        f" Knowledge reuse rate  : {m['knowledge_reuse_rate']}",
        f" Mem-assisted solve    : {m['memory_assisted_solve_rate']}",
        f" Cost (avg / total)    : ${m['avg_cost_usd']} / ${m['total_cost_usd']}",
        f" Avg wall time / task  : {m['avg_wall_time_s']}s",
        "=" * 56,
    ]
    return "\n".join(lines)
