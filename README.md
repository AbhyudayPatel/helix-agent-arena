# HELIX — Trajectory Intelligence Platform

> A self-healing AppWorld agent that treats the **trajectory** —
> `State → Decision → Action → Outcome` — as the unit of observability, prediction, and repair.

![alt text](image.png)
![alt text](image-1.png)

Built for the `://agent_arena` hackathon (AppWorld + HydraDB). Every run is recorded as a
graph, monitored live, healed on failure, and reused — details in
[`ARCHITECTURE.md`](ARCHITECTURE.md) · [`RESULTS.md`](RESULTS.md) · [`HYDRADB.md`](HYDRADB.md).

**What it does:** grounded bootstrap → subgoal plan → world-model picks the best branch →
ReAct code loop → live monitor (loops/errors/stalls) → self-healer (recall + diagnose + repair,
won't repeat a failed fix) → **verification gate** before finishing → trajectory indexed to
HydraDB for reuse.

## Agent architecture

![HELIX architecture](reports/architecture.png)

Per-task, HELIX records a `State→Decision→Action→Outcome` graph and acts on it live. Below is a
**real self-healing run** — the task **recovered 18 times and still solved** (red = `recovers`
edges from the self-healer; the monitor catches the failures):

![HELIX self-healing trajectory](reports/healing_flow.png)

Deep dive in [`ARCHITECTURE.md`](ARCHITECTURE.md).

---

## Results (real runs)

**Claude Sonnet 4.6 (recommended config):**

| run | set | tasks | **TGC** |
|---|---|---|---|
| `team_helix_sonnet` | test_normal | 10 | **80.0% (8/10)** |
| `team_helix_sonnet_20` | test_normal | 20 | 70.0% (14/20) |

The official ReAct baseline on AppWorld test_normal is **48.8 TGC** — **Sonnet 4.6 + HELIX hits
80% on a 10-task test_normal sample**, well above it (and ~5× cheaper than Opus).

**Official eval set (`agent_arena_eval`, 10 hard challenge tasks):**

| run | model | tasks | **TGC / SGC** |
|---|---|---|---|
| `team_helix` | Llama 3.3 70B (OpenRouter) | 10 | **20% / 20%** (2/10) |

Llama 70B is the open-model baseline — it floors out on the hard `test_challenge` tier (3 easy /
3 medium / 4 hard). For a competitive submission, run **Sonnet/Opus** on the same set (the scaffold
got 80% on a test_normal sample with Sonnet). Outputs + `evaluations/agent_arena_eval.json` are in
`experiments/outputs/team_helix/`.

**Wider benchmarks (Opus 4.8, full stack + HydraDB):**

| run | set | tasks | TGC |
|---|---|---|---|
| `dev_final` | dev | 57 | 78.9% (45/57) |
| `v2_dev` | dev (no memory) | 20 | 70.0% |
| `dev_ablation` | dev (plain ReAct) | 20 | 60.0% |

- **Ablation:** full stack **75%** vs plain ReAct **60%** (+15pp), fewer steps & errors.
- **Memory:** **75.9% with** recalled trajectories vs **57.6% without** (+18pp).
- **World-model:** 83% accuracy (Brier 0.14).

---

## Setup (one-time, already done here)

```powershell
uv venv .venv --python 3.12 --seed
uv pip install --python .venv\Scripts\python.exe -e . appworld
.\.venv\Scripts\appworld.exe install ; .\.venv\Scripts\appworld.exe download data
```
Requires `ANTHROPIC_API_KEY`. On Windows always run in UTF-8 mode (`$env:PYTHONUTF8="1"`).

## Run (Anthropic — Sonnet recommended, Opus for max score)

```powershell
$env:PYTHONUTF8="1"; $env:MODEL="claude-sonnet-4-6"     # recommended (Opus: claude-opus-4-8)

# iterate on dev (writes trajectory graphs to reports/<exp>/)
.\.venv\Scripts\python.exe -m helix.run --split dev --limit 10 --experiment dev10 `
    --model claude-sonnet-4-6 --max-steps 40 --no-memory

# OFFICIAL eval + submission (the 10-task agent_arena_eval set)
$env:APPWORLD_DATASET="agent_arena_eval"; $env:MAX_TASKS="0"; $env:APPWORLD_EXPERIMENT="team_<name>"
.\.venv\Scripts\python.exe hack_agent_arena\agent.py
.\.venv\Scripts\appworld.exe evaluate team_<name> agent_arena_eval
# submit experiments/outputs/team_<name>/  (evaluations/agent_arena_eval.json + every tasks/<id>/dbs/)
```

The v3 scaffold (verification gate, repair-memory, subgoal plan, ast-guard) is built to carry
Sonnet at ~5× lower cost than Opus. HydraDB integration earns the bonus (see `HYDRADB.md`).
