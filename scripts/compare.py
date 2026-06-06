"""Fair ablation comparison between two experiments (full-stack vs plain ReAct).

Compares on the INTERSECTION of task ids present in both experiments'
summaries.json, so it's a true head-to-head. Writes reports/comparison.html and
prints a markdown table.

Usage: .venv\\Scripts\\python.exe scripts\\compare.py [full_exp] [plain_exp]
"""
import json
import sys
from pathlib import Path

from helix.win_compat import ensure_utf8_mode

ensure_utf8_mode()

from helix.config import REPORTS_DIR  # noqa: E402


def load_summaries(exp: str) -> dict:
    p = Path(REPORTS_DIR) / exp / "summaries.json"
    rows = json.loads(p.read_text(encoding="utf-8"))
    return {r["task_id"]: r for r in rows}


def agg(rows: list[dict]) -> dict:
    n = len(rows)
    if not n:
        return {"n": 0}
    solved = sum(1 for r in rows if r.get("solved"))
    steps = sum(r.get("num_steps", 0) for r in rows)
    errors = sum(r.get("num_errors", 0) for r in rows)
    recov = sum(r.get("num_recoveries", 0) for r in rows)
    cost = sum(r.get("total_cost_usd", 0) or 0 for r in rows)
    return {
        "n": n,
        "tgc_pct": round(100 * solved / n, 1),
        "solved": solved,
        "avg_steps": round(steps / n, 2),
        "avg_errors": round(errors / n, 2),
        "recoveries": recov,
        "avg_cost_usd": round(cost / n, 4),
    }


def main() -> int:
    full = sys.argv[1] if len(sys.argv) > 1 else "dev_final"
    plain = sys.argv[2] if len(sys.argv) > 2 else "dev_ablation"
    sa, sb = load_summaries(full), load_summaries(plain)
    common = sorted(set(sa) & set(sb))
    if not common:
        print("No shared tasks between", full, "and", plain)
        return 1
    A = agg([sa[t] for t in common])
    B = agg([sb[t] for t in common])

    metrics = [("Task Goal Completion %", "tgc_pct"), ("Solved", "solved"),
               ("Avg steps", "avg_steps"), ("Avg errors", "avg_errors"),
               ("Recoveries", "recoveries"), ("Avg cost $", "avg_cost_usd")]
    print(f"\nAblation on {len(common)} shared tasks:  FULL={full}  vs  PLAIN={plain}\n")
    print(f"| metric | {full} (full) | {plain} (plain) |")
    print("|---|---|---|")
    for label, key in metrics:
        print(f"| {label} | {A[key]} | {B[key]} |")

    rows_html = "".join(
        f"<tr><td>{label}</td><td>{A[key]}</td><td>{B[key]}</td></tr>"
        for label, key in metrics)
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>HELIX ablation</title>
<style>body{{font-family:Arial;background:#0f172a;color:#e2e8f0;padding:24px}}
table{{border-collapse:collapse}} td,th{{border:1px solid #334155;padding:8px 14px}}
th{{color:#94a3b8}} h1{{font-size:18px}}</style></head><body>
<h1>HELIX ablation - full stack vs plain ReAct ({len(common)} shared tasks)</h1>
<table><tr><th>metric</th><th>{full} (full)</th><th>{plain} (plain)</th></tr>{rows_html}</table>
<p style="color:#64748b">Full = memory + world-model + self-healing + monitor. Plain = none.</p>
</body></html>"""
    out = Path(REPORTS_DIR) / "comparison.html"
    out.write_text(html, encoding="utf-8")
    print("\nwrote:", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
