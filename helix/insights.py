"""Cross-run analysis & logging - turns the recorded trajectories into insights.

Reads every saved trajectory + experiment summary and produces:
  * an aggregate analysis (TGC, failure patterns, per-template performance,
    world-model calibration, knowledge-reuse effectiveness, cost/step/latency),
  * reports/INSIGHTS.md (human-readable),
  * reports/run_log.jsonl (append-only history of runs).

Pure analysis over JSON files - imports no AppWorld, safe to run anytime.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from .config import REPORTS_DIR, TRAJECTORY_DIR
from .trajectory import Trajectory


def load_all_trajectories(dirpath: Path | str = TRAJECTORY_DIR) -> list[Trajectory]:
    out = []
    for p in sorted(Path(dirpath).glob("*.trajectory.json")):
        try:
            out.append(Trajectory.load(p))
        except Exception:
            pass
    return out


def _pct(a, b):
    return round(100 * a / b, 1) if b else None


def analyze(trajs: list[Trajectory]) -> dict:
    n = len(trajs)
    if n == 0:
        return {"num_trajectories": 0}
    solved = [t for t in trajs if t.solved]

    fail_errors = Counter()
    for t in trajs:
        if not t.solved:
            for o in t.nodes_of("outcome"):
                if o.status == "error" and o.data.get("error_type"):
                    fail_errors[o.data["error_type"]] += 1

    per_template: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for t in trajs:
        pre = t.task_id.rsplit("_", 1)[0]
        per_template[pre][0] += 1
        per_template[pre][1] += int(bool(t.solved))

    wm_pairs = []
    for t in trajs:
        for d in t.nodes_of("decision"):
            if "predicted_success" in d.data and "actual_success" in d.data:
                wm_pairs.append((float(d.data["predicted_success"]), int(d.data["actual_success"])))
    wm_acc = (_pct(sum(int((p >= 0.5) == bool(a)) for p, a in wm_pairs), len(wm_pairs))
              if wm_pairs else None)
    wm_brier = (round(sum((p - a) ** 2 for p, a in wm_pairs) / len(wm_pairs), 4)
                if wm_pairs else None)
    cal = {"low(<0.5)": [0, 0], "high(>=0.5)": [0, 0]}
    for p, a in wm_pairs:
        k = "high(>=0.5)" if p >= 0.5 else "low(<0.5)"
        cal[k][0] += 1
        cal[k][1] += a
    calibration = {k: {"n": v[0], "actual_solve_rate": _pct(v[1], v[0])} for k, v in cal.items()}

    informed = [t for t in trajs if any(e.relation == "informs" for e in t.edges)]
    non_informed = [t for t in trajs if t not in informed]

    err_outcomes = sum(len([o for o in t.nodes_of("outcome") if o.status == "error"]) for t in trajs)
    recovered = 0
    for t in trajs:
        srcs = {e.src for e in t.edges if e.relation == "recovers"}
        recovered += len([o for o in t.nodes_of("outcome") if o.status == "error" and o.id in srcs])

    costly = sorted(trajs, key=lambda t: t.total_cost, reverse=True)[:5]
    slowest = sorted(trajs, key=lambda t: t.wall_time, reverse=True)[:5]

    return {
        "num_trajectories": n,
        "solved": len(solved),
        "task_goal_completion_pct": _pct(len(solved), n),
        "failure_error_types": dict(fail_errors.most_common()),
        "per_template": {k: {"n": v[0], "solved": v[1], "tgc_pct": _pct(v[1], v[0])}
                         for k, v in sorted(per_template.items())},
        "world_model": {"n": len(wm_pairs), "accuracy_pct": wm_acc, "brier": wm_brier,
                        "calibration": calibration},
        "knowledge_reuse": {
            "tasks_informed": len(informed),
            "solve_rate_with_memory_pct": _pct(sum(t.solved for t in informed), len(informed)),
            "solve_rate_without_memory_pct": _pct(sum(t.solved for t in non_informed), len(non_informed)),
        },
        "recovery": {"error_outcomes": err_outcomes, "recovered": recovered,
                     "recovery_rate_pct": _pct(recovered, err_outcomes)},
        "avg_steps": round(sum(t.num_steps for t in trajs) / n, 2),
        "avg_cost_usd": round(sum(t.total_cost for t in trajs) / n, 4),
        "total_cost_usd": round(sum(t.total_cost for t in trajs), 4),
        "avg_wall_s": round(sum(t.wall_time for t in trajs) / n, 2),
        "most_expensive": [{"task": t.task_id, "cost": t.total_cost, "solved": t.solved} for t in costly],
        "slowest": [{"task": t.task_id, "wall_s": t.wall_time, "steps": t.num_steps} for t in slowest],
    }


def write_insights_md(analysis: dict, path: Path | str) -> Path:
    path = Path(path)
    if analysis.get("num_trajectories", 0) == 0:
        path.write_text("# HELIX Insights\n\nNo trajectories found yet.\n", encoding="utf-8")
        return path
    a = analysis
    lines = [
        "# HELIX — Insights (auto-generated)",
        f"_generated {datetime.now().isoformat(timespec='seconds')} over "
        f"{a['num_trajectories']} trajectories_\n",
        f"- **Task Goal Completion**: {a['task_goal_completion_pct']}% ({a['solved']}/{a['num_trajectories']})",
        f"- **Avg steps**: {a['avg_steps']} | **avg cost**: ${a['avg_cost_usd']} | "
        f"**avg wall**: {a['avg_wall_s']}s | **total cost**: ${a['total_cost_usd']}",
        f"- **Recovery rate**: {a['recovery']['recovery_rate_pct']}% "
        f"({a['recovery']['recovered']}/{a['recovery']['error_outcomes']} error-steps healed)",
        f"- **World-model**: accuracy {a['world_model']['accuracy_pct']}% "
        f"(Brier {a['world_model']['brier']}, n={a['world_model']['n']})",
        "",
        "## Knowledge reuse (memory)",
        f"- tasks informed by recalled trajectories: {a['knowledge_reuse']['tasks_informed']}",
        f"- solve-rate WITH memory: {a['knowledge_reuse']['solve_rate_with_memory_pct']}% | "
        f"WITHOUT: {a['knowledge_reuse']['solve_rate_without_memory_pct']}%",
        "",
        "## World-model calibration",
    ]
    for k, v in a["world_model"]["calibration"].items():
        lines.append(f"- predicted {k}: n={v['n']}, actual solve-rate {v['actual_solve_rate']}%")
    lines.append("\n## Failure patterns (error types in failed tasks)")
    if a["failure_error_types"]:
        for k, v in a["failure_error_types"].items():
            lines.append(f"- `{k}` × {v}")
    else:
        lines.append("- none recorded")
    lines.append("\n## Per-template performance")
    for k, v in a["per_template"].items():
        lines.append(f"- `{k}`: {v['tgc_pct']}% ({v['solved']}/{v['n']})")
    lines.append("\n## Most expensive tasks")
    for r in a["most_expensive"]:
        lines.append(f"- {r['task']}: ${r['cost']} (solved={r['solved']})")
    lines.append("\n## Slowest tasks")
    for r in a["slowest"]:
        lines.append(f"- {r['task']}: {r['wall_s']}s, {r['steps']} steps")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def build_run_log(reports_dir: Path | str = REPORTS_DIR) -> Path:
    """Consolidate every experiment's metrics.json into an append-only history."""
    reports_dir = Path(reports_dir)
    log_path = reports_dir / "run_log.jsonl"
    rows = []
    for metrics_file in sorted(reports_dir.glob("*/metrics.json")):
        try:
            m = json.loads(metrics_file.read_text(encoding="utf-8"))
        except Exception:
            continue
        rows.append({
            "experiment": metrics_file.parent.name,
            "logged_at": datetime.now().isoformat(timespec="seconds"),
            "metrics": m,
        })
    log_path.write_text("\n".join(json.dumps(r) for r in rows) + ("\n" if rows else ""),
                        encoding="utf-8")
    return log_path
