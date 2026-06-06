"""Central configuration for HELIX.

Everything is overridable via environment variables so the same code runs
unchanged on a laptop (local fallbacks) and at the hackathon venue (HydraDB +
strong models). Toggles let us run ablations for the benchmark.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# NOTE: AppWorld owns ./data and ./experiments (it wipes ./data on re-download),
# so HELIX keeps its own state in a dedicated, separate directory.
EXPERIMENTS_DIR = ROOT / "experiments"          # shared with AppWorld eval outputs
REPORTS_DIR = ROOT / "reports"
APPWORLD_DATA_DIR = ROOT / "data"               # owned by AppWorld
DATA_DIR = ROOT / "helix_store"                 # owned by HELIX
MEMORY_DIR = DATA_DIR / "memory"
CACHE_DIR = DATA_DIR / "cache"
TRAJECTORY_DIR = DATA_DIR / "trajectories"

for _d in (EXPERIMENTS_DIR, REPORTS_DIR, DATA_DIR, MEMORY_DIR, CACHE_DIR, TRAJECTORY_DIR):
    _d.mkdir(parents=True, exist_ok=True)


def _flag(name: str, default: str = "1") -> bool:
    return os.environ.get(name, default).lower() in ("1", "true", "yes", "on")


@dataclass
class Config:
    # --- Models ---------------------------------------------------------
    # Main agent loop. Sonnet is the cost/quality sweet-spot for many-step
    # code agents; bump to claude-opus-4-8 at the venue for max score.
    agent_model: str = os.environ.get("HELIX_AGENT_MODEL", "claude-sonnet-4-6")
    # High-stakes planning / synthesis.
    planner_model: str = os.environ.get("HELIX_PLANNER_MODEL", "claude-opus-4-8")
    # Cheap, fast model for world-model branch scoring.
    world_model_model: str = os.environ.get("HELIX_WM_MODEL", "claude-haiku-4-5-20251001")
    embedding_model: str = os.environ.get("HELIX_EMBED_MODEL", "text-embedding-3-small")
    embedding_dim: int = int(os.environ.get("HELIX_EMBED_DIM", "1536"))

    # --- Budgets --------------------------------------------------------
    max_steps: int = int(os.environ.get("HELIX_MAX_STEPS", "40"))
    recovery_budget: int = int(os.environ.get("HELIX_RECOVERY_BUDGET", "6"))
    max_tokens_per_call: int = int(os.environ.get("HELIX_MAX_TOKENS", "4096"))

    # --- Memory / retrieval --------------------------------------------
    retrieval_k: int = int(os.environ.get("HELIX_RETRIEVAL_K", "5"))

    # --- Feature toggles (for ablations) -------------------------------
    enable_memory: bool = _flag("HELIX_MEMORY")
    enable_world_model: bool = _flag("HELIX_WORLD_MODEL")
    enable_healing: bool = _flag("HELIX_HEALING")
    enable_graphviz_render: bool = _flag("HELIX_RENDER", "1")

    # --- HydraDB --------------------------------------------------------
    hydra_url: str | None = os.environ.get("HYDRADB_URL") or os.environ.get("HYDRA_URL")
    hydra_api_key: str | None = os.environ.get("HYDRADB_API_KEY") or os.environ.get("HYDRA_API_KEY")
    hydra_tenant: str = os.environ.get("HYDRADB_TENANT", "helix")
    hydra_collection: str = os.environ.get("HYDRADB_COLLECTION", "trajectories")
    # managed knowledge-graph memory (HydraDB's LLM pipeline -> entity/relation
    # extraction + token usage). Separate tenant from the BYOE embeddings tenant.
    hydra_kg_tenant: str = os.environ.get("HYDRADB_KG_TENANT", "helix_kg")
    hydra_kg: bool = _flag("HYDRADB_KG", "1")

    # --- Keys -----------------------------------------------------------
    anthropic_api_key: str | None = os.environ.get("ANTHROPIC_API_KEY")
    openai_api_key: str | None = os.environ.get("OPENAI_API_KEY")
    groq_api_key: str | None = os.environ.get("GROQ_API_KEY")
    groq_base_url: str = os.environ.get("GROQ_BASE_URL", "https://api.groq.com/openai/v1")

    @property
    def use_hydra(self) -> bool:
        # the hydra-db-python SDK authenticates with the api key (token); no URL needed
        return bool(self.hydra_api_key)


CONFIG = Config()

# Approximate USD pricing per 1M tokens (input, output). Used only for the cost
# accounting display / cost-prediction metric; override freely.
PRICING = {
    "claude-opus-4-8": (15.0, 75.0),
    "claude-sonnet-4-6": (3.0, 15.0),
    "claude-haiku-4-5-20251001": (1.0, 5.0),
    "text-embedding-3-small": (0.02, 0.0),
    "text-embedding-3-large": (0.13, 0.0),
}
