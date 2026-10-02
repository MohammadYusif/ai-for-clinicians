<!-- Generated from day1/m2-prompting.qmd by tools/build_prompt_library.py. Do not edit. -->

```text
1. ROLE: You are a family physician, writing for a cardiologist.
   CONTEXT: A referral. Use ONLY the facts below. Write [MISSING: what] if something is absent.
   FACTS: [facts]
   CONSTRAINTS: Add no findings, doses, or diagnoses. No hedging.

2. ROLE: You are a pediatrician, writing for a baby's parents.
   CONTEXT: A home-care handout. Use ONLY the facts below.
   FACTS: [facts]
   FORMAT: Three short headings. Maximum 150 words.

3. ROLE: You are a hospital physician, writing for the family doctor.
   FORMAT: Five headings. Maximum 250 words.
   CONSTRAINTS: Add no findings, doses, or diagnoses. No hedging.
   Write a discharge summary for my patient.
```
