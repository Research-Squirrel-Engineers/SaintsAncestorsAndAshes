# Ashes (Campanian Ignimbrite findspots): where the numbers come from

Sections 2.1 and 3.3 of the paper. 27 numbers; 27 ok.

Every entry says what the paper states, what the script counts, which file it reads, how the number is defined and why it is in the paper. The scripts are in `py/claims/ashes.py`; each entry names its function. Research questions: Q1 density of layer b, Q2 unevenness, Q3 hubs, Q4 uncertainty.

### C-01 · section 2.1 · findspots in the CI table

- **Paper:** 74 · **Counted:** 74 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ci/ci_findspots.csv
- **Script:** `py/claims/ashes.py::findspots_csv`
- **What is counted:** rows of ci_findspots.csv
- **Why it is in the paper:** the home dataset of the case (Thiery and Schenk 2023a)

### C-02 · section 2.1 · findspots that exist only in the fuzzy-sl Wikibase

- **Paper:** 5 · **Counted:** 5 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv
- **Script:** `py/claims/ashes.py::findspots_fuzzysl`
- **What is counted:** findspots with origin 'fuzzy-sl' (chosen by the statement 'part of Campanian Ignimbrite Findspots'; list in data/raw/manual/ci_fuzzysl_only.yaml)
- **Why it is in the paper:** the case includes both datasets ('gerne beide'); the paper states the extension

### C-03 · section 2.1 · findspots in total

- **Paper:** 79 · **Counted:** 79 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv
- **Script:** `py/claims/ashes.py::findspots`
- **What is counted:** rows of findspots.csv (C-01 plus C-02)
- **Why it is in the paper:** the denominator of every Ashes percentage; also the reason a single findspot moves a percentage by more than one point

### C-04 · section 3.3 · publications that report the findspots

- **Paper:** 34 · **Counted:** 34 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/publications.csv
- **Script:** `py/claims/ashes.py::publications`
- **What is counted:** distinct publications after normalising the literature column (37 spellings of 32 publications in the table, plus those of the fuzzy-sl findspots)
- **Why it is in the paper:** layer a (the network the data state): the second node type of the findspot-publication network

### C-05 · section 3.3 · citations (findspot-publication edges)

- **Paper:** 106 · **Counted:** 106 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_publication.csv
- **Script:** `py/claims/ashes.py::citations`
- **What is counted:** rows of the edge list
- **Why it is in the paper:** layer a (the network the data state): the number of edges of the two-mode network

### C-06 · section 3.3 · findspots that rest on a single publication

- **Paper:** 57 · **Counted:** 57 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_publication.csv
- **Script:** `py/claims/ashes.py::findspots_one_pub`
- **What is counted:** findspots with exactly one edge in the findspot-publication list
- **Why it is in the paper:** layer a (the network the data state): most findspots depend on one source, so the network is sparse

### C-07 · section 3.3 · components of the publication projection

- **Paper:** 11 · **Counted:** 11 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/publications.csv, edges_publication_projection.csv
- **Script:** `py/claims/ashes.py::pub_components`
- **What is counted:** one-mode projection onto the publications (joined when they report a common findspot); components counted with networkx, isolated publications included
- **Why it is in the paper:** layer a (the network the data state): the literature falls into few clusters

### C-08 · section 3.3 · publications in the largest component

- **Paper:** 23 · **Counted:** 23 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/edges_publication_projection.csv
- **Script:** `py/claims/ashes.py::pub_largest`
- **What is counted:** size of the largest component of C-07
- **Why it is in the paper:** layer a (the network the data state): one core of the literature

### C-09 · section 3.3 · publications that share no findspot

- **Paper:** 9 · **Counted:** 9 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/edges_publication_projection.csv
- **Script:** `py/claims/ashes.py::pub_isolates`
- **What is counted:** isolated nodes of the projection
- **Why it is in the paper:** layer a (the network the data state): publications that stand alone

### C-10 · section 3.3 · median distance of a findspot to the Phlegraean Fields (km)

- **Paper:** 123.9 · **Counted:** 123.9 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv
- **Script:** `py/claims/ashes.py::distance_median`
- **What is counted:** median of distance_km (great-circle, to the findspot 'Phlegraean Fields'), the source itself excluded
- **Why it is in the paper:** layer a (the network the data state): how far the tephra travelled, in the record

### C-11 · section 3.3 · distance of the most distant findspot (km)

- **Paper:** 2,752.5 · **Counted:** 2752.5 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv
- **Script:** `py/claims/ashes.py::distance_max`
- **What is counted:** maximum of distance_km
- **Why it is in the paper:** layer a (the network the data state): the reach of the record

### C-12a · section 3.3 · findspots with medium location certainty

- **Paper:** 48 · **Counted:** 48 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv
- **Script:** `py/claims/ashes.py::certainty_medium`
- **What is counted:** findspots with certainty 'medium' (CSV certainty or fuzzy-sl level)
- **Why it is in the paper:** Q4 How is uncertainty recorded? the CI case records uncertainty as a certainty level per coordinate

### C-12b · section 3.3 · findspots with high location certainty

- **Paper:** 14 · **Counted:** 14 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv
- **Script:** `py/claims/ashes.py::certainty_high`
- **What is counted:** findspots with certainty 'high'
- **Why it is in the paper:** Q4 How is uncertainty recorded? see C-12a

### C-13 · section 3.3 · external links of layer b

- **Paper:** 108 · **Counted:** 108 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_hub.csv
- **Script:** `py/claims/ashes.py::links`
- **What is counted:** rows of the findspot-hub list that point to an external hub (Wikidata, OpenStreetMap, GeoNames, Wikipedia); the 19 links to fuzzy-sl items are not counted
- **Why it is in the paper:** Q1 How dense is layer b? the size of layer b in the CI case

### C-14 · section 3.3 · external links per findspot (mean)

- **Paper:** 1.37 · **Counted:** 1.37 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_hub.csv
- **Script:** `py/claims/ashes.py::links_per_findspot`
- **What is counted:** C-13 divided by C-03
- **Why it is in the paper:** Q1 How dense is layer b? density of layer b

### C-15a · section 3.3 · findspots linked to Wikidata (%)

- **Paper:** 60.8 · **Counted:** 60.8 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_hub.csv
- **Script:** `py/claims/ashes.py::pct_wikidata`
- **What is counted:** distinct findspots with a Wikidata link / all findspots
- **Why it is in the paper:** Q3 Which hubs carry layer b? Wikidata is the main hub of the CI case

### C-15b · section 3.3 · findspots linked to OpenStreetMap (%)

- **Paper:** 45.6 · **Counted:** 45.6 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_hub.csv
- **Script:** `py/claims/ashes.py::pct_osm`
- **What is counted:** distinct findspots with an OSM link / all findspots
- **Why it is in the paper:** Q3 Which hubs carry layer b? OSM, the hub shared by all cases

### C-15c · section 3.3 · findspots linked to GeoNames (%)

- **Paper:** 29.1 · **Counted:** 29.1 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_hub.csv
- **Script:** `py/claims/ashes.py::pct_geonames`
- **What is counted:** distinct findspots with a GeoNames link / all findspots
- **Why it is in the paper:** Q3 Which hubs carry layer b? the gazetteer of the CI case

### C-16 · section 3.3 · findspots typed as archaeological sites

- **Paper:** 13 · **Counted:** 13 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv
- **Script:** `py/claims/ashes.py::arch_sites`
- **What is counted:** findspots whose spatial type includes fsl:ArchaeologicalSite (the 9 of the table plus those of fuzzy-sl)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? coverage depends on the kind of site

### C-17 · section 3.3 · archaeological sites linked to Wikidata

- **Paper:** 12 · **Counted:** 12 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv, edges_findspot_hub.csv
- **Script:** `py/claims/ashes.py::arch_wikidata`
- **What is counted:** archaeological sites (C-16) with a Wikidata link
- **Why it is in the paper:** Q2 How unevenly is layer b spread? archaeological sites are almost all in Wikidata

### C-18 · section 3.3 · share of archaeological sites linked to Wikidata (%)

- **Paper:** 92.3 · **Counted:** 92.3 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** see C-17
- **Script:** `py/claims/ashes.py::arch_wikidata_pct`
- **What is counted:** C-17 divided by C-16
- **Why it is in the paper:** Q2 How unevenly is layer b spread? same as C-17 as a share

### C-19 · section 3.3 · findspots of the table with a close match

- **Paper:** 51 · **Counted:** 51 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ci/ci_findspots.csv
- **Script:** `py/claims/ashes.py::close_match`
- **What is counted:** rows with relatedtohow = skos:closeMatch
- **Why it is in the paper:** Q4 How is uncertainty recorded? the CI case records uncertainty as a match type per link

### C-20 · section 3.3 · findspots of the table with a weaker or doubtful match

- **Paper:** 23 · **Counted:** 23 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ci/ci_findspots.csv
- **Script:** `py/claims/ashes.py::weak_match`
- **What is counted:** rows with relatedtohow other than skos:closeMatch (fsl:spatialCloseMatch, fsl:partlyMatch, fsl:dubiousMatch)
- **Why it is in the paper:** Q4 How is uncertainty recorded? see C-19

### C-21 · section 3.3 · share of table findspots with a weaker or doubtful match (%)

- **Paper:** 31.1 · **Counted:** 31.1 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ci/ci_findspots.csv
- **Script:** `py/claims/ashes.py::weak_match_pct`
- **What is counted:** C-20 divided by C-01
- **Why it is in the paper:** Q4 How is uncertainty recorded? see C-19

### C-22 · section 3.3 · fuzzy-sl items that are members of the CI findspot collection

- **Paper:** 19 · **Counted:** 19 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_hub.csv
- **Script:** `py/claims/ashes.py::fuzzysl_members`
- **What is counted:** findspots with a link to a fuzzy-sl item (hub 'fuzzy-sl')
- **Why it is in the paper:** Q3 Which hubs carry layer b? the fuzzy-sl Wikibase as a domain hub of the case

### C-23 · section 3.3 · external links that fuzzy-sl adds to those of the table

- **Paper:** 1 · **Counted:** 1 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/fuzzysl_matches.csv
- **Script:** `py/claims/ashes.py::fuzzysl_new`
- **What is counted:** external resources recorded on a matched fuzzy-sl item and not in the CSV (column resources_only_in_fuzzysl, counted per resource)
- **Why it is in the paper:** Q1 How dense is layer b? the fuzzy-sl Wikibase adds almost nothing to layer b

### C-24 · section 3.3 · external resources linked from findspots more than 100 km apart

- **Paper:** 1 · **Counted:** 1 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/05-ashes/suspicious_links.csv
- **Script:** `py/claims/ashes.py::suspicious`
- **What is counted:** OSM/Wikidata/GeoNames resources shared by two findspots whose coordinates are more than 100 km apart (Phlegraean Fields and Crvena Stijena: 420.1 km)
- **Why it is in the paper:** layer b exposed an error in layer a (Discussion: 'Layer B is a probe of layer A')
