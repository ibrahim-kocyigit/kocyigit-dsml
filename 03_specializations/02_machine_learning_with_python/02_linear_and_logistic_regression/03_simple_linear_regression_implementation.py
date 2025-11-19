from __future__ import annotations
import numpy as np


class SimpleLinearRegression:
    """
    A simple implementation of Simple Linear Regression for educational purposes.

    This class provides methods to fit a linear model to data and make predictions.
    It uses the closed-form solution for ordinary least squares regression.

    Attributes:
        slope (float): The estimated slope (coefficient) of the regression line.
        intercept (float): The estimated intercept of the regression line.

    Methods:
        fit(X, y): Fits the model to the input features X and target y.
        predict(X): Predicts target values for given input features X.
    """

    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> SimpleLinearRegression:
        """
        Fits the Simple Linear Regression model to the input features X and target y.

        Args:
            X (np.ndarray): 1D array of input features.
            y (np.ndarray): 1D array of target values.

        Returns:
            SimpleLinearRegression: The fitted model instance.
        """
        # Slope = cov(X, y) / var(X)
        self.slope = np.cov(X, y, bias=True)[0, 1] / np.var(X)

        """
        # Alternatively, we can use the formula from the lecture:
        self.slope = np.sum((X - np.mean(X)) * (y - np.mean(y))) / np.sum(
            ((X - np.mean(X)) ** 2)
        )
        """

        # Intercept: y_bar - slope * x_bar
        self.intercept = np.mean(y) - self.slope * np.mean(X)

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts target values for given input features X using the trained model.

        Args:
            X (np.ndarray): 1D array of input features.

        Returns:
            np.ndarray: Predicted target values.
        """
        if self.slope is None or self.intercept is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return self.slope * X + self.intercept


# Next: 04_simple_linear_regression_lab.ipynb
