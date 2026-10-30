# -*- coding: utf-8 -*-
"""
claims.figures -- the statistics figures of step 10 against the numbers in the text
====================================================================================

Reads the tables that step 10 writes next to its figures (dist/10-statistics/).
Each claim ties a number that one of the figures draws to the number the text
states, so that figure and text cannot disagree. Numbers that only a figure
shows have paper=None (status NEW).
"""

from __future__ import annotations

from .core import claim, dist, floats, pct

Q1 = "Q1 How dense is layer b?"
Q2 = "Q2 How unevenly is layer b spread?"
Q3 = "Q3 Which hubs carry layer b?"
Q4 = "Q4 How is uncertainty recorded?"
FIG = "figure img/10-statistics/"


def _kinds_share(case):
    t = dist("10-statistics/hub-kinds.csv")
    t = t[t["case"] == case]
    n = float(t["of"].iloc[0])
    return pct(sum(float(r["entities"]) for _, r in t.iterrows() if r["kinds of hub"] != "0"
                   and r["kinds of hub"] != "1"), n)


def _kinds_claim(cid, case, paper):
    @claim(cid, "3.4", f"{case}: entities with two or more kinds of hub, from the hub-kinds figure (%)",
           paper=paper, source="dist/10-statistics/hub-kinds.csv",
           how="entities of the case in the bars '2 kinds', '3 kinds' and '4 or more' of the figure, divided by all "
               "entities of the case; the number of kinds is counted as in step 06 (the wells count Wikidata, "
               "their home, as a kind)",
           why=f"{Q3} {FIG}hub-kinds.png shows the distribution behind the text's 'at least two kinds of hub'")
    def _f():
        return _kinds_share(case)
    _f.__name__ = f"hub_kinds_{case.split()[0].lower()}"
    return _f


for _cid, _case, _paper in (("F-01a", "Ogham stones", "70.2"), ("F-01b", "Holy wells", "99.3"),
                            ("F-01c", "CI findspots", "39.2")):
    _kinds_claim(_cid, _case, _paper)


@claim("F-02", "3.1", "statements with AMT weight 0.9 in the uncertainty figure", paper=20,
       source="dist/10-statistics/uncertainty.csv",
       how="statements with weight 0.90 in panel A of the figure",
       why=f"{Q4} {FIG}uncertainty.png, panel A: the number of uncertain readings")
def fig_weight():
    t = dist("10-statistics/uncertainty.csv")
    return int(t[(t["recorded as"] == "AMT weight") & (t["value"] == "0.90")]["count"].iloc[0])


@claim("F-03", "3.3", "findspots with a match type in the uncertainty figure", paper=74,
       source="dist/10-statistics/uncertainty.csv",
       how="sum of the four bars of panel B (one match type per row of the CI table)",
       why=f"{Q4} {FIG}uncertainty.png, panel B: the figure covers the 74 findspots of the table, as the text does")
def fig_match_total():
    t = dist("10-statistics/uncertainty.csv")
    return int(floats(t[t["recorded as"] == "match type of the link"]["count"]).sum())


@claim("F-04", "3.3", "findspots in the uncertainty figure, panel C", paper=79,
       source="dist/10-statistics/uncertainty.csv",
       how="sum of the bars of panel C (certainty level of every findspot, the source included)",
       why=f"{Q4} {FIG}uncertainty.png, panel C: the figure covers all 79 findspots")
def fig_cert_total():
    t = dist("10-statistics/uncertainty.csv")
    return int(floats(t[t["recorded as"] == "certainty of the coordinate"]["count"]).sum())


@claim("F-05", "3.3", "findspots drawn in the distance figure", paper=None,
       source="dist/10-statistics/ci-distance.csv",
       how="findspots of the figure: all 79 less the source itself (the Phlegraean Fields, distance 0), so the level "
           "'medium' has 47 findspots there and 48 in the text",
       why=f"{Q4} {FIG}ci-distance.png: says why the figure and the text differ by one")
def fig_distance_n():
    return int(floats(dist("10-statistics/ci-distance.csv")["findspots"]).sum())


_REGIONS = (("F-06a", "Ireland", "306/375"), ("F-06b", "Wales", "1/47"), ("F-06c", "Scotland", "1/56"),
            ("F-06d", "England", "1/17"), ("F-06e", "Isle of Man", "2/9"))


def _region_claim(cid, region, paper):
    @claim(cid, "3.1", f"{region}: stones joined to Wikidata / all stones, from the regions figure", paper=paper,
           source="dist/10-statistics/ogham-regions.csv",
           how="dark part / full bar of the region in the figure",
           why=f"{Q2} {FIG}ogham-regions.png draws the regional gradient that the text states in numbers")
    def _f():
        t = dist("10-statistics/ogham-regions.csv")
        r = t[t["region"] == region].iloc[0]
        return f"{r['joined_to_wikidata']}/{r['stones']}"
    _f.__name__ = f"fig_region_{region.replace(' ', '_')}"
    return _f


for _a in _REGIONS:
    _region_claim(*_a)


@claim("F-07", "3.1", "stones held more than 100 km from their findspot, from the distance histogram", paper=94,
       source="dist/10-statistics/custody-distance.csv",
       how="sum of the dark bars (bins from 100 km) of the histogram",
       why=f"{Q2} {FIG}custody-distance.png: the histogram and the text count the same stones")
def fig_custody_over_100():
    t = dist("10-statistics/custody-distance.csv")
    return int(floats(t[floats(t["from_km"]) >= 100]["stones"]).sum())
