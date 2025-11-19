from __future__ import annotations
import numpy as np


# This basic implementation works for univariate polynomial regression only.
class PolynomialRegression:
    """
    PolynomialRegression implements univariate polynomial regression using multiple linear regression as the underlying model.

    Parameters
    ----------
    degree : int
        The degree of the polynomial features to generate.
    learning_rate : float, optional
        The learning rate for gradient descent (default is 0.01).
    max_iters : int, optional
        The maximum number of iterations for gradient descent (default is 1000).

    Methods
    -------
    fit(X, y)
        Fits the polynomial regression model to the training data.
    predict(X)
        Predicts target values for given input data.
    """

    def __init__(self, degree: int, learning_rate: float = 0.01, max_iters: int = 1000):
        self.degree = degree
        self.model = MultipleLinearRegression(
            learning_rate=learning_rate, max_iters=max_iters
        )

    def _transform(self, X: np.ndarray) -> np.ndarray:
        """
        Transforms input data X into polynomial features up to the specified degree.

        Parameters
        ----------
        X : np.ndarray
            Input feature array of shape (n_samples, 1) or (n_samples,).

        Returns
        -------
        X_poly : np.ndarray
            Transformed feature array of shape (n_samples, degree), where each column
            corresponds to X raised to the power of 1 up to 'degree'.
        """
        X_poly = np.ones((len(X), self.degree))
        for i in range(1, self.degree + 1):
            X_poly[:, i - 1] = (X**i).ravel()
        return X_poly

    def fit(self, X: np.ndarray, y: np.ndarray) -> PolynomialRegression:
        """
        Fits the polynomial regression model to the training data.

        Parameters
        ----------
        X : np.ndarray
            Input feature array of shape (n_samples, 1) or (n_samples,).
        y : np.ndarray
            Target values of shape (n_samples,).

        Returns
        -------
        self : PolynomialRegression
            Returns the fitted model.
        """
        X_poly = self._transform(X)
        self.model.fit(X_poly, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts target values for given input data.

        Parameters
        ----------
        X : np.ndarray
            Input feature array of shape (n_samples, 1) or (n_samples,).

        Returns
        -------
        y_pred : np.ndarray
            Predicted target values of shape (n_samples,).
        """
        X_poly = self._transform(X)
        return self.model.predict(X_poly)


# This class was copied from the related implementation file
class MultipleLinearRegression:
    """
    MultipleLinearRegression implements multivariate linear regression using either gradient descent or the normal equation.

    Parameters
    ----------
    learning_rate : float, optional
        The learning rate for gradient descent (default is 0.01).
    max_iters : int, optional
        The maximum number of iterations for gradient descent (default is 1000).

    Methods
    -------
    fit(X, y, method="gradient_descent")
        Fits the linear regression model to the training data using the specified method.
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
        Fits the linear regression model to the training data using the specified method.

        Parameters
        ----------
        X : np.ndarray
            Input feature array of shape (n_samples, n_features).
        y : np.ndarray
            Target values of shape (n_samples,).
        method : str, optional
            Method to use for fitting ('gradient_descent' or 'normal_equation'). Default is 'gradient_descent'.

        Returns
        -------
        self : MultipleLinearRegression
            Returns the fitted model.
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
        Performs gradient descent to fit the linear regression model.

        Parameters
        ----------
        X : np.ndarray
            Input feature array of shape (n_samples, n_features).
        y : np.ndarray
            Target values of shape (n_samples,).

        Returns
        -------
        self : MultipleLinearRegression
            Returns the fitted model.
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
        Performs linear regression using the normal equation.

        Parameters
        ----------
        X : np.ndarray
            Input feature array of shape (n_samples, n_features).
        y : np.ndarray
            Target values of shape (n_samples,).

        Returns
        -------
        self : MultipleLinearRegression
            Returns the fitted model.
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
            Input feature array of shape (n_samples, n_features).

        Returns
        -------
        y_pred : np.ndarray
            Predicted target values of shape (n_samples,).
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return X @ self.weights + self.bias


# Next: 04_polynomial_regression_lab.ipynb
