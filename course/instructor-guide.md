# Instructor guide

Trainer-facing. Not published to the site. The repository is public, so nothing here is secret: no
roster, no participant names, no answer key for the scored quiz.

## How to run a session

1. **Open the day's first deck** (the links are in the run-of-show below) and press `S`. The speaker view shows the
   slide, the next slide, a clock and your notes. Keep it on a second screen or in a window you do not share. Share
   the deck window, not your whole desktop.
2. **Paste two links into the chat:** the deck, so people can open it in a window of their own, and the handout page.
3. **Follow the slides in order.** A topic slide (the dark one) carries the topic's brief in its notes: the goal, what to
   have ready, what to watch for, what people ask, and the line into the next topic. Every slide after it opens its notes
   with its own time budget (`1:30`), then what to say, then what to do. The budgets of a topic add up to its minutes.
4. **Say which move it is.** Every activity is one of five (below), and the slide shows it as a label and a time. Say the
   label out loud the first few times and people learn the rhythm.
5. **Keep the clock on the plan slide.** Each deck opens with a table of its topics and their minutes, generated from
   `timing.json`, so the clock on the slide is always the clock in the repository.

The handouts are the participants' reference: the prompts to copy and the tables to fill in. The decks are what you
present. A lab has both: the deck is your driver and the lab page is where participants work.

## The five moves

Everything interactive is one of these, announced on the slide. Write any new activity with them
(`authoring-guide.md`, section 9).

| Move | What happens | Notes for the instructor |
|---|---|---|
| **Chat** | Everyone types at once; you read a few out | Say "three, two, one, send" so answers land together. Allow 60 to 90 seconds for a sentence. Read out two or three, not all |
| **Speak** | Two or three people unmute when asked | Ask by name, or ask for volunteers in the chat. Silence for ten seconds is normal |
| **Share** | One person shares a screen when asked | Ask in the chat for "I can share"; never press someone into it |
| **Pair** | A breakout room of two, three to six minutes | Used twice only: Lab 3 part 1 and the pair check in Module 8. Open the rooms, then look in on a few |
| **Solo** | Own device, own assistant | The labs. Watch the chat for stuck people; a co-host helps |

**If the platform has no breakout rooms**, the two pair steps have fallbacks in the speaker notes, and both keep the
point of the step. Lab 3 part 1: each person checks their own saved output cold, as if someone else had written it, then
types the kind of error they would most easily have missed. Module 8: each person types their decision (use, fix,
discard) and the one mark they are least sure of, and the group asks "where did that come from?" about three of them.

**A co-host is worth having** for the labs: someone to watch the chat, admit latecomers and look in on breakout rooms
while you teach. The course does not depend on one.

## The weekend at a glance

Three days, two hours each, online. Each day is **120 minutes including a 10-minute break**: 110 minutes of teaching
and lab, 330 in total. The hands-on labs are 30 + 35 + 25 = 90 minutes, over a quarter of the weekend.

| Day | Job of the day | Lab |
|---|---|---|
| **One** — Foundations | Get a better draft: why the tools sound sure, the four-part prompt, choosing a tool | Templates, limits, tool face-off |
| **Two** — Applications | Use it on real documents and teaching, and check that outputs agree | One case, three outputs |
| **Three** — Safety & Ethics | Make the check and the privacy line automatic | Spot the error |

Two sentences carry everything: **"AI drafts. You decide."** and **"Tone is not a signal. A
verification step is."** If a discussion drifts, steer it back to one of them.

## What changed from the brief

The site departs from `BRIEF.md` in these places. Each is deliberate; each can be reversed.

### 1. Day One did not add up, so it was re-timed

The brief's Day One table sums to **130 minutes**, not the 120 it states. Its own Lab One spec
(15 + 10 + 5 + 5) is **35 minutes**, not the 25 in its table, so read literally Day One is **140**.
Days Two and Three sum to 120 as briefed and are unchanged.

| Item | Brief | Now | Why this one |
|---|---:|---:|---|
| Course opener | 10 | 5 | The home page and the first slides carry the pitch; the rule follows straight after |
| Structure fixes it (notes) | 10 | 5 | Lab 1 part 1 is now its hands-on, so the demo can be the before-and-after alone |
| Live demo, two tools | 10 | 5 | Pre-load both tools and paste rather than type; the lab's face-off is the group's own run |
| Lab One | 25 in the table, 35 in the spec | 30 (12 + 8 + 5 + 5) | All four parts kept; the two long parts trimmed |

If you would rather cut elsewhere, edit `course/timing.json` and the `[N min]` badge on the page and the deck, then run
`python tools/check_timing.py`. It reports every page, deck, badge and total that disagrees. Options that work: fold
the live demo into the start of Lab 1 part 3 and give the face-off ten minutes; or drop "Structure fixes it" as its
own topic and let Lab 1 part 1 carry it.

### 2. Three claims on the old deck needed correcting (done in the new decks)

- **`saudi-scribes`, last line.** The old deck said "Purpose-built tools already beat generic prompting for this exact
  complaint." The pilot behind the slide reported documentation quality ratings for one scribe; it did not compare
  against generic prompting (the paper describes a single-arm pilot). The deck now says reported accuracy was 4.35 of 5,
  short of the maximum, so the note is still read line by line.
- **`saudi-scribes`, Augnito card.** The old deck said the scribe is "integrated directly into the hospital's own medical
  records system." The public announcement (a press release dated 31 January 2025, signed at the Arab Health Exhibition)
  uses the future tense: the agreement "will see" the scribe integrated with the EMR/HIS, in a phased rollout, and it
  reports no deployment or accuracy figures. The deck says it was announced for integration. The slide title, "Already
  Live in Saudi Clinics", is fair for a pilot and generous for an announcement; confirm each tool's current status before
  Day Two.
- **`geography`** said OpenEvidence "requires a US medical license". The brief says **US NPI verification**, and that it
  **withdrew from the EU and UK in April 2026**. The deck uses the brief's wording, dated "as of September 2026".
  Re-check availability the week you teach: it changes.

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
- Checks that fail CI: the clock, the prompt library, unfinished placeholders, the decks' structure, and any wording
  that assumes a shared room.

### 6. The tool comparisons do not depend on Vera Health, or on any tool

The brief pairs a general assistant with a literature-grounded tool in both labs and the live demo, and the first
draft assumed everyone would have Vera Health access. Its public information does not settle that for Saudi
participants, or for a trainer who is not a clinician: the Terms require users to be healthcare professionals in
practice or in training and bar people in countries under US sanctions (Saudi Arabia is not among those named), but
how credentials are checked is not published. So the site's only requirement is **one general assistant**. The
"second option" in each comparison is whichever of three the person can open: a literature-grounded tool, the
assistant's own search or citation mode, or a plain literature search (PubMed or a library database).
[Module 3](../day1/m3-choosing-tools.qmd#second-option) defines it, and the setup page, both labs and the decks
point to it. For the live demo, a clinician colleague's account or a participant's screen also works.

### 7. The course is online first, and the script moved into the decks

The old activities that assumed a shared space (the ones in the list at the end of `authoring-guide.md`, section 9) are gone
from every page, deck and note, and the lint keeps them out (rule 5 in `CLAUDE.md`). Each became one of the five moves. The three
long talking-points files were folded into the decks: the slide text is on the slide, and what to say and do is in the
speaker notes under it, so there is one thing to follow instead of three. The Lab 3 examples and answer keys moved to
[`lab3-examples.md`](lab3-examples.md) and are shared from a private copy, never from a site deck.

### 8. Not done

- **The scored quiz.** The brief marks it "kept" and it is not in the material I was given. The bank on
  `assessment.qmd` is practice, not the quiz. If the scored quiz becomes a form, keep it and its key out of
  this public repository, and apply the answer-position and answer-length balancing rules in your workspace.
- **A trainer read of the decks.** They were built from the old scripts and checked by machine (structure, wording,
  overflow, contrast, notes). Nobody has presented them yet. The live-demo question is still yours to choose (see
  "Open decisions"): the `demo-grid` slide points to the `evidence-question` prompt, and you paste your question into it.
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

| Clock | Min | Topic | Slides | Handout |
|---|---:|---|---|---|
| 0:00 | 5 | Why this weekend (course opener) | [m1-rule-and-mechanics#opener](../slides/m1-rule-and-mechanics.qmd#/opener) | [m1-rule-and-mechanics#opener](../day1/m1-rule-and-mechanics.qmd#opener) |
| 0:05 | 5 | The rule for the weekend | [m1-rule-and-mechanics#rule](../slides/m1-rule-and-mechanics.qmd#/rule) | [m1-rule-and-mechanics#rule](../day1/m1-rule-and-mechanics.qmd#rule) |
| 0:10 | 10 | How these tools actually work | [m1-rule-and-mechanics#how-it-works](../slides/m1-rule-and-mechanics.qmd#/how-it-works) | [m1-rule-and-mechanics#how-it-works](../day1/m1-rule-and-mechanics.qmd#how-it-works) |
| 0:20 | 5 | Your three-question check | [m1-rule-and-mechanics#three-questions](../slides/m1-rule-and-mechanics.qmd#/three-questions) | [m1-rule-and-mechanics#three-questions](../day1/m1-rule-and-mechanics.qmd#three-questions) |
| 0:25 | 5 | Where the extra words come from | [m2-prompting#extra-words](../slides/m2-prompting.qmd#/extra-words) | [m2-prompting#extra-words](../day1/m2-prompting.qmd#extra-words) |
| 0:30 | 10 | Anatomy of a good prompt | [m2-prompting#anatomy](../slides/m2-prompting.qmd#/anatomy) | [m2-prompting#anatomy](../day1/m2-prompting.qmd#anatomy) |
| 0:40 | 5 | Structure fixes it (notes) | [m2-prompting#structure-notes](../slides/m2-prompting.qmd#/structure-notes) | [m2-prompting#structure-notes](../day1/m2-prompting.qmd#structure-notes) |
| 0:45 | 15 | Same framework, three more jobs | [m2-prompting#three-more-jobs](../slides/m2-prompting.qmd#/three-more-jobs) | [m2-prompting#three-more-jobs](../day1/m2-prompting.qmd#three-more-jobs) |
| 1:00 | 5 | Not all AI is the same | [m3-choosing-tools#tool-types](../slides/m3-choosing-tools.qmd#/tool-types) | [m3-choosing-tools#tool-types](../day1/m3-choosing-tools.qmd#tool-types) |
| 1:05 | 5 | Same tool, different doctor | [m3-choosing-tools#different-doctor](../slides/m3-choosing-tools.qmd#/different-doctor) | [m3-choosing-tools#different-doctor](../day1/m3-choosing-tools.qmd#different-doctor) |
| 1:10 | 5 | Live demo: same question, two tools | [m3-choosing-tools#live-demo](../slides/m3-choosing-tools.qmd#/live-demo) | [m3-choosing-tools#live-demo](../day1/m3-choosing-tools.qmd#live-demo) |
| 1:15 | 5 | Spend your quota on purpose | [m3-choosing-tools#quota](../slides/m3-choosing-tools.qmd#/quota) | [m3-choosing-tools#quota](../day1/m3-choosing-tools.qmd#quota) |
| 1:20 | 10 | Break | - | - |
| 1:30 | 12 | Lab One, part 1 — Template test | [lab1-templates-and-limits#part-1](../slides/lab1-templates-and-limits.qmd#/part-1) | [lab1-templates-and-limits#part-1](../day1/lab1-templates-and-limits.qmd#part-1) |
| 1:42 | 8 | Lab One, part 2 — Break it on purpose | [lab1-templates-and-limits#part-2](../slides/lab1-templates-and-limits.qmd#/part-2) | [lab1-templates-and-limits#part-2](../day1/lab1-templates-and-limits.qmd#part-2) |
| 1:50 | 5 | Lab One, part 3 — Tool face-off | [lab1-templates-and-limits#part-3](../slides/lab1-templates-and-limits.qmd#/part-3) | [lab1-templates-and-limits#part-3](../day1/lab1-templates-and-limits.qmd#part-3) |
| 1:55 | 5 | Lab One — Debrief | [lab1-templates-and-limits#debrief](../slides/lab1-templates-and-limits.qmd#/debrief) | [lab1-templates-and-limits#debrief](../day1/lab1-templates-and-limits.qmd#debrief) |

Total 120 min.

### Day 2: Applications

| Clock | Min | Topic | Slides | Handout |
|---|---:|---|---|---|
| 0:00 | 10 | Four places AI already fits | [m4-notes-and-audiences#four-places](../slides/m4-notes-and-audiences.qmd#/four-places) | [m4-notes-and-audiences#four-places](../day2/m4-notes-and-audiences.qmd#four-places) |
| 0:10 | 5 | Notes, done right | [m4-notes-and-audiences#notes-done-right](../slides/m4-notes-and-audiences.qmd#/notes-done-right) | [m4-notes-and-audiences#notes-done-right](../day2/m4-notes-and-audiences.qmd#notes-done-right) |
| 0:15 | 10 | Already live in Saudi clinics | [m4-notes-and-audiences#saudi-scribes](../slides/m4-notes-and-audiences.qmd#/saudi-scribes) | [m4-notes-and-audiences#saudi-scribes](../day2/m4-notes-and-audiences.qmd#saudi-scribes) |
| 0:25 | 15 | Same note, three audiences | [m4-notes-and-audiences#three-audiences](../slides/m4-notes-and-audiences.qmd#/three-audiences) | [m4-notes-and-audiences#three-audiences](../day2/m4-notes-and-audiences.qmd#three-audiences) |
| 0:40 | 8 | From case to slide deck | [m5-talks-and-teaching#case-to-deck](../slides/m5-talks-and-teaching.qmd#/case-to-deck) | [m5-talks-and-teaching#case-to-deck](../day2/m5-talks-and-teaching.qmd#case-to-deck) |
| 0:48 | 12 | Building a full talk, not just an outline | [m5-talks-and-teaching#full-talk](../slides/m5-talks-and-teaching.qmd#/full-talk) | [m5-talks-and-teaching#full-talk](../day2/m5-talks-and-teaching.qmd#full-talk) |
| 1:00 | 8 | Teaching with AI | [m5-talks-and-teaching#teaching-with-ai](../slides/m5-talks-and-teaching.qmd#/teaching-with-ai) | [m5-talks-and-teaching#teaching-with-ai](../day2/m5-talks-and-teaching.qmd#teaching-with-ai) |
| 1:08 | 7 | Grading yourself | [m5-talks-and-teaching#grading-yourself](../slides/m5-talks-and-teaching.qmd#/grading-yourself) | [m5-talks-and-teaching#grading-yourself](../day2/m5-talks-and-teaching.qmd#grading-yourself) |
| 1:15 | 10 | Break | - | - |
| 1:25 | 20 | Lab Two, part 1 — One case, three outputs | [lab2-one-case-three-outputs#part-1](../slides/lab2-one-case-three-outputs.qmd#/part-1) | [lab2-one-case-three-outputs#part-1](../day2/lab2-one-case-three-outputs.qmd#part-1) |
| 1:45 | 10 | Lab Two, part 2 — Tool check, again | [lab2-one-case-three-outputs#part-2](../slides/lab2-one-case-three-outputs.qmd#/part-2) | [lab2-one-case-three-outputs#part-2](../day2/lab2-one-case-three-outputs.qmd#part-2) |
| 1:55 | 5 | Lab Two, part 3 — Share-out | [lab2-one-case-three-outputs#part-3](../slides/lab2-one-case-three-outputs.qmd#/part-3) | [lab2-one-case-three-outputs#part-3](../day2/lab2-one-case-three-outputs.qmd#part-3) |

Total 120 min.

### Day 3: Safety & Ethics

| Clock | Min | Topic | Slides | Handout |
|---|---:|---|---|---|
| 0:00 | 10 | Confidently wrong | [m6-confidently-wrong#confidently-wrong](../slides/m6-confidently-wrong.qmd#/confidently-wrong) | [m6-confidently-wrong#confidently-wrong](../day3/m6-confidently-wrong.qmd#confidently-wrong) |
| 0:10 | 15 | Lab Three, part 1 — Trade and catch | [lab3-spot-the-error#part-1](../slides/lab3-spot-the-error.qmd#/part-1) | [lab3-spot-the-error#part-1](../day3/lab3-spot-the-error.qmd#part-1) |
| 0:25 | 10 | Lab Three, part 2 — Instructor examples | [lab3-spot-the-error#part-2](../slides/lab3-spot-the-error.qmd#/part-2) | [lab3-spot-the-error#part-2](../day3/lab3-spot-the-error.qmd#part-2) |
| 0:35 | 10 | The rule that isn't optional | [m7-privacy#the-rule](../slides/m7-privacy.qmd#/the-rule) | [m7-privacy#the-rule](../day3/m7-privacy.qmd#the-rule) |
| 0:45 | 15 | Where doctors get this wrong | [m7-privacy#where-doctors-go-wrong](../slides/m7-privacy.qmd#/where-doctors-go-wrong) | [m7-privacy#where-doctors-go-wrong](../day3/m7-privacy.qmd#where-doctors-go-wrong) |
| 1:00 | 10 | Break | - | - |
| 1:10 | 20 | Back to the rule, applied to a real case | [m8-back-to-the-rule#back-to-the-rule](../slides/m8-back-to-the-rule.qmd#/back-to-the-rule) | [m8-back-to-the-rule#back-to-the-rule](../day3/m8-back-to-the-rule.qmd#back-to-the-rule) |
| 1:30 | 20 | Assessment quiz | [m8-back-to-the-rule#assessment](../slides/m8-back-to-the-rule.qmd#/assessment) | [m8-back-to-the-rule#assessment](../day3/m8-back-to-the-rule.qmd#assessment) |
| 1:50 | 10 | Certificate and closing | [m8-back-to-the-rule#closing](../slides/m8-back-to-the-rule.qmd#/closing) | [m8-back-to-the-rule#closing](../day3/m8-back-to-the-rule.qmd#closing) |

Total 120 min.
<!-- runofshow:end -->

## Before each day

**Every day.** A good connection, headphones, and a timer you can see. Share a single window, not your desktop. Your
presenting machine signed in to a general assistant, plus your second option (see Module 3) in another window. The
deck open with the speaker view on a second screen. The case cards page open. Test screen sharing and, for Day One and
Day Three, breakout rooms: enable them in the platform settings before the call, because most platforms need that
done by the host in advance. Join ten minutes early.

**Day One.** Type the live-demo question into a text file so you can paste it into both tools at once. **Rehearse the demo
the day before and keep screenshots of the real outputs as a fallback**: real ones, never invented. Nothing needs
verifying: anyone without a working second option uses another of the three, or follows your shared screen.

**Day Two.** Re-check the Sahl AI and Augnito facts against the brief. Have `reference/practice-source` open.

**Day Three.** Have the Lab 3 examples ready to share from a private copy (`lab3-examples.md`, or the private deck). Prepare
the certificates and the quiz logistics outside the repository. Have a message ready to post on the morning of Day Three
reminding people to keep their Lab One "break it on purpose" output open.

## The moments that carry the weekend

Protect these, and let the others shrink if the clock forces it.

**Day One.** (1) The chat filling with a plausible next word, and no two years agreeing: plausible is not
correct. (2) Each participant seeing their own numbers for the templated versus untemplated note. (3) Someone
saying "but it sounded so sure" after the break-it probe.

**Day Two.** (1) The group finding the three planted problems in an AI-drafted note. (2) A cross-output check
catching a follow-up interval that differs between the chart note and the patient instructions. (3) The
"4.35 out of 5, is that good?" discussion, because it shows how to read a number.

**Day Three.** (1) A participant finding a fabricated reference in a partner's Lab 1 output. (2) The
screenshot vignette, when the group realizes the name was in the banner. (3) Someone running the check on their
own output and saying "no" to the third question, which is the outcome the whole weekend is for.

## Running the call

- **A group that asks questions.** Keep a visible parking lot, in the chat or on the chalkboard (press `B`). Most questions
  are answered by the three-question check, so answer in under a minute and say which question it was.
- **Mixed enthusiasm.** The skeptic and the enthusiast are both right. Give the skeptic the checking job
  and the enthusiast the prompting job.
- **If someone pastes real patient data during a lab.** Do not shame. Stop for a minute and use it:
  this is the exact case Day Three is about. Send them to "If it already happened" on the privacy checklist.
- **If a tool gives an excellent answer during a face-off.** Use it. Ask: would you catch it if it were wrong?
- **Specialties differ.** The cards span primary care, medicine, pediatrics and surgery. Let a participant
  use the card closest to their own work.
- **Quiet chat.** People type slower than they talk and some will not type. Read a few answers out by first name,
  thank them, and ask a second question; do not wait out the silence.
- **The chalkboard** (press `B`, `C` to draw on the slide) works on a shared deck, for circling the changed dose or
  keeping a parking lot. Press `B` again to put it away.

## Risks and fallbacks

| What goes wrong | Fallback |
|---|---|
| A tool is down or slow during the live demo | Show the screenshots of real outputs from your rehearsal; say they are a recorded run |
| A participant cannot open a literature-grounded tool | Either of the other two second options works; nothing depends on it |
| A participant hits the free-tier limit mid-lab | Switch to the other tool; never share a login |
| A participant has no assistant account | They follow your shared screen and still fill in the grid; the setup page says so |
| Breakout rooms are not available | Use the fallbacks under "The five moves"; both pair steps have one |
| Screen sharing fails | Paste the deck link and the page link in the chat and have people follow in their own window; present from the chat |
| The chat is disabled or full | Ask for "1 / 2 / 3" by unmuting in turn, or use the platform's reactions for yes and no |
| A participant joins late | A co-host sends the deck link and the lab page; they pick up at the current slide |
| Wi-Fi fails | Phones on mobile data, with synthetic cases only |
| Hospital networks block a tool | Own device and connection, synthetic cases only; never bypass a control with real patient data |
| Lab 3 part 1 surfaces nothing to catch | Move to the prepared examples in part 2 |
| Arabic output looks wrong | Ask for Modern Standard Arabic in simple wording, and say a fluent reader must check it |

## Open decisions

Facts nobody had. None of them is on a published page or in a deck (`python tools/check_placeholders.py` fails CI if a
placeholder ever appears there); they are listed here and nowhere else.

**Assessment (Day Three, topic 8: the site says only "a short quiz covering all three days").**
Open or closed book, and whether the course site, notes or an AI tool may be used. Format: an online form or a
shared document, number and type of questions, how long the quiz itself takes within the twenty minutes. Pass mark,
if any, and whether the certificate depends on it. How results are given and whether answers are reviewed. What
early finishers do, and whether a retake or late finish is allowed. How the quiz is delivered and collected.

**Closing (Day Three, topic 9).** How and when certificates are issued, and in what form. The feedback link, and
whether the form is anonymous. Whether SCFHS CPD accreditation is granted and for how many hours (see
`accreditation.md`); until then the course claims none. How long participants keep access to the site, and any
terms on sharing it.

**Before Day One.** Your second option for the live demo. A literature-grounded tool such as Vera Health is for
healthcare professionals, so if you are not one, use your assistant's search mode, a literature search, or a
clinician's screen. The question for the live demo (topic 11). Which video platform, and whether breakout rooms and
a co-host are available.

**Before Day Two.** The current status of Sahl AI and Augnito at the sites named. Read the Sahl AI paper's
abstract yourself: its text could not be opened when this was written, so 42.2 of 45 and 4.35 of 5 are the
brief's figures, not independently checked here (a search result confirmed the paper exists, is a prospective
single-arm pilot, and used a modified PDQI-9).

**For the repository.** It is public at `MohammadYusif/ai-for-clinicians` and the site is live at
`https://mohammadyusif.github.io/ai-for-clinicians/`. Which licence, if any: with none, others can read and fork
the repository but have no right to reuse it. Whether `lab3-examples.md` should stay in the public repository: it
holds the two examples and their answer keys, which a participant could find and read before the exercise. Who reads the
case cards as a clinician.

## Where things are

| What | Where |
|---|---|
| The decks you present, with the script in the notes | `slides/`, one per module and lab, same file name as its handout |
| The handouts, with the prompts to copy | `day1/`, `day2/`, `day3/` |
| The clock, the single source of every minute | `course/timing.json`; the tables on the slides and the run-of-show above are generated from it |
| The Lab 3 examples and answer keys, trainer only | `course/lab3-examples.md` |
| How to write or change a page, a deck or a note | `course/authoring-guide.md` |
| The checks | `tools/`; `README.md` lists them |

**The claude.ai deck** (the link in `BRIEF.md`) is a copy for anyone who prefers editing slides in that tool. Its speaker
notes were refreshed from these decks on 2 October 2026, and it holds the four Lab 3 example slides that the site
decks deliberately leave out. It does not follow later edits to the site decks: when the two disagree, the site wins.
