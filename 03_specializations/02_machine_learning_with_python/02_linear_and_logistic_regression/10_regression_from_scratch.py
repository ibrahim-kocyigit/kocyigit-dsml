# ---------------------------- REGRESSION FROM SCRATCH ---------------------------- #
# This file includes implementations of simple linear regression, multiple linear
# regression, and logistic regression from scratch using NumPy. Even though
# I tried to implement best practices when it comes to code organization and
# structure, I did not include any docstrings to keep the code concise and
# focused on the core logic.
# --------------------------------------------------------------------------------- #


from __future__ import annotations
import numpy as np


class SimpleLinearRegression:
    def __init__(self):
        self.intercept = None
        self.slope = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> SimpleLinearRegression:
        self.slope = np.cov(X, y, bias=True)[0, 1] / np.var(X)  # rise / run
        self.intercept = np.mean(y) - self.slope * np.mean(X)
        return self  # So that users can chain methods

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.slope * X + self.intercept


class MultipleLinearRegression:
    def __init__(self, learning_rate: float = 0.001, max_iter: int = 1000):
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


# Sigmoid function for logistic regression
def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-z))


class LogisticRegression:
    def __init__(self, learning_rate: float = 0.001, max_iters: int = 1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> LogisticRegression:
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

    def predict(self, X: np.ndarray, mode: str = "prob") -> np.ndarray:
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        probs = sigmoid(X @ self.weights + self.bias)
        if mode == "prob":
            return probs
        elif mode == "class":
            return (probs >= 0.5).astype(int)
        else:
            raise ValueError("mode must be 'prob' or 'class'")
