"""AppWorld environment adapter.

Wraps the in-process AppWorld world and turns the raw ``execute`` string into a
structured :class:`Observation` (status / error-type / latency / api-call count)
that the trajectory recorder and monitor can reason over.

Two Windows requirements are baked in here:
  * ``timeout_seconds=None``  -> avoids the Unix-only SIGALRM timeout path.
  * the process must run in UTF-8 mode (see :func:`helix.win_compat.ensure_utf8_mode`)
    so AppWorld's report writer doesn't choke on unicode.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from appworld import AppWorld, load_task_ids

from .util import real_clock

_ERROR_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_.]*(?:Error|Exception|Warning))\b\s*:?(.*)$")
_FAILED_PREFIX = "Execution failed. Traceback:"


@dataclass
class Observation:
    raw: str
    status: str = "ok"            # ok | error | empty
    error_type: str | None = None
    error_message: str = ""
    latency_s: float = 0.0
    num_api_calls: int = 0
    code: str = ""

    @property
    def is_error(self) -> bool:
        return self.status == "error"

    def digest(self, limit: int = 1200) -> str:
        r = self.raw.strip()
        return (r[:limit] + f"\n...[+{len(r) - limit} chars]") if len(r) > limit else r


def parse_observation(raw: str, code: str, latency_s: float) -> Observation:
    text = (raw or "").strip()
    num_calls = len(re.findall(r"\bapis\.\w+\.\w+\(", code))
    if text.startswith(_FAILED_PREFIX):
        etype, emsg = _extract_error(text)
        return Observation(raw=raw, status="error", error_type=etype,
                           error_message=emsg, latency_s=latency_s,
                           num_api_calls=num_calls, code=code)
    if not text or text == "Execution successful.":
        return Observation(raw=raw or "Execution successful.", status="empty",
                           latency_s=latency_s, num_api_calls=num_calls, code=code)
    return Observation(raw=raw, status="ok", latency_s=latency_s,
                       num_api_calls=num_calls, code=code)


def _extract_error(traceback_text: str) -> tuple[str, str]:
    for line in reversed(traceback_text.strip().splitlines()):
        m = _ERROR_RE.match(line.strip())
        if m:
            return m.group(1), m.group(2).strip()
    return "Error", traceback_text.strip().splitlines()[-1] if traceback_text.strip() else ""


class AppWorldEnvironment:
    """Drives a single AppWorld task at a time for an experiment."""

    def __init__(self, experiment_name: str = "helix"):
        self.experiment_name = experiment_name
        self.world: AppWorld | None = None
        self.task_id: str | None = None
        self._owns_world = False

    # -- lifecycle --------------------------------------------------------- #
    def _world_info(self) -> dict:
        sup = self.world.task.supervisor
        return {
            "task_id": self.task_id,
            "instruction": self.world.task.instruction,
            "supervisor": {
                "first_name": sup.first_name,
                "last_name": sup.last_name,
                "email": sup.email,
                "phone_number": sup.phone_number,
            },
            "allowed_apps": list(self.world.task.allowed_apps),
            "datetime": str(self.world.task.datetime),
        }

    def reset(self, task_id: str) -> dict:
        self.close()
        self.task_id = task_id
        self.world = AppWorld(
            task_id=task_id,
            experiment_name=self.experiment_name,
            timeout_seconds=None,        # Windows: avoid SIGALRM
        )
        self._owns_world = True
        return self._world_info()

    def attach(self, world) -> dict:
        """Wrap an EXISTING AppWorld world (e.g. created by the official harness's
        `with AppWorld(...) as world:`). We do not own its lifecycle."""
        self.close()
        self.world = world
        self.task_id = getattr(world, "task_id", None)
        self._owns_world = False
        return self._world_info()

    def close(self) -> None:
        if self.world is not None and self._owns_world:
            try:
                self.world.close()
            except Exception:
                pass
        self.world = None
        self._owns_world = False

    # -- interaction ------------------------------------------------------- #
    def execute(self, code: str) -> Observation:
        assert self.world is not None, "call reset() first"
        t0 = real_clock()  # real_clock: AppWorld freezes time.time()/perf_counter via freezegun
        raw = self.world.execute(code)
        return parse_observation(raw, code, round(real_clock() - t0, 3))

    def completed(self) -> bool:
        assert self.world is not None
        try:
            return bool(self.world.task_completed())
        except Exception:
            return False

    def evaluate(self) -> dict:
        assert self.world is not None
        try:
            tracker = self.world.evaluate(suppress_errors=True)
            d = tracker.to_dict(stats_only=True)
            d["success"] = bool(tracker.success)
            return d
        except Exception as e:  # noqa: BLE001
            return {"success": False, "error": str(e)}

    # -- prompt helpers ---------------------------------------------------- #
    def supervisor_line(self, info: dict) -> str:
        s = info["supervisor"]
        return (f"{s['first_name']} {s['last_name']} "
                f"(email: {s['email']}, phone: {s['phone_number']})")


def list_task_ids(split: str, limit: int | None = None) -> list[str]:
    ids = load_task_ids(split)
    return ids[:limit] if limit else list(ids)
