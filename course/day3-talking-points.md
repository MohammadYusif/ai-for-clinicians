# Day Three — Safety & Ethics: talking points

Instructor script for the 120-minute day. Topic numbers follow `course/timing.json`; item 6 is the 10-minute break and has no block. Clock cues inside a topic count from that topic's start; the line under each heading gives the day clock. Deck status is `new` or `kept` with the slide id. Speaker notes are plain text of at most 900 characters, ready to paste. The two Lab Three backup examples and their answer keys live only in this file (see "Lab 3 — facilitation"): never in the deck notes, never on the participant page.

Day clock: 0:00 Topic 1 · 0:10 Lab Three (Topic 2–3) · 0:35 Topic 4 · 0:45 Topic 5 · 1:00 break · 1:10 Topic 7 · 1:30 Topic 8 · 1:50 Topic 9 · 2:00 end.

Say four things in exactly these words, every time they come up. The rule: "AI drafts. You decide." The three-question check: "Could I defend this to a colleague? Does it point to something I can verify? Would I catch it if it were wrong?", followed by "If the answer to any of these is no, that's the signal to slow down, not the finding to accept." The privacy line: "No patient identifiers into a consumer AI tool. Ever. Full stop." The error words: invented, omitted, altered.

Facts still to settle before the day are marked [TRAINER TO CONFIRM: ...], mostly in Topics 8 and 9.

## Topic 1 — Confidently wrong (10 min)

Participant page: [Module 6](../day3/m6-confidently-wrong.qmd#confidently-wrong). Day clock 0:00–0:10. Deck status: kept `day3-divider` and `confidently-wrong`; new `verify-five-moves` and `source-ladder`.

**Goal**: By the end, everyone can say why a confident tone proves nothing and can name the five verification moves, which is all Lab Three needs.

**Slides**

1. `day3-divider` (kept)
   - Headline: Safety & Ethics
   - On-slide: Day Three · Safety & Ethics · Verification, privacy, and the final assessment.
   - Visual: existing dark divider, `#0F172A` ground, large indigo "03", gradient diamond at right. No change.
   - Notes: Welcome to Day Three. Days One and Two were about getting good output. Today is about the two ways output hurts a patient: it is wrong and nobody notices, or it is right and it should never have left your hands. Three parts: how to check what a tool tells you, the privacy rule that is not optional, and a group check of your own work from this weekend. Ask who has the Lab One output open, the one with the PRACTICE OUTPUT line at the top, and who does not; a fresh one takes two minutes. After the break we also use one output from Days One or Two, so keep those open.
2. `confidently-wrong` (kept)
   - Headline: Confidently Wrong
   - On-slide: "AI states things in the same tone whether it's right or wrong. Tone is not a signal. A verification step is." · flow: Draft with AI, Cross-check the source, Confirm or correct, Use.
   - Visual: existing light slide (`#FBFBFD`), 72 px title, one-line claim, four-card flow with the last card ("Use") tinted `#EEF2FF`. No change.
   - Notes: Recall Day One: the tool predicts likely words, and likely is not the same as true. When it is wrong it writes in the same calm tone as when it is right, so tone tells you nothing. The only signal is a step you do yourself between the draft and the use. Say made-up or fabricated for false content; the word you will hear elsewhere is hallucination, same thing. Name the three ways clinical text goes wrong: invented, omitted, altered. Then say: the arrow between draft and use is where you work, and the next slide makes it something you can do in minutes.
3. `verify-five-moves` (new)
   - Headline: Five moves, every time
   - On-slide: (1) five-card flow: Extract every checkable claim · Find each source yourself · Mark: confirmed, wrong, could-not-find · Fix it or discard it · Name the error. (2) "Could-not-find counts as wrong."
   - Visual: light slide. Five white cards in a row (border `#E2E5EA`, indigo numerals 1 to 5, DM Sans), card 3 tinted teal `#CCFBF1`. Below, one indigo pill with the last line.
   - Notes: This is the whole method, and Lab Three uses only this. One, pull out every claim you could check: numbers, names, citations, dates, doses, guideline references. Two, find each source yourself; do not ask the tool to confirm itself. Three, mark each claim confirmed, wrong, or could-not-find, and treat could-not-find as wrong. Four, fix it in the document or discard the output. Five, name the kind of error: invented, omitted, altered, or a fabricated citation. The card adds one pass inside move three: read the source against the output once, for what was left out. Then run the Case A worked example from the page.
4. `source-ladder` (new)
   - Headline: Where the truth lives
   - On-slide: (1) ladder: The primary source: the guideline, label or paper itself > Your institution's formulary or guideline > A second AI is not a source. (2) Stakes: Wording, low. Summaries, medium. Doses, allergies, diagnoses, anything in a chart: the primary source, always. (3) "Asked it for citations? Open every one."
   - Visual: light slide, two columns. Left: three-rung ladder, top rung filled indigo, middle white, bottom rung struck through in muted red. Right: three-row table (Stakes, Check) with a thin teal bar growing from low to full. Footer pill in indigo carries item 3.
   - Notes: Where you look matters as much as whether you look. Best is the primary source: the guideline, the drug label, the paper itself. Next is your institution's formulary or guideline, which is what colleagues will hold you to. A second AI is not a source: two tools agreeing is two predictions, not a check. Asking a tool for citations does not fix this, because citations can be fabricated. Open every one and read the line it is supposed to support. Effort scales with stakes. Wording, low. Summaries, medium. Doses, allergies, diagnoses and anything in a chart: always the primary source.

**Say**

- 0:00–0:45, `day3-divider`. Frame the day: output hurts a patient two ways, wrong and unnoticed, or right and never meant to leave your hands. Verification first, then privacy, then your own work. Hands: who has the Lab One output open?
- 0:45–3:00, `confidently-wrong`. Same tone, right or wrong; that is how the tool writes, not a fault waiting to be fixed. Tone is not a signal; a step is. Name the three failures: invented, omitted, altered.
- 3:00–6:30, `verify-five-moves`. A claim is anything a colleague could answer with "says who?" Walk the five moves, then the Case A worked example. Stress move 3, then the card's extra pass: read the source against the output once, for what was left out.
- 6:30–9:00, `source-ladder`. Poll: "A second tool agrees with the first. Verified?" Then citations, then stakes.
- 9:00–10:00. Point to the verification card at the end of Module 6. "Lab Three uses nothing else."

**Do**

1. Before class: Module 6 open on a second screen, the Case A card beside its worked example.
2. At 3:00, the room calls out every checkable claim in the Case A summary, then marks each against the card. Key: "headaches more frequent" and "review in 6 weeks" are altered (the card says less frequent, and 4 weeks); "follows current guidelines" is could-not-find; the omission is the repeat creatinine and potassium in 2 weeks.
3. At 6:30, run the poll.

**If asked**

- Can the tool check its own answer? It can list claims (the claim-list prompt on the page). It cannot be the check: it re-reads its output with the habits that produced it.
- How often is it wrong? No number would apply to your tool on your task, so quote none. The Sahl AI pilot reported 4.35 of 5 for accuracy, clinician-rated: short of the maximum, so notes are still read line by line.
- Does a literature-grounded tool solve this? It gives you something to open. You still open it and read the line it supports.

**Watch for**

- "It has citations" heard as "verified"; could-not-find drifting into "probably fine."
- Pairs planning a second tool "to double-check". Redirect to the ladder.
- Running long: cut the ladder to one minute before shortening the lab.

**Bridge**: "You have five moves and a card. Now see whether they catch an error you did not plant: swap your Lab One output with a neighbor."

## Topic 2–3 — Lab Three, parts 1 and 2: trade and catch, then instructor examples (25 min)

Participant page: [Lab Three](../day3/lab3-spot-the-error.qmd), [part 1](../day3/lab3-spot-the-error.qmd#part-1) and [part 2](../day3/lab3-spot-the-error.qmd#part-2). Day clock 0:10–0:35. Deck status: new `lab3`, `lab3-example-a`, `lab3-source-a`, `lab3-example-b`, `lab3-source-b`. The minute-by-minute, the two backup examples and their answer keys are in "Lab 3 — facilitation" at the end of this file. None of that is on the participant page.

**Goal**: By the end, each doctor has run the five moves on an output they did not write and can name the habit that would have caught the error faster.

**Slides**

1. `lab3` (new)
   - Headline: Lab Three: Spot the Error
   - On-slide: (1) Part 1, 15 min: swap the output you saved in Lab One and check it, cold. (2) Part 2, 10 min: instructor examples, together. (3) Your only tools: the five moves and the verification card.
   - Visual: light slide. Two cards side by side with badges "15 min" (indigo) and "10 min" (teal); item 3 as an indigo pill underneath.
   - Notes: Launch the lab. Swap your Lab One output with a neighbor; the PRACTICE OUTPUT line at the top marks it as unreliable, so it is safe to trade. Do not say what you found in Lab One. Check cold with the verification card: extract the claims, find each source yourself, mark each claim, name the error. Do not ask any tool whether the output is right. Record as you go. Nine minutes to check, three to compare, two to write what would have caught it faster. If you saved no output, run a fresh probe from Lab One's menu now and add the warning line.
2. `lab3-example-a` (new)
   - Headline: Example A: practice output
   - On-slide: (1) PRACTICE OUTPUT: CONTAINS DELIBERATELY UNRELIABLE CONTENT. NOT FOR CLINICAL USE. (2) The Example A text, exactly as in "Lab 3 — facilitation". (3) "Everything here is fictional."
   - Visual: light slide. Warning line in a muted-red pill across the top; the text in one white card (`#E2E5EA` border), DM Sans at 26 px or larger; footer line in slate `#475569`.
   - Notes: Everything on this slide is fictional. Give one minute to read and list every checkable claim on paper, then one minute to read the text against itself: do its parts agree with each other? Call out any disagreement, not the answer. Do not show the source card yet. If someone announces an error early, ask which step found it and let them hold it for the call-it round.
3. `lab3-source-a` (new)
   - Headline: Source card A
   - On-slide: (1) "The only documents that exist for this exercise." (2) The card text, exactly as in the facilitation section. (3) "Mark each claim: confirmed, wrong, could-not-find."
   - Visual: same layout as `lab3-example-a`; the card tinted `#EEF2FF` so it reads as a source; item 3 as a teal pill at the bottom.
   - Notes: This card lists the only documents that exist for this exercise. Check each claim against it and mark it confirmed, wrong or could-not-find. Anything not on the card is could-not-find, and could-not-find counts as wrong. Then call it: for each finding, the claim, how you would confirm it, and the kind of error. Reveal by asking, not telling, then give the key. Have the key in hand; it is not on the slide.
4. `lab3-example-b` (new)
   - Headline: Example B: practice output
   - On-slide: as `lab3-example-a`, with the Example B text.
   - Visual: as `lab3-example-a`.
   - Notes: Same routine as Example A, and fictional throughout. One minute to list, one minute to read the text against itself, then the source card. Ask the room what they would do at work with a reference they cannot find.
5. `lab3-source-b` (new)
   - Headline: Source card B
   - On-slide: as `lab3-source-a`, with the Source card B text.
   - Visual: as `lab3-source-a`.
   - Notes: Same routine as Source card A. Reveal by asking: which error needed no source at all, and which needed the card? What is the difference between a claim that is wrong and one you could not find? At work the answer is the same for both: it does not go into the document as it stands.

**Say**

- 0:00–1:00, `lab3`. Launch and swap. "You did not write it, so read it the way a colleague would. Do not say what you found in Lab One. The card, a source you find yourself, nothing else." Odd number: one trio, pass outputs around. No output: a fresh probe from Lab One's menu, warning line on top.
- 1:00–10:00, check cold. Circulate and ask each pair: "Show me your claims list." "Where did you look: a source, or another tool?" "What is marked could-not-find, and what did you do with it?" Time calls at 4:00 ("claims listed, sources next") and 8:00 ("mark, fix or discard, name the error").
- 10:00–13:00, compare. Swap back. Where findings differ, each says how they checked. The disagreements are the useful part.
- 13:00–15:00, reflect. "What would have caught it faster?" on paper, two answers aloud, habits on the board.
- 15:00–25:00, Part 2. The page's routine: read and list (1), check (4), call it (3), score yourself (2). With two examples each gets half and the last minute is the debrief. Script, texts and keys: "Lab 3 — facilitation".

**Do**

1. Before class: slides loaded, a visible timer, the facilitation section open on your own screen, not projected.
2. At 0:00 start the 15-minute timer and let pairs form.
3. While circulating, note two good marks and one error type for the debrief.
4. At 15:00, choose: one example at the page's full timings, or two at half each. Run two when the room is quick or Part 1 surfaced little.

**If asked**

- Can I use an AI to help me check? Not to decide what is true. The page's rule: do not ask a tool whether the output is right. A tool may help list claims; a second tool is not a source.
- What if I cannot find a source? That is the result: could-not-find, treated as wrong. Say which source you would go to.
- Nothing seems wrong. Did we fail? Not necessarily. List what you confirmed and where. A clean result you cannot show is not yet a clean result.
- The tool refused, or hedged. Note what it said it could not do, then swap for an output that is not a refusal. See "Common problems".

**Watch for**

- Reading for sense instead of extracting claims: nobody has a written list.
- A "confirmed" with no "where", or a source that is another AI.
- The dip at 15:00. Hold Part 2 to the page's clock.

**Bridge**: "You have felt what the habit costs and what it catches. The other way this goes wrong never looks like an error: the output is right and the input was the problem. That is Module 7."

## Topic 4 — The rule that isn't optional (10 min)

Participant page: [Module 7](../day3/m7-privacy.qmd#the-rule), with the [privacy checklist](../reference/privacy-checklist.qmd). Day clock 0:35–0:45. Deck status: kept `privacy-rule` (one wording fix); new `identifier-floor`, `deidentify`, `formats-that-leak`.

**Goal**: By the end, everyone can say the privacy line, say what the law does and does not tell them in three sentences, and de-identify a sentence and re-read it as a stranger.

**Slides**

1. `privacy-rule` (kept; one wording fix)
   - Headline: No patient identifiers into a consumer AI tool. Ever. Full stop.
   - On-slide: (1) eyebrow: The Rule That Isn't Optional. (2) the privacy line. (3) "Saudi Arabia's Personal Data Protection Law, enforced by SDAIA, classifies health data as sensitive personal data, with real financial and operational penalties for mishandling it."
   - Visual: existing dark slide, `#0F172A`, soft-red eyebrow (`#FCA5A5`), centered 70 px headline, muted blue-grey body. Only the body sentence changes: the deck says "Saudi's" and omits "enforced by SDAIA"; fix both to match the course wording.
   - Notes: Read the line aloud with the room. A consumer AI tool is a general assistant you signed up for yourself. An approved tool is one your institution has vetted and contracted. The law: Saudi Arabia's Personal Data Protection Law, enforced by SDAIA, classifies health data as sensitive personal data, alongside genetic and biometric data, with real financial and operational penalties. That is all the course says about it: no article numbers, no fine amounts, no legal conclusions. For what applies to you, ask your institution's data protection officer or legal team. This is education, not legal advice.
2. `identifier-floor` (new)
   - Headline: A floor, not a ceiling
   - On-slide: (1) Name · ID or iqama number · file number · phone · address · exact date of birth · exact dates · photograph. (2) Any combination of details rare enough to point to one person. (3) The test: can a person be identified, directly or indirectly?
   - Visual: light slide. The eight identifiers as white chips in two rows, item 2 as an indigo pill under them, item 3 in one large teal-tinted card on the right.
   - Notes: This list is a floor, not a ceiling. The real test is whether a person can be identified, directly or indirectly, from what you paste: by a colleague, a neighbor or the family. Any one detail can look harmless; together they can point to one person: a rare condition, a small town, a date. Exact dates count, not only birth dates. Photographs count, including any image with a face or a distinguishing mark.
3. `deidentify` (new)
   - Headline: De-identify, then re-read
   - On-slide: (1) Remove · Replace · Generalize · Re-read as a stranger. (2) Before (fictional): "[Patient name], 64, file [file number], admitted to [hospital name] on [exact date] with pneumonia and discharged on [exact date]. Lives in [small town]; her daughter is a nurse on the same ward." After: "A woman in her 60s was admitted with pneumonia and discharged on day 4. She lives outside the city with family." (3) A judgment, not a guarantee. When in doubt, use a case card.
   - Visual: before/after, as in the page. Four steps as a small row on top; the before card with each bracket underlined in muted red; the after card in teal `#CCFBF1`; item 3 as a slate footer line.
   - Notes: Four steps, as on the page. Remove every identifier. Replace with neutral labels: the patient, a woman in her 60s. Generalize: an age becomes a decade, a place becomes outside the city, an exact date becomes day 3. Re-read as a stranger: could you tell who this is? The brackets stand for real values that never appear in this course. The detail people leave in is the daughter who is a nurse on the same ward: it points to someone and adds nothing. Instead of pasting, in this order: an approved tool, de-identify, or a synthetic case. When in doubt, use a case card.
4. `formats-that-leak` (new)
   - Headline: Beyond the text
   - On-slide: (1) Table, format and what it can carry: screenshot (banner: name, file number, date of birth), photograph (face, wristband, tattoo, date stamp), lab PDF (headers, footers, barcodes), recording (a spoken name, a voice), filename. (2) Turning off chat history does not make a consumer tool an approved one. (3) Not sure? Do not paste.
   - Visual: light slide. Five-row table with muted-red dots; items 2 and 3 as two indigo pills below.
   - Notes: Identifiers hide outside the text. A screenshot of the chart carries the banner: name, file number, date of birth. A photograph can carry a face, a wristband, a tattoo, a date stamp. A lab PDF has headers, footers, barcodes and the ordering clinician. A recording carries a spoken name and the voice itself. Even the filename can identify. Turning off chat history, or changing any privacy setting, does not turn a consumer tool into an approved one; only your institution's approval does. Not sure? Do not paste.

**Say**

- 0:00–2:30, `privacy-rule`. Read the line together. Define consumer AI tool and approved tool: who chose it. Then the law in three sentences, and stop: enforced by SDAIA; health data is sensitive personal data, like genetic and biometric; real financial and operational penalties. "For what applies to you, ask your data protection officer or legal team. I am teaching, not advising."
- 2:30–5:00, `identifier-floor`. The list is a floor. The test is whether anyone could be identified, directly or indirectly. Three harmless details can add up to one person.
- 5:00–8:00, `deidentify`. The page's "Try it": the room marks every identifier and every pointing detail in the before text (one minute), then show the after. Land on the nurse daughter. "A woman in her 60s with pneumonia describes no one in particular."
- 8:00–9:30, `formats-that-leak`. Walk the table, then the toggle line.
- 9:30–10:00. "Not sure? Do not paste." Point to the privacy checklist.

**Do**

1. Before class: the privacy checklist open on a second screen.
2. At 5:00, if the deck cannot hide the after card, ask the room to read only the top card first.
3. At 8:00, ask: "Which of these surprised you?" Take two answers. Do not ask who has done it.

**If asked**

- What counts as an approved tool? One your institution vetted and contracted for patient information. Ask which are approved, and for what.
- Does a paid plan, or turning off history, make it fine? No. A paid personal account is still a consumer tool, and settings do not change who approved it.
- Have I broken the law, and what are the penalties? Both are for your data protection officer or legal team. The law carries real financial and operational penalties; this course quotes no amounts or articles. If it already happened, the checklist steps apply.

**Watch for**

- "There is no name, so it is fine." The list is a floor; the test is whether anyone could be identified.
- Legal debate. Park it: the answer is always the data protection officer or legal team.
- A doctor confessing a past paste. Thank them, point to "If it already happened", and take the detail offline.

**Bridge**: "That is the rule and the test. Now the situations where careful, well-meaning doctors break it without noticing: four short situations."

## Topic 5 — Where doctors get this wrong (15 min)

Participant page: [Module 7](../day3/m7-privacy.qmd#where-doctors-go-wrong), four situations. Day clock 0:45–1:00. Deck status: all new: `vignette-cleanup`, `vignette-screenshot`, `vignette-phone-scribe`, `vignette-anonymized`, `vignette-lines`. The reveal for each situation, matching the page, is in that slide's Notes.

**Goal**: By the end, everyone can spot the identifier and the pathway in a realistic situation and name what to do instead.

**Slides**

1. `vignette-cleanup` (new)
   - Headline: "Just to clean up the wording"
   - On-slide: (1) Tag: Fictional, invented for this course. (2) A physician finishing a long clinic pastes a full discharge summary into a free chatbot on a personal account: "tidy the language before I sign." (3) What is wrong, and what should happen instead?
   - Visual: light slide. A white card with a chat-bubble quote; a small muted-red "Fictional" tag at top left; the question in an indigo pill at the bottom.
   - Notes: Read the scenario aloud, one minute in pairs, two answers, then reveal. The summary opens with the name and file number, then admission and discharge dates, the family's town, diagnoses and medicines. Wrong: identifiers attached to a full clinical picture. It went from the institution's records to a personal account on a consumer tool nobody vetted or contracted, and deleting the chat does not undo it. The tidied text also comes back unchecked, so Module 6 applies. Instead: the approved tool, or write it yourself and paste only de-identified text or a synthetic case, then check against the original. The line: Take the wording to the tool. Leave the patient behind.
2. `vignette-screenshot` (new)
   - Headline: "The screenshot"
   - On-slide: (1) Tag: Fictional, invented for this course. (2) On a night shift, a doctor screenshots a lab result and pastes it into a consumer chatbot: "what does the pattern suggest?" No name was typed. (3) What is wrong, and what should happen instead?
   - Visual: as `vignette-cleanup`, with a schematic screenshot in the card: a banner strip labeled "name · file number · date of birth" outlined in muted red above a small lab table.
   - Notes: One minute in pairs, two answers, then reveal. The screenshot includes the banner across the top of the record. Wrong: the banner carries name, file number and date of birth, and the report may add a barcode and the ordering clinician. Nothing identifying was typed and it left anyway, because an image carries everything inside it. Cropping helps only if every other part of the image and the file's metadata is checked. The answer that comes back is a draft: the doctor decides. Instead: ask a senior colleague through the institution's channels, or retype only the values you need, age as a decade, no dates, into an approved tool, and check against a primary source. The line: The banner is part of the picture.
3. `vignette-phone-scribe` (new)
   - Headline: "My own scribe"
   - On-slide: (1) Tag: Fictional, invented for this course. (2) A resident records a whole consultation on a free phone transcription app, then pastes the transcript into a chatbot to draft the note: "the hospital has scribes that do the same." The patient was never told. (3) What is wrong, and how does this differ from the Day Two scribes?
   - Visual: as `vignette-cleanup`, with a phone outline and a waveform in the card.
   - Notes: One minute in pairs, two answers, then reveal. Wrong: the recording holds a name spoken aloud, a voice, and everything the family said in the room. It lands on the servers of a free app, then as a transcript in a second consumer tool: two disclosures, both to services no institution approved. The Day Two scribes were put in place by institutions. That was the institution's decision, not an individual doctor's, and it is the difference. Instead: use the scribe your institution approved, the way it says. If there is none, take your own notes and write the note yourself, and ask whether one is planned. The line: A scribe is approved by your institution, not by how well it works.
4. `vignette-anonymized` (new; bonus)
   - Headline: "It's anonymized"
   - On-slide: (1) Tag: Fictional, invented for this course. Bonus. (2) A doctor preparing a teaching case for an AI-drafted deck says it is anonymized: no name anywhere. It describes a child with a very rare condition, the small town, and the exact date of admission. (3) Who could name this family?
   - Visual: as `vignette-cleanup`, with three chips ("rare condition", "small town", "exact date") converging by indigo lines on one silhouette.
   - Notes: Bonus, two minutes; drop it first if you are behind. Ask: who in this room could name the family? Wrong: each detail might pass alone; together they point to one family, and anyone in that town, or any doctor who saw the case, would know who it is. That is what any combination of details rare enough to point to one person means. Removing the name was step one of four. Instead: generalize until the details point nowhere: an age band, a region, day 3 for a date. If the rare condition is the giveaway and the teaching point survives without it, keep the point and change the story: that makes it a synthetic case. Unsure: ask the data protection officer. The line: No name is not the same as no identity.
5. `vignette-lines` (new)
   - Headline: Three ways it leaks
   - On-slide: (1) Take the wording to the tool. Leave the patient behind. (2) The banner is part of the picture. (3) A scribe is approved by your institution, not by how well it works.
   - Visual: light slide. Three cards in a row, one per line, each with a muted-red top border; a teal line beneath: "Instead: an approved tool, de-identify, or a synthetic case."
   - Notes: Three leaks, one rule, and three lines from the page. The bonus line: no name is not the same as no identity. Before any paste, ask: is this tool approved for patient information? If not, is what I am pasting synthetic or fully de-identified, with no identifier in the text or the file, and nothing that would let someone who knows this person recognize them? If you cannot say yes, do not paste. If it already happened: stop, write down what was pasted, into which tool and when, report it through your institution's process and to its data protection officer, and do not assume deleting the chat undoes it.

**Say**

- 0:00–1:00. "Four situations, all invented; none is a real patient or incident. Read, one minute in pairs, two answers, then what I see." The people in them are busy, not careless: the tool was open and the shortcut looked harmless.
- Core situations, 3 minutes each: 0:30 a volunteer reads; 1:00 pairs; 1:00 two answers, pushing for the specific identifiers and the pathway; 0:30 reveal from the slide Notes, then the line. `vignette-cleanup` 1:00–4:00, `vignette-screenshot` 4:00–7:00, `vignette-phone-scribe` 7:00–10:00.
- 10:00–12:00, `vignette-anonymized`. Bonus: drop it first if behind, but keep its line.
- 12:00–15:00, `vignette-lines`. Read the before-any-paste questions. Then: "Where in your own week could this happen?" Two answers, no confessions required.

**Do**

1. Before class: five slides loaded, the privacy checklist open, a visible timer.
2. A different volunteer reads each scenario aloud.
3. At 2:00 into each situation, reveal even if hands are up.
4. If a doctor begins describing a real case from their own practice, stop them before any detail: "Keep it general. No real patient goes into this room."

**If asked**

- What if the patient consented? Consent to care is not consent to send information to a tool your institution has not approved. Whether consent changes anything is for your data protection officer or legal team.
- Everyone in my department does this. Common is not approved. If it has happened, the checklist steps apply, including reporting through your institution's process.
- A photo of a rash or a scan, no face? Images can carry a face, a tattoo, a wristband, a date stamp or a header. Imaging AI is outside this course; ask what your institution approves.

**Watch for**

- "I would have done the same." Treat the motive as reasonable. The fix is a route, not a scolding.
- The first situation swallowing time. Hold three minutes each.
- Slipping into a legal debate: park it with the data protection officer or legal team.

**Bridge**: "Break, ten minutes. When you come back, bring one output from your weekend, from Day One or Day Two, not the one from Lab Three. We run the three questions on it."

## Topic 7 — Back to the rule, applied to a real case (20 min)

Participant page: [Module 8, back to the rule](../day3/m8-back-to-the-rule.qmd#back-to-the-rule). Day clock 1:10–1:30 (after the break). Deck status: kept `back-to-rule` (reword the three pills to the exact questions); new `check-card`. Rounds, as on the page: 2 minutes alone, 6 in pairs, 8 in triads or the whole room, 4 to synthesize.

**Goal**: By the end, each doctor has run the three questions on one of their own outputs, decided use, fix or discard, and written one Monday line.

**Slides**

1. `back-to-rule` (kept; pills reworded)
   - Headline: Back to the Rule
   - On-slide: (1) "Pick one AI output from this weekend. Run it through the three questions from Day One." (2) Three pills: Could I defend this to a colleague? · Does it point to something I can verify? · Would I catch it if it were wrong?
   - Visual: existing light slide, 72 px title, 44 px semibold prompt, three indigo pills on `#EEF2FF`. Only change: the pills carry the exact questions instead of the short forms; stack them if they do not fit one row.
   - Notes: This is not a recap. On Day One the three questions were a card you were handed; today they are a habit you either have or do not. Pick an output you made on Day One or Two that looks fine, not the one you took apart in Lab Three. If you have none, make one in two minutes from Case C with the prompt on the page. Use only outputs from the course's synthetic cases; nothing from a real patient. Alone first, so that whatever your partner catches is something you really missed. If the answer to any of these is no, that's the signal to slow down, not the finding to accept.
2. `check-card` (new)
   - Headline: The check card
   - On-slide: (1) Table: the three questions, each with "Yes or no, and the evidence". (2) Decision: use, fix, or discard. Kind of error: invented, omitted, altered, fabricated citation, or none found. (3) What I will change on Monday: ______
   - Visual: light slide. A three-row table in white with `#E2E5EA` borders; under it two teal chips for Decision and Kind of error; a blank line for the Monday sentence with an indigo underline.
   - Notes: This is the card on the page, laid out for one output. For each question write yes or no and the evidence: exactly what you opened. Finding nothing wrong is a valid result; an empty evidence line is not. Then the decision: use, fix or discard. Then the kind of error: invented, omitted, altered, fabricated citation or citation, or none found. Check against the source, not against the tool; in this room the source is the case card. The last line is the Monday line: one sentence starting with a verb, small enough to do on your first day back.

**Say**

- 0:00–2:00, alone. Thirty seconds on `back-to-rule`, then `check-card`, left up until 8:00. "Read your output slowly. Mark every number, name, date, dose and source. Fill in the card, except the Monday line, against the case card, not the tool." Anyone without an output makes one from Case C now and starts their card in the pair round.
- 2:00–8:00, pairs, 3 minutes each way. "Defend it to a colleague." The partner asks "where did that come from?" of every mark and points at anything unmarked. If you disagree, the source decides: not either of you, not another AI. Swap at 5:00.
- 8:00–16:00, triads or whole room. Small room: hands on each decision (use, fix, discard), then call on three people. Larger room: triads, a minute each (what it was, what you decided, the error or none). Finish on: "What did your partner catch that you missed?"
- 16:00–20:00, synthesize. Board answers to: which question most often came out no, which kind of error came up most, what would have caught it faster. Everyone writes the Monday line and reads it to a neighbor; three are read aloud.

**Do**

1. Before class: draw the tally on the board (columns Q1, Q2, Q3 for "no", and invented, omitted, altered, fabricated). Have the Case C prompt from the page ready.
2. During pairs, listen for "looks right" with nothing opened. Ask: "What did you open?"
3. At 16:00 collect the tally by hands. Say once: this measures these outputs and this room, not any tool. Nudge vague Monday lines toward an action, a thing to check and a moment, as in the page's table.

**If asked**

- Do I run all three questions on every output at work? Scale to the stakes, as in Module 6. For anything that goes into a chart or leaves your hands, yes.
- My honest answer to question 3 is no. That is the signal to slow down, not the finding to accept. Verify against the source, or do not use AI for that piece.
- Everything came out yes. Is that fine? Yes, if question 2's evidence names something you actually opened. A yes with no evidence is a maybe.

**Watch for**

- "It looks right" in the evidence column, or "I asked the tool" as the source.
- The Lab Three output picked again: this round is for the output that looks fine. Anything with real patient detail: stop it and use a synthetic case.
- Triads where one person talks, and tool debates in the synthesis. Steer back to the three questions.

**Bridge**: "You have checked your own work. The last check of the day is on the whole weekend: twenty minutes, all three days."

## Topic 8 — Assessment quiz (20 min)

Participant page: [Module 8, assessment](../day3/m8-back-to-the-rule.qmd#assessment), with the practice bank on the [assessment page](../assessment.qmd). Day clock 1:30–1:50. Deck status: kept `assessment`. The scored quiz and its answer key never go into this repository or this file; the practice bank is deliberately not the scored quiz.

**Goal**: By the end, every doctor has taken the quiz under the same, clearly stated conditions and knows where to practice afterward.

**Slides**

1. `assessment` (kept)
   - Headline: Assessment & Certificate
   - On-slide: (1) The Quiz: "A short quiz covering all three days, taken at the close of Day Three." (2) The Certificate: "A certificate of completion for every doctor who finishes the weekend."
   - Visual: existing light slide, 72 px title, two white cards with icons (indigo check-circle for the quiz, teal star for the certificate). No change. Point to the quiz card now and return for the certificate card in Topic 9.
   - Notes: The quiz closes Day Three and covers all three days. It runs twenty minutes. Before you start, give the logistics from your confirmed sheet: open or closed book, how it is delivered and handed in, and what to do when you finish. Say what it is for: to show what stuck, not to trick anyone. The practice bank on the assessment page is separate from the quiz, so it is not a preview; use it afterward to find what you are unsure of. Once it starts, answer logistics only and do not teach. Afterward, note the topics that made you hesitate: that is your reading list for the next two weeks.

**Say**

- 0:00–2:00, `assessment`. "Twenty minutes, all three days. It checks what stuck." Give the logistics from the confirmed list below. Point to the "What it covers" checklist on the page and to the practice bank: "afterward, not a preview."
- 2:00–17:00, the quiz. Stay quiet and visible; logistics questions only, no hints. Time calls at halfway and five minutes out. [TRAINER TO CONFIRM: how long the quiz itself takes within these twenty minutes; adjust these cues once the format is known.]
- 17:00–20:00. Collect or confirm submission. "Whatever the result, note the topics that made you hesitate. That is your reading list for the next two weeks."

**Do**

1. Before the day, settle every item below; none is on the participant page or in the deck. Do not improvise a policy in the room.
   - [TRAINER TO CONFIRM: open or closed book, including whether the course site, notes or any AI tool may be used]
   - [TRAINER TO CONFIRM: format: paper or online form, number of questions, question types]
   - [TRAINER TO CONFIRM: pass mark, if any, and whether the certificate depends on the result]
   - [TRAINER TO CONFIRM: how results are given (individually, in the room, not at all) and whether answers are reviewed afterward]
   - [TRAINER TO CONFIRM: what participants do when they finish early, and whether a retake or a late finish is allowed]
   - [TRAINER TO CONFIRM: how the quiz is delivered and collected, and whether phones or laptops are allowed]
2. At 0:00, show `assessment` while you give the logistics. During the quiz, hold the room quiet.

**If asked**

- Is it open book? May I use an AI tool? Is there a pass mark? Will we go over the answers? Answer only from the confirmed sheet. If an item is not confirmed, say so and say when you will tell them.
- Does the certificate depend on the result? The deck promises a certificate of completion to every doctor who finishes the weekend. Anything beyond that comes from the confirmed sheet.
- Can I practice first? The practice bank on the assessment page is for afterward. It is not a preview of these questions.

**Watch for**

- Improvising a policy under pressure. "Let me confirm" beats a guess.
- Hints or tone during the quiz, and phones coming out by habit to ask a tool. State the rule before the start.
- Anxiety. Say once that the quiz shows what stuck, for the course; it is not a judgment of them as doctors.

**Bridge**: "Quiz done. Ten minutes left: your certificate, four things to keep, and a plan for your first two weeks."

## Topic 9 — Certificate and closing (10 min)

Participant page: [Module 8, closing](../day3/m8-back-to-the-rule.qmd#closing). Day clock 1:50–2:00. Deck status: kept `assessment` (second use, certificate card) and `closing`; new `keep-two-lines`, `keep-two-tools`, `first-two-weeks`, `not-covered`. The page's four things to keep are split over two slides so no slide carries more than three items.

**Goal**: By the end, each doctor knows what the certificate is, can say the four things to keep, and has written down one low-risk task and one colleague to teach.

**Slides**

1. `assessment` (kept; second use)
   - Headline: Assessment & Certificate
   - On-slide: as in Topic 8; point to the Certificate card.
   - Visual: existing slide, no change.
   - Notes: Return to this slide for the certificate card only. Every doctor who finishes the weekend receives a certificate of completion. Say plainly what it is: a certificate of completion. Make no CME, CPD or accreditation claim. Say how and when it is issued, from your confirmed sheet. Then move on to what you take back to work.
2. `keep-two-lines` (new)
   - Headline: Keep these two lines
   - On-slide: (1) AI drafts. You decide. (2) No patient identifiers into a consumer AI tool. Ever. Full stop.
   - Visual: dark slide (`#0F172A`), two lines stacked in large white type, a soft-red `#FCA5A5` rule beside the privacy line, a small indigo label above.
   - Notes: If you keep nothing else from the weekend, keep two lines in these exact words. The rule: AI drafts. You decide. The privacy line: No patient identifiers into a consumer AI tool. Ever. Full stop. Say each aloud with the room, once. A consumer AI tool is a general assistant you sign up for yourself. If you are not sure whether something counts as an identifier, do not paste it; the privacy checklist has the list.
3. `keep-two-tools` (new)
   - Headline: Keep these two tools
   - On-slide: (1) The three questions: Could I defend this to a colleague? Does it point to something I can verify? Would I catch it if it were wrong? (2) The four parts: Role · Context · Format · Constraints.
   - Visual: light slide, two cards. Left: the three questions as a numbered list. Right: four chips, with the memory line under them in slate: "Who it is, what it knows, what shape to return, what to avoid."
   - Notes: Two tools to keep. The three questions: Could I defend this to a colleague? Does it point to something I can verify? Would I catch it if it were wrong? If the answer to any of these is no, that's the signal to slow down, not the finding to accept. When you find a mistake, name it: invented, omitted, altered. The four parts of a prompt: Role, Context, Format, Constraints. Who it is, what it knows, what shape to return, what to avoid. Your reusable prompts are in the prompt library on the site.
4. `first-two-weeks` (new)
   - Headline: Your first two weeks
   - On-slide: (1) Four steps: one low-risk task, run the check on every output · keep a prompt library · ask your institution about its policy and approved tools · teach one colleague. (2) "Until you have an answer, the privacy line is your policy."
   - Visual: light slide. Four numbered cards in a row, badges "Week 1" (indigo) on the first three and "Week 2" (teal) on the fourth; item 2 as a slate footer line.
   - Notes: Four steps, in order, each small on purpose. Start of week one: pick one low-risk task, such as rewording an email to a colleague or a first outline for a talk, and run the check on every output. Keep patient data out of it. In week one, keep a prompt library: save prompts that gave a draft you would use, with the four parts and a placeholder where the facts go, never the facts. In week one, ask your institution whether it has a policy on AI tools and which tools it has approved, for which uses. In week two, teach one colleague for ten minutes, on a synthetic case. Now write down the task and the colleague.
5. `not-covered` (new)
   - Headline: What this course did not cover
   - On-slide: (1) Imaging AI · Clinical decision support and regulation · Medico-legal questions · AI built into your hospital's record system, in depth. (2) "Treat the rule as the place to start, then ask someone who works in that area."
   - Visual: light slide. Four muted white cards with thin grey borders; item 2 as an indigo pill below.
   - Notes: Be honest and brief. This weekend was about text: drafting, summarizing and checking, with general assistants and a few purpose-built tools. Four areas were outside it. Imaging AI: tools that analyze scans, slides and other images. Clinical decision support and regulation: systems that recommend inside clinical workflows, and the rules on how they may be used. Medico-legal questions: who answers for an AI-drafted note that turns out wrong. The rule tells you where the decision sits; it is not a legal position, so ask your data protection officer or legal team. AI built into your hospital's record system, in depth. For all four, ask someone who works in that area.
6. `closing` (kept)
   - Headline: Thank You
   - On-slide: (1) Thank You. (2) AI for Clinicians. (3) Feedback line, once confirmed: [TRAINER TO CONFIRM: feedback link and how it is shared: on the slide, in chat or by QR code].
   - Visual: existing dark closing slide, 120 px title, two gradient diamonds. Add one small line at the bottom for the feedback link (DM Sans 24 px, `#AEB8D1`) only after it is confirmed.
   - Notes: Thank the room. Say the last line once: AI drafts. You decide. Run the check every time. Give the feedback link and say how to reach it, from your confirmed sheet. Remind them of the two things they wrote down: the low-risk task and the colleague.

**Say**

- 0:00–1:00, `assessment`. "Every doctor who finishes the weekend receives a certificate of completion." Say what it is and no more. [TRAINER TO CONFIRM: how and when certificates are issued, and in what form.]
- 1:00–3:00, `keep-two-lines`, `keep-two-tools`. "If you keep nothing else, keep these four things in these words." The room says the rule and the privacy line aloud; read the three questions together; give the memory line for the four parts.
- 3:00–6:00, `first-two-weeks`. Four steps, one Monday action each. Then the two-minute "Try it" on the page: write the one low-risk task and the colleague.
- 6:00–7:30, `not-covered`. Short and honest. "The rule is where to start, not the whole answer."
- 7:30–9:00, feedback. [TRAINER TO CONFIRM: the feedback link, and whether the form is anonymous.] Ask for it while they are in the room.
- 9:00–10:00, `closing`. "AI drafts. You decide. Run the check every time." Thank the room.

**Do**

1. Before the day: certificates ready; feedback link ready; the closing section of Module 8 open for the plan wording.
2. At 1:00, have the room say the rule aloud with you, once.
3. At 4:30, the "Try it": everyone writes two lines, the task and the colleague. Do not collect them.
4. At 7:30, share the feedback link and leave `closing` up while certificates go out by the confirmed process.

**If asked**

- Does the certificate carry CME or CPD hours? It is a certificate of completion; the course makes no CME or accreditation claim. [TRAINER TO CONFIRM: whether any SCFHS CPD accreditation is in place; until confirmed, say none is claimed.]
- Which tool on Monday? Whatever your institution approves for patient information; for non-patient tasks, a general assistant you already have. Availability changes, so check.
- Who is responsible if an AI-drafted note is wrong? A medico-legal question outside this course. "AI drafts. You decide" says where the decision sits; it is not a legal position. Ask your data protection officer or legal team.
- Can I share the site? [TRAINER TO CONFIRM: how long participants keep access to the course site, and any terms on sharing the materials.]

**Watch for**

- A CME, CPD or accreditation claim slipping in, from the room or from you.
- The closing crowding out the plan: cut `not-covered` to one minute before you shorten the first two weeks.
- Tool endorsements. The course recommends none.

**Bridge**: This closes the course, so the bridge is to Monday: "Take the low-risk task you just wrote down and run the check on its first output. AI drafts. You decide."

## Lab 3 — facilitation

Participant page: [Lab Three](../day3/lab3-spot-the-error.qmd), 25 minutes: part 1, trade and catch (15), and part 2, instructor examples (10). Day clock 0:10–0:35. The page describes only the procedure, the reflection and how to run a peer-check at work. It has no answers and no examples: those live in this section only, and never in the deck notes.

**Goal**: Each doctor runs the five moves on an output they did not write, types every error they find, and names one habit that would have caught it faster.

### Before class

- At the close of Day Two, or by message on the morning of Day Three, ask everyone to keep their Lab One "break it on purpose" output open. Its first line must be the label `PRACTICE OUTPUT: CONTAINS DELIBERATELY UNRELIABLE CONTENT. NOT FOR CLINICAL USE.` Anyone whose copy lacks it adds it before trading.
- Choose one fresh probe from Lab One's part 2 menu to read aloud for anyone with no saved output.
- Load the five Lab Three slides (`lab3`, `lab3-example-a`, `lab3-source-a`, `lab3-example-b`, `lab3-source-b`) and check that the example text reads from the back of the room.
- Keep this section on your own screen. Do not project it, paste it into the deck notes, or hand out the keys.

### Materials

The participant page with its recording table and reflection; the verification card in Module 6; the five slides; a visible timer; a board or flipchart for the claims list and the habits; this section.

### Minute-by-minute

Part 1, trade and catch (15 minutes, the page's four steps):

| Clock | What happens |
|---|---|
| 0:00–1:00 | Swap. Launch `lab3`. Pairs hand over the output and the question that produced it; nobody says what they found in Lab One. Odd number: one trio. No output: fresh probe now, warning line on top. |
| 1:00–10:00 | Check cold, nine minutes. Down the verification card: extract the claims, find each source, mark each claim, name the error, recording as they go. Time calls at 4:00 and 8:00. |
| 10:00–13:00 | Compare. Hand it back; where findings differ, each says how they checked. |
| 13:00–15:00 | Reflect. "What would have caught it faster?" on paper; hear two answers aloud. |

Part 2, instructor examples (10 minutes, the page's four steps). One example, at the page's full timings:

| Clock | What happens |
|---|---|
| 0:00–1:00 | Project `lab3-example-a`. Read and list every checkable claim. |
| 1:00–2:00 | Read the text against itself: do its parts agree with each other? |
| 2:00–5:00 | Project `lab3-source-a`. Check each claim against the card and mark it. |
| 5:00–8:00 | Call it. For each finding: the claim, how you would confirm it, the kind of error. |
| 8:00–10:00 | Give the key. Everyone counts what they found and missed and notes the kind of error they missed. Ask the page's reflection: which kind did you find fastest, and which did you walk past? |

Two examples, each at half: per example, list and read against itself 0:45, card and marks 1:45, call it 1:15, key and score 0:45. Example A runs 0:00–4:30, Example B 4:30–9:00, debrief 9:00–10:00.

### What good looks like

- A written claims list exists before anyone looks anything up.
- Every "confirmed" names what was opened. "I asked the tool" is not a source.
- At least one claim is marked could-not-find and treated as wrong, and the pair says what they did about it.
- Errors are typed in the course's words.
- The reflection names a habit ("I would list the numbers first"), not a tool.

### Common problems and fixes

| Problem | What to do |
|---|---|
| Nothing to catch: the output looks clean | The page's rule: a clean result counts only if they can list what they confirmed and where. If they can, it is valid; move to Example A early. If not, that is the finding. |
| The tool refused or hedged | Note what it said it could not do, as the page asks, then swap for an output that is not a refusal: another pair's, or a fresh probe. Ask what they would have done with a confident wrong answer. |
| Someone did not save an output | A fresh probe now with the warning line on top (two minutes), or join a pair as a third checker. |
| No checkable claims: opinion or general advice | Ask for a version with specific numbers, names or citations, or go straight to Example A. |
| A pair pastes the output into a tool to ask what is wrong, or "confirms" with a second AI | The page's warning: that returns a second draft, not a check. A second AI is not a source. Re-mark the claim could-not-find until a real source is opened. |
| Sources unreachable | Mark could-not-find, treat as wrong, and say which source they would go to. |
| The output holds anything that looks like a real patient's details | Stop. Nothing from a real patient belongs in this room, and the page says not to swap it. Use a fresh probe and restate the privacy line. |
| A pair finishes early | Recording table and reflection, then swap with another pair. |

### Debrief prompts

Pick three. Ask, do not tell.

1. Which errors were easiest to find, and which needed a source?
2. Did any "confirmed" rest on another AI, or on memory?
3. What would have caught it faster: a habit, not a tool?
4. Which of the five moves did you skip under time pressure?
5. What would you change in your own prompt? (The page's example: add to CONSTRAINTS "Do not cite sources or guidelines; I will supply them.")
6. How would you run this as a peer-check at work? Who is your second pair of eyes?

### Backup examples and answer keys

Two prepared examples for Part 2. Both are fictional and non-clinical: a made-up day clinic, its reminder pilot and a training workshop. Every clinic, document, number and name is invented for this exercise; none exists. Each carries the practice-output label because each contains deliberately unreliable content. The planted errors are generic (a figure, a document number, a citation year, a citation that cannot be found), never a clinical fact. Project the text first and the source card second, keep the key to yourself until the call-it round, and reveal by asking. The card is "the only documents that exist for this exercise", so could-not-find has a clear meaning.

#### Example A: reminder pilot summary (three planted errors)

Projected text (`lab3-example-a`):

```text
PRACTICE OUTPUT: CONTAINS DELIBERATELY UNRELIABLE CONTENT. NOT FOR CLINICAL USE.

Summary: Riverbend Day Clinic text-reminder pilot (fictional)

This summary is based on Pilot Report RC-207. Over six weeks, the clinic sent text reminders to one group of patients and none to another. The pilot enrolled 200 patients: 120 in the reminder group and 100 in the comparison group. Fewer appointments were missed in the reminder group than in the comparison group. The design follows the Riverbend Network Scheduling Guide (2022), which recommends comparing reminder and no-reminder groups over at least four weeks.

Source: Pilot Report RC-270.
```

Source card (`lab3-source-a`):

```text
SOURCE CARD A (fictional). The only documents that exist for this exercise.

1. Riverbend Day Clinic, Reminder Pilot Report, document RC-270. The pilot ran for six weeks: text reminders were sent to one group and none to the other. It enrolled 200 patients: 120 in the reminder group and 80 in the comparison group. Fewer appointments were missed in the reminder group than in the comparison group. The pilot design followed the Riverbend Network Scheduling Guide.

2. Riverbend Network Scheduling Guide, 2019 edition. Recommends comparing reminder and no-reminder groups over at least four weeks.
```

Answer key A:

| # | In the text | What is wrong | Kind | How the five moves find it |
|---|---|---|---|---|
| 1 | "200 patients: 120 in the reminder group and 100 in the comparison group" | 120 + 100 is 220, not 200. The card gives 80 in the comparison group. | Altered (a figure) | Move 1 lists the numbers. Adding 120 and 100 shows the text disagreeing with itself before any lookup. Moves 2 and 3: the card says 80, so 100 is wrong. Move 4 corrects it. |
| 2 | "Pilot Report RC-207" in the first line, "Pilot Report RC-270" in the last | Two numbers for one report. The card gives RC-270, so RC-207 is wrong. | Altered (a document number) | Move 1 lists both identifiers. They cannot both be right, but only the card says which. Mark RC-207 wrong. |
| 3 | "Riverbend Network Scheduling Guide (2022)" | The card gives the 2019 edition. | Altered (a citation year) | Nothing in the text gives it away. Move 2 opens the card; mark 2022 wrong; move 4 corrects it. |

Correct, and to be confirmed against a named line of the card: six weeks; reminders to one group and none to the other; fewer missed in the reminder group; the guide recommends at least four weeks; the source line, RC-270; the design followed the guide. A "confirmed" with no line named is not confirmed.

Draw out: error 1 needed no source, error 2 needed the source only to say which number was right, and error 3 needed the source alone.

#### Example B: workshop summary (two planted errors)

Projected text (`lab3-example-b`):

```text
PRACTICE OUTPUT: CONTAINS DELIBERATELY UNRELIABLE CONTENT. NOT FOR CLINICAL USE.

Summary: Riverbend Day Clinic documentation workshop (fictional)

The workshop ran three sessions: 40 minutes on templates, 30 minutes on abbreviations and 45 minutes on handover notes, for a total of two hours. Thirty-nine staff attended: 18 on the first day and 21 on the second. The organizers adapted the format from Quality Circle Memo QC-88.

Source: Workshop Report WR-12.
```

Source card (`lab3-source-b`):

```text
SOURCE CARD B (fictional). The only documents that exist for this exercise.

1. Riverbend Day Clinic, Documentation Workshop Report, document WR-12. Three sessions: templates, 40 minutes; abbreviations, 30 minutes; handover notes, 50 minutes; total 120 minutes. Attendance: 18 on the first day and 21 on the second, 39 in total. The format was adapted from the clinic's earlier training day.
```

Answer key B:

| # | In the text | What is wrong | Kind | How the five moves find it |
|---|---|---|---|---|
| 1 | "40 minutes ... 30 minutes ... 45 minutes ... a total of two hours" | 40 + 30 + 45 is 115 minutes, not 120. The card gives 50 minutes for handover notes. | Altered (a figure) | Move 1 lists the numbers and adds them: the text disagrees with itself before any lookup. Move 2: the card shows 50. Move 4 corrects it. |
| 2 | "Quality Circle Memo QC-88" | Not on the card. The card says the format was adapted from the clinic's earlier training day and lists no memo. | Fabricated citation | Move 1 extracts the citation. Move 2: there is nothing to open. Move 3: could-not-find, which counts as wrong however plausible the number looks. Move 4: delete it, or replace it with what the card says. |

Correct: 18 + 21 = 39; three sessions; the 40 and 30 minute sessions; the source line, WR-12.

Draw out: in real life the search for QC-88 would run through the institution's document system and the open web. Here the card is the whole world. A citation that cannot be found is treated as wrong.

If someone flags a line that is not in either key, check it against the card. If the card supports it, it is confirmed. If the card is silent, could-not-find is a fair mark; note it and fix the example afterward.
