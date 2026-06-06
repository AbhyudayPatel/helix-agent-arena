# HELIX — Lab Notebook (insights & improvement backlog)

A running record of what we learned building HELIX on AppWorld, the failure modes
we hit, the fixes, and what to try next. Pair with `reports/INSIGHTS.md` (auto-generated
from the trajectory logs) and the per-experiment `metrics.json` / `summaries.json`.

## What is logged where (everything is recorded)
- **Per task**: `helix_store/trajectories/<task>.trajectory.json` — the full graph
  (every State/Decision/Action/Outcome, monitor signals, recoveries, world-model
  predictions + realized outcomes, per-step cost/latency, the exact code + observation).
- **Per experiment**: `reports/<exp>/metrics.json` (Trajectory Intelligence Benchmark),
  `summaries.json` (per-task rollup), `index.html` (dashboard), `graphs/<task>.{html,svg,dot}`.
- **AppWorld native**: `experiments/outputs/<exp>/tasks/<task>/logs/environment_io.md`
  (code↔output), `logs/api_calls.jsonl`, `evaluation/report.md`.
- **Cross-run history**: `reports/run_log.jsonl` + `reports/INSIGHTS.md` (via `scripts/analyze.py`).
- **LLM accounting**: token + USD totals per run (`GLOBAL_USAGE`), per-decision cost on the graph.

## Timeline of failure modes → fixes (the hard-won lessons)
1. **Python 3.14 vs AppWorld deps** → isolate with `uv venv --python 3.12`.
2. **`signal.SIGALRM` (Unix-only) in AppWorld's timeout** → construct `AppWorld(timeout_seconds=None)`.
3. **cp1252 UnicodeEncodeError** when AppWorld writes reports → run in UTF-8 mode
   (`PYTHONUTF8=1`; `win_compat.ensure_utf8_mode()` self-re-execs).
4. **freezegun freezes `time.time()`/`perf_counter`/`monotonic`** during a task →
   latency/wall-time read 0. Fix: capture the real `perf_counter` at import, hidden in
   a list so freezegun's scanner can't swap it (`util.real_clock`).
5. **Sonnet hallucinated app data** (invented a 30-song Spotify library, fake passwords,
   submitted a made-up answer) instead of calling APIs. Fixes that worked:
   - switch the agent loop to **Opus 4.8** (executes for real),
   - a **deterministic grounded opening** (auto-fetch task/passwords/profile/apps as step 1),
   - an explicit **anti-fabrication** prompt section.
6. **Opus 4.8 rejects `temperature`** ("deprecated for this model") → omit it (auto-detected).
7. **Multi-source aggregation / answer-format failures** (e.g. "top-4 most played R&B
   across songs+albums+playlists"): the agent under-collected or mis-formatted. Adding a
   **COMPLETENESS & ANSWERS** prompt section (full pagination, gather every named source,
   compute in Python, match exact format, re-read+verify before complete_task) took the
   `50e1ac9_*` template from **0/3 → 3/3**.
8. **Streamlit (>=1.58) needs starlette>=1; AppWorld's FastAPI 0.110 needs starlette<0.38**
   → incompatible. Keep the venv AppWorld-clean; run the optional Streamlit explorer under
   the system Python (the static HTML dashboard needs nothing).
9. **HydraDB** integrates via `hydra-db-python` (token auth, no URL). `tenant.create` is
   async ("accepted"); `embeddings.insert(... upsert=True)` and `embeddings.search(...)`
   work with BYOE vectors + metadata. We store the **trajectory graph** (nodes+edges) in
   the task-record metadata, so the graph lives in HydraDB, not just the vector.
10. **"HydraDB shows no token usage"** — because BYOE (raw embeddings) sends *our* vectors,
   HydraDB does no LLM work → 0 tokens (correct/efficient, verified: the `final` collection
   returned the real benchmark records). Token usage only comes from HydraDB's **managed**
   pipeline. So we added `upload.knowledge` (LLM entity/relation extraction → token usage +
   a queryable trajectory knowledge graph) + `recall.full_recall(graph_context=True)`, wired
   into `index_trajectory`, and bulk-ingested all 87 trajectories. See `HYDRADB.md`.

## Behavioral observations
- AppWorld is exact-match scored and hard; per-task Opus runs are **nondeterministic**
  (the same easy task solved in 9 steps once, failed-rushed in 8 another time). Judge on
  aggregates, not single tasks.
- The monitor's `over_exploring`/`budget_burn → replan` and `repeated_error/loop → heal`
  signals fire in practice and recover runs.
- Knowledge reuse only triggers off **solved** trajectories (by design) — the more we
  solve, the more later same-template variants benefit.

## Final benchmark (Opus 4.8, HydraDB memory) — see RESULTS.md
- **dev 57: TGC 78.9%** (45/57); L1 76.7%, L2 83.3%, L3 66.7%. train-seed 30: 60.0%.
- **Ablation** (same 20 dev tasks): full **75.0%** vs plain **60.0%** (+15pp), fewer steps
  (12.2 vs 15.5), fewer errors (1.1 vs 2.0), 20 recoveries vs 0, lower cost.
- **Memory reuse**: 75.9% solve WITH vs 57.6% WITHOUT (+18pp, 87 runs).
- **World-model**: 80.5% acc, Brier 0.16, well-calibrated. **Recovery**: ~28–44% of failed steps healed.
- Campaign cost ≈ $208 (Opus); avg $1.60/task on dev.

## Implemented after the big run (data-driven from the logs)
- **`over_exploring` was too trigger-happy** (fired step ~4 on nearly every task) →
  raised `DOC_STREAK_LIMIT` 4→6 in `monitor.py`.
- **Heal loops** (10–16 consecutive heals of the same error) → **heal escalation**: after
  3 repeated heals the agent is told to abandon the approach / try a different path / finalize
  with partial results (`agent._escalation_block`); skips the healer LLM call to save cost.
- **Auto-logging**: every run now emits `reports/<exp>/INSIGHTS.md` + appends `run_log.jsonl`.

## Improvement backlog (ranked by expected score impact)
1. **Self-verification gate before finalizing**: when the agent calls `complete_task`, run
   one mandatory verify turn (re-read task + recompute) before accepting — catches rushed
   wrong answers (the 8-step easy-task failure). Risk: may second-guess correct answers; A/B it.
2. **Per-template prompt priors** from `INSIGHTS.md`: feed the agent the known-good app/API
   pattern for the closest solved template (already partially via memory; make it sharper).
3. **Answer normalization**: enforce exact stored strings + ordering programmatically where
   the task shape is detectable (lists, counts).
4. **Model routing**: Haiku/Sonnet for trivially-easy tasks (with grounding), Opus for hard
   — cut cost ~3–5× at similar score.
5. **Pagination/aggregation helper**: a tested utility the agent can call to fully page a
   list API, reducing under-collection.
6. **World-model-driven retries**: if predicted P(success) is low after a plan, branch and
   try the runner-up before committing.
7. **Throughput**: shard tasks across processes for checkpoints (tasks are independent).
8. **Cost**: truncate old observations in the conversation more aggressively for long tasks.

## Reproducing the headline results
```powershell
$env:PYTHONUTF8="1"; $env:HYDRADB_API_KEY="..."; $env:HYDRADB_COLLECTION="final"
.\.venv\Scripts\python.exe -m helix.run --split dev --limit 57 --experiment dev_final --max-steps 28
.\.venv\Scripts\python.exe scripts\analyze.py     # -> reports/INSIGHTS.md + run_log.jsonl
```
