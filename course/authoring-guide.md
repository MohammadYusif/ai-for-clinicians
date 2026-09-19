# Authoring guide

The contract for anyone writing or editing a page in this repository: fixed vocabulary, markup,
voice, and the limits on what a page may claim. Read `CLAUDE.md` (the three rules) and
`course/BRIEF.md` (the source of truth) first. Every page is written for **doctors who are not
technical**, of any specialty, in a room that asks questions.

## 1. The fixed vocabulary — use these exact words

These recur across all three days. A reader who meets a differently-worded version will assume it
is a different tool. Reuse, don't paraphrase.

**The rule.** "AI drafts. You decide."

**The three-question check.** Exact wording, in this order:

1. Could I defend this to a colleague?
2. Does it point to something I can verify?
3. Would I catch it if it were wrong?

Followed by: "If the answer to any of these is no, that's the signal to slow down, not the finding to accept."
Full card: `reference/three-question-check.qmd`.

**The verification workflow.** Draft with AI → Cross-check the source → Confirm or correct → Use.

**The four-part framework** (spelled out and hyphenated in prose; the brief's "4-part" is the same
thing). *Role · Context · Format · Constraints*. One line each:

- **Role** — who the AI is writing as, and for whom.
- **Context** — the facts it may use, and what the output is for. Only the facts you give it.
- **Format** — the exact shape: template, headings, length.
- **Constraints** — what it must not do: no invented facts, no hedging, the units, the reading level.

Memory line: *"Who it is, what it knows, what shape to return, what to avoid."*

The canonical skeleton (reproduce exactly when the framework is first taught; reuse as the base
for every later prompt):

```text
ROLE: You are [role], writing for [audience].
CONTEXT: [What this is for.] Use ONLY the facts below. If something needed is missing, write [MISSING: what] instead of guessing.
FACTS:
[paste the facts]
FORMAT: [Exact template or headings.] Maximum [N] words.
CONSTRAINTS: Do not add findings, doses, or diagnoses that are not in the facts. No hedging phrases. [Units, reading level, abbreviations.]
```

**The privacy line.** "No patient identifiers into a consumer AI tool. Ever. Full stop."

**How AI-drafted clinical text goes wrong** — three words, used everywhere: **invented** (something
added that is not in the source), **omitted** (something dropped that was), **altered** (a value,
negation, side, date, or unit changed). "Invented, omitted, altered."

**Terms.** *Consumer AI tool*: a general assistant you sign up for yourself (ChatGPT, Claude,
Gemini on a personal account). *Approved tool*: one your institution has vetted and contracted.
*General assistant* vs *literature-grounded tool* (Vera Health and similar) vs *ambient scribe*
(Sahl AI, Augnito). *Synthetic case*: fictional. *Case card*: an entry in `reference/case-cards.qmd`.
Say "made-up" or "fabricated" for false content the tool produced, and mention "hallucination" once,
as the word they will hear elsewhere.

## 2. Which case goes where

Clinical facts come **only** from the case cards (`reference/case-cards.qmd`, anchors `#case-a` …
`#case-e`) and the fictional protocol (`reference/practice-source.qmd`). Do not invent extra clinical
details. If an example truly needs a fact that is not on a card, leave a `[placeholder]` and say so in
your report so the card can be extended in one place.

| Where | Card |
|---|---|
| Module 1, "how these tools work" room exercise | none — a plain-language sentence-completion exercise |
| Module 2 §7 "Structure fixes it" (SOAP note) | **A** |
| Module 2 §8 "Three more jobs": referral letter / discharge summary / patient handout | **C** / **B** / **D** |
| Lab 1 template test | **A** |
| Module 4 §4 "Same note, three audiences" | **E** |
| Module 5 slides / quiz examples | **A** (slides), the practice source (quiz) |
| Lab 2 "one case, three outputs" | default **A**; any card allowed |
| Module 6–8 examples | any; prefer a card not already used on that day |

Day One §8 and Day Two §4 must not feel like the same demo. **Day One §8** shows the *framework*
traveling across three *different* document types and three *different* cases. **Day Two §4** takes
*one* event and changes only the *audience*, and adds the skill Day One never taught: checking that
the three outputs agree with each other (a "source of truth" fact sheet first, then three prompts
that all draw on it).

## 3. Page anatomy and markup

Every module and lab page:

```markdown
---
title: "Module 2 — Anatomy of a good prompt"
subtitle: "Day One · 35 min"
---

Two or three sentences: why this matters to a doctor, in plain words.

::: {.session-meta}
Time
:   35 minutes, four topics

Uses
:   [Case A](../reference/case-cards.qmd#case-a), [Case C](../reference/case-cards.qmd#case-c)

You leave with
:   One sentence per thing they can do afterward.
:::
```

**Timed sections** are `##` headings, one per row in `course/timing.json`, with the badge and the
exact anchor from that file, in this order:

```markdown
## 3. How these tools actually work [10 min]{.time} {#how-it-works}
```

The number (`3.`) restarts on each page. The anchor and minutes must match `timing.json`; run
`python tools/check_timing.py --allow-missing` to check your pages. Use `###` for anything inside a
timed section. **Never** put a `[N min]{.time}` badge anywhere except a timed heading.

**Each timed section** has, in this order: (1) one or two sentences framing why a doctor cares;
(2) the teaching, in short paragraphs, tables, and lists; (3) a worked example from a case card, with
the full prompt; (4) where useful, a two-minute room activity; (5) exactly one closing line in a
tip callout titled "Keep this".

**Callouts** (always `appearance="simple"`):

| Callout | Use |
|---|---|
| `callout-tip` | "Keep this" — the one-line takeaway closing each timed section |
| `callout-warning` | "Watch for" — a specific pitfall |
| `callout-important` | a non-negotiable safety rule (the privacy line, verify every number) |
| `callout-note` | an aside, a room activity ("Try it"), or an illustrative output |

```markdown
::: {.callout-tip appearance="simple"}
## Keep this
AI drafts. You decide.
:::
```

**Prompts** are fenced ```` ```text ````, with placeholders in `[square brackets]` and the four
labels in capitals. A prompt a doctor would reuse after the course gets a library marker directly
above it, and only those:

````markdown
<!-- prompt: soap-note | SOAP progress note | Turn jotted visit facts into a progress note in a fixed template -->
```text
ROLE: ...
```
````

The slug is lowercase-kebab and unique across the repository. The marker is metadata only (HTML
comments are dropped from the page). `python tools/build_prompt_library.py` collects them.

**Illustrative outputs** — an example of what a tool "might" return — are always labeled, never
shown as a measurement, and never claim to come from a named product:

```markdown
::: {.callout-note appearance="simple"}
## Illustrative output — written for this course, not captured from a real tool
> ...
:::
```

**Other markup.** Tables are pipe tables, at most five short columns. Checklists are `- [ ]` task
lists. Diagrams are Mermaid (```` ```{mermaid} ````), at most eight nodes, styled with the palette
(indigo `#4F46E5`, teal `#14B8A6`, fills `#EEF2FF` / `#CCFBF1`). Links between pages are relative
`.qmd` paths (`../reference/case-cards.qmd#case-b`). No images. Arabic goes in
`::: {lang="ar"}` blocks (the theme sets right-to-left), always with a line telling the reader that
a fluent reader must check it. Prefer commas and colons; keep em dashes rare.

## 4. What a page may claim

- **No invented numbers.** No accuracy figures, percentages, time-saving estimates, adoption
  statistics, or "studies show". The only quantitative facts about tools are those in the "Research
  already gathered" section of `course/BRIEF.md` (Sahl AI's 42.2/45 and 4.35/5, etc.). Numbers in
  examples come from the case cards.
- **No invented sources.** No citations, guideline titles or numbers, DOIs, or URLs. Do not add
  external links; if a page truly needs one, write `[LINK NEEDED: what]` and report it.
- **Product facts** only as the brief states them, worded no more strongly than it, with "as of
  September 2026" where availability could change. Name only: ChatGPT, Claude, Gemini (general
  assistants), Vera Health and OpenEvidence (literature-grounded), Sahl AI and Augnito (scribes).
- **Claim discipline on the scribes.** The Sahl AI pilot reported clinician-rated documentation
  quality on a modified PDQI-9 (42.2 of 45; 4.35 of 5 for accuracy). It did not compare against
  generic prompting, and it did not measure patient outcomes. Never write that purpose-built tools
  "beat" or "outperform" generic prompting. Do say that even the strongest reported accuracy score was
  short of the maximum, which is why the note is still read line by line.
- **Law.** Only what the brief gives: the PDPL is enforced by SDAIA, classifies health data as
  sensitive personal data alongside genetic and biometric data, and carries real financial and
  operational penalties. No article numbers, no fine amounts, no legal conclusions. Anything more is
  "ask your institution's data protection officer or legal team". This is education, not legal advice.
- **Medicine.** Nothing here is clinical guidance. An example never asks an AI to choose a dose or a
  diagnosis; doses in prompts are copied from a case card, and the lesson is that the doctor supplies
  the numbers and the tool never changes them.
- **Deliberately unreliable outputs.** Anything the course asks a tool to get wrong (Lab 1 part 2, Lab 3)
  is labeled at the top of what participants save: `PRACTICE OUTPUT: CONTAINS DELIBERATELY UNRELIABLE
  CONTENT. NOT FOR CLINICAL USE.` The trainer's backup examples use *generic* errors (a wrong
  citation year, a mismatched document number), never a specific fabricated clinical fact.
- **Real patients.** None. Vignettes are invented and say so.

## 5. Voice

Second person, plain, colleague to colleague. Short paragraphs (four lines at most). Concrete over
abstract: name the tool behavior, then the clinical consequence. American spelling. No hype
("revolutionary", "game-changing", "unlock", "leverage"), no exclamation marks, no emoji, no
scolding. Respect the reader's expertise: they know medicine; this course is about a tool. Define a
technical word once, in plain terms, the first time it appears on a page. Every paragraph should
give a clinician something they can do on Monday.

## 6. Instructor material (`course/dayN-talking-points.md`)

One block per timed topic, in run-of-show order, headed
`## Topic N — Title (X min)` with a line linking the participant page and stating the deck status
(`new`, or `kept` with the existing slide id). The existing deck's slide ids are: `cover`, `why`,
`outcomes`, `agenda`, `day1-divider`, `rule`, `gutcheck`, `extra-words`, `structure-fix`,
`tool-types`, `geography`, `quota`, `lab1`, `day2-divider`, `four-places`, `notes-right`,
`saudi-scribes`, `case-to-deck`, `teaching-ai`, `lab2`, `day3-divider`, `confidently-wrong`,
`privacy-rule`, `back-to-rule`, `assessment`, `closing`. Blocks contain:

- **Goal** — one sentence: what the room can do or say afterward.
- **Slides** — each with an id (existing, or a proposed new one), a headline, the on-slide text
  (three items at most), a visual note in the deck's style (card row, before/after, big number,
  flow, table; DM Sans; indigo/teal on `#0F172A` / `#FBFBFD`), and `Notes:` — plain text of at most
  900 characters that can be pasted straight into the deck's speaker notes.
- **Say** — the talking points in order, with clock cues ("0:00–2:00"), as a script an instructor
  can glance at, not a transcript.
- **Do** — any live demo or room activity, as numbered steps, including what to have open beforehand.
- **If asked** — three to five questions a room of doctors actually asks, each with a short answer.
- **Watch for** — misconceptions and the moment that goes wrong.
- **Bridge** — the sentence into the next topic.

Labs end the day's file with a **Lab N — facilitation** section: before class, materials,
minute-by-minute, what good looks like, common problems and fixes, debrief prompts, and (Lab 3)
the prepared backup examples with their answers.

## 7. Size

A page is as long as its minutes justify and no longer: about 100 to 130 words of participant text per
minute of class time, plus the prompts and tables. A lab page is 1,300 to 2,000 words. Talking points
run 250 to 450 words per topic plus slide specs. Padding is worse than brevity.

## 8. Before you say you are done

- `python tools/check_timing.py --allow-missing` passes for your pages (anchors and badges).
- Every prompt worth reusing has its `<!-- prompt: ... -->` marker; no marker precedes anything else.
- Every clinical fact traces to a case card or the practice source; no invented number, source, or link.
- Every example output is in an "Illustrative output" callout.
- The exact wording of the rule, the three questions, the four parts, and the privacy line matches section 1.
- You edited only the files you were assigned.
