# Studying Macroeconomic Indicators & Their Impact on S&P 500 Returns

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

## Data Quality

## Data Cleaning

## Findings

## Future Work

## Challenges

## Reproducibility

## References

