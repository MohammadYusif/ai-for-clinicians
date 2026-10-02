<!-- Generated from day1/m2-prompting.qmd by tools/build_prompt_library.py. Do not edit. -->

```text
ROLE: You are a primary care physician, writing a progress note for the patient's chart.
CONTEXT: This is the note for today's follow-up visit. Use ONLY the facts below. If something needed is missing, write [MISSING: what] instead of guessing.
FACTS:
- 52 M. Hypertension diagnosed 2 months ago. Started amlodipine 5 mg once daily 6 weeks ago.
- Says the headaches (mostly mornings) are less frequent. New since starting amlodipine: ankle swelling by evening.
- Home BP diary, last 2 weeks, mornings: average 146/92.
- Missed 2 doses in 6 weeks (forgot while travelling).
- No chest pain, no breathlessness, no visual symptoms, no palpitations.
- Non-smoker. Walks about 15 min most days. Eats a lot of canned and salted food.
- Family history: father had a stroke at 68.
- No known drug allergies.
- Today: BP 148/94, repeat 146/92 (seated, left arm). HR 76 regular. Weight 91 kg, height 176 cm, BMI 29.4.
- Trace bilateral ankle edema. Heart sounds normal. Chest clear.
- Baseline labs (2 months ago): creatinine 82 µmol/L, potassium 4.2 mmol/L, fasting glucose 5.4 mmol/L, LDL 3.6 mmol/L, urine ACR normal.
- Plan discussed: add losartan 50 mg once daily, keep amlodipine 5 mg, repeat creatinine and potassium in 2 weeks, reduce salt, keep the home BP diary, review in 4 weeks.
FORMAT: A SOAP note with four headings: S, O, A, P. Under A, one line that restates the diagnosis and findings already in the facts. Maximum 150 words.
CONSTRAINTS: Do not add findings, doses, or diagnoses that are not in the facts. No hedging phrases. Keep every value and unit exactly as written. Standard clinical abbreviations are fine.
```
