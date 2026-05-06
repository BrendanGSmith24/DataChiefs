import os
import hashlib
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

FRED_API_KEY = os.getenv("FRED_API_KEY")

RAW_DIR = "Data_API/Raw"
os.makedirs(RAW_DIR, exist_ok=True)

OBSERVATION_START = "2016-05-01"
OBSERVATION_END = "2026-05-01"

FRED_SERIES = {
    "CPI": "CPIAUCSL",
    "FEDFUNDS": "FEDFUNDS",
    "SP500": "SP500",
    "UNRATE": "UNRATE",
}


def sha256_file(file_path):
    hash_object = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hash_object.update(chunk)

    return hash_object.hexdigest()


def get_fred_series(series_id, output_name):
    url = "https://api.stlouisfed.org/fred/series/observations"

    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": OBSERVATION_START,
        "observation_end": OBSERVATION_END,
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()

    data = response.json()["observations"]

    df = pd.DataFrame(data)
    df = df[["date", "value"]]
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    output_path = os.path.join(RAW_DIR, f"{output_name}.csv")
    df.to_csv(output_path, index=False)

    checksum = sha256_file(output_path)

    print(f"Saved {output_path}")
    print(f"SHA-256: {checksum}")


def main():
    if FRED_API_KEY is None:
        raise ValueError("Missing FRED_API_KEY. Add it to your .env file.")

    for output_name, series_id in FRED_SERIES.items():
        get_fred_series(series_id, output_name)


if __name__ == "__main__":
    main()