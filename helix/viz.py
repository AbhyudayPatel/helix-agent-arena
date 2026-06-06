"""Trajectory visualization.

Three outputs per trajectory, in increasing order of portability:
  * .dot   - Graphviz source (always written)
  * .svg/.png - rendered if the Graphviz `dot` binary is available (best effort)
  * .html  - self-contained interactive graph (vis-network via CDN); always works,
             no local binary needed. This is the demo surface: click any node to
             inspect the exact code / observation / decision behind it.

Nodes are colored by outcome status; recovery edges are red dashed; world-model
prediction branches are purple dashed; retrieved-memory influences are blue dotted.
"""
from __future__ import annotations

import json
from pathlib import Path

from .trajectory import KIND_SHAPE, STATUS_COLOR, Trajectory
from .util import trim

# vis-network shape per node kind
_VIS_SHAPE = {
    "state": "box",
    "decision": "ellipse",
    "action": "box",
    "outcome": "box",
    "prediction": "diamond",
    "memory": "database",
}
_EDGE_STYLE = {
    "recovers": {"color": "#ef4444", "dashes": True, "width": 3},
    "predicts": {"color": "#a855f7", "dashes": True, "width": 1},
    "informs": {"color": "#3b82f6", "dashes": [2, 4], "width": 1},
    "decides": {"color": "#94a3b8", "dashes": False, "width": 2},
    "acts": {"color": "#94a3b8", "dashes": False, "width": 2},
    "yields": {"color": "#94a3b8", "dashes": False, "width": 2},
    "transitions": {"color": "#64748b", "dashes": False, "width": 2},
}


def _node_detail(n) -> str:
    d = n.data
    lines = [f"[{n.kind.upper()} {n.id}] step {n.step} | status={n.status}"]
    if n.kind == "decision":
        if d.get("thought"):
            lines.append("THOUGHT:\n" + trim(d["thought"], 700))
        if d.get("diagnosis"):
            lines.append("DIAGNOSIS:\n" + trim(d["diagnosis"], 500))
        if "predicted_success" in d:
            lines.append(f"predicted P(success)={d['predicted_success']}"
                         + (f"  actual={d.get('actual_success')}" if 'actual_success' in d else ""))
        if d.get("chosen_plan"):
            lines.append("CHOSEN PLAN:\n" + trim(d["chosen_plan"], 400))
    elif n.kind == "action":
        lines.append("CODE:\n" + trim(d.get("code", ""), 1200))
    elif n.kind == "outcome":
        if d.get("error_type"):
            lines.append(f"error_type={d['error_type']}")
        if d.get("signals"):
            lines.append(f"monitor signals: {d['signals']}")
        lines.append(f"latency={d.get('latency_s')}s  api_calls={d.get('num_api_calls')}")
        lines.append("OUTPUT:\n" + trim(d.get("raw", d.get("digest", "")), 1200))
    elif n.kind == "prediction":
        lines.append(f"P(success)={d.get('p_success')}  source={d.get('source')}")
        lines.append("PLAN:\n" + trim(d.get("plan", ""), 400))
        if d.get("rationale"):
            lines.append("WHY: " + trim(d["rationale"], 300))
    elif n.kind == "memory":
        lines.append(f"similarity={d.get('score')}")
        p = d.get("payload", {})
        lines.append("RECALLED:\n" + trim(p.get("instruction", "") or p.get("approach", ""), 600))
    elif n.kind == "state":
        if d.get("instruction"):
            lines.append("TASK:\n" + trim(d["instruction"], 400))
    return "\n".join(lines)


def trajectory_to_vis(traj: Trajectory) -> dict:
    nodes = []
    for n in traj.nodes:
        detail = _node_detail(n)
        nodes.append({
            "id": n.id,
            "label": f"{n.id}: {trim(n.label, 38)}",
            "shape": _VIS_SHAPE.get(n.kind, "box"),
            "color": {"background": STATUS_COLOR.get(n.status, "#e2e8f0"),
                      "border": "#475569"},
            "font": {"multi": False, "size": 13,
                     "face": "monospace" if n.kind == "action" else "arial"},
            "title": detail,
            "detail": detail,
            "group": n.kind,
        })
    edges = []
    for e in traj.edges:
        style = _EDGE_STYLE.get(e.relation, {"color": "#94a3b8", "dashes": False, "width": 1})
        edges.append({
            "from": e.src, "to": e.dst, "label": e.relation, "arrows": "to",
            "color": {"color": style["color"]}, "dashes": style["dashes"],
            "width": style["width"], "font": {"size": 10, "align": "middle"},
        })
    return {"nodes": nodes, "edges": edges}


def to_dot(traj: Trajectory) -> str:
    lines = ["digraph trajectory {", "  rankdir=LR;", '  node [style=filled, fontname="Helvetica"];',
             '  graph [labelloc="t", fontsize=16, '
             f'label="HELIX trajectory: {traj.task_id} | solved={traj.solved} | '
             f'steps={traj.num_steps} errors={traj.num_errors} recoveries={traj.num_recoveries}"];']
    gv_shape = {"state": "box", "decision": "ellipse", "action": "note",
                "outcome": "box", "prediction": "diamond", "memory": "cylinder"}
    for n in traj.nodes:
        color = STATUS_COLOR.get(n.status, "#e2e8f0")
        shape = gv_shape.get(n.kind, "box")
        label = f"{n.id}: {trim(n.label, 40)}".replace('"', "'")
        lines.append(f'  {n.id} [shape={shape}, fillcolor="{color}", label="{label}"];')
    for e in traj.edges:
        style = _EDGE_STYLE.get(e.relation, {})
        attrs = [f'label="{e.relation}"']
        if style.get("dashes"):
            attrs.append('style=dashed')
        col = style.get("color")
        if col:
            attrs.append(f'color="{col}"')
        lines.append(f'  {e.src} -> {e.dst} [{", ".join(attrs)}];')
    lines.append("}")
    return "\n".join(lines)


def _ensure_dot_on_path() -> None:
    """Add common Graphviz install dirs to PATH so the `dot` binary is found
    even when its installer didn't refresh the current shell's PATH."""
    import os
    import shutil

    if shutil.which("dot"):
        return
    candidates = [
        r"C:\Program Files\Graphviz\bin",
        r"C:\Program Files (x86)\Graphviz\bin",
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Graphviz\bin"),
        "/usr/bin", "/usr/local/bin", "/opt/homebrew/bin",
    ]
    for d in candidates:
        if os.path.isdir(d):
            os.environ["PATH"] = d + os.pathsep + os.environ.get("PATH", "")


def render_graphviz(traj: Trajectory, out_stem: Path, formats=("svg",)) -> list[Path]:
    """Render PNG/SVG via the Graphviz binary if present; returns written paths."""
    _ensure_dot_on_path()
    dot_src = to_dot(traj)
    written = []
    try:
        import graphviz  # python wrapper; needs the `dot` binary on PATH
        src = graphviz.Source(dot_src)
        for fmt in formats:
            path = src.render(filename=str(out_stem), format=fmt, cleanup=True)
            written.append(Path(path))
    except Exception:
        pass  # binary not available - the .dot and .html still cover us
    return written


_HTML_TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>HELIX Trajectory __TASK__</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
  body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#0f172a;color:#e2e8f0}
  header{padding:10px 16px;background:#1e293b;border-bottom:1px solid #334155}
  header h1{margin:0;font-size:16px} header .sub{font-size:12px;color:#94a3b8;margin-top:4px}
  .wrap{display:flex;height:calc(100vh - 64px)}
  #net{flex:3;height:100%}
  #side{flex:1;max-width:420px;overflow:auto;padding:12px;background:#111827;border-left:1px solid #334155}
  #side pre{white-space:pre-wrap;word-break:break-word;font-size:12px;color:#cbd5e1}
  .legend{font-size:11px;color:#94a3b8;padding:6px 16px;background:#1e293b}
  .chip{display:inline-block;padding:1px 7px;border-radius:8px;margin-right:6px;color:#0f172a}
</style></head>
<body>
<header><h1>HELIX - Trajectory Intelligence</h1><div class="sub">__SUB__</div></header>
<div class="legend">
  <span class="chip" style="background:#bfdbfe">start</span>
  <span class="chip" style="background:#bbf7d0">ok</span>
  <span class="chip" style="background:#fecaca">error</span>
  <span class="chip" style="background:#fdba74">recovery</span>
  <span class="chip" style="background:#e9d5ff">prediction</span>
  &nbsp; edges: gray=flow, <span style="color:#ef4444">red=recovers</span>,
  <span style="color:#a855f7">purple=predicts</span>, <span style="color:#3b82f6">blue=memory</span>
</div>
<div class="wrap">
  <div id="net"></div>
  <div id="side"><b>Click any node</b> to inspect the exact decision / code / observation.<pre id="detail"></pre></div>
</div>
<script>
const DATA = __PAYLOAD__;
const nodes = new vis.DataSet(DATA.nodes);
const edges = new vis.DataSet(DATA.edges);
const network = new vis.Network(document.getElementById('net'), {nodes, edges}, {
  layout:{hierarchical:{enabled:true,direction:'LR',sortMethod:'directed',levelSeparation:190,nodeSpacing:90}},
  physics:false,
  interaction:{hover:true,navigationButtons:true,keyboard:true},
  nodes:{borderWidth:1,shapeProperties:{interpolation:false}},
});
function show(id){const n=nodes.get(id); document.getElementById('detail').textContent = n? n.detail : '';}
network.on('selectNode', p => show(p.nodes[0]));
network.on('hoverNode', p => show(p.node));
</script>
</body></html>"""


def render_html(traj: Trajectory, out_path: Path) -> Path:
    payload = trajectory_to_vis(traj)
    s = traj.summary()
    sub = (f"task {traj.task_id} | solved={traj.solved} | steps={s['num_steps']} | "
           f"errors={s['num_errors']} | recoveries={s['num_recoveries']} | "
           f"WM-acc={s['world_model_accuracy']} | cost=${s['total_cost_usd']} | "
           f"{trim(traj.instruction, 90)}")
    html = (_HTML_TEMPLATE
            .replace("__PAYLOAD__", json.dumps(payload))
            .replace("__TASK__", traj.task_id)
            .replace("__SUB__", sub.replace("<", "&lt;")))
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    return out_path


def visualize(traj: Trajectory, out_dir: Path) -> dict:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / traj.task_id
    dot_path = stem.with_suffix(".dot")
    dot_path.write_text(to_dot(traj), encoding="utf-8")
    html_path = render_html(traj, stem.with_suffix(".html"))
    images = render_graphviz(traj, stem, formats=("svg",))
    return {"dot": dot_path, "html": html_path,
            "images": [str(p) for p in images]}
