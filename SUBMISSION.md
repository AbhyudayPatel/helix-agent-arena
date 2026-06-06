# Submission — HELIX (`://agent_arena`)

| Field | Value |
|---|---|
| **Team name** | `helix` |
| **GitHub repo** | https://github.com/AbhyudayPatel/helix-agent-arena |
| **Agent** | `hack_agent_arena/agent.py` (HELIX) — general, code-writing AppWorld agent |
| **Model used (eval run)** | `meta-llama/llama-3.3-70b-instruct` (OpenRouter) |
| **Self-reported TGC / SGC** | **20.0 / 20.0** on `agent_arena_eval` (2/10) |
| **HydraDB used?** | **yes** — trajectory vector memory (BYOE) + managed knowledge-graph (`upload.knowledge` / `full_recall`) |
| **Integrity** | **confirmed** — general agent, **no `task_id` hardcoding** |

## Output folder (re-evaluatable)
```
experiments/outputs/team_helix/
├── evaluations/agent_arena_eval.json     # TGC/SGC + per-task pass/fail
└── tasks/<id>/dbs/*.jsonl                 # final app DB state for re-evaluation
```
Reproduce the score:
```bash
appworld evaluate team_helix agent_arena_eval        # or: python scripts/evaluate_partial.py team_helix agent_arena_eval
```

## What HELIX is
A self-healing **trajectory-intelligence** agent: every run is a `State→Decision→Action→Outcome`
graph that is monitored live, **healed** on failure (recall → diagnose → repair, never repeating a
failed fix), planned over by a **world-model**, **verified** before finishing, and **reused** from
HydraDB. Architecture + diagrams in [`README.md`](README.md) / [`ARCHITECTURE.md`](ARCHITECTURE.md);
HydraDB details in [`HYDRADB.md`](HYDRADB.md).

## Notes on the number
Llama 3.3 70B is the open-model baseline and floors out on the hard `test_challenge` tier (the
eval set is 3 easy / 3 medium / 4 hard). With **Claude Sonnet 4.6**, the same agent scored **80%
(8/10)** on a `test_normal` sample (`experiments/outputs/team_helix_sonnet/`) — to submit the
competitive number, run the agent on `agent_arena_eval` with `MODEL=claude-sonnet-4-6` and
regenerate `evaluations/agent_arena_eval.json`.

## Run it
```bash
export APPWORLD_EXPERIMENT=team_helix APPWORLD_DATASET=agent_arena_eval MAX_TASKS=0
python hack_agent_arena/agent.py
appworld evaluate team_helix agent_arena_eval
```
Full reproduction steps + setup in [`README.md`](README.md). Hackathon rules/format in
[`hack_agent_arena/SUBMISSION.md`](hack_agent_arena/SUBMISSION.md).
