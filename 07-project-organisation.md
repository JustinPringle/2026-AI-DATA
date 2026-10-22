---
title: Organising a project
teaching: 5
exercises: 3
---

::::::::::::::::::::::::::::::::::::::: objectives

- Lay out a project folder that separates raw data, processed data and outputs.
- Name files so they sort, and so people and programs can read them.
- Plan storage and backups for raw data.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How should I organise the files of a project?
- Where should I keep raw data, and how should I back it up?

::::::::::::::::::::::::::::::::::::::::::::::::::

A tidy table is one file. A thesis, a funded project or an office process
produces hundreds. The same principle applies at the level of folders:
organise so that someone else, including you in two years, can find things
without asking.

## A folder skeleton

```text
beach-water-quality/
  README.txt            what, who, conventions, rules for sharing and AI use
  data/
    raw/                original files exactly as received; read-only
    processed/          tidy files made from raw
  docs/                 data dictionary, protocols, permits, ethics approval
  scripts/              code that turns raw into processed, and processed into results
  outputs/              figures, tables, model results; can be regenerated
```

The rule that matters most: **files flow one way**, from `raw` to
`processed` to `outputs`. Nothing is ever written back into `raw`.

## Leave raw data raw

Raw data are the foundation. Every result must trace back to them.

- Make the `raw` folder read-only (right-click > Properties > Read-only on
  Windows; Get Info > Sharing & Permissions on macOS).
- Never open a raw file and save over it. Excel may change dates, drop
  leading zeros or convert codes even if you edit nothing.
- When raw data arrive from an instrument, a lab or a collaborator, record
  where they came from and when in the README.

## Name files for people and programs

A good file name says what the file holds, sorts correctly, and contains no
characters that break software.

| Avoid | Prefer |
| --- | --- |
| `Data final FINAL v2 (Lerato).xlsx` | `2025-03-04_beach-wq_enterococci_raw.xlsx` |
| `results new.csv` | `2025-05-12_beach-wq_enterococci_tidy_v03.csv` |
| `Fig 3.png` | `fig03_enterococci-by-site.png` |

Rules:

1. Start with the date as `YYYY-MM-DD`, so files sort in time order.
2. Use hyphens within a part and underscores between parts; no spaces.
3. Number versions with leading zeros: `v01`, `v02`, ..., `v10`.
4. Never use "final". There is always another version.

For files that change often, such as scripts, version control (Git) beats
version numbers in names. See the Software Carpentry lesson
[Version Control with Git](https://swcarpentry.github.io/git-novice/).

## Give every sample a unique identifier

`DBN-2024-003` identifies one sample for ever. "North Beach, 19 March" does
not: a second sample on the same day, or a re-test, breaks it. Assign the
identifier when the sample is collected, write it on the bottle, and use it
in every file that refers to the sample. It is the key that joins your field
sheet to the lab results.

## Store and back up

- Keep data where you **and your supervisor or manager** can reach them.
  Data held only on a student's laptop leave with the student.
- Keep **at least two backups in different physical places**, for example
  the institutional network or cloud storage plus an external drive kept at
  home.
- Check that backups can be restored. A backup never tested is a hope.
- Large data (camera footage, PIV images, model output) need a plan before
  collection starts: how much space, where, and for how long. Ask your
  institution's research data or IT service what is provided.

::::::::::::::::::::::::::::::::::::::: challenge

## Exercise: your own project

Sketch the folder skeleton for a project of your own. Where do your raw
data live today? How many copies exist, and where? Who else can reach them?

:::::::::::::::: solution

## Discussion

Common answers: raw data mixed with processed files; one copy, on a laptop;
nobody else has access. Each is one change away from being fixed. Write
that change on your sticky note.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Write a README

`README_TEMPLATE.txt` in the lesson data gives a skeleton: what the data
are, the folder layout, the files, conventions for dates, missing values and
units, a processing log, rules for access and AI use, and how to cite the
data. Fill it in at the start of a project and update it as you go.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Separate raw data, processed data, scripts and outputs; files flow one way.
- Make raw data read-only and record their origin.
- Name files with ISO dates, no spaces and numbered versions.
- Give every sample a unique identifier.
- Keep at least two backups in different places, and test them.

::::::::::::::::::::::::::::::::::::::::::::::::::
