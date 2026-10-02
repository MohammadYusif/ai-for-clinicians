#!/usr/bin/env python3
"""Structural checks for the decks in slides/, run on the source, before anything renders.

reveal.js is unforgiving about a few things that Quarto renders without complaint and that only show
up as a broken slide in the browser. This catches them in the .qmd:

  * a "##" or "###" heading inside a ::: div: pandoc turns it into a nested <section>, and reveal.js
    makes the slide a vertical stack (callout titles, the first line inside a ::: callout, are fine;
    use a [Title]{.t} paragraph in a card instead);
  * a ::: notes block before the first heading: it becomes an empty slide of its own;
  * unbalanced ::: fences;
  * a "#" or "##" slide with no {#id}, or an id used twice in one deck (the id is the slide's URL);
  * an {{< include >}} of a file that does not exist.

    python tools/check_decks.py                       # every deck
    python tools/check_decks.py slides/m2-prompting.qmd
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
BRACES = re.compile(r"\{([^}]*)\}\s*$")
QUOTED = re.compile(r'"[^"]*"')
ID = re.compile(r"#([A-Za-z0-9_-]+)")
DIV_OPEN = re.compile(r"^\s*(:{3,})\s*(\{.*\}|\S+)\s*$")
DIV_CLOSE = re.compile(r"^\s*:{3,}\s*$")
INCLUDE = re.compile(r"\{\{<\s*include\s+(\S+)\s*>\}\}")


def check(path: Path) -> list[str]:
    rel = path.relative_to(ROOT).as_posix()
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    stack: list[tuple[str, int, int]] = []  # (attrs, line, non-empty lines seen inside)
    ids: dict[str, int] = {}
    seen_heading = False
    fenced = False
    for no in range(i, len(lines)):
        line = lines[no]
        n = no + 1
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        if fenced:
            continue
        for inc in INCLUDE.findall(line):
            if not (path.parent / inc).exists():
                errors.append(f"{rel}:{n}: include not found: {inc}")
        if DIV_CLOSE.match(line):
            if not stack:
                errors.append(f"{rel}:{n}: a ::: closes nothing")
            else:
                stack.pop()
            continue
        m = DIV_OPEN.match(line)
        if m:
            attrs = m.group(2)
            if "notes" in attrs and not seen_heading:
                errors.append(f"{rel}:{n}: ::: notes before the first heading becomes an empty slide; put it under a heading")
            stack.append((attrs, n, 0))
            continue
        h = HEADING.match(line)
        if h:
            level = len(h.group(1))
            if stack:
                attrs, at, seen = stack[-1]
                callout_title = "callout" in attrs and seen == 0 and level == 2
                if not callout_title:
                    errors.append(f"{rel}:{n}: a heading inside the ::: div opened at line {at} becomes a nested slide; use a [Title]{{.t}} paragraph")
            else:
                seen_heading = True
                if level <= 2:
                    braces = BRACES.search(h.group(2))
                    # a colour in an attribute ("#4338ca") is not the slide's id
                    idm = ID.search(QUOTED.sub("", braces.group(1))) if braces else None
                    if not idm:
                        errors.append(f"{rel}:{n}: slide has no {{#id}}: {h.group(2)[:50]}")
                    elif idm.group(1) in ids:
                        errors.append(f"{rel}:{n}: id '{idm.group(1)}' is also used at line {ids[idm.group(1)]}")
                    else:
                        ids[idm.group(1)] = n
            if stack:
                a, at, seen = stack[-1]
                stack[-1] = (a, at, seen + 1)
            continue
        if line.strip() and stack:
            a, at, seen = stack[-1]
            stack[-1] = (a, at, seen + 1)
    for attrs, at, _ in stack:
        errors.append(f"{rel}:{at}: ::: {attrs} is never closed")
    return errors


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    only = {Path(a).resolve() for a in sys.argv[1:]}
    decks = sorted(p for p in (ROOT / "slides").glob("*.qmd") if not p.name.startswith("_"))
    if only:
        decks = [d for d in decks if d.resolve() in only]
    errors: list[str] = []
    for d in decks:
        errors += check(d)
    if errors:
        print("DECK STRUCTURE ERRORS:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    print(f"decks: {len(decks)} deck(s), structure ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
