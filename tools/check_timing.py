#!/usr/bin/env python3
"""Check that the course clock adds up.

course/timing.json is the single source for every minute in this course. This
script fails (exit 1) unless:

  1. each day's items sum to exactly `day_minutes` (120), break included;
  2. every item with a `ref` (page#anchor) points at a page that carries a
     heading with that {#anchor} and a matching [N min]{.time} badge;
  3. no page carries a time badge that timing.json does not know about.

It also prints the run-of-show with clock times, and how each day compares with
what course/BRIEF.md scheduled (the brief's Day One summed to 130, or 140 with
its own Lab One spec, while claiming 120 - which is why this check exists).

    python tools/check_timing.py                  # check + print the run-of-show
    python tools/check_timing.py --quiet          # errors only
    python tools/check_timing.py --allow-missing  # sums only; pages not written yet
    python tools/check_timing.py --write-guide    # regenerate the run-of-show in course/instructor-guide.md

The run-of-show tables in course/instructor-guide.md sit between <!-- runofshow:start --> and
<!-- runofshow:end --> and are generated from timing.json; the check fails if they drift.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMING = ROOT / "course" / "timing.json"

HEADING = re.compile(r"^(#{2,4})\s+(.*?)\s*$")
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


def runofshow_markdown(data: dict) -> str:
    """The run-of-show tables, generated from timing.json so the instructor guide cannot go stale."""
    out: list[str] = []
    for day in data["days"]:
        out += [f"### Day {day['day']}: {day['title']}", "", "| Clock | Min | Topic | Site page |", "|---|---:|---|---|"]
        at = 0
        for i in day["items"]:
            if i.get("break"):
                page = "-"
            else:
                path, _, anchor = i["ref"].partition("#")
                page = f"[{path.split('/')[-1][:-4]}#{anchor}](../{i['ref']})"
            out.append(f"| {clock(at)} | {i['min']} | {i['title']} | {page} |")
            at += i["min"]
        out += ["", f"Total {at} min.", ""]
    return "\n".join(out).rstrip() + "\n"


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

        for page, anchors in expected.items():
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
