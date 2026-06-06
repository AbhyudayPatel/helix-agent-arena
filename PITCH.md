# HELIX — Pitch & Demo Script

## One sentence
We built a **trajectory-intelligence platform**: instead of merely executing actions, our
AppWorld agent records every run as a `State → Decision → Action → Outcome` graph, simulates
outcomes before acting, predicts and **heals failures in real time**, and **reuses prior
trajectories** to solve new tasks — every run explainable as a graph, every trajectory stored
in **HydraDB**.

## Why it's different
Everyone else ships *an agent* and logs prompts/tokens. We ship the **layer above** it:

| Today's observability | HELIX |
|---|---|
| tokens, requests, latency, cost | states, decisions, actions, world-transitions, outcomes |
| "GPT failed / Claude worked" | "this trajectory pattern fails 91% of the time → take this branch" |
| logs | a graph you can query, predict over, and heal |

Four working subsystems, all visible in the trajectory graph:
1. **Monitor** — reads the live trajectory each step; fires `heal`/`replan`/`abort`.
2. **World-model** — scores candidate plans `P(success) = LLM ⊕ memory prior`, picks the best.
3. **Self-healer** — on failure: recall a similar past fix → diagnose → propose distinct fixes → world-model picks → inject.
4. **Memory (HydraDB)** — stores trajectory vectors + the graph; recalls winning approaches for similar tasks.

## HydraDB (bonus track) — used as the agent's context substrate
A trajectory *is* a graph whose nodes carry embeddings — HydraDB's graph+vector+memory store
is its natural home. We use `hydra-db-python` (raw BYOE embeddings): each trajectory record is
inserted with its metadata, and **task-level records carry the compact trajectory graph
(nodes+edges) in metadata**, so the graph itself lives in HydraDB. Before every task (and every
recovery) we semantic-search HydraDB for similar solved trajectories. Verified live:
insert + search return correctly-scored, metadata-rich hits.

We use **both** HydraDB paths: BYOE raw-embedding vectors (fast, cheap per-decision recall)
**and** the managed knowledge-graph pipeline (`upload.knowledge` → LLM entity/relation
extraction → `recall.full_recall(graph_context=True)`), which turns our trajectories into a
queryable knowledge graph and exercises HydraDB's differentiated graph+memory engine. See
`HYDRADB.md`.

## Demo script (3 minutes)
1. **Dashboard** — open `reports/dev_final/index.html`: Task-Goal-Completion + recovery rate +
   world-model accuracy + knowledge-reuse tiles, failure-pattern panel, per-task table.
2. **A healed run** — open a trajectory graph with a red `recovers` edge: "the monitor caught a
   repeated failure, the healer diagnosed it and switched approach — and the task still solved."
   (e.g. `82e2fac_1` recovered twice and solved.)
3. **World-model branches** — point at the purple `predicts` diamonds on the plan node: the
   agent scored strategies and chose the highest-probability one *before* acting.
4. **Knowledge reuse** — show the blue `informs` edges: a later task reused a recalled solved
   trajectory from HydraDB. Cite the 0→3 lift on the `50e1ac9` template after tuning, and
   `INSIGHTS.md` reuse solve-rate with vs without memory.
5. **Ablation** — `reports/comparison.html`: full stack vs plain ReAct on the same tasks.
6. **It's all logged** — `INSIGHTS.md`, `run_log.jsonl`, `LAB_NOTEBOOK.md`.

## Numbers to cite (from the live benchmark — see RESULTS.md)
- **Dev Task-Goal-Completion: 78.9% (45/57)** — competitive vs ~40–60% published ReAct baselines.
- **Ablation (+15pp)**: full stack **75.0%** vs plain ReAct **60.0%** on the same 20 dev tasks,
  with fewer steps (12.2 vs 15.5), fewer errors (1.1 vs 2.0), and lower cost.
- **Memory reuse (+18pp)**: 75.9% solve WITH recalled trajectories vs 57.6% WITHOUT (87 runs).
- **World-model**: 80.5% accuracy, Brier 0.16, well-calibrated (high-conf → 82.6% solve).
- **Self-healing**: solved tasks after 16 / 12 / 9 recoveries; ~28–44% of failed steps healed.
- **Tuning win**: `50e1ac9_{1,2,3}` aggregation template **0/3 → 3/3** after the completeness/verify prompt.

## Why this is where AI infra is going
Agents are becoming autonomous and long-horizon. The unit that matters is no longer the prompt
— it's the **trajectory**. HELIX makes trajectories first-class: observed, predicted, healed,
and reused. That's an operating system for autonomous intelligence, not another agent.
