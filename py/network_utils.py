#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
network_utils.py -- shared constants, paths and deterministic writers
=====================================================================

Every step module imports from here rather than repeating a path, a seed or a
writer. The schema-figure helpers (boxes, arrows, hub bar, palette) will be
copied from ``hdoku26-visuals`` into ``py/schema_utils.py`` in the first step
that draws a schema figure -- copied, not referenced, so this repository keeps
building when the other one moves on.

Authors: Florian Thiery (LEIZA / Research Squirrel Engineers Network)
Licence: MIT (this script) / CC BY 4.0 (the figures and tables it produces)
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
from pathlib import Path
from typing import Iterable, Sequence

# --------------------------------------------------------------------------- #
# Release marker and seed -- NOT datetime.now(), NOT an unseeded layout.
# Bump RELEASE by hand when the content set changes.
# --------------------------------------------------------------------------- #
RELEASE = "2026-09-30"
SEED = 20251127          # ArcheoFOSS 2025, Busto Arsizio, 27 November 2025

# --------------------------------------------------------------------------- #
# Paths, resolved relative to the repository root
# --------------------------------------------------------------------------- #
ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"
DIST = ROOT / "dist"
IMG = ROOT / "img"
FONTS = ROOT / "fonts"

FONT_REGULAR = FONTS / "FiraSans-Regular.ttf"
FONT_MEDIUM = FONTS / "FiraSans-Medium.ttf"
FONT_BOLD = FONTS / "FiraSans-Bold.ttf"      # headings and panel letters (OFL, same licence file)
FONT_SANS = "Fira Sans"

# One output folder per step, the same name under dist/ and img/.
OUT_NAMES = {
    "02": "00-inventory",
    "03": "03-ancestors",
    "04": "04-saints",
    "05": "05-ashes",
    "06": "06-lod-layer",
    "07": "07-synthesis",
    "08": "paper",
    "09": "09-claims",
    "10": "10-statistics",
    "11": "11-gaps",
}


def dist_dir(step: str) -> Path:
    return DIST / OUT_NAMES[step]


def img_dir(step: str) -> Path:
    return IMG / OUT_NAMES[step]


def ensure_dirs(*dirs: Path) -> None:
    """Create output folders on demand. Called by a step right before it
    writes, so a step with nothing to do leaves no empty folder behind."""
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)


def rel(path: Path) -> str:
    """Repository-relative path with forward slashes -- the same string on
    Windows and Linux, so logs and reports do not differ by platform."""
    return Path(path).resolve().relative_to(ROOT).as_posix()


# --------------------------------------------------------------------------- #
# Deterministic writers
# --------------------------------------------------------------------------- #
def content_fingerprint(data: bytes) -> str:
    """Short, stable fingerprint for logs and the data inventory."""
    return hashlib.sha256(data).hexdigest()[:12]


def write_text(path: Path, text: str) -> str:
    """UTF-8, LF line endings, exactly one trailing newline."""
    text = text.rstrip("\n") + "\n"
    ensure_dirs(path.parent)
    path.write_bytes(text.encode("utf-8"))
    return rel(path)


def write_json(path: Path, obj) -> str:
    """Sorted keys, no ASCII escaping, two-space indent, trailing newline."""
    return write_text(path, json.dumps(obj, sort_keys=True, ensure_ascii=False, indent=2))


def write_csv(path: Path, header: Sequence[str], rows: Iterable[Sequence]) -> str:
    """CSV with LF line endings and minimal quoting. The caller sorts the
    rows; this function does not, because only the caller knows the key."""
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(header)
    for row in rows:
        writer.writerow(row)
    return write_text(path, buf.getvalue())


# --------------------------------------------------------------------------- #
# matplotlib, set up once per process so that every network figure is
# byte-reproducible: fixed hash salt for SVG ids, no creation date in the
# metadata, the vendored Fira Sans instead of whatever the machine has.
# --------------------------------------------------------------------------- #
def setup_matplotlib():
    """Import matplotlib lazily, configure it for reproducible output and
    return the pyplot module."""
    os.environ.setdefault("SOURCE_DATE_EPOCH", "0")
    import matplotlib

    matplotlib.use("Agg")
    from matplotlib import font_manager

    for font in (FONT_REGULAR, FONT_MEDIUM, FONT_BOLD):
        font_manager.fontManager.addfont(str(font))
    matplotlib.rcParams.update({
        "font.family": FONT_SANS,
        "svg.hashsalt": f"network--ogham-holywells-ci-{RELEASE}",
        "svg.fonttype": "none",       # text stays text in the SVG
        "path.simplify": False,
        # legends are framed boxes, so they read as legends on every figure
        "legend.frameon": True, "legend.fancybox": False, "legend.framealpha": 1.0,
        "legend.facecolor": SURFACE, "legend.edgecolor": INK_MUTED,
        "legend.borderpad": 0.55, "legend.borderaxespad": 0.5,
        "patch.linewidth": 0.5,
    })
    import matplotlib.pyplot as plt

    return plt


def save_figure(fig, out_dir: Path, name: str, *, dpi: int = 300, tight: bool = True) -> list[str]:
    """Write <name>.svg and <name>.png without date metadata and return the
    two paths, in the shape main.py expects from a step. `tight` crops the
    page to the drawn content (no white margin around frame or labels); the
    key image passes tight=False to keep its exact 4:3 page."""
    ensure_dirs(out_dir)
    svg_path = out_dir / f"{name}.svg"
    png_path = out_dir / f"{name}.png"
    crop = dict(bbox_inches="tight", pad_inches=0.04) if tight else {}
    fig.savefig(svg_path, metadata={"Date": None, "Creator": None}, **crop)
    # matplotlib writes SVG in text mode, i.e. with CRLF on Windows: normalise
    # to LF so the file is the same on every platform
    svg_path.write_bytes(svg_path.read_bytes().replace(b"\r\n", b"\n"))
    fig.savefig(png_path, dpi=dpi, metadata={"Software": None}, **crop)
    return [rel(svg_path), rel(png_path)]


# --------------------------------------------------------------------------- #
# Colours shared by every case study. Validated with the dataviz validator
# (scripts/validate_palette.js, light surface, --pairs all, 2026-10-20):
# only three categorical hues pass all-pairs, so three hubs get a hue and
# every other hub is drawn in neutral ink with its name written next to it.
# Hub identity is never colour alone: hub nodes always carry a direct label.
# --------------------------------------------------------------------------- #
SURFACE = "#fcfcfb"
INK = "#2c2c2a"          # primary text
INK_MUTED = "#5f5e5a"    # secondary text, axes
RULE = "#c9c7c0"         # recessive lines, basemap outline
LAND = "#efede7"
SEA = "#ffffff"

HUB_COLORS = {
    "Wikidata": "#2a78d6",       # categorical slot 1 (blue)
    "OpenStreetMap": "#eb6834",  # slot 2 (orange)
    "GeoNames": "#1baf7a",       # slot 3 (aqua); < 3:1 on the surface -> always labelled
}
HUB_OTHER = "#73726c"            # fuzzy-sl, Wikipedia, Logainm, SMR, ... (labelled)

# Ordinal certainty (fuzzy-sl certaintyLevel): one neutral ramp, dark = sure.
# Kept neutral so it never competes with the hub hues in a shared figure.
# 'dubious' takes the reserved critical red and is always drawn as a ring;
# 'not stated' (no certainty qualifier) is a grey ring.
CERTAINTY_COLORS = {
    "high": "#2c2c2a",
    "medium": "#73726c",
    "low": "#b4b2a9",
    "representative": "#d8d6cf",
    "dubious": "#d03b3b",
    "not stated": "#9a9890",
}
CERTAINTY_ORDER = ["high", "medium", "low", "representative", "dubious", "not stated"]


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance on a sphere of radius 6371.0088 km."""
    import math

    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(a))


def write_graphml(graph, path: Path) -> str:
    """GraphML for Gephi/igraph with nodes and edges in sorted order, so the
    file only changes when the graph does."""
    import networkx as nx

    ordered = graph.__class__()
    ordered.graph.update(graph.graph)
    for node in sorted(graph.nodes, key=str):
        ordered.add_node(node, **graph.nodes[node])
    for u, v, data in sorted(graph.edges(data=True), key=lambda e: (str(e[0]), str(e[1]))):
        ordered.add_edge(u, v, **data)
    ensure_dirs(path.parent)
    text = "\n".join(nx.generate_graphml(ordered, prettyprint=True))
    return write_text(path, text)


def place_labels(ax, items, *, offsets=None, avoid=(), fontsize=6.0, color=None, **text_kw):
    """Greedy, deterministic label placement: for each (x, y, text) try a few
    offsets around the point (in points) and keep the one whose box overlaps
    least with the labels already placed and with the `avoid` boxes (display
    coordinates). Labels are placed in the given order, so put the important
    ones first. Returns the text artists."""
    from matplotlib.transforms import Bbox

    offsets = offsets or [(0, -6, "center", "top"), (0, 6, "center", "bottom"),
                          (6, 0, "left", "center"), (-6, 0, "right", "center"),
                          (5, -5, "left", "top"), (-5, -5, "right", "top"),
                          (5, 5, "left", "bottom"), (-5, 5, "right", "bottom")]
    fig = ax.figure
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    placed: list = [Bbox(b) if not isinstance(b, Bbox) else b for b in avoid]
    artists = []

    def overlap(b):
        total = 0.0
        for o in placed:
            w = min(b.x1, o.x1) - max(b.x0, o.x0)
            h = min(b.y1, o.y1) - max(b.y0, o.y0)
            if w > 0 and h > 0:
                total += w * h
        return total

    for x, y, text in items:
        best = None
        for dx, dy, ha, va in offsets:
            t = ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points",
                            ha=ha, va=va, fontsize=fontsize, color=color or INK, **text_kw)
            bb = t.get_window_extent(renderer).expanded(1.04, 1.12)
            score = overlap(bb)
            if best is None or score < best[0]:
                if best is not None:
                    best[1].remove()
                best = (score, t, bb)
            else:
                t.remove()
            if score == 0:
                break
        placed.append(best[2])
        artists.append(best[1])
    return artists


def marker_boxes(ax, xs, ys, radius_pt=3.0):
    """Display-space boxes around point markers, for place_labels(avoid=...)."""
    from matplotlib.transforms import Bbox

    r = radius_pt * ax.figure.dpi / 72
    out = []
    for x, y in zip(xs, ys):
        px, py = ax.transData.transform((x, y))
        out.append(Bbox([[px - r, py - r], [px + r, py + r]]))
    return out


def nudge_apart(ax, pos, labels, *, fontsize=5.6, bbox=None, iterations=80, pad_px=2.0):
    """Move nodes that are drawn as text boxes until their boxes no longer
    overlap. `labels` maps node -> text. Works in display space, pushes each
    overlapping pair apart along the axis of least overlap, and returns the
    updated positions (data coordinates). Deterministic: pairs are visited in
    sorted order."""
    fig = ax.figure
    texts = {n: ax.text(*pos[n], t, fontsize=fontsize, ha="center", va="center", bbox=bbox)
             for n, t in labels.items()}
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    size = {n: (t.get_window_extent(renderer).width + pad_px,
                t.get_window_extent(renderer).height + pad_px) for n, t in texts.items()}
    for t in texts.values():
        t.remove()
    disp = {n: list(ax.transData.transform(pos[n])) for n in labels}
    nodes = sorted(labels, key=str)
    for _ in range(iterations):
        moved = False
        for i, a in enumerate(nodes):
            for b in nodes[i + 1:]:
                dx = disp[b][0] - disp[a][0]
                dy = disp[b][1] - disp[a][1]
                ox = (size[a][0] + size[b][0]) / 2 - abs(dx)
                oy = (size[a][1] + size[b][1]) / 2 - abs(dy)
                if ox > 0 and oy > 0:
                    moved = True
                    if oy <= ox:
                        s = 0.5 * oy * (1 if dy >= 0 else -1)
                        disp[a][1] -= s
                        disp[b][1] += s
                    else:
                        s = 0.5 * ox * (1 if dx >= 0 else -1)
                        disp[a][0] -= s
                        disp[b][0] += s
        if not moved:
            break
    inv = ax.transData.inverted()
    out = dict(pos)
    for n in nodes:
        out[n] = tuple(inv.transform(disp[n]))
    return out


def busy_grid(fig):
    """Rasterise the figure as drawn so far and return f(bbox) -> share of
    'busy' (clearly darker than the background) pixels inside a display-space
    box. Used to put labels and map furniture where nothing is drawn."""
    import numpy as np

    fig.canvas.draw()
    rgb = np.asarray(fig.canvas.buffer_rgba())[:, :, :3].astype(float) / 255.0
    busy = ((rgb @ np.array([0.2126, 0.7152, 0.0722])) < 0.80).astype(np.int64)
    h, w = busy.shape
    acc = np.zeros((h + 1, w + 1), dtype=np.int64)
    acc[1:, 1:] = busy.cumsum(0).cumsum(1)

    def frac(b):
        x0, x1 = int(max(0, b.x0)), int(min(w, b.x1))
        y0, y1 = int(max(0, h - b.y1)), int(min(h, h - b.y0))
        if x1 <= x0 or y1 <= y0:
            return 1.0
        n = acc[y1, x1] - acc[y0, x1] - acc[y1, x0] + acc[y0, x0]
        return float(n) / float((x1 - x0) * (y1 - y0))
    return frac


def _overlap_area(a, b):
    w = min(a.x1, b.x1) - max(a.x0, b.x0)
    h = min(a.y1, b.y1) - max(a.y0, b.y0)
    return w * h if w > 0 and h > 0 else 0.0


def callout_labels(ax, items, *, avoid=(), fontsize=5.8, rings=(11, 20, 31, 44, 60, 80, 105),
                   n_angles=16, bounds=None, zorder=8, bbox=None, line_color=None, **text_kw):
    """Labels set beside their point and joined to it by a thin leader line.
    For each (x, y, text), in the given order, candidate positions on rings
    around the point are scored by overlap with labels already placed, with
    the `avoid` boxes (display coordinates), by how much is drawn underneath
    (busy_grid) and by distance; the cheapest wins, so labels drift into empty
    space and the leader line tells which point they belong to. Candidates
    outside `bounds` (default: the axes) are discarded. Deterministic."""
    import math
    from matplotlib.transforms import Bbox

    fig = ax.figure
    frac = busy_grid(fig)
    renderer = fig.canvas.get_renderer()
    bounds = bounds or ax.get_window_extent()
    box = bbox or dict(boxstyle="square,pad=0.18", fc=SURFACE, ec=INK_MUTED, lw=0.35, alpha=0.96)
    placed = [Bbox(b) if not isinstance(b, Bbox) else b for b in avoid]
    probe = ax.annotate("", (0, 0), xytext=(0, 0), textcoords="offset points", fontsize=fontsize,
                        bbox=box, **text_kw)
    artists = []
    for x, y, text in items:
        probe.set_text(text)
        probe.xy = (x, y)
        best = None
        for ri, r in enumerate(rings):
            for k in range(n_angles):
                ang = 2 * math.pi * ((k + 0.5 * (ri % 2)) / n_angles + 0.125)
                c, s = math.cos(ang), math.sin(ang)
                ha = "left" if c > 0.35 else "right" if c < -0.35 else "center"
                va = "bottom" if s > 0.35 else "top" if s < -0.35 else "center"
                probe.xyann = (r * c, r * s)
                probe.set_ha(ha)
                probe.set_va(va)
                bb = probe.get_window_extent(renderer).expanded(1.08, 1.35).padded(3)
                area = max(bb.width * bb.height, 1.0)
                outside = 1.0 - _overlap_area(bb, bounds) / area
                if outside > 0.01:
                    continue
                score = (300 * sum(_overlap_area(bb, o) for o in placed) / area
                         + 10 * frac(bb) + 0.02 * r + 0.004 * k)
                if best is None or score < best[0]:
                    best = (score, r * c, r * s, ha, va, bb)
        if best is None:
            continue
        _, dx, dy, ha, va, bb = best
        t = ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                        fontsize=fontsize, color=INK, zorder=zorder, bbox=box,
                        arrowprops=dict(arrowstyle="-", lw=0.45, color=line_color or INK_MUTED,
                                        shrinkA=0, shrinkB=1.5, relpos=(0.5, 0.5)),
                        **text_kw)
        placed.append(bb)
        artists.append(t)
    probe.remove()
    return artists
