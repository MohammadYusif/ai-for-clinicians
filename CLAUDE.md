# ai-for-clinicians — working rules

A three-day, two-hours-a-day course for doctors (Physician AI Literacy), published as a
[Quarto](https://quarto.org) site to GitHub Pages and built the same way as the
`llm-application-engineering` and `time-series-forecasting-ai-systems` sibling sites:
theory pages plus hands-on labs, rendered straight into the site, nothing executed at build
time. Read this before adding a page, changing a minute, or touching `_quarto.yml`.
The house style for prose, markup and vocabulary is `course/authoring-guide.md`.

## The five rules everything else serves

**1. The clock adds up.** Each day is exactly 120 minutes including its 10-minute break.
`course/timing.json` is the single source of every minute; each timed section on the site
carries a `[N min]{.time}` badge that must match it. `python tools/check_timing.py` fails
otherwise, and CI runs it. The source brief (`course/BRIEF.md`) claimed 120 for Day One while
its own table summed to 130 (140 with its Lab One spec) — that is the mistake this rule exists
to stop. Change a duration in `timing.json` and on its page in the same commit.

**2. No real patient, ever.** Every case is a synthetic card in `reference/case-cards.qmd`.
No name, ID, file number, phone, date of birth, photograph, screenshot from an EMR, or
"anonymized" real vignette goes into this repository, including the vignettes on the privacy
page and any example prompt. The course teaches that identifiable patient data does not go
into a consumer AI tool; the repository is held to the same rule. Doses and values on the
cards are fictional and are the *only* clinical numbers an example may use.

**3. Nothing is claimed about AI that the site cannot back.** No performance figure,
percentage, time-saving estimate, "studies show", guideline number, DOI or URL from memory.
A fact about a named product or a law comes from the "Research already gathered" section of
`course/BRIEF.md`, is worded no more strongly than that source, and carries an as-of date
where availability could change. Example AI outputs are *illustrative*: written by the course
author, labeled as such in a callout, never presented as a measurement of any tool. What the
room sees for itself in a lab (ticks against a card, sources it could open) is theirs, not a claim of the
site's. Do not soften the labels and do not add a number without a source.

**4. The course relies on no tool but one general assistant.** No lab, demo or setup step may require a
particular product, a verification step, or anyone's approval. A product appears only as an example of a
type, and every activity has a fallback that needs nothing more: Module 3's "second option" (a
literature-grounded tool, the assistant's own search mode, or a plain literature search) is the pattern.
Vera Health once was a requirement; a trainer who is not a clinician cannot register for it, and its public
terms do not say how credentials are checked. `tools/lint_content.py` blocks the phrasings that made it one.

**5. The course is delivered online, and nothing assumes a shared room.** Everyone is on a video call with their
own device and their own assistant. No page, deck or note may tell anyone to turn to a neighbor, raise a hand, look
at a board or a projector, write on paper, or hand something over. Every activity is one of five moves (Chat,
Speak, Share, Pair, Solo; `course/authoring-guide.md`, section 9), chat first. A Pair step (a breakout room of two) is
used only where a second person catching what you missed is the point, and carries a no-breakout fallback in its
notes. Say "the group", not "the room". `tools/lint_content.py` blocks the wording that gives a page away, in the
pages, the decks and the trainer's notes.

**The call is three tabs.** The course runs on Google Meet. A participant has the call, the slides (the trainer pastes the
link; each prompt, case and source has a Copy prompt button on its slide, and goes into the chat too for anyone without the
deck) and one assistant, and nothing else. The group does each step with the trainer, who runs it on the shared screen too. So a deck never links to another page and never tells
anyone to open one (the lint blocks it), a block to paste is pulled into its slide from the handout by
`tools/build_prompt_library.py` (`slides/_paste-*.md`, generated, never hand-edited), and a handout is for afterwards.

## Layout

| Path | What |
|---|---|
| `index.qmd`, `setup.qmd`, `assessment.qmd` | site root pages; `index.qmd` is the course map, one card per module and lab |
| `day1/`, `day2/`, `day3/` | the **handouts**: the modules (`mN-*.qmd`) and labs (`labN-*.qmd`), in run-of-show order, with the prompts |
| `slides/` | the **decks**: one reveal.js deck per module and lab, same file name and anchors as its handout, speaker notes under every slide; `_metadata.yml`, `theme.scss`, `section.lua`, and the generated `_glance-dayN.md` / `_plan-*.md` tables and `_paste-*.md` blocks (every prompt, lab paste block, case card and the practice source, written by `build_prompt_library.py`; a slide includes them, never retypes them) |
| `reference/` | case cards, practice source, prompt library (generated), tool guide, glossary, privacy guide, troubleshooting |
| `course/` | trainer-facing: the instructor guide, the Lab 3 examples, accreditation notes, the authoring guide, the source brief, `timing.json`. The script is the speaker notes in the decks. **Not rendered to the site, but the repository is public** — nothing in it may be a secret |
| `tools/` | `check_timing.py`, `check_decks.py`, `build_prompt_library.py`, `check_placeholders.py`, `lint_content.py`, `check_links.py`, and two browser-console audits, `contrast_audit.js` (pages) and `deck_audit.js` (decks) |
| `.github/workflows/publish.yml` | timing check, prompt-library check, render, link audit, deploy |

## The prompt library is generated

`reference/prompt-library.qmd` is built from the prompts in the day pages. A reusable prompt is
marked in its page with `<!-- prompt: slug | Title | when to use -->` directly above its
```` ```text ```` block. **Never hand-edit the library** — edit the prompt where it is taught, then
run `python tools/build_prompt_library.py`. CI runs it with `--check` and fails on drift, so the
page a reader copies from can never differ from the page that taught it.

## Render, don't just read source

A `.qmd` looking right in the editor proves nothing; pandoc changes structure in ways only the
HTML shows. Before calling a page done:

```
python tools/check_timing.py
python tools/check_decks.py
python tools/build_prompt_library.py --check
python tools/check_placeholders.py
python tools/lint_content.py
quarto render
python tools/check_links.py        # every internal link and #fragment in _site/
```

then look at the rendered page in **both** light and dark mode and at phone width — the labs
are used on laptops and phones during the call. Mermaid diagrams must have become `<svg>`, not raw text.
Run `tools/contrast_audit.js` in the browser too: contrast worked out by hand is not the
contrast that renders (the first audit of this site found Bootstrap's grey on the dark breadcrumb
bar at 2.85:1, and a blockquote at 3.7:1, in a palette that passed on paper). A deck is audited the
same way with `tools/deck_audit.js` (overflow, nested slides, contrast, missing notes), and looked at
in the browser at 1280 x 720. The browser caches a deck page hard: add `?v=2` to the address after a re-render.

## Site gotchas (inherited from the sibling sites — binding here)

- **Never write a linked image as its own paragraph** (`[![x](y)](z)`): Quarto's implicit-figures
  pass silently drops the `<a>`. Use raw HTML. (This site has almost no images; keep it that way.)
- **Don't add `revealjs` as a project-level format.** It makes Quarto render every page twice and
  the render dies. A deck says `format: revealjs` in its own front matter (the shared options are in
  `slides/_metadata.yml`), and only that page renders as slides: this is how the decks in `slides/` work.
- **A heading inside a `:::` div becomes a nested slide.** pandoc turns it into a `<section>` and
  reveal.js makes the whole slide a vertical stack. In a deck use a `[Title]{.t}` paragraph in a card.
  `tools/check_decks.py` catches it in the source; `deck_audit.js` catches it in the render.
- **`::: notes` before a deck's first heading becomes an empty slide.** Notes go under a heading.
- **Quarto bakes the slide menu icons into a data-URI**, so `color` does not recolour them; the theme
  uses a `filter` on dark slides (`slides/theme.scss`).
- **`execute: enabled: false` project-wide is deliberate.** Nothing on this site runs; every
  block is read or copied by a participant.
- **A page not listed in the sidebar `contents:` will not show in navigation** even if it
  renders. Keep `_quarto.yml` in step with `day1/`–`day3/` and `reference/`.
- **Prompts are ```` ```text ```` fences, and Quarto gives those no copy button** (its own button only
  attaches to recognised code languages; a bare fence gets none either). `assets/copy-prompts.html`,
  included after every page body, adds a "Copy prompt" button to each `pre.text`, with a select-all fallback
  when the clipboard API is blocked. Keep prompts on the `text` fence, and re-check the button after any
  change to how code blocks are styled.
- **Quarto sets inline `code` to `white-space: pre`, which no wrap value can break.** A long file name
  in backticks (Module 7) overflowed a 360px phone screen. `_components.scss` sets `pre-wrap` and
  `overflow-wrap: anywhere` on inline code; keep both if you touch that rule.
- **Mermaid draws with its light theme even in dark mode**: nodes keep their own light fills, so give every
  node an explicit fill and a dark text colour. `theme-dark.scss` brightens only the arrow lines.
- **A `.qmd` link stays `.qmd` in the HTML when its target does not exist**, so a missing or misnamed page
  shows up as a broken link in `check_links.py`, not as a render error.
- **A `#` after a space in a YAML plain value starts a comment** (a workflow step name lost its tail this way).
  Quote any step name that contains one.
- **Scripted YAML edits can strand orphaned keys** under a deleted parent. Re-read the whole block.
- **The theme compiles twice** (`theme-light.scss`, `theme-dark.scss`), both importing
  `_components.scss`. A colour that reads on one ground may not on the other — check contrast in both.
- Wide tables scroll inside themselves (the theme does this globally); the page body never scrolls sideways.

## Public repository: what must never be committed

- a real patient's data in any form, or a screenshot that contains any;
- the **Lab 3 examples' source cards and the answer keys on the site** (`course/lab3-examples.md` holds them for the
  trainer; they are never in a page, a deck or a deck's notes, and the instructor shares them from a private deck);
- the **scored assessment quiz and its answer key** (the practice bank on `assessment.qmd` is
  deliberately not the scored quiz; if the scored one is built as a form, its answer-position
  and answer-length balancing rules from the trainer's workspace apply, and it stays out of this repo);
- participant names, rosters, feedback, certificates;
- an API key, an account password, or a private invitation link.

## Windows

The trainer's machine is Windows. Python is `python` (not `python3`). Arabic appears in the
patient-handout examples, so scripts read and write UTF-8 explicitly. Quarto is on `PATH` as
`quarto`; the publish workflow pins the same version the sibling sites use (see the workflow).

## What is verified and what is not

The clock, the prompt library, the placeholders, the canonical wording, the banned claims, the
pasted case card and every internal link are machine-checked. The clinical *content* of the case
cards and the wording of the safety rules are authored: a clinician should read the cards before
the course runs. There is no Arabic text in the repository (the Arabic handout variant asks a tool
to write it), so if Arabic is ever added, a fluent reader must check it.
