"""://agent_arena submission agent — powered by HELIX.

Drop-in replacement for the starter ReAct agent. Same harness contract
(`with AppWorld(...) as world: solve(world)`), but the brain is HELIX: a
trajectory-graph agent with a grounded bootstrap, subgoal decomposition,
world-model planning, a live monitor, self-healing with repair-memory, a
verification gate, and (optional) HydraDB-backed trajectory memory.

Run (env vars match the official starter):
  export APPWORLD_EXPERIMENT=team_<yourname>
  export APPWORLD_DATASET=dev            # dev | test_normal | test_challenge
  export MAX_TASKS=2                      # 0 = all
  export MODEL=claude-opus-4-8           # or claude-sonnet-4-6
  python agent.py
Then: appworld evaluate $APPWORLD_EXPERIMENT $APPWORLD_DATASET

Note on validity: on the test splits HELIX runs memory in RECALL-ONLY mode
(solve() never indexes), so it never learns from the answer key -> no leakage.
Seed memory from the TRAIN split beforehand to get the (valid) reuse benefit.
"""
import os
import sys

# make the HELIX package importable when running this file from the repo subdir
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

from helix.win_compat import ensure_utf8_mode

ensure_utf8_mode()

from appworld import AppWorld, load_task_ids                       # noqa: E402
from helix.agent import HelixAgent                                 # noqa: E402
from helix.appworld_env import AppWorldEnvironment                 # noqa: E402
from helix.llm import GLOBAL_USAGE                                 # noqa: E402

DATASET = os.environ.get("APPWORLD_DATASET", "dev")
EXPERIMENT = os.environ.get("APPWORLD_EXPERIMENT", "team_helix")
MODEL = os.environ.get("MODEL", "claude-opus-4-8")
MAX_TASKS = int(os.environ.get("MAX_TASKS", "0"))                  # 0 = all
MAX_STEPS = int(os.environ.get("MAX_INTERACTIONS", "40"))
USE_MEMORY = os.environ.get("HELIX_MEMORY", "1") == "1"
USE_WM = os.environ.get("HELIX_WORLD_MODEL", "1") == "1"
USE_HEAL = os.environ.get("HELIX_HEALING", "1") == "1"

# Windows can't use AppWorld's SIGALRM timeout; disable it there only.
TIMEOUT = None if sys.platform.startswith("win") else int(os.environ.get("APPWORLD_TIMEOUT", "100"))


def build_agent(env):
    memory = world_model = healer = None
    if USE_MEMORY:
        from helix.memory.retrieval import TrajectoryMemory
        memory = TrajectoryMemory()
        print(f"[helix] memory backend = {memory.backend} (recall-only on test = leakage-free)")
    if USE_WM:
        from helix.world_model import WorldModel
        world_model = WorldModel(memory=memory)
    if USE_HEAL:
        from helix.healing import SelfHealer
        healer = SelfHealer(memory=memory, world_model=world_model)
    return HelixAgent(env, memory=memory, world_model=world_model, healer=healer,
                      model=MODEL, max_steps=MAX_STEPS, verbose=True)


def main() -> None:
    task_ids = load_task_ids(DATASET)
    if MAX_TASKS:
        task_ids = task_ids[:MAX_TASKS]
    env = AppWorldEnvironment(EXPERIMENT)
    agent = build_agent(env)
    print(f"[helix] running '{EXPERIMENT}' on {len(task_ids)} '{DATASET}' tasks with {MODEL}")

    solved = 0
    for i, task_id in enumerate(task_ids, 1):
        print(f"\n[{i}/{len(task_ids)}] {task_id}")
        try:
            with AppWorld(task_id=task_id, experiment_name=EXPERIMENT,
                          timeout_seconds=TIMEOUT) as world:
                traj = agent.solve(world, split=DATASET, experiment=EXPERIMENT)
                solved += int(bool(traj.solved))
        except Exception as e:  # never let one task kill the run
            print(f"  ! error on {task_id}: {e}")

    print(f"\n[helix] done. solved {solved}/{len(task_ids)} (self-reported). "
          f"usage: {GLOBAL_USAGE.snapshot()}")
    print(f"[helix] outputs in ./experiments/outputs/{EXPERIMENT}/")
    print(f"[helix] now run:  appworld evaluate {EXPERIMENT} {DATASET}")


if __name__ == "__main__":
    main()
