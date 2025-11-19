from __future__ import annotations
import numpy as np


class MultipleLinearRegression:
    """
    MultipleLinearRegression implements multiple linear regression using gradient descent or the normal equation.

    Parameters
    ----------
    learning_rate : float, optional
        The step size for gradient descent (default is 0.01).
    max_iters : int, optional
        The number of iterations for gradient descent (default is 1000).

    Methods
    -------
    fit(X, y, method='gradient_descent')
        Fits the model to the data using the specified method.
    predict(X)
        Predicts target values for given input data.
    """

    def __init__(self, learning_rate: float = 0.01, max_iters: int = 1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None

    def fit(
        self, X: np.ndarray, y: np.ndarray, method: str = "gradient_descent"
    ) -> MultipleLinearRegression:
        """
        Fits the MultipleLinearRegression model to the data using the specified method.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix of shape (n_samples, n_features).
        y : np.ndarray
            Target vector of shape (n_samples,).
        method : str, optional
            Method to fit the model: 'gradient_descent' or 'normal_equation' (default is 'gradient_descent').

        Returns
        -------
        MultipleLinearRegression
            The fitted model instance.

        Raises
        ------
        ValueError
            If an invalid method is specified.
        """
        if method == "gradient_descent":
            return self._fit_gradient_descent(X, y)
        if method == "normal_equation":
            return self._fit_normal_equation(X, y)
        raise ValueError(
            f"Invalid method specified: {method}. Choose 'gradient_descent' or 'normal_equation'."
        )

    def _fit_gradient_descent(
        self, X: np.ndarray, y: np.ndarray
    ) -> MultipleLinearRegression:
        """
        Fits the model to the data using gradient descent.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix of shape (n_samples, n_features).
        y : np.ndarray
            Target vector of shape (n_samples,).

        Returns
        -------
        MultipleLinearRegression
            The fitted model instance.
        """
        n_samples, n_features = X.shape
        self.bias = 0
        self.weights = np.zeros(n_features)

        for _ in range(self.max_iters):
            y_hat = X @ self.weights + self.bias
            error = y - y_hat
            dw = (-2 / n_samples) * X.T @ error
            db = (-2 / n_samples) * np.sum(error)
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db

        return self

    def _fit_normal_equation(
        self, X: np.ndarray, y: np.ndarray
    ) -> MultipleLinearRegression:
        """
        Fits the model to the data using the normal equation.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix of shape (n_samples, n_features).
        y : np.ndarray
            Target vector of shape (n_samples,).

        Returns
        -------
        MultipleLinearRegression
            The fitted model instance.
        """
        X_b = np.c_[X, np.ones(X.shape[0])]
        theta = np.linalg.inv((X_b.T @ X_b)) @ X_b.T @ y
        self.weights = theta[:-1]
        self.bias = theta[-1]
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts target values for given input data.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix of shape (n_samples, n_features).

        Returns
        -------
        np.ndarray
            Predicted target values of shape (n_samples,).
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return X @ self.weights + self.bias


# Next: 07_multiplie_linear_regression_lab.ipynb
