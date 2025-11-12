# ----- Implementation: Multiple Linear Regression ----- #

from __future__ import annotations
import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-z))


class LogisticRegressor:
    def __init__(self, learning_rate: float = 0.01, max_iters: int = 1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> LogisticRegressor:
        n_observations, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.max_iters):
            y_hat = sigmoid(X @ self.weights + self.bias)
            error = y - y_hat
            dw = (-1 / n_observations) * X.T @ error
            db = (-1 / n_observations) * np.sum(error)
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db
        return self
