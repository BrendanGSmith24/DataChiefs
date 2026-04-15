# Project Plan

## Overview
Our project aims to investigate the relationship between the S&P 500 index and macroeconomic indicators from the Federal Reserve Economic Data (FRED) database. The goal is to evaluate whether commonly referenced economic indicators like interest rates, inflation rates, or unemployment rates exhibit meaningful correlations with equity market performance over time. By analyzing these relationships, we hope to determine whether movements in economic indicators tend to precede, coincide with, or show little connection to changes in the S&P 500. 

To accomplish this, we will combine financial market data with economic time series data. Historical S&P 500 index values will be retrieved using Yahoo Finance's API tool, while macroeconomic indicators will be collected through the FRED API. These datasets will then be cleaned and standardized so that both sources share a consistent date format and frequency. Preprocessing the data is critical to overall project success, because conclusions cannot be drawn without accurate and consistent data. Also, using database orginizations concepts will be essential to creating automated and stable tests.

To begin, we will perform exploratory data analysis and statistical testing. This includes calculating correlations between S&P 500 returns and the selected economic indicators, visualizing the relationships through time series plots and scatterplots, and examining how correlations change across different time periods. We will also consider potential limitations such as reporting frequency differences and the possibility that relationships may be weak or non-linear.

## Team
**Brendan Smith**
- Retrieve S&P 500 data using the Yahoo Finance API
- Assist with collecting macroeconomic indicators from the FRED API
- Perform exploratory data analysis on the S&P 500 data
- Generate visualizations such as time series plots and scatterplots
- Contribute to interpreting results and documenting findings

**Christopher Boukalis**
- Retrieve macroeconomic indicator data from the FRED API
- Clean and preprocess the datasets to ensure consistent date formats and frequencies
- Merge the economic data with the S&P 500 dataset using date joins
- Perform statistical analysis including correlation calculations
- Assist with documenting methodology and preparing the final report

**Shared Responsibilities**
- Validate data quality and reproducibility
- Interpret results and identify potential limitations
- Collaborate on the final report and presentation
- Automating and validating workflows for final submission

## Research Questions

* How strongly are macroeconomic indicators (such as interest rates, inflation, and unemployment rates) correlated with changes in the S&P 500 over time?
* Do the relationships between returns and indicators remain consistent across different time periods, or do they change during different market environments like COVID or The Great Financial Crisis of 2008?

## Datasets

* **Consumer Price Index 1960-2024 FRED** (Federal Reserve Bank of St. Louis)
https://fred.stlouisfed.org/series/FPCPITOTLZGUSA

This dataset contains the timeseries data for the inflation level faced by consumers by using a basket of consumer goods. These goods are split amongst all industries that everyday US consumers use such as food and beverages, education and communication tools, and housing. This dataset will be used to identify how inflation and the S&P 500 are related.

* **Unemployment Rate 1948-2026 FRED** (Federal Reserve Bank of St. Louis)
https://fred.stlouisfed.org/series/UNRATE

This dataset contains the timeseries data for the unemployment rate of the United States. Unemployment is defined as people in the US capable of work that are 16 years or older as a percentage of the total workforce. Using unemployment can show when the overall macro economy is in a period of growth or recession. It will be especially useful for looking at period such as COVID or the Great Financial Crisis.

* **Federal Funds Effective Rate 1954-2026 FRED** (Federal Reserve Bank of St. Louis)
https://fred.stlouisfed.org/series/FEDFUNDS

This dataset contains the timeseries data for the federal funds effective rate for the United States. This is a key measure of monetary policy in the United States, because the Federal Reserve Bank is able to set a target value that banks can lend to one another over night. This rate will be important to identify periods of easier or more difficult borrowing of money. 

* **S&P 500 Index Historical Data 1927–2026** (Yahoo Finance API)
https://finance.yahoo.com/quote/%5EGSPC/history/]

This dataset provides the historical performance of the S&P 500, a stock market index tracking 500 of the largest companies listed on U.S. stock exchanges. We will use the Adjusted Close prices to account for dividends and stock splits, providing a "true" reflection of market value over time. This dataset is the cornerstone of our project, acting as the primary benchmark against which we will measure the correlation and impact of the macroeconomic indicators pulled from FRED.

### **Kaggle Clause**
We did not use Kaggle.

## Timeline
The following schedule outlines the tasks, descriptions, and responsibilities for the duration of the project.

### **Week 1: Data Acquisition & Cleaning**

* **API Integration:** Access the FRED API and Yahoo Finance public API to pull historical data for interest rates, CPI, unemployment rate, and S&P 500 price levels.

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

* **Data Mismatch**: Another issue that we will have to deal with is the mismatch between our two data sources. S&P 500 data is available on a daily basis, but most macro indicators from FRED (such as unemployment rate or CPI) are only updated monthly or quarterly. This will require us to smooth out data manually during pre-processing.

## Gaps

While our current plan provides a strong base for our analysis, we have identified several gaps that could be addressed to improve our findings.

**Missing Internal Data:** Our current datasets focus heavily on broad economic factors. However, the S&P 500 is also significantly driven by micro-economic factors such as corporate earnings reports and profit margins. The lack of company-level fundamental data means we may miss the internal drivers of market performance.

**Advanced Modeling:** We are currently planning to utilize standard correlation and linear regression techniques. However, financial time-series data is often non-linear and may be better analyzed by using more advanced methods, such as Machine Learning models or specific time-series forecasting. 


