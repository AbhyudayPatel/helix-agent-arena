"""HydraDB backend for trajectory memory (live, via the hydra-db-python SDK).

HydraDB is a unified context substrate for stateful agents. A trajectory is a
graph whose nodes carry embeddings, so we store each trajectory record as a raw
embedding document (BYOE) whose metadata carries the payload AND, for task-level
records, the compact trajectory graph itself (nodes+edges) - so the graph lives
in HydraDB, not just the vectors.

Auth is by API key (token); no URL needed. Activate with HYDRADB_API_KEY.
Construction raises if the SDK/key is missing, so get_vector_store() falls back
to the local store automatically.
"""
from __future__ import annotations

import json
import time

from ..config import CONFIG
from .store import Hit, VectorStore


class HydraVectorStore(VectorStore):
    backend = "hydradb"

    def __init__(self, name: str | None = None):
        if not CONFIG.hydra_api_key:
            raise RuntimeError("HYDRADB_API_KEY not set")
        try:
            from hydra_db import HydraDB
        except Exception as e:  # noqa: BLE001
            raise ImportError(f"hydra-db-python not installed: {e}")
        try:
            from hydra_db import RawEmbeddingDocument, RawEmbeddingVector
        except Exception:  # auto-gen package sometimes only exposes via submodules
            from hydra_db.types.raw_embedding_document import RawEmbeddingDocument
            from hydra_db.types.raw_embedding_vector import RawEmbeddingVector
        self._Doc = RawEmbeddingDocument
        self._Vec = RawEmbeddingVector
        self.client = HydraDB(token=CONFIG.hydra_api_key)
        self.tenant = CONFIG.hydra_tenant
        self.sub = name or CONFIG.hydra_collection
        self._count = 0
        self._ensure_tenant()
        # managed knowledge-graph memory (separate, non-embeddings tenant)
        self.kg_tenant = CONFIG.hydra_kg_tenant
        self._kg_count = 0
        if CONFIG.hydra_kg:
            try:
                self.client.tenant.create(tenant_id=self.kg_tenant)
            except Exception:
                pass

    def _ensure_tenant(self) -> None:
        try:
            self.client.tenant.create(tenant_id=self.tenant, is_embeddings_tenant=True,
                                      embeddings_dimension=CONFIG.embedding_dim)
            time.sleep(1.0)  # brief grace for background provisioning
        except Exception:
            pass  # already exists / accepted

    def add(self, id: str, vector, payload: dict) -> None:
        self.add_many([(id, vector, payload)])

    def add_many(self, items) -> None:
        docs = []
        for id_, vec, payload in items:
            v = [float(x) for x in vec]
            docs.append(self._Doc(source_id=str(id_), metadata=payload,
                                  embeddings=[self._Vec(chunk_id=str(id_), embedding=v)]))
        if not docs:
            return
        last = None
        for attempt in range(5):
            try:
                self.client.embeddings.insert(tenant_id=self.tenant, sub_tenant_id=self.sub,
                                              embeddings=docs, upsert=True)
                self._count += len(docs)
                return
            except Exception as e:  # noqa: BLE001 - tenant may still be provisioning
                last = e
                time.sleep(3.0)
        print(f"[hydradb] insert failed after retries: {repr(last)[:200]}")

    def search(self, vector, k: int = 5, where: dict | None = None) -> list[Hit]:
        v = [float(x) for x in vector]
        try:
            res = self.client.embeddings.search(tenant_id=self.tenant, sub_tenant_id=self.sub,
                                                query_embedding=v, limit=max(k * 6, k))
        except Exception as e:  # noqa: BLE001
            print(f"[hydradb] search failed: {repr(e)[:200]}")
            return []
        hits: list[Hit] = []
        for r in res:
            payload = getattr(r, "metadata", None) or {}
            if where and not all(payload.get(kk) == vv for kk, vv in where.items()):
                continue
            hits.append(Hit(id=str(getattr(r, "source_id", "")),
                            score=float(getattr(r, "score", 0.0) or 0.0), payload=payload))
            if len(hits) >= k:
                break
        return hits

    def ingest_knowledge(self, source_id: str, text: str, metadata: dict | None = None) -> None:
        """Feed a trajectory into HydraDB's managed graph/memory pipeline.

        Unlike the raw-embedding path, this runs HydraDB's LLM entity/relation
        extraction (so it shows up as token usage) and builds a queryable
        knowledge graph of trajectories. Best-effort and non-fatal.
        """
        if not CONFIG.hydra_kg:
            return
        md = {k: str(v) for k, v in (metadata or {}).items()
              if isinstance(v, (str, int, float, bool))}
        source = {
            "id": str(source_id),
            "tenant_id": self.kg_tenant,
            "sub_tenant_id": self.sub,
            "title": (md.get("title") or str(source_id))[:120],
            "type": "agent_trajectory",
            "content": {"text": text[:6000]},
            "tenant_metadata": md,
        }
        try:
            self.client.upload.knowledge(tenant_id=self.kg_tenant, sub_tenant_id=self.sub,
                                         upsert=True, app_sources=json.dumps([source]))
            self._kg_count += 1
        except Exception as e:  # noqa: BLE001
            print(f"[hydradb] kg ingest failed: {repr(e)[:160]}")

    def graph_recall(self, query: str, k: int = 3):
        """Graph-aware contextual recall via HydraDB's managed pipeline (token usage)."""
        if not CONFIG.hydra_kg:
            return None
        try:
            return self.client.recall.full_recall(
                tenant_id=self.kg_tenant, sub_tenant_id=self.sub, query=query,
                mode="fast", graph_context=True, max_results=k)
        except Exception as e:  # noqa: BLE001
            print(f"[hydradb] graph_recall failed: {repr(e)[:160]}")
            return None

    def clear(self) -> None:
        # HydraDB persists server-side; for a clean campaign set a fresh
        # HYDRADB_COLLECTION (sub-tenant) rather than deleting in place.
        print("[hydradb] clear() is a no-op (server-side store). "
              "Set HYDRADB_COLLECTION to a fresh name to start clean.")

    def save(self) -> None:
        pass

    def __len__(self) -> int:
        # >=1 so retrieval always queries HydraDB (enables cross-process reuse:
        # seed in one run, recall in the next). Search handles emptiness.
        return max(self._count, 1)
