#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py -- recount every number of the paper

    python main.py

Reads the tables under dist/ and the snapshots under data/raw/, counts every
number that the text of the paper states (py/claims/) and writes the result to
dist/09-claims/: claims.csv (one row per number) and CLAIMS-*.md (what is
counted, from which file, and why).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "py"))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import step_09_claims  # noqa: E402

if __name__ == "__main__":
    for path in step_09_claims.main():
        print("wrote", path)
