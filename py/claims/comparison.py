# -*- coding: utf-8 -*-
"""
claims.comparison -- the numbers of 3.4 and of the Discussion
==============================================================

Reads dist/06-lod-layer/comparison.csv and hubs.csv (step 06). Both tables
count entities per case: the 504 stones, the 936 wells, the 79 findspots.
"""

from __future__ import annotations

from .core import claim, dist, floats, pct

Q1 = "Q1 How dense is layer b?"
Q2 = "Q2 How unevenly is layer b spread?"
Q3 = "Q3 Which hubs carry layer b?"
Q4 = "Q4 How is uncertainty recorded?"

CASES = {"stones": "Ogham stones", "wells": "Holy wells", "findspots": "CI findspots"}


def _share(case, measure):
    c = dist("06-lod-layer/comparison.csv")
    r = c[(c["case"] == CASES[case]) & (c["measure"] == measure)].iloc[0]
    return pct(float(r["entities"]), float(r["of"]))


def _make(cid, case, measure, paper, why, how_extra=""):
    @claim(cid, "3.4", f"{CASES[case]} with: {measure} (%)", paper=paper, source="dist/06-lod-layer/comparison.csv",
           how=f"entities of the case with at least one record of kind '{measure}' / all entities of the case "
               f"(step 06 assigns every hub to one kind; py/step_06_lod_layer.py){how_extra}",
           why=why)
    def _f():
        return _share(case, measure)
    _f.__name__ = f"{case}_{measure.replace(' ', '_')}"
    return _f


_make("X-01a", "stones", "any external record", "93.8", f"{Q1} nearly every entity has some external record")
_make("X-01b", "wells", "any external record", None, f"{Q1} see X-01a",
      "; NOTE: this share counts the Holy Well Semantic Concept as a hub; the text states 96.0 % of the wells with an "
      "external identifier record (claim T-16)")
_make("X-01c", "findspots", "any external record", "100.0", f"{Q1} see X-01a")
_make("X-02", "stones", "domain hub", "83.5",
      f"{Q3} the Ogham stones lean on the domain hubs of the community",
      "; NOTE: this is the share for all domain hubs together (CISP and Trismegistos); CISP alone is 81.3 % "
      "(claim A-14) -- the text names the domain hubs, with CISP above all, for the 83.5 %")
_make("X-03", "stones", "heritage register", "64.3", f"{Q3} SMR (Ireland), the heritage register of the stones")
_make("X-04", "wells", "heritage register", "91.8", f"{Q3} the wells lean on heritage registers")
_make("X-05", "findspots", "heritage register", "0.0", f"{Q3} the CI findspots have no heritage register")
_make("X-06a", "stones", "two or more kinds of hub", "70.2", f"{Q3} how many kinds of hub an entity reaches")
_make("X-06b", "wells", "two or more kinds of hub", "99.3", f"{Q3} see X-06a")
_make("X-06c", "findspots", "two or more kinds of hub", "39.2", f"{Q3} see X-06a")


def _hubs_by_cases():
    h = dist("06-lod-layer/hubs.csv")
    h = h[floats(h["entities"]) > 0]
    return h.groupby("hub")["case"].nunique()


@claim("X-07", "3.4", "hubs that the three cases reach in total", paper=18, key="06:hubs_total",
       source="dist/06-lod-layer/hubs.csv",
       how="distinct hubs with at least one entity, over the three cases (hubs.csv, rows with entities > 0)",
       why=f"{Q3} no single hub is enough: the cases reach 18 hubs")
def hubs_total():
    return len(_hubs_by_cases())


@claim("X-08", "3.4", "hubs used by all three cases", paper="OpenStreetMap", key="06:hubs_shared_by_all",
       source="dist/06-lod-layer/hubs.csv", how="hubs reached by entities of all three cases",
       why=f"{Q3} the only hub that connects all three cases; basis of the federated-design argument")
def hubs_all():
    s = _hubs_by_cases()
    return "; ".join(sorted(s[s == 3].index))


@claim("X-09", "3.4", "hubs used by exactly two cases", paper="Logainm; SMR (Ireland); Wikidata",
       key="06:hubs_shared_by_two", source="dist/06-lod-layer/hubs.csv",
       how="hubs reached by entities of exactly two cases",
       why=f"{Q3} Wikidata is the home dataset of the wells and a hub for the other two")
def hubs_two():
    s = _hubs_by_cases()
    return "; ".join(sorted(s[s == 2].index))


@claim("X-10", "Discussion", "percentage points that one CI findspot is worth", paper="more than one",
       source="dist/05-ashes/findspots.csv", how="100 divided by 79 findspots, rounded to one decimal "
       "(the check passes if the result is above 1.0)",
       why="Limits: with 79 findspots, small shifts change the percentages visibly")
def one_findspot():
    return "more than one" if 100 / 79 > 1.0 else "not more than one"
