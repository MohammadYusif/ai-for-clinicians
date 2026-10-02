<!-- Generated from day1/m2-prompting.qmd by tools/build_prompt_library.py. Do not edit. -->

```text
ROLE: You are a hospital physician on an internal medicine ward, writing a discharge summary for the patient's primary care physician.
CONTEXT: This is the summary that goes with the patient on the day of discharge. Use ONLY the facts below. If something needed is missing, write [MISSING: what] instead of guessing.
FACTS:
- Diagnosis this admission: pneumonia, right lower lobe.
- 64 F. Type 2 diabetes (metformin 1000 mg twice daily), hypertension (amlodipine 5 mg once daily). No known drug allergies. Non-smoker.
- Presented with 4 days of cough with yellow-green sputum, fever, and right-sided chest pain worse on deep breathing.
- On arrival: T 38.9 °C, HR 102, RR 24, BP 118/70, SpO2 91% on room air.
- CXR: right lower lobe consolidation. WBC 15.2 x10^9/L, CRP 168 mg/L, creatinine 88 µmol/L, glucose 11.8 mmol/L, HbA1c 63 mmol/mol (7.9%).
- Blood cultures: no growth at 48 h, final result pending. Sputum culture sent, result pending at discharge.
- Treatment: ceftriaxone 1 g IV once daily for 3 days plus azithromycin 500 mg once daily for 3 days (hospital days 1 to 3). Oxygen off from hospital day 3. Afebrile since hospital day 3.
- Step-down to oral amoxicillin-clavulanate 875/125 mg twice daily started on hospital day 4. Total planned antibiotic course 7 days, so 3 more days at home after discharge.
- Insulin sliding scale in hospital; glucose 7 to 10 mmol/L over the last 24 h. Metformin continued.
- At discharge: T 36.8 °C, HR 78, RR 16, BP 122/74, SpO2 96% on room air. Walking on the ward, eating well.
- Discharge medicines: amoxicillin-clavulanate 875/125 mg twice daily for 3 more days, metformin 1000 mg twice daily, amlodipine 5 mg once daily, paracetamol 1 g up to four times daily if needed.
- Influenza and pneumococcal vaccination status: not documented.
- Follow-up: primary care in 1 week. Chest imaging at 6 weeks only if symptoms persist. Return sooner for worse breathing, fever after 48 h of tablets, confusion, chest pain, or coughing blood.
FORMAT: Five headings, in this order: Diagnoses, Hospital course, Discharge medicines, Pending results, Follow-up. Discharge medicines as a list, one line each. Maximum 250 words.
CONSTRAINTS: Copy the discharge medicines exactly as listed in the facts: no change to any name, dose, frequency or duration. Do not add findings, doses, or diagnoses that are not in the facts. If a result is pending, say it is pending; do not guess the result. No hedging phrases. Keep every value and unit exactly as written.
```
