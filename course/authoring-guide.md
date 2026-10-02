# Authoring guide

The contract for anyone writing or editing a page or a deck in this repository: fixed vocabulary, markup,
voice, and the limits on what a page may claim. Read `CLAUDE.md` (the five rules) and
`course/BRIEF.md` (the source of truth) first. Every page is written for **doctors who are not
technical**, of any specialty, on a call where people type their questions. The course is online
first: section 9 says what that rules out.

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
| Module 1, "how these tools work" chat exercise | none — a plain-language sentence-completion exercise |
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

Every module and lab page (the handout; the deck is in section 10):

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
the full prompt; (4) where useful, a two-minute activity on the call, written with one of the
moves in section 9; (5) exactly one closing line in a tip callout titled "Keep this".

**Callouts** (always `appearance="simple"`):

| Callout | Use |
|---|---|
| `callout-tip` | "Keep this" — the one-line takeaway closing each timed section |
| `callout-warning` | "Watch for" — a specific pitfall |
| `callout-important` | a non-negotiable safety rule (the privacy line, verify every number) |
| `callout-note` | an aside, an activity ("Try it"), or an illustrative output |

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
comments are dropped from the page). `python tools/build_prompt_library.py` collects them. Markers live
in the handout pages only: a deck shows a prompt without one, and links to the library for the rest.

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
  external links; if a page truly needs one, write `[LINK NEEDED: what]` and report it. A link someone has
  opened and vouched for goes into `ALLOWED_URLS` in `tools/lint_content.py`, with a comment saying when and how.
- **Product facts** only as the brief states them, or as a vendor's own public page states them (dated, and
  linked as above), worded no more strongly than the source, with "as of September 2026" where availability
  could change. Name only: ChatGPT, Claude, Gemini (general assistants), Vera Health and OpenEvidence
  (literature-grounded), Sahl AI and Augnito (scribes).
- **No dependency.** No lab, demo or setup step may require a particular product, an account that needs
  verification, or anyone's approval. The only requirement is one general assistant of the participant's
  choice. A product appears as an example of a type, and every activity has a fallback that needs nothing
  more (the "second option" in Module 3 is the pattern). `tools/lint_content.py` blocks the phrasings that
  once made Vera Health a requirement.
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
give a clinician something they can do on Monday. Titles and subtitles say what the reader needs and
no more: no stock third item ("· English"), no tagline, nothing that reads as generated.

## 6. Speaker notes and the trainer's guide

The decks carry the script. There is no separate talking-points file: open a deck, press `S` for the
speaker view, and the notes under each slide are what to say and do. `course/instructor-guide.md` holds what
does not belong on a slide: the run-of-show, the online moves and their fallbacks, what to have open before each
day, risks, and the decisions still open.

## 7. Size

A handout page is as long as its minutes justify and no longer: about 100 to 130 words of participant text per
minute of class time, plus the prompts and tables. A lab page is 1,300 to 2,000 words. A deck has two to
six working slides per topic; a slide holds one idea and no more than about forty words. Padding is worse than brevity.

## 8. Before you say you are done

- `python tools/check_timing.py --allow-missing` passes for your pages and decks (anchors and badges).
- Every prompt worth reusing has its `<!-- prompt: ... -->` marker in the handout; no marker precedes anything else.
- Every clinical fact traces to a case card or the practice source; no invented number, source, or link.
- Every example output is labeled illustrative.
- The exact wording of the rule, the three questions, the four parts, and the privacy line matches section 1.
- `python tools/lint_content.py` and `python tools/check_decks.py` pass, and nothing assumes a shared room.
- You edited only the files you were assigned.

## 9. Online first

The course runs on a video call. Everyone is on their own device with their own assistant; nobody sits next to
anybody. Write every activity so that it works there. Each interactive moment is one of five moves, and a slide
announces it the same way every time, with a label and a time (for example "Chat · 1 min").

| Move | What happens | Use it for |
|---|---|---|
| **Chat** | Everyone types an answer at once; the trainer reads a few out | A vote (type 1, 2 or 3), a one-sentence answer, the next word |
| **Speak** | Two or three people unmute when asked | A short answer, a debrief |
| **Share** | One person shares a screen when asked | An output shown beside its source |
| **Pair** | A breakout room of two, three to six minutes | Checking each other's work, and only that |
| **Solo** | Your own device, your own assistant, quietly | The labs |

How to write for it:

- **Chat first.** If an activity can be done in the chat, it is. A chat answer takes longer to type than to say, so
  give sixty to ninety seconds for one sentence.
- **Pair only where a second person catching what you missed is the point.** That is Lab 3 part 1 and the Day Three pair
  check. Every pair step carries its fallback in the speaker notes: the same step done in the chat, or alone.
- **Nothing physical.** No worksheet to collect, no wall to write on, nothing to hand over. Say "your notes", "the
  chalkboard (press B in a deck)", "share your screen".
- **Say the group.** Write "everyone", "the group" or "the call", and "have ready" in place of "bring".
- **No platform feature beyond chat and screen sharing**, except breakout rooms for the pair steps. A tool the
  platform may not have is a dependency (rule 4).

Words that give a page away are blocked by `tools/lint_content.py` in pages, decks and the trainer's notes. Written
here as an example of what not to put in front of participants, inside a fence so the lint skips it:

```text
"Tell your neighbor." "Turn to the person next to you." "Show of hands." "Hands up." "In pairs."
"Walk the room." "The whiteboard." "On paper." "Print this page." "Project the page." "In the room."
```

## 10. Decks (`slides/`)

Each module and lab has a deck, built with reveal.js through Quarto, in the same look as the SDAIA course decks: a white
ground, left-aligned text, a hairline under each title, dark topic slides, a teal progress bar. A deck has the
same file name and the same anchors as its handout (`day1/m2-prompting.qmd` and `slides/m2-prompting.qmd`).
The shared options and theme are `slides/_metadata.yml` and `slides/theme.scss`; a deck's own front matter is its
title, subtitle and `format: revealjs`. **revealjs is never a project-level format** (CLAUDE.md).

**Order.** The title slide (from the front matter); `## In this module {#plan}` holding
`{{< include _plan-<deck>.md >}}`, a table generated from `timing.json`; then one topic slide per timed section,
`# Title [N min]{.time} {#anchor}` with the minutes and anchor from `timing.json`, each followed by two to six working
slides `## Title {#id}`. Slide ids are lowercase kebab, unique in the deck, and are the slide's URL (`#/id`).

**Speaker notes** are `::: notes` at the end of the slide, plain markdown, at most 900 characters (1,600 on a topic
slide). A working slide's notes open with its time budget (`**1:30.**`, minutes and seconds, adding up to the topic's
minutes), then **Say** in the voice of the trainer, then **Do** in terms of the five moves. A topic slide's notes are the
topic's brief: **Goal.** **Have ready.** **Watch for.** **If asked.** **Bridge.** Never put a lab answer key in a
note; never put `[TRAINER TO CONFIRM]` in one (an open decision goes in `instructor-guide.md`).

**Components** (CSS in `theme.scss`; use only these):

````markdown
::: {.cards}
::: {.card}
[Short title]{.t}

One or two lines. `.card .teal` for the teal edge, `.dashed` for "not this", `.tint` for emphasis, `.dark` for a dark card.
:::
:::

[01]{.num}              <!-- a big numeral at the top of a card -->

::: {.flow}
::: {.step}
[1]{.num} Draft with AI
:::
::: {.step}
[2]{.num} Cross-check the source
:::
:::

::: {.columns}
::: {.column width="50%"}
left
:::
::: {.column width="50%"}
right
:::
:::

::: {.move .chat}
[Chat · 1 min]{.tag} Type your answer.
:::
````

A move strip is `.move` plus one of `.chat`, `.speak`, `.share`, `.pair`, `.solo`; the label is the first span. Other
helpers: `[text]{.illustrative}` (the label every invented output carries), `[text]{.pill}`, `[text]{.huge}`,
`[text]{.big}`, `.muted`, `.small`, and `.vc` to push a short slide's content toward the middle. Tables,
blockquotes, callouts and ```` ```text ```` prompt blocks (they get a "Copy prompt" button) are styled already.
Reveals are `::: {.fragment}`.

**Never** write a `##` or `###` heading inside a `:::` div (pandoc turns it into a nested slide; use a `[Title]{.t}`
paragraph), put a `::: notes` block before the first heading (it becomes an empty slide), or add an image. A slide's
text is what a doctor needs to see, not the script: the script is in the notes.

**Check a deck** without rendering: `python tools/check_decks.py slides/<deck>.qmd` and
`python tools/lint_content.py slides/<deck>.qmd`. Render with `quarto render slides/<deck>.qmd`, then run
`tools/deck_audit.js` in the browser on the result: it reports overflow, nested slides, low contrast and missing notes.
