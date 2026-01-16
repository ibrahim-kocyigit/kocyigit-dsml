import numpy as np


class KMeans:
    """
    K-Means Clustering Algorithm

    Parameters:
    -----------
    k : int
        Number of clusters
    max_iters : int
        Maximum number of iterations
    tol : float
        Tolerance for convergence (minimum centroid movement)
    random_state : int
        Seed for reproducibility
    """

    def __init__(self, k=3, max_iters=100, tol=1e-4, random_state=None):
        # TODO: Store hyperparameters as instance attributes
        pass

    def _initialize_centroids(self, X):
        """
        Randomly select k data points as initial centroids.

        Hint: Use np.random.choice to select k indices without replacement
        """
        # TODO: Implement centroid initialization
        pass

    def _compute_distances(self, X):
        """
        Compute Euclidean distance from each point to each centroid.

        Returns: Array of shape (n_samples, k)

        Hint: ||x - mu||^2 = sum((x - mu)^2) for each centroid
        """
        # TODO: Implement distance calculation
        pass

    def _assign_clusters(self, X):
        """
        Assign each data point to the nearest centroid.

        Returns: Array of cluster labels, shape (n_samples,)

        Hint: Use np.argmin on the distances
        """
        # TODO: Implement cluster assignment
        pass

    def _update_centroids(self, X):
        """
        Recalculate centroids as the mean of assigned points.

        Hint: For each cluster i, new centroid = mean of all points where label == i
        """
        # TODO: Implement centroid update
        pass

    def _has_converged(self, old_centroids):
        """
        Check if centroids have stopped moving (within tolerance).

        Hint: Compare distance between old and new centroids
        """
        # TODO: Implement convergence check
        pass

    def _compute_inertia(self, X):
        """
        Compute Within-Cluster Sum of Squares (WCSS).

        Formula: J = sum of squared distances from each point to its centroid

        Hint: This is useful for the Elbow Method
        """
        # TODO: Implement inertia calculation
        pass

    def fit(self, X):
        """
        Fit the K-Means model to data X.

        Steps:
        1. Initialize centroids randomly
        2. Loop until convergence or max_iters:
           a. Assign each point to nearest centroid
           b. Save old centroids
           c. Update centroids to cluster means
           d. Check for convergence
        3. Compute final inertia
        """
        # TODO: Implement the main K-Means algorithm
        pass

    def predict(self, X):
        """
        Predict cluster labels for new data points.

        Hint: Use the learned centroids to assign clusters
        """
        # TODO: Implement prediction for new data
        pass

    def fit_predict(self, X):
        """
        Fit the model and return cluster labels.
        """
        # TODO: Combine fit and predict
        pass


# =============================================================================
# TESTING YOUR IMPLEMENTATION
# =============================================================================

if __name__ == "__main__":
    # TODO: Generate sample data using np.random or sklearn.datasets.make_blobs

    # TODO: Create KMeans instance and fit to data

    # TODO: Print results (labels, centroids, inertia)

    # TODO: (Optional) Visualize clusters using matplotlib

    # TODO: (Optional) Compare with sklearn.cluster.KMeans
    pass
