import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC  # Support Vector Classifier
from sklearn.datasets import make_classification
from sklearn import metrics

# =======================================
# 1. INTRODUCTION TO SUPPORT VECTOR MACHINES (SVM)
# =======================================
# - SVM is a powerful and versatile classification algorithm.
# - Core Idea: It finds the optimal hyperplane (a line in 2D, a plane in 3D, etc.)
#   that best separates the classes by maximizing the "margin" or distance
#   between the closest points of the different classes.
#
# - Support Vectors: These are the data points that lie closest to the decision
#   boundary. They are the critical points that "support" or define the hyperplane.
#
# - The Kernel Trick: To handle non-linear data, SVMs use a "kernel trick" to
#   project the data into a higher dimension where it becomes linearly separable.
#   Common kernels: 'linear', 'poly', 'rbf' (Radial Basis Function).
#
# - CRITICAL: Like KNN, SVMs are highly sensitive to the scale of the features.
#   Feature scaling is an essential preprocessing step.


# =======================================
# 2. STEP 1 & 2: CREATE, SPLIT, AND SCALE THE DATA
# =======================================
# - We'll use the same data generation and preprocessing steps for consistency.

print("--- Step 1 & 2: Data Preparation ---")
# Create data
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=42,
    n_clusters_per_class=1,
)
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Created, split, and scaled the dataset.")
print("-" * 30)


# =======================================
# 3. MODEL 1: LINEAR SVM
# =======================================
# - A linear SVM finds a straight-line decision boundary.

print("--- Model 1: Linear SVM ---")
# Instantiate the model with a linear kernel
linear_svm = SVC(kernel="linear", random_state=42)

# Train the model
linear_svm.fit(X_train_scaled, y_train)
print("Linear SVM model trained.")
y_pred_linear = linear_svm.predict(X_test_scaled)
accuracy_linear = metrics.accuracy_score(y_test, y_pred_linear)
print(f"Linear SVM Accuracy: {accuracy_linear:.3f}")
print("-" * 30)


# =======================================
# 4. MODEL 2: NON-LINEAR SVM (RBF KERNEL)
# =======================================
# - The RBF kernel allows the SVM to find complex, non-linear decision boundaries.
# - It is a powerful and common default choice for SVMs.
# - Key Hyperparameters:
#   - `C`: Regularization parameter. Controls the trade-off between a smooth
#     decision boundary and classifying training points correctly.
#   - `gamma`: Kernel coefficient. Defines how much influence a single training
#     example has.

print("--- Model 2: Non-Linear SVM (RBF Kernel) ---")
rbf_svm = SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42)
rbf_svm.fit(X_train_scaled, y_train)
print("RBF SVM model trained.")
y_pred_rbf = rbf_svm.predict(X_test_scaled)
accuracy_rbf = metrics.accuracy_score(y_test, y_pred_rbf)
print(f"RBF SVM Accuracy: {accuracy_rbf:.3f}")
print("-" * 30)


# =======================================
# 5. VISUALIZING THE DECISION BOUNDARIES
# =======================================
# - The plot will show the linear vs. non-linear boundaries and highlight
#   the support vectors that define them.

print("--- Visualizing Decision Boundaries and Support Vectors ---")
# --- Create a figure with two subplots ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("SVM Decision Boundaries", fontsize=16)

models = [linear_svm, rbf_svm]
titles = ["Linear SVM", "RBF Kernel SVM"]

# --- Loop through models to plot ---
for i, model in enumerate(models):
    ax = axes[i]

    # Create a mesh grid
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

    # Predict on the grid (must use the same scaler)
    Z = model.predict(scaler.transform(np.c_[xx.ravel(), yy.ravel()]))
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3, cmap="viridis")

    # Plot the test data
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap="viridis", edgecolors="k")

    # Highlight the support vectors
    ax.scatter(
        model.support_vectors_[:, 0],
        model.support_vectors_[:, 1],
        s=100,
        facecolors="none",
        edgecolors="red",
        lw=2,
        label="Support Vectors",
    )

    ax.set_title(titles[i])
    ax.set_xlabel("Feature 1 (Scaled)")
    ax.set_ylabel("Feature 2 (Scaled)")
    ax.legend()

print("Generated plots showing model decision boundaries and support vectors.")

# --- Display the plots ---
plt.show()

# --- End of File ---
