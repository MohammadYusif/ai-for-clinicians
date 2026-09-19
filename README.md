# AI for Clinicians

**Physician AI Literacy** · three days, two hours a day

Course site: **<https://mohammadyusif.github.io/ai-for-clinicians/>**

A practical, hands-on course for doctors on using AI tools well in daily practice, documentation, and teaching. Most participants already have a chatbot open between patients; the course makes that deliberate instead of accidental. The site holds the teaching, the prompts, the labs, and the reference cards.

> **AI drafts. You decide.**

Every patient in this repository is fictional. This is educational material, not medical or legal advice.

## The three days

| Day | Modules | Lab |
|---|---|---|
| **One** — Foundations | 1 The rule and how these tools work · 2 Anatomy of a good prompt · 3 Choosing the right tool | Lab 1: templates, limits, and a tool face-off (30 min) |
| **Two** — Applications | 4 Notes and audiences (with the Saudi scribes) · 5 Talks and teaching | Lab 2: one case, three outputs (35 min) |
| **Three** — Safety & Ethics | 6 Confidently wrong · 7 Patient privacy · 8 Back to the rule | Lab 3: spot the error (25 min) |

Each day is exactly 120 minutes including a 10-minute break. `course/timing.json` is the single source of every minute.

## What is in here

| Path | What |
|---|---|
| `index.qmd`, `setup.qmd`, `assessment.qmd` | the course site's root pages (Quarto → GitHub Pages) |
| `day1/`, `day2/`, `day3/` | the modules and labs, in run-of-show order |
| `reference/` | case cards, practice source, prompt library, three-question check, privacy checklist, glossary, troubleshooting |
| `course/` | trainer-facing and deliberately **not** published to the site: instructor guide, per-day talking points and slide text, accreditation notes, the source brief, `timing.json` |
| `tools/` | the checks below |
| `.github/workflows/publish.yml` | checks, render, link audit, deploy |

## Working on this repository

```bash
quarto preview                          # the site, at http://localhost:4731

python tools/check_timing.py            # every day sums to 120, every badge matches
python tools/build_prompt_library.py    # rebuild reference/prompt-library.qmd (generated)
python tools/check_placeholders.py      # no unfinished markers left in published pages
python tools/lint_content.py            # canonical wording present, banned claims absent
quarto render && python tools/check_links.py   # every internal link and #fragment in _site/
```

`tools/contrast_audit.js` is a browser-console tool that measures text contrast on the rendered pages in light and dark mode. Python is standard library only; there is nothing to install beyond [Quarto](https://quarto.org) (the workflow pins 1.10.18).

## Publishing

The workflow runs every check and renders the site on each push, then deploys it to GitHub Pages. Pages is set
to the **GitHub Actions** source (Settings → Pages), and the deploy steps run only while the repository is
public. A change to a page, the theme, `tools/` or `course/timing.json` deploys on push; anything else can be
deployed by running the workflow by hand.

## The four rules

1. **The clock adds up.** A duration changes in `course/timing.json` and on its page in the same commit; CI fails otherwise.
2. **No real patient, ever.** Every case is a synthetic card in `reference/case-cards.qmd`.
3. **Nothing is claimed about AI that the site cannot back.** Facts about products and law come from the source brief or a vendor's own dated public page; example outputs are labeled illustrative.
4. **The course relies on no tool but one general assistant.** A product is only an example of a type, and every activity has a fallback that needs nothing more.

`CLAUDE.md` has the detail, and `course/authoring-guide.md` has the voice, markup, and vocabulary for anyone writing a page.
