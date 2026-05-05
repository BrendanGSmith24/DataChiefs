#!/bin/bash
set -e

echo "Starting full pipeline..."

echo "Running data acquisition..."
python Scripts/acquire_fred_data.py

echo "Running data cleaning and integration..."
python Scripts/clean_merge_fred_data.py

echo "Running analysis..."
python Scripts/analysis.py

echo "Running regression..."
python Scripts/regression.py

echo "Pipeline complete."