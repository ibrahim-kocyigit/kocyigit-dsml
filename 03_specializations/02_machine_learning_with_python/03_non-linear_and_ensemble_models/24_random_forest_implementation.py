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
    ) -> None:
        """
        A Random Forest classifier implementation.

        This class builds an ensemble of decision trees, each trained on a bootstrap sample of the data,
        and aggregates their predictions for classification tasks. It supports fitting to data, making
        predictions, and configuring the number of trees, tree depth, minimum samples per split, and the
        number of features considered at each split.

        Attributes:
            n_trees (int): Number of decision trees in the forest.
            max_depth (int): Maximum depth of each decision tree.
            min_samples_split (int): Minimum number of samples required to split an internal node.
            max_features (int | None): Number of features to consider when looking for the best split.
            trees (list[DecisionTree] | None): List of trained decision trees in the forest.
        """
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.trees: list[DecisionTree] | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> RandomForest:
        """
        Fits the random forest classifier to the training data.

        This method trains multiple decision trees on different bootstrap samples of the data.
        Each tree is trained independently and added to the ensemble.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).
            y (np.ndarray): Target labels of shape (n_samples,).

        Returns:
            RandomForest: The fitted random forest instance.
        """
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
        """
        Predicts class labels for the input samples using the trained random forest.

        This method aggregates predictions from all decision trees in the forest and
        returns the most common class label for each sample.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).

        Returns:
            np.ndarray: Predicted class labels for each sample.

        Raises:
            ValueError: If the model has not been fitted yet.
        """
        if self.trees is None:
            raise ValueError("Model is not fitted yet.")
        predictions = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(predictions, 0, 1)
        return np.array([self._most_common_label(pred) for pred in tree_preds])

    def _bootstrap_samples(self, X: np.ndarray, y: np.ndarray) -> Tuple:
        """
        Generates a bootstrap sample from the dataset.

        This method randomly selects samples from the original dataset with replacement,
        creating a new dataset of the same size. This is used to train each tree in the
        random forest on a different subset of the data.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).
            y (np.ndarray): Target labels of shape (n_samples,).

        Returns:
            Tuple[np.ndarray, np.ndarray]: The bootstrapped feature matrix and target labels.
        """
        n_samples = X.shape[0]
        idx = np.random.choice(n_samples, n_samples, replace=True)
        return X[idx], y[idx]

    def _most_common_label(self, y: np.ndarray):
        """
        Finds the most common class label in the given array.

        Args:
            y (np.ndarray): Array of class labels.

        Returns:
            int: The most common class label in the array.

        Raises:
            ValueError: If the input array is empty.
        """
        if len(y) == 0:
            raise ValueError("Cannot find most common label in empty array")
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
    ) -> None:
        """
        A node in the decision tree.

        Each node represents a decision point or a leaf in the tree. Internal nodes store the feature index and threshold used for splitting, as well as references to their left and right child nodes. Leaf nodes store the predicted class value.

        Attributes:
            feature_id (int | None): Index of the feature used for splitting at this node (None for leaf nodes).
            threshold (float | None): Threshold value for splitting the feature (None for leaf nodes).
            left (Node | None): Left child node (None for leaf nodes).
            right (Node | None): Right child node (None for leaf nodes).
            value (int | None): Predicted class label for leaf nodes (None for internal nodes).
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
        max_features: int | None = None,
    ) -> None:
        """
        A simple implementation of a Decision Tree classifier for classification tasks.

        This class supports fitting a decision tree to labeled data, making predictions,
        and controlling tree complexity via parameters such as minimum samples per split,
        maximum tree depth, and the number of features considered at each split.

        Attributes:
            min_samples_split (int): The minimum number of samples required to split an internal node.
            max_depth (int): The maximum depth of the tree.
            max_features (int | None): The number of features to consider when looking for the best split.
            root (Node | None): The root node of the trained decision tree.
        """
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.max_features = max_features
        self.root: Node | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> DecisionTree:
        """
        Fits the decision tree classifier to the training data.

        This method builds the decision tree by recursively splitting the data
        to maximize information gain, subject to the stopping criteria.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).
            y (np.ndarray): Target labels of shape (n_samples,).

        Returns:
            DecisionTree: The fitted decision tree instance.
        """
        n_features = X.shape[1]
        self._n_split_features = (
            n_features
            if self.max_features is None
            else min(n_features, self.max_features)
        )
        self.root = self._grow_tree(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts class labels for the input samples using the trained decision tree.

        Args:
            X (np.ndarray): Feature matrix of shape (n_samples, n_features).

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

        This method iterates over the provided feature indices and all unique thresholds
        for each feature, calculating the information gain for each possible split.
        It returns the feature index and threshold that yield the highest information gain.

        Args:
            X (np.ndarray): Feature matrix for the current node.
            y (np.ndarray): Target labels for the current node.
            feature_idx (np.ndarray): Indices of features to consider for splitting.

        Returns:
            Tuple[int | None, float | None]: The index of the best feature and the best threshold for splitting.
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
        Calculates the entropy of a set of class labels.

        Entropy is a measure of impurity or disorder in a set of labels. It is defined as:
            H(y) = -sum(p_i * log2(p_i))
        where p_i is the probability of class i in the set y.

        Args:
            y (np.ndarray): Array of class labels.

        Returns:
            float: The entropy value.
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
        Calculates the information gain of a potential split on a feature column at a given threshold.

        Information gain measures the reduction in entropy (impurity) achieved by splitting the data
        at the specified threshold. It is computed as the difference between the parent node's entropy
        and the weighted average entropy of the child nodes after the split.

        Args:
            X_column (np.ndarray): The feature column to split on.
            y (np.ndarray): The target labels corresponding to the feature column.
            threshold (float): The threshold value to split the feature column.

        Returns:
            float: The information gain achieved by the split.
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
        Recursively grows the decision tree by finding the best split at each node.

        Args:
            X (np.ndarray): Feature matrix for the current node.
            y (np.ndarray): Target labels for the current node.
            depth (int, optional): Current depth of the tree. Defaults to 0.

        Returns:
            Node: The root node of the (sub)tree.
        """
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
        """
        Finds the most common class label in the given array.

        Args:
            y (np.ndarray): Array of class labels.

        Returns:
            int: The most common class label in the array.

        Raises:
            ValueError: If the input array is empty.
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
            X_column (np.ndarray): Feature column to split on.
            threshold (float): Threshold value for the split.

        Returns:
            Tuple[np.ndarray, np.ndarray]: Indices for the left (<= threshold) and right (> threshold) splits.
        """
        left_idx = np.argwhere(X_column <= threshold).flatten()
        right_idx = np.argwhere(X_column > threshold).flatten()
        return left_idx, right_idx

    def _traverse_tree(self, x: np.ndarray, node: Node) -> int:
        """
        Recursively traverses the decision tree to predict the class label for a single sample.

        Args:
            x (np.ndarray): Feature vector for a single sample.
            node (Node): Current node in the decision tree.

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
