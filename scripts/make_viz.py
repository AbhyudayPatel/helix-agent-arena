"""Render a saved trajectory to .dot / .svg / interactive .html.

Usage: .venv\\Scripts\\python.exe scripts\\make_viz.py [trajectory.json]
"""
import json
import sys
from pathlib import Path

from helix.win_compat import ensure_utf8_mode

ensure_utf8_mode()

from helix.config import REPORTS_DIR       # noqa: E402
from helix.trajectory import Trajectory     # noqa: E402
from helix.viz import visualize             # noqa: E402


def main() -> int:
    p = (sys.argv[1] if len(sys.argv) > 1
         else "helix_store/trajectories/82e2fac_1.trajectory.json")
    traj = Trajectory.load(p)
    out = visualize(traj, Path(REPORTS_DIR) / "graphs")
    print(json.dumps(out, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
