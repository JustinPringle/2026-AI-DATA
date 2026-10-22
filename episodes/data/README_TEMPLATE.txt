README — [PROJECT NAME]
=======================================================
Last updated: [YYYY-MM-DD]        Maintainer: [Name, email]

1. WHAT IS THIS?
   [One or two sentences: what was measured, where, when, why.]
   Example: Weekly Enterococci counts and surface water temperature at
   four Durban beaches, March-April 2024 and 2025. SYNTHETIC TEACHING DATA.

2. FOLDER LAYOUT
   data/raw/         Original files exactly as received. READ-ONLY. Never edit.
   data/processed/   Cleaned, tidy files produced from raw (see section 5).
   scripts/          Code that turns raw into processed, and processed into results.
   outputs/          Figures, tables, model outputs. Can be regenerated.
   docs/             Protocols, data dictionary, ethics/permit letters.

3. FILES
   File                                   Description
   -------------------------------------  ------------------------------------
   [data/raw/...xlsx]                     [who produced it, when, how]
   [data/processed/...tidy.csv]           [one row per sample; see dictionary]
   [docs/...data_dictionary.csv]          [column definitions, units, codes]

4. CONVENTIONS
   Dates:          ISO 8601, YYYY-MM-DD
   Missing values: blank cell; reason recorded in column [missing_reason]
   Censored data:  [below_detection / above_count_range flags; describe limits]
   Units:          in the column name, e.g. water_temp_c
   File names:     YYYY-MM-DD_project_content_vNN.ext, no spaces

5. PROCESSING LOG (what was done to raw to make processed)
   [YYYY-MM-DD] [Initials] [Step, e.g. merged 2024 and 2025 tabs; harmonised
                            site names to 4 categories; converted temp in F to C]

6. ACCESS, SHARING AND AI USE
   Who may use this data:      [e.g. project team only until publication]
   Personal information?       [Yes/No. If yes: POPIA basis, where stored]
   May it be uploaded to AI tools? [Approved institutional tool only / No / Yes]
   Licence on release:         [e.g. CC-BY 4.0]
   Backups:                    [primary location] + [second, different location]

7. HOW TO CITE
   [Author(s) (Year). Title. Repository. DOI]
