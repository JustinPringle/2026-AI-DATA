---
title: Instructor Notes
---

## The session in one sentence

One hour, run as a single exercise: the presenter gives a prompt, pairs carry
it out on the beach water quality workbook, and the presenter draws the
principle from what they find. Learners have the prompts on the
[Session prompts](../learners/prompts.md) page; this page holds the run sheet,
the debrief points and the answer keys.

## Place in the workshop

This is the last session of the *Using AI in Postgraduate Studies* workshop.
It follows Prof Randhir Rawatlal's session, *Working with generative AI on a
postgraduate project*, and deliberately repeats his practices on a dataset,
so learners meet each one a second time in use. Name the link aloud each time
it comes up. The **RR** column below gives the minute in his session plan.

| Here | RR | His point | How it returns here |
| --- | --- | --- | --- |
| Step 1 | 0-5 | Raw data never edited | Copy the tab before touching it |
| Step 3 | 45-50 | Flag faulty data | Flag columns for `<10`, `TNTC`; a reason column for blanks |
| Check 1 | 40-45 | Test on cases with known answers | The −26.0 fails a sanity check; 149.7 is the known answer for Topic 2 |
| Step 5 | 5-10 | Standing instructions read every session | The data dictionary is the data's standing instructions |
| Step 7 | 30-34 | Repeated, checkable work goes to a tool | Ask for the code, not just the number |
| Step 8 | 0-5, 10-13 | Repository; log line; which model may read which file | `raw`/`processed` folders; a log line for Step 7; four POPIA cases |

If the order of sessions changes, change "as Prof Rawatlal showed" to "as
Prof Rawatlal will show" and keep the links.

## Before the session

- **Data.** Check that the links on the [Setup](../learners/setup.md) page
  download. Put the zip on the LAN share, or on the desktop of each LAN
  machine, as a fallback.
- **LAN.** Confirm that the LAN machines have Excel or LibreOffice, a browser,
  and access to chatgpt.com, claude.ai and gemini.google.com.
- **Chat models.** The demonstrators test Steps 6 and 7 on a free account
  with each of ChatGPT, Claude and Gemini the day before, note any upload
  limits, and keep screenshots of the answers for the projector.
- **Projector.** The presenter's machine has the workbook, the tidy CSV and a
  logged-in chat model open in separate windows, at large font size.
- **Print.** A few copies of both data tabs of the messy workbook, for pairs
  without a device, and the prompt sheet.
- **Sticky notes.** Two colours: one for "stuck", one for the closing
  commitment.

## Demonstrators

Two demonstrators circulate, one on each side of the room (or one in the LAN
if it is used). Brief them on:

- Excel on Windows and macOS, LibreOffice and Google Sheets menus for
  **Move or Copy**, **Sort**, **Filter**, **Save As CSV UTF-8** and
  **Data Validation**.
- Sorting a whole block, never one column ("Expand the selection").
- Attaching a file in each chat model, and pasting CSV text when uploads fail.
- Not giving answers during Steps 2 and 5; ask "what would a program see
  here?" instead.

## Run sheet

### Topic 1 · The table a machine can read

**0-5 · Step 1, find the mean.**
Prompt: "Copy a tab, then use AVERAGE for North Beach 2024."
Expected: −26.0. Ask: "Would you put this in a thesis? A count of bacteria
cannot be negative." Point out that they copied the tab first: raw data are
never edited (RR 0-5). Do not explain the −26 yet.

**5-10 · Step 2, what stops a computer?**
Prompt: "List everything that would stop a program, or a model, reading this
sheet." Take four or five answers. From them, state the three rules: each
variable in a column, each observation in a row, one value in each cell. Use
Sipho's two side-by-side blocks as the example
([episode 1](../episodes/01-format-data.md)).

**10-15 · Step 3, sort and filter.**
Prompt: "Sort the counts largest to smallest; filter the site column."
Expected: text (`55 cfu`, `<10`) sorts above the numbers, `-999` sits at the
bottom of them, blanks at the very end. Lerato's filter shows thirteen names
for four beaches. Debrief: a blank plus a `missing_reason` column, flag
columns for censored values (RR 45-50), a fixed list enforced by a drop-down
([episode 4](../episodes/04-quality-control.md)). Demonstrate the drop-down in
one minute if time allows.

**15-20 · Step 4, what day is A9?**
Prompt: "What date is A9? Save as CSV UTF-8, open in a text editor, then in
Excel." Expected: A9 `04/02/2024` reads as 4 February in South Africa; the
weekly schedule shows it is 2 April. `12 Mar` gains the current year on
reopening. Debrief: ISO 8601, CSV UTF-8 as the master copy
([episodes 3](../episodes/03-dates-as-data.md) and
[5](../episodes/05-exporting-data.md)).

**20-30 · Check 1.**
Pairs tick their Step 2 list against Key 1 (on the projector), then compute
the mean from the tidy CSV. Explain the −26 now:
(308 + 54 − 999 + 114 + 252 + 115) / 6 = −26.0. `AVERAGE` counted `-999` as
a number and silently skipped `55 cfu` and `<10` because they are text. The
measured counts give 149.7, n = 6. Point out that 149.7 is now a *known
answer*: anything that reports otherwise in Topic 2 is wrong (RR 40-45).

### Topic 2 · Giving the model its context

**30-35 · Step 5, write the dictionary.**
Prompt: "Without looking, define `sample_id`, `collector`,
`above_count_range`, `water_temp_c` and `notes`." Then compare with the
dictionary file. Typical gaps: the upper count limit (2000 cfu/100 mL), the
temperature unit, that `sample_id` is never reused. Link: the dictionary is
to the data what Prof Rawatlal's initialisation file is to a project, the
standing instructions the model reads every time (RR 5-10).

**35-40 · Step 6, ask the model, messy.**
Prompt: "Ask a free chat model for the North Beach 2024 mean from the messy
workbook." Pairs write down the answer and whether the model mentioned
`-999`, `<10` or `55 cfu`. Answers vary by model and by run; collect three or
four aloud. That variation is the point.

**40-45 · Step 7, ask the model, tidy.**
Prompt: "Attach the tidy CSV and dictionary, use the prompt on the sheet, and
ask for the code." Pairs compare with the known answer and read which rows
the code kept. Link: asking for the code turns a conversation into a tool you
can check and re-run (RR 30-34).

**45-50 · Step 8, your own data.**
Prompt: "Sketch your project folder, log Step 7 in one line, and decide the
four cases." Keep the debrief short; Prof Rawatlal has covered the repository
and data classes (RR 0-5, 10-13). Stress only what is new: `raw` is
read-only and files flow one way to `processed` and `outputs`
([episode 7](../episodes/07-project-organisation.md)).

**50-60 · Check 2.**
Key 2 on the projector. Close by asking each learner to write on a sticky
note one change they will make to their own data this week.

## Key 1 · Problems planted in the messy workbook

Nineteen problems. Pairs typically find eight to twelve. Each is described in
[episode 2](../episodes/02-common-mistakes.md).

| # | Problem | Where |
| --- | --- | --- |
| 1 | Two tables side by side on one tab | `2024 Sipho`, A-D and F-I |
| 2 | Two tabs for one kind of data, with different column names, order and units | `2024 Sipho`, `2025_Lerato (final) v2` |
| 3 | Merged cells | Sipho A1:I1, A3:D3, F3:I3 |
| 4 | Title and legend inside the data | Sipho A1, A15 |
| 5 | Blank: zero, missing or forgotten? | Sipho G9 |
| 6 | `-999` as a missing-value code, counted by `AVERAGE` | Sipho B7; Summary B3 gives −26.0 |
| 7 | Censored values typed as text | `<10`: Sipho B10, G7; Lerato C6, C30. `TNTC`: Sipho G6 |
| 8 | Units typed into number cells | `55 cfu` Sipho B8; Lerato C5, C13, C21, C28, C35. `23.0C` throughout Lerato column D |
| 9 | Numbers stored as text | Sipho temperatures C6, C7, C9, C10, C12 and H6, H7, H9, H10, H12 |
| 10 | Five date formats, one with no year | Sipho A5-A9; Lerato column B |
| 11 | Ambiguous day and month | Sipho A9 `04/02/2024` (2 April); Lerato B5, B11, B16, B22, B27, B32 are month-first. B11 `03/04/2025` is 4 March, not 3 April |
| 12 | Thirteen spellings of four beaches, including trailing spaces | Lerato column A (A5, A9 end in a space) |
| 13 | Colour carries meaning | Red = above a guideline (Sipho, Lerato); yellow = "exclude" (Lerato rows 5-6); Summary B5 asks for a count of red cells |
| 14 | Information in a cell comment | Sipho B6: "Retest? Lab said contamination possible" |
| 15 | More than one value in a cell | Lerato column E (tide / sea state); F8 (two counts, two categories) |
| 16 | A calculation inside the data | Lerato row 10, `Mean North Beach`, which averages only six of eight values (101.7) |
| 17 | Header repeated part-way down | Lerato row 19 |
| 18 | Fahrenheit among Celsius | Lerato D14, 74.1 °F = 23.4 °C |
| 19 | Problem column names and special characters | `Entero (cfu/100mL)`, `Temp °C`, `Site / tide`; Lerato F12 has an em-dash and curly quotes from WhatsApp; tab name `2025_Lerato (final) v2` |

**A trap worth showing.** Summary B4 gives the Addington 2024 mean as 102.8,
which matches the tidy answer. It is right by luck: there is no `-999` in
that column, and `AVERAGE` dropped `TNTC`, `<10` and the blank, which the
tidy calculation also excludes. A correct number from a broken method is
still a broken method.

## Key 2 · Model runs and the four cases

**Step 6 (messy).** No single right answer. Look for whether the model
noticed the two-table layout, treated `-999` as missing, and said what it did
with `<10` and `55 cfu`. Some models report −26.0; some report a number near
149.7 without saying which cells they dropped; a few ask a clarifying
question. Only the last behaviour is acceptable without checking.

**Step 7 (tidy).** The full answer, for checking any model's output:

| Site | Year | Mean (cfu/100 mL) | n | Below detection | Above range | Missing (reason) |
| --- | --- | --- | --- | --- | --- | --- |
| North Beach | 2024 | 149.7 | 6 | 1 | 0 | 1 (bottle_broken) |
| Addington | 2024 | 102.8 | 5 | 1 | 1 | 1 (not_sampled_rough_sea) |
| North Beach | 2025 | 112.4 | 7 | 1 | 0 | 0 |
| Addington | 2025 | 215.6 | 8 | 0 | 0 | 0 |
| uShaka | 2025 | 48.2 | 8 | 0 | 0 | 0 |
| Umhlanga Main | 2025 | 144.3 | 7 | 1 | 0 | 0 |

**Step 8 (four cases).**

1. **Yes.** The beach data are synthetic and CC-BY.
2. **Only with conditions.** Check the funder agreement; use an
   institution-approved tool.
3. **No,** not as it stands. Student numbers and marks are personal
   information under POPIA. Remove them first, or use an approved tool.
4. **No,** unless participants consented and the ethics approval allows it.
   Anonymise first.

A good log line for Step 7:

```text
2026-11-10  JP  Mean count per site and year from tidy CSV, with dictionary;
                Claude (free), prompt in docs/prompts/2026-11-10_means.txt;
                checked North Beach 2024 against known answer 149.7, n = 6.
```

## If there are no devices

- Steps 1-4: pairs mark problems on the printout; the presenter performs each
  prompt on the projector.
- Steps 6-7: a demonstrator runs both queries on the projector, or shows the
  screenshots taken the day before.
- Steps 5 and 8 need only paper.

## Common problems

- **Excel looks different on every machine.** Do not demonstrate menus at
  length; the demonstrators handle them pair by pair.
- **Opening files from inside the zip.** Excel opens them read-only. Unzip
  first.
- **Uploads refused on a free account.** Paste the CSV text into the chat
  instead; open the CSV in a text editor, select all, copy.
- **A quiet room at Step 2.** Start the list yourself with one problem, or ask
  a demonstrator for theirs.
