---
title: Session prompts
---

The session is one exercise in eight steps. Work in pairs. Do each step when
the presenter calls it, then stop and listen to the debrief. The two checks
are marked against a key before you move on.

Download the data first: see [Setup](setup.md).

## Topic 1 · The table a machine can read

**Step 1 · Find the mean (0-5 min).**
Open `beach_water_quality_MESSY.xlsx`. Copy the `2024 Sipho` tab (right-click
the tab > Move or Copy > Create a copy) and work only on the copy. Use
`=AVERAGE()` to find the mean Enterococci count at North Beach in 2024.
Would you put this number in a thesis?

**Step 2 · What stops a computer? (5-10 min).**
List everything in the workbook that would stop a program, or an AI tool,
from calculating the mean count per beach correctly. Look at both data tabs
and the `Summary` tab.

**Step 3 · Sort and filter (10-15 min).**
On your copy, select all of Sipho's North Beach block and sort it by the
count column, largest to smallest. Where do the problem values end up? Then,
on Lerato's tab, select the `Site` column and switch on **Data > Filter**.
How many distinct beach names does the drop-down list? How many beaches were
sampled?

**Step 4 · What day is A9? (15-20 min).**
What date is in cell A9 of Sipho's tab? Copy the North Beach block to a new
tab, save that tab as **CSV UTF-8**, and open the CSV in a text editor
(Notepad, TextEdit). Then open the CSV again in Excel. What happened to the
dates?

**Check 1 (20-30 min).**
Compare your list from Step 2 with the presenter's key. Then open
`beach_water_quality_tidy.csv` and recompute the North Beach 2024 mean from
the rows where `enterococci_cfu_100ml` is not blank. Which number is right,
and why was the first one wrong?

## Topic 2 · Giving the model its context

**Step 5 · Write the dictionary (30-35 min).**
Without opening the dictionary file, write one line for each of these columns
of the tidy file: `sample_id`, `collector`, `above_count_range`,
`water_temp_c`, `notes`. For each, give its meaning, type, units or format,
and allowed values. Then compare with
`beach_water_quality_data_dictionary.csv`.

**Step 6 · Ask the model, messy (35-40 min).**
Start a new chat. Attach `beach_water_quality_MESSY.xlsx` and ask:

```text
What was the mean Enterococci count at North Beach in 2024?
```

Write down the answer. Did the model mention `-999`, `<10` or `55 cfu`?

**Step 7 · Ask the model, tidy (40-45 min).**
Start another new chat. Attach `beach_water_quality_tidy.csv` and
`beach_water_quality_data_dictionary.csv`, and paste this prompt:

```text
Attached: beach_water_quality_tidy.csv and its data dictionary.
Using only rows where enterococci_cfu_100ml is not blank, give the mean
count per site per year, with n. Report separately how many samples per
site were below detection, above the count range, or missing, and why.
Show the code you used.
```

Compare the North Beach 2024 answer with Step 6. Read the code: which rows
did it keep?

**Step 8 · Your own data (45-50 min).**
On paper: sketch the folder layout for your own project, using `raw`,
`processed`, `docs`, `scripts` and `outputs`. Write one log line recording
Step 7 (date, initials, what was done, tool, prompt, how you checked it).
Then decide, for each case below, whether it may go into a free, public chat
model: yes, no, or only with conditions.

1. The synthetic beach dataset from this session.
2. Your unpublished thesis data, collected under a funder agreement.
3. A class list with student numbers and marks, which you want "tidied up".
4. Interview transcripts in which participants are named.

**Check 2 (50-60 min).**
Compare your answers to Steps 6, 7 and 8 with the presenter's key. Write on
your sticky note one change you will make to your own data this week.
