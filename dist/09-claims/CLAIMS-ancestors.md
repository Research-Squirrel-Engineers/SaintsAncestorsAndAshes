# Ancestors (Ogham stones): where the numbers come from

Sections 2.1 and 3.1 of the paper. 54 numbers; 54 ok.

Every entry says what the paper states, what the script counts, which file it reads, how the number is defined and why it is in the paper. The scripts are in `py/claims/ancestors.py`; each entry names its function. Research questions: Q1 density of layer b, Q2 unevenness, Q3 hubs, Q4 uncertainty.

### A-01 · section 2.1 · stones in the Ogham corpus

- **Paper:** 504 · **Counted:** 504 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ogham/places.csv
- **Script:** `py/claims/ancestors.py::stones`
- **What is counted:** rows of places.csv: one row per stone of the OG(H)AM EpiDoc edition
- **Why it is in the paper:** the denominator of every Ancestors percentage; says how large the case is

### A-02 · section 3.1 · stones that carry at least one kinship statement

- **Paper:** 107 · **Counted:** 107 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ogham/persons.csv
- **Script:** `py/claims/ancestors.py::stones_with_kinship`
- **What is counted:** distinct stone ids in persons.csv (a stone counts once however many statements it carries)
- **Why it is in the paper:** layer a (the network the data state): shows that only a fifth of the corpus has a kinship formula at all

### A-03 · section 3.1 · share of stones with a kinship statement (%)

- **Paper:** 21.2 · **Counted:** 21.2 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/persons.csv, places.csv
- **Script:** `py/claims/ancestors.py::stones_with_kinship_pct`
- **What is counted:** A-02 divided by A-01
- **Why it is in the paper:** layer a (the network the data state): the same point as A-02 as a share

### A-04 · section 3.1 · kinship statements

- **Paper:** 116 · **Counted:** 116 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ogham/persons.csv
- **Script:** `py/claims/ancestors.py::kinship_statements`
- **What is counted:** rows of persons.csv: one row per reified statement 'person X is son/grandson/... of Y' on a stone
- **Why it is in the paper:** layer a (the network the data state): the number of edges of the kinship network

### A-05a · section 3.1 · statements whose first relation is 'son of'

- **Paper:** 89 · **Counted:** 89 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the first relation of each formula, by the lemma: maqqas = son of, muccoviias = of the kin of, avias = descendant of, celias = client of, koi = here lies; none of these = unstated (rule: py/step_03_ancestors.py::_relation)
- **Why it is in the paper:** layer a (the network the data state): which kinds of relation the stones state; the formula words are the edge types

### A-05b · section 3.1 · statements whose first relation is 'of the kin of'

- **Paper:** 13 · **Counted:** 13 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the first relation of each formula, by the lemma: maqqas = son of, muccoviias = of the kin of, avias = descendant of, celias = client of, koi = here lies; none of these = unstated (rule: py/step_03_ancestors.py::_relation)
- **Why it is in the paper:** layer a (the network the data state): which kinds of relation the stones state; the formula words are the edge types

### A-05c · section 3.1 · statements whose first relation is 'descendant of'

- **Paper:** 9 · **Counted:** 9 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the first relation of each formula, by the lemma: maqqas = son of, muccoviias = of the kin of, avias = descendant of, celias = client of, koi = here lies; none of these = unstated (rule: py/step_03_ancestors.py::_relation)
- **Why it is in the paper:** layer a (the network the data state): which kinds of relation the stones state; the formula words are the edge types

### A-05d · section 3.1 · statements whose first relation is 'client of'

- **Paper:** 3 · **Counted:** 3 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the first relation of each formula, by the lemma: maqqas = son of, muccoviias = of the kin of, avias = descendant of, celias = client of, koi = here lies; none of these = unstated (rule: py/step_03_ancestors.py::_relation)
- **Why it is in the paper:** layer a (the network the data state): which kinds of relation the stones state; the formula words are the edge types

### A-05e · section 3.1 · statements whose first relation is 'here lies'

- **Paper:** 1 · **Counted:** 1 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the first relation of each formula, by the lemma: maqqas = son of, muccoviias = of the kin of, avias = descendant of, celias = client of, koi = here lies; none of these = unstated (rule: py/step_03_ancestors.py::_relation)
- **Why it is in the paper:** layer a (the network the data state): which kinds of relation the stones state; the formula words are the edge types

### A-05f · section 3.1 · statements whose first relation is 'unstated'

- **Paper:** 1 · **Counted:** 1 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the first relation of each formula, by the lemma: maqqas = son of, muccoviias = of the kin of, avias = descendant of, celias = client of, koi = here lies; none of these = unstated (rule: py/step_03_ancestors.py::_relation)
- **Why it is in the paper:** layer a (the network the data state): which kinds of relation the stones state; the formula words are the edge types

### A-26a · section 3.1 · the formula word written in the text for 'son of'

- **Paper:** maqi · **Counted:** maqi · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/words.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the formula word of the relation 'son of' in the edition's word list (MAQI; the text writes it lowercase and in italics, as 'maqi'); the check is that the word occurs in words.csv as a formula and returns it in the form the text should use
- **Why it is in the paper:** layer a (the network the data state): the formula words are the edge types of the kinship network; the text names each one

### A-26b · section 3.1 · the formula word written in the text for 'of the kin of'

- **Paper:** mucoi · **Counted:** mucoi · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/words.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the formula word of the relation 'of the kin of' in the edition's word list (MUCOI; the text writes it lowercase and in italics, as 'mucoi'); the check is that the word occurs in words.csv as a formula and returns it in the form the text should use
- **Why it is in the paper:** layer a (the network the data state): the formula words are the edge types of the kinship network; the text names each one

### A-26c · section 3.1 · the formula word written in the text for 'descendant of'

- **Paper:** avi · **Counted:** avi · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/words.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the formula word of the relation 'descendant of' in the edition's word list (AVI; the text writes it lowercase and in italics, as 'avi'); the check is that the word occurs in words.csv as a formula and returns it in the form the text should use
- **Why it is in the paper:** layer a (the network the data state): the formula words are the edge types of the kinship network; the text names each one

### A-26d · section 3.1 · the formula word written in the text for 'client of'

- **Paper:** celi · **Counted:** celi · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/words.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the formula word of the relation 'client of' in the edition's word list (CELI; the text writes it lowercase and in italics, as 'celi'); the check is that the word occurs in words.csv as a formula and returns it in the form the text should use
- **Why it is in the paper:** layer a (the network the data state): the formula words are the edge types of the kinship network; the text names each one

### A-26e · section 3.1 · the formula word written in the text for 'here lies'

- **Paper:** koi · **Counted:** koi · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/words.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** the formula word of the relation 'here lies' in the edition's word list (KOI; the text writes it lowercase and in italics, as 'koi'); the check is that the word occurs in words.csv as a formula and returns it in the form the text should use
- **Why it is in the paper:** layer a (the network the data state): the formula words are the edge types of the kinship network; the text names each one

### A-06 · section 3.1 · connected components of the kinship network

- **Paper:** 208 · **Counted:** 208 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/persons.csv, edges_kinship.csv
- **Script:** `py/claims/ancestors.py::kin_components`
- **What is counted:** graph with stone nodes and person nodes; a stone is joined to every person it names, and persons are joined by the kinship statements; components counted with networkx
- **Why it is in the paper:** layer a (the network the data state): the headline finding that the kinship network is fragmented

### A-07 · section 3.1 · components that reach beyond a single stone

- **Paper:** 8 · **Counted:** 8 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/persons.csv, edges_kinship.csv
- **Script:** `py/claims/ancestors.py::kin_components_across`
- **What is counted:** components of A-06 that contain more than one stone node
- **Why it is in the paper:** layer a (the network the data state): only these components are a network in the sense of linking stones; all others are one stone

### A-08 · section 3.1 · names or kin groups that recur on more than one stone

- **Paper:** 12 · **Counted:** 12 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/persons.csv
- **Script:** `py/claims/ancestors.py::names_on_several_stones`
- **What is counted:** person and kin-group nodes of persons.csv whose stone list has more than one stone
- **Why it is in the paper:** layer a (the network the data state): these recurring names are the only joints between stones; the paper says 'joined by 12'

### A-09 · section 3.1 · kinship statements with an AMT weight below 1.0

- **Paper:** 20 · **Counted:** 20 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/edges_kinship.csv
- **Script:** `py/claims/ancestors.py::kinship_weight_below_1`
- **What is counted:** statements whose Academic Meta Tool weight (amt_weight) is less than 1.0; the crosswalk (tei--epidoc-crosswalk, py/persons.py) gives 0.90 where the lemma in the edition ends with a question mark and 1.00 otherwise
- **Why it is in the paper:** Q4 How is uncertainty recorded? Ancestors records doubt as an AMT weight on each statement

### A-10 · section 3.1 · stones held by an institution today

- **Paper:** 182 · **Counted:** 182 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::stones_held`
- **What is counted:** rows of keepers.csv: one row per stone with a known keeper
- **Why it is in the paper:** layer a (the network the data state), custody: the second relation of the case (findspot to institution)

### A-11 · section 3.1 · median distance findspot to institution (km)

- **Paper:** 110.4 · **Counted:** 110.4 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::custody_median`
- **What is counted:** median of distance_km: great-circle distance between the findspot and the keeper's coordinates (haversine, as in py/network_utils.py::haversine_km), over the 182 stones
- **Why it is in the paper:** layer a (the network the data state), custody: shows that stones are often far from where they were found

### A-12 · section 3.1 · stones held more than 100 km from their findspot

- **Paper:** 94 · **Counted:** 94 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::custody_over_100`
- **What is counted:** rows of keepers.csv with distance_km above 100
- **Why it is in the paper:** layer a (the network the data state), custody: the same point as A-11, as a count

### A-13a · section 3.1 · stones held by the National Museum of Ireland

- **Paper:** 64 · **Counted:** 64 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::keeper_nmi`
- **What is counted:** rows of keepers.csv with this keeper
- **Why it is in the paper:** layer a (the network the data state), custody: the largest holder; the paper names the three largest

### A-13b · section 3.1 · stones held by University College Cork

- **Paper:** 28 · **Counted:** 28 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::keeper_ucc`
- **What is counted:** rows of keepers.csv with this keeper
- **Why it is in the paper:** layer a (the network the data state), custody: second-largest holder

### A-13c · section 3.1 · stones held by the National Museums of Scotland

- **Paper:** 25 · **Counted:** 25 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::keeper_nms`
- **What is counted:** rows of keepers.csv with this keeper
- **Why it is in the paper:** layer a (the network the data state), custody: third-largest holder

### A-13d · section 3.1 · institutions that hold the 182 stones

- **Paper:** 37 · **Counted:** 37 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::keepers_n`
- **What is counted:** distinct values of the keeper column
- **Why it is in the paper:** layer a (the network the data state), custody: how concentrated the holdings are

### A-13e · section 3.1 · institutions that hold a single stone

- **Paper:** 22 · **Counted:** 22 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::keepers_single`
- **What is counted:** keepers that occur in exactly one row
- **Why it is in the paper:** layer a (the network the data state), custody: a long tail of small holders

### A-13f · section 3.1 · median distance findspot to National Museum of Ireland (km)

- **Paper:** 231.2 · **Counted:** 231.2 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** median of distance_km over the stones that National Museum of Ireland holds
- **Why it is in the paper:** layer a (the network the data state), custody: collections differ in the reach of their holdings (figure of the keepers, screenshots of the web map)

### A-13g · section 3.1 · median distance findspot to National Museums of Scotland (km)

- **Paper:** 354.7 · **Counted:** 354.7 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** median of distance_km over the stones that National Museums of Scotland holds
- **Why it is in the paper:** layer a (the network the data state), custody: collections differ in the reach of their holdings (figure of the keepers, screenshots of the web map)

### A-13h · section 3.1 · median distance findspot to University College Cork (km)

- **Paper:** 31.9 · **Counted:** 31.9 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** median of distance_km over the stones that University College Cork holds
- **Why it is in the paper:** layer a (the network the data state), custody: collections differ in the reach of their holdings (figure of the keepers, screenshots of the web map)

### A-13i · section 3.1 · median distance findspot to Manx Museum (km)

- **Paper:** 17 · **Counted:** 16.9 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** median of distance_km over the stones that Manx Museum holds
- **Why it is in the paper:** layer a (the network the data state), custody: collections differ in the reach of their holdings (figure of the keepers, screenshots of the web map)

### A-13j · section 3.1 · median distance findspot to British Museum (km)

- **Paper:** 597.9 · **Counted:** 597.9 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** median of distance_km over the stones that British Museum holds
- **Why it is in the paper:** layer a (the network the data state), custody: collections differ in the reach of their holdings (figure of the keepers, screenshots of the web map)

### A-13k · section 3.1 · stones of the Manx Museum found on the Isle of Man

- **Paper:** 6 · **Counted:** 6 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::manx_local`
- **What is counted:** rows with keeper Manx Museum and findspot_country Isle of Man
- **Why it is in the paper:** layer a (the network the data state), custody: a local hub

### A-13l · section 3.1 · stones of University College Cork found in Ireland

- **Paper:** 28 · **Counted:** 28 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::ucc_local`
- **What is counted:** rows with keeper University College Cork and findspot_country Ireland
- **Why it is in the paper:** layer a (the network the data state), custody: a local hub

### A-13m · section 3.1 · stones of the British Museum by country of the findspot

- **Paper:** Ireland 6; England 2; Wales 1 · **Counted:** Ireland 6; England 2; Wales 1 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::bm_countries`
- **What is counted:** findspot_country of the rows with keeper British Museum
- **Why it is in the paper:** layer a (the network the data state), custody: the British Museum as a distant collection

### A-13n · section 3.1 · stones of the British Museum that crossed a national border

- **Paper:** 7 · **Counted:** 7 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/keepers.csv
- **Script:** `py/claims/ancestors.py::bm_crossed`
- **What is counted:** the museum is in London (England): stones of the British Museum whose findspot_country is not England
- **Why it is in the paper:** layer a (the network the data state), custody: the red arcs of the web map

### A-13o · section 3.1 · keeper matches to Wikidata with the weight 0.70 (made automatically)

- **Paper:** 27 · **Counted:** 27 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/keepers.csv
- **Script:** `py/claims/ancestors.py::keeper_w70`
- **What is counted:** rows of keepers.csv with amt_weight 0.70 (match_status auto)
- **Why it is in the paper:** layer a (the network the data state), uncertainty: weights of the crosswalk for the match of a keeper to Wikidata

### A-13p · section 3.1 · keeper matches to Wikidata with the weight 1.00 (verified)

- **Paper:** 2 · **Counted:** 2 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/keepers.csv
- **Script:** `py/claims/ancestors.py::keeper_w100`
- **What is counted:** rows of keepers.csv with amt_weight 1.00 (match_status verified)
- **Why it is in the paper:** layer a (the network the data state), uncertainty: see A-13o

### A-14 · section 3.1 · share of stones with a CISP number (%)

- **Paper:** 81.3 · **Counted:** 81.3 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** data/raw/ogham/places.csv
- **Script:** `py/claims/ancestors.py::cisp_pct`
- **What is counted:** stones whose cisp column is not empty, divided by all stones
- **Why it is in the paper:** Q1 How dense is layer b? Layer b begins in the home dataset: the corpus already carries identifiers

### A-15 · section 3.1 · share of stones linked to Logainm (%)

- **Paper:** 48.0 · **Counted:** 48 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::logainm_pct`
- **What is counted:** stones with a Logainm gazetteer link (column gazetteers), divided by all stones
- **Why it is in the paper:** Q1 How dense is layer b? the place-name gazetteer of Ireland as a hub of layer b

### A-16 · section 3.1 · Wikidata items for Ogham stones

- **Paper:** 1,297 · **Counted:** 1297 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/wikidata_clusters.csv
- **Script:** `py/claims/ancestors.py::wd_items`
- **What is counted:** all item ids listed in the clusters and the single items (instance of Ogham stone, Q2016147)
- **Why it is in the paper:** Q1 How dense is layer b? Wikidata holds more items than there are stones, so counting items would overstate the coverage

### A-17 · section 3.1 · concept clusters of Wikidata items (joined by P1382)

- **Paper:** 384 · **Counted:** 384 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/wikidata_clusters.csv
- **Script:** `py/claims/ancestors.py::wd_clusters`
- **What is counted:** clusters of kind 'concept cluster': items of different projects (CISP, Macalister, Ogham in 3D, Research Squirrel) joined by 'partially coincident with' (P1382)
- **Why it is in the paper:** Q1 How dense is layer b? the unit of counting for layer b; a stone is reached through its cluster, not through an item

### A-18 · section 3.1 · single Wikidata items outside any cluster

- **Paper:** 53 · **Counted:** 53 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/wikidata_clusters.csv
- **Script:** `py/claims/ancestors.py::wd_single`
- **What is counted:** clusters of kind 'single item'
- **Why it is in the paper:** Q2 How unevenly is layer b spread? mostly British stones; these items are not joined to the corpus

### A-19 · section 3.1 · median number of Wikidata items per joined stone

- **Paper:** 3 · **Counted:** 3 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::wd_items_per_stone`
- **What is counted:** median of wikidata_items (count of item ids) over the stones that are joined to a cluster
- **Why it is in the paper:** Q1 How dense is layer b? shows how far item counts overstate stone counts (Discussion: layer B reflects modelling choices)

### A-20 · section 3.1 · stones joined to a Wikidata cluster

- **Paper:** 311 · **Counted:** 311 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::stones_joined`
- **What is counted:** stones whose wikidata_cluster is not empty (joined by the CIIC number or the CISP identifier in the label)
- **Why it is in the paper:** Q1 How dense is layer b? the density of layer b towards Wikidata

### A-21 · section 3.1 · share of stones joined to Wikidata (%)

- **Paper:** 61.7 · **Counted:** 61.7 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::stones_joined_pct`
- **What is counted:** A-20 divided by A-01
- **Why it is in the paper:** Q1 How dense is layer b? same as A-20 as a share

### A-22 · section 3.1 · Wikidata clusters with an external identifier

- **Paper:** 79 · **Counted:** 79 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/wikidata_clusters.csv
- **Script:** `py/claims/ancestors.py::clusters_ext_id`
- **What is counted:** clusters (concept clusters and single items) with at least one external identifier
- **Why it is in the paper:** Q1 How dense is layer b? few of the clusters carry links of their own: layer b is thin beyond Wikidata

### A-23 · section 3.1 · Wikidata clusters with an OpenStreetMap link

- **Paper:** 58 · **Counted:** 58 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/wikidata_clusters.csv
- **Script:** `py/claims/ancestors.py::clusters_osm`
- **What is counted:** clusters whose external identifiers include an OpenStreetMap node id
- **Why it is in the paper:** Q3 Which hubs carry layer b? OSM as a hub for the Ogham case

### A-24a · section 3.1 · stones joined to Wikidata / all stones, Ireland

- **Paper:** 306/375 · **Counted:** 306/375 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** stones of the region with a Wikidata cluster / all stones of the region (region from the edition's place data)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the regional gradient: Ireland is joined, the other regions are barely present

### A-24b · section 3.1 · stones joined to Wikidata / all stones, Wales

- **Paper:** 1/47 · **Counted:** 1/47 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** stones of the region with a Wikidata cluster / all stones of the region (region from the edition's place data)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the regional gradient: Ireland is joined, the other regions are barely present

### A-24c · section 3.1 · stones joined to Wikidata / all stones, Scotland

- **Paper:** 1/56 · **Counted:** 1/56 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** stones of the region with a Wikidata cluster / all stones of the region (region from the edition's place data)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the regional gradient: Ireland is joined, the other regions are barely present

### A-24d · section 3.1 · stones joined to Wikidata / all stones, England

- **Paper:** 1/17 · **Counted:** 1/17 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** stones of the region with a Wikidata cluster / all stones of the region (region from the edition's place data)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the regional gradient: Ireland is joined, the other regions are barely present

### A-24e · section 3.1 · stones joined to Wikidata / all stones, Isle of Man

- **Paper:** 2/9 · **Counted:** 2/9 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::_f`
- **What is counted:** stones of the region with a Wikidata cluster / all stones of the region (region from the edition's place data)
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the regional gradient: Ireland is joined, the other regions are barely present

### A-25 · section 3.1 · stones with neither a gazetteer link nor a Wikidata cluster

- **Paper:** 142 · **Counted:** 142 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/03-ancestors/stones.csv
- **Script:** `py/claims/ancestors.py::stones_without_link`
- **What is counted:** stones with empty gazetteers and empty wikidata_cluster
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the part of the corpus that layer b does not reach at all
