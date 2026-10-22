---
title: AI tools and your data
teaching: 3
exercises: 2
---

::::::::::::::::::::::::::::::::::::::: objectives

- Decide whether a given dataset may be given to an AI tool.
- Record AI-assisted processing so that it can be checked and repeated.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What data may I give to an AI tool?
- How do I keep AI-assisted work reproducible?

::::::::::::::::::::::::::::::::::::::::::::::::::

## What may leave the building

Uploading a file to an AI tool sends it to a third party. Depending on the
tool and your account, the provider may store it, and some consumer
services may use it to improve their models. Before you upload, ask three
questions:

1. **Does it contain personal information?** Names, student or staff
   numbers, ID numbers, contact details, health information or marks are
   personal information under South Africa's Protection of Personal
   Information Act (POPIA). Processing them needs a lawful basis and
   adequate safeguards.
2. **Is it bound by an agreement?** Funders, industry partners, permit
   conditions and data-sharing agreements may restrict where data go.
3. **Is it unpublished or confidential?** Unpublished results, examination
   material and intellectual property deserve the same care you would give
   an email to a stranger.

If any answer is yes, use only a tool your institution has approved for
that kind of data, or remove the sensitive parts first.

::::::::::::::::::::::::::::::::::::::::: callout

## Your institution's rules

[ADD: link to your institution's guideline on generative AI and its list of
approved tools.]

[ADD: name or office of the POPIA information officer to contact with
questions.]

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: challenge

## Exercise: may it go into a public AI chatbot?

For each case, decide: yes, no, or only with conditions.

1. The synthetic beach dataset from this lesson.
2. Your unpublished thesis data, collected under a funder agreement.
3. A class list with student numbers and marks, which you want "tidied up".
4. Interview transcripts in which participants are named.

:::::::::::::::: solution

## Solution

1. **Yes.** It is synthetic and openly licensed.
2. **Only with conditions.** Check the agreement, and use an
   institution-approved tool.
3. **No,** not as it stands. It is personal information under POPIA. Remove
   names and numbers first, or use an approved tool.
4. **No,** unless the participants consented to it and your ethics approval
   allows it. Anonymise first.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Keep AI-assisted work reproducible

If an AI tool cleaned, transformed or analysed your data, treat it like any
other instrument and log its settings. Add a line to the processing log in
your README:

```text
2025-05-12  JP  Harmonised site names (13 variants -> 4) with an AI assistant
                [tool name and version]; prompt saved as docs/prompts/2025-05-12_sites.txt;
                output checked against a Data > Filter list of distinct values.
```

Better still, ask the tool for code, check the code, and save and run the
code yourself. A saved script repeats exactly; a chat conversation does
not.

## Organisation is what makes AI useful

The habits in this lesson do two jobs. They protect your data from the
mistakes of people, spreadsheets and AI tools. They also make your data
ready for the analysis, modelling and machine learning you may want to do
next: a tidy table with a data dictionary is close to training-ready; a
messy workbook is months of cleaning away.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Before uploading, check for personal information, agreements and confidentiality.
- Use institution-approved tools for sensitive data, or remove the sensitive parts first.
- Log AI-assisted processing like any instrument: tool, date, prompt, and how you checked the result.
- Prefer code you can save and re-run over answers in a chat.

::::::::::::::::::::::::::::::::::::::::::::::::::
