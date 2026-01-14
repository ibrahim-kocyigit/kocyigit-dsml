from __future__ import annotations
import numpy as np


class DecisionStump:
    def __init__(self) -> None:
        """
        A simple decision stump classifier for use as a weak learner in AdaBoost.

        A decision stump is a one-level decision tree that splits data based on a single feature and threshold.
        It predicts either -1 or +1 for each sample, depending on the feature value and learned polarity.

        Attributes
        ----------
        feature_id : int or None
            Index of the feature used for splitting.
        threshold : float or None
            Threshold value for the split.
        polarity : int or None
            Direction of the inequality (1 or -1).
        alpha : float or None
            Weight of the stump in the AdaBoost ensemble.
        """
        self.feature_id: int | None = None
        self.threshold: float | None = None
        self.polarity: int | None = None
        self.alpha: float | None = None

    def fit(
        self, X: np.ndarray, y: np.ndarray, sample_weights: np.ndarray
    ) -> DecisionStump:
        """
        Fit the decision stump to the data using weighted samples.

        Parameters
        ----------
        X : np.ndarray
            Training input samples of shape (n_samples, n_features).
        y : np.ndarray
            Target values of shape (n_samples,). Must be -1 or +1.
        sample_weights : np.ndarray
            Sample weights of shape (n_samples,).

        Returns
        -------
        DecisionStump
            The fitted DecisionStump instance.
        """
        n_samples, n_features = X.shape
        min_error = np.inf

        for feature_id in range(n_features):
            X_col = X[:, feature_id]
            unique_vals = np.unique(X_col)
            if unique_vals.size == 1:
                continue
            thresholds = (unique_vals[:-1] + unique_vals[1:]) / 2

            for threshold in thresholds:
                for polarity in [1, -1]:
                    preds = np.ones(n_samples)

                    if polarity == 1:
                        preds[X_col < threshold] = -1
                    else:
                        preds[X_col >= threshold] = -1

                    error = np.sum(sample_weights[preds != y])

                    if error < min_error:
                        self.feature_id = feature_id
                        self.threshold = threshold
                        self.polarity = polarity
                        min_error = error
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class labels for samples in X using the fitted decision stump.

        Parameters
        ----------
        X : np.ndarray
            Input samples of shape (n_samples, n_features).

        Returns
        -------
        np.ndarray
            Predicted class labels (-1 or +1) for each sample.
        """
        if self.feature_id is None or self.threshold is None or self.polarity is None:
            raise RuntimeError("DecisionStump must be fitted before calling predict().")

        n_samples = X.shape[0]
        preds = np.ones(n_samples)
        X_col = X[:, self.feature_id]

        if self.polarity == 1:
            preds[X_col < self.threshold] = -1
        else:
            preds[X_col >= self.threshold] = -1

        return preds


class AdaBoost:
    def __init__(self, n_estimators: int = 50) -> None:
        """
        AdaBoost classifier using decision stumps as weak learners.

        Attributes
        ----------
        n_estimators : int
            The maximum number of weak learners (decision stumps) to use.
        stumps : list
            List of fitted DecisionStump instances used in the ensemble.
        """
        self.n_estimators = n_estimators
        self.stumps = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> AdaBoost:
        """
        Fit the AdaBoost model using the provided training data.

        Parameters
        ----------
        X : np.ndarray
            Training input samples of shape (n_samples, n_features).
        y : np.ndarray
            Target values of shape (n_samples,). Must be -1 or +1.

        Returns
        -------
        AdaBoost
            The fitted AdaBoost instance.
        """
        if not np.all(np.isin(y, [-1, 1])):
            raise ValueError("y must contain only -1 and +1 labels for AdaBoost.")

        n_samples = X.shape[0]
        sample_weights = np.full(n_samples, 1 / n_samples)

        for _ in range(self.n_estimators):
            stump = DecisionStump()
            stump.fit(X, y, sample_weights)
            preds = stump.predict(X)
            error = np.sum(sample_weights[preds != y])

            if error <= 1e-12:
                stump.alpha = 10.0  # effectively infinite weight for a perfect stump
                self.stumps.append(stump)
                break
            if error >= 0.5:
                # Skip weak learners that are no better than random.
                break

            alpha = 0.5 * np.log(
                (1 - error) / (error + 1e-10)
            )  # add small value to avoid division by zero
            stump.alpha = alpha
            sample_weights *= np.exp(-alpha * y * preds)
            sample_weights /= np.sum(sample_weights)
            self.stumps.append(stump)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class labels for samples in X.

        Parameters
        ----------
        X : np.ndarray
            Input samples of shape (n_samples, n_features).

        Returns
        -------
        np.ndarray
            Predicted class labels (-1 or +1) for each sample.
        """
        n_samples = X.shape[0]
        final_preds = np.zeros(n_samples)
        for stump in self.stumps:
            final_preds += stump.alpha * stump.predict(X)
        signs = np.sign(final_preds)
        # Map zeros (exact ties) to +1 for determinism.
        signs[signs == 0] = 1
        return signs


if __name__ == "__main__":
    # Simple test case
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    X, y = make_classification(
        n_samples=100, n_features=5, n_informative=3, n_redundant=0, random_state=42
    )
    y = np.where(y == 0, -1, 1)  # Convert labels to -1 and +1

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = AdaBoost(n_estimators=10)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"AdaBoost Test Accuracy: {accuracy * 100:.2f}%")
