# -*- coding: utf-8 -*-
"""
claims.gaps -- the lists of step 11 against the numbers named in the PRIMER
============================================================================

Reads dist/11-gaps/metrics.csv. None of these numbers is in the text yet
(paper=None, status NEW, except where noted); they are the findings that the text can name:
the single Ogham items that no project joins to the corpus, and the sources
of the holy wells that Wikidata no longer describes.
"""

from __future__ import annotations

from .core import claim, dist

LA = "Q2 How unevenly is layer b spread?"
LS = "Q3 Which hubs carry layer b?"


def _m(key):
    t = dist("11-gaps/metrics.csv")
    return t[t["key"] == key]["value"].iloc[0]


def _add(cid, section, statement, key, how, why, paper=None):
    @claim(cid, section, statement, paper=paper, source="dist/11-gaps/metrics.csv", how=how, why=why)
    def _f():
        return _m(key)
    _f.__name__ = "gap_" + key
    return _f


_add("G-01", "3.1", "single Ogham items with a stone of the corpus within 5 km", "single_items_with_candidate",
     "single items (no project, no P1382 link) whose Wikidata coordinate lies within 5 km of at least one stone "
     "of the corpus; a coordinate alone is a weak hint, so these are candidates, not links",
     f"{LA} how far a coordinate comparison could close the gap between the single items and the corpus", paper=46)
_add("G-02", "3.1", "single Ogham items whose CIIC number in the label is that of a stone nearby", "single_items_ciic_match",
     "single items whose label 'CIIC n' equals the CIIC number of a stone within 5 km",
     f"{LA} the control for G-01: where the number agrees, the corpus has already joined item and stone (G-07)", paper=5)
_add("G-07", "3.1", "of those, single items that the corpus already joins to that stone", "single_items_ciic_match_joined",
     "G-02 items that are listed in the wikidata_items of the stone (dist/03-ancestors/stones.csv): the join over "
     "the CIIC identifier worked, the item is a one-item cluster of a joined stone and not a gap",
     f"{LA} shows that the single items with a matching CIIC number are not missing links")
_add("G-08", "3.1", "single items with a stone nearby and no joined stone among them", "single_items_open_candidate",
     "G-01 items for which none of the stones within 5 km is joined to them: the candidates to check by hand",
     f"{LA} the real list of candidates (G-01 less G-07)", paper=None)
_add("G-03", "3.2", "P1343 sources that Wikidata no longer describes", "dead_sources",
     "sources of the holy wells whose label is still the bare QID (no label, no statement, no redirect)",
     f"{LS} the community hub of the wells is not kept up: sources of the wells point into the void", paper=66)
_add("G-04", "3.2", "well-source edges that point at such a source", "dead_source_edges",
     "edges of the well-source table whose source is one of the sources of G-03", f"{LS} see G-03", paper=159)
_add("G-05", "3.2", "share of the well-source edges that point at such a source (%)", "dead_source_edges_pct",
     "G-04 divided by all well-source edges", f"{LS} see G-03", paper="4.8")
_add("G-06", "3.2", "wells with at least one such source", "dead_source_wells",
     "distinct wells in the edges of G-04", f"{LS} see G-03")
