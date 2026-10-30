# Saints, Ancestors and Ashes: numbers

Every number that the paper *Saints, Ancestors and Ashes: Open Semantic Networks from Holy Wells and Ogham Inscriptions to the Campanian Ignimbrite* states, counted again from the data and traced to its source. This is a small excerpt of the full pipeline, [network--ogham-holywells-ci](https://github.com/Research-Squirrel-Engineers/network--ogham-holywells-ci): it holds the snapshots, the derived tables and the code that counts the claims, but not the networks' GraphML files, the figures or the steps that draw them.

## Run

    pip install -r requirements.txt
    python main.py

Python 3.10 or later. The run reads `dist/` and `data/raw/`, counts 166 numbers (161 equal the value in the text, 5 are counted but not stated in it) and rewrites `dist/09-claims/`. The result is the same on every run.

## What is where

| Path | Content |
|---|---|
| `dist/09-claims/claims.csv` | One row per number: section, statement, value in the text, counted value, status, source file, function, definition, reason |
| `dist/09-claims/CLAIMS-*.md` | The same per case (Ancestors, Saints, Ashes, comparison, gaps, final text), readable |
| `py/claims/` | One function per number; each can be read in a few lines |
| `dist/03-ancestors/`, `04-saints/`, `05-ashes/`, `06-lod-layer/`, `10-statistics/`, `11-gaps/` | The derived tables that the claims read (edge lists, node tables, metrics), copied from the full repository |
| `dist/paper/numbers.csv` | The numbers that the full pipeline writes itself, for the cross-check in `claims.csv` (`numbers_csv`) |
| `data/raw/` | The snapshots the tables are built from (OG(H)AM crosswalk tables, Wikidata and fuzzy-sl query results, CI findspots); `data/raw/README.md` says where each file comes from |
| `paper/captions.txt` | The captions of the 19 figures and the key image as submitted |

## Reading a status

- **ok**: the counted value equals the value in the text, compared at the precision the text states.
- **DIFF**: they differ (none at present).
- **new**: counted, but not in the text, for example the findings on gaps in the linked data (`CLAIMS-gaps.md`).

## Not covered

The weights of the five readings of Gigha 1 (0.27, 0.27, 0.18, 0.18, 0.09) come from the prototype [LinkedOpenOgham/tei--epidoc-amt](https://github.com/LinkedOpenOgham/tei--epidoc-amt) and are not counted here. The figures are in the full repository and in the supplementary files of the paper.

## Licences

Code: MIT (`LICENSE`). Tables and counts: CC BY 4.0, derived from the OG(H)AM EpiDoc corpus (CC BY 4.0), Wikidata (CC0), the Campanian Ignimbrite findspots (Thiery and Schenk 2023, CC BY 4.0) and the fuzzy-sl Wikibase (CC BY 4.0). The Ogham name index in `data/raw/ogham/rdf/og_persons_1.ttl` is CC BY-NC-SA 3.0 IE, unlike the rest.

## Citation

See `CITATION.cff`.
