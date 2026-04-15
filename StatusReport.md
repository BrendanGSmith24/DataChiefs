# Status Report
## Task Updates
For this stage of the project, we primarily focused on data acquisition, cleaning, standardization, and merging, followed by an initial exploratory analysis.

Our first step was collecting all the required datasets. For Macroeconomic indicators, (CPI, unemployment rate, and the federal funds rate) we downloaded them directly as CSV files from the FRED database. We chose to download them because it was the most efficient method and ensured we were working with clean, structured data. For the S&P 500, we retrieved historical price data from Yahoo Finance and focused on adjusted close values to reflect true market performance.

One of the more important parts of our workflow was standardizing the frequency of the datasets. One big issue was that the macroeconomic indicators were only available at a monthly level, but the S&P 500 data was recorded daily. To fix this mismatch, we decided to convert the S&P 500 data to a monthly frequency by selecting the last trading day of each month and then calculating monthly returns from that. This step made sure that we were able to align all datasets consistently for analysis.

After aligning frequencies, our next step was to handle data cleaning and preprocessing. We standardized column names, converted dates into a consistent datetime format, and confirmed that all variables were ready to be used for analysis. We also checked for both explicit and implicit missing values across all datasets, although we did not find any significant missing data or unexpected gaps, which allowed us to move forward without needing to impute data or remove rows.

Next, we prepared the datasets to be merged. All the datasets were aligned on a common monthly 'Date' column, which ensured that timestamps matched exactly. After merging, we verified that there was no duplication or errors. Ultimately, we finished with one unified dataframe that includes S&P 500 returns alongside macroeconomic indicators. We also implemented a reproducible workflow using script-based execution (analysis.py, regression.py, and run_all.sh), allowing the entire pipeline to be rerun from raw data to final outputs.

Finally, we began our exploratory data analysis. We generated correlation matrices and time-series visualizations to get a good understanding of all relationships between the variables. These outputs helped us validate that our data pipeline is working correctly and provided early insights that we will use for our regression analysis in the next stage.

## Relevant Artifacts
The following artifacts are included in our GitHub repository:

- Raw datasets: `/data/raw/`
- Cleaned datasets: `/data/Cleaned/final_dataset.csv`
- Data preprocessing workflow: `/scripts/analysis.py`
- Regression script: `/scripts/regression.py`
- Pipeline execution script: `/scripts/run_all.sh`
- Visualization outputs: `/results/`

## Updated Timeline
**Week 1: Data Acquisition & Cleaning (Completed)**
* Downloaded all datasets from FRED and Yahoo Finance
* Converted and stored datasets as CSV files
* Standardized date column and variable types
* Checked for and resolved missing data

**Weeks 2–3: Data Analysis (Completed)**
* Converted S&P 500 data from daily to monthly frequency
* Successfully merged all datasets on a monthly Date column
* Generated correlation matrices
* Created initial visualizations

**Weeks 4–5: Evaluation & Final Report (Upcoming)**
* Conduct regression analysis to evaluate predictive relationships
* Expand visualizations and improve analysis
* Interpret results and finalize conclusions
* Complete final report

## Project Plan Changes
Our overall project plan is the same, but we made a few important adjustments based on both feedback and implementation.

First, based on feedback from the Project Plan, we now explicitly discussed and implemented our merging strategy. All datasets are now merged using the Date column at a monthly level, so that they're consistent across all variables.

Second, we successfully created tags and releases for our project milestones. This should ensure that our work is well-documented and reproducible.

Finally, we decided to modify our preprocessing approach slightly, and priotize date standardization earlier in the workflow than originally planned. 

## Challenges
* The most significant challenge we encountered was handling the difference in data frequency between datasets due to the fact that the S&P 500 data is recorded daily but macroeconomic indicators are reported monthly. We evaluated multiple approaches to address this issue and ultimately decided to convert the S&P 500 data to monthly frequency by selecting the last trading day of each month. 

* Another challenge was to ensure that all datasets were perfectly aligned on the same month. Even small inconsistencies in date formatting could lead to incorrect merges or missing data after joining. We resolved this by standardizing all date columns to a consistent monthly format before merging.

* We also carefully checked for both explicit and implicit missing values across all datasets. While we initially expected to encounter gaps, we did not find any significant missing data after standardization, which simplified the preprocessing stage.

## Contribution Summary
### Brendan Smith Summary
- Organized the project repository into a clear, modular structure (Data, Scripts, Results, etc.)
- Built a fully reproducible data analysis workflow using analysis.py, regression.py, and run_all.sh
- Worked on the visualizations and regression modeling that will be used for drawing final conclusions from our data sets
- Ensured reproducibility through proper dependency management (requirements.txt) and script-based execution
- Resolved Git version control issues by correctly creating tags and releases for project milestones
### Christopher Boukalis Summary
- Downloaded and managed macroeconomic datasets from the FRED database.
- Standardized datasets by handling data type conversions and resolving missing values.
- Verified date consistency across sources and resampled S&P 500 data to a monthly frequency.
- Merged multiple different sources into a single, analysis-ready dataframe.

