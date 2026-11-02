---
title: Going further
---

## After the session

The session covers what to do with data in a spreadsheet and how to hand them
to an AI tool. The next steps, roughly in order:

- **Clean messy categories at scale.** OpenRefine clusters spelling variants
  (thirteen beach names into four) and records every step it takes. See the
  [Data Carpentry OpenRefine lesson](https://datacarpentry.org/OpenRefine-ecology-lesson/).
- **Move the analysis into code.** A script repeats exactly; a spreadsheet
  and a chat conversation do not. Start with the Data Carpentry lessons in
  [Python](https://datacarpentry.org/python-ecology-lesson/) or
  [R](https://datacarpentry.org/R-ecology-lesson/), or ask a chat model to
  write the code and check it against a case with a known answer.
- **Track versions of scripts and text.** See
  [Version Control with Git](https://swcarpentry.github.io/git-novice/).
- **Publish your data.** A tidy CSV, a data dictionary and a README are most
  of what a data repository asks for. Read about the FAIR principles at
  [GO FAIR](https://www.go-fair.org/fair-principles/).

## Commas inside values

If a value contains a comma, such as a note reading `calm, clear`, a CSV
must enclose it in double quotes: `"calm, clear"`. Excel does this for you
when it saves a CSV. Trouble starts when files are built by hand or by a
script that ignores quoting: the comma splits the value across two columns.

If your data hold many commas, use tab-separated values (TSV) instead, and
say so in the data dictionary.

In South Africa, some computers are set to use a comma as the decimal
separator, so `22,5` means 22.5. Excel on such a computer may save a "CSV"
separated by semicolons. Check your regional settings, and use a full stop
as the decimal separator in shared data.
