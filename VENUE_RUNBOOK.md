# HELIX — Venue Runbook (agent_arena, 6h)

Operational guide for running and demoing HELIX at the hackathon.

## 0. Sanity (already set up in this repo)
```powershell
$env:PYTHONUTF8="1"                       # required on Windows
.\.venv\Scripts\python.exe scripts\smoke_test.py   # should print SMOKE TEST OK
```

## 1. Run for a checkpoint
The leaderboard ranks by raw AppWorld score (Task Goal Completion). Run the full
self-healing stack on the target split, then submit the AppWorld evaluation.

```powershell
# Opus (best accuracy). Seed memory on train first so reuse helps later splits.
.\.venv\Scripts\python.exe -m helix.run --split train --limit 90 --experiment seed
.\.venv\Scripts\python.exe -m helix.run --split test_normal --experiment ckpt1
```
AppWorld per-task evaluations are written under
`experiments/outputs/<experiment>/tasks/<task_id>/evaluation/`. The official
aggregate can also be produced with the AppWorld CLI:
```powershell
.\.venv\Scripts\appworld.exe evaluate ckpt1 test_normal
```

## 2. Model / cost / time tradeoff
- **`claude-opus-4-8`** (default): solves tasks for real; ~$0.5–2/task; use for ranked runs.
- **`claude-sonnet-4-6`** (`--model claude-sonnet-4-6`): ~5× cheaper/faster but tends to
  hallucinate app data on AppWorld — only use with the grounded bootstrap on, and verify quality.
- Bound per-task cost with `--max-steps` (default 40; 25 is a good cap).
- `world_model`/`healer` add a few cheap calls per task; disable with `--no-world-model`/`--no-healing` to cut cost.
- Parallelism: tasks are independent — run several `--tasks ...` shards in separate processes if you need throughput, then merge `reports/*/`.

## 3. HydraDB (bonus points)
```powershell
uv pip install --python .venv\Scripts\python.exe hydra-db-python
$env:HYDRADB_URL="..."; $env:HYDRADB_API_KEY="..."
# memory automatically uses HydraDB; confirm method names in helix/memory/hydra_store.py
.\.venv\Scripts\python.exe -m helix.run --split dev --limit 5 --experiment hydra_check
# look for: "[memory] using HydraDB backend"
```
Story for judges: a trajectory *is* a graph whose nodes carry embeddings — HydraDB's
graph+vector+memory substrate is the natural home for it, so we retrieve *contextually
similar trajectories* before every decision and every recovery.

## 4. Ablations (for the pitch — show the layers earn their keep)
```powershell
.\.venv\Scripts\python.exe -m helix.run --split dev --limit 10 --experiment full
.\.venv\Scripts\python.exe -m helix.run --split dev --limit 10 --no-memory --no-world-model --no-healing --experiment plain
```
Compare `reports/full/metrics.json` vs `reports/plain/metrics.json`.

## 5. What to show judges
1. Open `reports/<exp>/index.html` — the Trajectory Intelligence Benchmark dashboard.
2. Click into a trajectory graph (`graphs/<task>.html`) — point at:
   - the **world-model prediction branches** (purple diamonds) at the plan node,
   - a **red `recovers` edge** where the monitor caught a failure and the healer fixed it,
   - the **blue `informs` edges** from recalled memories on a reused task.
3. Live explorer (optional): run with a streamlit-capable Python (the **system**
   Python, NOT the AppWorld venv — streamlit's starlette conflicts with FastAPI 0.110):
   `python -m streamlit run helix/dashboard_app.py` from the project root.
4. The one-sentence pitch (see README).

## 6. Knobs
`HELIX_AGENT_MODEL`, `HELIX_MAX_STEPS`, `HELIX_RETRIEVAL_K`,
`HELIX_MEMORY/WORLD_MODEL/HEALING=0|1`, `HYDRADB_URL/HYDRADB_API_KEY`.
