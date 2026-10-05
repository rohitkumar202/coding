"""Generates images/dfs_bfs.svg — a cheat sheet for dfs() and bfs() in graph/traversal_list.py.

Run from the project root:  python3 images/generate_traversal.py
Edit GRAPH / *_CODE / *_ORDER / *_RULES below when graph/traversal_list.py changes.
"""
import math
from html import escape
from pathlib import Path

# Must match `graph` in graph/traversal_list.py
GRAPH = {0: [1, 2], 1: [3, 4], 2: [4], 3: [5], 4: [5], 5: []}

# Node positions inside a panel (x relative to panel left, y absolute)
POS = {0: (285, 145), 1: (185, 215), 2: (385, 215), 3: (135, 285), 4: (285, 285), 5: (210, 355)}

# Must match the code in graph/traversal_list.py; lines in *_HIGHLIGHT (1-based) get a marker
DFS_CODE = """def dfs(node, graph, visited):
  if node not in visited:
    print(node)
    visited.add(node)  # mark on entry
    for neighbor in graph[node]:
      dfs(neighbor, graph, visited)"""
DFS_HIGHLIGHT = {2, 4}

BFS_CODE = """def bfs(queue, graph, visited):
  queue = deque(queue)
  visited.update(queue)
  while queue:
    node = queue.popleft()
    print(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)  # mark on enqueue
        queue.append(neighbor)"""
BFS_HIGHLIGHT = {2, 8, 9}

# Output of running each function from node 0
DFS_ORDER = [0, 1, 3, 5, 4, 2]
BFS_ORDER = [0, 1, 2, 3, 4, 5]

DFS_RULES = [
    "Mark visited when you ENTER a node, before recursing",
    "(else a cycle recurses forever).",
    "Print after the visited check, so each node prints once.",
]
BFS_RULES = [
    "Mark visited when you ENQUEUE, not when you pop,",
    "so each node enters the queue only once.",
    "deque.popleft() is O(1); list.pop(0) is O(n).",
]

W, H = 1200, 840
PANEL_W = 570
R = 21
INK, MUTED, EDGE = "#1f2937", "#6b7280", "#9ca3af"
CODE_BG, CODE_INK = "#0f172a", "#e2e8f0"


def text(x, y, s, size=15, color=INK, weight="normal", anchor="start", family="sans"):
    fam = "DejaVu Sans Mono, Menlo, Consolas, monospace" if family == "mono" else "Inter, Segoe UI, Helvetica, Arial, sans-serif"
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" fill="{color}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{escape(s).replace(" ", "&#160;")}</text>')


def panel(ox, title, subtitle, color, tint, hl, order, code, highlight, rules, levels):
    out = [f'<rect x="{ox}" y="20" width="{PANEL_W}" height="{H - 70}" rx="16" fill="{tint}" stroke="{color}" stroke-width="2"/>']
    out.append(text(ox + 24, 58, title, 24, color, "bold"))
    out.append(text(ox + 24, 84, subtitle, 15, MUTED))

    if levels:  # BFS: dashed bands showing it goes level by level
        for i, y in enumerate(sorted({p[1] for p in POS.values()})):
            out.append(f'<line x1="{ox + 20}" y1="{y}" x2="{ox + PANEL_W - 20}" y2="{y}" stroke="#fdba74" stroke-dasharray="5 5"/>')
            out.append(text(ox + PANEL_W - 24, y - 6, f"level {i}", 12, color, anchor="end"))

    # Directed edges, shortened so arrowheads stop at the node border
    for u, nbrs in GRAPH.items():
        for v in nbrs:
            (x1, y1), (x2, y2) = POS[u], POS[v]
            d = math.hypot(x2 - x1, y2 - y1)
            dx, dy = (x2 - x1) / d, (y2 - y1) / d
            tx, ty = ox + x2 - dx * R, y2 - dy * R  # arrow tip on the target's border
            out.append(f'<line x1="{ox + x1 + dx * R:.1f}" y1="{y1 + dy * R:.1f}" x2="{tx - dx * 8:.1f}" '
                       f'y2="{ty - dy * 8:.1f}" stroke="{EDGE}" stroke-width="2"/>')
            bx, by = tx - dx * 11, ty - dy * 11
            out.append(f'<polygon points="{tx:.1f},{ty:.1f} {bx - dy * 5:.1f},{by + dx * 5:.1f} {bx + dy * 5:.1f},{by - dx * 5:.1f}" fill="{EDGE}"/>')

    # Nodes with a badge showing visit order
    for node, (x, y) in POS.items():
        out.append(f'<circle cx="{ox + x}" cy="{y}" r="{R}" fill="#fff" stroke="{color}" stroke-width="2.5"/>')
        out.append(text(ox + x, y + 6, str(node), 17, INK, "bold", "middle"))
        bx, by = ox + x + R - 2, y - R + 2
        out.append(f'<circle cx="{bx}" cy="{by}" r="11" fill="{color}"/>')
        out.append(text(bx, by + 4, str(order.index(node) + 1), 12, "#fff", "bold", "middle"))

    out.append(text(ox + 24, 410, "Visit order:", 15, MUTED))
    out.append(text(ox + 118, 410, "  →  ".join(map(str, order)), 17, INK, "bold"))

    # Code block
    out.append(f'<rect x="{ox + 20}" y="428" width="{PANEL_W - 40}" height="236" rx="10" fill="{CODE_BG}"/>')
    for i, line in enumerate(code.splitlines(), 1):
        y = 452 + (i - 1) * 21
        if i in highlight:
            out.append(f'<rect x="{ox + 20}" y="{y - 15}" width="{PANEL_W - 40}" height="21" fill="{hl}"/>')
            out.append(f'<rect x="{ox + 20}" y="{y - 15}" width="4" height="21" fill="{color}"/>')
        out.append(text(ox + 36, y, line, 14, CODE_INK, family="mono"))

    # Key rules
    out.append(text(ox + 24, 694, "Remember", 15, color, "bold"))
    for i, rule in enumerate(rules):
        out.append(text(ox + 24, 718 + i * 22, rule, 14.5, INK))
    return out


def main():
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
    ]
    parts += panel(20, "DFS · Depth-First Search", "Go DEEP first · uses a stack (recursion)",
                   "#2563eb", "#eff6ff", "#1e3a8a", DFS_ORDER, DFS_CODE, DFS_HIGHLIGHT, DFS_RULES, levels=False)
    parts += panel(610, "BFS · Breadth-First Search", "Go WIDE first, level by level · uses a queue",
                   "#ea580c", "#fff7ed", "#7c2d12", BFS_ORDER, BFS_CODE, BFS_HIGHLIGHT, BFS_RULES, levels=True)
    adj = "   ".join(f"{u}→{v}" for u, v in GRAPH.items() if v)
    parts.append(text(W / 2, H - 22, f"graph:  {adj}        Both run in O(V + E)    ·    badge = visit order",
                      14, MUTED, anchor="middle"))
    parts.append("</svg>")

    out = Path(__file__).with_name("dfs_bfs.svg")
    out.write_text("\n".join(parts) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
