from __future__ import annotations

import numpy as np
import numpy.typing as npt


class DBSCAN:
    def __init__(self, eps: float = 0.5, min_samples: int = 5) -> None:
        """
        Density-Based Spatial Clustering of Applications with Noise (DBSCAN) implementation.

        DBSCAN is a clustering algorithm that groups together points that are closely packed together,
        marking as outliers points that lie alone in low-density regions. It requires two parameters:
        - eps: The maximum distance between two samples for them to be considered as in the same neighborhood.
        - min_samples: The number of samples (or total weight) in a neighborhood for a point to be considered as a core point.

        Attributes:
            eps (float): The maximum distance between two samples for them to be considered neighbors.
            min_samples (int): The number of samples required to form a dense region (core point).
            labels_ (np.ndarray): Cluster labels for each point in the dataset after fitting.
            core_samples_ (np.ndarray): Boolean mask indicating which points are core points.
            visited (np.ndarray): Boolean mask indicating which points have been visited during clustering.
            n_clusters_ (int): Number of clusters found.
            n_noise_ (int): Number of noise points detected.
        """
        self.eps = eps
        self.min_samples = min_samples
        self.labels_: npt.NDArray[np.int16] | None = None
        self.core_samples_: npt.NDArray[np.bool_] | None = None
        self.visited: npt.NDArray[np.bool_] | None = None
        self.n_clusters_: int | None = None
        self.n_noise_: int | None = None

    def _get_neighbors(self, X: np.ndarray, point_id: int) -> list[int]:
        """
        Find all points in the dataset X within self.eps distance of the point at point_id.

        Parameters:
            X (np.ndarray): The dataset of points.
            point_id (int): The index of the point to find neighbors for.

        Returns:
            list[int]: Indices of all neighboring points within self.eps distance.
        """
        distances = np.sqrt(np.sum((X - X[point_id]) ** 2, axis=1))
        return np.where(distances <= self.eps)[0].tolist()

    def _expand_cluster(
        self, X: np.ndarray, point_id: int, neighbors: list[int], cluster_id: int
    ) -> None:
        """
        Expand the cluster with all density-reachable points from the given core point.

        Parameters:
            X (np.ndarray): The dataset of points.
            point_id (int): The index of the core point to start expansion from.
            neighbors (list[int]): Indices of neighboring points within self.eps distance.
            cluster_id (int): The cluster label to assign to density-reachable points.

        Returns:
            None
        """
        assert self.labels_ is not None
        assert self.core_samples_ is not None
        assert self.visited is not None

        # Assign cluster_id to the current (core) point
        self.labels_[point_id] = cluster_id

        # Create a queue and add all neighbors to it
        queue = neighbors.copy()

        # While queue is not empty...
        while queue:
            # Pop a point from queue
            current_point = queue.pop(0)

            # If point was already visited, skip it
            if self.visited[current_point]:
                continue

            # Mark point as visited
            self.visited[current_point] = True

            # Get neighbors of this point
            current_neighbors = self._get_neighbors(X, current_point)

            # If point has >= min_samples neighbors (it's a core point):
            if len(current_neighbors) >= self.min_samples:
                # Assign current_point to the cluster (it's a core point):
                self.labels_[current_point] = cluster_id
                self.core_samples_[current_point] = True

                for neighbor in current_neighbors:
                    # If neighbor is noise (-1), reassign to current cluster
                    if self.labels_[neighbor] == -1:
                        self.labels_[neighbor] = cluster_id

                    # If neighbor is unassigned (0), assign to current cluster and add to queue
                    if self.labels_[neighbor] == 0:
                        self.labels_[neighbor] = cluster_id
                        queue.append(neighbor)

    def fit(self, X: np.ndarray) -> DBSCAN:
        """
        Perform DBSCAN clustering from features or distance matrix.

        Parameters:
            X (np.ndarray): The dataset of points to cluster.

        Returns:
            DBSCAN: The fitted DBSCAN instance.
        """
        n_samples = X.shape[0]
        if n_samples == 0:
            raise ValueError("X must contain at least one sample.")

        self.labels_ = np.zeros(n_samples, dtype=np.int16)
        self.core_samples_ = np.zeros(n_samples, dtype=bool)
        self.visited = np.zeros(n_samples, dtype=bool)
        cluster_id = 0

        assert self.labels_ is not None
        assert self.core_samples_ is not None
        assert self.visited is not None

        # For each point in the dataset:
        for point_id in range(n_samples):
            # If point already has a label (not 0) skip it
            if self.labels_[point_id] != 0:
                continue

            # Mark as visited
            self.visited[point_id] = True

            # Get neighbors
            neighbors = self._get_neighbors(X, point_id)

            # If number of neighbors < min_samples:
            if len(neighbors) < self.min_samples:
                # Label point as noise (-1)
                self.labels_[point_id] = -1
            else:
                # Increment cluster_id
                cluster_id += 1
                # Expand cluster from this point
                self._expand_cluster(X, point_id, neighbors, cluster_id)

        # Add cluster metadata
        self.n_clusters_ = cluster_id  # Number of clusters found
        self.n_noise_ = np.sum(self.labels_ == -1)  # Number of noise points

        return self

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        """
        Assign cluster labels to the dataset X and return the labels.

        Parameters:
            X (np.ndarray): The dataset of points to cluster.

        Returns:
            np.ndarray: Array of cluster labels assigned to each point.
        """
        self.fit(X)
        assert self.labels_ is not None
        return self.labels_
