"""Probe the live HydraDB API to confirm tenant/insert/search behavior.

Run: $env:HYDRADB_API_KEY="..."; .venv\\Scripts\\python.exe scripts\\hydra_probe.py
(The key is read from env and never written to disk.)
"""
import os
import time

try:
    from hydra_db import HydraDB, RawEmbeddingDocument, RawEmbeddingVector
except Exception:
    from hydra_db import HydraDB
    from hydra_db.types.raw_embedding_document import RawEmbeddingDocument
    from hydra_db.types.raw_embedding_vector import RawEmbeddingVector

from helix.llm import Embedder

TENANT = "helix"
SUB = "trajectories"
DIM = 1536


def main():
    key = os.environ.get("HYDRADB_API_KEY")
    assert key, "set HYDRADB_API_KEY"
    c = HydraDB(token=key)

    try:
        r = c.tenant.create(tenant_id=TENANT, is_embeddings_tenant=True, embeddings_dimension=DIM)
        print("tenant.create ->", r)
    except Exception as e:  # noqa: BLE001
        print("tenant.create err:", repr(e)[:300])

    # wait briefly for provisioning, polling infra if available
    for _ in range(10):
        try:
            st = c.tenant.infra_status(tenant_id=TENANT)
            print("infra_status ->", st)
            break
        except Exception as e:  # noqa: BLE001
            print("infra_status err:", repr(e)[:160]); time.sleep(3)

    emb = Embedder()
    texts = {
        "probe_task_1": "most liked song in my spotify playlists",
        "probe_task_2": "least played song in my spotify library",
        "probe_task_3": "send a venmo payment to a friend",
    }
    docs = []
    for sid, txt in texts.items():
        v = [float(x) for x in emb.embed(txt)]
        docs.append(RawEmbeddingDocument(
            source_id=sid,
            metadata={"type": "task", "instruction": txt, "solved": True},
            embeddings=[RawEmbeddingVector(chunk_id=sid, embedding=v)],
        ))

    for attempt in range(6):
        try:
            ins = c.embeddings.insert(tenant_id=TENANT, sub_tenant_id=SUB, embeddings=docs, upsert=True)
            print("insert ->", ins)
            break
        except Exception as e:  # noqa: BLE001
            print(f"insert err (attempt {attempt}):", repr(e)[:300]); time.sleep(4)

    q = [float(x) for x in emb.embed("what is the top liked track in my spotify playlists")]
    try:
        res = c.embeddings.search(tenant_id=TENANT, sub_tenant_id=SUB, query_embedding=q, limit=3)
        print("search ->", len(res), "hits")
        for h in res:
            print("  ", h.source_id, "score=", h.score, "meta=", h.metadata)
    except Exception as e:  # noqa: BLE001
        print("search err:", repr(e)[:400])


if __name__ == "__main__":
    main()
