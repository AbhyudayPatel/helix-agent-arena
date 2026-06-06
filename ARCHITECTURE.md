# HELIX — Architecture (deep dive)

HELIX is a **trajectory-intelligence agent**. The whole design rests on one idea:

> The unit of computation is not a prompt/response. It is a **trajectory** —
> `State → Decision → Action → Outcome → State → …` — recorded as a graph, and
> then *observed, predicted over, healed, and reused* in real time.

Everything below is how that idea becomes running code.

---

## 0. The mental model (one screen)

```
                         ┌───────────────────────── HELIX loop (per task) ─────────────────────────┐
   AppWorld task ─────▶  │  S0 ─plan─▶ bootstrap ─▶  ┌── ReAct step ──┐  ─▶ … ─▶ complete ─▶ eval   │
                         │                          │ decide→act→obs  │                              │
                         │   memory recall ─────────┘      │           └── monitor ── heal/replan ──┘ │
                         └────────────────────────────────┼──────────────────────────────────────────┘
                                                          ▼
                          every step is appended to a TRAJECTORY GRAPH (nodes+edges),
                          which the Monitor reads live, the World-Model predicts over,
                          the Healer repairs, and the Memory indexes for the next task.
```

Five engines act on the trajectory:

| engine | reads | writes / acts | uses ground truth? |
|---|---|---|---|
| **Agent (ReAct)** | conversation + grounded data | code actions on AppWorld | no |
| **Monitor** | live trajectory | signals → intervention (heal/replan/abort) | no |
| **World-model** | task + candidate plans + memory prior | picks the highest-P(success) branch | no |
| **Self-healer** | failed outcome + recent history + memory | recovery guidance injected into next turn | no |
| **Memory** | trajectory at end of task | vectors + knowledge graph (HydraDB) | only on *train* |

---

## 1. End-to-end control flow (one task)

```
run_task(task_id):
  │
  ├─(1) env.reset(task_id)                         # AppWorld world, timeout_seconds=None
  │        └─▶ instruction, supervisor, allowed_apps, datetime
  │
  ├─(2) Trajectory()  +  add S0 (start state)
  │
  ├─(3) MEMORY RECALL  recall_for_task(instruction)
  │        └─▶ similar SOLVED approaches → memory nodes + task_lessons text
  │
  ├─(4) WORLD-MODEL PLAN  _plan()
  │        ├─ LLM proposes 2–3 strategies
  │        ├─ world_model.assess(strategies) = 0.7·LLM + 0.3·memory_prior
  │        ├─ add d0 (plan decision) + prediction nodes (purple)
  │        └─▶ chosen strategy → plan_block
  │
  ├─(5) initial user message  = instruction + supervisor + apps + lessons + plan_block
  │
  ├─(6) BOOTSTRAP (deterministic step 1)
  │        └─ execute: show_active_task + show_account_passwords + show_profile + app_descriptions
  │           → grounds the model in REAL data (kills "solve it in my head")
  │
  ├─(7) REACT LOOP  step = 2 … max_steps:
  │        a. text   = LLM.complete(SYSTEM_PROMPT, messages)        # prompt-cached
  │        b. thought, code = split_thought_code(text)
  │        c. add DECISION node   (prev_state ─decides→ decision)
  │              • first model decision: memory ─informs→ decision
  │              • if pending_recovery: decision.status=recovery; failed_outcome ─recovers→ decision
  │        d. if no code → nudge, continue
  │        e. add ACTION node  (decision ─acts→ action)
  │           obs = env.execute(code)  →  Observation(status, error_type, latency, api_calls)
  │           add OUTCOME node  (action ─yields→ outcome)
  │        f. add STATE node    (outcome ─transitions→ state);  reset heal counter if non-error
  │        g. report = MONITOR.observe(trajectory)               # signals + intervention
  │        h. dispatch:
  │              heal   → (≥3 repeats? escalate : healer.plan_recovery) → inject guidance
  │              replan → inject "commit to progress" nudge
  │              abort  → inject "call complete_task now"
  │        i. append observation (+guidance) as next user message
  │        j. if env.completed():  break          # agent called apis.supervisor.complete_task
  │
  ├─(8) eval = env.evaluate()   → {success, num_tests, difficulty}
  │     trajectory.finalize(eval, usage)
  │
  └─(9) return trajectory
            └─(runner) save JSON · index into MEMORY · visualize · metrics · dashboard
```

---

## 2. Component deep dives

### 2.1 AppWorld environment adapter — `appworld_env.py`
- Wraps AppWorld **in-process** (embedded IPython shell; no server). Variables persist across `execute` calls.
- `execute(code)` runs the code and **parses** the raw string into a structured `Observation`:
  - `status` ∈ {ok, error, empty}; `error_type` (regex on the traceback's last `*Error/*Exception`);
    `latency_s` (measured with a freezegun-proof clock); `num_api_calls` (counts `apis.x.y(`).
- `completed()` → `world.task_completed()`; `evaluate()` → `TestTracker.to_dict()` + `.success`.
- Windows specifics baked in: `timeout_seconds=None` (no SIGALRM) and UTF-8 mode.

### 2.2 The trajectory graph — `trajectory.py`
Node kinds and what they carry:

| kind | shape | key data |
|---|---|---|
| `state` | box | instruction/apps (S0), or "progressed/error" |
| `decision` | ellipse | thought, context, cost, model, predicted/actual_success, diagnosis |
| `action` | note | the exact python `code` |
| `outcome` | box | status, error_type, latency, num_api_calls, **monitor signals**, raw output |
| `prediction` | diamond | a world-model branch: plan + p_success + rationale |
| `memory` | cylinder | a recalled trajectory: similarity score + payload |

Edges: `decides` (state→decision), `acts` (decision→action), `yields` (action→outcome),
`transitions` (outcome→state), `recovers` (failed outcome→recovery decision, red),
`predicts` (plan decision→prediction, purple), `informs` (memory→decision, blue).

Derived metrics live here: `num_steps`, `num_errors`, `num_recoveries`, `recovery_rate`,
`world_model_accuracy` (predicted≥0.5 vs realized), `total_cost`, `wall_time`. Serializes
to JSON; `compact_graph()` emits the node/edge view stored in HydraDB.

### 2.3 LLM layer — `llm.py`
- `ClaudeLLM.complete(system, messages)` — Anthropic call with **prompt caching** on the
  large static system prompt (cache_control), exponential-backoff retries, and global
  token/cost accounting. Auto-omits `temperature` for models that reject it (opus-4-8).
- `Embedder.embed(texts)` — OpenAI `text-embedding-3-small` (1536-dim) with a disk cache;
  deterministic hashing fallback if no OpenAI key (memory never hard-fails).

### 2.4 The agent — `agent.py`
- **Grounded bootstrap**: a deterministic first action fetches the real task + credentials +
  profile + app list, so the model starts from real data (the single biggest anti-hallucination win).
- **Planning**: proposes strategies, scores them with the world-model, records the branches.
- **ReAct loop**: think → one python block → execute → observe; full conversation kept,
  observations truncated. Completion is detected via `task_completed()`.
- **System prompt** encodes the hard rules: never fabricate, discover APIs via `api_docs`,
  login via supervisor passwords, paginate fully, gather every named source, match the exact
  answer format, and **verify before** `complete_task`.

### 2.5 Monitor — `monitor.py`  (the observe→decide loop)
After every step it scans the live trajectory and raises signals:
`repeated_error` (≥2 trailing errors), `recurring_error_type`, `action_loop` (repeated code),
`no_progress` (identical observations), `over_exploring` (≥6 doc-only actions), `budget_burn` (≥80% steps).
It maps signals → one intervention by priority: **abort > heal > replan > continue**.

### 2.6 World-model — `world_model.py`  (model-based planning)
`assess(instruction, context, plans)` scores each candidate branch:
```
P(success | plan) = 0.7 · LLM_estimate(plan, context)   # fast model, JSON probabilities
                  + 0.3 · memory_prior(instruction)       # fraction of similar tasks solved
```
Picks `argmax`. The chosen branch's `predicted_success` is later compared to the realized
outcome → the **world-model accuracy / Brier** metric.

### 2.7 Self-healer — `healing.py`
On a monitor `heal`, `plan_recovery(instruction, failed_obs, recent_history)`:
1. `recall_for_error` → how a *similar error* was fixed before (knowledge reuse).
2. LLM diagnoses the **root cause** and proposes 2–3 **distinct** fixes + one concrete guidance.
3. World-model scores the fixes; the best becomes the recommendation.
4. Returns guidance that's injected into the next turn; the recovery is drawn as a red `recovers` edge.
**Escalation:** after 3 repeated heals of the same failure the agent is told to abandon the
approach entirely (different API/app, or finalize with partial results) — breaks heal-loops.

### 2.8 Memory — `memory/`  (knowledge reuse + the HydraDB substrate)
- `Embedder` + a pluggable `VectorStore` (`LocalVectorStore` numpy | `HydraVectorStore`).
- `TrajectoryMemory.index_trajectory(traj)` writes **two** things:
  - **BYOE vectors**: step records (all) + a task record (if solved, with the winning code
    sequence) + the compact graph in metadata → `embeddings.insert` (HydraDB) or numpy.
  - **Managed knowledge graph**: `upload.knowledge` → HydraDB's LLM extracts entities
    (apps/APIs/errors) + relations → a queryable trajectory graph (this is the token-using path).
- Recall: `recall_for_task` (similar solved approaches → injected as lessons),
  `recall_for_error` (similar recoveries), `success_prior` (world-model prior),
  `graph_recall` (graph-aware contextual retrieval via HydraDB).

### 2.9 Metrics, viz, reporting — `metrics.py` / `viz.py` / `report.py` / `insights.py`
- `metrics.aggregate` → the Trajectory Intelligence Benchmark (TGC, recovery rate, planning
  efficiency, world-model accuracy, knowledge-reuse rate).
- `viz` → per-trajectory interactive HTML (vis-network) + Graphviz SVG/DOT.
- `report` → the dashboard; `insights` → cross-run analysis + `run_log.jsonl`.

---

## 3. Key sub-flows

### 3.1 Monitor → intervention
```
after step → observe(traj)
   trailing errors ≥2 ───────────────▶ heal
   same error type twice ────────────▶ heal
   repeated action in window ────────▶ heal
   3 identical observations ─────────▶ replan
   ≥6 doc-only actions ──────────────▶ replan
   steps ≥ 80% budget ───────────────▶ replan
   steps ≥ budget ───────────────────▶ abort
   else ─────────────────────────────▶ continue
```

### 3.2 Heal path
```
heal signal
  └─ consec_heals += 1
       ├─ <3 → recall_for_error → LLM diagnose+fixes → world-model picks best → inject guidance
       └─ ≥3 → ESCALATE: "abandon this approach; different API/app or finalize partial"
  └─ next decision tagged 'recovery'; failed_outcome ──recovers──▶ recovery decision (red edge)
```

### 3.3 Memory write/read + HydraDB dual path
```
end of task ──index_trajectory──┐
                                ├─ BYOE: embeddings.insert(vectors + metadata{graph})  → fast vector recall  (0 tokens)
                                └─ MANAGED: upload.knowledge(text) → entity/relation graph → graph recall (token usage)

before task ──recall_for_task(instruction)──▶ embeddings.search → similar SOLVED approaches ──informs──▶ first decision
on failure  ──recall_for_error(error)──────▶ embeddings.search → similar recoveries ─────────────────▶ heal guidance
```

---

## 3b. v3 scaffold additions (the score-hardening layer)

Layered on the loop above, validated A/B (kept only on no-regression):

- **Subgoal decomposition** — `_plan` now calls `_decompose(task)` to produce an ordered,
  verifiable checklist (login → fetch-all-of-X → filter → act → verify), scored for feasibility by
  the world-model and injected as the `EXECUTION PLAN`. Keeps L2/L3 tasks from skipping a source.
- **Verification gate** — when the agent calls `complete_task`, the loop does NOT break. It injects
  `VERIFICATION_PROMPT`, forcing a re-read + recompute/re-query + fix pass; it finalizes only when the
  agent re-calls `complete_task` (or a small verify-budget elapses). Catches rushed answers and
  partially-done "do X to all Y" tasks.
- **Repair-memory** — `SelfHealer.plan_recovery(..., tried_fixes=[...])` conditions on fixes already
  attempted this task so it proposes a *different* root-cause fix; the agent tracks `tried_fixes` and
  escalates after 3. This broke the 10–16-heal `recurring_error_type` loops.
- **ast pre-guard** — before `execute`, `ast.parse(code)`; if it's prose-echoed-as-code, record the
  error and force a correction without burning an AppWorld interaction (stabilizes error spirals).
- **Step-level procedural recall** — `memory.recall_for_step(situation)` returns the single
  (situation→action) pattern that worked in a similar spot, injected as a `PROCEDURAL HINT` (active
  only with memory). Episodic *and* procedural memory, not just trajectory-level.

```
  decision step:  recall_for_step(situation) ─hint─▶ LLM ─▶ ast.parse guard ─▶ execute
  on failure:     monitor ─heal─▶ healer(tried_fixes) ─▶ (escalate after 3)
  on complete:    complete_task ─▶ VERIFICATION (re-read, recompute/re-query, fix) ─▶ re-complete ─▶ done
```

## 3c. Official harness integration (`solve(world)`)

The `://agent_arena` harness owns the world: `with AppWorld(task_id, experiment_name) as world: solve(world)`.
HELIX plugs in without changing its core:

```
run_task(task_id):  info = env.reset(task_id)   # we create the world (our runner)
solve(world):       info = env.attach(world)    # harness created it; we attach (don't own its lifecycle)
both ──▶ _run(info)  # identical trajectory-intelligence loop
```

`env.attach(world)` wraps the given world (and `close()` won't free a world we don't own). Because
`solve()` never calls `index_trajectory`, memory is **recall-only on the test split → no
ground-truth leakage**. `hack_agent_arena/agent.py` is the drop-in submission entry.

## 4. Applications (beyond the AppWorld score)

HELIX is really a **trajectory-intelligence layer** that wraps *any* tool-using agent. The
AppWorld agent is one instantiation. The reusable capabilities:

1. **Self-healing production agents** — drop the Monitor + Healer around any agent so it
   detects loops/failures live and recovers instead of silently failing.
2. **Agent observability / "Datadog for agents"** — every run is an explainable graph with
   per-step cost/latency/error and the exact code+observation; the dashboard + INSIGHTS give
   failure patterns, calibration, and cost analytics across runs.
3. **Continual learning from experience** — the memory turns solved runs into reusable
   approaches; later tasks recall them (+18pp solve-rate in our ablation). This is "learn from
   trajectories, not tokens."
4. **Model-based planning / risk control** — the world-model predicts P(success) per branch
   before acting, and gates irreversible actions (payments, sends) behind higher confidence.
5. **Regression & evaluation harness** — run a split, get the Trajectory Intelligence
   Benchmark + ablations; compare agents/models/prompts on the same tasks.
6. **A trajectory knowledge graph** (HydraDB) — query "how were tasks like X solved, what
   errors occurred, which apps/APIs are involved" across all past runs.

In short: an **operating system for autonomous intelligence** — observe (what happened),
explain (why), predict (what will happen), heal (fix it live), and improve (reuse) — with the
trajectory graph as the universal substrate.
