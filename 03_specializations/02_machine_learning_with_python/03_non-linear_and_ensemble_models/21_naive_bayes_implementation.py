from __future__ import annotations
import numpy as np
from collections import Counter, defaultdict


class MultinomialNB:
    def __init__(self, alpha: float = 1.0):
        self.alpha = alpha
        self.class_log_prior_: np.ndarray | None = None  # log P(y)
        self.feature_log_prob_: np.ndarray | None = None  # log P(x_i | y)
        self.classes_: np.ndarray | None = None  # unique class labels
        self.vocab_size_: int | None = None  # number of features (columns)

    def fit(self, X: np.ndarray, y: np.ndarray) -> MultinomialNB:
        """
        Fit the Multinomial Naive Bayes classifier.

        Parameters
        ----------
        X : np.ndarray
            Training data of shape (n_samples, n_features).
        y : np.ndarray
            Target values of shape (n_samples,).

        Returns
        -------
        MultinomialNB
            Returns self.
        """
        self.classes_ = np.unique(y)
        n_samples, self.vocab_size_ = X.shape

        assert self.vocab_size_ is not None  # type narrowing for checker

        # Compute class priors: P(y=c)
        counter = Counter(y)
        self.class_log_prior_ = np.array(
            [np.log(counter[c] / n_samples) for c in self.classes_]
        )

        # Compute feature counts per class
        feature_counts = np.zeros((len(self.classes_), self.vocab_size_))
        for id, c in enumerate(self.classes_):
            feature_counts[id] = X[y == c].sum(axis=0)

        # Apply Laplace smoothing and compute log probabilities
        smoothed = (feature_counts + self.alpha) / (
            feature_counts.sum(axis=1, keepdims=True) + self.alpha * self.vocab_size_
        )
        self.feature_log_prob_ = np.log(smoothed)

        return self

    def _joint_log_likelihood(self, X: np.ndarray) -> np.ndarray:
        """
        Compute joint log likelihood for all samples and classes.

        Parameters
        ----------
        X : np.ndarray
            Test data of shape (n_samples, n_features).

        Returns
        -------
        np.ndarray
            Joint log likelihood of shape (n_samples, n_classes).
        """

        assert self.feature_log_prob_ is not None  # type narrowing for checker

        return X @ self.feature_log_prob_.T + self.class_log_prior_

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class labels for samples in X.

        Parameters
        ----------
        X : np.ndarray
            Test data of shape (n_samples, n_features).

        Returns
        -------
        np.ndarray
            Predicted class labels of shape (n_samples,).
        """
        if self.classes_ is None or self.feature_log_prob_ is None:
            raise ValueError("Model must be fitted before making predictions.")

        jll = self._joint_log_likelihood(X)
        pred_indices = np.argmax(jll, axis=1)
        return self.classes_[pred_indices]
