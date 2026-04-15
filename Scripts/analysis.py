import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("Results/Figures", exist_ok=True)
os.makedirs("Results/Tables", exist_ok=True)

df = pd.read_csv("Data/Cleaned/merged.csv", parse_dates=["date"])

df = df.sort_values("date")

df["sp500_return"] = df["sp500_close"].pct_change()

df = df.dropna()

df.to_csv("Data/Cleaned/final_dataset.csv", index=False)

corr = df[[
    "sp500_return",
    "unemployment_rate",
    "fed_funds_rate",
    "inflation"
]].corr()

corr.to_csv("Results/Tables/correlation_matrix.csv")

plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.savefig("Results/Figures/correlation_heatmap.png")
plt.close()


plt.figure()
plt.plot(df["date"], df["sp500_return"])
plt.title("S&P 500 Returns Over Time")
plt.savefig("Results/Figures/sp500_returns.png")
plt.close()

for col in ["unemployment_rate", "fed_funds_rate", "inflation"]:
    plt.figure()
    sns.regplot(x=df[col], y=df["sp500_return"])
    plt.title(f"{col} vs S&P 500 Returns")
    plt.savefig(f"Results/Figures/scatter_{col}.png")
    plt.close()

df.describe().to_csv("Results/Tables/summary_stats.csv")

df["rolling_corr_inflation"] = df["sp500_return"].rolling(12).corr(df["inflation"])

plt.figure()
plt.plot(df["date"], df["rolling_corr_inflation"])
plt.title("Rolling Correlation (Inflation vs Returns)")
plt.savefig("Results/Figures/rolling_corr_inflation.png")
plt.close()

print("Analysis complete.")