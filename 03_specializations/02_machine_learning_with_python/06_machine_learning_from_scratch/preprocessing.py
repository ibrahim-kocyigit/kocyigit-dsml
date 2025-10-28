import numpy as np


class StandardScaler:
    """
    Standardizes features by removing the mean and scaling to unit variance.
    The standard score of a sample `x` is calculated as: z = (x - u) / s
    """

    def __init__(self):
        """
        Initializes the scaler's parameters.
        """
        self.mean_ = None
        self.scale_ = None

    def fit(self, X: np.ndarray) -> "StandardScaler":
        """
        Compute the mean and standard deviation to be used for later scaling.

        Args:
            X (np.ndarray): The data used to compute the mean and standard deviation.

        Returns:
            StandardScaler: The fitted scaler instance
        """
        self.mean_ = np.mean(X, axis=0)
        self.scale_ = np.std(X, axis=0)

        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Perform standardization by centering and scaling.

        Args:
            X (np.ndarray): The data to scale.

        Raises:
            ValueError: If called before the .fit() method.

        Returns:
            np.ndarray: The transformed data.
        """
        if self.mean_ is None or self.scale_ is None:
            raise ValueError(
                ".transform() method cannot be called before the .fit() method."
            )

        return (X - self.mean_) / self.scale_

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Fit to data, then transform it.

        Args:
            X (np.ndarray): The data to fit and transform

        Returns:
            np.ndarray: The transformed data.
        """
        self.fit(X)

        return self.transform(X)
