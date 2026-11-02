---
title: Setup
---

You need three things for this session, and nothing to install if you use
the LAN computers or Google Sheets:

1. a laptop, or a seat in the LAN next to the venue;
2. a spreadsheet program: Excel, LibreOffice Calc (free) or Google Sheets
   (free, in the browser);
3. a free account with a chat model: ChatGPT, Claude or Gemini. Create and
   test it **before** the session; sign-up emails can take a while to arrive.

Work in pairs if devices are short.

::::::::::::::::::::::::::::::::::::::::::  prereq

## Data

Download all the lesson files in one go:

**[2026-AI-DATA_data.zip](https://justinpringle.github.io/2026-AI-DATA/data/2026-AI-DATA_data.zip)**

Unzip it into a new folder, for example `Documents/ai-data-workshop/`.
Do not open the files straight from the zip; Excel opens them read-only and
saves your changes somewhere you will not find them.

Or download the files one at a time:

| File | What it is | Used in |
| --- | --- | --- |
| [beach_water_quality_MESSY.xlsx](https://justinpringle.github.io/2026-AI-DATA/data/beach_water_quality_MESSY.xlsx) | Two field assistants' spreadsheets, as received | Topic 1, Topic 2 |
| [beach_water_quality_tidy.csv](https://justinpringle.github.io/2026-AI-DATA/data/beach_water_quality_tidy.csv) | The same data, tidy | Topic 1 check, Topic 2 |
| [beach_water_quality_data_dictionary.csv](https://justinpringle.github.io/2026-AI-DATA/data/beach_water_quality_data_dictionary.csv) | What each column of the tidy file means | Topic 2 |
| [README_TEMPLATE.txt](https://justinpringle.github.io/2026-AI-DATA/data/README_TEMPLATE.txt) | A README skeleton for your own project | Topic 2 |
| [demo_messy_vs_tidy.py](https://justinpringle.github.io/2026-AI-DATA/data/demo_messy_vs_tidy.py) | Optional Python demonstration of the two means | Topic 2 (optional) |

If a link above does not work, the same files are in the
[data folder on GitHub](https://github.com/JustinPringle/2026-AI-DATA/tree/main/episodes/data):
open a file and click **Download raw file**.

#### About the data

The data are **synthetic**: weekly Enterococci counts and water temperatures
at four Durban beaches, March to April 2024 (two beaches, collected by
"Sipho") and 2025 (four beaches, collected by "Lerato"). No real monitoring
results or people are involved, so the data may be given to any AI tool.
They are released under CC-BY 4.0.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::  prereq

## Software

#### Spreadsheet

- **Excel**: available to UKZN staff and students through Microsoft 365.
- **LibreOffice Calc**: free; download from
  [libreoffice.org](https://www.libreoffice.org/download/download-libreoffice/).
- **Google Sheets**: free in the browser. Upload the `.xlsx` to Google Drive
  and open it with Google Sheets.

Menus differ between programs and between Windows and macOS. The ideas do
not. The demonstrators will help you find the right menu.

#### Chat model

A free account with [ChatGPT](https://chatgpt.com), [Claude](https://claude.ai)
or [Gemini](https://gemini.google.com). Check that you can attach a file to a
message. If your account cannot attach files, you can paste the contents of
the CSV instead.

#### Python (optional)

Not needed. To run the optional demonstration, open
[Google Colab](https://colab.research.google.com) (free, in the browser),
upload `demo_messy_vs_tidy.py`, `beach_water_quality_MESSY.xlsx` and
`beach_water_quality_tidy.csv`, and run `!python demo_messy_vs_tidy.py`.

::::::::::::::::::::::::::::::::::::::::::::::::::
