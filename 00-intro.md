---
title: Introduction
teaching: 2
exercises: 3
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain why the layout of data decides what a program, or an AI tool, does with it.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Why does data organisation matter when I use AI tools?

::::::::::::::::::::::::::::::::::::::::::::::::::

## One field sheet, two answers

Sipho sampled North Beach eight times in 2024 and typed the Enterococci
counts into a spreadsheet. Ask the spreadsheet for the mean and it says
**−26.0**. A count of bacteria cannot be negative. The correct mean of the
same field sheet is **149.7**.

Nothing crashed and nothing warned. The spreadsheet did exactly what the
layout told it to do. An AI tool given the same sheet reads it just as
literally, and reports its answer with more confidence.

This session is about closing that gap: organising data so that people,
programs and AI tools all read it the way you intend.

## How the session runs

The whole session is one exercise, done in pairs, on one synthetic dataset:
Enterococci counts at four Durban beaches, recorded by two field assistants
in two very different, very messy spreadsheets. The presenter gives a prompt;
you carry it out; the presenter draws out the principle from what you found.
The prompts are on the [Session prompts](../learners/prompts.md) page.

- **Topic 1 · The table a machine can read.** Tidy data, missing and
  censored values, categories, dates and export.
  ([Episodes 1-5](01-format-data.md))
- **Topic 2 · Giving the model its context.** The data dictionary, asking a
  chat model about messy and tidy data, project folders, and what data may go
  to which tool. ([Episodes 6-8](06-data-dictionary.md))

Each topic ends with a check against a key.

::::::::::::::::::::::::::::::::::::::::: callout

## Following Prof Rawatlal's session

This session comes after *Working with generative AI on a postgraduate
project*. Several of his practices return here, applied to data: raw data
never edited, standing instructions for the model, a log line for AI-assisted
work, which data may go to which model, and testing against a known answer.
Watch for them.

::::::::::::::::::::::::::::::::::::::::::::::::::

## What this session will not teach

Statistics, plotting or programming. Spreadsheets are good for entering and
checking data; for analysis, a script is easier to check and to repeat. See
[Going further](../learners/discuss.md).

:::::::::::::::::::::::::::::::::::::::: keypoints

- Programs and AI tools read data literally; the layout decides the answer.
- A wrong answer from messy data arrives without a warning.

::::::::::::::::::::::::::::::::::::::::::::::::::
