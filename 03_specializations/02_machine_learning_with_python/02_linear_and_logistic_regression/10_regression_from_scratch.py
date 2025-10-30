# ---------------------------- REGRESSION FROM SCRATCH ---------------------------- #
# This file includes implementations of simple linear regression, multiple linear
# regression, and logistic regression from scratch using NumPy. Additionally,
# there are tutorial functions demonstrating how to use each model with synthetic
# datasets, along with evaluation metrics.
#
# Even though I tried to implement best practices when it comes to code organization
# and structure, I did not include any docstrings or type hints to keep the code
# concise and focused on the core logic.
# --------------------------------------------------------------------------------- #

from __future__ import annotations
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


# Sigmoid function for logistic regression
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Simple Linear Regression implementation
class SimpleLinearRegression:
    def __init__(self):
        self.intercept = None
        self.slope = None

    def fit(self, X, y):
        self.slope = np.cov(X, y, bias=True)[0, 1] / np.var(X)  # rise / run
        self.intercept = np.mean(y) - self.slope * np.mean(X)
        return self

    def predict(self, X):
        if self.slope is None or self.intercept is None:
            raise ValueError("Model is not fitted yet. Call .fit() before .predict()")
        return self.slope * X + self.intercept


# Multiple Linear Regression implementation
class MultipleLinearRegression:
    def __init__(self, learning_rate=0.001, max_iter=1000):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
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

    def predict(self, X):
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not fitted yet. Call .fit() before .predict()")
        return X @ self.weights + self.bias


# Logistic Regression implementation
class LogisticRegression:
    def __init__(self, learning_rate=0.001, max_iters=1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
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

    def predict(self, X, mode="prob"):
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not fitted yet. Call .fit() before .predict()")
        probs = sigmoid(X @ self.weights + self.bias)
        if mode == "prob":
            return np.array(probs)
        elif mode == "class":
            return (np.array(probs) >= 0.5).astype(int)
        else:
            raise ValueError("mode must be 'prob' or 'class'")


# Tutorial functions for each regression type
def simple_linear_regression_tutorial():
    print("Running Simple Linear Regression tutorial...")
    X, y = datasets.make_regression(  # type: ignore
        n_samples=100, n_features=1, noise=10, random_state=42
    )
    X = X.flatten()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    slr = SimpleLinearRegression()
    slr.fit(X_train, y_train)
    y_hat = slr.predict(X_test)
    mse_slr = mean_squared_error(y_test, y_hat)
    r2_slr = r2_score(y_test, y_hat)
    print("\n======== Simple Linear Regression Results ========")
    print(f"Coefficient (slope): {slr.slope:.2f}")
    print(f"Intercept: {slr.intercept:.2f}")
    print(f"Mean Squared Error: {mse_slr:.2f}")
    print(f"R² Score: {r2_slr:.2f}")
    print("=" * 50)
    print(" ")


def multiple_linear_regression_tutorial():
    print("Running Multiple Linear Regression tutorial...")
    X, y = datasets.make_regression(  # type: ignore
        n_samples=100, n_features=3, noise=15, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    mlr = MultipleLinearRegression()
    mlr.fit(X_train, y_train)
    y_hat = mlr.predict(X_test)
    mse_mlr = mean_squared_error(y_test, y_hat)
    r2_mlr = r2_score(y_test, y_hat)
    print("\n======== Multiple Linear Regression Results ========")
    print(f"Weights: {mlr.weights}")
    print(f"Bias: {mlr.bias:.2f}")
    print(f"Mean Squared Error: {mse_mlr:.2f}")
    print(f"R² Score: {r2_mlr:.2f}")
    print("=" * 52)
    print(" ")


def logistic_regression_tutorial():
    print("Running Logistic Regression tutorial...")
    X, y = datasets.make_classification(
        n_samples=200,
        n_features=3,
        n_informative=2,
        n_redundant=0,
        n_clusters_per_class=1,
        random_state=42,
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test, mode="class")
    accuracy = np.mean(y_pred == y_test)
    print("\n======== Logistic Regression Results =========")
    print(f"Weights: {logreg.weights}")
    print(f"Bias: {logreg.bias:.2f}")
    print(f"Accuracy: {accuracy:.2f}")
    print("=" * 46)
    print(" ")


# Main function to run the tutorials
def main():
    simple_linear_regression_tutorial()
    multiple_linear_regression_tutorial()
    logistic_regression_tutorial()


# Entry point
if __name__ == "__main__":
    main()
