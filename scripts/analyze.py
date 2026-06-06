"""Generate cross-run insights + history from the recorded trajectories.

Writes:
  reports/INSIGHTS.md     - human-readable aggregate analysis
  reports/insights.json   - same analysis as JSON
  reports/run_log.jsonl   - append-only history of every experiment's metrics

Usage: .venv\\Scripts\\python.exe scripts\\analyze.py [trajectory_dir]
"""
import json
import sys
from pathlib import Path

from helix.win_compat import ensure_utf8_mode

ensure_utf8_mode()

from helix.config import REPORTS_DIR, TRAJECTORY_DIR          # noqa: E402
from helix.insights import (analyze, build_run_log,            # noqa: E402
                            load_all_trajectories, write_insights_md)


def main() -> int:
    src = sys.argv[1] if len(sys.argv) > 1 else TRAJECTORY_DIR
    trajs = load_all_trajectories(src)
    analysis = analyze(trajs)
    Path(REPORTS_DIR).mkdir(parents=True, exist_ok=True)
    (Path(REPORTS_DIR) / "insights.json").write_text(
        json.dumps(analysis, indent=2), encoding="utf-8")
    md = write_insights_md(analysis, Path(REPORTS_DIR) / "INSIGHTS.md")
    log = build_run_log(REPORTS_DIR)
    print(f"analyzed {analysis.get('num_trajectories', 0)} trajectories")
    print("wrote:", md)
    print("wrote:", log)
    print(json.dumps({k: analysis.get(k) for k in
                      ("task_goal_completion_pct", "solved", "num_trajectories",
                       "recovery", "world_model", "knowledge_reuse")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
