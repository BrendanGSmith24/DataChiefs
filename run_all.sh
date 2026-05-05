#!/bin/bash

echo "Starting full pipeline..."

# Step 1: Acquire data from FRED API
echo "Running data acquisition..."
python Scripts/acquire_fred_data.py

# Step 2: Clean and merge datasets
echo "Running data cleaning and integration..."
python Scripts/clean_merge_fred_data.py

echo "Pipeline complete."