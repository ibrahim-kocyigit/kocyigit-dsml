from __future__ import annotations
import numpy as np

"""
Key tips:

Labels must be {-1, 1} (not {0, 1}).
Start with uniform weights w = np.ones(n) / n.
Weighted error = sum(w[y != predictions]).
Update rule: w *= np.exp(-alpha * y * predictions), then normalize.
Final prediction: weighted vote via np.sign(sum of alpha * stump predictions).
"""


class DecisionStump:
    """A single-feature threshold classifier (weak learner for AdaBoost)."""

    def __init__(self):
        self.polarity = 1  # 1 or -1 (flip prediction direction)
        self.feature_idx = None  # which feature to split on
        self.threshold = None  # threshold value
        self.alpha = None  # weight of this stump in final prediction

    def predict(self, X: np.ndarray) -> np.ndarray:
        # Apply threshold to selected feature
        # predictions = ones(n_samples)
        # if polarity == 1: predictions[X[:, feature_idx] < threshold] = -1
        # else: predictions[X[:, feature_idx] >= threshold] = -1
        # return predictions
        return np.array([])


class AdaBoost:
    def __init__(self, n_estimators: int = 50):
        self.n_estimators = n_estimators
        self.stumps: list[DecisionStump] = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> AdaBoost:
        # y should be {-1, 1}
        # Initialize sample weights: w = ones(n_samples) / n_samples
        # For each estimator:
        #   1. Create a DecisionStump
        #   2. Find best feature, threshold, and polarity by:
        #      - For each feature:
        #        - For each unique value as threshold:
        #          - Try polarity=1 and polarity=-1
        #          - Compute weighted error: sum(w[incorrect predictions])
        #      - Pick combination with min error
        #   3. Compute stump weight: alpha = 0.5 * log((1 - error) / (error + 1e-10))
        #   4. Update sample weights:
        #      - w *= exp(-alpha * y * predictions)
        #      - Normalize w so sum(w) = 1
        #   5. Store stump with its alpha
        # return self
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        # For each stump:
        #   Get predictions and multiply by stump.alpha
        # Sum all weighted predictions
        # Return sign (or threshold at 0): np.sign(sum)
        return np.array([])
