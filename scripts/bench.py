"""Robust HELIX entrypoint (handles Windows UTF-8 mode via self-re-exec).

Equivalent to `python -m helix.run ...` but safe even when PYTHONUTF8 is unset.

Usage: .venv\\Scripts\\python.exe scripts\\bench.py --split dev --limit 5
"""
import sys

from helix.win_compat import ensure_utf8_mode

ensure_utf8_mode()

from helix.run import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
