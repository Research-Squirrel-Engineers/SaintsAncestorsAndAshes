# -*- coding: utf-8 -*-
"""
claims.ashes -- the numbers of 2.1 (Ashes) and 3.3 of the paper
================================================================

Reads the CI findspot table under data/raw/ci/ (74 rows) and the step-05 tables
under dist/05-ashes/ (79 findspots: the 74 plus 5 that exist only in fuzzy-sl).
"""

from __future__ import annotations

import statistics

import networkx as nx

from .core import claim, dist, floats, pct, raw

Q1 = "Q1 How dense is layer b?"
Q2 = "Q2 How unevenly is layer b spread?"
Q3 = "Q3 Which hubs carry layer b?"
Q4 = "Q4 How is uncertainty recorded?"
LA = "layer a (the network the data state)"


def _fs():
    return dist("05-ashes/findspots.csv")


def _hub():
    return dist("05-ashes/edges_findspot_hub.csv")


def _external():
    """The links to external hubs (the links to fuzzy-sl items are drawn in the flow figure but are not external)."""
    h = _hub()
    return h[h["hub"] != "fuzzy-sl"]


def _linked(hub):
    return _external().query("hub == @hub")["findspot"].nunique()


@claim("C-01", "2.1", "findspots in the CI table", paper=74, key="05:findspots_csv",
       source="data/raw/ci/ci_findspots.csv", how="rows of ci_findspots.csv",
       why="the home dataset of the case (Thiery and Schenk 2023a)")
def findspots_csv():
    return len(raw("ci/ci_findspots.csv"))


@claim("C-02", "2.1", "findspots that exist only in the fuzzy-sl Wikibase", paper=5, key="05:findspots_fuzzysl_only",
       source="dist/05-ashes/findspots.csv", how="findspots with origin 'fuzzy-sl' (chosen by the statement "
       "'part of Campanian Ignimbrite Findspots'; list in data/raw/manual/ci_fuzzysl_only.yaml)",
       why="the case includes both datasets ('gerne beide'); the paper states the extension")
def findspots_fuzzysl():
    return int((_fs()["origin"] == "fuzzy-sl").sum())


@claim("C-03", "2.1", "findspots in total", paper=79, key="05:findspots", source="dist/05-ashes/findspots.csv",
       how="rows of findspots.csv (C-01 plus C-02)",
       why="the denominator of every Ashes percentage; also the reason a single findspot moves a percentage by more than one point")
def findspots():
    return len(_fs())


@claim("C-04", "3.3", "publications that report the findspots", paper=34, key="05:publications",
       source="dist/05-ashes/publications.csv",
       how="distinct publications after normalising the literature column (37 spellings of 32 publications in the "
           "table, plus those of the fuzzy-sl findspots)",
       why=f"{LA}: the second node type of the findspot-publication network")
def publications():
    return len(dist("05-ashes/publications.csv"))


@claim("C-05", "3.3", "citations (findspot-publication edges)", paper=106, key="05:citations",
       source="dist/05-ashes/edges_findspot_publication.csv", how="rows of the edge list",
       why=f"{LA}: the number of edges of the two-mode network")
def citations():
    return len(dist("05-ashes/edges_findspot_publication.csv"))


@claim("C-06", "3.3", "findspots that rest on a single publication", paper=57, key="05:findspots_with_one_publication",
       source="dist/05-ashes/edges_findspot_publication.csv",
       how="findspots with exactly one edge in the findspot-publication list",
       why=f"{LA}: most findspots depend on one source, so the network is sparse")
def findspots_one_pub():
    e = dist("05-ashes/edges_findspot_publication.csv")
    return int((e.groupby("findspot").size() == 1).sum())


def _pub_graph():
    e = dist("05-ashes/edges_publication_projection.csv")
    g = nx.Graph()
    g.add_nodes_from(dist("05-ashes/publications.csv")["publication"])
    g.add_edges_from(zip(e["publication_1"], e["publication_2"]))
    return g


@claim("C-07", "3.3", "components of the publication projection", paper=11, key="05:projection_components",
       source="dist/05-ashes/publications.csv, edges_publication_projection.csv",
       how="one-mode projection onto the publications (joined when they report a common findspot); components "
           "counted with networkx, isolated publications included",
       why=f"{LA}: the literature falls into few clusters")
def pub_components():
    return nx.number_connected_components(_pub_graph())


@claim("C-08", "3.3", "publications in the largest component", paper=23, key="05:projection_largest_component",
       source="dist/05-ashes/edges_publication_projection.csv", how="size of the largest component of C-07",
       why=f"{LA}: one core of the literature")
def pub_largest():
    return max(len(c) for c in nx.connected_components(_pub_graph()))


@claim("C-09", "3.3", "publications that share no findspot", paper=9, key="05:projection_isolates",
       source="dist/05-ashes/edges_publication_projection.csv", how="isolated nodes of the projection",
       why=f"{LA}: publications that stand alone")
def pub_isolates():
    return sum(1 for n in _pub_graph() if _pub_graph().degree(n) == 0)


@claim("C-10", "3.3", "median distance of a findspot to the Phlegraean Fields (km)", paper="123.9",
       key="05:distance_median_km", source="dist/05-ashes/findspots.csv",
       how="median of distance_km (great-circle, to the findspot 'Phlegraean Fields'), the source itself excluded",
       why=f"{LA}: how far the tephra travelled, in the record")
def distance_median():
    f = _fs()
    f = f[f["label"] != "Phlegraean Fields"]
    return round(statistics.median(floats(f["distance_km"])), 1)


@claim("C-11", "3.3", "distance of the most distant findspot (km)", paper="2,752.5", key="05:distance_max_km",
       source="dist/05-ashes/findspots.csv", how="maximum of distance_km", why=f"{LA}: the reach of the record")
def distance_max():
    return round(floats(_fs()["distance_km"]).max(), 1)


@claim("C-12a", "3.3", "findspots with medium location certainty", paper=48, key="05:certainty_medium",
       source="dist/05-ashes/findspots.csv", how="findspots with certainty 'medium' (CSV certainty or fuzzy-sl level)",
       why=f"{Q4} the CI case records uncertainty as a certainty level per coordinate")
def certainty_medium():
    return int((_fs()["certainty"] == "medium").sum())


@claim("C-12b", "3.3", "findspots with high location certainty", paper=14, key="05:certainty_high",
       source="dist/05-ashes/findspots.csv", how="findspots with certainty 'high'", why=f"{Q4} see C-12a")
def certainty_high():
    return int((_fs()["certainty"] == "high").sum())


@claim("C-13", "3.3", "external links of layer b", paper=108, key="05:lod_links",
       source="dist/05-ashes/edges_findspot_hub.csv",
       how="rows of the findspot-hub list that point to an external hub (Wikidata, OpenStreetMap, GeoNames, "
           "Wikipedia); the 19 links to fuzzy-sl items are not counted",
       why=f"{Q1} the size of layer b in the CI case")
def links():
    return len(_external())


@claim("C-14", "3.3", "external links per findspot (mean)", paper="1.37", key="05:lod_links_per_findspot",
       source="dist/05-ashes/edges_findspot_hub.csv", how="C-13 divided by C-03", why=f"{Q1} density of layer b")
def links_per_findspot():
    return round(links() / findspots(), 2)


@claim("C-15a", "3.3", "findspots linked to Wikidata (%)", paper="60.8", key="",
       source="dist/05-ashes/edges_findspot_hub.csv", how="distinct findspots with a Wikidata link / all findspots",
       why=f"{Q3} Wikidata is the main hub of the CI case")
def pct_wikidata():
    return pct(_linked("Wikidata"), findspots())


@claim("C-15b", "3.3", "findspots linked to OpenStreetMap (%)", paper="45.6", key="",
       source="dist/05-ashes/edges_findspot_hub.csv", how="distinct findspots with an OSM link / all findspots",
       why=f"{Q3} OSM, the hub shared by all cases")
def pct_osm():
    return pct(_linked("OpenStreetMap"), findspots())


@claim("C-15c", "3.3", "findspots linked to GeoNames (%)", paper="29.1", key="",
       source="dist/05-ashes/edges_findspot_hub.csv", how="distinct findspots with a GeoNames link / all findspots",
       why=f"{Q3} the gazetteer of the CI case")
def pct_geonames():
    return pct(_linked("GeoNames"), findspots())


@claim("C-16", "3.3", "findspots typed as archaeological sites", paper=13, key="05:archaeological_sites",
       source="dist/05-ashes/findspots.csv",
       how="findspots whose spatial type includes fsl:ArchaeologicalSite (the 9 of the table plus those of fuzzy-sl)",
       why=f"{Q2} coverage depends on the kind of site")
def arch_sites():
    return int((_fs()["archaeological"] == "True").sum())


@claim("C-17", "3.3", "archaeological sites linked to Wikidata", paper=12, key="05:lod_wikidata_archaeological",
       source="dist/05-ashes/findspots.csv, edges_findspot_hub.csv",
       how="archaeological sites (C-16) with a Wikidata link",
       why=f"{Q2} archaeological sites are almost all in Wikidata")
def arch_wikidata():
    f = _fs()
    arch = set(f.loc[f["archaeological"] == "True", "node"])
    e = _external()
    return e[(e["hub"] == "Wikidata") & e["findspot"].isin(arch)]["findspot"].nunique()


@claim("C-18", "3.3", "share of archaeological sites linked to Wikidata (%)", paper="92.3", key="",
       source="see C-17", how="C-17 divided by C-16", why=f"{Q2} same as C-17 as a share")
def arch_wikidata_pct():
    return pct(arch_wikidata(), arch_sites())


@claim("C-19", "3.3", "findspots of the table with a close match", paper=51, key="05:match_closeMatch",
       source="data/raw/ci/ci_findspots.csv", how="rows with relatedtohow = skos:closeMatch",
       why=f"{Q4} the CI case records uncertainty as a match type per link")
def close_match():
    return int((raw("ci/ci_findspots.csv")["relatedtohow"] == "skos:closeMatch").sum())


@claim("C-20", "3.3", "findspots of the table with a weaker or doubtful match", paper=23, key="05:match_not_close",
       source="data/raw/ci/ci_findspots.csv",
       how="rows with relatedtohow other than skos:closeMatch (fsl:spatialCloseMatch, fsl:partlyMatch, "
           "fsl:dubiousMatch)",
       why=f"{Q4} see C-19")
def weak_match():
    return int((raw("ci/ci_findspots.csv")["relatedtohow"] != "skos:closeMatch").sum())


@claim("C-21", "3.3", "share of table findspots with a weaker or doubtful match (%)", paper="31.1", key="",
       source="data/raw/ci/ci_findspots.csv", how="C-20 divided by C-01", why=f"{Q4} see C-19")
def weak_match_pct():
    return pct(weak_match(), findspots_csv())


@claim("C-22", "3.3", "fuzzy-sl items that are members of the CI findspot collection", paper=19,
       key="05:fuzzysl_ci_members", source="dist/05-ashes/edges_findspot_hub.csv",
       how="findspots with a link to a fuzzy-sl item (hub 'fuzzy-sl')",
       why=f"{Q3} the fuzzy-sl Wikibase as a domain hub of the case")
def fuzzysl_members():
    return _hub().query("hub == 'fuzzy-sl'")["findspot"].nunique()


@claim("C-23", "3.3", "external links that fuzzy-sl adds to those of the table", paper=1, key="05:fuzzysl_new_resources",
       source="dist/05-ashes/fuzzysl_matches.csv",
       how="external resources recorded on a matched fuzzy-sl item and not in the CSV (column "
           "resources_only_in_fuzzysl, counted per resource)",
       why=f"{Q1} the fuzzy-sl Wikibase adds almost nothing to layer b")
def fuzzysl_new():
    m = dist("05-ashes/fuzzysl_matches.csv")["resources_only_in_fuzzysl"]
    return int(m.map(lambda s: len([x for x in s.split(";") if x])).sum())


@claim("C-24", "3.3", "external resources linked from findspots more than 100 km apart", paper=1,
       key="05:suspicious_shared_links", source="dist/05-ashes/suspicious_links.csv",
       how="OSM/Wikidata/GeoNames resources shared by two findspots whose coordinates are more than 100 km "
           "apart (Phlegraean Fields and Crvena Stijena: 420.1 km)",
       why="layer b exposed an error in layer a (Discussion: 'Layer B is a probe of layer A')")
def suspicious():
    s = dist("05-ashes/suspicious_links.csv")
    return int((floats(s["distance_km"]) > 100).sum())
