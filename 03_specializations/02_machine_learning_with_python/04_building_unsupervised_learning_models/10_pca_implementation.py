from __future__ import annotations
import numpy as np


class PCA:
    def __init__(self, n_components: int):
        """
        Principal Component Analysis (PCA) implementation.

        This class provides a simple implementation of PCA for dimensionality reduction.
        It can be used to fit a PCA model to data, transform data to a lower-dimensional
        space, and combine both steps with fit_transform.

        Parameters
        ----------
        n_components : int
            Number of principal components to keep.

        Attributes
        ----------
        components_ : np.ndarray or None
            Principal axes in feature space, representing the directions of maximum variance.
        mean_ : np.ndarray or None
            Per-feature empirical mean, estimated from the training set.
        """
        self.n_components = n_components
        self.components_: np.ndarray | None = None
        self.mean_: np.ndarray | None = None

    def fit(self, X: np.ndarray) -> PCA:
        """
        Fit the PCA model to the data.

        Parameters
        ----------
        X : np.ndarray
            The input data of shape (n_samples, n_features).

        Returns
        -------
        self : PCA
            Returns the fitted PCA instance.
        """
        # Center the data
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_

        # Compute covariance matrix
        cov_matrix = np.cov(X_centered, rowvar=False)

        # Compute eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

        # Sort eigenvalues and eigenvectors
        sorted_idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[sorted_idx]
        eigenvectors = eigenvectors[:, sorted_idx]

        # Save the top n_components
        self.components_ = eigenvectors[:, : self.n_components]

        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Project the data onto the principal components.

        Parameters
        ----------
        X : np.ndarray
            The input data of shape (n_samples, n_features).

        Returns
        -------
        X_pca : np.ndarray
            The projected data of shape (n_samples, n_components).
        """
        if self.components_ is None or self.mean_ is None:
            raise RuntimeError(
                "PCA instance is not fitted yet. Call 'fit' before 'transform'."
            )

        # Center the data
        X_centered = X - self.mean_

        # Project data onto principal components
        X_pca = np.dot(X_centered, self.components_)

        return X_pca

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Fit the PCA model to the data and return the projected data.

        Parameters
        ----------
        X : np.ndarray
            The input data of shape (n_samples, n_features).

        Returns
        -------
        X_pca : np.ndarray
            The projected data of shape (n_samples, n_components).
        """
        self.fit(X)
        return self.transform(X)


# Next: 11_pca_lab.ipynb
