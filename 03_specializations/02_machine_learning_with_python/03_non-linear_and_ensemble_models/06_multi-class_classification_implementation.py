from __future__ import annotations
from itertools import combinations

import numpy as np


# Helper functions
def sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Computes the sigmoid activation for the input.

    Args:
        z (np.ndarray): Input array or scalar.

    Returns:
        np.ndarray: Output after applying sigmoid function.
    """
    return 1 / (1 + np.exp(-z))


# The binary classifier that will wrap for multi-class classification
class LogisticClassifier:
    """
    A simple binary logistic regression classifier for use in multi-class classification strategies.

    Attributes:
        learning_rate (float): The step size for gradient descent.
        max_iters (int): The number of iterations for training.
        weights (np.ndarray): The learned weights after fitting.
        bias (float): The learned bias after fitting.

    Methods:
        fit(X, y): Trains the classifier using input features X and binary labels y.
        predict(X): Predicts binary class labels for input features X.
        predict_proba(X): Predicts probabilities for input features X.
    """

    def __init__(self, learning_rate: float = 0.01, max_iters: int = 1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> LogisticClassifier:
        """
        Trains the binary logistic regression classifier using gradient descent.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).
            y (np.ndarray): Binary target vector of shape (n_samples,).

        Returns:
            LogisticClassifier: The trained classifier instance.
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

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts binary class labels for input features X.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).

        Returns:
            np.ndarray: Predicted binary class labels (0 or 1) for each sample.
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        probs = sigmoid(X @ self.weights + self.bias)
        return (probs >= 0.5).astype(int)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts probabilities for input features X.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).

        Returns:
            np.ndarray: Predicted probabilities for each sample.
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return sigmoid(X @ self.weights + self.bias)


class OneVsRestClassifier:
    """
    Implements the One-vs-Rest (OvR) strategy for multi-class classification using a binary classifier.

    Attributes:
        binary_clf_class: The binary classifier class to use (default: LogisticClassifier).
        learning_rate (float): Learning rate for training each binary classifier.
        max_iters (int): Number of iterations for training each binary classifier.
        classifiers (list): List of trained binary classifiers, one for each class.
        classes (np.ndarray): Array of unique class labels.

    Methods:
        fit(X, y): Trains one binary classifier per class using OvR strategy.
        predict(X): Predicts multi-class labels by selecting the class with the highest probability.
    """

    def __init__(
        self,
        binary_clf_class=LogisticClassifier,
        learning_rate: float = 0.01,
        max_iters: int = 1000,
    ):
        self.binary_clf_class = binary_clf_class
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.classifiers = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> OneVsRestClassifier:
        """
        Trains one binary classifier per class using the One-vs-Rest strategy.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).
            y (np.ndarray): Target vector of shape (n_samples,).

        Returns:
            OneVsRestClassifier: The trained classifier instance.
        """
        self.classifiers = []
        self.classes = np.unique(y)
        for class_ in self.classes:
            clf = self.binary_clf_class(self.learning_rate, self.max_iters)
            y_binary = (y == class_).astype(int)
            clf.fit(X, y_binary)
            self.classifiers.append(clf)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts multi-class labels for input features X using the OvR strategy.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).

        Returns:
            np.ndarray: Predicted multi-class labels for each sample.
        """
        if self.classifiers is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        probs = [clf.predict_proba(X) for clf in self.classifiers]
        probs = np.column_stack(probs)
        return self.classes[np.argmax(probs, axis=1)]


class OneVsOneClassifier:
    """
    Implements the One-vs-One (OvO) strategy for multi-class classification using a binary classifier.

    Attributes:
        binary_clf_class: The binary classifier class to use (default: LogisticClassifier).
        learning_rate (float): Learning rate for training each binary classifier.
        max_iters (int): Number of iterations for training each binary classifier.
        classifiers (dict): Dictionary of trained binary classifiers for each class pair.
        classes (np.ndarray): Array of unique class labels.

    Methods:
        fit(X, y): Trains one binary classifier per pair of classes using OvO strategy.
        predict(X): Predicts multi-class labels by majority voting among all classifiers.
    """

    def __init__(
        self,
        binary_clf_class=LogisticClassifier,
        learning_rate: float = 0.01,
        max_iters: int = 1000,
    ):
        self.binary_clf_class = binary_clf_class
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.classifiers = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> OneVsOneClassifier:
        """
        Trains one binary classifier per pair of classes using the One-vs-One strategy.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).
            y (np.ndarray): Target vector of shape (n_samples,).

        Returns:
            OneVsOneClassifier: The trained classifier instance.
        """
        self.classifiers = {}
        self.classes = np.unique(y)
        pairs = list(combinations(self.classes, 2))
        for class_1, class_2 in pairs:
            clf = self.binary_clf_class(self.learning_rate, self.max_iters)

            # Get the data corresponding to the current pair of classes
            idx = np.where((y == class_1) | (y == class_2))[0]
            X_pair = X[idx]
            y_pair = y[idx]

            # We map class_1 to 0 and class_2 to 1
            y_binary = (y_pair == class_2).astype(int)

            clf.fit(X_pair, y_binary)
            self.classifiers[(class_1, class_2)] = clf
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts multi-class labels for input features X using the OvO strategy.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).

        Returns:
            np.ndarray: Predicted multi-class labels for each sample.
        """
        if self.classifiers is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        votes = np.zeros((X.shape[0], len(self.classes)))
        class_to_index = {cls: idx for idx, cls in enumerate(self.classes)}
        for (class_1, class_2), clf in self.classifiers.items():
            preds = clf.predict(X)
            for i, pred in enumerate(preds):
                if pred == 0:
                    votes[i, class_to_index[class_1]] += 1
                else:
                    votes[i, class_to_index[class_2]] += 1
        return self.classes[np.argmax(votes, axis=1)]


class SoftmaxClassifier:
    def __init__(self, learning_rate: float = 0.01, max_iters: int = 1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None
        self.classes = []

    def _softmax(self, z: np.ndarray) -> np.ndarray:
        """
        Computes the softmax activation for a set of scores.
        A numerical stability trick (subtracting the max) is used to prevent overflow.

        Args:
            z (np.ndarray): The input scores matrix (n_samples, n_classes).

        Returns:
            np.ndarray: The matrix of probabilities (n_samples, n_classes).
        """
        z_shifted = z - np.max(z, axis=1, keepdims=True)
        exp_z_shifted = np.exp(z_shifted)
        return exp_z_shifted / np.sum(exp_z_shifted, axis=1, keepdims=True)

    def _onehot(self, y: np.ndarray) -> np.ndarray:
        """
        Converts a 1D array of integer labels into a 2D one-hot encoded matrix.

        Args:
            y (np.ndarray): The input labels.

        Returns:
            np.ndarray: The one-hot encoded matrix.
        """
        n_classes = len(self.classes)
        n_samples = len(y)
        y_one_hot = np.zeros((n_samples, n_classes))
        class_to_index = {cls: i for i, cls in enumerate(self.classes)}
        y_indices = np.array([class_to_index[label] for label in y])
        y_one_hot[np.arange(n_samples), y_indices] = 1
        return y_one_hot

    def fit(self, X: np.ndarray, y: np.ndarray) -> SoftmaxClassifier:
        n_samples, n_features = X.shape
        self.classes = np.unique(y)
        n_classes = len(self.classes)
        self.weights = np.zeros((n_features, n_classes))
        self.bias = np.zeros(n_classes)

        for _ in range(self.max_iters):
            p_hat = self._softmax(X @ self.weights + self.bias)
