# Studying Macroeconomic Indicators & Their Impact on S&P 500 Returns
This product uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank of St. Louis

## Contributors
- Team: Data Chiefs
- Brendan Smith
- Christopher Boukalis

## Summary
Financial markets and macroeconomic policy are a constant topic of conversation in the news, earnings calls, and central bank briefings. Most of this discussion is based on the idea that economic indicators like interest rates, inflation, and unemployment can help us understand or even predict how the stock market will behave in the future. Our team built this project to test out that theory through creating a comprehensive and reproducible pipeline. By pulling data directly from the Federal Reserve Economic Data (FRED) API and historical prices from Yahoo Finance, we were able to treat the relationship between the economy and the S&P 500 as a hypothesis that needed to be tested through careful data curation and statistical modeling.

For our project, we decided to focus on two main research questions. First, we were curious to see how strongly specific indicators actually correlated with monthly S&P 500 returns. We decided to select the Consumer Price Index (CPI), the Federal Funds Rate, and the Unemployment Rate, as our main variables of interest. Second, we wanted to know if those relationships stay the same over time or if they shift during major market shocks like COVID-19 in 2020, or the aggressive interest rate hikes in 2022. 

To find these answers, we developed an end-to-end automated workflow that handles the entire process, from acquiring the data through FRED, to running the regression analysis. To acquire our data from FRED, we used API calls and immediately generated SHA-256 checksums for each file. During this process, we realized that there was a frequency mismatch between our sources. While the S&P 500 data is recorded daily, the FRED indicators are only published monthly. We considered a few options to transform the data, and we ultimately decided  to aggregate the daily stock prices into a monthly average. This way, we were able to align the datasets without having to create synthetic values or losing track of the market’s performance. We then standardized everything into a common timestamp, and used an inner-join to create a final dataset that had 117 months of clean data from June 2016 to March 2026.

For our analysis, we benchmarked a linear regression model against a more complex random forest model. We started by splitting our data to maintain consistency and avoid any potential data leakage into our training set. Interestingly, we were surprised to find that both models showed us that these indicators had very little power to predict market moves. The linear regression model had an R^2 of -0.043, and the random forest model was only slightly better. Out of all the indicator variables, unemployment had the strongest correlation with market returns, which might have been partly due to the recovery period after the corona virus. Ultimately, the findings in our analysis helped us confirm that the equity markets are forward-pricing measures.

In this project, we really emphasized being as transparent as possible. Every decision we made is documented, and the entire process can be re-executed with a single shell script. Our main goal was to still maintain good data management throughout the duration of our study.

## Data Profile
### Overview
This project uses four datasets obtained from the Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org/) to examine the relationship between macroeconomic conditions and S&P 500 market performance. The datasets include the Consumer Price Index (CPI), Federal Funds Rate (FEDFUNDS), Unemployment Rate (UNRATE), and S&P 500 Index (SP500). Each dataset captures a different aspect of the broader economic environment, representing inflation, monetary policy, labor market conditions, and equity market price level.

These datasets complement each other by providing useful information needed to evaluate whether macroeconomic indicators help explain changes in equity market returns. The S&P 500 is used as the primary outcome variable, while inflation, interest rates, and unemployment serve as explanatory macroeconomic feature variables.

All datasets contain a date field, which allows them to be merged using time as the primary key. The primary difference between the datasets is their reporting frequency. The S&P 500 is reported daily while the macroeconomic indicators are reported monthly. To address this, all data was standardized to a monthly time scale prior to integration. The datasets were first combined into an integrated dataset using a shared `month` variable as the primary key.

The final dataset used for analysis and regression modeling is 
- `Data_API/Integrated/fred_macro_analysis_ready.csv`.

### CPI Dataset
The Consumer Price Index (CPI) dataset is the CPIAUCSL series obtained from the FRED API (https://fred.stlouisfed.org/series/CPIAUCSL). This data measures the average change over time in prices paid by urban consumers for a broad basket of goods and services and serves as a primary indicator of inflation.

The dataset is structured as a time series with two fields, a date column and a numeric value representing the CPI index level. The data is reported at a monthly frequency and is seasonally adjusted.

Within the repository, the CPI dataset is stored at two different stages of the data pipeline
- `Data_API/Raw/CPI.csv` (raw data pulled from the FRED API)
- `Data_API/Cleaned/CPI.csv` (cleaned dataset)
### Federal Funds Dataset
The Federal Funds Rate dataset is the FEDFUNDS series obtained from the FRED API (https://fred.stlouisfed.org/series/FEDFUNDS). This dataset represents the effective federal funds rate, which is the interest rate at which banking institutions lend balances to each other overnight and serves as a key indicator of U.S. monetary policy.

The dataset is structured as a time series with two fields, a date column and a numeric value representing the interest rate level. The data is reported at a monthly frequency and is not seasonally adjusted.

Within the repository, the FEDFUNDS dataset is stored at two different stages of the data pipeline
- `Data_API/Raw/FEDFUNDS.csv` (raw data pulled from the FRED API)
- `Data_API/Cleaned/FEDFUNDS.csv` (cleaned dataset)
### Unemployment Rate Dataset
The Unemployment Rate dataset is the UNRATE series obtained from the FRED API (https://fred.stlouisfed.org/series/UNRATE). This dataset measures the percentage of the total labor force that is unemployed, but they are actively seeking employment. This indicator serves as a key indicator of labor market conditions.

The dataset is structured as a time series with two fields, a date column and a numeric value representing the unemployment rate as a percentage of the labor force. The data is reported at a monthly frequency and is seasonally adjusted.

Within the repository, the UNRATE dataset is stored at two different stages of the data pipeline
- `Data_API/Raw/UNRATE.csv` (raw data pulled from the FRED API)
- `Data_API/Cleaned/UNRATE.csv` (cleaned dataset)
### S&P 500 Dataset
The S&P 500 dataset is the SP500 series obtained from FRED API (https://fred.stlouisfed.org/series/SP500). This dataset represents the daily closing value of the S&P 500 index, which serves as a broad measure of equity market performance in the United States.

The dataset is structured as a time series with two fields, a date column and a numeric value representing the index level. Unlike the macroeconomic indicator datasets, the S&P 500 data is reported at a daily frequency.

Within the repository, the SP500 dataset is stored at two different stages of the data pipeline
- `Data_API/Raw/SP500.csv` (raw data pulled from the FRED API)
- `Data_API/Cleaned/SP500.csv` (cleaned and averaged into a monthly dataset)
### Data Usage
All of the datasets are integrated using a common primary key based off time (`month`) to create a unified dataset of macroeconomic indicators and market performance. The datasets have different reporting frequencies, so the S&P 500 data (daily) was aggregated to a monthly average to align with the monthly reporting of macroeconomic indicators (CPI, FEDFUNDS, and UNRATE).

The first stage of integration produces the dataset
- `Data_API/Integrated/fred_macro_integrated.csv`
 At this stage, the dataset represents a structured combination of cleaned economic and financial data, but it does not yet include feature variables useful for statistical analysis.

A second dataset is then created
- `Data_API/Integrated/fred_macro_analysis_ready.csv`
This dataset is derived from the merged and cleaned dataset. It includes additional transformations that make it more useful for analysis. Specifically, the S&P 500 index is converted into monthly returns, and CPI values are transformed into inflation rates. These transformations convert time series and level data into percentage changes, which allows for better comparison between variables.

The analysis ready dataset is used for all visualization, statistical analysis, and regression modeling. In this project, S&P 500 returns serve as the primary outcome variable, while inflation, interest rates, and unemployment serve as feature variables.
### Legal & Ethical Constraints
All data used in this project is obtained from the Federal Reserve Economic Data (FRED) API and is subject to the FRED Terms of Use. By using the API, we agreed to comply with all applicable legal, copyright, and usage restrictions associated with each data series. Some datasets may be owned by third parties such as Standard and Poors.

The project uses the FRED API in a compliant manner by retrieving data programmatically for analysis without redistributing proprietary content. Required attribution is acknowledged, and the project does not imply endorsement by the Federal Reserve Bank of St. Louis.

To ensure responsible data handling, the FRED API key is stored securely in a `.env` file and is not included in the public repository. Additionally, checksum hashes are generated for downloaded datasets and stored in `Results/Tables/fred_checksums.txt` to verify data integrity and reproducibility.

## Data Quality

## Data Cleaning

## Findings

## Future Work

## Challenges

## Reproducibility

## References

