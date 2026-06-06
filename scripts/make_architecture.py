"""Render the HELIX system architecture to reports/architecture.svg (+ .dot)."""
import sys
from pathlib import Path

from helix.viz import _ensure_dot_on_path

DOT = r"""
digraph HELIX {
  rankdir=TB; bgcolor="#0f172a"; fontcolor="#e2e8f0"; fontname="Helvetica";
  node [style=filled, fontname="Helvetica", color="#475569", fontcolor="#0f172a"];
  edge [color="#94a3b8", fontcolor="#cbd5e1", fontname="Helvetica", fontsize=10];
  labelloc="t"; fontsize=20;
  label="HELIX - Trajectory Intelligence Platform";

  subgraph cluster_brain {
    label="trajectory intelligence layer"; color="#334155"; fontcolor="#94a3b8";
    WM   [label="World Model\n(P(success) = LLM (+) memory prior)", shape=box, fillcolor="#e9d5ff"];
    MON  [label="Monitor\n(loops/errors/budget -> heal/replan/abort)", shape=box, fillcolor="#fde68a"];
    HEAL [label="Self-Healer\n(recall -> diagnose -> fix)", shape=box, fillcolor="#fdba74"];
    MEM  [label="Memory\n(HydraDB / local vectors)", shape=cylinder, fillcolor="#bfdbfe"];
    TRAJ [label="Trajectory Graph\nState -> Decision -> Action -> Outcome", shape=box, fillcolor="#bbf7d0"];
  }
  AGENT [label="HelixAgent\nReAct code loop (Claude Opus)", shape=box, fillcolor="#a7f3d0"];
  ENV   [label="AppWorld\n(in-process; apis.*; evaluate)", shape=box, fillcolor="#e2e8f0"];
  VIZ   [label="Viz + Dashboard\n(vis-network HTML, Graphviz, metrics)", shape=box, fillcolor="#e2e8f0"];

  AGENT -> ENV   [label="execute(code)"];
  ENV   -> AGENT [label="observation / score"];
  AGENT -> TRAJ  [label="records"];
  TRAJ  -> MON   [label="observe (live)"];
  MON   -> HEAL  [label="heal"];
  MON   -> AGENT [label="replan / abort"];
  HEAL  -> AGENT [label="recovery guidance"];
  WM    -> AGENT [label="best branch"];
  MEM   -> AGENT [label="recalled approaches"];
  TRAJ  -> MEM   [label="index solved"];
  MEM   -> WM    [label="success prior"];
  MEM   -> HEAL  [label="past recoveries"];
  TRAJ  -> VIZ   [label="graph + metrics"];
}
"""


def main() -> int:
    _ensure_dot_on_path()
    out_dir = Path("reports")
    out_dir.mkdir(exist_ok=True)
    (out_dir / "architecture.dot").write_text(DOT, encoding="utf-8")
    try:
        import graphviz
        graphviz.Source(DOT).render(filename=str(out_dir / "architecture"),
                                    format="svg", cleanup=True)
        print("wrote reports/architecture.svg")
    except Exception as e:  # noqa: BLE001
        print("dot render skipped:", e, "(architecture.dot still written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
