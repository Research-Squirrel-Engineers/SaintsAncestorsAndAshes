#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step_09_claims.py -- where every number of the paper comes from (step 09, PRIMER S9)
=====================================================================================

For each number that the paper states there is a claim in py/claims/*.py: a
short function that counts the number from a table, with a plain-words
definition (``how``), the files it reads (``source``) and the reason it is in
the paper (``why``). This step runs all claims, compares each result with the
value the paper states, and writes the result so that one can read it.

Inputs
    data/raw/**, dist/03-*..06-*, dist/paper/numbers.csv (step 08, for the cross-check)

Outputs
    dist/09-claims/
        README.md           status overview and the list of what to look at
        claims.csv          one row per claim (machine-readable)
        CLAIMS-<case>.md    per case: every number with source, definition, reason

Statuses: OK (equal to the paper), DIFF (differs), TODO (the paper still has a
placeholder), NEW (not in the paper). ``numbers_csv`` says whether the number
agrees with the one step 08 wrote to dist/paper/numbers.csv.

Run on its own:  python py/step_09_claims.py     or    python main.py --only 09
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import network_utils as nu  # noqa: E402

PAPER_SECTIONS = {
    "ancestors": ("Ancestors (Ogham stones)", "Sections 2.1 and 3.1"),
    "saints": ("Saints (holy wells)", "Sections 2.1 and 3.2"),
    "ashes": ("Ashes (Campanian Ignimbrite findspots)", "Sections 2.1 and 3.3"),
    "comparison": ("Comparison of the three cases", "Section 3.4 and the Discussion"),
    "paper_text": ("Numbers of the final text", "Sections 3.1, 3.2 and 3.5 (institutions, women and men, doubt, threshold)"),
    "gaps": ("Gaps in the linked data", "Findings of step 11 (dist/11-gaps/)"),
    "figures": ("The statistics figures against the text", "Figures of step 10 (img/10-statistics/)"),
}
ICON = {"OK": "ok", "DIFF": "DIFF", "TODO": "TODO", "NEW": "new"}


def _load():
    from claims import ancestors, ashes, comparison, core, figures, gaps, paper_text, saints  # noqa: F401  (importing registers the claims)

    return core.run_all()


def _block(c) -> list[str]:
    lines = [f"### {c.cid} · section {c.section} · {c.statement}", ""]
    paper = c.paper if c.paper is not None else "(not in the text)"
    cross = {"agree": "agrees with dist/paper/numbers.csv", "differ": "DIFFERS from dist/paper/numbers.csv",
             "": "no key in numbers.csv"}[c.numbers_csv]
    lines += [f"- **Paper:** {paper} · **Counted:** {c.value} · **Status:** {ICON[c.status]} · {cross}",
              f"- **Where it comes from:** {c.source or '–'}",
              f"- **Script:** `{c.script}`",
              f"- **What is counted:** {c.how or '–'}",
              f"- **Why it is in the paper:** {c.why or '–'}", ""]
    return lines


def main() -> list[str]:
    claims = _load()
    out = nu.dist_dir("09")
    nu.ensure_dirs(out)
    written = [nu.write_csv(
        out / "claims.csv",
        ["id", "section", "statement", "paper", "counted", "status", "numbers_csv", "source", "script", "how", "why"],
        [(c.cid, c.section, c.statement, c.paper or "", c.value, c.status, c.numbers_csv, c.source, c.script,
          c.how, c.why) for c in claims])]

    by_module: dict[str, list] = {}
    for c in claims:
        by_module.setdefault(c.script.split("/")[-1].split(".py")[0], []).append(c)
    for module, (title, where) in PAPER_SECTIONS.items():
        cl = by_module.get(module, [])
        n = Counter(c.status for c in cl)
        lines = [f"# {title}: where the numbers come from", "",
                 f"{where} of the paper. {len(cl)} numbers; "
                 + ", ".join(f"{n[s]} {ICON[s]}" for s in ("OK", "DIFF", "TODO", "NEW") if n[s]) + ".", "",
                 "Every entry says what the paper states, what the script counts, which file it reads, "
                 "how the number is defined and why it is in the paper. The scripts are in "
                 f"`py/claims/{module}.py`; each entry names its function. Research questions: "
                 "Q1 density of layer b, Q2 unevenness, Q3 hubs, Q4 uncertainty.", ""]
        for c in cl:
            lines += _block(c)
        written.append(nu.write_text(out / f"CLAIMS-{module}.md", "\n".join(lines).rstrip() + "\n"))

    total = Counter(c.status for c in claims)
    cross_bad = [c for c in claims if c.numbers_csv == "differ"]
    look = [c for c in claims if c.status in ("DIFF", "TODO") or c.numbers_csv == "differ"]
    lines = ["# Claims: where every number of the paper comes from", "",
             f"{len(claims)} numbers, each counted by a function in `py/claims/`. "
             + ", ".join(f"{total[s]} {ICON[s]}" for s in ("OK", "DIFF", "TODO", "NEW") if total[s]) + ".",
             "", "Read one file per case:", ""]
    lines += [f"- [`CLAIMS-{m}.md`](CLAIMS-{m}.md): {t} ({w})" for m, (t, w) in PAPER_SECTIONS.items()]
    lines += ["", "`claims.csv` holds the same in one table.", "", "## What to look at", ""]
    if look:
        lines += ["| id | section | statement | paper | counted | status |", "|---|---|---|---|---|---|"]
        lines += [f"| {c.cid} | {c.section} | {c.statement} | {c.paper} | {c.value} | {ICON[c.status]}"
                  f"{' (numbers.csv differs)' if c.numbers_csv == 'differ' else ''} |" for c in look]
    else:
        lines.append("Nothing: every number in the text equals the counted value.")
    lines += ["", "## How to read a status", "",
              "- ok: the counted value equals the value in the text (compared at the precision the text states).",
              "- DIFF: the counted value differs from the text; either the text or the definition is wrong.",
              "- TODO: the text still has a placeholder; the counted value is what to put there.",
              "- new: the number is counted but not (yet) in the text.",
              "- numbers.csv: `dist/paper/numbers.csv` (step 08) is written by the pipeline itself; "
              "'agrees' means that the independent count here gives the same number."]
    written.append(nu.write_text(out / "README.md", "\n".join(lines).rstrip() + "\n"))

    print(f"[09]   {len(claims)} claims: " + ", ".join(f"{total[s]} {ICON[s]}" for s in ("OK", "DIFF", "TODO", "NEW")
                                                       if total[s]))
    for c in look:
        print(f"[09]   check: {c.cid} ({c.section}) {c.statement}: paper {c.paper}, counted {c.value}, {c.status}"
              f"{', numbers.csv ' + c.numbers_csv if c.numbers_csv == 'differ' else ''}")
    if cross_bad:
        print(f"[09]   {len(cross_bad)} numbers differ from dist/paper/numbers.csv")
    return written


if __name__ == "__main__":
    main()
