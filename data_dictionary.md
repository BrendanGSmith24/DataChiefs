## Data Dictionary 

This document describes every dataset used in this project, the elements contained in each file, and the transformations applied between stages of the pipeline. All datasets originate from the Federal Reserve Economic Data (FRED) API maintained by the Federal Reserve Bank of St. Louis.
The pipeline produces files at three stages:

1. **Raw** — pulled directly from the FRED API (`Data_API/Raw/`)
2. **Cleaned** — standardized to a monthly frequency with renamed columns (`Data_API/Cleaned/`)
3. **Integrated** — merged across all four series on a shared monthly key (`Data_API/Integrated/`)

---
## 1. Raw Datasets (`Data_API/Raw/`)

All four raw files share the same two-column structure as returned by the FRED API. 

### Shared schema

| Column | Type | Units | Description |
|---|---|---|---|
| `date` | string (YYYY-MM-DD) | calendar date | For monthly series this is the first day of the month; for SP500 it is the trading day. |
| `value` | float | varies by series (see below) | Numeric value. May be missing for non-trading days in SP500. |

### File-by-file details

| File | FRED Series ID | Frequency | Units of `value` | Seasonally Adjusted | Source URL |
|---|---|---|---|---|---|
| `CPI.csv` | CPIAUCSL | Monthly | Index, 1982–1984 = 100 | Yes | https://fred.stlouisfed.org/series/CPIAUCSL |
| `FEDFUNDS.csv` | FEDFUNDS | Monthly | Percent (annualized rate) | No | https://fred.stlouisfed.org/series/FEDFUNDS |
| `UNRATE.csv` | UNRATE | Monthly | Percent of labor force | Yes | https://fred.stlouisfed.org/series/UNRATE |
| `SP500.csv` | SP500 | Daily (business days) | Index level (price) | No | https://fred.stlouisfed.org/series/SP500 |

---

## 2. Cleaned Datasets (`Data_API/Cleaned/`)

The cleaning step (`Scripts/clean_merge_fred_data.py`) does the following for the three monthly series:

- Parses `date` to a proper datetime
- Renames `value` to a descriptive variable name
- Snaps the date to the first of the month and stores it in a new `month` column
- Drops missing rows and any duplicate months
- Sorts by `month` ascending

For SP500, the daily series is also modified to a monthly average. 

### `CPI.csv`

| Column | Type | Units | Description |
|---|---|---|---|
| `month` | date (YYYY-MM-01) | first day of month | Primary key for joining across series. |
| `cpi` | float | Index, 1982–1984 = 100 | Consumer Price Index for All Urban Consumers (CPIAUCSL), seasonally adjusted. |

### `FEDFUNDS.csv`

| Column | Type | Units | Description |
|---|---|---|---|
| `month` | date (YYYY-MM-01) | first day of month | Primary key for joining across series. |
| `fed_funds_rate` | float | Percent (annualized) | Effective Federal Funds Rate, monthly average, not seasonally adjusted. |

### `UNRATE.csv`

| Column | Type | Units | Description |
|---|---|---|---|
| `month` | date (YYYY-MM-01) | first day of month | Primary key for joining across series. |
| `unemployment_rate` | float | Percent of labor force | Civilian unemployment rate, seasonally adjusted. |

### `SP500.csv`

| Column | Type | Units | Description |
|---|---|---|---|
| `month` | date (YYYY-MM-01) | first day of month | Primary key for joining across series. Aggregated from daily observations. |
| `sp500_monthly_avg` | float | Index level (price) | Mean of all daily SP500 closing values within the calendar month. |

---

## 3. Integrated Datasets (`Data_API/Integrated/`)

### `fred_macro_integrated.csv`

| Column | Type | Units | Description | Source |
|---|---|---|---|---|
| `month` | date | first day of month | Primary key. | Common to all cleaned files |
| `cpi` | float | Index, 1982–1984 = 100 | Consumer Price Index. | `Cleaned/CPI.csv` |
| `fed_funds_rate` | float | Percent (annualized) | Effective Federal Funds Rate. | `Cleaned/FEDFUNDS.csv` |
| `unemployment_rate` | float | Percent of labor force | Civilian unemployment rate. | `Cleaned/UNRATE.csv` |
| `sp500_monthly_avg` | float | Index level (price) | Monthly average of daily SP500 closes. | `Cleaned/SP500.csv` |

### `fred_macro_analysis_ready.csv`

| Column | Type | Units | Description | Derivation |
|---|---|---|---|---|
| `month` | date | first day of month | Primary key. | Carried over |
| `cpi` | float | Index, 1982–1984 = 100 | Consumer Price Index level. | Carried over |
| `fed_funds_rate` | float | Percent (annualized) | Effective Federal Funds Rate. | Carried over |
| `unemployment_rate` | float | Percent of labor force | Civilian unemployment rate. | Carried over |
| `sp500_monthly_avg` | float | Index level (price) | Monthly average of daily SP500 closes. | Carried over |
| `sp500_return` | float | **Decimal** | Month-over-month return on the SP500 monthly average. Used as the regression target variable. | `sp500_monthly_avg.pct_change()` |
| `inflation` | float | **Percent** | Month-over-month percent change in CPI. | `cpi.pct_change() * 100` |

> **Note:** `sp500_return` and `inflation` are stored on **different scales**. `sp500_return` is a decimal proportion, while `inflation` has already been multiplied by 100 to express a percent. Any analysis that compares the two directly should account for this difference.

---

## 4. Primary Keys and Joins

| File | Primary Key | Join Strategy |
|---|---|---|
| `Cleaned/CPI.csv`, `Cleaned/FEDFUNDS.csv`, `Cleaned/UNRATE.csv`, `Cleaned/SP500.csv` | `month` | Inner join on `month` produces `fred_macro_integrated.csv` |
| `Integrated/fred_macro_integrated.csv` | `month` | One-to-one source for `fred_macro_analysis_ready.csv` |
| `Integrated/fred_macro_analysis_ready.csv` | `month` | Final analysis input; consumed by `Scripts/regression.py` |

---

## 5. Source Scripts

| Script | Produces |
|---|---|
| `Scripts/acquire_fred_data.py` | All four raw files in `Data_API/Raw/` plus checksums |
| `Scripts/clean_merge_fred_data.py` | All four cleaned files plus `fred_macro_integrated.csv` and the data quality report |
| `Scripts/analysis.py` | `fred_macro_analysis_ready.csv` plus correlation tables and figures |
| `Scripts/regression.py` | Regression model outputs in `Results/Tables/` |
