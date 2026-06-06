"""HELIX benchmark runner.

Runs the trajectory-intelligence agent over AppWorld tasks, records + visualizes
every trajectory, indexes them into memory for reuse, and emits the Trajectory
Intelligence Benchmark + an HTML dashboard.

Examples:
  # smoke: 3 dev tasks, full stack, Opus
  python -m helix.run --split dev --limit 3
  # seed memory on train, then evaluate dev (knowledge reuse kicks in)
  python -m helix.run --split train --limit 20
  python -m helix.run --split dev --limit 20
  # ablation: plain ReAct
  python -m helix.run --split dev --limit 10 --no-memory --no-world-model --no-healing
"""
from __future__ import annotations

import argparse
import json
import os

from .win_compat import ensure_utf8_mode

ensure_utf8_mode()

from .agent import HelixAgent                                     # noqa: E402
from .appworld_env import AppWorldEnvironment, list_task_ids      # noqa: E402
from .config import CONFIG, REPORTS_DIR, TRAJECTORY_DIR           # noqa: E402
from .healing import SelfHealer                                   # noqa: E402
from .llm import GLOBAL_USAGE                                     # noqa: E402
from .memory.retrieval import TrajectoryMemory                    # noqa: E402
from .metrics import aggregate, format_report                     # noqa: E402
from .report import build_dashboard                               # noqa: E402
from .trajectory import Trajectory                                # noqa: E402
from .viz import visualize                                        # noqa: E402
from .world_model import WorldModel                               # noqa: E402


def parse_args():
    p = argparse.ArgumentParser(description="HELIX AppWorld runner")
    p.add_argument("--split", default="dev",
                   choices=["train", "dev", "test_normal", "test_challenge"])
    p.add_argument("--limit", type=int, default=3)
    p.add_argument("--tasks", default="", help="comma-separated task ids (overrides split sampling)")
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--experiment", default="helix")
    p.add_argument("--model", default=os.environ.get("HELIX_AGENT_MODEL", "claude-opus-4-8"))
    p.add_argument("--max-steps", type=int, default=CONFIG.max_steps)
    p.add_argument("--no-memory", action="store_true")
    p.add_argument("--no-world-model", action="store_true")
    p.add_argument("--no-healing", action="store_true")
    p.add_argument("--no-bootstrap", action="store_true")
    p.add_argument("--no-viz", action="store_true")
    p.add_argument("--reset-memory", action="store_true")
    p.add_argument("--read-only-memory", action="store_true",
                   help="recall from memory but do NOT index new trajectories "
                        "(leaderboard-valid: no ground-truth leakage on test splits)")
    p.add_argument("--quiet", action="store_true")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if args.tasks:
        task_ids = [t.strip() for t in args.tasks.split(",") if t.strip()]
    else:
        ids = list_task_ids(args.split)
        task_ids = ids[args.offset: args.offset + args.limit]

    memory = None if args.no_memory else TrajectoryMemory()
    if memory is not None and args.reset_memory:
        memory.reset()
    world_model = None if args.no_world_model else WorldModel(memory=memory)
    healer = None if args.no_healing else SelfHealer(memory=memory, world_model=world_model)

    config_note = (f"model={args.model} | memory={memory is not None}"
                   f"({memory.backend if memory else '-'}) | "
                   f"world_model={world_model is not None} | healing={healer is not None} | "
                   f"bootstrap={not args.no_bootstrap}")
    print(config_note)
    if memory is not None:
        print(f"[memory] backend={memory.backend} starting size={len(memory)}")

    env = AppWorldEnvironment(args.experiment)
    trajs: list[Trajectory] = []
    graphs_dir = REPORTS_DIR / args.experiment / "graphs"

    for i, tid in enumerate(task_ids, 1):
        print(f"\n===== [{i}/{len(task_ids)}] task {tid} =====")
        agent = HelixAgent(env, memory=memory, world_model=world_model, healer=healer,
                           model=args.model, max_steps=args.max_steps,
                           verbose=not args.quiet, bootstrap=not args.no_bootstrap)
        try:
            traj = agent.run_task(tid, split=args.split, experiment=args.experiment)
        except Exception as e:  # noqa: BLE001 - never let one task kill the run
            print(f"[run] task {tid} crashed: {e}")
            continue
        try:  # saving is for the dashboard only - never let it block a run
            traj.save(TRAJECTORY_DIR)
            traj.save(REPORTS_DIR / args.experiment / "trajectories")
        except Exception as e:  # noqa: BLE001
            print(f"[run] trajectory save failed (non-fatal): {e}")
        if memory is not None and not args.read_only_memory:
            try:
                memory.index_trajectory(traj)
            except Exception as e:  # noqa: BLE001
                print(f"[memory] index failed: {e}")
        if not args.no_viz:
            try:
                visualize(traj, graphs_dir)
            except Exception as e:  # noqa: BLE001
                print(f"[viz] failed: {e}")
        trajs.append(traj)

    env.close()

    metrics = aggregate(trajs)
    print("\n" + format_report(metrics))
    print("usage:", GLOBAL_USAGE.snapshot())

    index = build_dashboard(trajs, REPORTS_DIR / args.experiment,
                            experiment=args.experiment, config_note=config_note)
    print("dashboard:", index)
    (REPORTS_DIR / args.experiment / "summaries.json").write_text(
        json.dumps([t.summary() for t in trajs], indent=2, default=str), encoding="utf-8")
    try:
        import datetime as _dt
        (REPORTS_DIR / args.experiment / "run_meta.json").write_text(json.dumps({
            "experiment": args.experiment, "config_note": config_note, "model": args.model,
            "split": args.split, "num_tasks": len(trajs),
            "logged_at": _dt.datetime.now().isoformat(timespec="seconds"), "metrics": metrics,
        }, indent=2, default=str), encoding="utf-8")
    except Exception as e:  # noqa: BLE001 - dashboard metadata is best-effort
        print(f"[run] run_meta save failed (non-fatal): {e}")

    # auto-emit per-experiment insights + append-only cross-run history
    try:
        from .insights import analyze, build_run_log, write_insights_md
        write_insights_md(analyze(trajs), REPORTS_DIR / args.experiment / "INSIGHTS.md")
        build_run_log(REPORTS_DIR)
    except Exception as e:  # noqa: BLE001
        print("[insights] skipped:", e)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
