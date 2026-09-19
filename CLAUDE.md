# ai-for-clinicians — working rules

A three-day, two-hours-a-day course for doctors (Physician AI Literacy), published as a
[Quarto](https://quarto.org) site to GitHub Pages and built the same way as the
`llm-application-engineering` and `time-series-forecasting-ai-systems` sibling sites:
theory pages plus hands-on labs, rendered straight into the site, nothing executed at build
time. Read this before adding a page, changing a minute, or touching `_quarto.yml`.
The house style for prose, markup and vocabulary is `course/authoring-guide.md`.

## The four rules everything else serves

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
room measures for itself in a lab (time, word count, edit count) is theirs, not a claim of the
site's. Do not soften the labels and do not add a number without a source.

**4. The course relies on no tool but one general assistant.** No lab, demo or setup step may require a
particular product, a verification step, or anyone's approval. A product appears only as an example of a
type, and every activity has a fallback that needs nothing more: Module 3's "second option" (a
literature-grounded tool, the assistant's own search mode, or a plain literature search) is the pattern.
Vera Health once was a requirement; a trainer who is not a clinician cannot register for it, and its public
terms do not say how credentials are checked. `tools/lint_content.py` blocks the phrasings that made it one.

## Layout

| Path | What |
|---|---|
| `index.qmd`, `setup.qmd`, `assessment.qmd` | site root pages |
| `day1/`, `day2/`, `day3/` | the modules (`mN-*.qmd`) and labs (`labN-*.qmd`), in run-of-show order |
| `reference/` | case cards, practice source, prompt library (generated), tool guide, glossary, privacy guide, troubleshooting |
| `course/` | trainer-facing: instructor guide, per-day talking points and slide text, accreditation notes, the source brief, `timing.json`. **Not rendered to the site, but the repository is public** — nothing in it may be a secret |
| `tools/` | `check_timing.py`, `build_prompt_library.py`, `check_placeholders.py`, `lint_content.py`, `check_links.py`, and `contrast_audit.js` (a browser-console contrast audit) |
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
python tools/build_prompt_library.py --check
python tools/check_placeholders.py
python tools/lint_content.py
quarto render
python tools/check_links.py        # every internal link and #fragment in _site/
```

then look at the rendered page in **both** light and dark mode and at phone width — the labs
are used on phones in the room. Mermaid diagrams must have become `<svg>`, not raw text.
Run `tools/contrast_audit.js` in the browser too: contrast worked out on paper is not the
contrast that renders (the first audit of this site found Bootstrap's grey on the dark breadcrumb
bar at 2.85:1, and a blockquote at 3.7:1, in a palette that passed on paper).

## Site gotchas (inherited from the sibling sites — binding here)

- **Never write a linked image as its own paragraph** (`[![x](y)](z)`): Quarto's implicit-figures
  pass silently drops the `<a>`. Use raw HTML. (This site has almost no images; keep it that way.)
- **Don't add `revealjs` as a project-level format.** It makes Quarto render every page twice and
  the render dies. If a page ever needs slides, render that one file with `--to revealjs`.
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
