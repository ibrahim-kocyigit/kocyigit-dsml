from __future__ import annotations
import argparse

import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


def sigmoid(z: np.ndarray | float | int) -> np.ndarray | float | int:
    """
    Computes the sigmoid activation function.

    Parameters
    ----------
    z : np.ndarray, float, or int
        Input value(s).

    Returns
    -------
    np.ndarray, float, or int
        Sigmoid of the input value(s).
    """
    return 1 / (1 + np.exp(-z))


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

        Sets the intercept and slope parameters to None.
        """
        self.intercept = None
        self.slope = None

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
        self.slope = np.cov(X, y, bias=True)[0, 1] / np.var(X)  # basically "rise / run"
        # Alternative: self.slope = (np.sum((X - x_bar) * (y - y_bar))) / (np.sum((X - x_bar) ** 2))
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

        Raises
        ------
        ValueError
            If the model has not been fitted (i.e., slope or intercept is None).
        """
        if self.slope is None or self.intercept is None:
            raise ValueError("Model is not fitted yet. Call .fit() before .predict()")
        return self.slope * X + self.intercept


class MultipleLinearRegression:
    """
    A simple implementation of multiple linear regression using gradient descent.

    This class estimates the parameters (weights and bias) of a linear relationship
    between multiple features and a target variable.

    Methods
    -------
    fit(X: np.ndarray, y: np.ndarray) -> MultipleLinearRegression
        Fits the multiple linear regression model to the provided data using gradient descent.

    predict(X: np.ndarray) -> np.ndarray
        Predicts target values using the fitted multiple linear regression model.
    """

    def __init__(self, learning_rate: float = 0.001, max_iter: int = 1000):
        """
        Initializes the MultipleLinearRegression model.

        Parameters
        ----------
        learning_rate : float, optional
            The learning rate for gradient descent (default is 0.001).
        max_iter : int, optional
            The maximum number of iterations for gradient descent (default is 1000).
        """
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> MultipleLinearRegression:
        """
        Fits the multiple linear regression model to the provided data using gradient descent.

        Parameters
        ----------
        X : np.ndarray
            2D array of feature values (shape: [n_samples, n_features]).
        y : np.ndarray
            1D array of target values (shape: [n_samples]).

        Returns
        -------
        MultipleLinearRegression
            The fitted MultipleLinearRegression instance.
        """
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
        """
        Predicts target values using the fitted multiple linear regression model.

        Parameters
        ----------
        X : np.ndarray
            2D array of feature values (shape: [n_samples, n_features]).

        Returns
        -------
        np.ndarray
            Predicted target values.

        Raises
        ------
        ValueError
            If the model has not been fitted (i.e., weights or bias is None).
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not fitted yet. Call .fit() before .predict()")
        return X @ self.weights + self.bias


class LogisticRegression:
    """
    A simple implementation of logistic regression using gradient descent.

    This class estimates the parameters (weights and bias) of a logistic regression model
    for binary classification tasks.

    Methods
    -------
    fit(X: np.ndarray, y: np.ndarray) -> LogisticRegression
        Fits the logistic regression model to the provided data using gradient descent.

    predict(X: np.ndarray, mode: str = "prob") -> np.ndarray
        Predicts probabilities or class labels using the fitted logistic regression model.
    """

    def __init__(self, learning_rate: float = 0.001, max_iters: int = 1000):
        """
        Initializes the LogisticRegression model.

        Parameters
        ----------
        learning_rate : float, optional
            The learning rate for gradient descent (default is 0.001).
        max_iters : int, optional
            The maximum number of iterations for gradient descent (default is 1000).
        """
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> LogisticRegression:
        """
        Fits the logistic regression model to the provided data using gradient descent.

        Parameters
        ----------
        X : np.ndarray
            2D array of feature values (shape: [n_samples, n_features]).
        y : np.ndarray
            1D array of binary target values (shape: [n_samples]).

        Returns
        -------
        LogisticRegression
            The fitted LogisticRegression instance.
        """
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
        """
        Predicts probabilities or class labels using the fitted logistic regression model.

        Parameters
        ----------
        X : np.ndarray
            2D array of feature values (shape: [n_samples, n_features]).
        mode : str, optional
            If "prob", returns predicted probabilities. If "class", returns predicted class labels (default is "prob").

        Returns
        -------
        np.ndarray
            Predicted probabilities or class labels.

        Raises
        ------
        ValueError
            If the model has not been fitted (i.e., weights or bias is None).
            If mode is not "prob" or "class".
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not fitted yet. Call .fit() before .predict()")

        probs = sigmoid(X @ self.weights + self.bias)
        if mode == "prob":
            return np.array(probs)
        elif mode == "class":
            return (np.array(probs) >= 0.5).astype(int)
        else:
            raise ValueError("mode must be 'prob' or 'class'")


def simple_linear_regression_tutorial():
    """
    Demonstrates simple linear regression using a synthetic dataset.

    This function generates a dataset with a single feature and a target variable,
    splits it into training and testing sets, fits a SimpleLinearRegression model,
    makes predictions, and prints evaluation metrics including the coefficient,
    intercept, mean squared error, and R² score.
    """
    # Create feature and target arrays
    X, y = datasets.make_regression(  # type: ignore
        n_samples=100, n_features=1, noise=10, random_state=42
    )

    X = X.flatten()

    # Split data into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initiate the simple linear regression model
    slr = SimpleLinearRegression()

    # Fit the model to the training data
    slr.fit(X_train, y_train)

    # Make predictions on the testing data using the fitted model
    y_hat = slr.predict(X_test)

    # Evaluate the MSE and R^2 score
    mse_slr = mean_squared_error(y_test, y_hat)
    r2_slr = r2_score(y_test, y_hat)

    # Print the results
    print("\n======== Simple Linear Regression Results ========")
    print(f"Coefficient (slope): {slr.slope:.2f}")
    print(f"Intercept: {slr.intercept:.2f}")
    print(f"Mean Squared Error: {mse_slr:.2f}")
    print(f"R² Score: {r2_slr:.2f}")
    print("=" * 50)
    print(" ")


def multiple_linear_regression_tutorial():
    """
    Demonstrates multiple linear regression using a synthetic dataset.

    This function generates a dataset with multiple features and a target variable,
    splits it into training and testing sets, fits a MultipleLinearRegression model,
    makes predictions, and prints evaluation metrics including the weights,
    bias, mean squared error, and R² score.
    """
    print("Running Multiple Linear Regression tutorial...")
    # Create feature matrix and target vector
    X, y = datasets.make_regression(  # type: ignore
        n_samples=100, n_features=3, noise=15, random_state=42
    )

    # Split data into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initiate the simple linear regression model
    mlr = MultipleLinearRegression()

    # Fit the model to the training data
    mlr.fit(X_train, y_train)

    # Make predictions on the testing data using the fitted model
    y_hat = mlr.predict(X_test)

    # Evaluate the MSE and R^2 score
    mse_mlr = mean_squared_error(y_test, y_hat)
    r2_mlr = r2_score(y_test, y_hat)

    # Print the results
    print("\n======== Multiple Linear Regression Results ========")
    print(f"Weights: {mlr.weights}")
    print(f"Bias: {mlr.bias:.2f}")
    print(f"Mean Squared Error: {mse_mlr:.2f}")
    print(f"R² Score: {r2_mlr:.2f}")
    print("=" * 52)
    print(" ")


def logistic_regression_tutorial():
    """
    Demonstrates logistic regression using a synthetic binary classification dataset.

    This function generates a dataset with multiple features for binary classification,
    splits it into training and testing sets, fits a LogisticRegression model,
    makes predictions (probabilities and class labels), evaluates accuracy,
    and prints model parameters and evaluation metrics.
    """
    print("Running Logistic Regression tutorial...")

    # Create a synthetic binary classification dataset
    X, y = datasets.make_classification(
        n_samples=200,
        n_features=3,
        n_informative=2,
        n_redundant=0,
        n_clusters_per_class=1,
        random_state=42,
    )

    # Split data into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initiate the logistic regression model
    logreg = LogisticRegression()

    # Fit the model to the training data
    logreg.fit(X_train, y_train)

    # Make predictions on the testing data using the fitted model
    y_pred = logreg.predict(X_test, mode="class")

    # Evaluate accuracy
    accuracy = np.mean(y_pred == y_test)

    # Print the results
    print("\n======== Logistic Regression Results =========")
    print(f"Weights: {logreg.weights}")
    print(f"Bias: {logreg.bias:.2f}")
    print(f"Accuracy: {accuracy:.2f}")
    print("=" * 46)
    print(" ")


def main():
    """
    Parses command-line arguments and runs the selected regression tutorial.

    Supported options:
    - "simple": Runs the simple linear regression tutorial.
    - "multiple": Runs the multiple linear regression tutorial.
    - "logistic": Runs the logistic regression tutorial.
    """

    # Parse command-line arguments to select tutorial
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
