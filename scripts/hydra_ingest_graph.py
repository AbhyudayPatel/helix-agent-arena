"""Feed all recorded trajectories into HydraDB's MANAGED knowledge-graph pipeline.

Unlike the raw-embedding (BYOE) path, this runs HydraDB's LLM entity/relation
extraction -> it shows up as token usage on the HydraDB dashboard and builds a
queryable knowledge graph of agent trajectories.

  $env:HYDRADB_API_KEY="..."; .venv\\Scripts\\python.exe scripts\\hydra_ingest_graph.py
"""
import sys

from helix.win_compat import ensure_utf8_mode

ensure_utf8_mode()

from helix.config import CONFIG                       # noqa: E402
from helix.insights import load_all_trajectories      # noqa: E402
from helix.memory.retrieval import TrajectoryMemory    # noqa: E402


def main() -> int:
    if not CONFIG.hydra_api_key:
        print("HYDRADB_API_KEY not set."); return 1
    mem = TrajectoryMemory()
    if mem.backend != "hydradb":
        print(f"backend is {mem.backend}, not hydradb."); return 1
    store = mem.store

    trajs = load_all_trajectories()
    print(f"Ingesting {len(trajs)} trajectories into HydraDB managed graph "
          f"(tenant={store.kg_tenant}, sub={store.sub})...")
    for i, t in enumerate(trajs, 1):
        approach = [(a.data.get("code", "") or "")[:200] for a in t.nodes_of("action")]
        text = TrajectoryMemory._knowledge_text(t, bool(t.solved), approach)
        store.ingest_knowledge(t.task_id, text, {
            "title": t.instruction[:80], "solved": bool(t.solved),
            "apps": ",".join(t.allowed_apps[:6]), "steps": t.num_steps,
            "recoveries": t.num_recoveries})
        if i % 10 == 0:
            print(f"  ...{i}/{len(trajs)} queued")
    print(f"\nQueued {store._kg_count} sources into HydraDB's graph pipeline.")
    print("HydraDB is now running entity/relation extraction on them -> check your")
    print("dashboard for TOKEN USAGE. Query the graph via store.graph_recall(query).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
