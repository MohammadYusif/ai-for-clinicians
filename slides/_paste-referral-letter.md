<!-- Generated from day1/m2-prompting.qmd by tools/build_prompt_library.py. Do not edit. -->

```text
ROLE: You are a family physician, writing a referral letter to a cardiologist who has not met the patient.
CONTEXT: This is a referral for a new problem. Use ONLY the facts below. If something needed is missing, write [MISSING: what] instead of guessing.
FACTS:
- 71 M. Hypertension, on amlodipine 5 mg once daily. Allergy: penicillin (rash). Ex-smoker, stopped 10 years ago.
- 3 weeks of breathlessness on exertion: now stops after about 1 block, previously 3 to 4 blocks. Occasional "fluttering". No chest pain, no syncope, no leg swelling.
- Exam: pulse irregularly irregular, about 108. BP 132/80. SpO2 97% on room air. JVP not raised. Chest clear. No peripheral edema.
- ECG today: atrial fibrillation, ventricular rate 112, no acute ST changes. No earlier ECG available to compare.
- Labs today: Hb 138 g/L, creatinine 96 µmol/L (eGFR 73 mL/min/1.73 m²), potassium 4.4 mmol/L, TSH 2.1 mIU/L.
- Not yet done: echocardiogram. Not on anticoagulation. No previous atrial fibrillation.
- CHA2DS2-VASc: age 65 to 74 (1) plus hypertension (1) = 2.
- Question for cardiology: rate versus rhythm strategy, and the anticoagulation decision. Asking for an appointment within 2 weeks. Patient prefers an Arabic-language consultation.
FORMAT: A letter with no headings. Paragraph 1: the question, then the urgency. Paragraph 2: only the history and findings that bear on the question. Paragraph 3: what has and has not been done. End with the allergy and the language preference. Maximum 200 words.
CONSTRAINTS: The allergy must appear. Do not add findings, doses, or diagnoses that are not in the facts. Do not answer the question or recommend a treatment: that is the cardiologist's decision. No hedging phrases. Keep every value and unit exactly as written.
```
