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
        self.n_iter_: int | None = None

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
        Check if centroids have stopped moving (within tolerance).

        Hint: Compare distance between old and new centroids using np.linalg.norm
        """
        # TODO: Implement convergence check
        pass

    def _compute_inertia(self, X: np.ndarray, labels: np.ndarray) -> float:
        """
        Compute Within-Cluster Sum of Squares (WCSS).

        Formula: J = sum of squared distances from each point to its centroid

        Hint: This is useful for the Elbow Method
        """
        # TODO: Implement inertia calculation
        pass

    def _validate_data(self, X: np.ndarray) -> None:
        """
        Validate input data.

        Checks:
        - X is 2D array
        - k <= n_samples
        - No NaN or Inf values
        """
        # TODO: Implement validation
        pass

    def fit(self, X: np.ndarray) -> "KMeans":
        """
        Fit the K-Means model to data X.

        Steps:
        1. Validate input data
        2. Initialize centroids randomly
        3. Loop until convergence or max_iters:
           a. Assign each point to nearest centroid
           b. Save old centroids
           c. Update centroids to cluster means
           d. Check for convergence
        4. Compute final inertia and store results

        Returns:
        --------
        self : KMeans
            Fitted estimator
        """
        # TODO: Implement the main K-Means algorithm
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict cluster labels for new data points.

        Hint: Use the learned centroids to assign clusters

        Raises:
        -------
        ValueError: If model hasn't been fitted yet
        """
        # TODO: Implement prediction for new data
        pass

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        """
        Fit the model and return cluster labels.
        """
        # TODO: Combine fit and predict
        pass


# =============================================================================
# TESTING YOUR IMPLEMENTATION
# =============================================================================

if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    import matplotlib.pyplot as plt

    # TODO: Generate sample data using make_blobs

    # TODO: Create KMeans instance and fit to data

    # TODO: Print results (labels, centroids, inertia, n_iter)

    # TODO: (Optional) Visualize clusters using matplotlib

    # TODO: (Optional) Implement Elbow Method

    # TODO: (Optional) Compare with sklearn.cluster.KMeans
    pass
