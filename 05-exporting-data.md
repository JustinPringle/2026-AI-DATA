---
title: Exporting data
teaching: 3
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- Store data in open, plain-text formats.
- Export a spreadsheet to CSV safely.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- In what format should I keep and share data?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Why not keep data as .xlsx?

- It is a proprietary format; other programs, and future versions, may read
  it differently.
- It hides things that are not data: colour, comments, formulas, merged
  cells, several tabs.
- Most data repositories, many journals and many funders require open
  formats.
- Dates stored in Excel's internal numbers can shift when files move between
  versions and systems ([episode 3](03-dates-as-data.md)).

## Use CSV (or TSV)

A CSV (comma-separated values) file is plain text: one row per line,
columns separated by commas. Any program can open it, including a text
editor, Python, R, a database and every AI tool. It holds one table, no
colour, no formulas and no comments. That is the point: it keeps only the
data.

To export from Excel: **File > Save As**, choose **CSV UTF-8
(Comma delimited) (.csv)**. Excel warns that only the active sheet is
saved and that some features will be lost. Both warnings are expected.

UTF-8 keeps characters such as `°`, `é` and isiZulu names intact.

You can still open a CSV in Excel. Keep the tidy CSV as your master copy
and treat any .xlsx as a working view.

::::::::::::::::::::::::::::::::::::::::: callout

## Commas inside data, and the decimal comma

If values contain commas (notes, addresses), make sure they are quoted, or
use tab-separated values (TSV). Some computers use a comma as the decimal
separator, so `22,5` may mean 22.5. Check your regional settings, and state
the decimal separator in the data dictionary. A full stop is the safe
choice for shared data.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Line endings

Windows ends lines with two hidden characters (CR LF); Linux and macOS use
one (LF). Most modern tools handle both. If a script reports values such as
`23.6\r`, convert the line endings with your text editor or a tool such as
`dos2unix`.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Keep master data in open, plain-text formats such as CSV or TSV, encoded as UTF-8.
- CSV stores only the data: one table, no formatting, no formulas.
- State the delimiter, decimal separator and encoding in the data dictionary.

::::::::::::::::::::::::::::::::::::::::::::::::::
