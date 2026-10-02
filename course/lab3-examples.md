# Lab 3: examples and answer keys

Trainer only. These are the two prepared examples for Lab 3 part 2, with their source cards and answer keys.
They are deliberately **not** on a page, in a deck, or in a deck's speaker notes: a participant who read them
first would lose the exercise. The repository is public, so this file is readable by anyone who goes looking;
what matters is that nobody meets the examples by following the course.

Share an example on the call from a private copy (the claude.ai deck, or this file). Show the text first and
the source card second, and keep the key to yourself until the "call it" round.

Two prepared examples for Part 2. Both are fictional and non-clinical: a made-up day clinic, its reminder pilot and a training workshop. Every clinic, document, number and name is invented for this exercise; none exists. Each carries the practice-output label because each contains deliberately unreliable content. The planted errors are generic (a figure, a document number, a citation year, a citation that cannot be found), never a clinical fact. Share the text first and the source card second, keep the key to yourself until the call-it round, and reveal by asking. The card is "the only documents that exist for this exercise", so could-not-find has a clear meaning.

## Example A: reminder pilot summary (three planted errors)

Text to share (`lab3-example-a`):

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

## Example B: workshop summary (two planted errors)

Text to share (`lab3-example-b`):

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
