# Gaps in the linked data: where the numbers come from

Findings of step 11 (dist/11-gaps/) of the paper. 8 numbers; 5 ok, 3 new.

Every entry says what the paper states, what the script counts, which file it reads, how the number is defined and why it is in the paper. The scripts are in `py/claims/gaps.py`; each entry names its function. Research questions: Q1 density of layer b, Q2 unevenness, Q3 hubs, Q4 uncertainty.

### G-01 · section 3.1 · single Ogham items with a stone of the corpus within 5 km

- **Paper:** 46 · **Counted:** 46 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/11-gaps/metrics.csv
- **Script:** `py/claims/gaps.py::_f`
- **What is counted:** single items (no project, no P1382 link) whose Wikidata coordinate lies within 5 km of at least one stone of the corpus; a coordinate alone is a weak hint, so these are candidates, not links
- **Why it is in the paper:** Q2 How unevenly is layer b spread? how far a coordinate comparison could close the gap between the single items and the corpus

### G-02 · section 3.1 · single Ogham items whose CIIC number in the label is that of a stone nearby

- **Paper:** 5 · **Counted:** 5 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/11-gaps/metrics.csv
- **Script:** `py/claims/gaps.py::_f`
- **What is counted:** single items whose label 'CIIC n' equals the CIIC number of a stone within 5 km
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the control for G-01: where the number agrees, the corpus has already joined item and stone (G-07)

### G-07 · section 3.1 · of those, single items that the corpus already joins to that stone

- **Paper:** (not in the text) · **Counted:** 5 · **Status:** new · no key in numbers.csv
- **Where it comes from:** dist/11-gaps/metrics.csv
- **Script:** `py/claims/gaps.py::_f`
- **What is counted:** G-02 items that are listed in the wikidata_items of the stone (dist/03-ancestors/stones.csv): the join over the CIIC identifier worked, the item is a one-item cluster of a joined stone and not a gap
- **Why it is in the paper:** Q2 How unevenly is layer b spread? shows that the single items with a matching CIIC number are not missing links

### G-08 · section 3.1 · single items with a stone nearby and no joined stone among them

- **Paper:** (not in the text) · **Counted:** 41 · **Status:** new · no key in numbers.csv
- **Where it comes from:** dist/11-gaps/metrics.csv
- **Script:** `py/claims/gaps.py::_f`
- **What is counted:** G-01 items for which none of the stones within 5 km is joined to them: the candidates to check by hand
- **Why it is in the paper:** Q2 How unevenly is layer b spread? the real list of candidates (G-01 less G-07)

### G-03 · section 3.2 · P1343 sources that Wikidata no longer describes

- **Paper:** 66 · **Counted:** 66 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/11-gaps/metrics.csv
- **Script:** `py/claims/gaps.py::_f`
- **What is counted:** sources of the holy wells whose label is still the bare QID (no label, no statement, no redirect)
- **Why it is in the paper:** Q3 Which hubs carry layer b? the community hub of the wells is not kept up: sources of the wells point into the void

### G-04 · section 3.2 · well-source edges that point at such a source

- **Paper:** 159 · **Counted:** 159 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/11-gaps/metrics.csv
- **Script:** `py/claims/gaps.py::_f`
- **What is counted:** edges of the well-source table whose source is one of the sources of G-03
- **Why it is in the paper:** Q3 Which hubs carry layer b? see G-03

### G-05 · section 3.2 · share of the well-source edges that point at such a source (%)

- **Paper:** 4.8 · **Counted:** 4.8 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/11-gaps/metrics.csv
- **Script:** `py/claims/gaps.py::_f`
- **What is counted:** G-04 divided by all well-source edges
- **Why it is in the paper:** Q3 Which hubs carry layer b? see G-03

### G-06 · section 3.2 · wells with at least one such source

- **Paper:** (not in the text) · **Counted:** 95 · **Status:** new · no key in numbers.csv
- **Where it comes from:** dist/11-gaps/metrics.csv
- **Script:** `py/claims/gaps.py::_f`
- **What is counted:** distinct wells in the edges of G-04
- **Why it is in the paper:** Q3 Which hubs carry layer b? see G-03
