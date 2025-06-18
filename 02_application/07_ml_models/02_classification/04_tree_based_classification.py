import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
from sklearn import metrics

# =======================================
# 1. INTRODUCTION TO TREE-BASED CLASSIFICATION
# =======================================
# - Tree-based models learn a hierarchy of simple if/else questions on the features
#   to split the data into purer and purer subsets.
#
# - Key Advantage: They can learn complex, non-linear decision boundaries.
#
# - IMPORTANT: Unlike distance-based models (KNN, SVM), tree-based models are
#   NOT sensitive to the scale of the features. Feature scaling is not required.
#
# - The Overfitting Problem: A single, deep decision tree is very prone to overfitting
#   by creating a unique "leaf" for every training sample.
#
# - The Ensemble Solution: A Random Forest builds MANY decision trees on random
#   subsets of the data and features, then takes a majority vote for the final
#   prediction. This drastically reduces overfitting and improves accuracy.


# =======================================
# 2. CREATE A NON-LINEAR SYNTHETIC DATASET
# =======================================
# - To see where tree models shine, we'll create a "moons" dataset, which
#   is impossible for a linear model to separate correctly.

print("--- Step 1: Creating Non-Linear Data ---")
# `make_moons` creates two interleaving half-circles.
X, y = make_moons(n_samples=300, noise=0.25, random_state=42)

# --- Visualize the data ---
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", edgecolors="k")
plt.title("Synthetic 'Moons' Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# --- Split data for training and testing ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print(f"Created a dataset with {len(X)} samples.")
print("-" * 30)


# =======================================
# 3. MODEL 1: DECISION TREE CLASSIFIER
# =======================================
# - We control the tree's complexity with `max_depth` to prevent overfitting.

print("--- Model 1: Decision Tree Classifier ---")
# Instantiate the model with a controlled depth
dt_clf = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_clf.fit(X_train, y_train)

# Evaluate the model
y_pred_dt = dt_clf.predict(X_test)
accuracy_dt = metrics.accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree Accuracy: {accuracy_dt:.3f}")
print("-" * 30)


# =======================================
# 4. MODEL 2: RANDOM FOREST CLASSIFIER
# =======================================
# - The Random Forest combines many trees to create a more robust model.
# - `n_estimators` is the hyperparameter for the number of trees in the forest.

print("--- Model 2: Random Forest Classifier ---")
# Instantiate the model with 100 trees
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)

# Evaluate the model
y_pred_rf = rf_clf.predict(X_test)
accuracy_rf = metrics.accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {accuracy_rf:.3f}")
print("-" * 30)


# =======================================
# 5. VISUALIZING THE DECISION BOUNDARIES
# =======================================
# - The plot will clearly show the "stair-step", axis-aligned nature of a single
#   decision tree vs. the smoother, more generalized boundary of the Random Forest.

print("--- Visualizing Decision Boundaries ---")
# --- Create a figure with two subplots ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("Decision Tree vs. Random Forest Decision Boundaries", fontsize=16)

models = [dt_clf, rf_clf]
titles = ["Decision Tree (max_depth=5)", "Random Forest (100 estimators)"]

# --- Loop through models to plot ---
for i, model in enumerate(models):
    ax = axes[i]

    # Create a mesh grid
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

    # Predict on the grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.4, cmap="viridis")

    # Overlay the actual test data points
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap="viridis", edgecolors="k")

    ax.set_title(titles[i])
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")

print("Generated plots showing the models' decision boundaries.")


# --- Display all plots ---
plt.show()

# --- End of File ---
