# -*- coding: utf-8 -*-
"""
claims.core -- the registry behind step 09
===========================================

A *claim* is one number (or short list) that the paper states. Every claim is a
small function that reads a table and returns the value, so that the number can
be traced by reading ten lines of code:

    @claim("A-07", "3.1", "stones held by an institution", paper="182",
           key="03:stones_in_institutions", source="data/raw/ogham/keepers.csv",
           how="rows of keepers.csv: one row per stone with a known keeper",
           why="layer a, custody: how far stones have travelled")
    def stones_held():
        return len(raw("ogham/keepers.csv"))

paper   the value exactly as the text states it ("1,297", "21.2", "TODO");
        None means: not in the text (yet), only reported.
key     optional key in dist/paper/numbers.csv (step 08). If given, the claim is
        also compared with the number the pipeline itself wrote there.
source  the file(s) the function reads, for the reader.
how     what exactly is counted, in plain words (goes into the Markdown report).
why     why the number is in the paper (research question, argument) -- the
        reason a reader would ask "why do you tell me this?".

Statuses
    OK    computed value equals the paper
    DIFF  computed value differs from the paper
    TODO  the paper still has a placeholder; the computed value is what goes in
    NEW   not in the paper (paper=None)
and, independently, ``numbers_csv`` = agree / differ / (empty if no key).
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
DIST = ROOT / "dist"

REGISTRY: list["Claim"] = []
_CACHE: dict[str, object] = {}


@dataclass
class Claim:
    cid: str
    section: str
    statement: str
    paper: str | None
    key: str
    source: str
    func: Callable
    value: str = ""
    status: str = ""
    numbers_csv: str = ""
    script: str = field(default="")
    how: str = ""      # the definition in plain words: what exactly is counted
    why: str = ""      # why the number is in the paper: which question or claim it carries


def claim(cid: str, section: str, statement: str, *, paper=None, key: str = "", source: str = "",
          how: str = "", why: str = ""):
    def deco(func):
        REGISTRY.append(Claim(cid, section, statement, None if paper is None else str(paper), key, source, func,
                              script=f"py/claims/{func.__module__.split('.')[-1]}.py::{func.__name__}",
                              how=how, why=why))
        return func
    return deco


# --------------------------------------------------------------------------- #
# reading
# --------------------------------------------------------------------------- #
def table(path: Path):
    """A CSV as a pandas DataFrame, every cell a string (no silent type guessing)."""
    import pandas as pd

    key = str(path)
    if key not in _CACHE:
        _CACHE[key] = pd.read_csv(path, dtype=str, keep_default_na=False)
    return _CACHE[key].copy()


def raw(rel: str):
    return table(RAW / rel)


def dist(rel: str):
    return table(DIST / rel)


def floats(series):
    return series.astype(float)


def pct(k: float, n: float, digits: int = 1) -> float:
    return round(100.0 * k / n, digits)


# --------------------------------------------------------------------------- #
# comparing
# --------------------------------------------------------------------------- #
def _num(text: str):
    t = text.replace(",", "").replace("%", "").replace(" ", "").strip()
    try:
        return float(t), (len(t.split(".")[1]) if "." in t else 0)
    except ValueError:
        return None


def fmt(value) -> str:
    if isinstance(value, float):
        return f"{value:.10g}"
    return str(value)


def same(computed, paper: str) -> bool:
    """Compare at the precision the paper states (21.2 vs 21.19 is equal)."""
    p = _num(paper)
    c = _num(fmt(computed))
    if p is not None and c is not None:
        return round(c[0], p[1]) == p[0]
    norm = lambda s: re.sub(r"\s+", " ", str(s)).strip().lower()
    return norm(computed) == norm(paper)


def load_numbers() -> dict[str, str]:
    path = DIST / "paper" / "numbers.csv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as fh:
        return {r["key"]: r["value"] for r in csv.DictReader(fh)}


def run_all() -> list[Claim]:
    numbers = load_numbers()
    for c in REGISTRY:
        c.value = fmt(c.func())
        if c.paper is None:
            c.status = "NEW"
        elif c.paper.strip().upper() == "TODO":
            c.status = "TODO"
        else:
            c.status = "OK" if same(c.value, c.paper) else "DIFF"
        if c.key and c.key in numbers:
            c.numbers_csv = "agree" if same(c.value, numbers[c.key]) else "differ"
    return REGISTRY
