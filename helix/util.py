"""Small shared helpers."""
from __future__ import annotations

import json
import re
import time as _time

# AppWorld freezes the clock with freezegun (tick=False) during a task, which
# zeroes time.time()/perf_counter/monotonic. We capture the real perf_counter at
# import time and hide it inside a list so freezegun's module-attribute scanner
# cannot swap it for a fake. real_clock() therefore returns true elapsed time
# even inside a frozen task - needed for honest latency/wall-time metrics.
_REAL_CLOCK_HOLDER = [_time.perf_counter]


def real_clock() -> float:
    return _REAL_CLOCK_HOLDER[0]()


def extract_json(text: str):
    """Best-effort extraction of the first JSON object/array from model text."""
    if not text:
        return None
    fenced = re.search(r"```(?:json)?\s*(.+?)```", text, re.DOTALL)
    if fenced:
        text = fenced.group(1)
    # try direct
    try:
        return json.loads(text.strip())
    except Exception:
        pass
    # try to find a balanced {...} or [...]
    for open_c, close_c in (("{", "}"), ("[", "]")):
        start = text.find(open_c)
        if start == -1:
            continue
        depth = 0
        for i in range(start, len(text)):
            if text[i] == open_c:
                depth += 1
            elif text[i] == close_c:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except Exception:
                        break
    return None


def extract_code(text: str) -> str | None:
    """Extract a python code block from a model message (ReAct action)."""
    if not text:
        return None
    blocks = re.findall(r"```(?:python|py)?\s*\n(.*?)```", text, re.DOTALL)
    if blocks:
        # last non-empty block
        for b in reversed(blocks):
            if b.strip():
                return b.strip()
    return None


def trim(s: str, n: int) -> str:
    s = (s or "").strip()
    return (s[: n] + f" ...[+{len(s) - n}]") if len(s) > n else s
