# Saints (holy wells): where the numbers come from

Sections 2.1 and 3.2 of the paper. 32 numbers; 32 ok.

Every entry says what the paper states, what the script counts, which file it reads, how the number is defined and why it is in the paper. The scripts are in `py/claims/saints.py`; each entry names its function. Research questions: Q1 density of layer b, Q2 unevenness, Q3 hubs, Q4 uncertainty.

### S-01 · section 2.1 · holy wells in Ireland and the UK in the snapshots

- **Paper:** 936 · **Counted:** 936 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/wells.csv
- **Script:** `py/claims/saints.py::wells`
- **What is counted:** distinct Wikidata items of holy wells found in any of the snapshots (data/raw/wikidata/holywells_*.json)
- **Why it is in the paper:** the denominator of every Saints percentage; says how large the case is

### S-02 · section 2.1 · wells with a coordinate and a namesake (P138)

- **Paper:** 651 · **Counted:** 651 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/wells.csv
- **Script:** `py/claims/saints.py::wells_with_namesake`
- **What is counted:** wells with a coordinate and at least one 'named after' (P138) statement: the patron network
- **Why it is in the paper:** layer a (the network the data state): the wells that can be joined to a saint and placed on a map

### S-03 · section 2.1 · namesakes (saints)

- **Paper:** 109 · **Counted:** 109 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::namesakes`
- **What is counted:** distinct values of P138 among the wells of S-02
- **Why it is in the paper:** layer a (the network the data state): the number of saint nodes

### S-04 · section 3.2 · wells named after Mary

- **Paper:** 210 · **Counted:** 210 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::mary`
- **What is counted:** wells of the namesake 'Mary' in the patron network
- **Why it is in the paper:** layer a (the network the data state): shows how unequal the saint distribution is (Q2 in layer a)

### S-05 · section 3.2 · wells named after Brigid of Kildare

- **Paper:** 157 · **Counted:** 157 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::brigid`
- **What is counted:** wells of this namesake
- **Why it is in the paper:** layer a (the network the data state): second-largest saint

### S-06 · section 3.2 · wells named after Saint Patrick

- **Paper:** 25 · **Counted:** 25 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::patrick`
- **What is counted:** wells of this namesake
- **Why it is in the paper:** layer a (the network the data state): third-largest saint

### S-07 · section 3.2 · edges of the per-namesake minimum spanning trees

- **Paper:** 561 · **Counted:** 561 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/edges_namesake_mst.csv
- **Script:** `py/claims/saints.py::mst_edges`
- **What is counted:** for each namesake the wells are joined by a minimum spanning tree over great-circle distances; rows of the edge list
- **Why it is in the paper:** layer a (the network the data state): turns a list of wells into a regional network per saint

### S-08 · section 3.2 · median spread of namesakes with at least three wells (km)

- **Paper:** 62.8 · **Counted:** 62.8 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::spread_median`
- **What is counted:** median of the radius of gyration (spread_km) of the wells of each namesake with at least 3 wells
- **Why it is in the paper:** layer a (the network the data state): how local a saint's cult is; the paper contrasts this with the big three

### S-09a · section 3.2 · spread of Saint Patrick's wells (km)

- **Paper:** 75.1 · **Counted:** 75.1 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::spread_patrick`
- **What is counted:** radius of gyration of the wells of this namesake
- **Why it is in the paper:** layer a (the network the data state): the big three are more widespread than the median saint

### S-09b · section 3.2 · spread of Mary's wells (km)

- **Paper:** 107.8 · **Counted:** 107.8 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::spread_mary`
- **What is counted:** radius of gyration of the wells of this namesake
- **Why it is in the paper:** layer a (the network the data state): see S-09a

### S-09c · section 3.2 · spread of Brigid of Kildare's wells (km)

- **Paper:** 108.8 · **Counted:** 108.8 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::spread_brigid`
- **What is counted:** radius of gyration of the wells of this namesake
- **Why it is in the paper:** layer a (the network the data state): see S-09a

### S-10 · section 3.2 · sources (P1343) that describe the wells

- **Paper:** 183 · **Counted:** 183 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/sources.csv
- **Script:** `py/claims/saints.py::sources`
- **What is counted:** distinct values of 'described by source' (P1343) on the wells
- **Why it is in the paper:** layer a (the network the data state): sources are Wikidata items themselves, so sources, wells and saints form one graph

### S-11 · section 3.2 · well-source statements

- **Paper:** 3,294 · **Counted:** 3294 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/edges_well_source.csv
- **Script:** `py/claims/saints.py::well_source_edges`
- **What is counted:** rows of the well-source edge list
- **Why it is in the paper:** layer a (the network the data state): the number of edges between wells and sources

### S-12 · section 3.2 · wells with at least one source

- **Paper:** 728 · **Counted:** 728 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/edges_well_source.csv
- **Script:** `py/claims/saints.py::wells_with_source`
- **What is counted:** distinct wells in the well-source edge list
- **Why it is in the paper:** layer a (the network the data state): how well documented the wells are

### S-13 · section 3.2 · connected components of the source projection

- **Paper:** 3 · **Counted:** 3 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/edges_well_source.csv
- **Script:** `py/claims/saints.py::source_components`
- **What is counted:** one-mode projection of the well-source graph onto the sources (two sources are joined if they describe a common well); components counted with networkx
- **Why it is in the paper:** layer a (the network the data state): the sources form one large block and two small ones

### S-14a · section 3.2 · wells described by 'Historic Environment Viewer (Ireland)'

- **Paper:** 585 · **Counted:** 585 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/sources.csv
- **Script:** `py/claims/saints.py::src_hev`
- **What is counted:** wells of this source (sources.csv, column wells)
- **Why it is in the paper:** layer a (the network the data state): the source that describes most wells

### S-14b · section 3.2 · wells described by the 6 Inch First Edition Ordnance Survey map of Ireland

- **Paper:** 495 · **Counted:** 495 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/sources.csv
- **Script:** `py/claims/saints.py::src_os1`
- **What is counted:** wells of this source
- **Why it is in the paper:** layer a (the network the data state): second-largest source

### S-14c · section 3.2 · wells described by the 2nd edition Ordnance Survey map of Ireland

- **Paper:** 422 · **Counted:** 422 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/sources.csv
- **Script:** `py/claims/saints.py::src_os2`
- **What is counted:** wells of this source
- **Why it is in the paper:** layer a (the network the data state): third-largest source

### S-15 · section 3.2 · sources that describe a single well

- **Paper:** 98 · **Counted:** 98 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/sources.csv
- **Script:** `py/claims/saints.py::sources_single`
- **What is counted:** sources with wells = 1
- **Why it is in the paper:** layer a (the network the data state): the long tail of sources

### S-16 · section 3.2 · namesakes with 20 or more wells that are in the GND

- **Paper:** 5 of 5 · **Counted:** 5 of 5 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::big_in_gnd`
- **What is counted:** namesakes with at least 20 wells, and how many of them have a GND record (authorities column)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? authority files follow renown: every big saint has one

### S-17a · section 3.2 · namesakes with a single well

- **Paper:** 63 · **Counted:** 63 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::single_namesakes`
- **What is counted:** namesakes with exactly one well (wells = 1)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the denominator of S-17: most saints are local

### S-17 · section 3.2 · namesakes with a single well that are in the GND (%)

- **Paper:** 27.0 · **Counted:** 27 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::single_in_gnd`
- **What is counted:** namesakes with exactly one well that have a GND record, divided by all such namesakes (63)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the contrast to S-16: local saints are rarely in the authority files

### S-18 · section 3.2 · namesakes in none of GND, VIAF and LoC

- **Paper:** 65 · **Counted:** 65 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::no_authority`
- **What is counted:** namesakes with an empty authorities column
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the share of saints that the authority files do not know

### S-19 · section 3.2 · share of namesakes in none of GND, VIAF and LoC (%)

- **Paper:** 59.6 · **Counted:** 59.6 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::no_authority_pct`
- **What is counted:** S-18 divided by S-03
- **Why it is in the paper:** Q2 How unevenly is layer b spread? same as S-18 as a share

### S-20 · section 3.2 · female namesakes

- **Paper:** 40 · **Counted:** 40 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/saints.py::female`
- **What is counted:** namesakes with gender 'female' (Wikidata sex or gender)
- **Why it is in the paper:** layer a (the network the data state): gender balance of the saints

### S-21a · section 3.2 · wells named after women

- **Paper:** 511 · **Counted:** 511 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/edges_well_namesake.csv, saints.csv
- **Script:** `py/claims/saints.py::wells_female`
- **What is counted:** distinct wells with at least one female namesake
- **Why it is in the paper:** layer a (the network the data state): Mary and Brigid dominate

### S-21b · section 3.2 · wells named after men

- **Paper:** 151 · **Counted:** 151 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/edges_well_namesake.csv, saints.csv
- **Script:** `py/claims/saints.py::wells_male`
- **What is counted:** distinct wells with at least one male namesake
- **Why it is in the paper:** layer a (the network the data state): see S-21a

### S-22 · section 3.2 · external records on the wells

- **Paper:** 1,999 · **Counted:** 1999 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/wells.csv
- **Script:** `py/claims/saints.py::well_records`
- **What is counted:** sum over the wells of the number of external records (identifiers in the hubs)
- **Why it is in the paper:** Q1 How dense is layer b? the wells are richly linked: layer b is dense here

### S-23 · section 3.2 · share of wells with an SMR (Ireland) record (%)

- **Paper:** 80.9 · **Counted:** 80.9 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/wells.csv
- **Script:** `py/claims/saints.py::wells_smr`
- **What is counted:** wells whose hubs include 'SMR (Ireland)', divided by all wells
- **Why it is in the paper:** Q3 Which hubs carry layer b? the Irish Sites and Monuments Record is the largest hub for the wells

### S-24 · section 3.2 · share of wells with an OpenStreetMap link (%)

- **Paper:** 69.9 · **Counted:** 69.9 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/wells.csv
- **Script:** `py/claims/saints.py::wells_osm`
- **What is counted:** wells whose hubs include 'OpenStreetMap', divided by all wells
- **Why it is in the paper:** Q3 Which hubs carry layer b? OSM is the second hub for the wells and the only hub shared by all three cases

### S-25 · section 3.2 · wells without any external record

- **Paper:** 37 · **Counted:** 37 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/04-saints/wells.csv
- **Script:** `py/claims/saints.py::wells_no_record`
- **What is counted:** wells with records = 0
- **Why it is in the paper:** Q1 How dense is layer b? only a few wells are not linked at all

### S-26 · section 3.2 · share of wells without any external record (%)

- **Paper:** 4.0 · **Counted:** 4 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/wells.csv
- **Script:** `py/claims/saints.py::wells_no_record_pct`
- **What is counted:** S-25 divided by S-01
- **Why it is in the paper:** Q1 How dense is layer b? same as S-25 as a share
