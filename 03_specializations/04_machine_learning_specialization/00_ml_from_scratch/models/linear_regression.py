import numpy as np


class LinearRegression:
    """
    A simple Linear Regression model implemented from scratch using Gradient Descent.

    Args:
        alpha (float, optional): The learning rate. Defaults to 0.001.
        epochs (int, optional): The number of iterations for gradient descent. Defaults to 1000.

    """

    def __init__(
        self,
        alpha: float = 0.001,
        epochs: int = 1000,
    ) -> None:
        """
        Initializes the model's configuration.

        """
        self.alpha = alpha
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(
        self,
        X: np.ndarray,
        y: np.ndarray,
    ) -> "LinearRegression":
        """
        Trains the linear regression model using the provided data.

        Args:
            X (np.ndarray): Training data features (num_observations, num_features).
            y (np.ndarray): Training data targets (num_observations).

        Returns:
            LinearRegression: The fitted model instance.

        """
        num_observations, num_features = X.shape

        # Initialize parameters
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Gradient Descent
        for _ in range(self.epochs):
            # Calculate predictions
            preds = X @ self.weights + self.bias

            # Calculate error
            error = preds - y

            # Calculate gradients
            dw = (1 / num_observations) * (X.T @ error)
            db = (1 / num_observations) * np.sum(error)

            # Update parameters
            self.weights = self.weights - self.alpha * dw
            self.bias = self.bias - self.alpha * db

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Makes predictions on new data using the trained model.

        Args:
            X (np.ndarray): New data to predict on.

        Raises:
            ValueError: If called before the .fit() method.

        Returns:
            np.ndarray: The predicted values.

        """

        # Check that weights or bias are not None before predicting
        if self.weights is None or self.bias is None:
            raise ValueError("LinearRegression model has not been fitted yet.")

        return X @ self.weights + self.bias
