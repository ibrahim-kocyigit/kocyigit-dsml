from __future__ import annotations
import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Compute the sigmoid function for the input array.

    Parameters:
        z (np.ndarray): Input array.

    Returns:
        np.ndarray: Output array after applying the sigmoid function element-wise.
    """
    return 1 / (1 + np.exp(-z))


class LogisticRegressor:
    """
    LogisticRegressor implements logistic regression using gradient descent.

    Attributes:
        learning_rate (float): Step size for gradient descent.
        max_iters (int): Number of iterations for training.
        weights (np.ndarray): Model weights after fitting.
        bias (float): Model bias after fitting.

    Methods:
        fit(X, y): Train the model using input features X and target y.
        predict_proba(X): Predict probabilities for input features X.
        predict(X, threshold): Predict binary labels for input features X.
    """

    def __init__(self, learning_rate: float = 0.01, max_iters: int = 1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> LogisticRegressor:
        """
        Fit the logistic regression model using gradient descent.

        Parameters:
            X (np.ndarray): Input feature matrix of shape (n_samples, n_features).
            y (np.ndarray): Target vector of shape (n_samples,).

        Returns:
            LogisticRegressor: The fitted model instance.
        """
        n_observations, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.max_iters):
            p_hat = sigmoid(X @ self.weights + self.bias)
            dw = (1 / n_observations) * X.T @ (p_hat - y)
            db = (1 / n_observations) * np.sum(p_hat - y)
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db
        return self

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """
        Predict probabilities for input features X.

        Parameters:
            X (np.ndarray): Input feature matrix of shape (n_samples, n_features).

        Returns:
            np.ndarray: Predicted probabilities for each sample.
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return sigmoid(X @ self.weights + self.bias)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """
        Predict binary labels for input features X.

        Parameters:
            X (np.ndarray): Input feature matrix of shape (n_samples, n_features).
            threshold (float): Threshold for converting probabilities to binary labels.

        Returns:
            np.ndarray: Predicted binary labels for each sample.
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return (sigmoid(X @ self.weights + self.bias) >= threshold).astype(int)


# Next: 10_logistic_regression_lab.ipynb
