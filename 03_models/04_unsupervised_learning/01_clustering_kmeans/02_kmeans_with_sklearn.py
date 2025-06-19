import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn import metrics

# =======================================
# 1. INTRODUCTION TO UNSUPERVISED LEARNING & CLUSTERING
# =======================================
# - Unsupervised Learning is a type of machine learning where we are given data
#   WITHOUT any labels or target variable (`y`).
# - The goal is to find hidden patterns or intrinsic structures within the data itself.
#
# - Clustering is a primary task in unsupervised learning. Its goal is to group
#   data points such that points in the same group (a "cluster") are more
#   similar to each other than to those in other groups.
#
# - K-Means is the most popular and straightforward clustering algorithm.


# =======================================
# 2. HOW K-MEANS CLUSTERING WORKS
# =======================================
# - The algorithm works iteratively to find the best cluster centers.
#   1. Initialization: Randomly place 'K' initial "centroids" (the center
#      points of the clusters). 'K' is a hyperparameter you must choose.
#   2. Assignment Step: Assign each data point to its nearest centroid.
#   3. Update Step: Recalculate the position of each centroid to be the mean
#      of all the data points assigned to it.
#   4. Repeat: Steps 2 and 3 are repeated until the centroids no longer move
#      significantly (the algorithm has converged).


# =======================================
# 3. STEP 1: CREATE A SYNTHETIC DATASET
# =======================================
# - We'll use scikit-learn's `make_blobs` to create a dataset with clear,
#   globular clusters for our algorithm to find.

print("--- Step 1: Creating Data for Clustering ---")
# `make_blobs` returns X (features) and y (the true cluster labels).
# We will ONLY use `y` at the end to evaluate our model's performance.
# The algorithm itself will never see the `y` labels.
X, y_true = make_blobs(
    n_samples=300,
    centers=4,  # We want to generate 4 distinct clusters
    cluster_std=1.0,  # Controls the spread of the clusters
    random_state=42,
)

# --- Visualize the data as the algorithm sees it (unlabeled) ---
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Unlabeled Synthetic Data for Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
print("Generated a dataset with 4 distinct (but unlabeled) blobs.")
print("-" * 30)


# =======================================
# 4. STEP 2: CREATE AND FIT THE K-MEANS MODEL
# =======================================
# - We follow the standard Scikit-Learn API, but note that `.fit()` only takes `X`.

print("--- Step 2: Training the K-Means Model ---")
# We instantiate the model, telling it to find 4 clusters.
# `n_init='auto'` is the modern default to handle the random initialization smartly.
kmeans = KMeans(n_clusters=4, random_state=42, n_init="auto")

# Fit the model to our feature data X. There is no y!
kmeans.fit(X)
print("K-Means model has been fitted to the data.")
print("-" * 30)


# =======================================
# 5. STEP 3: INSPECT THE RESULTS
# =======================================
# - After fitting, the model has two important attributes:
#   - `.cluster_centers_`: The final coordinates of the centroids.
#   - `.labels_`: An array where each element is the cluster ID (0-3)
#     assigned to the corresponding data point in X.

print("--- Step 3: Inspecting the Results ---")
# Get the coordinates of the final cluster centers
centroids = kmeans.cluster_centers_
print("Final Centroid Locations:\n", centroids.round(2))

# Get the cluster labels assigned to each data point
assigned_labels = kmeans.labels_
print("\nFirst 10 assigned cluster labels:\n", assigned_labels[:10])
print("-" * 30)


# =======================================
# 6. STEP 4: VISUALIZE THE CLUSTERING RESULTS
# =======================================
# - The best way to see the result is to plot the data again, but this time
#   color the points according to the labels assigned by the K-Means algorithm.

print("--- Step 4: Visualizing the Results ---")
plt.figure(figsize=(10, 7))

# Create a scatter plot, coloring points by their assigned labels
plt.scatter(X[:, 0], X[:, 1], c=assigned_labels, s=50, cmap="viridis")

# Plot the final centroids on top
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="red",
    s=200,
    alpha=0.9,
    marker="X",
    label="Centroids",
)

plt.title("K-Means Clustering Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
print("Generated a plot showing the data points colored by their assigned cluster.")


# =======================================
# 7. A NOTE ON EVALUATION
# =======================================
# - Since we have the true labels for this synthetic dataset, we can evaluate
#   how well our unsupervised algorithm did at rediscovering them.
# - The Adjusted Rand Score measures the similarity between two data clusterings.
#   A score of 1.0 is a perfect match.
ari = metrics.adjusted_rand_score(y_true, assigned_labels)
print(f"\nAdjusted Rand Score (vs. true labels): {ari:.3f}")


# --- Display all plots ---
plt.show()

# --- End of File ---
