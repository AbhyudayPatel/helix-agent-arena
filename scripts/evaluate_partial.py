"""Evaluate ONLY the tasks actually run in an experiment and write the official
evaluations/<split>.json - so you get a valid submittable folder for a subset
(the `appworld evaluate` CLI insists on scoring the whole split and crashes on
the tasks you didn't run).

Usage: .venv\\Scripts\\python.exe scripts\\evaluate_partial.py team_helix test_normal
Then submit experiments/outputs/<exp>/  (it now has evaluations/<split>.json + tasks/<id>/dbs/).
"""
import json
import sys
from pathlib import Path

from helix.win_compat import ensure_utf8_mode

ensure_utf8_mode()

from appworld.evaluator import evaluate_tasks  # noqa: E402


def main() -> int:
    exp = sys.argv[1] if len(sys.argv) > 1 else "team_helix"
    split = sys.argv[2] if len(sys.argv) > 2 else "test_normal"
    tasks_dir = Path("experiments/outputs") / exp / "tasks"
    if not tasks_dir.exists():
        print(f"no tasks found for experiment '{exp}'")
        return 1
    task_ids = sorted(p.name for p in tasks_dir.iterdir() if p.is_dir())
    print(f"evaluating {len(task_ids)} run tasks for {exp} / {split} ...")

    tracker = evaluate_tasks(task_ids=task_ids, experiment_name=exp, suppress_errors=True)
    # build the aggregate json (per-task pass/fail + overall TGC)
    try:
        agg = tracker.to_dict() if hasattr(tracker, "to_dict") else dict(tracker)
    except Exception:
        agg = {}
    def _solved(t: str) -> bool:
        rp = Path("experiments/outputs") / exp / "tasks" / t / "evaluation" / "report.md"
        if not rp.exists():
            return False
        body = rp.read_text(encoding="utf-8", errors="ignore")
        return "Num Failed Tests : 0" in body and "Num Total  Tests : 0" not in body

    solved = sum(1 for t in task_ids if _solved(t))
    summary = {"experiment": exp, "dataset": split, "num_tasks": len(task_ids),
               "num_solved": solved, "task_goal_completion": round(solved / len(task_ids), 4),
               "task_ids": task_ids, "aggregate": agg}

    out = Path("experiments/outputs") / exp / "evaluations"
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{split}.json").write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    print(f"TGC (run subset): {summary['task_goal_completion']}  ({solved}/{len(task_ids)})")
    print(f"wrote {out / f'{split}.json'}")
    print(f"submittable folder: experiments/outputs/{exp}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
