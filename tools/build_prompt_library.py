#!/usr/bin/env python3
"""Build reference/prompt-library.qmd from the prompts taught in the day pages.

A reusable prompt is marked in its page, directly above its ```text block:

    <!-- prompt: soap-note | SOAP progress note | Turn jotted visit facts into a progress note -->
    ```text
    ROLE: ...
    ```

The library is generated so that the page a participant copies from can never differ
from the page that taught the prompt. Never hand-edit it: edit the prompt where it is
taught, then run this script.

    python tools/build_prompt_library.py           # rebuild the library
    python tools/build_prompt_library.py --check   # fail if it is out of date (CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "reference" / "prompt-library.qmd"
TIMING = ROOT / "course" / "timing.json"

DAYS = {
    "day1": "Day One — Foundations",
    "day2": "Day Two — Applications",
    "day3": "Day Three — Safety & Ethics",
}

MARKER = re.compile(
    r"^<!--\s*prompt:\s*(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)\s*\|\s*(?P<title>[^|]+?)\s*\|\s*(?P<use>.+?)\s*-->\s*$"
)
STRAY = re.compile(r"<!--\s*prompt:")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
ANCHOR = re.compile(r"\{#([A-Za-z0-9_-]+)(?:\s[^}]*)?\}")
BADGE = re.compile(r"\s*\[\d+\s*min\]\{\.time\}")
ATTRS = re.compile(r"\s*\{[^}]*\}\s*$")
NUMBER = re.compile(r"^\d+\.\s+")
TITLE = re.compile(r'^title:\s*"?(.*?)"?\s*$')


def page_order() -> list[str]:
    """Day pages in run-of-show order (from timing.json), then anything else, sorted."""
    ordered: list[str] = []
    if TIMING.exists():
        for day in json.loads(TIMING.read_text(encoding="utf-8"))["days"]:
            for item in day["items"]:
                page = item.get("ref", "").partition("#")[0]
                if page and page not in ordered:
                    ordered.append(page)
    extras = sorted(
        p.relative_to(ROOT).as_posix()
        for d in DAYS
        for p in (ROOT / d).glob("*.qmd")
        if p.relative_to(ROOT).as_posix() not in ordered
    )
    return [p for p in ordered if (ROOT / p).exists()] + extras


def clean_heading(text: str) -> str:
    text = BADGE.sub("", text)
    text = ATTRS.sub("", text)
    return NUMBER.sub("", text).strip()


def extract(page: str) -> list[dict]:
    lines = (ROOT / page).read_text(encoding="utf-8").splitlines()
    front = next((TITLE.match(l).group(1) for l in lines[:12] if TITLE.match(l)), page)
    short = front.split(" — ")[0].strip()
    found, anchor, label = [], None, None
    i = 0
    while i < len(lines):
        line = lines[i]
        h = HEADING.match(line)
        if h:
            a = ANCHOR.search(h.group(2))
            if a:
                anchor, label = a.group(1), clean_heading(h.group(2))
        m = MARKER.match(line.strip())
        if m:
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or lines[j].strip() != "```text":
                raise SystemExit(f"{page}:{i + 1}: prompt marker '{m['slug']}' is not followed by a ```text block")
            k = j + 1
            body = []
            while k < len(lines) and lines[k].strip() != "```":
                body.append(lines[k])
                k += 1
            if k >= len(lines):
                raise SystemExit(f"{page}:{i + 1}: prompt '{m['slug']}' has no closing ```")
            found.append(
                {
                    "slug": m["slug"],
                    "title": m["title"],
                    "use": m["use"],
                    "body": "\n".join(body).rstrip(),
                    "page": page,
                    "anchor": anchor,
                    "where": f"{short}" + (f", {label}" if label else ""),
                    "line": i + 1,
                }
            )
            i = k
        elif STRAY.search(line):
            raise SystemExit(f"{page}:{i + 1}: malformed prompt marker (need: <!-- prompt: slug | Title | when to use -->)")
        i += 1
    return found


def build() -> str:
    prompts: list[dict] = []
    for page in page_order():
        prompts.extend(extract(page))

    seen: dict[str, dict] = {}
    for p in prompts:
        if p["slug"] in seen:
            other = seen[p["slug"]]
            raise SystemExit(f"duplicate prompt slug '{p['slug']}': {other['page']}:{other['line']} and {p['page']}:{p['line']}")
        if "```" in p["body"]:
            raise SystemExit(f"{p['page']}:{p['line']}: prompt '{p['slug']}' contains a code fence")
        seen[p["slug"]] = p

    out = [
        "---",
        'title: "Prompt library"',
        'subtitle: "Every reusable prompt from the course, ready to copy"',
        "---",
        "",
        "::: {.callout-important appearance=\"simple\"}",
        "## Synthetic or de-identified facts only",
        "Replace the `[square brackets]` with facts from a [case card](case-cards.qmd) or a fully de-identified case. Patient identifiers never go into a consumer AI tool: see the [privacy checklist](privacy-checklist.qmd).",
        ":::",
        "",
        "::: {.callout-note appearance=\"simple\"}",
        "## This page is generated",
        "It is built from the prompts in the day pages by `tools/build_prompt_library.py`, so it can never disagree with the page that taught each prompt. To change a prompt, edit it where it is taught. Whatever a prompt returns, run the [three-question check](three-question-check.qmd) on it.",
        ":::",
        "",
    ]

    if not prompts:
        out += ["No prompts have been marked in the day pages yet.", ""]
        return "\n".join(out)

    out += ["| Prompt | Use when | Taught in |", "|---|---|---|"]
    for p in prompts:
        target = f"../{p['page']}" + (f"#{p['anchor']}" if p["anchor"] else "")
        out.append(f"| [{p['title']}](#p-{p['slug']}) | {p['use']} | [{p['where']}]({target}) |")
    out.append("")

    current = None
    for p in prompts:
        day = p["page"].split("/")[0]
        if day != current:
            out += [f"## {DAYS.get(day, day)}", ""]
            current = day
        target = f"../{p['page']}" + (f"#{p['anchor']}" if p["anchor"] else "")
        out += [
            f"### {p['title']} {{#p-{p['slug']}}}",
            "",
            f"**Use when:** {p['use']}  ",
            f"**Taught in:** [{p['where']}]({target})",
            "",
            "```text",
            p["body"],
            "```",
            "",
        ]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if the library is out of date")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    text = build()
    count = text.count("\n```text\n")
    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
        if current != text:
            print("reference/prompt-library.qmd is out of date. Run: python tools/build_prompt_library.py", file=sys.stderr)
            return 1
        print(f"prompt library: up to date ({count} prompts)")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {OUT.relative_to(ROOT).as_posix()} ({count} prompts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
