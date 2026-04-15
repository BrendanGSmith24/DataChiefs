#!/bin/bash

echo "Running analysis..."
python Scripts/analysis.py

echo "Running regression..."
python Scripts/regression.py

echo "All steps completed."