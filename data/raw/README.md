# data/raw — inputs, unchanged, read-only

Everything a network, figure or number shows comes from a file in this
directory. Nothing here is written by the build (`python main.py`), and no
step of the build reaches the network. The Wikidata snapshots under
`wikidata/` are the one exception to "copied by hand": they are written by
`python main.py harvest`, from the queries under `queries/`, and their fetch
dates are recorded in `wikidata/harvest.json`.

`.gitattributes` keeps every file here byte for byte as obtained (no
line-ending conversion), so the fingerprints in
`dist/00-inventory/inventory.csv` are the same on Windows and Linux.

| Path | What | Obtained |
|---|---|---|
| `ogham/persons.csv` | 116 relations on 107 Ogham stones from the formula words (MAQI, MUCOI, AVI, KOI, CELI …): from-name, relation lemma and surface form, gloss, to-name, whether the object is a kin group, uncertainty | [LinkedOpenOgham/tei--epidoc-crosswalk](https://github.com/LinkedOpenOgham/tei--epidoc-crosswalk) `out/persons.csv`, commit `4b4157d` (2026-07-31); derived from the OG(H)AM EpiDoc editions ([lguariento/og-h-am](https://github.com/lguariento/og-h-am), CC BY 4.0) |
| `ogham/keepers.csv` | 182 stones held by 37 institutions: findspot and keeper coordinates, keeper QID, distance in km | same repository and commit, `out/keepers.csv` |
| `ogham/places.csv` | 504 stones with CIIC, CISP, Trismegistos and SMR numbers, place names at every level, gazetteer URIs, coordinates and their certainty | same repository and commit, `out/places.csv` |
| `ogham/words.csv` | 673 word tokens of all readings (formula, element, compound), with translation, Wikidata link and McManus reference | same repository and commit, `out/words.csv` |
| `ogham/rdf/persons.crm.ttl` | The kinship statements as CIDOC CRM: 358 persons (214 with a normalised name from the edition's nym reference, 144 named only as read), 33 kin groups, 116 reified relation statements with relation lemma and AMT weight (1.00, or 0.90 where the reading is uncertain), 28 `skos:closeMatch` to the Ogham name index | same repository and commit, `out/persons.crm.ttl`, CC BY 4.0 |
| `ogham/rdf/places.crm.ttl` | Stones, findspots and the place hierarchy (`P89_falls_within`) with WKT; 146 `skos:closeMatch` from places to Logainm (142), the Welsh historic place names (3) and Wikidata (1), each also reified with an AMT weight | same repository and commit, `out/places.crm.ttl`, CC BY 4.0 |
| `ogham/rdf/keepers.crm.ttl` | The 37 institutions holding stones, their location and `skos:closeMatch` to Wikidata (29), reified with weight, match status and confidence | same repository and commit, `out/keepers.crm.ttl`, CC BY 4.0 |
| `ogham/rdf/og_persons_1.ttl` | The Ogham name index of lod.ogham.link: 538 person names (OP4000xx) with provenance | same repository and commit, `ontologies/upstream/og_persons_1.ttl`; from [ogi-ogham/ogham-datav1](https://github.com/ogi-ogham/ogham-datav1) — **CC BY-NC-SA 3.0 IE**, unlike the rest of this directory |
| `holywells/holywells-by-patron.json` | Wikidata query result: holy wells (Q1371047) in Ireland and the United Kingdom with coordinate and namesake (P138): 950 rows, 651 wells, 109 namesakes; gender layer, OSM, SMR, administrative unit, diocese, image | Wikidata Query Service, 2026-09-28 (CC0), snapshot taken over from [florianthiery/hdoku26-visuals](https://github.com/florianthiery/hdoku26-visuals) `data/raw/sparql/`, commit `5b21f35` |
| `holywells/holywells-concept.json` | Wikidata query result: 268 wells carrying the Holy Well Semantic Concept (Q126443332) of the WikiProject HolyWells | same |
| `ci/ci_findspots.csv` | 74 Campanian Ignimbrite findspots: literature, WKT point, certainty level, the matched LOD resource and the kind of match, source, spatial type, method, agent (ORCID) | [Research-Squirrel-Engineers/GeoScience-FAIRification-LOD](https://github.com/Research-Squirrel-Engineers/GeoScience-FAIRification-LOD) `data/raw/ci/cifindspots_part_full.csv`, commit `4696888` (2026-08-14), CC BY 4.0 (Thiery & Schenk 2023, doi:10.5281/zenodo.10361309) |
| `ci/ci_site_annotations.csv` | 3 findspots annotated as archaeological sites, with category, context, note, confidence and Wikidata QID | same repository and commit, `data/curated/ci_site_annotations.csv` |
| `basemap/ne_50m_land.geojson` | Natural Earth 1:50m land polygons, for the CI map | Natural Earth (public domain), copied from GeoScience-FAIRification-LOD `data/raw/basemap/`, commit `4696888` |
| `manual/ci_fuzzysl_only.yaml` | The five CI findspots recorded only in the fuzzy-sl Wikibase (QIDs and a note each). Since the statements snapshot, step 05 derives the list from "part of Campanian Ignimbrite Findspots" and uses this file as a cross-check and fallback | compiled by comparing the fuzzy-sl snapshot with the CSV, 2026-10-20; confirmed by the statements snapshot |
| `manual/holywells_labels.yaml` | English labels the harvest returned as bare QIDs (Q126875543, Ó Dálaigh vol. II), each with where it was read | read from the Wikidata snapshot in hdoku26-visuals, 2026-10-20 |
| `queries/*.rq` | The SPARQL queries `harvest` sends: nine to Wikidata — Ogham stones (identifiers; places; item statements, among them the P1382 links between the concept items), holy wells (identifiers; sources with title; details of the sources without label or title, with redirects; namesakes; identifiers of the namesakes; administrative units) — and three to the fuzzy-sl Wikibase (links out; coordinates with qualifiers; text and item statements), whose endpoint is named in the query's first line | written for this repository |
| `wikidata/*.json` | One result per query, rows sorted | `python main.py harvest` (Wikidata Query Service, CC0; fuzzy-sl Wikibase, CC BY 4.0); fetch date per file in `wikidata/harvest.json` |
| `wikidata/harvest.json` | Per query: fetch date, row count, fingerprint of the query text, endpoint | written by `python main.py harvest` |
