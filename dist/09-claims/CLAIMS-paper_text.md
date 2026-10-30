# Numbers of the final text: where the numbers come from

Sections 3.1, 3.2 and 3.5 (institutions, women and men, doubt, threshold) of the paper. 18 numbers; 18 ok.

Every entry says what the paper states, what the script counts, which file it reads, how the number is defined and why it is in the paper. The scripts are in `py/claims/paper_text.py`; each entry names its function. Research questions: Q1 density of layer b, Q2 unevenness, Q3 hubs, Q4 uncertainty.

### T-01 · section 3.1 · stones held by the three largest institutions

- **Paper:** 117 · **Counted:** 117 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/paper_text.py::top_three`
- **What is counted:** the three largest values of the keeper counts (National Museum of Ireland 64, University College Cork 28, National Museums of Scotland 25) added up
- **Why it is in the paper:** layer a (the network the data state), custody: a few national holders keep most of the stones

### T-02 · section 3.1 · share of the held stones that the three largest institutions keep (%)

- **Paper:** 64.3 · **Counted:** 64.3 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/paper_text.py::top_three_pct`
- **What is counted:** T-01 divided by all stones with a known keeper (A-10)
- **Why it is in the paper:** layer a (the network the data state), custody: see T-01

### T-03 · section 3.2 · female namesakes with at least three wells

- **Paper:** 15 · **Counted:** 15 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/paper_text.py::women_n`
- **What is counted:** namesakes with gender 'female' and at least 3 wells
- **Why it is in the paper:** layer a (the network the data state): the group behind the women/men contrast

### T-04 · section 3.2 · male namesakes with at least three wells

- **Paper:** 15 · **Counted:** 15 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/paper_text.py::men_n`
- **What is counted:** namesakes with gender 'male' and at least 3 wells
- **Why it is in the paper:** layer a (the network the data state): see T-03

### T-05 · section 3.2 · median spread of female namesakes with at least three wells (km)

- **Paper:** 87.7 · **Counted:** 87.7 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/paper_text.py::women_spread`
- **What is counted:** median of the radius of gyration (spread_km) over the namesakes of T-03
- **Why it is in the paper:** layer a (the network the data state): in these data the networks of female saints are wider (Mary and Brigid are among them)

### T-06 · section 3.2 · median spread of male namesakes with at least three wells (km)

- **Paper:** 34.3 · **Counted:** 34.3 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/saints.csv
- **Script:** `py/claims/paper_text.py::men_spread`
- **What is counted:** median of the radius of gyration over the namesakes of T-04
- **Why it is in the paper:** layer a (the network the data state): see T-05

### T-07 · section 3.5 · kinship statements with the AMT weight 1.00

- **Paper:** 96 · **Counted:** 96 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/uncertainty.csv
- **Script:** `py/claims/paper_text.py::w100`
- **What is counted:** statements with amt_weight 1.00 (116 less the 20 of A-09)
- **Why it is in the paper:** Q4 How is uncertainty recorded? Ancestors: the two weights

### T-08 · section 3.5 · findspots with a spatially close match

- **Paper:** 14 · **Counted:** 14 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/uncertainty.csv
- **Script:** `py/claims/paper_text.py::m_spatial`
- **What is counted:** rows of the CI table with relatedtohow fsl:spatialCloseMatch
- **Why it is in the paper:** Q4 How is uncertainty recorded? Ashes: match type

### T-09 · section 3.5 · findspots with a partial match

- **Paper:** 5 · **Counted:** 5 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/uncertainty.csv
- **Script:** `py/claims/paper_text.py::m_partial`
- **What is counted:** rows of the CI table with relatedtohow fsl:partlyMatch
- **Why it is in the paper:** Q4 How is uncertainty recorded? Ashes: match type

### T-10 · section 3.5 · findspots with a dubious match

- **Paper:** 4 · **Counted:** 4 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/uncertainty.csv
- **Script:** `py/claims/paper_text.py::m_dubious`
- **What is counted:** rows of the CI table with relatedtohow fsl:dubiousMatch
- **Why it is in the paper:** Q4 How is uncertainty recorded? Ashes: match type

### T-11 · section 3.5 · findspots whose coordinate has a lower certainty level or none

- **Paper:** 17 · **Counted:** 17 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/uncertainty.csv
- **Script:** `py/claims/paper_text.py::cert_rest`
- **What is counted:** all findspots less those with the level high (14) and medium (48): low, representative, dubious, not stated
- **Why it is in the paper:** Q4 How is uncertainty recorded? Ashes: certainty of the coordinate; the text says 'lower or not stated for the remaining 17'

### T-12 · section 3.5 · groups of stones that the kinship statements join (all statements)

- **Paper:** 7 · **Counted:** 7 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/paper_text.py::groups_all`
- **What is counted:** graph of the statements (person to person) with each stone joined to the persons it names; components that contain more than one stone
- **Why it is in the paper:** Q4 How is uncertainty recorded? threshold example: the weights change the network

### T-13 · section 3.5 · stones in those groups (all statements)

- **Paper:** 17 · **Counted:** 17 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/paper_text.py::stones_all`
- **What is counted:** stone nodes in the components of T-12
- **Why it is in the paper:** Q4 How is uncertainty recorded? see T-12

### T-14 · section 3.5 · groups of stones when only statements with weight 1.00 count

- **Paper:** 4 · **Counted:** 4 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/paper_text.py::groups_100`
- **What is counted:** as T-12 on the statements with amt_weight 1.00
- **Why it is in the paper:** Q4 How is uncertainty recorded? see T-12

### T-15 · section 3.5 · stones in those groups (weight 1.00 only)

- **Paper:** 10 · **Counted:** 10 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/paper_text.py::stones_100`
- **What is counted:** stone nodes in the components of T-14
- **Why it is in the paper:** Q4 How is uncertainty recorded? see T-12

### T-16 · section 3.4 · share of wells with at least one external identifier record (%)

- **Paper:** 96.0 · **Counted:** 96 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/wells.csv
- **Script:** `py/claims/paper_text.py::wells_with_record`
- **What is counted:** wells with records above 0 (the identifiers on the well item), divided by all wells (S-01); the same wells as 'only 37 wells have no external record' (S-25, S-26) in 3.2
- **Why it is in the paper:** Q2 How unevenly is layer b spread? nearly every well has an external record; the number agrees with 3.2

### T-17 · section 3.2 · wells with both a female and a male namesake

- **Paper:** 11 · **Counted:** 11 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/04-saints/edges_well_namesake.csv, saints.csv
- **Script:** `py/claims/paper_text.py::wells_both`
- **What is counted:** wells that have at least one female and at least one male namesake (511 + 151 - 11 = 651 wells)
- **Why it is in the paper:** layer a (the network the data state): the counts of wells named after women and after men overlap by these wells

### T-18 · section 3.4 · share of CI findspots with a link to a hub other than fuzzy-sl (%)

- **Paper:** 100.0 · **Counted:** 100 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/05-ashes/edges_findspot_hub.csv, findspots.csv
- **Script:** `py/claims/paper_text.py::ci_external_share`
- **What is counted:** findspots with at least one link to Wikidata, OpenStreetMap, GeoNames or Wikipedia, divided by all findspots; the five findspots that exist only in fuzzy-sl are counted only if they have such a link
- **Why it is in the paper:** Q1 How dense is layer b? the 100 % of 3.4 does not rest on fuzzy-sl being the home dataset of five findspots
