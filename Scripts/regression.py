import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("Data/Cleaned/final_dataset.csv")

X = df[["unemployment_rate", "fed_funds_rate", "inflation"]]
X = sm.add_constant(X)
y = df["sp500_return"]

model = sm.OLS(y, X).fit()

with open("Results/Tables/regression_summary.txt", "w") as f:
    f.write(model.summary().as_text())

print("Regression complete.")