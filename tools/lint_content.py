#!/usr/bin/env python3
"""Mechanical checks for the authoring rules in course/authoring-guide.md.

Errors (exit 1):
  * the canonical wording is missing where the course depends on it (the rule, the three
    questions, the four parts, the verification workflow, the privacy line);
  * a banned claim appears in a published page: "outperform", "beats generic prompting",
    "studies show", PDPL article numbers or fine amounts, an external URL nobody vouched for,
    an AI attribution line;
  * a timed section does not carry exactly one "Keep this" closing callout;
  * wording that assumes people share a room (a neighbor, a show of hands, a whiteboard, paper, a
    projector): the course is delivered online (CLAUDE.md, rule 5). Use the chat, a breakout pair, or
    a shared screen, as course/authoring-guide.md section 9 describes;
  * a deck's speaker notes run past the limit (900 characters, 1,600 on a topic slide).

Warnings (printed, exit 0): percentages and exclamation marks in prose outside the case cards,
which need a human to decide whether they are a case fact or an invented claim.

    python tools/lint_content.py                       # everything
    python tools/lint_content.py slides/m2-prompting.qmd   # just these files (for an author mid-edit)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOBS = ["*.qmd", "day1/*.qmd", "day2/*.qmd", "day3/*.qmd", "reference/*.qmd", "slides/*.qmd"]
# Trainer-facing notes are held to the same online-first wording. BRIEF.md is the source brief, kept verbatim.
COURSE_DOCS = ["course/*.md"]
VERBATIM = {"course/BRIEF.md"}

REQUIRED: dict[str, list[str]] = {
    "day1/m1-rule-and-mechanics.qmd": [
        "AI drafts. You decide.",
        "Could I defend this to a colleague?",
        "Does it point to something I can verify?",
        "Would I catch it if it were wrong?",
    ],
    "reference/three-question-check.qmd": [
        "Could I defend this to a colleague?",
        "Does it point to something I can verify?",
        "Would I catch it if it were wrong?",
        "If the answer to any of these is no, that's the signal to slow down, not the finding to accept.",
    ],
    "day1/m2-prompting.qmd": [
        "ROLE:",
        "CONTEXT:",
        "FORMAT:",
        "CONSTRAINTS:",
        "Use ONLY the facts below. If something needed is missing, write [MISSING: what] instead of guessing.",
        "Who it is, what it knows, what shape to return, what to avoid",
    ],
    "day3/m6-confidently-wrong.qmd": ["Draft with AI", "Cross-check the source", "Confirm or correct", "Tone is not a signal"],
    "day3/m7-privacy.qmd": ["No patient identifiers into a consumer AI tool. Ever. Full stop."],
    "reference/privacy-checklist.qmd": ["No patient identifiers into a consumer AI tool. Ever. Full stop."],
    # The decks teach the same sentences, so they carry the same canonical wording as the pages.
    "slides/m1-rule-and-mechanics.qmd": [
        "AI drafts. You decide.",
        "Could I defend this to a colleague?",
        "Does it point to something I can verify?",
        "Would I catch it if it were wrong?",
        "If the answer to any of these is no, that's the signal to slow down, not the finding to accept.",
        "No patient identifiers into a consumer AI tool. Ever. Full stop.",
    ],
    "slides/m2-prompting.qmd": [
        "ROLE:",
        "CONTEXT:",
        "FORMAT:",
        "CONSTRAINTS:",
        "Use ONLY the facts below. If something needed is missing, write [MISSING: what] instead of guessing.",
        "Who it is, what it knows, what shape to return, what to avoid",
    ],
    "slides/m6-confidently-wrong.qmd": ["Draft with AI", "Cross-check the source", "Confirm or correct", "Tone is not a signal"],
    "slides/m7-privacy.qmd": ["No patient identifiers into a consumer AI tool. Ever. Full stop."],
}

BANNED = [
    (re.compile(r"\boutperform\w*", re.I), "claims a tool 'outperforms'; the brief supports no such comparison"),
    (re.compile(r"\bbeats?\s+(generic|general)\b|\bbetter than generic\b", re.I), "claims purpose-built tools beat generic prompting; the Sahl AI pilot did not test that"),
    (re.compile(r"\bstudies (show|have shown|suggest)\b|\bresearch (shows|has shown)\b|\baccording to (a )?(study|studies)\b", re.I), "an unsourced 'studies show' claim"),
    (re.compile(r"\bArticle\s+\d+\b|\bمادة\s*\d+", re.I), "a PDPL article number; the brief supplies none"),
    (re.compile(r"\b(SAR|SR)\s*[\d,]+|\b[\d,.]+\s*(million|billion)?\s*riyals?\b|\bfines? of\b|\bimprisonment\b", re.I), "a fine or penalty amount; the brief supplies none"),
    (re.compile(r"Co-Authored-By|Generated with|Anthropic"), "an AI attribution or vendor line"),
    # The course relies on no tool but one general assistant (CLAUDE.md, rule 4). These phrasings made a
    # verification step or a specific product a requirement; they must not come back.
    (re.compile(r"verified for your account|professional verification before|complete .{0,30}professional verification|Vera Health verification|\b(two|both) accounts\b|neighbor who has access", re.I), "makes a specific tool or a verification step a requirement (CLAUDE.md, rule 4)"),
]
# The course is delivered online (CLAUDE.md, rule 5). Everyone is on their own device, so nothing may
# assume a neighbor, a whiteboard, paper or a projector. Checked on prose only, so a fenced block that
# shows a forbidden phrase as an example (the authoring guide does) is not itself an error.
ONLINE_WHY = "assumes people share a room; the course runs online (CLAUDE.md, rule 5): use the chat, a breakout pair, or a shared screen"
ONLINE = [
    # "a colleague, a neighbor, or the family" is about who might recognize a patient, not about who sits where.
    re.compile(r"\bneighbou?rs?\b(?!, or the family)", re.I),
    re.compile(r"next to you|beside you|next to each other|person next|sitting next", re.I),
    re.compile(r"\bin pairs\b|\bpair (up|with)\b|\bpair people\b|\bin triads?\b|\bswap (screens?|with)\b", re.I),
    re.compile(r"show of hands|\bhands? up\b|raise (your|a) hand|hold(s)? up (one|two|three|\d)|finger game|\bfingers\b", re.I),
    re.compile(r"walk (around|the room)|round the room|go round the", re.I),
    re.compile(r"\bthe (whole |entire )?room\b|\ba room of\b|training room|\bvenue\b|\barrive\b", re.I),
    re.compile(r"whiteboard|flip ?chart|\bon paper\b|\bprojector\b|\bproject(s|ed)? (the|it|this|one|them|a)\b", re.I),
    re.compile(r"\bprint(ed|able)?\b|\bhand(ed)? out\b|in person|in-person|classroom", re.I),
]
NOTES_OPEN = re.compile(r"^:::\s*notes\s*$")
NOTES_LIMIT, TOPIC_NOTES_LIMIT = 900, 1600

# The course's fixed vocabulary (authoring guide, section 1). A reader who meets a differently
# worded name will assume it is a different tool, so drift is worth a warning.
VOCAB = [
    (re.compile(r"\b4[- ]part\b|\bfour part\b", re.I), "the four-part framework (spelled out, hyphenated)"),
    (re.compile(r"\b(3|three)[ ]question[ -]check\b|\b3-question\b|\bthree questions? check\b", re.I), "the three-question check"),
    (re.compile(r"\bverification (process|procedure|routine)\b", re.I), "the verification workflow"),
    (re.compile(r"\bfabricated source\b", re.I), "a fabricated citation (the fourth kind of error, after invented, omitted, altered)"),
]
URL = re.compile(r"https?://[^\s)>\]\"']+")
# External URLs somebody has opened and vouched for. Anything else fails the lint.
ALLOWED_URLS: set[str] = {
    # Sahl AI pilot paper, JMIR Medical Informatics, March 2026 (title, journal and design confirmed by search on 2026-09-19)
    "https://medinform.jmir.org/2026/1/e83335",
    # Augnito / Almoosa Health press release, 31 January 2025 (fetched; future tense: "will see ... integrated")
    "https://www.prnewswire.com/news-releases/augnito-secures-major-enterprise-partnership-with-almoosa-health-302365216.html",
    # Vera Health Terms of Service: eligibility and sanctions clauses quoted in Module 3 (fetched 2026-09-19)
    "https://www.verahealth.ai/terms",
}

TIMED = re.compile(r"^##\s+.*\[\d+\s*min\]\{\.time\}")
KEEP = re.compile(r"^##\s+Keep this\s*$")
H2 = re.compile(r"^##\s+")
DIV_OPEN = re.compile(r"^\s*:{3,}\s*(\{|\S)")
DIV_CLOSE = re.compile(r"^\s*:{3,}\s*$")
PERCENT = re.compile(r"\d\s*%")


def card_bullets(card: str) -> list[str]:
    """The bullet lines of one case card, e.g. card='a' for the block under {#case-a}."""
    lines = (ROOT / "reference" / "case-cards.qmd").read_text(encoding="utf-8").splitlines()
    out, seen, in_block = [], False, False
    for line in lines:
        if line.startswith("## ") and f"{{#case-{card}}}" in line:
            seen = True
        elif line.startswith("## ") and seen:
            break
        elif seen and line.strip().startswith("::: {.case-card"):
            in_block = True
        elif seen and in_block and line.strip() == ":::":
            break
        elif seen and in_block and line.startswith("- "):
            out.append(line[2:].strip())
    return out


# Pages that paste a case card's facts into a prompt block. The paste is a copy, so it is
# checked against the card: a card that changes must change here too.
CARD_COPIES = {"day1/lab1-templates-and-limits.qmd": "a"}


def prose_lines(path: Path):
    """(line_no, text) for lines outside code fences."""
    fenced = False
    for no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        if not fenced:
            yield no, line


def deck_notes_errors(rel: str, lines: list[str]) -> list[str]:
    """A deck's speaker notes: at most NOTES_LIMIT characters, TOPIC_NOTES_LIMIT on a "#" topic slide."""
    out: list[str] = []
    level, in_notes, start, buf, fenced = 0, False, 0, [], False
    for no, line in enumerate(lines, 1):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        if fenced:
            continue
        if in_notes:
            if DIV_CLOSE.match(line):
                size = len(" ".join(buf).strip())
                limit = TOPIC_NOTES_LIMIT if level == 1 else NOTES_LIMIT
                if size > limit:
                    out.append(f"{rel}:{start}: speaker notes are {size} characters, the limit is {limit}")
                in_notes, buf = False, []
            elif line.strip():
                buf.append(line.strip())
            continue
        m = re.match(r"^(#{1,2})\s", line)
        if m:
            level = len(m.group(1))
        elif NOTES_OPEN.match(line):
            in_notes, start = True, no
    return out


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []
    only = {Path(a).resolve() for a in sys.argv[1:]}

    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists() or (only and path.resolve() not in only):
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"{rel}: missing the canonical wording: {needle!r}")

    for rel, card in CARD_COPIES.items():
        path = ROOT / rel
        if path.exists():
            body = path.read_text(encoding="utf-8")
            expected = card_bullets(card)
            if not expected:
                errors.append(f"{rel}: could not read the bullets of case card {card.upper()} from reference/case-cards.qmd")
            for bullet in expected:
                if bullet not in body:
                    errors.append(f"{rel}: the pasted Case {card.upper()} block has drifted from the card; missing: {bullet[:80]!r}")

    # The trainer's notes are held to the online-first wording too (and nothing else here).
    for g in COURSE_DOCS:
        for path in sorted(ROOT.glob(g)):
            rel = path.relative_to(ROOT).as_posix()
            if rel in VERBATIM or (only and path.resolve() not in only):
                continue
            for no, line in prose_lines(path):
                for pattern in ONLINE:
                    if pattern.search(line):
                        errors.append(f"{rel}:{no}: {ONLINE_WHY}: {line.strip()[:110]}")
                        break

    pages = sorted({p for g in GLOBS for p in ROOT.glob(g) if not p.name.startswith("_")})
    if only:
        pages = [p for p in pages if p.resolve() in only]
    for path in pages:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        for no, line in prose_lines(path):
            for pattern in ONLINE:
                if pattern.search(line):
                    errors.append(f"{rel}:{no}: {ONLINE_WHY}: {line.strip()[:110]}")
                    break
        if rel.startswith("slides/"):
            errors += deck_notes_errors(rel, lines)

        for pattern, why in BANNED:
            for no, line in enumerate(lines, 1):
                if pattern.search(line):
                    errors.append(f"{rel}:{no}: {why}: {line.strip()[:110]}")

        for no, line in enumerate(lines, 1):
            for url in URL.findall(line):
                if url.rstrip(".,;") not in ALLOWED_URLS:
                    errors.append(f"{rel}:{no}: external URL not vouched for: {url}")

        # Exactly one "## Keep this" callout heading inside each timed section. A callout's title is
        # itself written as a "##" heading inside a ::: div, so only "##" lines at div depth 0 start
        # or end a section; anything inside a div (or a code fence) is content.
        if any(TIMED.match(l) for l in lines):
            sections: list[tuple[int, str, int]] = []
            current = None
            depth, fenced = 0, False
            for no, line in enumerate(lines, 1):
                if line.lstrip().startswith(("```", "~~~")):
                    fenced = not fenced
                    continue
                if fenced:
                    continue
                if DIV_CLOSE.match(line):
                    depth = max(0, depth - 1)
                elif DIV_OPEN.match(line):
                    depth += 1
                elif H2.match(line):
                    if KEEP.match(line):
                        if current:
                            current = (current[0], current[1], current[2] + 1)
                    elif depth == 0:
                        if current:
                            sections.append(current)
                        current = (no, line.strip(), 0) if TIMED.match(line) else None
            if current:
                sections.append(current)
            for no, head, keeps in sections:
                if keeps != 1:
                    errors.append(f"{rel}:{no}: timed section has {keeps} 'Keep this' callouts, expected exactly 1: {head[:70]}")

        for no, line in prose_lines(path):
            for pattern, canonical in VOCAB:
                if pattern.search(line):
                    warnings.append(f"{rel}:{no}: vocabulary drift, the course says {canonical!r}: {line.strip()[:100]}")
        if rel != "reference/glossary.qmd" and len(re.findall(r"hallucinat", text, re.I)) > 2:
            warnings.append(f"{rel}: 'hallucination' appears more than twice; the course says 'made-up' or 'fabricated' and names the word once")

        if rel != "reference/case-cards.qmd" and rel != "reference/practice-source.qmd":
            for no, line in prose_lines(path):
                if PERCENT.search(line) and not re.search(r"SpO2|HbA1c", line) and not line.lstrip().startswith(":::"):
                    warnings.append(f"{rel}:{no}: percentage in prose (case fact or invented claim?): {line.strip()[:100]}")
                if "!" in line and not line.lstrip().startswith(("<!--", "#", ":::", "|")) and "![" not in line:
                    warnings.append(f"{rel}:{no}: exclamation mark: {line.strip()[:100]}")

    if warnings:
        print(f"{len(warnings)} warning(s) for a human to judge:")
        for w in warnings[:60]:
            print(f"  {w}")
        if len(warnings) > 60:
            print(f"  ... and {len(warnings) - 60} more")
    if errors:
        print("\nCONTENT LINT ERRORS:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    print(f"content lint: {len(pages)} pages, no errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
