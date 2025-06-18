import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn import metrics

# =======================================
# 1. INTRODUCTION TO K-NEAREST NEIGHBORS (KNN)
# =======================================
# - KNN is a simple, intuitive, and non-parametric classification algorithm.
# - It is often called a "lazy learner" because it doesn't learn a "model" in the
#   traditional sense. It simply memorizes the entire training dataset.
#
# - How it works for classification:
#   1. To classify a new data point, it looks at the 'K' closest data points
#      (its "neighbors") in the training set based on a distance metric (e.g., Euclidean distance).
#   2. It takes a majority vote among those neighbors. The new point is assigned the
#      class that is most common among its K nearest neighbors.
#
# - The "K" is a hyperparameter you must choose. A small K can be sensitive to noise,
#   while a large K can oversmooth the decision boundary.
#
# - CRITICAL: Because KNN is based on distance, it is highly sensitive to the
#   scale of the features. Feature scaling is an essential preprocessing step.


# =======================================
# 2. STEP 1: CREATE AND SPLIT THE DATASET
# =======================================
# - We'll use the same data generation function as the last lesson to allow for
#   a direct comparison with Logistic Regression.

print("--- Step 1: Creating & Splitting Data ---")
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=42,
    n_clusters_per_class=1,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Created and split a dataset with {len(X)} samples.")
print("-" * 30)


# =======================================
# 3. STEP 2: FEATURE SCALING
# =======================================
# - We apply StandardScaler to ensure both features have a similar scale,
#   so that one feature does not dominate the distance calculations.

print("--- Step 2: Scaling Features ---")
scaler = StandardScaler()
# Fit on the training data and transform it
X_train_scaled = scaler.fit_transform(X_train)
# ONLY transform the test data using the scaler fitted on the training data
X_test_scaled = scaler.transform(X_test)
print("Applied StandardScaler to training and testing sets.")
print("-" * 30)


# =======================================
# 4. STEP 3 & 4: CREATE AND TRAIN THE MODEL
# =======================================
# - We instantiate the model with a chosen `n_neighbors` (K) and fit it to the
#   *scaled* training data.

print("--- Step 3 & 4: Training the KNN Model ---")
# Let's choose K=5 for this example
model = KNeighborsClassifier(n_neighbors=5)

# Fit the model
model.fit(X_train_scaled, y_train)
print("KNN model (K=5) trained successfully.")
print("-" * 30)


# =======================================
# 5. STEP 5: MAKE PREDICTIONS
# =======================================
print("--- Step 5: Making Predictions ---")
y_pred = model.predict(X_test_scaled)
print("Sample Predictions:", y_pred[:10])
print("Actual Values:   ", y_test[:10])
print("-" * 30)


# =======================================
# 6. STEP 6: VISUALIZE THE DECISION BOUNDARY
# =======================================
# - The decision boundary for KNN is often complex and non-linear, as it adapts
#   to the local structure of the data. This provides a clear contrast to the
#   straight-line boundary of Logistic Regression.

print("--- Step 6: Visualizing the Decision Boundary ---")
fig, ax = plt.subplots(figsize=(10, 6))

# Create a mesh grid
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# We must scale the grid points before predicting on them
Z = model.predict(scaler.transform(np.c_[xx.ravel(), yy.ravel()]))
Z = Z.reshape(xx.shape)

# Create a contour plot
ax.contourf(xx, yy, Z, alpha=0.3, cmap="viridis")
# Overlay the actual test data points
ax.scatter(
    X_test[:, 0], X_test[:, 1], c=y_test, cmap="viridis", edgecolors="k", marker="o"
)

ax.set_title("K-Nearest Neighbors (K=5) Decision Boundary")
ax.set_xlabel("Feature 1 (Scaled)")
ax.set_ylabel("Feature 2 (Scaled)")

print("Generated a plot showing the model's non-linear decision boundary.")
print("-" * 30)


# =======================================
# 7. STEP 7: EVALUATE THE MODEL
# =======================================
print("--- Step 7: Evaluating the Model ---")
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.3f}")

# The confusion matrix shows a breakdown of correct and incorrect predictions for each class.
conf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)


# --- Display all plots ---
plt.show()

# --- End of File ---
