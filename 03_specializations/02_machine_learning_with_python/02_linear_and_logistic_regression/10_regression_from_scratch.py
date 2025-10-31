# ---------------------------- REGRESSION FROM SCRATCH ---------------------------- #
# This file includes implementations of simple linear regression, multiple linear
# regression, and logistic regression from scratch using NumPy. Even though
# I tried to implement best practices when it comes to code organization and
# structure, I did not include any docstrings to keep the code concise and
# focused on the core logic.
# --------------------------------------------------------------------------------- #


from __future__ import annotations
import numpy as np


# Sigmoid function for logistic regressor
def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-z))


# Just a regressor for this lecture, not a classifier
class LogisticRegressor:
    def __init__(self, learning_rate: float = 0.001, max_iters: int = 1000):
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
            dw = (1 / n_observations) * X.T @ (y_hat - y)
            db = (1 / n_observations) * np.sum(y_hat - y)
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return sigmoid(X @ self.weights + self.bias)
