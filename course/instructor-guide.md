# Instructor guide

Trainer-facing. Not published to the site. The repository is public, so nothing here is secret: no
roster, no participant names, no answer key for the scored quiz.

Per-day talking points, slide text and lab facilitation notes are in `day1-talking-points.md`,
`day2-talking-points.md` and `day3-talking-points.md`. Accreditation notes are in `accreditation.md`.
The source brief is `BRIEF.md`.

## The weekend at a glance

Three days, two hours each, English. Each day is **120 minutes including a 10-minute break**:
110 minutes of teaching and lab, 330 in total. The hands-on labs are 30 + 35 + 25 = 90 minutes, a
quarter of the weekend, and most modules carry a two-minute room activity on top.

| Day | Job of the day | Lab |
|---|---|---|
| **One** — Foundations | Get a better draft: why the tools sound sure, the four-part prompt, choosing a tool | Templates, limits, tool face-off |
| **Two** — Applications | Use it on real documents and teaching, and check that outputs agree | One case, three outputs |
| **Three** — Safety & Ethics | Make the check and the privacy line automatic | Spot the error |

Two sentences carry everything: **"AI drafts. You decide."** and **"Tone is not a signal. A
verification step is."** If a discussion drifts, steer it back to one of them.

## What changed from the brief

The site departs from `BRIEF.md` in six places. Each is deliberate; each can be reversed.

### 1. Day One did not add up, so it was re-timed

The brief's Day One table sums to **130 minutes**, not the 120 it states. Its own Lab One spec
(15 + 10 + 5 + 5) is **35 minutes**, not the 25 in its table, so read literally Day One is **140**.
Days Two and Three sum to 120 as briefed and are unchanged.

| Item | Brief | Now | Why this one |
|---|---:|---:|---|
| Course opener | 10 | 5 | The home page and the first slides carry the pitch; the rule follows straight after |
| Structure fixes it (notes) | 10 | 5 | Lab 1 part 1 is now its hands-on, so the demo can be the before-and-after alone |
| Live demo, two tools | 10 | 5 | Pre-load both tools and paste rather than type; the lab's face-off is the room's own run |
| Lab One | 25 in the table, 35 in the spec | 30 (12 + 8 + 5 + 5) | All four parts kept; the two long parts trimmed |

If you would rather cut elsewhere, edit `course/timing.json` and the `[N min]` badge on the page, then run
`python tools/check_timing.py`. It reports every page, badge and total that disagrees. Options that
work: fold the live demo into the start of Lab 1 part 3 and give the face-off ten minutes; or drop
"Structure fixes it" as its own topic and let Lab 1 part 1 carry it.

### 2. Three claims on existing slides need correcting

- **`saudi-scribes`, last line.** It reads "Purpose-built tools already beat generic prompting for this exact
  complaint." The pilot behind the slide reported documentation quality ratings for one scribe; it did not
  compare against generic prompting (the paper describes a single-arm pilot). The site claims only what the
  pilot shows. Suggested replacement: *"Reported accuracy was 4.35 of 5, short of the maximum, so the note is
  still read line by line."*
- **`saudi-scribes`, Augnito card.** It says the scribe is "integrated directly into the hospital's own medical
  records system." The public announcement (a press release dated 31 January 2025, signed at the Arab Health
  Exhibition) uses the future tense: the agreement "will see" the scribe integrated with the EMR/HIS, in a
  phased rollout, and it reports no deployment or accuracy figures. Suggested replacement: *"An Arabic-capable
  ambient scribe, announced in January 2025 for integration with the hospital's own medical records system."*
  The slide title, "Already Live in Saudi Clinics", is fair for a pilot and generous for an announcement; confirm
  each tool's current status before class.
- **`geography`** says OpenEvidence "requires a US medical license". The brief says **US NPI
  verification**, and that it **withdrew from the EU and UK in April 2026**. The site uses the brief's
  wording, dated "as of September 2026". Re-check availability the week you teach: it changes.

### 3. "A real case" became a synthetic case card

The brief's labs say "one real note" and "one real case". The privacy rule arrives on Day Three, after two
days of labs, so real cases would have participants breaking the rule while being taught it. Every lab
uses one of five synthetic cards (`reference/case-cards.qmd`), and the setup page says so. Participants
may bring a case of their own only if it is fully de-identified, and Day Three explains why that is a
judgment, not a guarantee.

### 4. Day One topic 8 and Day Two topic 4 were the same demo

Both used a referral, a discharge document and a patient handout. They now do different jobs. **Day One §8**
shows the *framework* traveling across three different document types on three different cases. **Day Two
§4** takes *one* event and changes only the *audience*, and teaches what Day One did not: write a
source-of-truth fact sheet first, then check that the three outputs agree with each other.

### 5. Things added that the brief did not ask for

- `reference/case-cards.qmd` and `reference/practice-source.qmd` (a fictional one-page protocol, so a
  quiz question has an answer that can be checked in seconds).
- A **prompt library** generated from the prompts in the day pages, so a participant can copy from one place
  and the copy can never differ from the teaching page.
- The `PRACTICE OUTPUT: CONTAINS DELIBERATELY UNRELIABLE CONTENT. NOT FOR CLINICAL USE.` line that
  participants put on the "break it on purpose" output they save in Lab 1 and swap in Lab 3.
- An optional Arabic-output variant for the patient-handout prompt (Case D's mother prefers Arabic), with the
  warning that a fluent reader must check whatever the tool writes.
- A setup page, a glossary, a troubleshooting page, and a self-check bank on `assessment.qmd`.
- Checks that fail CI: the clock, the prompt library, and unfinished placeholders.

### 6. Not done

- **The scored quiz.** The brief marks it "kept" and it is not in the material I was given. The bank on
  `assessment.qmd` is practice, not the quiz. If the scored quiz becomes a form, keep it and its key out of
  this public repository, and apply the answer-position and answer-length balancing rules in your workspace.
- **The deck.** Not edited. Slide text and paste-ready speaker notes are in the talking-points files.
- **A clinician read of the case cards.** The values are internally consistent (the eGFR and the
  CHA2DS2-VASc score were recomputed) but a tool cannot vouch for clinical realism. There is no Arabic text
  anywhere in this repository: the Arabic variant of the patient handout asks the tool to write Arabic and
  tells the reader that a fluent colleague must check it before a family sees it.
- **A licence.** No `LICENSE` file was added; that is your decision.

## Run-of-show

Generated from `course/timing.json`. Do not edit between the markers; change `timing.json` and run
`python tools/check_timing.py --write-guide`.

<!-- runofshow:start -->
### Day 1: Foundations

| Clock | Min | Topic | Site page |
|---|---:|---|---|
| 0:00 | 5 | Why this weekend (course opener) | [m1-rule-and-mechanics#opener](../day1/m1-rule-and-mechanics.qmd#opener) |
| 0:05 | 5 | The rule for the weekend | [m1-rule-and-mechanics#rule](../day1/m1-rule-and-mechanics.qmd#rule) |
| 0:10 | 10 | How these tools actually work | [m1-rule-and-mechanics#how-it-works](../day1/m1-rule-and-mechanics.qmd#how-it-works) |
| 0:20 | 5 | Your three-question check | [m1-rule-and-mechanics#three-questions](../day1/m1-rule-and-mechanics.qmd#three-questions) |
| 0:25 | 5 | Where the extra words come from | [m2-prompting#extra-words](../day1/m2-prompting.qmd#extra-words) |
| 0:30 | 10 | Anatomy of a good prompt | [m2-prompting#anatomy](../day1/m2-prompting.qmd#anatomy) |
| 0:40 | 5 | Structure fixes it (notes) | [m2-prompting#structure-notes](../day1/m2-prompting.qmd#structure-notes) |
| 0:45 | 15 | Same framework, three more jobs | [m2-prompting#three-more-jobs](../day1/m2-prompting.qmd#three-more-jobs) |
| 1:00 | 5 | Not all AI is the same | [m3-choosing-tools#tool-types](../day1/m3-choosing-tools.qmd#tool-types) |
| 1:05 | 5 | Same tool, different doctor | [m3-choosing-tools#different-doctor](../day1/m3-choosing-tools.qmd#different-doctor) |
| 1:10 | 5 | Live demo: same question, two tools | [m3-choosing-tools#live-demo](../day1/m3-choosing-tools.qmd#live-demo) |
| 1:15 | 5 | Spend your quota on purpose | [m3-choosing-tools#quota](../day1/m3-choosing-tools.qmd#quota) |
| 1:20 | 10 | Break | - |
| 1:30 | 12 | Lab One, part 1 — Template test | [lab1-templates-and-limits#part-1](../day1/lab1-templates-and-limits.qmd#part-1) |
| 1:42 | 8 | Lab One, part 2 — Break it on purpose | [lab1-templates-and-limits#part-2](../day1/lab1-templates-and-limits.qmd#part-2) |
| 1:50 | 5 | Lab One, part 3 — Tool face-off | [lab1-templates-and-limits#part-3](../day1/lab1-templates-and-limits.qmd#part-3) |
| 1:55 | 5 | Lab One — Debrief | [lab1-templates-and-limits#debrief](../day1/lab1-templates-and-limits.qmd#debrief) |

Total 120 min.

### Day 2: Applications

| Clock | Min | Topic | Site page |
|---|---:|---|---|
| 0:00 | 10 | Four places AI already fits | [m4-notes-and-audiences#four-places](../day2/m4-notes-and-audiences.qmd#four-places) |
| 0:10 | 5 | Notes, done right | [m4-notes-and-audiences#notes-done-right](../day2/m4-notes-and-audiences.qmd#notes-done-right) |
| 0:15 | 10 | Already live in Saudi clinics | [m4-notes-and-audiences#saudi-scribes](../day2/m4-notes-and-audiences.qmd#saudi-scribes) |
| 0:25 | 15 | Same note, three audiences | [m4-notes-and-audiences#three-audiences](../day2/m4-notes-and-audiences.qmd#three-audiences) |
| 0:40 | 8 | From case to slide deck | [m5-talks-and-teaching#case-to-deck](../day2/m5-talks-and-teaching.qmd#case-to-deck) |
| 0:48 | 12 | Building a full talk, not just an outline | [m5-talks-and-teaching#full-talk](../day2/m5-talks-and-teaching.qmd#full-talk) |
| 1:00 | 8 | Teaching with AI | [m5-talks-and-teaching#teaching-with-ai](../day2/m5-talks-and-teaching.qmd#teaching-with-ai) |
| 1:08 | 7 | Grading yourself | [m5-talks-and-teaching#grading-yourself](../day2/m5-talks-and-teaching.qmd#grading-yourself) |
| 1:15 | 10 | Break | - |
| 1:25 | 20 | Lab Two, part 1 — One case, three outputs | [lab2-one-case-three-outputs#part-1](../day2/lab2-one-case-three-outputs.qmd#part-1) |
| 1:45 | 10 | Lab Two, part 2 — Tool check, again | [lab2-one-case-three-outputs#part-2](../day2/lab2-one-case-three-outputs.qmd#part-2) |
| 1:55 | 5 | Lab Two, part 3 — Share-out | [lab2-one-case-three-outputs#part-3](../day2/lab2-one-case-three-outputs.qmd#part-3) |

Total 120 min.

### Day 3: Safety & Ethics

| Clock | Min | Topic | Site page |
|---|---:|---|---|
| 0:00 | 10 | Confidently wrong | [m6-confidently-wrong#confidently-wrong](../day3/m6-confidently-wrong.qmd#confidently-wrong) |
| 0:10 | 15 | Lab Three, part 1 — Trade and catch | [lab3-spot-the-error#part-1](../day3/lab3-spot-the-error.qmd#part-1) |
| 0:25 | 10 | Lab Three, part 2 — Instructor examples | [lab3-spot-the-error#part-2](../day3/lab3-spot-the-error.qmd#part-2) |
| 0:35 | 10 | The rule that isn't optional | [m7-privacy#the-rule](../day3/m7-privacy.qmd#the-rule) |
| 0:45 | 15 | Where doctors get this wrong | [m7-privacy#where-doctors-go-wrong](../day3/m7-privacy.qmd#where-doctors-go-wrong) |
| 1:00 | 10 | Break | - |
| 1:10 | 20 | Back to the rule, applied to a real case | [m8-back-to-the-rule#back-to-the-rule](../day3/m8-back-to-the-rule.qmd#back-to-the-rule) |
| 1:30 | 20 | Assessment quiz | [m8-back-to-the-rule#assessment](../day3/m8-back-to-the-rule.qmd#assessment) |
| 1:50 | 10 | Certificate and closing | [m8-back-to-the-rule#closing](../day3/m8-back-to-the-rule.qmd#closing) |

Total 120 min.
<!-- runofshow:end -->

## Before each day

**Every day.** A projector and a timer the room can see. Your presenting machine signed in to a general
assistant *and* Vera Health, in separate tabs. The site open on `reference/case-cards`. A short link to the
site on the first slide. Printed copies of the three-question check (one page) and the day's lab worksheet.

**Day One.** Type the live-demo question into a text file so you can paste it into both tools at once.
**Rehearse the demo the day before and keep screenshots of the real outputs as a fallback**: real ones,
never invented. Check who has finished Vera Health verification and pair up anyone who has not.

**Day Two.** Re-check the Sahl AI and Augnito facts against the brief. Have `reference/practice-source` open.

**Day Three.** Have the Lab 3 backup examples ready to project (in `day3-talking-points.md`). Prepare the
certificates and the quiz logistics outside the repository.

## The moments that carry the weekend

Protect these, and let the others shrink if the clock forces it.

**Day One.** (1) The room finishing a half-sentence, and every answer being plausible: plausible is not
correct. (2) Each participant seeing their own numbers for the templated versus untemplated note. (3) Someone
saying "but it sounded so sure" after the break-it probe.

**Day Two.** (1) The room finding the three planted problems in an AI-drafted note. (2) A cross-output check
catching a follow-up interval that differs between the chart note and the patient instructions. (3) The
"4.35 out of 5, is that good?" discussion, because it shows how to read a number.

**Day Three.** (1) A participant finding a fabricated reference in a neighbor's Lab 1 output. (2) The
screenshot vignette, when the room realizes the name was in the banner. (3) Someone running the check on their
own output and saying "no" to the third question, which is the outcome the whole weekend is for.

## Running the room

- **A room that asks questions.** Keep a visible parking lot. Most questions are answered by the
  three-question check, so answer in under a minute and say which question it was.
- **Mixed enthusiasm.** The skeptic and the enthusiast are both right. Give the skeptic the checking job
  and the enthusiast the prompting job.
- **If someone pastes real patient data during a lab.** Do not shame. Stop the room for a minute and use it:
  this is the exact case Day Three is about. Send them to "If it already happened" on the privacy checklist.
- **If a tool gives an excellent answer during a face-off.** Use it. Ask: would you catch it if it were wrong?
- **Specialties differ.** The cards span primary care, medicine, pediatrics and surgery. Let a participant
  swap to the card closest to their own work.

## Risks and fallbacks

| What goes wrong | Fallback |
|---|---|
| A tool is down or slow during the live demo | Show the screenshots of real outputs from your rehearsal; say they are a recorded run |
| Vera Health verification is pending for someone | Pair them with a neighbor for the face-off |
| A participant hits the free-tier limit mid-lab | Switch to the other tool; never share a login |
| Wi-Fi fails | Phones on mobile data, with synthetic cases only |
| Hospital networks block a tool | Own device and connection, synthetic cases only; never bypass a control with real patient data |
| Lab 3 swap surfaces nothing to catch | Use the two prepared backup examples |
| Arabic output looks wrong | Ask for Modern Standard Arabic in simple wording, and say a fluent reader must check it |

## Open decisions

Facts nobody had. None of them is on a published page (`python tools/check_placeholders.py` fails CI if one
ever appears there); each is marked `[TRAINER TO CONFIRM: ...]` in the talking-points file that needs it, and
`grep -rn "TRAINER TO CONFIRM" course/` lists them all.

**Assessment (Day Three, topic 8: the site says only "a short quiz covering all three days").**
Open or closed book, and whether the course site, notes or an AI tool may be used. Format: paper or online
form, number and type of questions, how long the quiz itself takes within the twenty minutes. Pass mark, if any,
and whether the certificate depends on it. How results are given and whether answers are reviewed. What early
finishers do, and whether a retake or late finish is allowed. How the quiz is delivered and collected, and
whether phones or laptops are allowed.

**Closing (Day Three, topic 9).** How and when certificates are issued, and in what form. The feedback link, and
whether the form is anonymous. Whether SCFHS CPD accreditation is granted and for how many hours (see
`accreditation.md`); until then the course claims none. How long participants keep access to the site, and any
terms on sharing it.

**Before Day One.** Your own Vera Health access, verified and working from the venue network. The question for
the live demo (topic 11).

**Before Day Two.** The current status of Sahl AI and Augnito at the sites named. Read the Sahl AI paper's
abstract yourself: its text could not be opened when this was written, so 42.2 of 45 and 4.35 of 5 are the
brief's figures, not independently checked here (a search result confirmed the paper exists, is a prospective
single-arm pilot, and used a modified PDQI-9).

**For the repository.** It is public at `MohammadYusif/ai-for-clinicians` and the site is live at
`https://mohammadyusif.github.io/ai-for-clinicians/`. Which licence, if any: with none, others can read and fork
the repository but have no right to reuse it. Whether `day3-talking-points.md` should stay public: its Lab Three
facilitation section holds the two backup examples and their answer keys, which a participant could find and read
before the exercise. Who reads the case cards as a clinician.

## Updating the deck

The deck is a Slides artifact at the link in `BRIEF.md`: `project/deck.json` plus one
`project/slides/<id>.html` per slide, with speaker notes of at most 4,000 characters. This repository holds
the words; nothing here edits the deck.

| Existing slide id | Topic | Change |
|---|---|---|
| `cover`, `agenda`, `day1-divider` | Opener | none |
| `why`, `outcomes` | Opener | **reword two cards that promised a time saving** ("Time back"; outcome 01 "cuts note-writing time"): the site makes no time claim, and Lab 1 has each participant measure their own. Replacement text is in the Day One script, Topic 1 |
| `rule` | The rule | none |
| `gutcheck` | Three questions | none |
| `extra-words` | Extra words | none |
| `structure-fix` | Structure fixes it | reframe as one application of the four-part framework; **soften the two captions**, which state unmeasured results as facts (replacements in the Day One script, Topic 7) |
| `tool-types` | Not all AI is the same | optional: preview scribes and EMR features |
| `geography` | Same tool, different doctor | **correct the OpenEvidence wording**: the old slide says "Free" and "a US medical license", neither of which the brief says (see above; replacement in the Day One script, Topic 10) |
| `quota` | Quota | add the two extra tips |
| `lab1` | Lab One | rewrite as the three-part lab on a synthetic case |
| `day2-divider`, `four-places` | Four places | none |
| `notes-right` | Notes done right | none |
| `saudi-scribes` | Saudi scribes | **replace the last line and the Augnito card** (see above); add "reading the numbers" |
| `case-to-deck`, `teaching-ai` | Deck and teaching | none |
| `lab2` | Lab Two | rewrite as three outputs, a tool check, and a share-out |
| `day3-divider`, `confidently-wrong` | Day Three | none (new verification slides added) |
| `privacy-rule` | The rule that isn't optional | one wording fix: "Saudi's Personal Data Protection Law" becomes "Saudi Arabia's Personal Data Protection Law, enforced by SDAIA" |
| `back-to-rule` | Back to the rule | expand into the group exercise; the three pills abbreviate the questions ("Can I verify it?", "Would I catch it wrong?"), so use the exact wording |
| `assessment`, `closing` | Close | closing expands into the first-two-weeks plan |

The new slides each day needs are specified, with headline, on-slide text, visual note and paste-ready
speaker notes (each under 900 characters; the deck allows 4,000), in the three talking-points files. In all,
they specify 79 slides: about 52 new and about 27 kept (several of those reworded), against the 26 in the deck
now. The deck's design system is in `BRIEF.md`.
