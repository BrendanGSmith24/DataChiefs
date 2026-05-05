import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

INTEGRATED_DATA_PATH = "Data_API/Integrated/fred_macro_integrated.csv"
ANALYSIS_READY_PATH = "Data_API/Integrated/fred_macro_analysis_ready.csv"

FIGURES_DIR = "Results/Figures"
TABLES_DIR = "Results/Tables"

os.makedirs(FIGURES_DIR, exist_ok=True)
os.makedirs(TABLES_DIR, exist_ok=True)


def load_data():
    df = pd.read_csv(INTEGRATED_DATA_PATH, parse_dates=["month"])
    df = df.sort_values("month")
    return df


def create_analysis_variables(df):
    df = df.copy()

    df["sp500_return"] = df["sp500_monthly_avg"].pct_change()
    df["inflation"] = df["cpi"].pct_change() * 100

    df = df.dropna()

    return df


def save_analysis_tables(df):
    df.describe().to_csv(f"{TABLES_DIR}/summary_stats.csv")

    corr = df[
        [
            "sp500_return",
            "inflation",
            "fed_funds_rate",
            "unemployment_rate",
        ]
    ].corr()

    corr.to_csv(f"{TABLES_DIR}/correlation_matrix.csv")

    return corr


def make_correlation_heatmap(corr):
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix of Macroeconomic Indicators and S&P 500 Returns")
    plt.tight_layout()
    plt.savefig(f"{FIGURES_DIR}/correlation_heatmap.png", dpi=300)
    plt.close()


def make_sp500_returns_plot(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["month"], df["sp500_return"])
    plt.title("Monthly S&P 500 Returns Over Time")
    plt.xlabel("Date")
    plt.ylabel("Monthly Return")
    plt.tight_layout()
    plt.savefig(f"{FIGURES_DIR}/sp500_returns.png", dpi=300)
    plt.close()


def make_macro_scatter_plots(df):
    variables = {
        "inflation": "Inflation",
        "fed_funds_rate": "Federal Funds Rate",
        "unemployment_rate": "Unemployment Rate",
    }

    for column, label in variables.items():
        plt.figure(figsize=(8, 6))
        sns.regplot(x=df[column], y=df["sp500_return"])
        plt.title(f"{label} vs Monthly S&P 500 Returns")
        plt.xlabel(label)
        plt.ylabel("Monthly S&P 500 Return")
        plt.tight_layout()
        plt.savefig(f"{FIGURES_DIR}/scatter_{column}.png", dpi=300)
        plt.close()


def make_rolling_correlation_plot(df):
    df = df.copy()

    df["rolling_corr_inflation"] = (
        df["sp500_return"]
        .rolling(window=12)
        .corr(df["inflation"])
    )

    plt.figure(figsize=(10, 6))
    plt.plot(df["month"], df["rolling_corr_inflation"])
    plt.title("12-Month Rolling Correlation Between Inflation and S&P 500 Returns")
    plt.xlabel("Date")
    plt.ylabel("Rolling Correlation")
    plt.tight_layout()
    plt.savefig(f"{FIGURES_DIR}/rolling_corr_inflation.png", dpi=300)
    plt.close()


def main():
    df = load_data()
    df = create_analysis_variables(df)

    df.to_csv(ANALYSIS_READY_PATH, index=False)

    corr = save_analysis_tables(df)

    make_correlation_heatmap(corr)
    make_sp500_returns_plot(df)
    make_macro_scatter_plots(df)
    make_rolling_correlation_plot(df)

    print("Analysis complete.")
    print(f"Analysis-ready data saved to {ANALYSIS_READY_PATH}")
    print(f"Tables saved to {TABLES_DIR}")
    print(f"Figures saved to {FIGURES_DIR}")


if __name__ == "__main__":
    main()