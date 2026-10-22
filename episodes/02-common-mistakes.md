---
title: Common mistakes
teaching: 0
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- Recognise and fix common spreadsheet formatting problems.
- Explain how each problem misleads a script or an AI tool.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What are the common formatting problems, and how do I avoid them?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

This episode is a reference. Do not teach it line by line; refer to it
during the debrief of the "spot the mess" exercise.

::::::::::::::::::::::::::::::::::::::::::::::::::

Each problem below appears in `beach_water_quality_MESSY.xlsx`. The cell
reference tells you where to look.

- [Multiple tables on one sheet](#multiple-tables-on-one-sheet)
- [Multiple tabs for the same kind of data](#multiple-tabs-for-the-same-kind-of-data)
- [Blanks and zeros](#blanks-and-zeros)
- [Problematic null values](#problematic-null-values)
- [Censored values: below detection, too many to count](#censored-values-below-detection-too-many-to-count)
- [Inconsistent categories](#inconsistent-categories)
- [Formatting that carries meaning](#formatting-that-carries-meaning)
- [Merged cells](#merged-cells)
- [Comments and units in cells](#comments-and-units-in-cells)
- [More than one value in a cell](#more-than-one-value-in-a-cell)
- [Calculations and repeated headers inside the data](#calculations-and-repeated-headers-inside-the-data)
- [Problematic column names](#problematic-column-names)
- [Special characters](#special-characters)
- [Metadata inside the data table](#metadata-inside-the-data-table)
- [Dates](03-dates-as-data.md)

## Multiple tables on one sheet

*Where:* `2024 Sipho`, columns A-D and F-I.

A computer treats each row as one observation. Two tables side by side make
it read a North Beach sample and an Addington sample as one record, with two
columns of the same name.

**Fix:** one table, with a `site` column.

## Multiple tabs for the same kind of data

*Where:* the `2024 Sipho` and `2025_Lerato (final) v2` tabs.

Separate tabs invite inconsistency: here the two collectors used different
column names, orders and units. Before any analysis someone must combine
them, and must do it correctly.

**Fix:** one table, with `collector` and date columns. When a long sheet
hides its header, freeze the top row (View > Freeze Panes) rather than
repeating the header.

## Blanks and zeros

*Where:* `2024 Sipho`, G9.

A zero is a measurement. A blank means nothing was recorded. Is G9 a count of
zero, a sample not taken, or a value someone forgot to type? Nobody can tell,
and the answer changes the mean.

**Fix:** record true zeros as `0`. Leave a cell blank only when no
measurement exists, and record why in a separate column (next section).

## Problematic null values

*Where:* `2024 Sipho`, B7 (`-999`).

Many programs treat `-999` as a number. Spreadsheet `AVERAGE` does, which is
why the North Beach mean in the `Summary` tab is negative.

| Null value | Problem | Recommendation |
| --- | --- | --- |
| 0 | Indistinguishable from a true zero | Never use |
| Blank | Hard to tell missing from overlooked, or from a space | Best option, with a reason column |
| -999, 999 | Read as numbers by many programs; enters calculations | Avoid |
| NA, na | Can be a real code; turns a numeric column into text in some tools | Acceptable in R |
| N/A, NULL, None, "No data", "Missing", -, . | Inconsistent support; changes the column's type | Avoid |

*Adapted from White et al. (2013),
[Nine simple ways to make it easier to (re)use your data](https://peerj.com/preprints/7/).*

**Fix:** a blank cell, plus a `missing_reason` column that says why
(`bottle_broken`, `not_sampled_rough_sea`). The reason is information;
keeping it lets you, or a model, tell a broken bottle from a rough sea.

## Censored values: below detection, too many to count

*Where:* `2024 Sipho`, B10 and G7 (`<10`); G6 (`TNTC`).

Laboratory and instrument data often hit a limit. The method cannot count
below 10 cfu/100 mL, or the plate is "too numerous to count". Typing `<10`
or `TNTC` puts text in a numeric column. Some programs then treat the whole
column as text; others drop those cells silently. Replacing them with `0`,
`5`, `10` or `2000` invents data.

**Fix:** leave the count blank and set a flag column:
`below_detection = TRUE` or `above_count_range = TRUE`. Record the limits in
the data dictionary. How to treat censored values in analysis is a
statistical decision; the data table's job is to record them honestly.

## Inconsistent categories

*Where:* `2025_Lerato (final) v2`, column A.

North Beach appears as `North Beach`, `north beach`, `North Bch` and
`North Beach ` (with a trailing space). Umhlanga appears three ways,
Addington three, uShaka three. People see four beaches. A computer sees
thirteen. A machine-learning model trained on this column learns thirteen
classes.

**Fix:** agree a fixed list of values, enforce it with a drop-down
([episode 4](04-quality-control.md)), and record the list in the data
dictionary. For cleaning many variants at once, OpenRefine's clustering
feature is effective; see the
[Data Carpentry OpenRefine lesson](https://datacarpentry.org/OpenRefine-ecology-lesson/).

## Formatting that carries meaning

*Where:* red cells in both tabs; yellow rows 5-6 in Lerato's tab.

Red means "exceeds guideline" to Sipho. Yellow means "exclude" to Lerato,
and to nobody else. Colour does not survive export to CSV, and no analysis
program or AI tool reads it.

**Fix:** a column for anything you would colour. Exceedance can be
calculated from the count; exclusion needs an `exclude` column and a reason.

## Merged cells

*Where:* `2024 Sipho`, A1 and row 3.

Merged cells look tidy and break almost everything that reads the file.

**Fix:** restructure so that nothing needs merging. Here, the merged beach
heading becomes a `site` column.

## Comments and units in cells

*Where:* `2024 Sipho`, B8 (`55 cfu`), the comment on B6; Lerato column D
(`23.0C`).

Spreadsheet comments are invisible to other programs. Units typed into a
cell turn a number into text.

**Fix:** a `notes` column for comments. Units in the column header
(`water_temp_c`), with one unit per column. Lerato's row 14 holds 74.1, a
temperature in Fahrenheit among Celsius values; convert it (23.4 °C) and
note the conversion in your processing log.

## More than one value in a cell

*Where:* Lerato column E (`HW+2 / calm`) and F8 (`1M swimmer, 2F swimmers`).

One cell holds tide state and sea state; another holds two counts and two
categories. Neither can be sorted, filtered or analysed.

**Fix:** one column per value: `tide`, `sea_state`, or a count column per
category.

## Calculations and repeated headers inside the data

*Where:* Lerato row 10 (`Mean North Beach`) and row 19 (header repeated).

A summary row is read as one more observation. A repeated header turns every
column into text from that row on.

**Fix:** keep raw data free of calculations. Calculate in a separate sheet,
or better, in a script.

## Problematic column names

*Where:* `Entero (cfu/100mL)`, `Temp °C`, `Site / tide`.

Spaces, brackets, slashes and symbols cause errors in most analysis tools.
Abbreviations that make sense today will not in six months.

| Good name | Good alternative | Avoid |
| --- | --- | --- |
| enterococci_cfu_100ml | EnterococciCfu100ml | Entero (cfu/100mL) |
| water_temp_c | WaterTempC | Temp °C |
| sample_date | SampleDate | Date |
| missing_reason | MissingReason | ? |
| site | Site | Site / tide |

## Special characters

*Where:* Lerato F12, pasted from WhatsApp, holds an em-dash and curly
quotation marks.

Text pasted from messaging apps or word processors brings invisible
characters, line breaks and non-standard quotes. These cause encoding errors
and split rows when the file is exported.

**Fix:** treat a text cell like a simple web form: letters, numbers,
spaces, basic punctuation. No line breaks.

## Metadata inside the data table

*Where:* `2024 Sipho`, A1 (title) and A15 (legend).

Information about the data is essential, but inside the table it breaks the
grid. Is row 15 an observation?

**Fix:** a separate plain-text file next to the data: a README and a data
dictionary ([episode 6](06-data-dictionary.md)).

*Text on metadata adapted from Research Data
[MANTRA](https://mantra.ed.ac.uk/), EDINA and Data Library, University of
Edinburgh, CC-BY 4.0, via the original Data Carpentry lesson.*

:::::::::::::::::::::::::::::::::::::::: keypoints

- Use one table per sheet and one sheet per kind of data.
- Record zeros as zeros; leave missing values blank and record why.
- Flag censored values in a column; never type `<10` or `TNTC` into a number column.
- Fix category spellings with a controlled list.
- Do not use colour, merged cells or comments to carry information.
- Put units in headers and one value in each cell.
- Keep calculations, legends and titles out of the data table.

::::::::::::::::::::::::::::::::::::::::::::::::::
