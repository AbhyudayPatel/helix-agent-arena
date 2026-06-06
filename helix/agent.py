"""HelixAgent - trajectory-aware, self-healing AppWorld agent.

A ReAct code agent (think -> python -> observe -> repeat) wrapped in the
trajectory-intelligence loop:

  * every step is recorded as State -> Decision -> Action -> Outcome in a graph
  * before the task, similar SOLVED trajectories are recalled and injected
  * at planning, the world-model scores candidate strategies and picks the best
  * after every step, the monitor inspects the live trajectory and may trigger
    HEAL (diagnose + recover) or REPLAN (commit to progress)
  * the chosen recovery is recorded with a `recovers` edge

All intelligence layers are optional; with them off this is a strong plain
ReAct agent.
"""
from __future__ import annotations

import ast
import types

from .config import CONFIG
from .llm import GLOBAL_USAGE, ClaudeLLM
from .monitor import TrajectoryMonitor
from .trajectory import Trajectory
from .util import extract_code, extract_json, trim

SYSTEM_PROMPT = """You are a meticulous, autonomous AI assistant that completes day-to-day digital tasks for your supervisor by operating real apps (spotify, gmail, venmo, amazon, todoist, splitwise, phone, file_system, simple_note) entirely on their behalf, through a stateful Python REPL.

Each turn: write a SHORT reasoning line, then EXACTLY ONE ```python``` block. The environment runs it and returns the printed output. Variables persist across turns. Keep going until the task is fully VERIFIED and finalized.

`apis` is available. Pre-imported: json, re, math, random, datetime, calendar, itertools, Counter, defaultdict, deepcopy, reduce, pendulum, and Date/DateTime/Time.

== NEVER FABRICATE ==
Never invent passwords, tokens, ids, names, numbers, dates, or answers. Every value must come from a real API response you printed. You have NOT seen this user's data - never imagine or predict an API's output. Work ONE step at a time; if a call fails, read the error and fix it - do not guess. Each block must make real apis.* calls or compute over already-printed data; never write prose as code.

== OPENING (you are already shown the real task, passwords, profile, and app list) ==
Use the passwords from show_account_passwords (never guess). Log in to each app you need with the supervisor's email or phone (check the login doc) and keep the returned access_token.

== DISCOVER APIS BEFORE USING THEM ==
Never guess an API name or its parameters. For each app you need:
  print(apis.api_docs.show_api_descriptions(app_name='venmo'))            # list its APIs
  print(apis.api_docs.show_api_doc(app_name='venmo', api_name='...'))     # FULL signature BEFORE the first call
Match parameter names/types EXACTLY. Read the response schema so you know which fields you'll get back. apis.api_docs.search_api_docs(query=...) helps find the right API.

== COLLECT COMPLETELY, COMPUTE IN CODE ==
- List APIs paginate (page_index/page_limit). LOOP until a page returns fewer than page_limit; gather EVERYTHING before computing. Print len() to confirm.
- Gather EVERY source the task names ("across songs, albums AND playlists" -> all three; "received payments" -> all of them).
- Do the logic in Python (filter/sort/sum/argmax/dedupe) over the FULL data. Don't eyeball, and don't print huge dumps - keep data in variables and print concise results/counts.
- For UNIQUE counts/lists, dedupe by a STABLE unique id (e.g. song_id), NEVER by display name/title: the same item can appear in several sources and different items can share a name. "Unique songs across X, Y, Z" = the count of DISTINCT ids pooled from all of X, Y and Z.

== ENTITIES & RELATIONSHIPS ==
"My roommates / coworkers / siblings / friends / family / spouse" are defined by the relationship field of contacts in the PHONE app. Resolve the people first (phone contacts -> their names/emails/phones), then map each to the relevant app account by matching name/email/phone. Never assume who is who.

== DATES & TIMES ==
"today / now / yesterday / last N days / this/last year" are relative to the environment's datetime (shown to you). Compute exact ranges with pendulum/Date and filter precisely (mind inclusive vs exclusive bounds).

== ACTION TASKS ("do X to ALL Y") ==
Apply the change to ALL items matching the filter and to NO others. Collect all candidates (paginate) -> filter precisely -> for EACH, check current state first to stay idempotent (don't double-like/comment/rate) -> perform the action -> keep a list of exactly what you changed. Missing one item, or touching a non-matching one, fails the task.

== ANSWERS ==
If the task asks a question, the answer must be exact and concise (a number / name / yes-no / list). For a list, join items with ', ' in the requested order, using the EXACT stored strings (no paraphrase/re-casing). Submit via apis.supervisor.complete_task(answer=...). For a pure action task with no question, use complete_task(status="success").

== FINISH = VERIFY, THEN AN API CALL ==
Completion is the API call complete_task(...) - saying "done" in text does nothing. Before finalizing, VERIFY: re-read apis.supervisor.show_active_task(), then re-derive the answer (or re-query the affected app state) and confirm EVERY requirement - which sources, the metric, the count, the order, the exact format, and for action tasks that ALL-and-ONLY the right items were changed with no duplicates. Fix anything wrong, then call complete_task.

Other rules: one ```python``` block per turn, valid Python only, always print what you need to inspect, and double-check inputs before irreversible actions (payments / sends / deletes)."""

VERIFICATION_PROMPT = (
    "\n\n[VERIFICATION REQUIRED - do NOT stop yet] You called complete_task. Before this is "
    "accepted, rigorously verify in code:\n"
    "1. Re-read the exact task: print(apis.supervisor.show_active_task()).\n"
    "2. QUESTION tasks: recompute the answer from the real data and confirm it matches EXACTLY "
    "in value, units, count, ordering, and format.\n"
    "3. ACTION tasks: re-query the affected app state and confirm EVERY required change was applied "
    "to ALL and ONLY the correct items (none missed, none extra, no duplicates).\n"
    "Print what you checked. If everything is correct, call apis.supervisor.complete_task(...) again "
    "with the SAME answer to confirm (do NOT change a correct answer). If you find ANY concrete error, "
    "FIX it (do the missing/incorrect actions or correct the answer), then call complete_task again."
)


# Deterministic grounded opening: fetch the real task, credentials, profile and
# app list so the model starts from real data and cannot "solve it in its head".
BOOTSTRAP_CODE = (
    "print('=== ACTIVE TASK ==='); print(apis.supervisor.show_active_task())\n"
    "print('=== ACCOUNT PASSWORDS (use these, never guess) ==='); "
    "print(apis.supervisor.show_account_passwords())\n"
    "print('=== YOUR (SUPERVISOR) PROFILE ==='); print(apis.supervisor.show_profile())\n"
    "print('=== AVAILABLE APPS ==='); print(apis.api_docs.show_app_descriptions())"
)


def split_thought_code(text: str) -> tuple[str, str | None]:
    code = extract_code(text)
    thought = text
    if code:
        # remove fenced blocks from the thought
        import re
        thought = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return thought.strip(), code


class HelixAgent:
    def __init__(self, env, *, memory=None, world_model=None, healer=None,
                 monitor: TrajectoryMonitor | None = None, model: str | None = None,
                 max_steps: int | None = None, verbose: bool = True,
                 bootstrap: bool = True, verify: bool = True, verify_budget: int = 6):
        self.env = env
        self.llm = ClaudeLLM(model=model or CONFIG.agent_model,
                             max_tokens=CONFIG.max_tokens_per_call)
        self.memory = memory
        self.world_model = world_model
        self.healer = healer
        self.max_steps = max_steps or CONFIG.max_steps
        self.monitor = monitor or TrajectoryMonitor(self.max_steps)
        self.verbose = verbose
        self.bootstrap = bootstrap
        self.verify = verify
        self.verify_budget = verify_budget

    def _log(self, *a):
        if self.verbose:
            print("[agent]", *a)

    # --------------------------------------------------------------------- #
    def run_task(self, task_id: str, split: str = "", experiment: str = "helix") -> Trajectory:
        """Create a fresh AppWorld world for task_id and solve it (our runner)."""
        info = self.env.reset(task_id)
        return self._run(info, split, experiment)

    def solve(self, world, split: str = "", experiment: str = "helix") -> Trajectory:
        """Drive an EXISTING AppWorld world - the official hackathon harness
        passes us a live `world` object; we attach to it instead of creating one."""
        info = self.env.attach(world)
        return self._run(info, split, experiment)

    def _run(self, info: dict, split: str = "", experiment: str = "helix") -> Trajectory:
        task_id = info["task_id"]
        sup = self.env.supervisor_line(info)
        traj = Trajectory(task_id, info["instruction"], split, experiment,
                          supervisor=sup, allowed_apps=info["allowed_apps"])
        usage0 = GLOBAL_USAGE.snapshot()
        self._log(f"task {task_id}: {trim(info['instruction'], 100)}")

        s0 = traj.add_state("Task received", step=0, status="start",
                            instruction=info["instruction"], supervisor=sup,
                            apps=info["allowed_apps"])

        # ---- retrieval-augmented context (memory) ----
        task_lessons, mem_node_ids = "", []
        if self.memory is not None:
            try:
                hits = self.memory.recall_for_task(info["instruction"], k=3)
                task_lessons = self.memory.task_lessons(hits)
                for h in hits:
                    mid = traj.add_memory(f"sim={h.score:.2f} {trim(h.payload.get('instruction',''),40)}",
                                          step=0, score=h.score, payload=h.payload)
                    mem_node_ids.append(mid)
            except Exception as e:  # noqa: BLE001
                self._log("memory recall failed:", e)

        # ---- world-model planning ----
        plan_block, plan_decision_id = self._plan(traj, info, s0)

        messages = [{"role": "user", "content": self._initial_user(info, task_lessons, plan_block)}]
        prev_state = s0
        last_digest = "(start)"
        pending_recovery = None
        recover_from = None
        consec_heals = 0
        tried_fixes: list[dict] = []
        verifying = False
        verify_start = -1
        verify_deadline = 0
        step = 0

        # deterministic grounded opening
        if self.bootstrap:
            prev_state, a_msg, u_msg, last_digest = self._do_bootstrap(traj, s0)
            messages.append({"role": "assistant", "content": a_msg})
            messages.append({"role": "user", "content": u_msg})
            step = 1

        linked_memory = False
        while step < self.max_steps:
            step += 1
            res = self.llm.complete(SYSTEM_PROMPT, messages)
            thought, code = split_thought_code(res.text)

            dec = traj.add_decision(trim(thought, 60) or "act", step,
                                    thought=thought, context=last_digest,
                                    cost_usd=res.cost_usd, model=res.model)
            traj.link(prev_state, dec, "decides")
            if not linked_memory and mem_node_ids:
                for mid in mem_node_ids:
                    traj.link(mid, dec, "informs")
                linked_memory = True
            if pending_recovery is not None:
                d = traj.node(dec)
                d.status = "recovery"
                d.data["diagnosis"] = pending_recovery.diagnosis
                if pending_recovery.predicted_success is not None:
                    d.data["predicted_success"] = pending_recovery.predicted_success
                if recover_from is not None:
                    traj.link(recover_from, dec, "recovers")
                pending_recovery, recover_from = None, None

            if not code:
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content":
                    "Please respond with your reasoning line followed by EXACTLY ONE "
                    "```python``` code block. If the task is complete, call "
                    "apis.supervisor.complete_task(...) in that block."})
                continue

            # pre-execution guard: reject non-Python (prose echoed as code) without
            # burning an AppWorld interaction, and force a crisp correction. This
            # stabilizes the agent when it degrades into syntax-error loops.
            try:
                ast.parse(code)
            except SyntaxError as se:
                act = traj.add_action(code, step)
                traj.link(dec, act, "acts")
                out = traj.add_outcome("error: SyntaxError", step, status="error",
                                       error_type="SyntaxError", digest=str(se.msg),
                                       raw=str(se), latency_s=0.0, num_api_calls=0,
                                       cost_usd=0.0)
                traj.link(act, out, "yields")
                ns = traj.add_state(f"S{step}: syntax error", step, status="error")
                traj.link(out, ns, "transitions")
                prev_state = ns
                messages.append({"role": "assistant", "content": res.text})
                messages.append({"role": "user", "content":
                    f"That was NOT valid Python (SyntaxError: {se.msg}). A code block must "
                    "contain ONLY executable Python - never prose, observation text, or "
                    "markdown. Re-emit exactly ONE corrected ```python``` block."})
                continue

            act = traj.add_action(code, step)
            traj.link(dec, act, "acts")
            obs = self.env.execute(code)
            out = traj.add_outcome(
                self._outcome_label(obs), step, status=obs.status,
                digest=obs.digest(), raw=trim(obs.raw, 2000),
                error_type=obs.error_type, latency_s=obs.latency_s,
                num_api_calls=obs.num_api_calls, cost_usd=0.0)
            traj.link(act, out, "yields")

            # world-model accuracy bookkeeping for recovery decisions
            d = traj.node(dec)
            if "predicted_success" in d.data:
                d.data["actual_success"] = 0 if obs.is_error else 1

            new_state = traj.add_state(self._state_label(obs, step), step,
                                       status=("error" if obs.is_error else "neutral"))
            traj.link(out, new_state, "transitions")
            prev_state = new_state
            last_digest = obs.digest(400)
            if not obs.is_error:
                consec_heals = 0  # progress made; reset the heal-escalation counter

            messages.append({"role": "assistant", "content": res.text})
            next_user = self._observation_user(obs)

            # ---- monitor: observe the live trajectory and decide ----
            report = self.monitor.observe(traj)
            traj.node(out).data["signals"] = report.signals
            if self.verbose and report.signals:
                self._log(f"step {step} signals={report.signals} -> {report.intervention}")

            if report.intervention == "heal" and self.healer is not None:
                consec_heals += 1
                recover_from = out
                if consec_heals >= 3:
                    # repeated heals of the same failure aren't working -> escalate
                    # (skip the healer LLM call, force a fundamentally different path)
                    pending_recovery = types.SimpleNamespace(
                        diagnosis=f"escalation after {consec_heals} failed heals",
                        predicted_success=None)
                    next_user += self._escalation_block(consec_heals)
                else:
                    rec = self.healer.plan_recovery(info["instruction"], obs,
                                                    self._recent_history(traj),
                                                    tried_fixes=tried_fixes)
                    pending_recovery = rec
                    if rec.chosen:
                        tried_fixes.append({"error_type": obs.error_type, "fix": rec.chosen})
                    next_user += self._heal_block(rec)
            elif report.intervention == "replan":
                next_user += f"\n\n[MONITOR] {report.message}"
            elif report.intervention == "abort":
                next_user += (f"\n\n[MONITOR] {report.message} You MUST call "
                              "apis.supervisor.complete_task(...) now with your best answer.")

            # procedural memory: hint the action pattern that worked in a similar spot
            if self.memory is not None and not obs.is_error and not verifying:
                try:
                    hh = self.memory.recall_for_step(info["instruction"], last_digest, k=2)
                    hint = self.memory.step_hints(hh)
                    if hint:
                        next_user += "\n\n" + hint
                except Exception:
                    pass

            # ---- completion + mandatory verification gate ----
            completed = self.env.completed()
            called_complete = "complete_task" in (code or "")
            if completed and self.verify and not verifying and (self.max_steps - step) > 2:
                # first completion: force one verification pass before finalizing
                verifying = True
                verify_start = step
                verify_deadline = step + self.verify_budget
                next_user += VERIFICATION_PROMPT
                self._log(f"complete_task at step {step}; entering verification")
            messages.append({"role": "user", "content": next_user})

            if completed and not self.verify:
                self._log(f"task_completed() at step {step}")
                break
            if verifying and step > verify_start and (called_complete or step >= verify_deadline):
                self._log(f"verified & finalized at step {step}")
                break

        # ---- finalize ----
        evaluation = self.env.evaluate()
        usage1 = GLOBAL_USAGE.snapshot()
        usage = {k: usage1[k] - usage0.get(k, 0) for k in usage1
                 if isinstance(usage1[k], (int, float))}
        traj.finalize(evaluation, usage=usage)
        if plan_decision_id is not None:
            pd = traj.node(plan_decision_id)
            if pd is not None:
                pd.data["actual_success"] = 1 if traj.solved else 0
        self._log(f"done: solved={traj.solved} steps={traj.num_steps} "
                  f"errors={traj.num_errors} recoveries={traj.num_recoveries} "
                  f"cost=${traj.total_cost}")
        return traj

    # ----- bootstrap ------------------------------------------------------ #
    def _do_bootstrap(self, traj, s0):
        dec = traj.add_decision("Bootstrap: ground in real account data", step=1,
                                thought="deterministic grounding of task, credentials, profile, apps",
                                context="(start)")
        traj.link(s0, dec, "decides")
        act = traj.add_action(BOOTSTRAP_CODE, step=1, label="bootstrap discovery")
        traj.link(dec, act, "acts")
        obs = self.env.execute(BOOTSTRAP_CODE)
        out = traj.add_outcome(self._outcome_label(obs), step=1, status=obs.status,
                               digest=obs.digest(), raw=trim(obs.raw, 2500),
                               error_type=obs.error_type, latency_s=obs.latency_s,
                               num_api_calls=obs.num_api_calls, cost_usd=0.0)
        traj.link(act, out, "yields")
        new_state = traj.add_state("S1: grounded", step=1,
                                   status=("error" if obs.is_error else "neutral"))
        traj.link(out, new_state, "transitions")
        a_msg = ("I'll first ground myself in the real account data (task, credentials, "
                 f"profile, available apps).\n```python\n{BOOTSTRAP_CODE}\n```")
        return new_state, a_msg, self._observation_user(obs), obs.digest(400)

    # ----- planning ------------------------------------------------------- #
    def _plan(self, traj, info, s0):
        """Decompose the task into an ordered subgoal checklist (HTN-lite) and score
        its feasibility with the world-model. The checklist is injected into context
        and tracked, so the agent doesn't skip a source/step on multi-goal L2/L3 tasks."""
        if self.world_model is None:
            return "", None
        subgoals = self._decompose(info)
        if not subgoals:
            return "", None
        d0 = traj.add_decision("Plan: decompose into subgoals", step=0,
                               thought="task decomposition + feasibility",
                               context="(start)")
        traj.link(s0, d0, "decides")
        plan_text = " -> ".join(subgoals)
        try:
            assessment = self.world_model.assess(info["instruction"], "(start)", [plan_text])
        except Exception:
            assessment = None
        if assessment and assessment.branches:
            b = assessment.branches[0]
            pid = traj.add_prediction(f"P={b.p_success:.2f} plan", step=0,
                                      p_success=b.p_success, plan=plan_text,
                                      rationale=b.rationale, source=b.source)
            traj.link(d0, pid, "predicts")
            traj.node(d0).data["predicted_success"] = b.p_success
        traj.node(d0).data["subgoals"] = subgoals
        block = ("EXECUTION PLAN - complete these subgoals IN ORDER, and confirm each is "
                 "actually done before moving to the next (never skip a source or step):\n"
                 + "\n".join(f"{i + 1}. {g}" for i, g in enumerate(subgoals)))
        return block, d0

    def _decompose(self, info) -> list[str]:
        sys = ("Decompose the AppWorld task into a SHORT ordered checklist of concrete, "
               "verifiable subgoals (e.g. log in to app X, fetch all of Y paginated, filter "
               "by Z, compute/act, verify). Be specific about which apps/sources/fields are "
               "involved. 3-8 items. Return ONLY JSON: {\"subgoals\":[\"...\"]}.")
        user = f"TASK: {info['instruction']}\nApps: {info['allowed_apps']}"
        try:
            res = self.llm.complete(sys, [{"role": "user", "content": user}], max_tokens=500)
            data = extract_json(res.text) or {}
            return [str(s)[:200] for s in data.get("subgoals", []) if str(s).strip()][:8]
        except Exception:
            return []

    # ----- prompt fragments ---------------------------------------------- #
    def _initial_user(self, info, task_lessons, plan_block) -> str:
        parts = [
            f"You are completing this task for {self.env.supervisor_line(info)}.",
            f"Environment date-time: {info['datetime']}.",
            f"\nTASK:\n{info['instruction']}",
            f"\nApps available (call via apis.<app>.<api>): {info['allowed_apps']}",
            "You have NOT seen the API signatures yet - discover them with apis.api_docs before calling.",
        ]
        if task_lessons:
            parts.append("\n" + task_lessons)
        if plan_block:
            parts.append("\n" + plan_block)
        parts.append("\nBegin. Think briefly, then output your first python code block.")
        return "\n".join(parts)

    @staticmethod
    def _observation_user(obs) -> str:
        head = "Execution output:" if not obs.is_error else "Execution FAILED:"
        # wider window so the agent can actually read fetched API docs / schemas
        return f"{head}\n```\n{obs.digest(2200)}\n```\nContinue with your next single python code block."

    @staticmethod
    def _heal_block(rec) -> str:
        out = ["\n\n[SELF-HEAL] The monitor detected repeated failure/loop."]
        if rec.diagnosis:
            out.append(f"Root-cause diagnosis: {rec.diagnosis}")
        if rec.chosen:
            out.append(f"Recommended fix: {rec.chosen}")
        if rec.guidance:
            out.append(f"Do this next: {rec.guidance}")
        if rec.lessons_text:
            out.append(rec.lessons_text)
        out.append("Change your approach accordingly; do not repeat the failing call.")
        return "\n".join(out)

    @staticmethod
    def _escalation_block(n: int) -> str:
        return ("\n\n[SELF-HEAL ESCALATION] You have tried to fix this same failure "
                f"{n} times without success. STOP this approach entirely. Either (a) "
                "achieve the goal a COMPLETELY different way (a different API/app/field), "
                "or (b) if this sub-goal is optional or is blocking the rest of the task, "
                "skip it, finish the other parts, and call complete_task with your best "
                "result. Do NOT repeat the failing call again.")

    @staticmethod
    def _outcome_label(obs) -> str:
        if obs.is_error:
            return f"error: {obs.error_type}"
        if obs.status == "empty":
            return "ok (no output)"
        return trim(obs.raw, 40)

    @staticmethod
    def _state_label(obs, step) -> str:
        return f"S{step}: {'error' if obs.is_error else 'progressed'}"

    @staticmethod
    def _recent_history(traj, n: int = 6) -> str:
        actions = traj.nodes_of("action")[-n:]
        a2o = {e.src: e.dst for e in traj.edges if e.relation == "yields"}
        lines = []
        for a in actions:
            o = traj.node(a2o.get(a.id))
            lines.append(f"CODE:\n{a.data.get('code','')}\nOUT: {trim(o.label if o else '', 120)}")
        return "\n---\n".join(lines)
