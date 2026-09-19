# Day Two talking points: Applications

Instructor script for Day Two: eight timed topics, a 10-minute break, then Lab Two, 120 minutes in all. Every minute comes from `course/timing.json`; vocabulary and claim limits come from `course/authoring-guide.md`. Participant pages: [Module 4](../day2/m4-notes-and-audiences.qmd), [Module 5](../day2/m5-talks-and-teaching.qmd), [Lab 2](../day2/lab2-one-case-three-outputs.qmd). Every case is a synthetic [case card](../reference/case-cards.qmd); no real patient is ever used.

| Topic | Min | Starts | Deck |
|---|---|---|---|
| 1 Four places AI already fits | 10 | 0:00 | kept `day2-divider`, `four-places`; new `day1-recap` |
| 2 Notes, done right | 5 | 0:10 | kept `notes-right`; new `sixty-second-review` |
| 3 Already live in Saudi clinics | 10 | 0:15 | kept `saudi-scribes` (text change); new `read-the-numbers`, `scribe-questions` |
| 4 Same note, three audiences | 15 | 0:25 | new `three-audiences`, `source-of-truth`, `consistency-check` |
| 5 From case to slide deck | 8 | 0:40 | kept `case-to-deck`; new `deidentify-slides` |
| 6 Building a full talk | 12 | 0:48 | new `full-talk`, `slide-qa` |
| 7 Teaching with AI | 8 | 1:00 | kept `teaching-ai`; new `mcq-habit` |
| 8 Grading yourself | 7 | 1:08 | new `grade-yourself`, `key-vs-source` |
| Break | 10 | 1:15 | none |
| Lab Two, three parts | 35 | 1:25 | kept `lab2` (text change) |

Two kept slides need new text before class: `saudi-scribes` (its last line is unsupported, see Topic 3) and `lab2` (it says "real case" and offers a choice this lab does not have, see the Lab 2 block). Prompt names below are the library slugs on the participant pages: `source-of-truth-sheet`, `chart-note-from-sheet`, `patient-instructions-from-sheet`, `colleague-letter-from-sheet`, `case-outline`, `full-talk-slides`, `quiz-from-source`, `answer-key-with-quotes`, `orient-and-verify`, `teaching-summary-from-source`.

## Topic 1 — Four places AI already fits (10 min)

Page: [Module 4, section 1](../day2/m4-notes-and-audiences.qmd#four-places). Deck: kept `day2-divider` and `four-places`; new `day1-recap`.

**Goal.** The room can name the four places, the trap in each, and the one of the three questions that guards it.

**Slides.**

1. `day2-divider` (kept, unchanged). Headline: "Applications". On-slide text: "Day Two"; "Notes, presentations, and teaching prep, hands-on." Visual: dark `#0F172A` full-bleed, large teal "02", indigo-to-teal diamond at right, DM Sans. Notes: Welcome back. Yesterday was the rule, the check and the framework. Today you use them on real jobs: notes, talks and teaching, ending with a lab where you build one case three ways. Ask for a show of hands: who used an AI tool since yesterday? Take two answers, no more. If an answer involves patient details, say we return to that on Day Three and move on.
2. `day1-recap` (new). Headline: "Day One in Three Lines". On-slide text: "The rule: AI drafts. You decide."; "The check: three questions"; "The framework: Role · Context · Format · Constraints". Visual: light `#FBFBFD`, three white cards in a row, indigo and teal icons, one line each. Notes: Say the first half of each line and let the room finish it. The rule: AI drafts, you decide. The check: Could I defend this to a colleague? Does it point to something I can verify? Would I catch it if it were wrong? The framework: who it is, what it knows, what shape to return, what to avoid. And the privacy line: No patient identifiers into a consumer AI tool. Ever. Full stop. Two minutes, then move on. Do not re-teach.
3. `four-places` (kept, unchanged). Headline: "Four Places AI Already Fits". On-slide text: the existing four cards, one line each: Daily Questions, Progress Notes, Presentations, Teaching Prep. Visual: card row, four white cards, alternating indigo and teal icons. Notes: One minute per card, always in the same order: the safe pattern, the trap, the question that guards it. Daily questions: orientation between patients, never the decision; the trap is an authoritative tone on a made-up answer; question 2. Progress notes: fixed template, every line read; the trap is a dropped fact; question 3. Presentations: a case with no identifiers; the trap is an identifier on a slide or a number the tool supplied; question 1. Teaching prep: material you may share; the trap is an invented citation or answer key; question 2.

**Say.**

- 0:00–1:00, `day2-divider`: "Welcome back. Yesterday was the rule, the check and the framework. Today you use them on real jobs."
- 1:00–3:00, `day1-recap`: say the first half of each line, let the room finish it.
- 3:00–7:00, `four-places`: one minute per card: safe pattern, trap, guarding question.
  - Daily questions: orientation, never the decision. Trap: a calm tone on a wrong answer, and a citation that looks real and is not. Question 2.
  - Progress notes: fixed template, every line read. Trap: a dropped fact. Question 3.
  - Presentations: a case with no identifiers. Trap: an identifier on a slide, or a number the tool supplied. Question 1: you will defend it in front of colleagues.
  - Teaching prep: material you may share. Trap: invented citations and answer keys. Question 2.
- 7:00–7:45: the finger game (Do).
- 7:45–9:30: worked example and Try it (Do).
- 9:30–10:00: bridge.

**Do.**

1. Before class: deck at `day2-divider`; `orient-and-verify` ready in your tool.
2. At 7:00 read four one-liners; the room holds up 1, 2 or 3 fingers for the guarding question.
   - A drug-interaction answer read straight into an order: 2.
   - The note lists a medicine the patient never took: 3.
   - A slide carries a scan with a name in the corner: 1, and the privacy line.
   - The answer key cites a paper nobody opened: 2.
3. At 7:45 run `orient-and-verify` on a general situation with no identifiers (the page uses new ankle swelling after starting amlodipine). Then 90 seconds: each person rewrites a question from this week with no patient detail, names the source where they would confirm it, and compares with a neighbor.

**If asked.**

- "Can I use it for decisions between patients?" Orientation, yes. The decision, no: AI drafts. You decide. Anything that changes care gets checked in a source you trust.
- "A literature-grounded tool shows citations. Is that enough?" It makes question 2 faster because you can open the source. Opening it is still your job.
- "My hospital has approved nothing. Now what?" Practice on the fictional cards, as here. For real patients: no patient identifiers into a consumer AI tool. Ever. Full stop. Ask your institution what is approved.

**Watch for.**

- "It's only a question" stops being harmless when the answer changes what happens to a patient.
- Someone volunteers a real patient story. Stop kindly, state the privacy line, switch to a card.
- A recap that runs past two minutes. Cut it.

**Bridge.** "The second place is the one you will meet first: the progress note. Five minutes on doing it right."

## Topic 2 — Notes, done right (5 min)

Page: [Module 4, section 2](../day2/m4-notes-and-audiences.qmd#notes-done-right). Deck: kept `notes-right`; new `sixty-second-review`.

**Goal.** The room can run a 60-second review on an AI-drafted note and find what was invented, omitted or altered.

**Slides.**

1. `notes-right` (kept, unchanged). Headline: "Notes, Done Right". On-slide text: "A fixed template, every time"; "An explicit length limit"; "You read every line before it's saved". Visual: light slide, three full-width white cards, indigo check icons, 32px semibold. Notes: Three habits, one per card. A fixed template means the tool returns the same headings every time, so a missing heading is visible. An explicit length limit means a number of words in the prompt, so padding has nowhere to go. The third habit is the one that protects the patient, and the next slide is how to do it. In this room we practice on a fictional case. With a real patient, the note stays in an approved tool. No patient identifiers into a consumer AI tool. Ever. Full stop.
2. `sixty-second-review` (new). Headline: "The 60-Second Review". On-slide text: "Source to draft: tick each fact off; what you cannot tick was omitted"; "Draft to source: find each line; not there is invented, a different value is altered"; "Check first: numbers, medicines, allergies, negations, dates, side, the plan". Visual: two white cards joined by an arrow, teal step numbers, with an indigo-tinted card beneath holding the check-first list. Notes: Two passes of thirty seconds, always against the facts you wrote down, never against your memory of the visit. Pass one, source to draft: tick each fact of your source off in the draft. Whatever you cannot tick was omitted. Pass two, draft to source: find each line of the draft in your source. A line you cannot find was invented. A line you find with a different value was altered. Spend the time where a slip costs most: numbers and units, medicines, allergies, negations, dates and intervals, side, and the plan. A smooth note is not a correct note; fluent writing is the tool's default, not evidence.

**Say.**

- 0:00–0:45, `notes-right`: "Day One's template test gave you the first two habits: a fixed template and a length limit. They shape the output. The third habit is the safety step, and the rest of this section is how."
- 0:45–1:45, `sixty-second-review`: two 30-second passes against the facts you wrote down. Source to draft finds what was omitted; draft to source finds what was invented or altered. Look first where a slip costs most, such as "no chest pain" turning into "chest pain".
- 1:45–4:15: worked example (Do).
- 4:15–5:00: "You found them because I told you there were three. In clinic nobody tells you, so the two passes are the same every time."

**Do.**

1. Before class: Case A ([card](../reference/case-cards.qmd#case-a)) on one half of the screen, the page's illustrative note on the other.
2. Say: "This draft was written for the course, not by any tool. It has three ordinary problems, one of each kind." Do not say which.
3. Sixty seconds, timer visible, pairs talking: 30 seconds per pass.
4. Take finds one at a time and name the word: the home diary average reads 164/92 and the card says 146/92 (altered); the plan drops the repeat creatinine and potassium in 2 weeks (omitted); "Advise walking 30 minutes daily" is not on the card (invented).
5. The MISSING line under Assessment is not a fourth problem: the card gives no assessment, so that is the template working. You write it.

**If asked.**

- "Doesn't reading every line cancel the time saved?" Whether you save time is what you measured in Lab One, and you will measure again in Lab Two. The review is the job either way.
- "Can I try this on my real notes?" Not in a consumer AI tool: no patient identifiers, ever. Ask your institution which tool is approved.
- "Do I have to record that AI helped?" I cannot give legal advice. Follow your institution's policy and ask its data protection officer or legal team.

**Watch for.**

- Finding all three quickly feels like mastery. There is no announced count in clinic; say so.
- Reviewing against memory of the visit instead of against what you wrote down.
- A fluent note that gets skimmed: the smoother it reads, the faster the eye moves.
- Asking the tool to redo a flawed note instead of correcting it yourself. A new draft needs a new review.

**Bridge.** "That was a note written by prompting a chat assistant. In some Saudi clinics the prompt disappears: the tool listens to the consultation. Ten minutes on that."

## Topic 3 — Already live in Saudi clinics (10 min)

Page: [Module 4, section 3](../day2/m4-notes-and-audiences.qmd#saudi-scribes). Deck: kept `saudi-scribes` (last line replaced); new `read-the-numbers` and `scribe-questions`.

**Goal.** The room can say what an ambient scribe is, read the Sahl AI numbers correctly, and list what to ask before adopting one.

**Slides.**

1. `saudi-scribes` (kept; last line replaced). Headline: "Already Live in Saudi Clinics". On-slide text: "42.2/45: Sahl AI's pilot documentation-quality score. A bilingual Arabic-English ambient scribe piloted in Riyadh clinics."; "Augnito at Almoosa Health: an Arabic-capable ambient scribe, announced in 2025 for integration with the hospital's own medical records system."; last line, new: "Reported accuracy was 4.35 of 5, short of the maximum, so the note is still read line by line." Visual: unchanged, a dark stat card with the big teal number beside a white card with an indigo icon, the closing line in indigo below; add "pilot" to the first card's label. Notes: Say what the tool is before the numbers. An ambient scribe listens to the consultation and drafts the note; you do not supply the facts. Both examples ran inside institutions. Sahl AI, a Saudi-built Arabic-English scribe, was piloted in outpatient, inpatient and primary care clinics in Riyadh; the pilot was published in JMIR Medical Informatics in March 2026. Augnito's Omni AI Scribe, which covers Arabic dialects, was the subject of an agreement announced in January 2025 to integrate it with Almoosa Specialist Hospital's records system, in a phased rollout. As of September 2026; availability can change. Say piloted, and announced: not used everywhere.
2. `read-the-numbers` (new). Headline: "Reading the Numbers Like a Clinician". On-slide text: "42.2 of 45: modified PDQI-9, clinician-rated documentation quality"; "4.35 of 5: the accuracy domain"; "Not a comparison with prompting. Not patient outcomes." Visual: big-number pair on a dark card, teal numerals, beside two white cards, one marked "is", one marked "is not". Notes: Two numbers, one careful reading. 42.2 of 45 is a documentation-quality score on a modified version of the Physician Documentation Quality Instrument, rated by clinicians in a pilot. 4.35 of 5 is the accuracy domain alone. The pilot did not compare the scribe with prompting a general assistant, and it did not measure patient outcomes, so neither claim can be made from it. Do not turn the score into a percentage; it is a rating scale. Accuracy short of the maximum is the reason the note is still read line by line.
3. `scribe-questions` (new). Headline: "Before Your Clinic Adopts a Scribe". On-slide text: "Who reviews and signs the note? What happens on an error?"; "How are patients told, and how do they say no? Where are audio and text stored?"; "Which Arabic dialects, and switches to English? How does it connect to our records system?" Visual: three white cards with indigo numerals, two questions each. Notes: Six questions to put to the vendor and to your institution; they are questions, not legal conclusions. Who reviews and signs the note before it enters the record. What happens when it makes an error, and who hears about it. How patients are told and how they say no. Where the audio and the text are stored, for how long, and who can open them. Which Arabic dialects it covers, and what it does when the consultation moves between Arabic and English. How it connects to your records system. Health data is sensitive personal data under the PDPL, which SDAIA enforces. For what that means for your clinic, ask your institution's data protection officer or legal team. This is education, not legal advice.

**Say.**

- 0:00–1:30: "An ambient scribe listens to the consultation and drafts the note. A chat assistant needs you to supply the facts. Both examples sit inside institutions, and in both you read every line."
- 1:30–3:30: Sahl AI and Augnito, dated "as of September 2026". Augnito: an integration announcement, no accuracy figures.
- 3:30–6:00: the two numbers, then the vote (Do).
- 6:00–8:30: the six questions (Do).
- 8:30–10:00: a transcription app on your own phone is a consumer AI tool, and a recording of a consultation is patient information. Try the six questions on an app you downloaded: how many can you answer? "No patient identifiers into a consumer AI tool. Ever. Full stop." Day Three returns to this.

**Do.**

1. At 4:00, three statements; hands up for those the pilot supports, then ask what evidence each would need.
   - "Scribes are better than prompting a chat assistant." No: no comparison was made.
   - "Clinicians rated the notes 42.2 of 45 in a pilot." Yes.
   - "Patients did better." No: outcomes were not measured.
2. At 6:00 pairs choose their first two questions and name who at their institution could answer them.

**If asked.**

- "Is a scribe legal in my clinic?" I cannot give legal advice. The PDPL, enforced by SDAIA, treats health data as sensitive personal data. Ask your institution's data protection officer or legal team.
- "Which is better, Sahl AI or Augnito?" The sources behind this course do not compare them.
- "Where can I read the pilot?" *A Bilingual Arabic-English Ambient AI Scribe for Clinical Documentation: Prospective Evaluation Study*, JMIR Medical Informatics, March 2026; the link is on the Module 4 page. The abstract describes a prospective, single-arm pilot, with notes rated at a development stage and an implementation stage (the summary I found gives 64 and 55 notes; confirm on the paper before saying so). The two scores on the slides are the brief's: the paper's text was not openable when this was written, so read the abstract yourself before class. Do not quote beyond the two scores.

**Watch for.**

- **Replace the old slide's last line.** The existing `saudi-scribes` slide ends "Purpose-built tools already beat generic prompting for this exact complaint." The pilot did not compare against generic prompting, so that line is unsupported and must be replaced. Supported replacement: "Reported accuracy was 4.35 of 5, short of the maximum, so the note is still read line by line."
- **The title says "live", and the Augnito card says "integrated".** The sources say piloted (Sahl AI) and an announced agreement (Augnito: the 31 January 2025 press release says the scribe "will" be integrated, in a phased rollout, and describes deployment as still to come). Correct the slide's Augnito card too: "An Arabic-capable ambient scribe, announced in January 2025 for integration with the hospital's own medical records system." Confirm current status at both sites before class; until then, say "piloted" and "announced".
- The score turned into a percentage. It is a rating scale, not percent correct.

**Bridge.** "Whether the note comes from a prompt or a scribe, one clinical event still has to be told three ways: to the chart, to the patient, and to the colleague who takes over. That is the next 15 minutes."

## Topic 4 — Same note, three audiences (15 min)

Page: [Module 4, section 4](../day2/m4-notes-and-audiences.qmd#three-audiences). Deck: new: `three-audiences`, `source-of-truth`, `consistency-check`.

**Goal.** The room can write a source-of-truth sheet once, draw three outputs from it, and check that the constant facts agree.

**Slides.**

1. `three-audiences` (new). Headline: "One Event, Three Audiences". On-slide text: "Chart note: the clinical team"; "Discharge instructions: the patient, in plain language"; "Colleague letter: the community physician, focused". Visual: flow, one white card at left ("Case E, post-operative day 1") with three arrows to three cards at right, indigo and teal. Notes: One clinical event, three readers, and only the audience changes. The chart note is for the clinical team, in clinical register. The discharge instructions are for the patient, in plain language. The letter is for the community physician: focused, one page. On Day One the framework travelled across different documents and cases. Today the case stays the same and the skill is new: checking that the three outputs agree with each other. A patient told one thing while the letter says another is the failure we are guarding against.
2. `source-of-truth` (new). Headline: "Write the Facts Once". On-slide text: "One sheet: facts only, checked against the card"; "Three prompts draw on it; only the audience changes"; "Check the three outputs against each other". Visual: three-step flow with arrows, teal numerals, the last card tinted `#EEF2FF`. Notes: The sheet is the fix for drift. Three prompts that each start from memory will disagree in small ways. Three prompts that start from one checked sheet can be compared with it. The sheet is facts only, one per line, no prose: the procedure, how the patient is today, medicines and doses, activity limits, follow-up, and the return-sooner list. Check it against the card for invented, omitted and altered content before anything else. If a fact changes, change the sheet and run the prompts again. Correct a fact in the sheet, not inside one output.
3. `consistency-check` (new). Headline: "What Changes, What Must Not". On-slide text: "Changes: audience, register, length, vocabulary"; "Must not change: procedure, medicines and doses, activity limits, follow-up interval, return-sooner list". Visual: two-card before/after, a white "Changes" card beside an indigo-tinted "Must not change" card. Notes: The left card is what should differ between the outputs; the right card is what may not. Take the constant facts one at a time and read each across all three outputs. Procedure: the same operation, the same day. Medicines and doses: the same drugs, amounts, intervals and limits. Activity limits and wound care: the same numbers. Follow-up: the same interval. Return-sooner list: the same items, none added, none dropped. You supply that list; the tool words it. A tool that adds a warning you did not choose has made a clinical decision. If all three agree, say so: agreement is a result of the check, not a reason to skip it.

**Say.**

- 0:00–2:00, `three-audiences`: "Day One showed the framework on three different jobs. Today one event goes to three readers and only the audience changes. The new skill is checking that the three outputs agree."
- 2:00–5:00, `source-of-truth`: write the facts once, checked against the card for invented, omitted and altered. All three prompts draw on it.
- 5:00–9:00: across the prompts, ROLE and FORMAT change; the FACTS block is the same sheet. In the letter, name and file number stay a placeholder you add yourself.
- 9:00–14:00, `consistency-check`: read the constant facts across the three outputs, one cell at a time. You supply the return-sooner list; the tool words it.
- 14:00–15:00: "Agreement is a result, not a reason to skip the check." Bridge.

**Do.**

1. Before class: [Case E](../reference/case-cards.qmd#case-e) on screen. Run all four prompts once in the tool you will demo, save the outputs as a backup, and read them against the table so no mismatch is a surprise.
2. Run `source-of-truth-sheet` live. Check it against the card with Topic 2's two passes, reading medicines, intervals and the return-sooner list twice. Fix the sheet by hand: it is the only place a fact is corrected.
3. Put the ROLE and FORMAT lines of the three prompts side by side. Run `patient-instructions-from-sheet` live; show `chart-note-from-sheet` and `colleague-letter-from-sheet` from the backup.
4. Put the page's consistency table on screen: seven rows, three output columns. Pairs answer the page's question: with 30 seconds, which row first, and why? Then fill it aloud, return-sooner first; the room calls match or mismatch. On a mismatch, fix the sheet or the prompt and rerun that output.

**If asked.**

- "Why not one prompt that returns all three?" You can, but a wrong fact is then hard to trace and has no single place to fix.
- "Isn't the sheet as much work as the note?" It is facts only. You will time it yourself in Lab Two.
- "Can it write the patient version in Arabic?" It can draft; a fluent Arabic reader must check it before it reaches a patient.

**Watch for.**

- The patient version losing a limit: "if needed", "with food", "maximum 4 g in 24 hours".
- The letter asking the colleague for something that is not on the sheet.
- A fact fixed inside one output instead of the sheet; the next run brings it back.
- Time: three live runs will not fit. Run one, show two.

**Bridge.** "That was one story for three readers. The next reader is a room of colleagues: from a case to a slide deck."

## Topic 5 — From case to slide deck (8 min)

Page: [Module 5, section 1](../day2/m5-talks-and-teaching.qmd#case-to-deck). Deck: kept `case-to-deck`; new `deidentify-slides`.

**Goal.** The room can run the four-step flow on Case A, take identifiers out before the first paste, and check an outline against the card.

**Slides.**

1. `case-to-deck` (kept, unchanged). Headline: "From Case to Slide Deck". On-slide text: the four-step flow, "Case notes", "Structured outline", "AI slide draft", "Your edit and delivery"; and the line "Every step after the outline is faster with AI. The edit at the end is still yours." Visual: flow of four white cards with arrows, the last card tinted `#EEF2FF` with an indigo arrow. Notes: Four steps, two owners. Steps 1 and 4 are yours: the case notes, de-identified, and the edit and delivery. Steps 2 and 3 are the tool's draft, which you check: the outline, then the slide text. Whatever you paste at step 1 is inherited by everything after it, so step 1 is where identifiers come out. The slide says every step after the outline is faster with AI. Whether it is faster for you is what you timed in Lab One; do not promise a saving. The edit at the end is still yours.
2. `deidentify-slides` (new). Headline: "Take Identifiers Out First". On-slide text: "No name, ID, file number, phone, or exact date"; "No scan, ECG, or screenshot with a name on it"; "Rare combinations of detail can identify: when in doubt, use a card". Visual: three white cards in a row, indigo "no" icons, one line each. Notes: The privacy line: No patient identifiers into a consumer AI tool. Ever. Full stop. For a teaching slide it covers two things: the prompt that builds the slide, and the slide itself. Leave out names and initials, file, ID and phone numbers, dates of birth, exact dates (write 6 weeks ago, not the calendar date), and any combination of details rare enough to point to one person. Images need more care than text: a face, a tattoo or a distinctive scar identifies someone even with the caption removed, and a scan or ECG may carry a name in the corner. Your institution's policy on teaching material comes first. Day Three returns to this.

**Say.**

- 0:00–1:30, `case-to-deck`: four steps, two owners. "Steps 1 and 4 are yours. Everything after step 1 inherits what you pasted, so identifiers come out first."
- 1:30–3:30, `deidentify-slides`: what to leave out; images need more care than text; your institution's policy comes first.
- 3:30–6:30: the `case-outline` prompt on Case A: Day One's four parts, plus your teaching points in your words and a cap on the outline. Read the outline against the card for invented, omitted, altered. Omission is fine when you chose it, a problem when the tool chose it and the talk depends on it.
- 6:30–8:00: "The edit at the end is still yours." Bridge.

**Do.**

1. Before class: [Case A](../reference/case-cards.qmd#case-a) and `case-outline` ready; run once beforehand as a backup.
2. At 3:30 paste the card under FACTS and these teaching points: compare what the patient says with what the diary and the clinic show; record what is new since the drug was started; build the next checks into the plan. Run it.
3. Room check, two minutes: tick every number against the card, then name one thing the outline left out (the father's stroke is a candidate) and say whether you would have left it out too.

**If asked.**

- "Can I put a real patient's scan on a slide?" An image can identify even with the caption removed. Your institution's consent and image policy decides; ask its data protection officer or legal team. I cannot give legal advice.
- "The name is removed, so is it de-identified?" It is one step. A combination of rare details can still point to one person, so de-identification is a judgment, not a guarantee. When in doubt, use a fictional case.
- "Can the tool build the slide file itself?" Some can, and features change often. The rule is the same in all of them: you check the text.
- "Do I tell the audience AI helped?" Follow your institution's or the meeting's policy; ask them.

**Watch for.**

- An outline that gains a learning objective, guideline or extra medicine the card does not contain.
- Treating the outline as finished. It is step 2 of 4.
- A promised time saving. Give no number; the room timed its own in Lab One.
- A doctor pasting a real case "just this once". Privacy line, then the card.

**Bridge.** "An outline gives you the order. A talk needs the words, a line to say and a picture for each slide. Next 12 minutes: where the numbers on a chart become your responsibility."

## Topic 6 — Building a full talk, not just an outline (12 min)

Page: [Module 5, section 2](../day2/m5-talks-and-teaching.qmd#full-talk). Deck: new: `full-talk`, `slide-qa`.

**Goal.** The room can turn an approved outline into slide text, one speaker note and one visual idea per slide, and check the result before anyone else sees it.

**Slides.**

1. `full-talk` (new). Headline: "One Level Past the Outline". On-slide text: "Slide text: a title and at most three short lines"; "One line of speaker notes"; "One visual suggestion: what to show, not the picture". Visual: three white cards in a row with indigo and teal icons (text, speech, chart), one line each. Notes: The outline gave you the order. Now ask for exactly three things per slide: the slide text, one line of speaker notes, and one visual suggestion. The short list is the discipline. Ask for a full slide and you may get paragraphs, a supporting statistic and a source line, and all three become yours to verify. Ask for three things and you have three things to check. The prompt also asks for a numbers ledger: every number on the slides with the fact it came from. It is a list for you to tick, not proof.
2. `slide-qa` (new). Headline: "Slide Check, Once Per Slide". On-slide text: "Every number and every chart value matches the source"; "No identifiers, on the slide or in the image"; "Every claim sourced, one idea per slide". Visual: one white card holding three unticked checkboxes with indigo outlines, large type. Notes: Run this once per slide before anyone else sees it. Numbers: digit by digit, value, unit, side, and which reading it belongs to. Tick against the card, not against the tool's own ledger. Identifiers: no name, file number, exact date, or image that shows a face or a name. Claims: each has a source you can name or is your own statement; delete any citation, statistic or guideline the tool added. One idea per slide, three lines at most. Every chart uses only values you supplied. The tool suggests the picture; the numbers come from you and the source.

**Say.**

- 0:00–1:30, `full-talk`: "The outline gave you the order. The hours go into the words, what you will say, and the picture, and a tool has the most room to add things you did not ask for."
- 1:30–5:00: `full-talk-slides`: exactly three things per slide, each capped. The FORMAT block does the work. Read slide 2 of the page's illustrative output.
- 5:00–8:00: the trap. "Which points would a chart of the home diary plot?" Case A gives only the two-week average, so daily values would be made-up. The numbers come from you and the source, never from the tool.
- 8:00–11:00, `slide-qa`: pairs run the check (Do).
- 11:00–12:00: change one slide at a time. "Make it more convincing" invites a statistic, a guideline name or a "Source:" line, and the tool cannot know whether any is real.

**Do.**

1. Before class: [Case A](../reference/case-cards.qmd#case-a), the approved three-slide outline from Topic 5, and `full-talk-slides` ready; a backup output saved.
2. At 1:30 run it with the card under FACTS and the outline under OUTLINE.
3. At 5:00 ask the room to find the VISUAL line that respects the missing daily values.
4. At 8:00 pairs swap screens and run the slide check on the other's three slides. Each reports one finding: a number that does not match, something not on the card, or "clean".
5. Ask: "If a slide is wrong, how do you ask for the fix?" One slide only, and say what to change.

**If asked.**

- "Can it draw the actual chart?" Some tools can. The rule is the same: the values come from you and the source; check every axis and label.
- "Can it add references to the slides?" It can produce ones that look real and are not. A citation you did not open is not a citation: question 2. Delete it or find the original yourself.
- "Can I paste a colleague's slides or a published figure?" Only material you are allowed to share with a third-party tool. Ask your institution.

**Watch for.**

- A visual suggestion treated as data. If a tool draws a line of daily readings, every point on it is made-up.
- Slide text that grows past three lines, or a statistic nobody asked for.
- The ledger treated as proof. Tick against the card.
- Asking for the whole deck again: it can change slides you already checked.

**Bridge.** "You have been the presenter. Now the teacher: the same tool writes quiz questions, with one habit worth knowing."

## Topic 7 — Teaching with AI (8 min)

Page: [Module 5, section 3](../day2/m5-talks-and-teaching.qmd#teaching-with-ai). Deck: kept `teaching-ai`; new `mcq-habit`.

**Goal.** The room can get quiz questions from a source they may share, and can check whether the correct answers are balanced by position and length.

**Slides.**

1. `teaching-ai` (kept; first card optionally reworded). Headline: "Teaching With AI". On-slide text: "Quiz questions from a guideline or paper, checked against the source"; "Study summaries, the same length discipline as note-writing"; "Useful for the residents and students you supervise". Visual: three full-width white cards, alternating indigo and teal icons, 30px semibold. Optional reword of the first card: "Quiz questions from a source you may share, checked against it". Notes: Three uses. Quiz questions written only from a source you paste, then checked against that source. Study summaries with the same discipline as a note: a fixed shape, a word limit, numbers copied exactly, and you read every line before a trainee does. Supervising: when a trainee brings an AI draft, ask to see the prompt and the source, and run the three-question check together. The first card says guideline or paper. Add the caution aloud: paste only material you are allowed to share with a third-party tool. A published paper is not automatically yours to paste.
2. `mcq-habit` (new). Headline: "The Habit to Check". On-slide text: "The correct answer tends to sit in the same position"; "It tends to be the longest option"; "Ask for balance, then check that it happened". Visual: before/after, left a row of five answer letters with four highlighted at C, right the fix in words; indigo and teal on white cards. Notes: A real weakness to check for. Tools that write multiple-choice questions tend to put the correct answer in the same position, and to make it the longest option. Both let a learner pass by guessing a letter or picking the longest option, without reading the source. So the prompt asks for balanced positions and option lengths, and then you check that it happened: read the answer letters, and find the longest option in each question. Check the rewritten questions against the source again, because a rewrite can change a fact.

**Say.**

- 0:00–1:30, `teaching-ai`: three uses, one line each: quizzes from a source you may share, summaries with the note discipline, supervising trainees.
- 1:30–3:00: "only from this text." Paste the source and tell the tool to use nothing else, so every question has an answer on the page in front of you. Only material you may share; your own teaching notes usually qualify; if unsure, ask your library or legal team.
- 3:00–6:30, `mcq-habit`: run the prompt, then count (Do).
- 6:30–8:00: the fix in plain words, then check the rewrite against the source again.

**Do.**

1. Before class: the [practice source](../reference/practice-source.qmd) open; `quiz-from-source` ready; a backup output saved.
2. At 3:00 run it with the nine lines of Protocol HBP-1 under SOURCE. Keep this quiz open: Topic 8 uses it.
3. Room check: read ANSWER LETTERS; does one letter carry most answers? Find the longest option in each question; is it the correct one more than once or twice?
4. If it balanced, say so and do not manufacture a failure. Show the page's deliberately unbalanced example as what the check is for.

**If asked.**

- "Can I paste a paper or guideline?" Only if you may share it with a third-party tool; its terms and your institution's policy decide. If you do not know, do not paste. I cannot give legal advice.
- "Can it mark my residents' answers?" It can draft feedback against a rubric you supply. You decide the grade and what the trainee hears.
- "Are these good enough for a real exam?" They are first drafts. The tool cannot tell you whether a question is fair; the next topic covers checking the key.
- "Can it write case-based questions?" It can draft fictional cases. You check every value, the logic and the key.

**Watch for.**

- The prompt already asks for balance, so a live run may pass. Check anyway; do not assume.
- A rewrite that fixes the letters but changes a fact.
- A trainee pasting a real note "just to tidy it". Privacy line.
- Questions asked for from general memory: a wrong question reads exactly like a right one.

**Bridge.** "The questions are checked against the source. The key is the part people forget, because a wrong key looks like an authority. Seven minutes on grading yourself."

## Topic 8 — Grading yourself (7 min)

Page: [Module 5, section 4](../day2/m5-talks-and-teaching.qmd#grading-yourself). Deck: new: `grade-yourself`, `key-vs-source`.

**Goal.** The room can ask for an answer key with a quotation for every answer, and spot-check the riskiest line against the real source.

**Slides.**

1. `grade-yourself` (new). Headline: "Grade the Key Before It Grades Anyone". On-slide text: "Ask for the key with a quotation for every answer"; "Check the riskiest question against the real source"; "If that check fails, the rest is unchecked, not fine". Visual: three-step flow with arrows, teal numerals, the last card tinted `#EEF2FF`. Notes: A quiz is an assessment. If its key is wrong, a trainee who answered correctly is marked wrong. The tool writes a wrong key line in the same confident voice as a right one, so "does this look right" is not a test. Ask for the key in the same conversation as the questions, with the exact words from the source that make each answer correct. A quotation turns "is this answer right" into "does this line say that", which you settle with the page open. Then check the riskiest question first: the one with a number, an exception, a threshold or a negation. If that check fails, the rest is unchecked, not fine.
2. `key-vs-source` (new). Headline: "Key Versus Source". On-slide text: "The key, question 3: A, all readings from days 1 to 7. \"Average all readings.\""; "The source, line 6: \"Discard the readings from day 1. Average all remaining readings.\""; label: "Illustrative key line, written for this course". Visual: before/after, a white "The key says" card beside a dark `#0F172A` "The source says" card with the dropped words in teal. Notes: The quotation is what lets you catch this. The key line is illustrative, written for this course. Question 3 asks which readings are averaged. The key says all readings from days 1 to 7 and quotes "Average all readings." Open the real source, not the tool's copy. Line 6 reads: "Discard the readings from day 1. Average all remaining readings." The key's quotation is not in the source. It is a shortened version that drops the discard, and the key's answer follows it. Questions 1 and 2 may match their lines, but the key has just shown it can be confidently wrong, so they get checked, not assumed.

**Say.**

- 0:00–1:00, `grade-yourself`: "A wrong key marks the right trainee wrong, in the same confident voice as a right one. 'Does this look right' is not a test."
- 1:00–2:30: `answer-key-with-quotes`: same conversation as the questions, exact words inside quotation marks, the line where they appear, NOT SUPPORTED when nothing supports an answer.
- 2:30–5:30, `key-vs-source`: the spot-check. Riskiest question first. The real page, not the tool's copy or its quotation. Three things: the quotation appears word for word, says what the key claims, and supports the letter given. If it fails, the rest is unchecked.
- 5:30–7:00: the three questions, then "If the answer to any of these is no, that's the signal to slow down, not the finding to accept." Bridge.

**Do.**

1. Before class: the Topic 7 quiz open; the [practice source](../reference/practice-source.qmd) in a second window; `answer-key-with-quotes` ready.
2. At 1:00 run it on the live quiz. Ask which question is riskiest: the one with a trap, such as the day-1 discard or the two thresholds.
3. At 2:30 spot-check that line: read the quotation aloud, a volunteer finds it in the source. Pass or fail?
4. Then show the page's illustrative key and run the check on question 3: the quotation is not in the source. Ask what you now do with the other questions: check each, or discard the set.

**If asked.**

- "Isn't it enough to check everything?" If you have time, yes. The spot-check is the minimum, and it tells you what to do when the minimum fails.
- "How can a quotation be wrong if it came from the source?" It can be shortened, altered or from the wrong line, as here. Check it word for word in the real source.
- "Can a second tool check the first one's key?" It can point you at lines to look at. Agreement between two tools is not a source.
- "What if the source itself is wrong?" Then the key is faithful to a wrong source. Check against the guideline or label you trust.

**Watch for.**

- Checking the tool's copy of the source, or its quotation, instead of the real page.
- "It passed, so the rest is fine." A pass verifies one line; the quotations only make the others quick to check.
- A quotation that is nearly right: shortened, or one word changed.
- Running long. The spot-check is the point; the discussion is optional.

**Bridge.** "That is Day Two's toolkit: notes, three audiences, talks and teaching. After the 10-minute break, Lab Two puts it together: one case, three outputs."

## Lab 2 — facilitation

Page: [Lab 2](../day2/lab2-one-case-three-outputs.qmd), parts [1](../day2/lab2-one-case-three-outputs.qmd#part-1), [2](../day2/lab2-one-case-three-outputs.qmd#part-2) and [3](../day2/lab2-one-case-three-outputs.qmd#part-3). 35 minutes, 1:25 to 2:00. Deck: kept `lab2` (text replaced); reuse `consistency-check` from Topic 4 on the projector during part 1, step 3.

**Goal.** Each participant leaves with a sheet they checked, three outputs and a grid showing whether they agree, a second tool comparison on a Day Two task, and one round of the three-question check on a peer's output.

**Slides.**

1. `lab2` (kept id; text replaced). Headline: "Lab Two". On-slide text: "Part 1: One case, three outputs (20 min)"; "Part 2: Tool check, again (10 min)"; "Part 3: Share-out (5 min)". Visual: unchanged full-bleed teal `#14B8A6`, "Hands-On" eyebrow in `#CCFBF1`, large white "Lab Two", the three parts in `#F0FDFA` under the title. Replace the old line "Turn one real case into a three-slide outline, or one paper into five quiz questions. Your choice.": this course never uses a real case, and the lab has no such choice. Notes: Lab Two is one case, three readers. Part 1, twenty minutes: build one source-of-truth sheet from a case card, check it against the card, draw a chart note, a patient handout and a three-slide teaching version from it, then fill in the consistency grid. Part 2, ten minutes: repeat Day One's tool comparison on a Day Two task. Part 3, five minutes: pairs present one output and we apply the three-question check together. Case cards only. The privacy line applies to every prompt you paste.

**Before class.**

- Case cards and the [practice source](../reference/practice-source.qmd) open on the projector; a visible countdown timer.
- Every participant has a general assistant and Vera Health or the literature-grounded tool from [setup](../setup.qmd). Anyone without one pairs with a neighbor and shares a screen.
- Run all of part 1 on Case A yourself, grid filled in, so you know what a mismatch looks like and can show a backup set if a tool goes down.
- The two grids and the worksheet at the end of the page, on paper or in a notes app.

**Say.**

- Part 1, min 0: "One case, three readers, one sheet. Build the sheet and fix it yourself before anything else. No patient identifiers into a consumer AI tool. Ever. Full stop. Cards only."
- Part 1, min 14: "Now: do the three outputs agree? Go to the sheet and the card, not to whichever output reads better."
- Part 2, min 0: "Same comparison as Day One, new task. Compare what you can see: stayed inside the text, added anything, cited something you could open, every number copied exactly."
- Part 3, min 0: "Pick the one output you would least want to be wrong. The handout is a good candidate, because a patient will act on it."

**Do.**

1. Part 1 (1:25), min 0 to 4: walk the room and confirm each person checks the sheet against the card line by line. This step decides the rest.
2. Min 4: "New chat for each output." Min 9: "Second output by now." Min 12: "Take what you have and move on."
3. Min 14: `consistency-check` on the projector. Ask anyone with an all-ok grid to show you where the follow-up interval sits in the handout. Pick three pairs for part 3: one with a mismatch, one whose handout added content, one clean.
4. Part 2 (1:45): default task is the study summary, `teaching-summary-from-source`, on the practice source. Min 1 to 5 both tools, 5 to 9 the table, 9 to 10 the two closing lines.
5. Part 3 (1:55): min 0 to 1 pairs choose their output; min 1 to 4 call two or three pairs, each shows the output beside the sheet, reads two lines and names one fact checked and where, then the room asks the three questions aloud and the pair answers; min 4 to 5 everyone writes one thing to change, in the sheet or the prompt.

**What good looks like.**

- The sheet was fixed before any output existed.
- Every dose, interval and reading is identical wherever it appears, copied from the sheet.
- Where the card is silent an output says [MISSING: ...] or says nothing.
- Every grid cell has a mark. A grid with no mismatch is a good result if they checked.
- Part 2 compares observable things, and the "because" names something they saw.
- In the share-out the presenter names a specific fact and where they checked it, not "it looked fine", and a "no" comes with a next step.

**Common problems and fixes.**

- A real case appears. Stop, use a card. If something identifiable was already pasted into a consumer AI tool, they tell their institution's data protection officer or legal team; Day Three covers it.
- Tool slow or quota gone: pair up, do the sheet and two outputs, and show your backup set.
- The sheet is prose or longer than the card: facts only, one per line.
- The handout contains a return-sooner list: Case A names none, so it did not come from the card. Delete it or replace it with one they write.
- Two outputs disagree: sheet and card decide. Ask whether the sheet was the source, fix it there, rerun that output in a new chat.
- A tool will not take the pasted text or answers from its own sources: they write it down. It is a result, not a failure.
- Fast finishers: another card through the same three prompts, or a handout in Arabic for a card with an Arabic preference (C or D), which a fluent Arabic reader must check.

**If asked.**

- "Why a new chat for each output?" An error in one cannot leak into the next, and each draws on the sheet, not on the others.
- "Why not OpenEvidence?" As of September 2026 it requires US NPI verification and withdrew from the EU and UK in April 2026, so it is not usable for a Saudi audience. Vera Health verifies healthcare professionals globally.
- "Which tool won?" That is not the result. The four questions in the table are.
- "Can I use my own case?" A case card is safer. If you bring one, apply the [privacy checklist](../reference/privacy-checklist.qmd) first; when in doubt, use a card.

**Watch for.**

- Skipping the sheet check to reach the outputs faster: the commonest failure.
- Judging by fluency: "this one reads better."
- A grid full of "ok" nobody looked at.
- Part 2 turning into a brand debate. Point at the table.
- Losing part 3. Protect five minutes; cut part 2's second task first.

**Debrief prompts.**

- Which fact was hardest to keep still across the three outputs?
- Did the sheet itself turn out to be the source of an error?
- Which output would you send without one more read? (The answer the rule expects: none.)
- What did the second tool do differently, and what would you use each for?

**Bridge.** "Tomorrow is Day Three: what goes wrong, and what never goes in. Bring the Lab One output you saved, which Lab Three uses, and one output from today, which the session Back to the rule uses."
