---
title: Data dictionaries, and AI as a reader
teaching: 3
exercises: 7
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain the minus-26 mean, and get the correct answer from tidy data.
- Write a data dictionary for a tidy table.
- Use the data dictionary as context when asking an AI tool about your data.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What should I record about my data, and where?
- How do I help an AI tool understand my data?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Back to minus 26

Sipho entered these values for North Beach in 2024:

`308, 54, -999, 55 cfu, 114, <10, 252, 115`

Spreadsheet `AVERAGE` keeps the six cells that are numbers, including
`-999`, and silently skips the two that are text:

(308 + 54 − 999 + 114 + 252 + 115) / 6 = **−26.0**

The tidy file records the same field sheet as six measured counts
(308, 54, 55, 114, 252, 115), one sample below detection, and one missing
because the bottle broke. The mean of the measured counts is **149.7**
(n = 6).

Both numbers came from the same field sheet. Only one survives a thesis
examiner. An AI assistant given the messy sheet will happily report the
other.

::::::::::::::::::::::::::::::::::::::::: callout

## See it in Python (optional)

`demo_messy_vs_tidy.py` in the lesson data reads both files and prints both
means. Run it from the folder holding the data:

```bash
python demo_messy_vs_tidy.py
```

```output
Messy mean : -26.0 <- '-999' counted as data; '55 cfu' and '<10' silently dropped
Tidy mean  : 149.7 (n = 6 measured; 1 below detection; 1 missing with a stated reason)
```

The messy code is what an AI assistant typically writes when asked for a
quick mean: read the column, convert to numbers, average. It runs without an
error. That is the danger.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Metadata: data about your data

A tidy table holds the values. It does not say what `below_detection`
means, what the detection limit was, or which site names are allowed. That
information is **metadata**, and it belongs in plain-text files kept beside
the data, never inside the table.

Two files cover most needs:

- a **data dictionary**: one row per column, saying what each column means;
- a **README**: what the dataset is, who made it, how it is organised, and
  what may be done with it ([episode 7](07-project-organisation.md)).

Many fields have metadata standards. The
[Digital Curation Centre](https://www.dcc.ac.uk/resources/metadata-standards/list)
keeps a list. Where none exists, ask: *what would a stranger need to use
this data without talking to me?*

## A data dictionary

Here is part of `beach_water_quality_data_dictionary.csv`:

| column | description | type | units_or_format | allowed_values_or_notes |
| --- | --- | --- | --- | --- |
| site | Beach sampling site | category | | North Beach, Addington, uShaka, Umhlanga Main |
| sample_date | Date the sample was collected | date | YYYY-MM-DD | |
| enterococci_cfu_100ml | Enterococci count | number | cfu per 100 mL | Blank when not measured, below detection or above range |
| below_detection | Count below detection limit | boolean | | TRUE means < 10 cfu/100 mL; count left blank |
| missing_reason | Why no measurement exists | category | | blank, bottle_broken, not_sampled_rough_sea |

::::::::::::::::::::::::::::::::::::::: challenge

## Exercise: write the dictionary

Without looking at the file, write dictionary entries for these columns of
`beach_water_quality_tidy.csv`: `sample_id`, `collector`,
`above_count_range`, `water_temp_c` and `notes`.

For each, give: what it means, its type, its units or format, and its
allowed values.

:::::::::::::::: solution

## Solution

Compare yours with `beach_water_quality_data_dictionary.csv`. Typical gaps:
the upper count limit for `above_count_range` (2000 cfu/100 mL), the unit
for temperature, and the rule that `sample_id` is never reused.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## The data dictionary is the prompt

An AI tool knows nothing about your project. Given only a CSV, it guesses
what `below_detection` means and what to do with blank counts. Given the
CSV *and* the dictionary, it can follow your definitions, and you can check
that it did.

A prompt that works:

```text
Attached: beach_water_quality_tidy.csv and its data dictionary.
Using only rows where enterococci_cfu_100ml is not blank, give the mean
count per site per year, with n. Report separately how many samples per
site were below detection, above the count range, or missing, and why.
Show the code you used.
```

Note the last line. Asking for the code lets you check the calculation,
rather than trusting a number.

::::::::::::::::::::::::::::::::::::::: challenge

## Exercise: messy versus tidy (demonstration)

If an approved AI tool is available, ask it for the mean count at North
Beach in 2024 twice: once giving it `beach_water_quality_MESSY.xlsx`, and
once giving it the tidy CSV with the data dictionary.

Which answer would you put in a thesis or a report? What did you need to
check before trusting either?

:::::::::::::::: solution

## Discussion

Answers vary between tools and between runs. With the messy file, look for
whether the tool noticed `-999`, `<10`, `TNTC`, the `55 cfu` cell and the
two-table layout, or quietly worked around them. With the tidy file and
dictionary, the answer should be 149.7 with n = 6, and the code should be
easy to check.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Calculations on messy data can be confidently wrong, in a spreadsheet or by an AI tool.
- Keep metadata in plain-text files beside the data: a data dictionary and a README.
- Give an AI tool the data dictionary with the data, and ask for the code it used.

::::::::::::::::::::::::::::::::::::::::::::::::::
