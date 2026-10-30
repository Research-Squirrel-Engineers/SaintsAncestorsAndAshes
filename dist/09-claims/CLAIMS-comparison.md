# Comparison of the three cases: where the numbers come from

Section 3.4 and the Discussion of the paper. 14 numbers; 13 ok, 1 new.

Every entry says what the paper states, what the script counts, which file it reads, how the number is defined and why it is in the paper. The scripts are in `py/claims/comparison.py`; each entry names its function. Research questions: Q1 density of layer b, Q2 unevenness, Q3 hubs, Q4 uncertainty.

### X-01a · section 3.4 · Ogham stones with: any external record (%)

- **Paper:** 93.8 · **Counted:** 93.8 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'any external record' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py)
- **Why it is in the paper:** Q1 How dense is layer b? nearly every entity has some external record

### X-01b · section 3.4 · Holy wells with: any external record (%)

- **Paper:** (not in the text) · **Counted:** 99.6 · **Status:** new · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'any external record' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py); NOTE: this share counts the Holy Well Semantic Concept as a hub; the text states 96.0 % of the wells with an external identifier record (claim T-16)
- **Why it is in the paper:** Q1 How dense is layer b? see X-01a

### X-01c · section 3.4 · CI findspots with: any external record (%)

- **Paper:** 100.0 · **Counted:** 100 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'any external record' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py)
- **Why it is in the paper:** Q1 How dense is layer b? see X-01a

### X-02 · section 3.4 · Ogham stones with: domain hub (%)

- **Paper:** 83.5 · **Counted:** 83.5 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'domain hub' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py); NOTE: this is the share for all domain hubs together (CISP and Trismegistos); CISP alone is 81.3 % (claim A-14) -- the text names the domain hubs, with CISP above all, for the 83.5 %
- **Why it is in the paper:** Q3 Which hubs carry layer b? the Ogham stones lean on the domain hubs of the community

### X-03 · section 3.4 · Ogham stones with: heritage register (%)

- **Paper:** 64.3 · **Counted:** 64.3 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'heritage register' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py)
- **Why it is in the paper:** Q3 Which hubs carry layer b? SMR (Ireland), the heritage register of the stones

### X-04 · section 3.4 · Holy wells with: heritage register (%)

- **Paper:** 91.8 · **Counted:** 91.8 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'heritage register' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py)
- **Why it is in the paper:** Q3 Which hubs carry layer b? the wells lean on heritage registers

### X-05 · section 3.4 · CI findspots with: heritage register (%)

- **Paper:** 0.0 · **Counted:** 0 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'heritage register' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py)
- **Why it is in the paper:** Q3 Which hubs carry layer b? the CI findspots have no heritage register

### X-06a · section 3.4 · Ogham stones with: two or more kinds of hub (%)

- **Paper:** 70.2 · **Counted:** 70.2 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'two or more kinds of hub' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py)
- **Why it is in the paper:** Q3 Which hubs carry layer b? how many kinds of hub an entity reaches

### X-06b · section 3.4 · Holy wells with: two or more kinds of hub (%)

- **Paper:** 99.3 · **Counted:** 99.3 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'two or more kinds of hub' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py)
- **Why it is in the paper:** Q3 Which hubs carry layer b? see X-06a

### X-06c · section 3.4 · CI findspots with: two or more kinds of hub (%)

- **Paper:** 39.2 · **Counted:** 39.2 · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/06-lod-layer/comparison.csv
- **Script:** `py/claims/comparison.py::_f`
- **What is counted:** entities of the case with at least one record of kind 'two or more kinds of hub' / all entities of the case (step 06 assigns every hub to one kind; py/step_06_lod_layer.py)
- **Why it is in the paper:** Q3 Which hubs carry layer b? see X-06a

### X-07 · section 3.4 · hubs that the three cases reach in total

- **Paper:** 18 · **Counted:** 18 · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/06-lod-layer/hubs.csv
- **Script:** `py/claims/comparison.py::hubs_total`
- **What is counted:** distinct hubs with at least one entity, over the three cases (hubs.csv, rows with entities > 0)
- **Why it is in the paper:** Q3 Which hubs carry layer b? no single hub is enough: the cases reach 18 hubs

### X-08 · section 3.4 · hubs used by all three cases

- **Paper:** OpenStreetMap · **Counted:** OpenStreetMap · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/06-lod-layer/hubs.csv
- **Script:** `py/claims/comparison.py::hubs_all`
- **What is counted:** hubs reached by entities of all three cases
- **Why it is in the paper:** Q3 Which hubs carry layer b? the only hub that connects all three cases; basis of the federated-design argument

### X-09 · section 3.4 · hubs used by exactly two cases

- **Paper:** Logainm; SMR (Ireland); Wikidata · **Counted:** Logainm; SMR (Ireland); Wikidata · **Status:** ok · agrees with dist/paper/numbers.csv
- **Where it comes from:** dist/06-lod-layer/hubs.csv
- **Script:** `py/claims/comparison.py::hubs_two`
- **What is counted:** hubs reached by entities of exactly two cases
- **Why it is in the paper:** Q3 Which hubs carry layer b? Wikidata is the home dataset of the wells and a hub for the other two

### X-10 · section Discussion · percentage points that one CI findspot is worth

- **Paper:** more than one · **Counted:** more than one · **Status:** ok · no key in numbers.csv
- **Where it comes from:** dist/05-ashes/findspots.csv
- **Script:** `py/claims/comparison.py::one_findspot`
- **What is counted:** 100 divided by 79 findspots, rounded to one decimal (the check passes if the result is above 1.0)
- **Why it is in the paper:** Limits: with 79 findspots, small shifts change the percentages visibly
