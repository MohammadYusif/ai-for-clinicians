<!-- Generated from day2/m4-notes-and-audiences.qmd by tools/build_prompt_library.py. Do not edit. -->

```text
ROLE: You are a surgeon, writing to the patient's community physician or clinic, who will see the patient next and has not seen the hospital record.
CONTEXT: Write a short handover letter from the fact sheet below. Use ONLY the facts below. If something needed is missing, write [MISSING: what] instead of guessing.
FACTS:
[paste the checked fact sheet]
FORMAT: Start with "Dear Colleague," and end with "[your name and role]". Begin with what was done and why. Then, in this order: status at discharge, medicines started, what the patient was told to do, follow-up arranged, and the warning signs the patient was told to return for. Write for a clinician and focus on what the reader must know or do; leave out detail that would not change their care. Maximum 150 words.
CONSTRAINTS: Do not add findings, doses, or diagnoses that are not in the facts. Keep every number and unit exactly as in the sheet. Include every item of the "Return sooner for" list. Use the placeholder [PATIENT NAME AND FILE NUMBER] wherever the patient would be named; I will add it myself. Do not invent a recipient name, date or contact detail. No hedging phrases.
```
