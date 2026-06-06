"""Run HelixAgent on a single AppWorld task (validation).

Usage:
  .venv\\Scripts\\python.exe scripts\\run_one.py [task_id] [--core]

--core runs plain ReAct (no memory/world-model/healing).
"""
import json
import sys

from helix.win_compat import ensure_utf8_mode

ensure_utf8_mode()

from helix.agent import HelixAgent                                  # noqa: E402
from helix.appworld_env import AppWorldEnvironment, list_task_ids   # noqa: E402
from helix.config import TRAJECTORY_DIR                             # noqa: E402
from helix.healing import SelfHealer                                # noqa: E402
from helix.llm import GLOBAL_USAGE                                  # noqa: E402
from helix.memory.retrieval import TrajectoryMemory                 # noqa: E402
from helix.world_model import WorldModel                            # noqa: E402


def main() -> int:
    args = [a for a in sys.argv[1:]]
    core = "--core" in args
    args = [a for a in args if not a.startswith("--")]
    task_id = args[0] if args else list_task_ids("train")[0]

    env = AppWorldEnvironment("helix_test")
    if core:
        agent = HelixAgent(env, max_steps=25, verbose=True)
        mem = None
    else:
        mem = TrajectoryMemory()
        wm = WorldModel(memory=mem)
        healer = SelfHealer(memory=mem, world_model=wm)
        agent = HelixAgent(env, memory=mem, world_model=wm, healer=healer,
                           max_steps=25, verbose=True)
        print(f"[memory] backend={mem.backend} size={len(mem)}")

    traj = agent.run_task(task_id, split="train", experiment="helix_test")
    env.close()

    if mem is not None:
        n = mem.index_trajectory(traj)
        print(f"[memory] indexed {n} records; store size now {len(mem)}")

    path = traj.save(TRAJECTORY_DIR)
    print("\n=== SUMMARY ===")
    print(json.dumps(traj.summary(), indent=2, default=str))
    print("\nusage:", GLOBAL_USAGE.snapshot())
    print("trajectory saved:", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
