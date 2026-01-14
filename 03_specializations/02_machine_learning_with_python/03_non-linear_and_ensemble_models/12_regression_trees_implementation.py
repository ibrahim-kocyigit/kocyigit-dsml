from __future__ import annotations
from typing import Tuple

import numpy as np


class Node:
    def __init__(
        self,
        feature_id: int | None = None,
        threshold: float | None = None,
        left: Node | None = None,
        right: Node | None = None,
        *,
        value: float | None = None,
    ) -> None:
        """
        A node in the regression tree.

        Parameters
        ----------
        feature_id : int | None, default=None
            Index of the feature used for splitting at this node.
        threshold : float | None, default=None
            Threshold value for the split.
        left : Node | None, default=None
            Left child node.
        right : Node | None, default=None
            Right child node.
        value : float | None, default=None
            Predicted value if this node is a leaf.
        """
        self.feature_id = feature_id
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value


class RegressionTree:
    def __init__(
        self,
        min_samples_split: int = 2,
        max_depth: int = 20,
    ) -> None:
        """
        A simple implementation of a regression tree for predicting continuous values.

        This class builds a binary decision tree by recursively splitting the data to minimize
        the mean squared error (MSE) at each node. The tree can be fitted to training data and
        used to predict target values for new samples.

        Parameters
        ----------
        min_samples_split : int, default=2
            The minimum number of samples required to split an internal node.
        max_depth : int, default=20
            The maximum depth of the tree.

        Attributes
        ----------
        root : Node | None
            The root node of the fitted regression tree.
        """
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.root: Node | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> RegressionTree:
        """
        Fit the regression tree to the training data.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix of shape (n_samples, n_features).
        y : np.ndarray
            Target values of shape (n_samples,).

        Returns
        -------
        RegressionTree
            The fitted regression tree instance.
        """
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y must have same number of samples")
        if X.shape[0] == 0:
            raise ValueError("Cannot fit on empty dataset")

        self.root = self._grow_tree(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict target values for the input feature matrix X.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix of shape (n_samples, n_features).

        Returns
        -------
        np.ndarray
            Predicted target values of shape (n_samples,).
        """
        if self.root is None:
            raise ValueError("Regression Tree is not fitted. Call .fit() first.")

        if X.ndim != 2:
            raise ValueError(f"Expected 2D array, got {X.ndim}D array instead!")

        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _best_split(
        self, X: np.ndarray, y: np.ndarray, feature_idx: np.ndarray
    ) -> Tuple[int | None, float | None]:
        """
        Find the best feature and threshold to split the data to minimize MSE.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix.
        y : np.ndarray
            Target values.
        feature_idx : np.ndarray
            Indices of features to consider for splitting.

        Returns
        -------
        Tuple[int | None, float | None]
            The index of the best feature and the best threshold for splitting.
        """
        best_mse = float("inf")
        split_id: int | None = None
        split_threshold: float | None = None

        for feature_id in feature_idx:
            X_column = X[:, feature_id]
            unique_values = np.unique(X_column)
            # Sampling thresholds for high-cardinality features
            if len(unique_values) > 100:
                thresholds = np.percentile(unique_values, np.linspace(10, 90, 9))
            elif len(unique_values) > 1:
                thresholds = (unique_values[:-1] + unique_values[1:]) / 2
            else:
                thresholds = unique_values
            for threshold in thresholds:
                mse = self._mse(X_column, y, threshold)
                if mse < best_mse:
                    best_mse = mse
                    split_id = feature_id
                    split_threshold = threshold

        return split_id, split_threshold

    def _grow_tree(self, X: np.ndarray, y: np.ndarray, depth: int = 0) -> Node:
        """
        Recursively grows the regression tree by finding the best split.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix for the current node.
        y : np.ndarray
            Target values for the current node.
        depth : int, default=0
            Current depth of the tree.

        Returns
        -------
        Node
            The constructed node (either a leaf or an internal node).
        """
        n_samples, n_features = X.shape
        feature_idx = np.arange(n_features)

        if (
            depth >= self.max_depth
            or n_samples < self.min_samples_split
            or len(np.unique(y)) == 1
        ):
            return Node(value=float(np.mean(y)))

        best_feature, best_threshold = self._best_split(X, y, feature_idx)

        if best_feature is None or best_threshold is None:
            leaf_value = float(np.mean(y))
            return Node(value=leaf_value)

        left_idx, right_idx = self._split(X[:, best_feature], best_threshold)
        left = self._grow_tree(X[left_idx, :], y[left_idx], depth + 1)
        right = self._grow_tree(X[right_idx, :], y[right_idx], depth + 1)

        return Node(best_feature, best_threshold, left, right)

    def _mse(self, X: np.ndarray, y: np.ndarray, threshold: float) -> float:
        """
        Calculate the mean squared error (MSE) for a potential split.

        Note: MSE minimization is equivalent to variance minimization when
        comparing splits, since the mean is constant within each split.

        Parameters
        ----------
        X : np.ndarray
            The feature column to split on.
        y : np.ndarray
            The target values.
        threshold : float
            The threshold value to split the data.

        Returns
        -------
        float
            The weighted mean squared error of the split.
        """
        n_samples = len(y)
        left_idx, right_idx = self._split(X, threshold)
        n_samples_left = len(left_idx)
        n_samples_right = len(right_idx)

        if n_samples_left == 0 or n_samples_right == 0:
            return float("inf")

        variance_left = np.var(y[left_idx], ddof=0)
        variance_right = np.var(y[right_idx], ddof=0)

        weighted_average = (n_samples_left / n_samples) * variance_left + (
            n_samples_right / n_samples
        ) * variance_right

        return float(weighted_average)

    def _split(
        self, X_column: np.ndarray, threshold: float
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Splits the data indices based on the given threshold.

        Parameters
        ----------
        X_column : np.ndarray
            The feature column to split on.
        threshold : float
            The threshold value to split the data.

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            Indices of samples going to the left and right child nodes.
        """
        left_idx = np.argwhere(X_column <= threshold).flatten()
        right_idx = np.argwhere(X_column > threshold).flatten()
        return left_idx, right_idx

    def _traverse_tree(self, x: np.ndarray, node: Node) -> float:
        """
        Traverse the tree recursively to make a prediction for a single sample.

        Parameters
        ----------
        x : np.ndarray
            Feature vector for a single sample.
        node : Node
            The current node in the tree.

        Returns
        -------
        float
            The predicted value for the sample.
        """
        if node.value is not None:
            return node.value

        if node.left is None or node.right is None:
            raise ValueError("Tree node is missing children during traversal")

        if node.feature_id is None or node.threshold is None:
            raise ValueError("Internal node missing feature_id or threshold")

        if x[node.feature_id] <= node.threshold:
            return self._traverse_tree(x, node.left)

        return self._traverse_tree(x, node.right)


# Next: 13_regression_trees_lab.ipynb
