#!/usr/bin/env python3
"""Check that the course clock adds up.

course/timing.json is the single source for every minute in this course. This
script fails (exit 1) unless:

  1. each day's items sum to exactly `day_minutes` (120), break included;
  2. every item with a `ref` (page#anchor) points at a page that carries a
     heading with that {#anchor} and a matching [N min]{.time} badge, and at a deck
     (slides/<same file name>) with the same heading, anchor and badge;
  3. no page or deck carries a time badge that timing.json does not know about;
  4. the "day at a glance" and per-deck "plan" tables that the decks include
     (slides/_glance-dayN.md, slides/_plan-<deck>.md) are exactly what timing.json says.

It also prints the run-of-show with clock times, and how each day compares with
what course/BRIEF.md scheduled (the brief's Day One summed to 130, or 140 with
its own Lab One spec, while claiming 120 - which is why this check exists).

    python tools/check_timing.py                  # check + print the run-of-show
    python tools/check_timing.py --quiet          # errors only
    python tools/check_timing.py --allow-missing  # sums only; pages not written yet
    python tools/check_timing.py --write-guide    # regenerate the run-of-show and the decks' plan tables

The run-of-show tables in course/instructor-guide.md sit between <!-- runofshow:start --> and
<!-- runofshow:end --> and are generated from timing.json; the check fails if they drift. So are the
tables on the slides: a deck includes them rather than retyping a minute.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMING = ROOT / "course" / "timing.json"

HEADING = re.compile(r"^(#{1,4})\s+(.*?)\s*$")
ANCHOR = re.compile(r"\{#([A-Za-z0-9_-]+)(?:\s[^}]*)?\}")
BADGE = re.compile(r"\[(\d+)\s*min\]\{\.time\}")


def page_headings(path: Path):
    """(line_no, anchor|None, badge_minutes|None) for each heading, skipping code fences."""
    out, fenced = [], False
    for no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = HEADING.match(line)
        if not m:
            continue
        anchor = ANCHOR.search(m.group(2))
        badge = BADGE.search(m.group(2))
        out.append((no, anchor.group(1) if anchor else None, int(badge.group(1)) if badge else None))
    return out


def clock(minutes: int) -> str:
    return f"{minutes // 60}:{minutes % 60:02d}"


GUIDE = ROOT / "course" / "instructor-guide.md"
START, END = "<!-- runofshow:start -->", "<!-- runofshow:end -->"


def deck_of(page: str) -> str:
    """slides/<file> for day1/<file>: a deck has the same file name and the same anchors as its handout."""
    return "slides/" + page.split("/")[-1]


def page_title(page: str) -> str:
    """The front-matter title of a handout, with its em dash turned into a colon."""
    for line in (ROOT / page).read_text(encoding="utf-8").splitlines()[:8]:
        m = re.match(r'^title:\s*"?(.*?)"?\s*$', line)
        if m:
            return m.group(1).replace(" — ", ": ")
    return page


def runofshow_markdown(data: dict) -> str:
    """The run-of-show tables, generated from timing.json so the instructor guide cannot go stale."""
    out: list[str] = []
    for day in data["days"]:
        out += [f"### Day {day['day']}: {day['title']}", "", "| Clock | Min | Topic | Slides | Handout |", "|---|---:|---|---|---|"]
        at = 0
        for i in day["items"]:
            if i.get("break"):
                slides = handout = "-"
            else:
                path, _, anchor = i["ref"].partition("#")
                stem = path.split("/")[-1][:-4]
                slides = f"[{stem}#{anchor}](../{deck_of(path)}#/{anchor})"
                handout = f"[{stem}#{anchor}](../{i['ref']})"
            out.append(f"| {clock(at)} | {i['min']} | {i['title']} | {slides} | {handout} |")
            at += i["min"]
        out += ["", f"Total {at} min.", ""]
    return "\n".join(out).rstrip() + "\n"


def day_blocks(day: dict) -> list[tuple[int, str, int]]:
    """(start minute, name, minutes) for a day, consecutive items from one page merged into one block."""
    blocks: list[list] = []
    at = 0
    for i in day["items"]:
        page = None if i.get("break") else i["ref"].partition("#")[0]
        if blocks and blocks[-1][3] == page and page is not None:
            blocks[-1][2] += i["min"]
        else:
            name = "Break" if page is None else page_title(page)
            blocks.append([at, name, i["min"], page])
        at += i["min"]
    return [(a, n, m) for a, n, m, _ in blocks]


def generated_tables(data: dict) -> dict[str, str]:
    """slides/_glance-dayN.md and slides/_plan-<deck>.md: the clock as the decks show it."""
    files: dict[str, str] = {}
    note = "<!-- Generated from course/timing.json by tools/check_timing.py --write-guide. Do not edit. -->\n\n"
    for day in data["days"]:
        rows = ["| Clock | Block | Min |", "|---|---|---:|"]
        rows += [f"| {clock(a)} | {n} | {m} |" for a, n, m in day_blocks(day)]
        files[f"slides/_glance-day{day['day']}.md"] = note + "\n".join(rows) + "\n"
        per: dict[str, list[str]] = {}
        at = 0
        for i in day["items"]:
            if not i.get("break"):
                stem = i["ref"].partition("#")[0].split("/")[-1][:-4]
                per.setdefault(stem, []).append(f"| {clock(at)} | {i['title']} | {i['min']} |")
            at += i["min"]
        for stem, lines in per.items():
            files[f"slides/_plan-{stem}.md"] = note + "\n".join(["| Day clock | Topic | Min |", "|---|---|---:|"] + lines) + "\n"
    return files


def sync_tables(data: dict, write: bool, allow_missing: bool) -> list[str]:
    errors: list[str] = []
    for rel, wanted in generated_tables(data).items():
        path = ROOT / rel
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == wanted:
            continue
        if write:
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(wanted)
            print(f"wrote {rel}")
        elif not (allow_missing and current is None):
            errors.append(f"{rel}: out of date; run python tools/check_timing.py --write-guide")
    return errors


CARD = re.compile(r'data-block="([a-z0-9-]+)"\}\s*\n\[[^\]]*\]\{\.kicker\}\s*\[(\d+) min\]\{\.mins\}')


def check_index(data: dict) -> list[str]:
    """The home page's course map shows each module's and lab's minutes; they must be the clock's."""
    index = ROOT / "index.qmd"
    if not index.exists():
        return []
    totals: dict[str, int] = {}
    for day in data["days"]:
        for i in day["items"]:
            if not i.get("break"):
                stem = i["ref"].partition("#")[0].split("/")[-1][:-4]
                totals[stem] = totals.get(stem, 0) + i["min"]
    shown = {m.group(1): int(m.group(2)) for m in CARD.finditer(index.read_text(encoding="utf-8"))}
    errors = []
    for stem, minutes in totals.items():
        if stem not in shown:
            errors.append(f"index.qmd: no course card for {stem} (data-block, kicker and minutes)")
        elif shown[stem] != minutes:
            errors.append(f"index.qmd: the card for {stem} says {shown[stem]} min, timing.json says {minutes}")
    for stem in shown:
        if stem not in totals:
            errors.append(f"index.qmd: a course card for {stem}, which timing.json does not list")
    return errors


def sync_guide(data: dict, write: bool, allow_missing: bool) -> list[str]:
    """Keep the run-of-show block in course/instructor-guide.md identical to timing.json."""
    if not GUIDE.exists():
        return [] if allow_missing else ["course/instructor-guide.md is missing"]
    text = GUIDE.read_text(encoding="utf-8")
    if START not in text or END not in text:
        return [f"course/instructor-guide.md has no {START} / {END} markers"]
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    wanted = f"{head}{START}\n{runofshow_markdown(data)}{END}{tail}"
    if wanted == text:
        return []
    if write:
        with open(GUIDE, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(wanted)
        print("wrote the run-of-show into course/instructor-guide.md")
        return []
    return ["course/instructor-guide.md: the run-of-show is out of date; run python tools/check_timing.py --write-guide"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true", help="print errors only")
    ap.add_argument("--allow-missing", action="store_true", help="skip page checks for pages that do not exist yet")
    ap.add_argument("--write-guide", action="store_true", help="regenerate the run-of-show block in course/instructor-guide.md")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    data = json.loads(TIMING.read_text(encoding="utf-8"))
    target = data["day_minutes"]
    errors: list[str] = []

    for day in data["days"]:
        items = day["items"]
        total = sum(i["min"] for i in items)
        brief = sum(i["brief_min"] for i in items)
        head = f"Day {day['day']} - {day['title']}"

        if total != target:
            errors.append(f"{head}: schedule sums to {total} min, target is {target}")

        expected: dict[str, dict[str, int]] = {}
        for i in items:
            if "ref" in i:
                page, _, anchor = i["ref"].partition("#")
                expected.setdefault(page, {})[anchor] = i["min"]

        for page, anchors in [(p, a) for p, a in expected.items()] + [(deck_of(p), a) for p, a in expected.items()]:
            path = ROOT / page
            if not path.exists():
                if not args.allow_missing:
                    errors.append(f"{head}: page not found: {page}")
                continue
            found = page_headings(path)
            by_anchor = {a: (no, b) for no, a, b in found if a}
            for anchor, minutes in anchors.items():
                if anchor not in by_anchor:
                    errors.append(f"{page}: no heading with {{#{anchor}}}")
                    continue
                no, badge = by_anchor[anchor]
                if badge is None:
                    errors.append(f"{page}:{no}: {{#{anchor}}} has no [N min]{{.time}} badge (expected {minutes})")
                elif badge != minutes:
                    errors.append(f"{page}:{no}: {{#{anchor}}} says {badge} min, timing.json says {minutes}")
            for no, anchor, badge in found:
                if badge is not None and anchor not in anchors:
                    errors.append(f"{page}:{no}: time badge on a heading that timing.json does not list ({anchor or 'no id'})")

        if not args.quiet:
            print(f"\n{head}")
            at = 0
            for i in items:
                where = i.get("ref", "-")
                flag = "" if i["min"] == i["brief_min"] else f"   (brief: {i['brief_min']})"
                print(f"  {clock(at)}  {i['min']:>3} min  {i['title']:<46} {where}{flag}")
                at += i["min"]
            status = "OK" if total == target else "WRONG"
            delta = f"{total - brief:+d}" if total != brief else "same as brief"
            print(f"  total {total} min (target {target}) {status}; the brief scheduled {brief} ({delta})")

    errors += sync_guide(data, args.write_guide, args.allow_missing)
    errors += sync_tables(data, args.write_guide, args.allow_missing)
    errors += check_index(data)

    if errors:
        print("\nTIMING ERRORS:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    if not args.quiet:
        print("\ntiming: every day sums to %d min and every badge matches" % target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
