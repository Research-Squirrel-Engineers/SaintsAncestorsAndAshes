# The statistics figures against the text: where the numbers come from

Figures of step 10 (img/10-statistics/) of the paper. 13 numbers; 12 ok, 1 new.

Every entry says what the paper states, what the script counts, which file it reads, how the number is defined and why it is in the paper. The scripts are in `py/claims/figures.py`; each entry names its function. Research questions: Q1 density of layer b, Q2 unevenness, Q3 hubs, Q4 uncertainty.

### F-01a · section 3.4 · Ogham stones: entities with two or more kinds of hub, from the hub-kinds figure (%)

- **Paper:** 70.2 · **Counted:** 70.2 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/hub-kinds.csv
- **Script:** `py/claims/figures.py::_f`
- **What is counted:** entities of the case in the bars '2 kinds', '3 kinds' and '4 or more' of the figure, divided by all entities of the case; the number of kinds is counted as in step 06 (the wells count Wikidata, their home, as a kind)
- **Why it is in the paper:** Q3 Which hubs carry layer b? figure img/10-statistics/hub-kinds.png shows the distribution behind the text's 'at least two kinds of hub'

### F-01b · section 3.4 · Holy wells: entities with two or more kinds of hub, from the hub-kinds figure (%)

- **Paper:** 99.3 · **Counted:** 99.3 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/hub-kinds.csv
- **Script:** `py/claims/figures.py::_f`
- **What is counted:** entities of the case in the bars '2 kinds', '3 kinds' and '4 or more' of the figure, divided by all entities of the case; the number of kinds is counted as in step 06 (the wells count Wikidata, their home, as a kind)
- **Why it is in the paper:** Q3 Which hubs carry layer b? figure img/10-statistics/hub-kinds.png shows the distribution behind the text's 'at least two kinds of hub'

### F-01c · section 3.4 · CI findspots: entities with two or more kinds of hub, from the hub-kinds figure (%)

- **Paper:** 39.2 · **Counted:** 39.2 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/hub-kinds.csv
- **Script:** `py/claims/figures.py::_f`
- **What is counted:** entities of the case in the bars '2 kinds', '3 kinds' and '4 or more' of the figure, divided by all entities of the case; the number of kinds is counted as in step 06 (the wells count Wikidata, their home, as a kind)
- **Why it is in the paper:** Q3 Which hubs carry layer b? figure img/10-statistics/hub-kinds.png shows the distribution behind the text's 'at least two kinds of hub'

### F-02 · section 3.1 · statements with AMT weight 0.9 in the uncertainty figure

- **Paper:** 20 · **Counted:** 20 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/uncertainty.csv
- **Script:** `py/claims/figures.py::fig_weight`
- **What is counted:** statements with weight 0.90 in panel A of the figure
- **Why it is in the paper:** Q4 How is uncertainty recorded? figure img/10-statistics/uncertainty.png, panel A: the number of uncertain readings

### F-03 · section 3.3 · findspots with a match type in the uncertainty figure

- **Paper:** 74 · **Counted:** 74 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/uncertainty.csv
- **Script:** `py/claims/figures.py::fig_match_total`
- **What is counted:** sum of the four bars of panel B (one match type per row of the CI table)
- **Why it is in the paper:** Q4 How is uncertainty recorded? figure img/10-statistics/uncertainty.png, panel B: the figure covers the 74 findspots of the table, as the text does

### F-04 · section 3.3 · findspots in the uncertainty figure, panel C

- **Paper:** 79 · **Counted:** 79 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/uncertainty.csv
- **Script:** `py/claims/figures.py::fig_cert_total`
- **What is counted:** sum of the bars of panel C (certainty level of every findspot, the source included)
- **Why it is in the paper:** Q4 How is uncertainty recorded? figure img/10-statistics/uncertainty.png, panel C: the figure covers all 79 findspots

### F-05 · section 3.3 · findspots drawn in the distance figure

- **Paper:** (not in the text) · **Counted:** 78 · **Status:** new · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/ci-distance.csv
- **Script:** `py/claims/figures.py::fig_distance_n`
- **What is counted:** findspots of the figure: all 79 less the source itself (the Phlegraean Fields, distance 0), so the level 'medium' has 47 findspots there and 48 in the text
- **Why it is in the paper:** Q4 How is uncertainty recorded? figure img/10-statistics/ci-distance.png: says why the figure and the text differ by one

### F-06a · section 3.1 · Ireland: stones joined to Wikidata / all stones, from the regions figure

- **Paper:** 306/375 · **Counted:** 306/375 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/ogham-regions.csv
- **Script:** `py/claims/figures.py::_f`
- **What is counted:** dark part / full bar of the region in the figure
- **Why it is in the paper:** Q2 How unevenly is layer b spread? figure img/10-statistics/ogham-regions.png draws the regional gradient that the text states in numbers

### F-06b · section 3.1 · Wales: stones joined to Wikidata / all stones, from the regions figure

- **Paper:** 1/47 · **Counted:** 1/47 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/ogham-regions.csv
- **Script:** `py/claims/figures.py::_f`
- **What is counted:** dark part / full bar of the region in the figure
- **Why it is in the paper:** Q2 How unevenly is layer b spread? figure img/10-statistics/ogham-regions.png draws the regional gradient that the text states in numbers

### F-06c · section 3.1 · Scotland: stones joined to Wikidata / all stones, from the regions figure

- **Paper:** 1/56 · **Counted:** 1/56 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/ogham-regions.csv
- **Script:** `py/claims/figures.py::_f`
- **What is counted:** dark part / full bar of the region in the figure
- **Why it is in the paper:** Q2 How unevenly is layer b spread? figure img/10-statistics/ogham-regions.png draws the regional gradient that the text states in numbers

### F-06d · section 3.1 · England: stones joined to Wikidata / all stones, from the regions figure

- **Paper:** 1/17 · **Counted:** 1/17 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/ogham-regions.csv
- **Script:** `py/claims/figures.py::_f`
- **What is counted:** dark part / full bar of the region in the figure
- **Why it is in the paper:** Q2 How unevenly is layer b spread? figure img/10-statistics/ogham-regions.png draws the regional gradient that the text states in numbers

### F-06e · section 3.1 · Isle of Man: stones joined to Wikidata / all stones, from the regions figure

- **Paper:** 2/9 · **Counted:** 2/9 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/ogham-regions.csv
- **Script:** `py/claims/figures.py::_f`
- **What is counted:** dark part / full bar of the region in the figure
- **Why it is in the paper:** Q2 How unevenly is layer b spread? figure img/10-statistics/ogham-regions.png draws the regional gradient that the text states in numbers

### F-07 · section 3.1 · stones held more than 100 km from their findspot, from the distance histogram

- **Paper:** 94 · **Counted:** 94 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/10-statistics/custody-distance.csv
- **Script:** `py/claims/figures.py::fig_custody_over_100`
- **What is counted:** sum of the dark bars (bins from 100 km) of the histogram
- **Why it is in the paper:** Q2 How unevenly is layer b spread? figure img/10-statistics/custody-distance.png: the histogram and the text count the same stones
