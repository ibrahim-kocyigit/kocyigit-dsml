from __future__ import annotations
import numpy as np


class SVM:
    def __init__(
        self,
        learning_rate: float = 0.001,
        lambda_param: float = 0.01,
        n_iters: int = 1000,
    ) -> None:
        """
        Support Vector Machine (SVM) implementation using stochastic gradient descent.

        This class implements a linear SVM classifier with hinge loss and L2 regularization.
        It supports binary classification with labels {0, 1}, which are internally mapped to {-1, 1}.

        Parameters
        ----------
        learning_rate : float, default=0.001
            The step size for gradient descent updates.
        lambda_param : float, default=0.01
            Regularization strength (L2 penalty).
        n_iters : int, default=1000
            Number of iterations for gradient descent.

        Attributes
        ----------
        weights : np.ndarray or None
            The learned weights after fitting.
        bias : float or None
            The learned bias after fitting.

        Methods
        -------
        fit(X, y)
            Fit the SVM model to the training data.
        predict(X)
            Predict class labels for samples in X.
        """
        self.lr = learning_rate
        self.lambda_ = lambda_param
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> SVM:
        """
        Fit the SVM model to the training data.

        Parameters
        ----------
        X : np.ndarray, shape (n_samples, n_features)
            Training data.
        y : np.ndarray, shape (n_samples,)
            Target labels (must be 0 or 1).

        Returns
        -------
        self : SVM
            Fitted estimator.
        """
        # Raise an error if y is not an array of 0s and 1s
        if set(y) != {0, 1}:
            raise ValueError("The target vector should consist of labels 0 and 1.")

        # Convert labels from {0, 1} to {-1, 1}
        y = 2 * y - 1

        # Get the number of samples and features
        n_samples, n_features = X.shape

        # Initialize weights to zeros (shape: n_features)
        self.weights = np.zeros(n_features)

        # Initialize bias to zero
        self.bias = 0

        # Loop for n_iters iterations:
        for _ in range(self.n_iters):
            # Compute the decision function output for all samples
            score = X @ self.weights - self.bias

            # Compute the margin condition for all samples
            margin_cond = y * score

            # Determine which samples violate the margin (margin_condition < 1)
            is_violate_margin = margin_cond < 1

            # Initialize gradient with regularization term (applied to ALL samples)
            dw = 2 * self.lambda_ * self.weights
            db = 0

            # For samples that violate margin condition (< 1), add hinge loss gradient
            dw -= np.sum(
                X[is_violate_margin] * y[is_violate_margin].reshape(-1, 1), axis=0
            )
            db += np.sum(y[is_violate_margin])

            # Average the gradients over all samples
            dw = dw / n_samples
            db = db / n_samples

            # Update weights using the gradient and learning rate
            self.weights = self.weights - self.lr * dw

            # Update bias using the gradient and learning rate
            self.bias = self.bias - self.lr * db

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class labels for samples in X.

        Parameters
        ----------
        X : np.ndarray, shape (n_samples, n_features)
            Input data.

        Returns
        -------
        predictions : np.ndarray, shape (n_samples,)
            Predicted class labels (0 or 1).
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not fitted. Use .fit() first.")

        if X.shape[1] != len(self.weights):
            raise ValueError(
                f"X has {X.shape[1]} features, but model was trained with {len(self.weights)} features."
            )

        score = X @ self.weights - self.bias

        # Convert from {-1, 1} back to {0, 1}
        predictions = np.sign(score)
        return np.where(predictions == -1, 0, 1)


# Next: 16_support_vector_machines_lab.ipynb
