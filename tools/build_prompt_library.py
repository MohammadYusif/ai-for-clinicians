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

The decks need the same text on a slide, because on the call the trainer pastes it into the chat
and everyone copies it from there. So this script also writes one small file per block into
slides/ (`_paste-<slug>.md`, a fenced block a deck pulls in with {{< include _paste-<slug>.md >}}):

  * every prompt above;
  * every lab block marked `<!-- paste: slug | What it is -->` above its ```text block (a case's
    facts, a one-line prompt, a warning line: things to paste that are not reusable prompts);
  * every case card in reference/case-cards.qmd, as `_paste-case-a.md` ... `_paste-case-e.md`.

A deck never types a prompt: the handout teaches it, the deck includes it, and --check fails if the
two ever differ.

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
PASTE_MARKER = re.compile(r"^<!--\s*paste:\s*(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)\s*\|\s*(?P<title>.+?)\s*-->\s*$")
STRAY = re.compile(r"<!--\s*(prompt|paste):")
CARDS = ROOT / "reference" / "case-cards.qmd"
PASTE_DIR = ROOT / "slides"
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


def fenced_body(lines: list[str], i: int, page: str, what: str) -> tuple[list[str], int]:
    """The text block that follows the marker on line i: (its lines, index of its closing fence)."""
    fence = "`" * 3
    j = i + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j >= len(lines) or lines[j].strip() != fence + "text":
        raise SystemExit(f"{page}:{i + 1}: {what} is not followed by a text block")
    k = j + 1
    body = []
    while k < len(lines) and lines[k].strip() != fence:
        body.append(lines[k])
        k += 1
    if k >= len(lines):
        raise SystemExit(f"{page}:{i + 1}: {what} has no closing fence")
    return body, k


def extract(page: str) -> tuple[list[dict], list[dict]]:
    """(prompts, pastes) marked in one page."""
    lines = (ROOT / page).read_text(encoding="utf-8").splitlines()
    front = next((TITLE.match(l).group(1) for l in lines[:12] if TITLE.match(l)), page)
    short = front.split(" — ")[0].strip()
    found, pastes, anchor, label = [], [], None, None
    i = 0
    while i < len(lines):
        line = lines[i]
        h = HEADING.match(line)
        if h:
            a = ANCHOR.search(h.group(2))
            if a:
                anchor, label = a.group(1), clean_heading(h.group(2))
        m = MARKER.match(line.strip())
        pm = PASTE_MARKER.match(line.strip())
        if pm:
            body, k = fenced_body(lines, i, page, f"paste marker '{pm['slug']}'")
            pastes.append({"slug": pm["slug"], "title": pm["title"], "body": "\n".join(body).rstrip(), "page": page, "line": i + 1})
            i = k
        elif m:
            body, k = fenced_body(lines, i, page, f"prompt marker '{m['slug']}'")
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
            raise SystemExit(
                f"{page}:{i + 1}: malformed marker (need: <!-- prompt: slug | Title | when to use --> or <!-- paste: slug | What it is -->)"
            )
        i += 1
    return found, pastes


def card_blocks() -> list[dict]:
    """Each case card as a block to paste: a first line naming the case, then its bullets, as plain text."""
    out: list[dict] = []
    lines = CARDS.read_text(encoding="utf-8").splitlines()
    letter, header, bullets, in_block = None, "", [], False
    for line in lines:
        h = re.match(r"^## Case ([A-E]) .*\{#case-([a-e])\}", line)
        if h:
            letter, header, bullets, in_block = h.group(2), "", [], False
        elif letter and line.startswith("## "):
            letter = None
        elif letter and line.strip().startswith("::: {.case-card"):
            in_block = True
        elif letter and in_block and line.strip() == ":::":
            setting = header.replace("Synthetic patient · ", "").replace(" · ", ", ")
            body = f"CASE {letter.upper()} (fictional patient): {setting}\n" + "\n".join(bullets)
            out.append({"slug": f"case-{letter}", "title": f"Case {letter.upper()}", "body": body, "page": "reference/case-cards.qmd", "line": 0})
            letter, in_block = None, False
        elif letter and in_block and line.startswith("**") and line.rstrip().endswith("**"):
            header = line.strip().strip("*").strip()
        elif letter and in_block and line.startswith("- "):
            bullets.append(line.replace("**", "").rstrip())
    return out


def source_block() -> list[dict]:
    """The practice source (reference/practice-source.qmd) as a block to paste: its title, then its numbered rules."""
    path = ROOT / "reference" / "practice-source.qmd"
    title, rules, in_block = "", [], False
    for line in path.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^## (Protocol .*?)\s*\{#protocol\}", line)
        if h:
            title, in_block = h.group(1), False
        elif title and line.strip().startswith("::: {.case-card"):
            in_block = True
        elif title and in_block and line.strip() == ":::":
            break
        elif title and in_block and re.match(r"^\d+\. ", line):
            rules.append(line.replace("**", "").rstrip())
    if not rules:
        raise SystemExit("reference/practice-source.qmd: could not read the numbered rules under {#protocol}")
    return [{"slug": "practice-source", "title": "The practice source", "body": title.upper().replace("(FICTIONAL)", "(fictional)") + "\n" + "\n".join(rules), "page": "reference/practice-source.qmd", "line": 0}]


def build() -> tuple[str, dict[str, str]]:
    """(the library page, {file name: text} for every slides/_paste-*.md)."""
    prompts: list[dict] = []
    pastes: list[dict] = []
    for page in page_order():
        found, marked = extract(page)
        prompts.extend(found)
        pastes.extend(marked)
    pastes.extend(card_blocks())
    pastes.extend(source_block())

    fence = "`" * 3
    files: dict[str, str] = {}
    for item in [*prompts, *pastes]:
        name = f"_paste-{item['slug']}.md"
        if name in files:
            raise SystemExit(
                f"duplicate block slug '{item['slug']}' ({item['page']}:{item['line']}): prompts, paste blocks and case cards share one namespace"
            )
        if fence in item["body"]:
            raise SystemExit(f"{item['page']}:{item['line']}: block '{item['slug']}' contains a code fence")
        files[name] = (
            f"<!-- Generated from {item['page']} by tools/build_prompt_library.py. Do not edit. -->\n\n"
            f"{fence}text\n{item['body']}\n{fence}\n"
        )

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
        return "\n".join(out), files

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
    return "\n".join(out), files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if the library is out of date")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    text, files = build()
    count = text.count("\n" + "`" * 3 + "text\n")
    existing = {p.name for p in PASTE_DIR.glob("_paste-*.md")}
    if args.check:
        stale: list[str] = []
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
        if current != text:
            stale.append("reference/prompt-library.qmd")
        for name, body in files.items():
            path = PASTE_DIR / name
            if not path.exists() or path.read_text(encoding="utf-8") != body:
                stale.append(f"slides/{name}")
        stale += [f"slides/{n} (no longer marked in any page)" for n in sorted(existing - set(files))]
        if stale:
            print("out of date: " + ", ".join(stale) + ". Run: python tools/build_prompt_library.py", file=sys.stderr)
            return 1
        print(f"prompt library: up to date ({count} prompts, {len(files)} blocks for the decks)")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    for name, body in files.items():
        with open(PASTE_DIR / name, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(body)
    for name in existing - set(files):
        (PASTE_DIR / name).unlink()
    print(f"wrote {OUT.relative_to(ROOT).as_posix()} ({count} prompts) and {len(files)} blocks in slides/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
