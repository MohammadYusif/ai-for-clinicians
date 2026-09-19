# AI for Clinicians — Expanded Content Brief

> Source brief, kept verbatim. Everything in this repository was built from it.
> Where the repository deliberately departs from it, `course/instructor-guide.md`
> ("What changed from the brief") says so and why.

## Why this file exists

The current deck (26 slides, published at https://claude.ai/artifact/KVj1mJP2pSmdoTrE4J4Jw1) has the right skeleton but not enough material to fill 2 hours a day, and the two labs were single-task and too easy. This is the working brief to draft full talking points and slide text against.

**Once the content below is fleshed out, bring it back to the link above to actually update the deck.** That Slides system is specific to claude.ai; Claude Code can draft the words but can't publish into it directly.

## The time math

About 7-8 real teaching topics a day at ~5 minutes of discussion each, plus one thin lab, comes to 60-70 minutes, not 120. The fix is roughly double the distinct sub-topics per day, more worked examples per topic instead of one, and three-part labs instead of one-task labs. Budgets below assume a 10-minute break each day and a room that asks questions, not a silent lecture.

---

## Day One — Foundations (target: 120 min)

| # | Topic | Status | Time | Content notes |
|---|-------|--------|------|----------------|
| 1 | Course opener (why / outcomes / agenda) | kept, shown once | 10 min | Already drafted. Shown at the very start of Day 1 only. |
| 2 | The rule for the weekend | kept | 5 min | "AI drafts. You decide." Opening frame. |
| 3 | **How these tools actually work, in 5 minutes** | **NEW** | 10 min | Non-technical: next-token prediction intuition, why it sounds confident whether right or wrong, "it only knows what's in the conversation." This is the foundation everything else leans on — worth doing properly rather than skipping to the rules. |
| 4 | Your three-question check | kept | 5 min | |
| 5 | Where the extra words come from | kept | 5 min | Problem framing before the fix. |
| 6 | **Anatomy of a good prompt** | **NEW** | 10 min | The reusable 4-part framework: role, context, format, constraints. This is the thing they should be able to apply to *any* prompt, not just notes — teach it as a standalone tool. |
| 7 | Structure fixes it (notes) | kept | 10 min | Now framed as one application of the framework above. |
| 8 | **Same framework, three more jobs** | **NEW** | 15 min | Apply the same 4-part framework to a referral letter, a discharge summary, and a patient-facing handout in plain language. Same technique, three different outputs — this is what makes the framework feel transferable instead of note-specific. |
| 9 | Not all AI is the same | kept | 5 min | |
| 10 | Same tool, different doctor | kept | 5 min | OpenEvidence vs. Vera Health access lesson. |
| 11 | **Live demo: same question, two tools** | **NEW** | 10 min | Instructor runs one real clinical question through two tools live, room compares outputs, before doing their own comparison in the lab. |
| 12 | Spend your quota on purpose | kept | 5 min | |
| 13 | Break | | 10 min | |
| 14 | **Lab One** (see full spec below) + debrief | expanded | 25 min | |

Total: 120 min.

---

## Day Two — Applications (target: 120 min)

| # | Topic | Status | Time | Content notes |
|---|-------|--------|------|----------------|
| 1 | Day Two divider + four places AI already fits | kept | 10 min | |
| 2 | Notes, done right | kept | 5 min | |
| 3 | Already live in Saudi clinics (Sahl AI / Augnito) | kept | 10 min | |
| 4 | **Same note, three audiences** | **NEW** | 15 min | One clinical event, three outputs: the chart note (clinical register), the discharge instructions (patient, plain language), the referral (colleague, focused). Reinforces audience-aware prompting as its own skill, not just "write a note." |
| 5 | From case to slide deck | kept | 8 min | |
| 6 | **Building a full talk, not just an outline** | **NEW** | 12 min | Go one level past the outline: actual slide text, a line of speaker notes, one chart/visual suggestion. Shows the full arc, not just the first step. |
| 7 | Teaching with AI | kept | 8 min | |
| 8 | **Grading yourself** | **NEW** | 7 min | Generate an answer key alongside the quiz questions, and cross-check one question against the real source before using it on trainees — ties hallucination-awareness into the teaching workflow specifically. |
| 9 | Break | | 10 min | |
| 10 | **Lab Two** (see full spec below) + debrief | expanded | 35 min | |

Total: 120 min.

---

## Day Three — Safety & Ethics (target: 120 min)

| # | Topic | Status | Time | Content notes |
|---|-------|--------|------|----------------|
| 1 | Day Three divider + confidently wrong (framing) | kept | 10 min | |
| 2 | **Lab Three: Spot the Error** (see full spec below) | **NEW** | 25 min | Day 3 currently has zero hands-on time — this is the fix. |
| 3 | The rule that isn't optional (privacy / PDPL) | kept | 10 min | |
| 4 | **Where doctors get this wrong** | **NEW** | 15 min | 2-3 realistic scenario vignettes (not real patient data) for room discussion — e.g. a colleague pasting an identifiable discharge summary into a public chatbot "to clean up the wording." What's wrong, what should happen instead. Turns the abstract rule into situations they'll actually recognize. |
| 5 | Break | | 10 min | |
| 6 | Back to the rule, applied to a real case from the weekend | kept, expanded | 20 min | Have each doctor bring one real AI output from Days 1-2 and run it through the three-question check as a group exercise, not just a recap slide. |
| 7 | Assessment quiz | kept | 20 min | |
| 8 | Certificate + closing | kept | 10 min | |

Total: 120 min.

---

## The three labs, in full

### Lab One — Day 1 (~35 min including debrief)
1. **Template test (15 min):** Draft one real note without a template, then again with one (using the 4-part framework from earlier in the day). Time both. Compare word count and how much editing each needed.
2. **Break it on purpose (10 min):** Ask the tool something slightly outside what it can reliably know — a very specific recent drug interaction, a local guideline number, a niche statistic. Watch it answer confidently anyway. Run the output through the three-question check. **Save this output** — Lab Three reuses it.
3. **Tool face-off (5 min):** Run the same clinical question through a general assistant and a literature-grounded tool. Which would you actually trust, and for what?
4. **Debrief (5 min):** Share one prompt that worked well.

### Lab Two — Day 2 (~35 min including debrief)
1. **One case, three outputs (20 min):** Take one real case and produce the chart note, the patient-facing handout, and a 3-slide teaching version from it — same underlying facts, three audiences, three prompts.
2. **Tool check, again (10 min):** Repeat Day 1's tool face-off on a Day-2-flavored task (a teaching summary or a referral) to see if the same pattern holds.
3. **Share-out (5 min):** Pairs present one output; room applies the three-question check together.

### Lab Three — Day 3 (~25 min, new)
1. **Trade and catch (15 min):** Doctors swap their "break it on purpose" output from Lab One with a neighbor and try to spot what's wrong, cold, using only the verification workflow taught earlier that day.
2. **Instructor examples (10 min):** 1-2 backup examples prepared in advance, built around safely generic errors (a wrong citation year, a mismatched guideline number) rather than a specific fabricated clinical fact, for rooms where the swap doesn't surface enough material.

---

## Research already gathered — don't re-derive these

- **Sahl AI:** A Saudi-built bilingual Arabic-English ambient scribe (Sahl AI, Riyadh), piloted across outpatient, inpatient, and primary care clinics within Riyadh First Health Cluster and King Saud Medical City. Scored 42.2 of 45 on a modified Physician Documentation Quality Instrument (PDQI-9), 4.35/5 on the accuracy domain specifically. Published in *JMIR Medical Informatics*, March 2026.
- **Augnito / Almoosa Health:** Augnito's Omni AI Scribe, multi-lingual including Arabic dialects, integrated directly into Almoosa Specialist Hospital's EMR/HIS (announced Jan 2025, Arab Health Exhibition).
- **Vera Health vs. OpenEvidence:** OpenEvidence is the best-known literature-grounded clinical AI tool but requires US NPI verification and withdrew from the EU/UK in April 2026 — not usable by a Saudi audience. Vera Health does the same job (citation-grounded answers from peer-reviewed literature) but verifies healthcare professionals globally with no geographic restriction, and is GDPR compliant.
- **Saudi PDPL:** The Personal Data Protection Law (enforced by SDAIA) explicitly classifies health data as sensitive personal data, alongside genetic and biometric data. Healthcare entities face real financial and operational penalties for mishandling it.
- **SCFHS CPD/CME accreditation:** SCFHS accredits CPD activities (lectures, conferences, synchronous/asynchronous e-learning) through its provider platform. A separate "Specialized Professional Program" track requires a minimum 14-day duration and doesn't carry CME hours at all — a weekend course needs the CPD-activity route, not that one. Requires CPD-provider status first (yours or a partner entity's), then activity-level accreditation for this specific course.

---

## Deck design system — for visual consistency when this comes back

- Dark: `#0F172A` · Light background: `#FBFBFD` · Card surface: `#FFFFFF`
- Accent 1 (indigo): `#4F46E5` · Accent 2 (teal): `#14B8A6`
- Body text: `#475569` · Body on dark: `#AEB8D1` · Border: `#E2E5EA`
- Typeface: DM Sans (single family, weights 400-800) — Google Fonts: `family=DM+Sans:wght@400;500;600;700;800`
- Type scale: 96 / 72 / 44 / 30 / 24
