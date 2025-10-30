from __future__ import annotations
import argparse
import numpy as np


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
        self.intercept = 0
        self.slope = 0

    def fit(self, X: np.ndarray, y: np.ndarray) -> SimpleLinearRegression:
        x_bar = np.mean(X)
        y_bar = np.mean(y)
        self.slope = (np.sum((X - x_bar) * (y - y_bar))) / (np.sum((X - x_bar) ** 2))
        self.intercept = y_bar - self.slope * x_bar
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.slope * X + self.intercept


def simple_linear_regression_tutorial():
    # This section will be updated
    print("Running Simple Linear Regression tutorial...")


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
