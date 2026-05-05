import os
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = "Data_API/Integrated/fred_macro_analysis_ready.csv"
RESULTS_DIR = "Results/Tables"

os.makedirs(RESULTS_DIR, exist_ok=True)


def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Missing {DATA_PATH}. Run ./run_all.sh first."
        )

    df = pd.read_csv(DATA_PATH, parse_dates=["month"])
    df = df.sort_values("month")

    return df


def evaluate_model(model_name, y_true, y_pred):
    return {
        "model": model_name,
        "r2": r2_score(y_true, y_pred),
        "mae": mean_absolute_error(y_true, y_pred),
        "rmse": mean_squared_error(y_true, y_pred) ** 0.5,
    }


def main():
    df = load_data()

    features = [
        "inflation",
        "fed_funds_rate",
        "unemployment_rate",
    ]

    target = "sp500_return"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        shuffle=False,
    )

    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    linear_predictions = linear_model.predict(X_test)

    random_forest_model = RandomForestRegressor(
        n_estimators=500,
        max_depth=4,
        random_state=42,
    )
    random_forest_model.fit(X_train, y_train)
    random_forest_predictions = random_forest_model.predict(X_test)

    results = [
        evaluate_model("Linear Regression", y_test, linear_predictions),
        evaluate_model("Random Forest Regressor", y_test, random_forest_predictions),
    ]

    results_df = pd.DataFrame(results)
    results_df.to_csv(
        f"{RESULTS_DIR}/regression_model_comparison.csv",
        index=False,
    )

    coefficients = pd.DataFrame({
        "feature": features,
        "linear_regression_coefficient": linear_model.coef_,
    })
    coefficients.to_csv(
        f"{RESULTS_DIR}/linear_regression_coefficients.csv",
        index=False,
    )

    importances = pd.DataFrame({
        "feature": features,
        "random_forest_importance": random_forest_model.feature_importances_,
    }).sort_values("random_forest_importance", ascending=False)

    importances.to_csv(
        f"{RESULTS_DIR}/random_forest_feature_importance.csv",
        index=False,
    )

    with open(f"{RESULTS_DIR}/regression_summary.txt", "w") as file:
        file.write("Regression Model Results\n")
        file.write("========================\n\n")

        file.write("Model Comparison:\n")
        file.write(results_df.to_string(index=False))
        file.write("\n\n")

        file.write("Linear Regression Coefficients:\n")
        file.write(coefficients.to_string(index=False))
        file.write("\n\n")

        file.write("Random Forest Feature Importance:\n")
        file.write(importances.to_string(index=False))
        file.write("\n")

    print("Regression complete.")
    print(f"Regression outputs saved to {RESULTS_DIR}")


if __name__ == "__main__":
    main()