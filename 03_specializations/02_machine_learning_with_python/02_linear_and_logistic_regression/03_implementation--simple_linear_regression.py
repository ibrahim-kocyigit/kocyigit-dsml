from __future__ import annotations
import numpy as np


class SimpleLinearRegression:
    def __init__(self):
        self.intercept = None
        self.slope = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> SimpleLinearRegression:
        # The slope: rise / run = cov(X, y) / var(X)
        self.slope = np.cov(X, y, bias=True)[0, 1] / np.var(X)

        """
        # The alternative formula (from the lecture):
        self.slope = np.sum((X - np.mean(X)) * (y - np.mean(y))) / np.sum((X - np.mean(X)) ** 2)
        """

        # The intercept: y_bar - slope * x_bar
        self.intercept = np.mean(y) - self.slope * np.mean(X)

        return self  # So that we can chain the calls

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.intercept is None or self.slope is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")

        return self.slope * X + self.intercept


# Next: 04_lab--simple_linear_regression.ipynb
