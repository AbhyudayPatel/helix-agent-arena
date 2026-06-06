"""Render detailed HELIX flowgraphs to reports/flow_*.svg (+ .dot)."""
import sys
from pathlib import Path

from helix.viz import _ensure_dot_on_path

CONTROL = r"""
digraph control {
  rankdir=TB; bgcolor="#0f172a"; fontname="Helvetica"; fontcolor="#e2e8f0";
  node[fontname="Helvetica", style=filled, color="#475569", fontcolor="#0f172a"];
  edge[color="#94a3b8", fontcolor="#cbd5e1", fontsize=10];
  labelloc=t; fontsize=18; label="HELIX — per-task control flow";

  reset[label="env.reset(task_id)\ninstruction + supervisor + apps", shape=box, fillcolor="#bfdbfe"];
  recall[label="MEMORY recall_for_task\n(similar solved approaches)", shape=cylinder, fillcolor="#bfdbfe"];
  plan[label="WORLD-MODEL plan\nscore strategies = 0.7·LLM + 0.3·prior", shape=box, fillcolor="#e9d5ff"];
  boot[label="BOOTSTRAP (step 1)\nfetch task+passwords+profile+apps", shape=box, fillcolor="#a7f3d0"];
  llm[label="LLM.complete(system, messages)\nthought + ONE python block", shape=box, fillcolor="#fde68a"];
  code[label="code present?", shape=diamond, fillcolor="#fef3c7"];
  exec[label="env.execute(code)\n→ Observation(status, error, latency)", shape=note, fillcolor="#e2e8f0"];
  rec[label="record Decision→Action→Outcome→State\ninto the trajectory graph", shape=box, fillcolor="#bbf7d0"];
  mon[label="MONITOR.observe(traj)\nsignals → intervention", shape=box, fillcolor="#fde68a"];
  iv[label="intervention?", shape=diamond, fillcolor="#fef3c7"];
  heal[label="SELF-HEAL\nrecall+diagnose+fix (or escalate)", shape=box, fillcolor="#fdba74"];
  replan[label="REPLAN nudge", shape=box, fillcolor="#fde68a"];
  done[label="task_completed()?", shape=diamond, fillcolor="#fef3c7"];
  evaln[label="env.evaluate()\nfinalize + index + visualize", shape=box, fillcolor="#a7f3d0"];

  reset->recall->plan->boot->llm;
  llm->code;
  code->llm[label="no → nudge"];
  code->exec[label="yes"];
  exec->rec->mon->iv;
  iv->heal[label="heal"]; iv->replan[label="replan"];
  iv->done[label="continue / abort"];
  heal->done; replan->done;
  done->llm[label="no (next step)"];
  done->evaln[label="yes"];
}
"""

MONITOR = r"""
digraph monitor {
  rankdir=LR; bgcolor="#0f172a"; fontname="Helvetica"; fontcolor="#e2e8f0";
  node[fontname="Helvetica", style=filled, color="#475569", fontcolor="#0f172a"];
  edge[color="#94a3b8", fontcolor="#cbd5e1", fontsize=10];
  labelloc=t; fontsize=18; label="Monitor — live trajectory signals → intervention";

  obs[label="observe(trajectory)", shape=box, fillcolor="#fde68a"];
  s1[label="≥2 trailing errors", fillcolor="#fecaca"];
  s2[label="same error type x2", fillcolor="#fecaca"];
  s3[label="repeated action (loop)", fillcolor="#fecaca"];
  s4[label="3 identical observations", fillcolor="#fde68a"];
  s5[label="≥6 doc-only actions", fillcolor="#fde68a"];
  s6[label="steps ≥ 80% budget", fillcolor="#fde68a"];
  s7[label="steps ≥ budget", fillcolor="#fdba74"];
  heal[label="HEAL", shape=box, fillcolor="#fdba74"];
  replan[label="REPLAN", shape=box, fillcolor="#fde68a"];
  abort[label="ABORT → finalize", shape=box, fillcolor="#fecaca"];

  obs->s1; obs->s2; obs->s3; obs->s4; obs->s5; obs->s6; obs->s7;
  s1->heal; s2->heal; s3->heal;
  s4->replan; s5->replan; s6->replan;
  s7->abort;
}
"""

MEMORY = r"""
digraph memory {
  rankdir=LR; bgcolor="#0f172a"; fontname="Helvetica"; fontcolor="#e2e8f0";
  node[fontname="Helvetica", style=filled, color="#475569", fontcolor="#0f172a"];
  edge[color="#94a3b8", fontcolor="#cbd5e1", fontsize=10];
  labelloc=t; fontsize=18; label="Memory + HydraDB dual path";

  traj[label="finished trajectory", shape=box, fillcolor="#bbf7d0"];
  idx[label="index_trajectory", shape=box, fillcolor="#bfdbfe"];
  byoe[label="BYOE vectors\nembeddings.insert(vectors + graph metadata)\n(0 tokens)", shape=cylinder, fillcolor="#bfdbfe"];
  kg[label="Managed graph\nupload.knowledge → entity/relation extraction\n(token usage)", shape=cylinder, fillcolor="#e9d5ff"];

  newtask[label="new task / failure", shape=box, fillcolor="#fde68a"];
  rtask[label="recall_for_task\nembeddings.search", shape=box, fillcolor="#bfdbfe"];
  rerr[label="recall_for_error\nembeddings.search", shape=box, fillcolor="#bfdbfe"];
  graphr[label="graph_recall\nfull_recall(graph_context)", shape=box, fillcolor="#e9d5ff"];
  dec[label="informs the next Decision\nor the Heal guidance", shape=ellipse, fillcolor="#a7f3d0"];

  traj->idx; idx->byoe; idx->kg;
  newtask->rtask; newtask->rerr; newtask->graphr;
  byoe->rtask[style=dashed]; byoe->rerr[style=dashed]; kg->graphr[style=dashed];
  rtask->dec; rerr->dec; graphr->dec;
}
"""


def main() -> int:
    _ensure_dot_on_path()
    out = Path("reports"); out.mkdir(exist_ok=True)
    graphs = {"flow_control": CONTROL, "flow_monitor": MONITOR, "flow_memory": MEMORY}
    try:
        import graphviz
        for name, dot in graphs.items():
            (out / f"{name}.dot").write_text(dot, encoding="utf-8")
            graphviz.Source(dot).render(filename=str(out / name), format="svg", cleanup=True)
            print("wrote", out / f"{name}.svg")
    except Exception as e:  # noqa: BLE001
        for name, dot in graphs.items():
            (out / f"{name}.dot").write_text(dot, encoding="utf-8")
        print("dot render skipped:", e, "(.dot files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
