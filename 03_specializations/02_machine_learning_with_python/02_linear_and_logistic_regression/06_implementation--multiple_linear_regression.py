from __future__ import annotations
import numpy as np


class MultipleLinearRegression:
    def __init__(self, learning_rate: float = 0.01, max_iter: int = 1000):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> MultipleLinearRegression:
        n_observations, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.max_iter):
            y_hat = X @ self.weights + self.bias
            dw = (-2 / n_observations) * X.T @ (y - y_hat)
            db = (-2 / n_observations) * np.sum(y - y_hat)
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return X @ self.weights + self.bias


# Next: 07_lab--multiplie_linear_regression.ipynb
