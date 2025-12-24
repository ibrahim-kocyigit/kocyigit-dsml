from __future__ import annotations

import numpy as np
from collections import Counter


class KNN:
    def __init__(self, k: int = 3):
        """
        k-Nearest Neighbors (kNN) classifier implementation from scratch.

        Parameters
        ----------
        k : int, default=3
            Number of neighbors to use.
        """
        self.k = k
        self.X_train: np.ndarray | None = None
        self.y_train: np.ndarray | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> KNN:
        """
        Store the training data.

        Parameters
        ----------
        X : np.ndarray
            Training data of shape (n_samples, n_features).
        y : np.ndarray
            Target values of shape (n_samples,).

        Returns
        -------
        KNN
            Returns self.
        """
        self.X_train = X
        self.y_train = y
        return self

    def _euclidean_distances(self, X: np.ndarray, x: np.ndarray) -> np.ndarray:
        """
        Compute the Euclidean distances between a single sample x and each sample in X.

        Parameters
        ----------
        X : np.ndarray
            Training data of shape (n_samples, n_features).
        x : np.ndarray
            Single sample of shape (n_features,).

        Returns
        -------
        np.ndarray
            Array of distances of shape (n_samples,).
        """
        return np.sqrt(np.sum((x - X) ** 2, axis=1))

    def _get_k_nearest_indices(self, distances: np.ndarray) -> np.ndarray:
        """
        Find the indices of the k nearest neighbors based on distances.

        Parameters
        ----------
        distances : np.ndarray
            Array of distances of shape (n_samples,).

        Returns
        -------
        np.ndarray
            Indices of the k smallest distances.
        """
        if self.k > distances.size:
            raise ValueError(f"k={self.k} exceeds number of points={distances.size}")
        return np.argsort(distances)[: self.k]

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict the class labels for the provided data.

        Parameters
        ----------
        X : np.ndarray
            Test samples of shape (n_samples, n_features).

        Returns
        -------
        np.ndarray
            Predicted class labels for each sample.
        """
        if self.X_train is None or self.y_train is None:
            raise ValueError("The model is not fitted yet.")

        X = np.asarray(X)
        y_pred = []

        for x in X:
            distances = self._euclidean_distances(self.X_train, x)
            k_idx = self._get_k_nearest_indices(distances)
            labels = self.y_train[k_idx]
            c = Counter(labels)
            y_pred.append(c.most_common(1)[0][0])

        return np.array(y_pred)
