# Claims: where every number of the paper comes from

166 numbers, each counted by a function in `py/claims/`. 161 ok, 5 new.

Read one file per case:

- [`CLAIMS-ancestors.md`](CLAIMS-ancestors.md): Ancestors (Ogham stones) (Sections 2.1 and 3.1)
- [`CLAIMS-saints.md`](CLAIMS-saints.md): Saints (holy wells) (Sections 2.1 and 3.2)
- [`CLAIMS-ashes.md`](CLAIMS-ashes.md): Ashes (Campanian Ignimbrite findspots) (Sections 2.1 and 3.3)
- [`CLAIMS-comparison.md`](CLAIMS-comparison.md): Comparison of the three cases (Section 3.4 and the Discussion)
- [`CLAIMS-paper_text.md`](CLAIMS-paper_text.md): Numbers of the final text (Sections 3.1, 3.2 and 3.5 (institutions, women and men, doubt, threshold))
- [`CLAIMS-gaps.md`](CLAIMS-gaps.md): Gaps in the linked data (Findings of step 11 (dist/11-gaps/))
- [`CLAIMS-figures.md`](CLAIMS-figures.md): The statistics figures against the text (Figures of step 10 (img/10-statistics/))

`claims.csv` holds the same in one table.

## What to look at

Nothing: every number in the text equals the counted value.

## How to read a status

- ok: the counted value equals the value in the text (compared at the precision the text states).
- DIFF: the counted value differs from the text; either the text or the definition is wrong.
- TODO: the text still has a placeholder; the counted value is what to put there.
- new: the number is counted but not (yet) in the text.
- numbers.csv: `dist/paper/numbers.csv` (step 08) is written by the pipeline itself; 'agrees' means that the independent count here gives the same number.
