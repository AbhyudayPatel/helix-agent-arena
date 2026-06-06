"""Pluggable vector store.

Interface intentionally tiny (add / search) so the backend is swappable:
  * LocalVectorStore - numpy cosine, zero external deps, always available.
  * HydraVectorStore - HydraDB (graph+vector context substrate), used at the
    venue when HYDRADB_URL / HYDRADB_API_KEY are set.

``get_vector_store`` picks HydraDB when configured and reachable, otherwise
falls back to local so the system never hard-fails.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from ..config import CONFIG, MEMORY_DIR


@dataclass
class Hit:
    id: str
    score: float
    payload: dict


class VectorStore:
    backend: str = "abstract"

    def add(self, id: str, vector, payload: dict) -> None:
        raise NotImplementedError

    def add_many(self, items) -> None:
        for i, v, p in items:
            self.add(i, v, p)

    def search(self, vector, k: int = 5, where: dict | None = None) -> list[Hit]:
        raise NotImplementedError

    def save(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def __len__(self) -> int:
        return 0


class LocalVectorStore(VectorStore):
    backend = "local"

    def __init__(self, name: str = "trajectories", dim: int | None = None,
                 path: str | Path | None = None):
        self.name = name
        self.dim = dim or CONFIG.embedding_dim
        self.path = Path(path) if path else (MEMORY_DIR / f"{name}.npz")
        self.ids: list[str] = []
        self.payloads: list[dict] = []
        self._mat: np.ndarray | None = None  # (N, dim) L2-normalized rows
        self._load()

    # -- persistence ------------------------------------------------------- #
    @property
    def _meta_path(self) -> Path:
        return self.path.with_suffix(".meta.json")

    def _load(self) -> None:
        if self.path.exists() and self._meta_path.exists():
            try:
                self._mat = np.load(self.path)["mat"]
                obj = json.loads(self._meta_path.read_text(encoding="utf-8"))
                self.ids = obj["ids"]
                self.payloads = obj["payloads"]
                self.dim = obj.get("dim", self.dim)
            except Exception:
                self._mat, self.ids, self.payloads = None, [], []

    def save(self) -> None:
        if self._mat is None:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(self.path, mat=self._mat)
        self._meta_path.write_text(
            json.dumps({"ids": self.ids, "payloads": self.payloads, "dim": self.dim}),
            encoding="utf-8",
        )

    # -- ops --------------------------------------------------------------- #
    @staticmethod
    def _norm(v) -> np.ndarray:
        v = np.asarray(v, dtype=np.float32).ravel()
        n = np.linalg.norm(v)
        return v / n if n > 0 else v

    def add(self, id: str, vector, payload: dict) -> None:
        v = self._norm(vector).reshape(1, -1)
        self._mat = v if self._mat is None else np.vstack([self._mat, v])
        self.ids.append(id)
        self.payloads.append(payload)

    def clear(self) -> None:
        self.ids, self.payloads, self._mat = [], [], None
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._meta_path.write_text(
            json.dumps({"ids": [], "payloads": [], "dim": self.dim}), encoding="utf-8")

    def search(self, vector, k: int = 5, where: dict | None = None) -> list[Hit]:
        if self._mat is None or not self.ids:
            return []
        sims = self._mat @ self._norm(vector)
        hits: list[Hit] = []
        for idx in np.argsort(-sims):
            p = self.payloads[idx]
            if where and not all(p.get(kk) == vv for kk, vv in where.items()):
                continue
            hits.append(Hit(self.ids[idx], float(sims[idx]), p))
            if len(hits) >= k:
                break
        return hits

    def __len__(self) -> int:
        return len(self.ids)


def get_vector_store(name: str = "trajectories") -> VectorStore:
    if CONFIG.use_hydra:
        try:
            from .hydra_store import HydraVectorStore
            store = HydraVectorStore(name)
            print(f"[memory] using HydraDB backend (collection={name})")
            return store
        except Exception as e:  # noqa: BLE001
            print(f"[memory] HydraDB unavailable ({e}); falling back to local store.")
    return LocalVectorStore(name)
