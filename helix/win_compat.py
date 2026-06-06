"""Windows compatibility shims for AppWorld.

AppWorld is developed on Unix and has two hard edges on Windows that we hit
during bring-up:

1. ``signal.SIGALRM`` based execution timeouts -> we always construct AppWorld
   with ``timeout_seconds=None`` (see :mod:`helix.appworld_env`).
2. Report files are written with the OS default codec (cp1252 on Windows),
   which blows up on the unicode in evaluation reports -> we run the
   interpreter in UTF-8 mode.

``ensure_utf8_mode`` makes (2) self-healing: if the process was not started in
UTF-8 mode, it re-execs itself with ``-X utf8`` so callers never have to
remember to set ``PYTHONUTF8``.
"""
from __future__ import annotations

import os
import sys


def ensure_utf8_mode() -> None:
    """Re-exec the interpreter in UTF-8 mode on Windows if needed."""
    if not sys.platform.startswith("win"):
        return
    if os.environ.get("PYTHONUTF8") == "1" or sys.flags.utf8_mode:
        return
    os.environ["PYTHONUTF8"] = "1"
    os.environ["PYTHONIOENCODING"] = "utf-8"
    try:
        os.execv(sys.executable, [sys.executable, "-X", "utf8", *sys.argv])
    except Exception:  # pragma: no cover - fall back to best-effort stdio reconfig
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass
