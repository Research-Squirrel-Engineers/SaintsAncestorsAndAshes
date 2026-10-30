# -*- coding: utf-8 -*-
"""
claims.saints -- the numbers of 2.1 (Saints) and 3.2 of the paper
==================================================================

Reads the step-04 tables under dist/04-saints/. They are built from the
Wikidata snapshots under data/raw/wikidata/ (see data/raw/README.md); the
snapshots are the raw data of this case, so the tables are the first place
where one can count by hand.
"""

from __future__ import annotations

import statistics

import networkx as nx

from .core import claim, dist, floats, pct

Q1 = "Q1 How dense is layer b?"
Q2 = "Q2 How unevenly is layer b spread?"
Q3 = "Q3 Which hubs carry layer b?"
Q4 = "Q4 How is uncertainty recorded?"
LA = "layer a (the network the data state)"


def _wells():
    return dist("04-saints/wells.csv")


def _saints():
    return dist("04-saints/saints.csv")


def _sources():
    return dist("04-saints/sources.csv")


# ----------------------------------------------------------------- 2.1 ---- #
@claim("S-01", "2.1", "holy wells in Ireland and the UK in the snapshots", paper=936, key="04:wells",
       source="dist/04-saints/wells.csv",
       how="distinct Wikidata items of holy wells found in any of the snapshots (data/raw/wikidata/holywells_*.json)",
       why="the denominator of every Saints percentage; says how large the case is")
def wells():
    return len(_wells())


@claim("S-02", "2.1", "wells with a coordinate and a namesake (P138)", paper=651, key="04:wells_with_namesake",
       source="dist/04-saints/wells.csv",
       how="wells with a coordinate and at least one 'named after' (P138) statement: the patron network",
       why=f"{LA}: the wells that can be joined to a saint and placed on a map")
def wells_with_namesake():
    w = _wells()
    return int(((w["namesakes"] != "") & (w["lat"] != "")).sum())


@claim("S-03", "2.1", "namesakes (saints)", paper=109, key="04:namesakes",
       source="dist/04-saints/saints.csv",
       how="distinct values of P138 among the wells of S-02", why=f"{LA}: the number of saint nodes")
def namesakes():
    return len(_saints())


# ----------------------------------------------------------------- 3.2 ---- #
@claim("S-04", "3.2", "wells named after Mary", paper=210, source="dist/04-saints/saints.csv",
       how="wells of the namesake 'Mary' in the patron network",
       why=f"{LA}: shows how unequal the saint distribution is (Q2 in layer a)")
def mary():
    s = _saints()
    return int(s.loc[s["label"] == "Mary", "wells"].iloc[0])


@claim("S-05", "3.2", "wells named after Brigid of Kildare", paper=157, source="dist/04-saints/saints.csv",
       how="wells of this namesake", why=f"{LA}: second-largest saint")
def brigid():
    s = _saints()
    return int(s.loc[s["label"] == "Brigid of Kildare", "wells"].iloc[0])


@claim("S-06", "3.2", "wells named after Saint Patrick", paper=25, source="dist/04-saints/saints.csv",
       how="wells of this namesake", why=f"{LA}: third-largest saint")
def patrick():
    s = _saints()
    return int(s.loc[s["label"] == "Saint Patrick", "wells"].iloc[0])


@claim("S-07", "3.2", "edges of the per-namesake minimum spanning trees", paper=561, key="04:mst_edges",
       source="dist/04-saints/edges_namesake_mst.csv",
       how="for each namesake the wells are joined by a minimum spanning tree over great-circle distances; "
           "rows of the edge list",
       why=f"{LA}: turns a list of wells into a regional network per saint")
def mst_edges():
    return len(dist("04-saints/edges_namesake_mst.csv"))


@claim("S-08", "3.2", "median spread of namesakes with at least three wells (km)", paper="62.8",
       key="04:spread_median_km_3plus", source="dist/04-saints/saints.csv",
       how="median of the radius of gyration (spread_km) of the wells of each namesake with at least 3 wells",
       why=f"{LA}: how local a saint's cult is; the paper contrasts this with the big three")
def spread_median():
    s = _saints()
    s = s[floats(s["wells"]) >= 3]
    return round(statistics.median(floats(s["spread_km"])), 1)


@claim("S-09a", "3.2", "spread of Saint Patrick's wells (km)", paper="75.1", key="04:spread_km_Q165479",
       source="dist/04-saints/saints.csv", how="radius of gyration of the wells of this namesake",
       why=f"{LA}: the big three are more widespread than the median saint")
def spread_patrick():
    s = _saints()
    return round(float(s.loc[s["label"] == "Saint Patrick", "spread_km"].iloc[0]), 1)


@claim("S-09b", "3.2", "spread of Mary's wells (km)", paper="107.8", key="04:spread_km_Q345",
       source="dist/04-saints/saints.csv", how="radius of gyration of the wells of this namesake",
       why=f"{LA}: see S-09a")
def spread_mary():
    s = _saints()
    return round(float(s.loc[s["label"] == "Mary", "spread_km"].iloc[0]), 1)


@claim("S-09c", "3.2", "spread of Brigid of Kildare's wells (km)", paper="108.8", key="04:spread_km_Q80979",
       source="dist/04-saints/saints.csv", how="radius of gyration of the wells of this namesake",
       why=f"{LA}: see S-09a")
def spread_brigid():
    s = _saints()
    return round(float(s.loc[s["label"] == "Brigid of Kildare", "spread_km"].iloc[0]), 1)


@claim("S-10", "3.2", "sources (P1343) that describe the wells", paper=183, key="04:sources",
       source="dist/04-saints/sources.csv",
       how="distinct values of 'described by source' (P1343) on the wells",
       why=f"{LA}: sources are Wikidata items themselves, so sources, wells and saints form one graph")
def sources():
    return len(_sources())


@claim("S-11", "3.2", "well-source statements", paper="3,294", key="04:source_statements",
       source="dist/04-saints/edges_well_source.csv", how="rows of the well-source edge list",
       why=f"{LA}: the number of edges between wells and sources")
def well_source_edges():
    return len(dist("04-saints/edges_well_source.csv"))


@claim("S-12", "3.2", "wells with at least one source", paper=728, key="04:wells_with_source",
       source="dist/04-saints/edges_well_source.csv",
       how="distinct wells in the well-source edge list", why=f"{LA}: how well documented the wells are")
def wells_with_source():
    return dist("04-saints/edges_well_source.csv")["well"].nunique()


@claim("S-13", "3.2", "connected components of the source projection", paper=3, key="04:source_projection_components",
       source="dist/04-saints/edges_well_source.csv",
       how="one-mode projection of the well-source graph onto the sources (two sources are joined if they describe "
           "a common well); components counted with networkx",
       why=f"{LA}: the sources form one large block and two small ones")
def source_components():
    e = dist("04-saints/edges_well_source.csv")
    g = nx.Graph()
    g.add_edges_from(zip(e["well"], e["source"]))
    srcs = set(e["source"])
    comps = [c for c in nx.connected_components(g)]
    # a well always sits in the component of its sources: count components that hold a source
    return sum(1 for c in comps if c & srcs)


@claim("S-14a", "3.2", "wells described by 'Historic Environment Viewer (Ireland)'", paper=585,
       source="dist/04-saints/sources.csv", how="wells of this source (sources.csv, column wells)",
       why=f"{LA}: the source that describes most wells")
def src_hev():
    s = _sources()
    return int(s.loc[s["label"] == "Historic Environment Viewer (Ireland)", "wells"].iloc[0])


@claim("S-14b", "3.2", "wells described by the 6 Inch First Edition Ordnance Survey map of Ireland", paper=495,
       source="dist/04-saints/sources.csv", how="wells of this source", why=f"{LA}: second-largest source")
def src_os1():
    s = _sources()
    return int(s.loc[s["label"] == "6 Inch First Edition Ordnance Survey map of Ireland", "wells"].iloc[0])


@claim("S-14c", "3.2", "wells described by the 2nd edition Ordnance Survey map of Ireland", paper=422,
       source="dist/04-saints/sources.csv", how="wells of this source", why=f"{LA}: third-largest source")
def src_os2():
    s = _sources()
    return int(s.loc[s["label"] == "2nd edition Ordnance Survey map of Ireland", "wells"].iloc[0])


@claim("S-15", "3.2", "sources that describe a single well", paper=98, key="04:sources_single_well",
       source="dist/04-saints/sources.csv", how="sources with wells = 1",
       why=f"{LA}: the long tail of sources")
def sources_single():
    return int((floats(_sources()["wells"]) == 1).sum())


@claim("S-16", "3.2", "namesakes with 20 or more wells that are in the GND", paper="5 of 5",
       key="", source="dist/04-saints/saints.csv",
       how="namesakes with at least 20 wells, and how many of them have a GND record (authorities column)",
       why=f"{Q2} authority files follow renown: every big saint has one")
def big_in_gnd():
    s = _saints()
    big = s[floats(s["wells"]) >= 20]
    return f"{int(big['authorities'].str.split(';').map(lambda a: 'GND' in a).sum())} of {len(big)}"


@claim("S-17a", "3.2", "namesakes with a single well", paper=63, key="04:namesakes_1_wells",
       source="dist/04-saints/saints.csv", how="namesakes with exactly one well (wells = 1)",
       why=f"{Q2} the denominator of S-17: most saints are local")
def single_namesakes():
    return int((floats(_saints()["wells"]) == 1).sum())


@claim("S-17", "3.2", "namesakes with a single well that are in the GND (%)", paper="27.0",
       key="08:namesakes_1_well_gnd_pct", source="dist/04-saints/saints.csv",
       how="namesakes with exactly one well that have a GND record, divided by all such namesakes (63)",
       why=f"{Q2} the contrast to S-16: local saints are rarely in the authority files")
def single_in_gnd():
    s = _saints()
    one = s[floats(s["wells"]) == 1]
    return pct(one["authorities"].str.split(";").map(lambda a: "GND" in a).sum(), len(one))


@claim("S-18", "3.2", "namesakes in none of GND, VIAF and LoC", paper=65, key="04:lod_namesakes_without_authority",
       source="dist/04-saints/saints.csv", how="namesakes with an empty authorities column",
       why=f"{Q2} the share of saints that the authority files do not know")
def no_authority():
    return int((_saints()["authorities"] == "").sum())


@claim("S-19", "3.2", "share of namesakes in none of GND, VIAF and LoC (%)", paper="59.6", key="",
       source="dist/04-saints/saints.csv", how="S-18 divided by S-03", why=f"{Q2} same as S-18 as a share")
def no_authority_pct():
    return pct(no_authority(), namesakes())


@claim("S-20", "3.2", "female namesakes", paper=40, key="04:namesakes_female", source="dist/04-saints/saints.csv",
       how="namesakes with gender 'female' (Wikidata sex or gender)", why=f"{LA}: gender balance of the saints")
def female():
    return int((_saints()["gender"] == "female").sum())


def _wells_by_gender(gender):
    s = _saints().set_index("node")["gender"]
    e = dist("04-saints/edges_well_namesake.csv")
    return e[e["namesake"].map(s) == gender]["well"].nunique()


@claim("S-21a", "3.2", "wells named after women", paper=511, key="04:wells_female_namesake",
       source="dist/04-saints/edges_well_namesake.csv, saints.csv",
       how="distinct wells with at least one female namesake", why=f"{LA}: Mary and Brigid dominate")
def wells_female():
    return _wells_by_gender("female")


@claim("S-21b", "3.2", "wells named after men", paper=151, key="04:wells_male_namesake",
       source="dist/04-saints/edges_well_namesake.csv, saints.csv",
       how="distinct wells with at least one male namesake", why=f"{LA}: see S-21a")
def wells_male():
    return _wells_by_gender("male")


@claim("S-22", "3.2", "external records on the wells", paper="1,999", key="04:lod_well_records",
       source="dist/04-saints/wells.csv",
       how="sum over the wells of the number of external records (identifiers in the hubs)",
       why=f"{Q1} the wells are richly linked: layer b is dense here")
def well_records():
    return int(floats(_wells()["records"]).sum())


@claim("S-23", "3.2", "share of wells with an SMR (Ireland) record (%)", paper="80.9", key="",
       source="dist/04-saints/wells.csv",
       how="wells whose hubs include 'SMR (Ireland)', divided by all wells",
       why=f"{Q3} the Irish Sites and Monuments Record is the largest hub for the wells")
def wells_smr():
    w = _wells()
    return pct(w["hubs"].str.contains("SMR \\(Ireland\\)").sum(), len(w))


@claim("S-24", "3.2", "share of wells with an OpenStreetMap link (%)", paper="69.9", key="",
       source="dist/04-saints/wells.csv",
       how="wells whose hubs include 'OpenStreetMap', divided by all wells",
       why=f"{Q3} OSM is the second hub for the wells and the only hub shared by all three cases")
def wells_osm():
    w = _wells()
    return pct(w["hubs"].str.contains("OpenStreetMap").sum(), len(w))


@claim("S-25", "3.2", "wells without any external record", paper=37, key="04:lod_wells_without_external_record",
       source="dist/04-saints/wells.csv", how="wells with records = 0",
       why=f"{Q1} only a few wells are not linked at all")
def wells_no_record():
    return int((floats(_wells()["records"]) == 0).sum())


@claim("S-26", "3.2", "share of wells without any external record (%)", paper="4.0", key="",
       source="dist/04-saints/wells.csv", how="S-25 divided by S-01", why=f"{Q1} same as S-25 as a share")
def wells_no_record_pct():
    return pct(wells_no_record(), wells())
