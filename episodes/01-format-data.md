---
title: Formatting data tables
teaching: 5
exercises: 12
---

::::::::::::::::::::::::::::::::::::::: objectives

- Describe the rules of tidy data.
- Identify what stops a computer from using a messy spreadsheet.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How should I lay out data in a spreadsheet?

::::::::::::::::::::::::::::::::::::::::::::::::::

## The most common mistake

The most common mistake is treating a spreadsheet like a notebook: relying
on context, notes in the margin, colour and the position of cells to carry
meaning. People can usually decode this. Computers cannot.

Set up a well-formatted table from the start, before you enter the first
result. Reorganising later costs far more, and every reorganisation risks
introducing errors.

## Three rules

1. **Each variable in its own column, each observation in its own row, one
   value in each cell.** A variable is something you measure or record:
   site, date, Enterococci count, water temperature. An observation is one
   sample.
2. **Leave raw data raw.** Copy the file before you clean it, and keep a
   plain-text log of every change you make.
3. **Keep explanations out of the cells.** Units go in the column header.
   Notes go in a notes column. Legends and definitions go in a separate
   file (a data dictionary, see [episode 6](06-data-dictionary.md)).

These rules are often called *tidy data*.

### An example

Sipho recorded each beach as its own block, side by side:

| NORTH BEACH | | | | ADDINGTON | | |
| --- | --- | --- | --- | --- | --- | --- |
| Date | Entero (cfu/100mL) | Temp °C | | Date | Entero (cfu/100mL) | Temp °C |
| 2024-03-05 | 308 | 23.6 | | 2024-03-05 | 91 | 22.5 |
| 12 Mar | 54 | 22.6 | | 12 Mar | TNTC | 20.8 |

To a computer, the first data row holds *one* observation with seven
values, two of them called "Date". The beach name sits in a merged heading
that no program will read.

The tidy version puts site in a column and gives each sample its own row:

| sample_id | site | sample_date | enterococci_cfu_100ml | above_count_range | water_temp_c |
| --- | --- | --- | --- | --- | --- |
| DBN-2024-001 | North Beach | 2024-03-05 | 308 | FALSE | 23.6 |
| DBN-2024-002 | North Beach | 2024-03-12 | 54 | FALSE | 22.6 |
| DBN-2024-009 | Addington | 2024-03-05 | 91 | FALSE | 22.5 |
| DBN-2024-010 | Addington | 2024-03-12 | | TRUE | 20.8 |

It is longer and less pretty. It is also the only one of the two that a
script, a database or an AI tool can use without guessing.

::::::::::::::::::::::::::::::::::::::::: callout

## Data entry and data analysis may want different layouts

A field sheet designed for fast entry on a boat may not be tidy. That is
acceptable, provided the conversion to a tidy table is written down and,
ideally, automated.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: challenge

## Exercise: spot the mess

Download `beach_water_quality_MESSY.xlsx` from the [Setup](../learners/setup.md)
page and open it.

Sipho sampled two beaches in 2024 and Lerato sampled four in 2025. Each kept
the data in their own way. You now own the data and want the mean
Enterococci count per beach.

With the person next to you, list everything in the workbook that would stop
you, or an AI tool, from calculating that mean correctly. For each problem,
write how you would fix it.

**Do not edit the original.** Copy a tab first.

:::::::::::::::: solution

## Solution

The workbook contains every mistake listed in
[the next episode](02-common-mistakes.md), and a few more. Among them:
two tables on one tab, merged headings, a title and a legend inside the
data, five different date formats, units typed into cells, `<10`, `TNTC`
and `-999` in a numeric column, colour used to flag exceedances, thirteen
spellings of four beach names, a mean calculated in the middle of the data,
a repeated header row, and a temperature in Fahrenheit among Celsius values.

The full answer key is in the [Instructor Notes](../instructors/instructor-notes.md).
The tidy result is `beach_water_quality_tidy.csv`.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Further reading

- Karl W. Broman and Kara H. Woo (2018). Data Organization in Spreadsheets.
  *The American Statistician*, 72(1), 2-10.
  [DOI: 10.1080/00031305.2017.1375989](https://doi.org/10.1080/00031305.2017.1375989)
- Hadley Wickham (2014). Tidy Data. *Journal of Statistical Software*, 59(10).
  [DOI: 10.18637/jss.v059.i10](https://doi.org/10.18637/jss.v059.i10)

:::::::::::::::::::::::::::::::::::::::: keypoints

- Put each variable in a column, each observation in a row, and one value in each cell.
- Never modify raw data; work on a copy and log your changes.
- Keep units in headers and explanations in a separate file.

::::::::::::::::::::::::::::::::::::::::::::::::::
