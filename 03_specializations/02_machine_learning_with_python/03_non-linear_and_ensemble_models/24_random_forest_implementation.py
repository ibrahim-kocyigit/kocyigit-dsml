from __future__ import annotations
from collections import Counter
from typing import Tuple

import numpy as np


class RandomForest:
    def __init__(
        self,
        n_trees: int = 10,
        max_depth: int = 10,
        min_samples_split: int = 2,
        max_features: int | None = None,
    ):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.trees: list[DecisionTree] | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> RandomForest:
        self.trees = []
        for _ in range(self.n_trees):
            tree = DecisionTree(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split,
                max_features=self.max_features,
            )
            X_sample, y_sample = self._bootstrap_samples(X, y)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.trees is None:
            raise ValueError("Model is not fitted yet.")
        predictions = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(predictions, 0, 1)
        return np.array([self._most_common_label(pred) for pred in tree_preds])

    def _bootstrap_samples(self, X: np.ndarray, y: np.ndarray) -> Tuple:
        n_samples = X.shape[0]
        idx = np.random.choice(n_samples, n_samples, replace=True)
        return X[idx], y[idx]

    def _most_common_label(self, y: np.ndarray):
        counter = Counter(y)
        return counter.most_common(1)[0][0]


class Node:
    def __init__(
        self,
        feature_id: int | None = None,
        threshold: float | None = None,
        left: Node | None = None,
        right: Node | None = None,
        *,
        value: int | None = None,
    ):
        self.feature_id = feature_id
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value


class DecisionTree:
    def __init__(
        self,
        min_samples_split: int = 2,
        max_depth: int = 20,
        max_features: int | None = None,
    ):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.max_features = max_features
        self.root: Node | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> DecisionTree:
        n_features = X.shape[1]
        self._n_split_features = (
            n_features
            if self.max_features is None
            else min(n_features, self.max_features)
        )
        self.root = self._grow_tree(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.root is None:
            raise ValueError("Decision Tree is not fitted. Call .fit() method first.")

        if X.ndim != 2:
            raise ValueError(f"Expected 2D array, got {X.ndim}D array instead")

        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _best_split(
        self, X: np.ndarray, y: np.ndarray, feature_idx: np.ndarray
    ) -> Tuple[int | None, float | None]:
        best_gain = -1
        split_id: int | None = None
        split_threshold: float | None = None

        for feature_id in feature_idx:
            X_column = X[:, feature_id]
            thresholds = np.unique(X_column)

            for threshold in thresholds:
                gain = self._information_gain(X_column, y, threshold)

                if gain > best_gain:
                    best_gain = gain
                    split_id = feature_id
                    split_threshold = threshold

        return split_id, split_threshold

    def _entropy(self, y: np.ndarray) -> float:
        if len(y) == 0:
            return 0
        hist = np.bincount(y)
        p_xs = hist / len(y)
        return -np.sum([p_x * np.log2(p_x) for p_x in p_xs if p_x > 0])

    def _information_gain(
        self, X_column: np.ndarray, y: np.ndarray, threshold: float
    ) -> float:
        # Calculate the parent entropy
        parent_entropy = self._entropy(y)

        # Create children
        left_idx, right_idx = self._split(X_column, threshold)
        n_samples_left = len(left_idx)
        n_samples_right = len(right_idx)

        # Return 0 if no children
        if n_samples_left == 0 or n_samples_right == 0:
            return 0

        # Calculate the weighted average entropy of children
        n_samples = len(y)
        entropy_left = self._entropy(y[left_idx])
        entropy_right = self._entropy(y[right_idx])
        child_entropy = (n_samples_left / n_samples) * entropy_left + (
            n_samples_right / n_samples
        ) * entropy_right

        # Calculate and return the information gain
        return parent_entropy - child_entropy

    def _grow_tree(self, X: np.ndarray, y: np.ndarray, depth: int = 0) -> Node:
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        feature_idx = np.random.choice(
            n_features, self._n_split_features, replace=False
        )

        # Check the stopping criteria
        if (
            depth >= self.max_depth
            or n_labels == 1
            or n_samples < self.min_samples_split
        ):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        # Find the best split
        best_feature, best_threshold = self._best_split(X, y, feature_idx)

        if best_feature is None or best_threshold is None:
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        # Create child nodes
        left_idx, right_idx = self._split(X[:, best_feature], best_threshold)
        left = self._grow_tree(X[left_idx, :], y[left_idx], depth + 1)
        right = self._grow_tree(X[right_idx, :], y[right_idx], depth + 1)

        return Node(best_feature, best_threshold, left, right)

    def _most_common_label(self, y: np.ndarray) -> int:
        if len(y) == 0:
            raise ValueError("Cannot find most common label in empty array")

        counter = Counter(y)
        return counter.most_common(1)[0][0]

    def _split(
        self, X_column: np.ndarray, threshold: float
    ) -> Tuple[np.ndarray, np.ndarray]:
        left_idx = np.argwhere(X_column <= threshold).flatten()
        right_idx = np.argwhere(X_column > threshold).flatten()
        return left_idx, right_idx

    def _traverse_tree(self, x: np.ndarray, node: Node) -> int:
        if node.value is not None:
            return node.value

        if node.left is None or node.right is None:
            raise ValueError("Tree node is missing children during traversal")

        if x[node.feature_id] <= node.threshold:
            return self._traverse_tree(x, node.left)

        return self._traverse_tree(x, node.right)
