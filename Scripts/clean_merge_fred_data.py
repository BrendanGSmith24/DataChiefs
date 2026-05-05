import os
import hashlib
import pandas as pd

RAW_DIR = "Data_API/Raw"
CLEAN_DIR = "Data_API/Cleaned"
INTEGRATED_DIR = "Data_API/Integrated"
RESULTS_DIR = "Results/Tables"

os.makedirs(CLEAN_DIR, exist_ok=True)
os.makedirs(INTEGRATED_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)


def sha256_file(file_path):
    hash_object = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()


def clean_monthly_series(file_name, value_name):
    path = os.path.join(RAW_DIR, file_name)

    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    df = df.rename(columns={"value": value_name})
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()

    df = df[["month", value_name]]
    df = df.dropna()
    df = df.drop_duplicates(subset=["month"])
    df = df.sort_values("month")

    output_path = os.path.join(CLEAN_DIR, file_name)
    df.to_csv(output_path, index=False)

    return df


def clean_sp500_daily_to_monthly():
    path = os.path.join(RAW_DIR, "SP500.csv")

    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    df = df.dropna()
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()

    monthly = (
        df.groupby("month", as_index=False)
        .agg(sp500_monthly_avg=("value", "mean"))
        .sort_values("month")
    )

    output_path = os.path.join(CLEAN_DIR, "SP500.csv")
    monthly.to_csv(output_path, index=False)

    return monthly


def create_quality_report(dataframes):
    rows = []

    for name, df in dataframes.items():
        rows.append({
            "dataset": name,
            "rows": len(df),
            "columns": len(df.columns),
            "start_month": df["month"].min(),
            "end_month": df["month"].max(),
            "missing_values": int(df.isna().sum().sum()),
            "duplicate_months": int(df["month"].duplicated().sum()),
        })

    quality_df = pd.DataFrame(rows)
    output_path = os.path.join(RESULTS_DIR, "fred_data_quality_report.csv")
    quality_df.to_csv(output_path, index=False)

    return quality_df


def main():
    cpi = clean_monthly_series("CPI.csv", "cpi")
    fedfunds = clean_monthly_series("FEDFUNDS.csv", "fed_funds_rate")
    unemployment = clean_monthly_series("UNRATE.csv", "unemployment_rate")
    sp500 = clean_sp500_daily_to_monthly()

    dataframes = {
        "CPI": cpi,
        "FEDFUNDS": fedfunds,
        "UNRATE": unemployment,
        "SP500": sp500,
    }

    create_quality_report(dataframes)

    merged = (
        cpi.merge(fedfunds, on="month", how="inner")
        .merge(unemployment, on="month", how="inner")
        .merge(sp500, on="month", how="inner")
        .sort_values("month")
    )

    merged_path = os.path.join(INTEGRATED_DIR, "fred_macro_integrated.csv")
    merged.to_csv(merged_path, index=False)

    checksum_path = os.path.join(RESULTS_DIR, "fred_checksums.txt")

    with open(checksum_path, "w") as file:
        for folder, filename in [
            (RAW_DIR, "CPI.csv"),
            (RAW_DIR, "FEDFUNDS.csv"),
            (RAW_DIR, "UNRATE.csv"),
            (RAW_DIR, "SP500.csv"),
            (CLEAN_DIR, "CPI.csv"),
            (CLEAN_DIR, "FEDFUNDS.csv"),
            (CLEAN_DIR, "UNRATE.csv"),
            (CLEAN_DIR, "SP500.csv"),
            (INTEGRATED_DIR, "fred_macro_integrated.csv"),
        ]:
            path = os.path.join(folder, filename)
            file.write(f"{path}: {sha256_file(path)}\n")

    print("Cleaned files saved to Data_API/Cleaned")
    print("Integrated file saved to Data_API/Integrated/fred_macro_integrated.csv")
    print("Quality report saved to Results/Tables/fred_data_quality_report.csv")
    print("Checksums saved to Results/Tables/fred_checksums.txt")
    print(merged.head())


if __name__ == "__main__":
    main()