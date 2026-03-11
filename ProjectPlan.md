# Project Plan

## Overview

## Team


## Research Question



## Datasets



## Timeline
The following schedule outlines the tasks, descriptions, and responsibilities for the duration of the project.

### **Week 1: Data Acquisition & Cleaning**

* **API Integration:** Access the FRED API and Yahoo Finance public API to pull five-year historical data for interest rates, CPI, CCI, and S&P 500 price levels.

* **Data Conversion:** Convert raw API responses into structured CSV files for data processing.

* **Alignment:** Standardize the "date" column across all datasets to prepare for merging.

* **Pre-processing:** Handle missing values, remove outliers, and normalize columns to prepare for statistical testing.

* **Responsibility:** Christopher and Brendan

### **Weeks 2–3: Data Analysis**

* **Correlation Matrix:** Generate a correlation analysis to identify which macro-indicators share the strongest relationship with S&P 500 performance.

* **Visual Mapping:** Create time-series plots and scatter plots to visualize the relationships between economic factors and market movement.

* **Sector Selection:** Brainstorm and select specific industry ETFs or indices (e.g., Technology, Financial Services, Consumer Staples) for comparative analysis.

* **Statistical Summary:** Calculate descriptive statistics (mean, volatility, and distribution) for both the macro-indicators and market returns.

* **Responsibility:** Christopher and Brendan

### **Weeks 4–5: Evaluation & Final Report**

* **Industry Sensitivity Testing:** Evaluate the varying degrees of vulnerability across different sectors to swings in interest rates and inflation (CPI).

* **Regression Analysis:** Conduct multivariate regression to determine the predictive power of macro-indicators on market returns.

* **Dashboard Development:** Build a visual dashboard (e.g., using Matplotlib, Seaborn, or Plotly) to highlight major trends and research findings.

* **Final Documentation:** Draft the formal project report, integrating the methodology, data visualizations, and final analytical conclusions.

* **Responsibility:** Christopher and Brendan

## Constraints
While the aim of this project is to uncover meaningful patterns & trends, there are several factors that may limit the precision of our analysis.

* **Correlation vs Causation**: One major limitation is that stock prices are influenced by a variety of factors, including corporate earnings, geopolitical events, investor sentiment, and many more. These all fall outside the scope of macro-economic indicators that we will be analyzing.

* **Data Mismatch**: Another issue that we will have to deal with is the mismatch between our two data sources. S&P 500 data is available on a daily basis, but most macro indicators from FRED (such as CPI or CCI) are only updated monthly or quarterly. This will require us to smooth out data manually during pre-processing.

* **Historical Scope**: Since we will focus on a 5 year window, our analysis provides a snapshot of the current economic environment but may not capture how these correlations behave during different long-term cycles, such as major recessions or periods of hyper-inflation.

## Gaps



