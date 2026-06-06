"""Deep HydraDB check: confirm our data is stored, and exercise the managed
(token-generating) graph pipeline. Key is read from env, never written to disk.

  $env:HYDRADB_API_KEY="..."; .venv\\Scripts\\python.exe scripts\\hydra_verify.py
"""
import json
import os
import time

from hydra_db import HydraDB

from helix.llm import Embedder

EMB_TENANT = "helix"        # BYOE embeddings tenant used by the benchmark
EMB_SUB = "final"           # the collection the big run wrote to
KG_TENANT = "helix_kg"      # managed graph/memory tenant (LLM pipeline -> token usage)
KG_SUB = "trajectories"


def main():
    key = os.environ.get("HYDRADB_API_KEY")
    assert key, "set HYDRADB_API_KEY"
    c = HydraDB(token=key)
    emb = Embedder()

    print("=== 1. BYOE search on tenant=helix sub=final (was the benchmark data persisted?) ===")
    q = [float(x) for x in emb.embed("most liked song in my spotify playlists")]
    try:
        res = c.embeddings.search(tenant_id=EMB_TENANT, sub_tenant_id=EMB_SUB,
                                  query_embedding=q, limit=5)
        print(f"  HITS: {len(res)}  (non-zero => HydraDB stored & served the benchmark trajectories)")
        for r in res:
            m = r.metadata or {}
            print("   -", r.source_id, "score=", round(r.score or 0, 3),
                  "type=", m.get("type"), "|", str(m.get("instruction", ""))[:55])
    except Exception as e:  # noqa: BLE001
        print("  BYOE search ERROR:", repr(e)[:300])

    print("\n  NOTE: BYOE (raw embeddings) uses OUR vectors, so HydraDB does no LLM work")
    print("  -> zero 'token usage' is EXPECTED for this path. Token usage comes from the")
    print("  managed graph pipeline below (upload.knowledge / recall.full_recall).")

    print("\n=== 2. Managed graph ingest (upload.knowledge -> entity/relation extraction) ===")
    try:
        c.tenant.create(tenant_id=KG_TENANT)
        time.sleep(1.5)
    except Exception as e:  # noqa: BLE001
        print("  tenant.create:", repr(e)[:160])
    source = {
        "id": "traj_demo_spotify_mostliked",
        "tenant_id": KG_TENANT,
        "sub_tenant_id": KG_SUB,
        "title": "Trajectory: most-liked Spotify song",
        "type": "agent_trajectory",
        "content": {"text": (
            "AppWorld task: find the title of the most-liked song in the user's Spotify "
            "playlists. Winning approach: get the spotify password from the supervisor, "
            "log in for an access_token, list all playlists, paginate every playlist's "
            "tracks, take the track with the maximum like_count, and answer with its title. "
            "Apps used: supervisor, api_docs, spotify. Outcome: solved.")},
        "tenant_metadata": {"app": "spotify", "solved": "true"},
    }
    try:
        up = c.upload.knowledge(tenant_id=KG_TENANT, sub_tenant_id=KG_SUB,
                                upsert=True, app_sources=json.dumps([source]))
        print("  upload.knowledge ->", str(up)[:400])
    except Exception as e:  # noqa: BLE001
        print("  upload.knowledge ERROR:", repr(e)[:400])

    print("\n=== 3. Managed recall (recall.full_recall, graph-aware -> token usage) ===")
    last = None
    for attempt in range(6):
        try:
            rr = c.recall.full_recall(tenant_id=KG_TENANT, sub_tenant_id=KG_SUB,
                                      query="how did we find the most liked spotify song",
                                      mode="fast", graph_context=True, max_results=3)
            print("  full_recall ->", str(rr)[:700])
            return
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(4)
    print("  full_recall ERROR:", repr(last)[:400])


if __name__ == "__main__":
    main()
