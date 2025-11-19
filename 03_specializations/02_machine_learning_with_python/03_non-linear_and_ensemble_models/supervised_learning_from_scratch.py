from __future__ import annotations
from itertools import combinations

import numpy as np


# Helper functions
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# The binary classifier that we will wrap for multi-class classification
class LogisticClassifier:
    def __init__(self, learning_rate: float = 0.01, max_iters: int = 1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> LogisticClassifier:
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

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        probs = sigmoid(X @ self.weights + self.bias)
        return (probs >= 0.5).astype(int)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        return sigmoid(X @ self.weights + self.bias)


class OneVsRestClassifier:
    def __init__(
        self,
        binary_clf_class,
        learning_rate: float = 0.01,
        max_iters: int = 1000,
    ):
        self.binary_clf_class = binary_clf_class
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.classifiers = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> OneVsRestClassifier:
        self.classifiers = []
        self.classes = np.unique(y)
        for class_ in self.classes:
            clf = self.binary_clf_class(self.learning_rate, self.max_iters)
            y_binary = (y == class_).astype(int)
            clf.fit(X, y_binary)
            self.classifiers.append(clf)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.classifiers is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        probs = [clf.predict_proba(X) for clf in self.classifiers]
        probs = np.column_stack(probs)
        return self.classes[np.argmax(probs, axis=1)]


class OneVsOneClassifier:
    def __init__(
        self, binary_clf_class, learning_rate: float = 0.01, max_iters: int = 1000
    ):
        self.binary_clf_class = binary_clf_class
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.classifiers = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> OneVsOneClassifier:
        self.classifiers = {}
        self.classes = np.unique(y)
        pairs = list(combinations(self.classes, 2))
        for class_1, class_2 in pairs:
            clf = self.binary_clf_class(self.learning_rate, self.max_iters)
            idx = np.where((y == class_1) | (y == class_2))
            clf.fit(X[idx], y[idx])
            self.classifiers[(class_1, class_2)] = clf
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.classifiers is None:
            raise ValueError("Model is not trained yet. Please call 'fit' first.")
        votes = np.zeros((X.shape[0], len(self.classes)))
        class_to_index = {cls: idx for idx, cls in enumerate(self.classes)}
        for (class_1, class_2), clf in self.classifiers.items():
            preds = clf.predict(X)
            for i, pred in enumerate(preds):
                if pred == class_1:
                    votes[i, class_to_index[class_1]] += 1
                else:
                    votes[i, class_to_index[class_2]] += 1
        print(votes)
        return self.classes[np.argmax(votes, axis=1)]
