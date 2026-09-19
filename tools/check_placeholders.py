#!/usr/bin/env python3
"""Fail if an unfinished-work marker is left in a page that will be published.

Authors leave [TRAINER TO CONFIRM: ...] or [LINK NEEDED: ...] where a fact is unknown. Those
belong in course/instructor-guide.md ("Open decisions"), not on a public course site, so the
publish workflow refuses to deploy while any remain in the rendered pages.

    python tools/check_placeholders.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"TRAINER TO CONFIRM|LINK NEEDED|\bTODO\b|\bFIXME\b|LOREM IPSUM")
GLOBS = ["*.qmd", "day1/*.qmd", "day2/*.qmd", "day3/*.qmd", "reference/*.qmd"]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    hits = []
    for pattern in GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            for no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if PATTERN.search(line):
                    hits.append(f"{path.relative_to(ROOT).as_posix()}:{no}: {line.strip()[:140]}")
    if hits:
        print("UNFINISHED PLACEHOLDERS in published pages:", file=sys.stderr)
        for h in hits:
            print(f"  {h}", file=sys.stderr)
        return 1
    print("placeholders: none left in published pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
