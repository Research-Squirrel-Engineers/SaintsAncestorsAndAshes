# -*- coding: utf-8 -*-
"""
claims.paper_text -- numbers that entered the final text and had no claim yet
==============================================================================

The institutions (3.1), the spread of women's and men's wells (3.2), the doubt
counts and the threshold example of 3.5. Every value is counted from the tables
of the steps, so that the sentence of the text can be checked against its source.

Not covered here: the five readings of Gigha 1 (weights 0.27, 0.27, 0.18, 0.18,
0.09). They come from the prototype tei--epidoc-amt (a separate repository, four
stones), not from this pipeline.
"""

from __future__ import annotations

import statistics

import networkx as nx

from .core import claim, dist, floats, pct, raw

LA = "layer a (the network the data state)"
Q1 = "Q1 How dense is layer b?"
Q2 = "Q2 How unevenly is layer b spread?"
Q4 = "Q4 How is uncertainty recorded?"


# ------------------------------------------------------------ 3.1 -------- #
def _top_three():
    vc = raw("ogham/keepers.csv")["keeper"].value_counts()
    return int(vc.iloc[:3].sum()), int(vc.sum())


@claim("T-01", "3.1", "stones held by the three largest institutions", paper=117, source="data/raw/ogham/keepers.csv",
       how="the three largest values of the keeper counts (National Museum of Ireland 64, University College Cork "
           "28, National Museums of Scotland 25) added up",
       why=f"{LA}, custody: a few national holders keep most of the stones")
def top_three():
    return _top_three()[0]


@claim("T-02", "3.1", "share of the held stones that the three largest institutions keep (%)", paper="64.3",
       source="data/raw/ogham/keepers.csv", how="T-01 divided by all stones with a known keeper (A-10)",
       why=f"{LA}, custody: see T-01")
def top_three_pct():
    a, b = _top_three()
    return pct(a, b)


# ------------------------------------------------------------ 3.2 -------- #
def _spread_by_gender(gender):
    s = dist("04-saints/saints.csv")
    s = s[(s["gender"] == gender) & (floats(s["wells"]) >= 3)]
    return len(s), round(statistics.median(floats(s["spread_km"])), 1)


@claim("T-03", "3.2", "female namesakes with at least three wells", paper=15, source="dist/04-saints/saints.csv",
       how="namesakes with gender 'female' and at least 3 wells", why=f"{LA}: the group behind the women/men contrast")
def women_n():
    return _spread_by_gender("female")[0]


@claim("T-04", "3.2", "male namesakes with at least three wells", paper=15, source="dist/04-saints/saints.csv",
       how="namesakes with gender 'male' and at least 3 wells", why=f"{LA}: see T-03")
def men_n():
    return _spread_by_gender("male")[0]


@claim("T-05", "3.2", "median spread of female namesakes with at least three wells (km)", paper="87.7",
       source="dist/04-saints/saints.csv",
       how="median of the radius of gyration (spread_km) over the namesakes of T-03",
       why=f"{LA}: in these data the networks of female saints are wider (Mary and Brigid are among them)")
def women_spread():
    return _spread_by_gender("female")[1]


@claim("T-06", "3.2", "median spread of male namesakes with at least three wells (km)", paper="34.3",
       source="dist/04-saints/saints.csv", how="median of the radius of gyration over the namesakes of T-04",
       why=f"{LA}: see T-05")
def men_spread():
    return _spread_by_gender("male")[1]


# ------------------------------------------------------------ 3.5 -------- #
def _unc(recorded, value):
    t = dist("10-statistics/uncertainty.csv")
    return int(floats(t[(t["recorded as"] == recorded) & (t["value"] == value)]["count"]).sum())


@claim("T-07", "3.5", "kinship statements with the AMT weight 1.00", paper=96, source="dist/10-statistics/uncertainty.csv",
       how="statements with amt_weight 1.00 (116 less the 20 of A-09)", why=f"{Q4} Ancestors: the two weights")
def w100():
    return _unc("AMT weight", "1.00")


@claim("T-08", "3.5", "findspots with a spatially close match", paper=14, source="dist/10-statistics/uncertainty.csv",
       how="rows of the CI table with relatedtohow fsl:spatialCloseMatch", why=f"{Q4} Ashes: match type")
def m_spatial():
    return _unc("match type of the link", "fsl:spatialCloseMatch")


@claim("T-09", "3.5", "findspots with a partial match", paper=5, source="dist/10-statistics/uncertainty.csv",
       how="rows of the CI table with relatedtohow fsl:partlyMatch", why=f"{Q4} Ashes: match type")
def m_partial():
    return _unc("match type of the link", "fsl:partlyMatch")


@claim("T-10", "3.5", "findspots with a dubious match", paper=4, source="dist/10-statistics/uncertainty.csv",
       how="rows of the CI table with relatedtohow fsl:dubiousMatch", why=f"{Q4} Ashes: match type")
def m_dubious():
    return _unc("match type of the link", "fsl:dubiousMatch")


@claim("T-11", "3.5", "findspots whose coordinate has a lower certainty level or none", paper=17,
       source="dist/10-statistics/uncertainty.csv",
       how="all findspots less those with the level high (14) and medium (48): low, representative, dubious, "
           "not stated",
       why=f"{Q4} Ashes: certainty of the coordinate; the text says 'lower or not stated for the remaining 17'")
def cert_rest():
    return sum(_unc("certainty of the coordinate", v) for v in ("low", "representative", "dubious", "not stated"))


def _groups(weight_only):
    k = dist("03-ancestors/edges_kinship.csv")
    if weight_only is not None:
        k = k[k["amt_weight"] == weight_only]
    g = nx.Graph()
    for _, r in k.iterrows():
        g.add_edge(r["person_1"], r["person_2"])
        g.add_edge("stone_" + r["stone"], r["person_1"])
        g.add_edge("stone_" + r["stone"], r["person_2"])
    cs = [c for c in nx.connected_components(g) if sum(x.startswith("stone_") for x in c) > 1]
    return len(cs), sum(sum(x.startswith("stone_") for x in c) for c in cs)


@claim("T-12", "3.5", "groups of stones that the kinship statements join (all statements)", paper=7,
       source="dist/03-ancestors/edges_kinship.csv",
       how="graph of the statements (person to person) with each stone joined to the persons it names; components "
           "that contain more than one stone",
       why=f"{Q4} threshold example: the weights change the network")
def groups_all():
    return _groups(None)[0]


@claim("T-13", "3.5", "stones in those groups (all statements)", paper=17, source="dist/03-ancestors/edges_kinship.csv",
       how="stone nodes in the components of T-12", why=f"{Q4} see T-12")
def stones_all():
    return _groups(None)[1]


@claim("T-14", "3.5", "groups of stones when only statements with weight 1.00 count", paper=4,
       source="dist/03-ancestors/edges_kinship.csv", how="as T-12 on the statements with amt_weight 1.00",
       why=f"{Q4} see T-12")
def groups_100():
    return _groups("1.00")[0]


@claim("T-15", "3.5", "stones in those groups (weight 1.00 only)", paper=10, source="dist/03-ancestors/edges_kinship.csv",
       how="stone nodes in the components of T-14", why=f"{Q4} see T-12")
def stones_100():
    return _groups("1.00")[1]


# ------------------------------------------------------------ 3.2, 3.4 -- #
@claim("T-16", "3.4", "share of wells with at least one external identifier record (%)", paper="96.0",
       source="dist/04-saints/wells.csv",
       how="wells with records above 0 (the identifiers on the well item), divided by all wells (S-01); the same "
           "wells as 'only 37 wells have no external record' (S-25, S-26) in 3.2",
       why=f"{Q2} nearly every well has an external record; the number agrees with 3.2")
def wells_with_record():
    w = dist("04-saints/wells.csv")
    return pct(int((floats(w["records"]) > 0).sum()), len(w))


@claim("T-17", "3.2", "wells with both a female and a male namesake", paper=11,
       source="dist/04-saints/edges_well_namesake.csv, saints.csv",
       how="wells that have at least one female and at least one male namesake (511 + 151 - 11 = 651 wells)",
       why=f"{LA}: the counts of wells named after women and after men overlap by these wells")
def wells_both():
    s = dist("04-saints/saints.csv").set_index("node")["gender"]
    e = dist("04-saints/edges_well_namesake.csv")
    g = e.assign(g=e["namesake"].map(s)).groupby("well")["g"].apply(set)
    return sum(1 for x in g if {"female", "male"} <= x)


@claim("T-18", "3.4", "share of CI findspots with a link to a hub other than fuzzy-sl (%)", paper="100.0",
       source="dist/05-ashes/edges_findspot_hub.csv, findspots.csv",
       how="findspots with at least one link to Wikidata, OpenStreetMap, GeoNames or Wikipedia, divided by all "
           "findspots; the five findspots that exist only in fuzzy-sl are counted only if they have such a link",
       why=f"{Q1} the 100 % of 3.4 does not rest on fuzzy-sl being the home dataset of five findspots")
def ci_external_share():
    f = dist("05-ashes/findspots.csv")
    e = dist("05-ashes/edges_findspot_hub.csv")
    return pct(e[e["hub"] != "fuzzy-sl"]["findspot"].nunique(), len(f))
