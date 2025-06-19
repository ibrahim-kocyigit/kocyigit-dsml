import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# =======================================
# 1. WHAT IS DIMENSIONALITY REDUCTION?
# =======================================
# - Dimensionality reduction is the process of reducing the number of input
#   features in a dataset while preserving as much important information as possible.
#
# - Why do it? (The "Curse of Dimensionality")
#   - As the number of features (dimensions) grows, the amount of data needed
#     to train a model effectively grows exponentially.
#   - Many algorithms become computationally slow or intractable in high dimensions.
#   - It can help remove redundant features and noise, sometimes leading to better model performance.
#
# - Principal Component Analysis (PCA) is the most widely used technique for
#   linear dimensionality reduction.


# =======================================
# 2. HOW PCA WORKS (INTUITIVE EXPLANATION)
# =======================================
# - PCA finds a new set of axes (called "principal components") for the data.
# - These new axes are ordered by the amount of variance they explain.
#   - The 1st component (PC1) is the direction that captures the most variance.
#   - PC2 is the next direction (orthogonal to PC1) that captures the most *remaining* variance.
# - By keeping only the first few components (e.g., the top 2), we can project the
#   original data onto a lower-dimensional space, creating a "shadow" of the
#   original data that preserves most of its structure.
#
# - CRITICAL: PCA is based on maximizing variance, so it is highly sensitive to
#   the scale of the features. Feature scaling is a mandatory preprocessing step.


# =======================================
# 3. STEP 1: CREATE A 3D SYNTHETIC DATASET
# =======================================
# - To demonstrate PCA, we'll create 3D data that has an underlying 2D structure
#   (like a "pancake" or plane of points in 3D space).

print("--- Step 1: Creating 3D Data ---")
np.random.seed(42)
# Create two independent base vectors
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
# Create 100 random points that are linear combinations of the two vectors plus noise
X = (
    (np.random.randn(100, 1) * vec1)
    + (np.random.randn(100, 1) * vec2)
    + np.random.randn(100, 3) * 0.5
)

# --- Visualize the original 3D data ---
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_title("Original 3D Dataset")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_zlabel("Feature 3")
print(f"Created a dataset with shape: {X.shape}")
print("-" * 30)


# =======================================
# 4. STEP 2: SCALE THE DATA AND APPLY PCA
# =======================================
# - We'll scale the data and then use PCA to reduce it from 3 to 2 dimensions.

print("--- Step 2: Scaling Data and Applying PCA ---")
# --- Scale the data ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- Apply PCA ---
# Instantiate PCA, telling it we want to reduce to 2 components.
pca = PCA(n_components=2)

# Fit PCA on the scaled data and transform it.
X_pca = pca.fit_transform(X_scaled)
print(f"Data shape after PCA: {X_pca.shape}")


# --- Inspect the results ---
# `explained_variance_ratio_` tells you the proportion of variance captured by each component.
print(
    f"\nExplained variance ratio of the 2 components: {pca.explained_variance_ratio_.round(3)}"
)
total_variance_explained = np.sum(pca.explained_variance_ratio_)
print(f"Total variance captured by the 2 components: {total_variance_explained:.2%}")
print("-" * 30)


# =======================================
# 5. STEP 3: VISUALIZE THE REDUCED 2D DATA
# =======================================
# - Now we can plot the result of our transformation, `X_pca`, as a simple 2D scatter plot.

print("--- Step 3: Visualizing the 2D Result ---")
plt.figure(figsize=(10, 7))
plt.scatter(
    X_pca[:, 0], X_pca[:, 1], c=X[:, 2], cmap="viridis"
)  # Color by the original 3rd dimension
plt.title("Data after PCA (Reduced to 2 Dimensions)")
plt.xlabel("First Principal Component")
plt.ylabel("Second Principal Component")
plt.grid(True)
plt.colorbar(label="Original Value of Feature 3")

print("Generated a 2D plot of the data projected onto its principal components.")


# --- Display all plots ---
plt.show()

# =======================================
# 6. USE CASES
# =======================================
# - Data Visualization: Reducing high-dimensional data to 2D or 3D for plotting.
# - Noise Reduction: Discarding components with low variance can filter out noise.
# - Preprocessing for ML: Using the reduced-dimension data can speed up training
#   and sometimes improve the performance of other ML algorithms.

# --- End of File ---
