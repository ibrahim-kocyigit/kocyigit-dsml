from __future__ import annotations
import argparse

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


class SimpleLinearRegression:
    """
    A simple implementation of simple linear regression.

    This class estimates the parameters (slope and intercept) of a linear relationship
    between a single feature and a target variable using the least squares method.

    Methods
    -------
    fit(X: np.ndarray, y: np.ndarray) -> SimpleLinearRegression
        Fits the linear regression model to the provided data.

    predict(X: np.ndarray) -> np.ndarray
        Predicts target values using the fitted linear model.
    """

    def __init__(self):
        """
        Initializes the SimpleLinearRegression model.

        Sets the intercept and slope parameters to zero.
        """
        self.intercept = 0
        self.slope = 0

    def fit(self, X: np.ndarray, y: np.ndarray) -> SimpleLinearRegression:
        """
        Fits the linear regression model to the provided data using the least squares method.

        Parameters
        ----------
        X : np.ndarray
            1D array of feature values.
        y : np.ndarray
            1D array of target values.

        Returns
        -------
        SimpleLinearRegression
            The fitted SimpleLinearRegression instance.
        """
        x_bar = np.mean(X)
        y_bar = np.mean(y)
        self.slope = (np.sum((X - x_bar) * (y - y_bar))) / (np.sum((X - x_bar) ** 2))
        # Alternative: self.slope = np.cov(X, y, bias=True)[0, 1] / np.var(X)
        self.intercept = y_bar - self.slope * x_bar
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts target values using the fitted linear model.

        Parameters
        ----------
        X : np.ndarray
            1D array of feature values.

        Returns
        -------
        np.ndarray
            Predicted target values.
        """
        return self.slope * X + self.intercept


class MultipleLinearRegression:
    def __init__(self): ...


def simple_linear_regression_tutorial():
    print("\nRunning Simple Linear Regression tutorial...")
    try:
        df = pd.read_csv("./data_git/salary_dataset.csv")
        print("Dataset loaded successfully.")
        X = df["YearsExperience"].values
        y = df["Salary"].values
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        slr = SimpleLinearRegression()
        slr.fit(X_train, y_train)
        y_hat = slr.predict(X_test)
        r2_slr = r2_score(y_test, y_hat)
        print("\n======== Simple Linear Regression Results ========")
        print(f"Coefficient (slope): {slr.slope:.3f}")
        print(f"Intercept: {slr.intercept:.3f}")
        print(f"R² Score: {r2_slr:.3f}")
        print("=" * 50)
        print(" ")
    except FileNotFoundError:
        print("Error: './data_git/salary_dataset.csv' not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return


def multiple_linear_regression_tutorial():
    print("Running Multiple Linear Regression tutorial...")


def logistic_regression_tutorial():
    print("Running Logistic Regression tutorial...")


def main():
    parser = argparse.ArgumentParser(description="Run regression tutorials.")
    parser.add_argument(
        "model",
        choices=["simple", "multiple", "logistic"],
        help="Which regression tutorial to run",
    )

    args = parser.parse_args()

    if args.model == "simple":
        simple_linear_regression_tutorial()
    elif args.model == "multiple":
        multiple_linear_regression_tutorial()
    elif args.model == "logistic":
        logistic_regression_tutorial()


if __name__ == "__main__":
    main()
