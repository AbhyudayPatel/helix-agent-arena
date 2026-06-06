"""TrajectoryMonitor - real-time observe -> decide loop.

After every step the monitor reads the *live* trajectory and emits signals plus a
recommended intervention. The agent consults this each turn and changes course
(heal / replan / abort) accordingly. This is the closed loop that makes the
trajectory actionable rather than merely observable.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# thresholds
MAX_CONSECUTIVE_ERRORS = 2
LOOP_WINDOW = 4
NO_PROGRESS_WINDOW = 3
# The expert prompt mandates reading full API docs before use, so a run of
# doc-reads early on is HEALTHY. Only flag genuinely excessive doc-spelunking.
DOC_STREAK_LIMIT = 10
BUDGET_WARN_FRACTION = 0.8

INTERVENTION_PRIORITY = ["abort", "heal", "replan", "continue"]


@dataclass
class MonitorReport:
    signals: list[str] = field(default_factory=list)
    intervention: str = "continue"
    message: str = ""
    details: dict = field(default_factory=dict)

    @property
    def needs_action(self) -> bool:
        return self.intervention in ("heal", "replan", "abort")


def _norm_code(code: str) -> str:
    return re.sub(r"\s+", " ", (code or "").strip()).lower()


class TrajectoryMonitor:
    def __init__(self, max_steps: int):
        self.max_steps = max_steps

    def observe(self, traj) -> MonitorReport:
        outcomes = traj.nodes_of("outcome")
        actions = traj.nodes_of("action")
        signals: list[str] = []
        details: dict = {}

        # 1. trailing consecutive errors
        trailing_errors = 0
        for o in reversed(outcomes):
            if o.status == "error":
                trailing_errors += 1
            else:
                break
        if trailing_errors >= MAX_CONSECUTIVE_ERRORS:
            signals.append("repeated_error")
            details["trailing_errors"] = trailing_errors

        # 2. same error type repeating
        err_types = [o.data.get("error_type") for o in outcomes if o.status == "error"]
        if len(err_types) >= 2 and err_types[-1] and err_types[-1] == err_types[-2]:
            signals.append("recurring_error_type")
            details["error_type"] = err_types[-1]

        # 3. action loop (same normalized code seen recently)
        recent_codes = [_norm_code(a.data.get("code", "")) for a in actions[-LOOP_WINDOW:]]
        if recent_codes and len(recent_codes) != len(set(recent_codes)):
            signals.append("action_loop")
            details["loop_window"] = LOOP_WINDOW

        # 4. no progress (repeated identical observations / all-empty)
        recent_obs = [(o.data.get("digest") or o.label) for o in outcomes[-NO_PROGRESS_WINDOW:]]
        if len(recent_obs) >= NO_PROGRESS_WINDOW and len(set(recent_obs)) == 1:
            signals.append("no_progress")

        # 5. stuck exploring docs without acting on a real app
        doc_streak = 0
        for a in reversed(actions):
            code = a.data.get("code", "")
            if "apis.api_docs" in code or re.search(r"apis\.supervisor\.show", code):
                doc_streak += 1
            else:
                break
        if doc_streak >= DOC_STREAK_LIMIT:
            signals.append("over_exploring")
            details["doc_streak"] = doc_streak

        # 6. budget burn
        frac = traj.num_steps / max(1, self.max_steps)
        if frac >= BUDGET_WARN_FRACTION:
            signals.append("budget_burn")
            details["step_fraction"] = round(frac, 2)

        intervention, message = self._decide(signals, traj)
        return MonitorReport(signals=signals, intervention=intervention,
                             message=message, details=details)

    def _decide(self, signals: list[str], traj) -> tuple[str, str]:
        if traj.num_steps >= self.max_steps:
            return "abort", "Step budget exhausted; finalize with best-effort answer."
        if "repeated_error" in signals or "recurring_error_type" in signals or "action_loop" in signals:
            return "heal", ("Detected repeated failure/loop. Stop retrying the same "
                            "approach; diagnose root cause and try a different API/path.")
        if "no_progress" in signals or "over_exploring" in signals:
            return "replan", ("No progress detected. Re-plan: commit to a concrete app "
                              "action that advances the task instead of more exploration.")
        if "budget_burn" in signals:
            return "replan", ("Running low on steps. Prioritize the remaining required "
                              "sub-goals and move to complete_task.")
        return "continue", ""
