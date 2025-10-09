# Imports for the model
import numpy as np

# Imports for the analysis
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from preprocessing import StandardScaler
from metrics import mean_squared_error
from pathlib import Path


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


def run_analysis():
    """
    This function contains the full, end-to-end tutorial script for
    running the linear regression analysis.

    """
    print("--- Starting Linear Regression Analysis ---")

    # Load the data
    sales = pd.read_csv("./data/marketing_sales.csv")

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        sales[["Marketing_Spend"]], sales["Revenue"], test_size=0.3, random_state=42
    )

    # Convert to numpy arrays
    X_train = np.array(X_train)
    X_test = np.array(X_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(
        X_test
    )  # Use the same scaler for the test set (no fitting this time)

    # Create the Regressor, fit the data, and make predictions
    reg = LinearRegression(alpha=0.001, epochs=10000)
    reg.fit(X_train_scaled, y_train)
    preds = reg.predict(X_test_scaled)

    # Calculate MSE
    mse = mean_squared_error(y_test, preds)
    print(f"Mean Squared Error on the test set: {mse:.2f}")

    # Visualize Results
    plt.figure(figsize=(8, 6))
    plt.scatter(X_test, y_test, color="blue", label="Actual Data")
    plt.plot(X_test, preds, color="red", linewidth=2, label="Our Prediction")
    plt.xlabel("Marketing Spend")
    plt.ylabel("Revenue")
    plt.title("Model Performance on Test Data")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    run_analysis()
