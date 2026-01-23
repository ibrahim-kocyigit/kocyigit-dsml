from __future__ import annotations

import numpy as np


class KMeans:
    def __init__(
        self,
        k: int = 3,
        max_iters: int = 100,
        tol: float = 1e-4,
        random_state: int | None = None,
    ) -> None:
        """
        KMeans clustering algorithm implementation using NumPy.

        Parameters
        ----------
        k : int, default=3
            The number of clusters to form.
        max_iters : int, default=100
            Maximum number of iterations of the k-means algorithm for a single run.
        tol : float, default=1e-4
            Relative tolerance with regards to inertia to declare convergence.
        random_state : int or None, default=None
            Determines random number generation for centroid initialization.

        Attributes
        ----------
        centroids : np.ndarray or None
            Coordinates of cluster centers after fitting.
        labels_ : np.ndarray or None
            Labels of each point after fitting.
        inertia_ : float or None
            Sum of squared distances of samples to their closest cluster center.
        n_iter_ : int
            Number of iterations run.
        """
        self.k = k
        self.max_iters = max_iters
        self.tol = tol
        self.random_state = random_state

        # Initialize RNG for reproducibility
        self.rng = np.random.default_rng(random_state)

        # Attributes to be set during fitting
        self.centroids: np.ndarray | None = None
        self.labels_: np.ndarray | None = None
        self.inertia_: float | None = None
        self.n_iter_: int = 0

    def _initialize_centroids(self, X: np.ndarray) -> np.ndarray:
        """
        Randomly select k unique data points from X as initial centroids.

        Parameters:
        -----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)

        Returns:
        --------
        initial_centroids : np.ndarray
            Initial centroids, shape (k, n_features)
        """
        n_samples = X.shape[0]
        idx = self.rng.choice(n_samples, self.k, replace=False)
        initial_centroids = X[idx]
        return initial_centroids

    def _compute_distances(self, X: np.ndarray) -> np.ndarray:
        """
        Compute squared Euclidean distances from each point in X to each centroid.

        Parameters:
        -----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)

        Returns:
        --------
        squared_distances : np.ndarray
            Squared distances, shape (n_samples, k)
        """
        assert self.centroids is not None, (
            "Centroids must be initialized before computing distances"
        )
        squared_distances = np.sum((X[:, np.newaxis, :] - self.centroids) ** 2, axis=2)
        return squared_distances

    def _assign_clusters(self, X: np.ndarray) -> np.ndarray:
        """
        Assign each data point to the nearest centroid.

        Parameters:
        -----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)

        Returns:
        --------
        labels : np.ndarray
            Cluster assignment for each point, shape (n_samples,)
        """
        distances = self._compute_distances(X)
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X: np.ndarray, labels: np.ndarray) -> np.ndarray:
        """
        Update centroids as the mean of assigned points for each cluster.

        Parameters:
        -----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)
        labels : np.ndarray
            Cluster assignment for each point, shape (n_samples,)

        Returns:
        --------
        new_centroids : np.ndarray
            Updated centroids, shape (k, n_features)
        """
        assert self.centroids is not None, (
            "Centroids must be initialized before updating"
        )
        new_centroids = self.centroids.copy()

        for cluster_index in range(self.k):
            mask = labels == cluster_index
            cluster_points = X[mask]
            if cluster_points.shape[0] > 0:
                new_centroids[cluster_index] = np.mean(cluster_points, axis=0)

        self.centroids = new_centroids
        return new_centroids

    def _has_converged(self, old_centroids: np.ndarray) -> bool:
        """
        Check if the centroids have converged.

        Parameters:
        -----------
        old_centroids : np.ndarray
            Centroids from the previous iteration, shape (k, n_features)

        Returns:
        --------
        converged : bool
            True if the change in centroids is less than the tolerance, else False
        """
        assert self.centroids is not None, (
            "Centroids must be initialized before checking convergence"
        )
        movement = np.linalg.norm(self.centroids - old_centroids)
        return bool(movement < self.tol)

    def _compute_inertia(self, X: np.ndarray, labels: np.ndarray) -> float:
        """
        Compute the inertia (sum of squared distances to the closest centroid).

        Parameters:
        -----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)
        labels : np.ndarray
            Cluster assignment for each point, shape (n_samples,)

        Returns:
        --------
        inertia : float
            Sum of squared distances of samples to their closest centroid.
        """
        assert self.centroids is not None, (
            "Centroids must be initialized before computing inertia"
        )
        distances = self._compute_distances(X)
        inertia = np.sum(distances[np.arange(len(X)), labels])
        return float(inertia)

    def _validate_data(self, X: np.ndarray) -> None:
        """
        Validate input data for KMeans.

        Parameters:
        -----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)

        Raises:
        -------
        ValueError: If X is not a 2D array, is empty, has fewer samples than clusters,
                    or contains NaN/infinite values.
        """
        n_samples = X.shape[0]

        if X.ndim != 2:
            raise ValueError("X has to be an 2D matrix")

        if n_samples == 0:
            raise ValueError("X cannot be an empty matrix")

        if self.k > n_samples:
            raise ValueError("You can't have more cluster than data points")

        if np.isnan(X).any() or np.isinf(X).any():
            raise ValueError("Feature matrix has NaN and/or infinity values.")

    def fit(self, X: np.ndarray) -> "KMeans":
        """
        Fit the KMeans model to the data.

        Parameters
        ----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)

        Returns
        -------
        self : KMeans
            Fitted estimator
        """

        self._validate_data(X)
        self.centroids = self._initialize_centroids(X)

        for i in range(self.max_iters):
            self.n_iter_ += 1
            labels = self._assign_clusters(X)
            old_centroids = self.centroids.copy()
            self._update_centroids(X, labels)
            if self._has_converged(old_centroids):
                break

        labels = self._assign_clusters(X)
        self.inertia_ = self._compute_inertia(X, labels)
        self.labels_ = labels
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Assign clusters to the input data using the fitted centroids.

        Parameters
        ----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)

        Returns
        -------
        labels : np.ndarray
            Cluster assignment for each point, shape (n_samples,)

        Raises
        ------
        ValueError: If the model has not been fitted yet.
        """
        if self.centroids is None:
            raise ValueError(
                "Model must be fitted before predictions. Call fit() first."
            )

        self._validate_data(X)
        return self._assign_clusters(X)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        """
        Fit the KMeans model to the data and return cluster assignments.

        Parameters
        ----------
        X : np.ndarray
            Data points, shape (n_samples, n_features)

        Returns
        -------
        labels : np.ndarray
            Cluster assignment for each point, shape (n_samples,)
        """
        self.fit(X)
        assert self.labels_ is not None, "Labels should be set after fit()"
        return self.labels_


# Next: 04_k-means_clustering_lab.ipynb
