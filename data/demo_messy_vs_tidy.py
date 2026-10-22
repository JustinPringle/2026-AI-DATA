"""Two-minute facilitator demo: the same question, messy vs tidy data.

Question: what is the mean Enterococci count at North Beach in 2024?
Run from the folder that holds the two data files:  python demo_messy_vs_tidy.py
"""
import pandas as pd

# 1. Messy: read the North Beach block of Sipho's tab the way a person (or an
#    AI assistant writing quick code) would: header on row 4, columns A-D.
messy = pd.read_excel("beach_water_quality_MESSY.xlsx", sheet_name="2024 Sipho",
                      header=3, usecols="A:D", nrows=8)
print(messy, "\n")
counts = pd.to_numeric(messy["Entero (cfu/100mL)"], errors="coerce")
print("Messy mean :", round(counts.mean(), 1),
      "<- '-999' counted as data; '55 cfu' and '<10' silently dropped")

# 2. Tidy: one row per sample, missingness explicit, units in the header.
tidy = pd.read_csv("beach_water_quality_tidy.csv", parse_dates=["sample_date"])
nb = tidy[(tidy.site == "North Beach") & (tidy.sample_date.dt.year == 2024)]
print("Tidy mean  :", round(nb.enterococci_cfu_100ml.mean(), 1),
      f"(n = {nb.enterococci_cfu_100ml.notna().sum()} measured;",
      f"{int(nb.below_detection.sum())} below detection;",
      f"{(nb.missing_reason.fillna('') != '').sum()} missing with a stated reason)")
