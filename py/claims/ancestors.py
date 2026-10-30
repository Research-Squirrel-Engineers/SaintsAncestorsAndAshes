# -*- coding: utf-8 -*-
"""
claims.ancestors -- the numbers of 2.1 (Ancestors) and 3.1 of the paper
========================================================================

Reads the OG(H)AM tables under data/raw/ogham/ and the step-03 tables under
dist/03-ancestors/. Where the raw table is enough (stones, keepers, kinship
statements) the number is counted from the raw table, so that it is checked
against the pipeline and not just copied from it.
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


def _stones():
    return raw("ogham/places.csv")


def _kin():
    return dist("03-ancestors/edges_kinship.csv")


# ----------------------------------------------------------------- 2.1 ---- #
@claim("A-01", "2.1", "stones in the Ogham corpus", paper=504, key="03:stones",
       source="data/raw/ogham/places.csv",
       how="rows of places.csv: one row per stone of the OG(H)AM EpiDoc edition",
       why="the denominator of every Ancestors percentage; says how large the case is")
def stones():
    return len(_stones())


# ----------------------------------------------------------------- 3.1 ---- #
@claim("A-02", "3.1", "stones that carry at least one kinship statement", paper=107, key="03:stones_with_kinship",
       source="data/raw/ogham/persons.csv",
       how="distinct stone ids in persons.csv (a stone counts once however many statements it carries)",
       why=f"{LA}: shows that only a fifth of the corpus has a kinship formula at all")
def stones_with_kinship():
    return raw("ogham/persons.csv")["stone"].nunique()


@claim("A-03", "3.1", "share of stones with a kinship statement (%)", paper="21.2", key="",
       source="data/raw/ogham/persons.csv, places.csv",
       how="A-02 divided by A-01",
       why=f"{LA}: the same point as A-02 as a share")
def stones_with_kinship_pct():
    return pct(stones_with_kinship(), stones())


@claim("A-04", "3.1", "kinship statements", paper=116, key="03:kinship_statements",
       source="data/raw/ogham/persons.csv",
       how="rows of persons.csv: one row per reified statement 'person X is son/grandson/... of Y' on a stone",
       why=f"{LA}: the number of edges of the kinship network")
def kinship_statements():
    return len(raw("ogham/persons.csv"))


RELATIONS = (("A-05a", "son of", 89), ("A-05b", "of the kin of", 13), ("A-05c", "descendant of", 9),
             ("A-05d", "client of", 3), ("A-05e", "here lies", 1), ("A-05f", "unstated", 1))


def _relation_claim(cid, word, paper):
    @claim(cid, "3.1", f"statements whose first relation is '{word}'", paper=paper,
           source="dist/03-ancestors/edges_kinship.csv",
           how="the first relation of each formula, by the lemma: maqqas = son of, muccoviias = of the kin of, "
               "avias = descendant of, celias = client of, koi = here lies; none of these = unstated "
               "(rule: py/step_03_ancestors.py::_relation)",
           why=f"{LA}: which kinds of relation the stones state; the formula words are the edge types")
    def _f():
        return int((_kin()["relation"] == word).sum())
    _f.__name__ = f"relation_{word.replace(' ', '_')}"
    return _f


for _cid, _word, _paper in RELATIONS:
    _relation_claim(_cid, _word, _paper)


FORMULA_WORDS = (("A-26a", "son of", "maqi", "MAQI", "maqi"), ("A-26b", "of the kin of", "mucoi", "MUCOI", "mucoi"),
                 ("A-26c", "descendant of", "avi", "AVI", "avi"), ("A-26d", "client of", "celi", "CELI", "celi"),
                 ("A-26e", "here lies", "koi", "KOI", "koi"))


def _formula_claim(cid, relation, paper, word, shown):
    @claim(cid, "3.1", f"the formula word written in the text for '{relation}'", paper=paper,
           source="data/raw/ogham/words.csv",
           how=f"the formula word of the relation '{relation}' in the edition's word list ({word}; the text writes "
               "it lowercase and in italics, as '" + shown + "'); the check is that the word occurs in words.csv as a "
               "formula and returns it in the form the text should use",
           why=f"{LA}: the formula words are the edge types of the kinship network; the text names each one")
    def _f():
        w = raw("ogham/words.csv")
        assert (w["word"] == word).sum() > 0, f"{word} not in words.csv"
        return word.lower()
    _f.__name__ = f"formula_{shown}"
    return _f


for _a in FORMULA_WORDS:
    _formula_claim(*_a)


def _kin_graph():
    """Stones and the persons they name, joined by the kinship statements (as in step 03)."""
    p = dist("03-ancestors/persons.csv")
    g = nx.Graph()
    for _, r in p.iterrows():
        for s in filter(None, r["stones"].split(";")):
            g.add_edge("stone_" + s, r["node"])
    for _, r in _kin().iterrows():
        g.add_edge(r["person_1"], r["person_2"])
    comps = list(nx.connected_components(g))
    n_stones = lambda c: sum(1 for x in c if x.startswith("stone_"))
    cross = [c for c in comps if n_stones(c) > 1]
    return p, comps, cross, n_stones


@claim("A-06", "3.1", "connected components of the kinship network", paper=208, key="03:kinship_components",
       source="dist/03-ancestors/persons.csv, edges_kinship.csv",
       how="graph with stone nodes and person nodes; a stone is joined to every person it names, and persons are "
           "joined by the kinship statements; components counted with networkx",
       why=f"{LA}: the headline finding that the kinship network is fragmented")
def kin_components():
    return len(_kin_graph()[1])


@claim("A-07", "3.1", "components that reach beyond a single stone", paper=8, key="03:kinship_components_across_stones",
       source="dist/03-ancestors/persons.csv, edges_kinship.csv",
       how="components of A-06 that contain more than one stone node",
       why=f"{LA}: only these components are a network in the sense of linking stones; all others are one stone")
def kin_components_across():
    return len(_kin_graph()[2])


@claim("A-08", "3.1", "names or kin groups that recur on more than one stone", paper=12,
       key="03:names_on_several_stones", source="dist/03-ancestors/persons.csv",
       how="person and kin-group nodes of persons.csv whose stone list has more than one stone",
       why=f"{LA}: these recurring names are the only joints between stones; the paper says 'joined by 12'")
def names_on_several_stones():
    p = _kin_graph()[0]
    return int(p["stones"].str.contains(";").sum())


@claim("A-09", "3.1", "kinship statements with an AMT weight below 1.0", paper=20,
       key="03:kinship_statements_weight_below_1", source="dist/03-ancestors/edges_kinship.csv",
       how="statements whose Academic Meta Tool weight (amt_weight) is less than 1.0; the crosswalk "
           "(tei--epidoc-crosswalk, py/persons.py) gives 0.90 where the lemma in the edition ends with a question "
           "mark and 1.00 otherwise",
       why=f"{Q4} Ancestors records doubt as an AMT weight on each statement")
def kinship_weight_below_1():
    return int((floats(_kin()["amt_weight"]) < 1.0).sum())


@claim("A-10", "3.1", "stones held by an institution today", paper=182, key="03:stones_in_institutions",
       source="data/raw/ogham/keepers.csv",
       how="rows of keepers.csv: one row per stone with a known keeper",
       why=f"{LA}, custody: the second relation of the case (findspot to institution)")
def stones_held():
    return len(raw("ogham/keepers.csv"))


@claim("A-11", "3.1", "median distance findspot to institution (km)", paper="110.4",
       key="03:custody_distance_median_km", source="data/raw/ogham/keepers.csv",
       how="median of distance_km: great-circle distance between the findspot and the keeper's coordinates "
           "(haversine, as in py/network_utils.py::haversine_km), over the 182 stones",
       why=f"{LA}, custody: shows that stones are often far from where they were found")
def custody_median():
    return round(statistics.median(floats(raw("ogham/keepers.csv")["distance_km"])), 1)


@claim("A-12", "3.1", "stones held more than 100 km from their findspot", paper=94, key="03:custody_over_100_km",
       source="data/raw/ogham/keepers.csv",
       how="rows of keepers.csv with distance_km above 100",
       why=f"{LA}, custody: the same point as A-11, as a count")
def custody_over_100():
    return int((floats(raw("ogham/keepers.csv")["distance_km"]) > 100).sum())


@claim("A-13a", "3.1", "stones held by the National Museum of Ireland", paper=64, source="data/raw/ogham/keepers.csv",
       how="rows of keepers.csv with this keeper",
       why=f"{LA}, custody: the largest holder; the paper names the three largest")
def keeper_nmi():
    return int((raw("ogham/keepers.csv")["keeper"] == "National Museum of Ireland").sum())


@claim("A-13b", "3.1", "stones held by University College Cork", paper=28, source="data/raw/ogham/keepers.csv",
       how="rows of keepers.csv with this keeper", why=f"{LA}, custody: second-largest holder")
def keeper_ucc():
    return int((raw("ogham/keepers.csv")["keeper"] == "University College Cork").sum())


@claim("A-13c", "3.1", "stones held by the National Museums of Scotland", paper=25, source="data/raw/ogham/keepers.csv",
       how="rows of keepers.csv with this keeper", why=f"{LA}, custody: third-largest holder")
def keeper_nms():
    return int((raw("ogham/keepers.csv")["keeper"] == "National Museums of Scotland").sum())


def _keepers():
    k = raw("ogham/keepers.csv")
    k["d"] = floats(k["distance_km"])
    return k


@claim("A-13d", "3.1", "institutions that hold the 182 stones", paper=37, source="data/raw/ogham/keepers.csv",
       how="distinct values of the keeper column", why=f"{LA}, custody: how concentrated the holdings are")
def keepers_n():
    return _keepers()["keeper"].nunique()


@claim("A-13e", "3.1", "institutions that hold a single stone", paper=22, source="data/raw/ogham/keepers.csv",
       how="keepers that occur in exactly one row", why=f"{LA}, custody: a long tail of small holders")
def keepers_single():
    vc = _keepers()["keeper"].value_counts()
    return int((vc == 1).sum())


def _median_of(keeper):
    k = _keepers()
    return round(statistics.median(k[k["keeper"] == keeper]["d"]), 1)


for _cid, _keeper, _paper in (("A-13f", "National Museum of Ireland", "231.2"), ("A-13g", "National Museums of Scotland", "354.7"),
                              ("A-13h", "University College Cork", "31.9"), ("A-13i", "Manx Museum", "17"),
                              ("A-13j", "British Museum", "597.9")):
    @claim(_cid, "3.1", f"median distance findspot to {_keeper} (km)", paper=_paper, source="data/raw/ogham/keepers.csv",
           how=f"median of distance_km over the stones that {_keeper} holds",
           why=f"{LA}, custody: collections differ in the reach of their holdings (figure of the keepers, screenshots of the web map)")
    def _f(_keeper=_keeper):
        return _median_of(_keeper)
    _f.__name__ = "median_" + _keeper.split()[0].lower() + "_" + _cid.lower().replace("-", "")


@claim("A-13k", "3.1", "stones of the Manx Museum found on the Isle of Man", paper=6, source="data/raw/ogham/keepers.csv",
       how="rows with keeper Manx Museum and findspot_country Isle of Man", why=f"{LA}, custody: a local hub")
def manx_local():
    k = _keepers()
    return int(((k["keeper"] == "Manx Museum") & (k["findspot_country"] == "Isle of Man")).sum())


@claim("A-13l", "3.1", "stones of University College Cork found in Ireland", paper=28, source="data/raw/ogham/keepers.csv",
       how="rows with keeper University College Cork and findspot_country Ireland", why=f"{LA}, custody: a local hub")
def ucc_local():
    k = _keepers()
    return int(((k["keeper"] == "University College Cork") & (k["findspot_country"] == "Ireland")).sum())


@claim("A-13m", "3.1", "stones of the British Museum by country of the findspot", paper="Ireland 6; England 2; Wales 1",
       source="data/raw/ogham/keepers.csv", how="findspot_country of the rows with keeper British Museum",
       why=f"{LA}, custody: the British Museum as a distant collection")
def bm_countries():
    k = _keepers()
    vc = k[k["keeper"] == "British Museum"]["findspot_country"].value_counts()
    return "; ".join(f"{c} {n}" for c, n in sorted(vc.items(), key=lambda x: (-x[1], x[0])))


@claim("A-13n", "3.1", "stones of the British Museum that crossed a national border", paper=7,
       source="data/raw/ogham/keepers.csv",
       how="the museum is in London (England): stones of the British Museum whose findspot_country is not England",
       why=f"{LA}, custody: the red arcs of the web map")
def bm_crossed():
    k = _keepers()
    return int(((k["keeper"] == "British Museum") & (k["findspot_country"] != "England")).sum())


@claim("A-13o", "3.1", "keeper matches to Wikidata with the weight 0.70 (made automatically)", paper=27,
       source="dist/03-ancestors/keepers.csv", how="rows of keepers.csv with amt_weight 0.70 (match_status auto)",
       why=f"{LA}, uncertainty: weights of the crosswalk for the match of a keeper to Wikidata")
def keeper_w70():
    k = dist("03-ancestors/keepers.csv")
    return int((k["amt_weight"] == "0.70").sum())


@claim("A-13p", "3.1", "keeper matches to Wikidata with the weight 1.00 (verified)", paper=2,
       source="dist/03-ancestors/keepers.csv", how="rows of keepers.csv with amt_weight 1.00 (match_status verified)",
       why=f"{LA}, uncertainty: see A-13o")
def keeper_w100():
    k = dist("03-ancestors/keepers.csv")
    return int((k["amt_weight"] == "1.00").sum())


@claim("A-14", "3.1", "share of stones with a CISP number (%)", paper="81.3", key="",
       source="data/raw/ogham/places.csv",
       how="stones whose cisp column is not empty, divided by all stones",
       why=f"{Q1} Layer b begins in the home dataset: the corpus already carries identifiers")
def cisp_pct():
    p = _stones()
    return pct((p["cisp"] != "").sum(), len(p))


@claim("A-15", "3.1", "share of stones linked to Logainm (%)", paper="48.0", key="",
       source="dist/03-ancestors/stones.csv",
       how="stones with a Logainm gazetteer link (column gazetteers), divided by all stones",
       why=f"{Q1} the place-name gazetteer of Ireland as a hub of layer b")
def logainm_pct():
    s = dist("03-ancestors/stones.csv")
    return pct(s["gazetteers"].str.contains("Logainm").sum(), len(s))


@claim("A-16", "3.1", "Wikidata items for Ogham stones", paper="1,297", key="03:wikidata_items",
       source="dist/03-ancestors/wikidata_clusters.csv",
       how="all item ids listed in the clusters and the single items (instance of Ogham stone, Q2016147)",
       why=f"{Q1} Wikidata holds more items than there are stones, so counting items would overstate the coverage")
def wd_items():
    c = dist("03-ancestors/wikidata_clusters.csv")
    return int(c["items"].str.split(";").map(len).sum())


@claim("A-17", "3.1", "concept clusters of Wikidata items (joined by P1382)", paper=384, key="03:wikidata_concept_clusters",
       source="dist/03-ancestors/wikidata_clusters.csv",
       how="clusters of kind 'concept cluster': items of different projects (CISP, Macalister, Ogham in 3D, "
           "Research Squirrel) joined by 'partially coincident with' (P1382)",
       why=f"{Q1} the unit of counting for layer b; a stone is reached through its cluster, not through an item")
def wd_clusters():
    c = dist("03-ancestors/wikidata_clusters.csv")
    return int((c["kind"] == "concept cluster").sum())


@claim("A-18", "3.1", "single Wikidata items outside any cluster", paper=53, key="03:wikidata_single_items",
       source="dist/03-ancestors/wikidata_clusters.csv",
       how="clusters of kind 'single item'", why=f"{Q2} mostly British stones; these items are not joined to the corpus")
def wd_single():
    c = dist("03-ancestors/wikidata_clusters.csv")
    return int((c["kind"] == "single item").sum())


@claim("A-19", "3.1", "median number of Wikidata items per joined stone", paper=3, key="06:ogham_stones_wikidata_items_per_entity",
       source="dist/03-ancestors/stones.csv",
       how="median of wikidata_items (count of item ids) over the stones that are joined to a cluster",
       why=f"{Q1} shows how far item counts overstate stone counts (Discussion: layer B reflects modelling choices)")
def wd_items_per_stone():
    s = dist("03-ancestors/stones.csv")
    s = s[s["wikidata_cluster"] != ""]
    return statistics.median(s["wikidata_items"].str.split(";").map(len))


@claim("A-20", "3.1", "stones joined to a Wikidata cluster", paper=311, key="03:stones_joined_to_wikidata",
       source="dist/03-ancestors/stones.csv",
       how="stones whose wikidata_cluster is not empty (joined by the CIIC number or the CISP identifier in the label)",
       why=f"{Q1} the density of layer b towards Wikidata")
def stones_joined():
    s = dist("03-ancestors/stones.csv")
    return int((s["wikidata_cluster"] != "").sum())


@claim("A-21", "3.1", "share of stones joined to Wikidata (%)", paper="61.7", key="",
       source="dist/03-ancestors/stones.csv", how="A-20 divided by A-01", why=f"{Q1} same as A-20 as a share")
def stones_joined_pct():
    return pct(stones_joined(), stones())


@claim("A-22", "3.1", "Wikidata clusters with an external identifier", paper=79, key="03:wikidata_clusters_with_external_id",
       source="dist/03-ancestors/wikidata_clusters.csv",
       how="clusters (concept clusters and single items) with at least one external identifier",
       why=f"{Q1} few of the clusters carry links of their own: layer b is thin beyond Wikidata")
def clusters_ext_id():
    c = dist("03-ancestors/wikidata_clusters.csv")
    return int((c["external_identifiers"] != "").sum())


@claim("A-23", "3.1", "Wikidata clusters with an OpenStreetMap link", paper=58, key="03:wikidata_clusters_openstreetmap",
       source="dist/03-ancestors/wikidata_clusters.csv",
       how="clusters whose external identifiers include an OpenStreetMap node id",
       why=f"{Q3} OSM as a hub for the Ogham case")
def clusters_osm():
    c = dist("03-ancestors/wikidata_clusters.csv")
    return int(c["external_identifiers"].str.contains("OpenStreetMap").sum())


REGIONS = (("A-24a", "Ireland", "306/375"), ("A-24b", "Wales", "1/47"), ("A-24c", "Scotland", "1/56"),
           ("A-24d", "England", "1/17"), ("A-24e", "Isle of Man", "2/9"))


def _region_claim(cid, region, paper):
    @claim(cid, "3.1", f"stones joined to Wikidata / all stones, {region}", paper=paper,
           source="dist/03-ancestors/stones.csv",
           how="stones of the region with a Wikidata cluster / all stones of the region (region from the "
               "edition's place data)",
           why=f"{Q2} the regional gradient: Ireland is joined, the other regions are barely present")
    def _f():
        s = dist("03-ancestors/stones.csv")
        r = s[s["region"] == region]
        return f"{int((r['wikidata_cluster'] != '').sum())}/{len(r)}"
    _f.__name__ = f"joined_{region.replace(' ', '_')}"
    return _f


for _cid, _region, _paper in REGIONS:
    _region_claim(_cid, _region, _paper)


@claim("A-25", "3.1", "stones with neither a gazetteer link nor a Wikidata cluster", paper=142,
       key="03:stones_without_lod_link", source="dist/03-ancestors/stones.csv",
       how="stones with empty gazetteers and empty wikidata_cluster",
       why=f"{Q2} the part of the corpus that layer b does not reach at all")
def stones_without_link():
    s = dist("03-ancestors/stones.csv")
    return int(((s["gazetteers"] == "") & (s["wikidata_cluster"] == "")).sum())
