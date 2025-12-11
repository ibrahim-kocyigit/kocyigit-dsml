from __future__ import annotations
from collections import Counter
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
        value: int | None = None,
    ):
        """
        Node for Decision Tree.

        Args:
            feature_id (int | None): Index of the feature used for splitting.
            threshold (float | None): Threshold value for the split.
            left (Node | None): Left child node.
            right (Node | None): Right child node.
            value (int | None): Class label if leaf node.
        """
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
    ):
        """
        DecisionTree classifier implementation from scratch.

        This class builds a decision tree for classification tasks using recursive binary splits
        based on maximizing information gain (entropy). Supports setting minimum samples required
        to split and maximum tree depth.

        Attributes:
            min_samples_split (int): Minimum number of samples required to split a node.
            max_depth (int): Maximum depth of the tree.
            root (Node | None): Root node of the fitted decision tree.
        """
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.root: Node | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> DecisionTree:
        """
        Fits the decision tree classifier to the training data.

        Args:
            X (np.ndarray): Feature matrix of training samples.
            y (np.ndarray): Target labels for training samples.

        Returns:
            DecisionTree: The fitted decision tree instance.
        """
        self.root = self._grow_tree(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts class labels for the input samples.

        Args:
            X (np.ndarray): Feature matrix of samples to predict.

        Returns:
            np.ndarray: Predicted class labels for each sample.
        """
        if self.root is None:
            raise ValueError("Decision Tree is not fitted. Call .fit() method first.")

        if X.ndim != 2:
            raise ValueError(f"Expected 2D array, got {X.ndim}D array instead")

        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _best_split(
        self, X: np.ndarray, y: np.ndarray, feature_idx: np.ndarray
    ) -> Tuple[int | None, float | None]:
        """
        Finds the best feature and threshold to split the data for maximum information gain.

        Args:
            X (np.ndarray): Feature matrix.
            y (np.ndarray): Target labels.
            feature_idx (np.ndarray): Indices of features to consider for splitting.

        Returns:
            Tuple[int | None, float | None]: Best feature index and threshold, or (None, None) if no valid split.
        """
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
        """
        Calculates the entropy of a label array.

        Args:
            y (np.ndarray): Array of non-negative integer class labels.

        Returns:
            float: Entropy value.
        """
        if len(y) == 0:
            return 0
        hist = np.bincount(y)
        p_xs = hist / len(y)
        return -np.sum([p_x * np.log2(p_x) for p_x in p_xs if p_x > 0])

    def _information_gain(
        self, X_column: np.ndarray, y: np.ndarray, threshold: float
    ) -> float:
        """
        Calculates the information gain for a potential split.

        Args:
            X_column (np.ndarray): Feature column to split.
            y (np.ndarray): Target labels.
            threshold (float): Threshold value to split on.

        Returns:
            float: Information gain from the split.
        """
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
        """
        Recursively grows the decision tree by finding the best split and creating child nodes.

        Args:
            X (np.ndarray): Feature matrix.
            y (np.ndarray): Target labels.
            depth (int, optional): Current depth of the tree. Defaults to 0.

        Returns:
            Node: The root node of the grown subtree.
        """
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # Consider all features for splitting (standard decision tree approach)
        feature_idx = np.arange(n_features)

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
        """
        Finds the most common label in the array.

        Args:
            y (np.ndarray): Array of class labels.

        Returns:
            int: The most frequent label.
        """
        if len(y) == 0:
            raise ValueError("Cannot find most common label in empty array")

        counter = Counter(y)
        return counter.most_common(1)[0][0]

    def _split(
        self, X_column: np.ndarray, threshold: float
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Splits the data indices based on the given threshold for a feature column.

        Args:
            X_column (np.ndarray): Feature column to split.
            threshold (float): Threshold value to split on.

        Returns:
            Tuple[np.ndarray, np.ndarray]: Indices for left (<= threshold) and right (> threshold) splits.
        """
        left_idx = np.argwhere(X_column <= threshold).flatten()
        right_idx = np.argwhere(X_column > threshold).flatten()
        return left_idx, right_idx

    def _traverse_tree(self, x: np.ndarray, node: Node) -> int:
        """
        Recursively traverses the tree to predict the class label for a single sample.

        Args:
            x (np.ndarray): Feature vector of the sample.
            node (Node): Current node in the tree.

        Returns:
            int: Predicted class label.
        """
        if node.value is not None:
            return node.value

        if node.left is None or node.right is None:
            raise ValueError("Tree node is missing children during traversal")

        if x[node.feature_id] <= node.threshold:
            return self._traverse_tree(x, node.left)

        return self._traverse_tree(x, node.right)

    def __repr__(self) -> str:
        """String representation of the DecisionTree."""
        if self.root is None:
            return "DecisionTree(unfitted)"
        return f"DecisionTree(max_depth={self.max_depth}, min_samples_split={self.min_samples_split})"


# Next: 10_decision_trees_lab.ipynb
