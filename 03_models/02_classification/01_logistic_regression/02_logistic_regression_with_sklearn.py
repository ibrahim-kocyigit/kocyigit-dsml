import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn import metrics

# =======================================
# 1. INTRODUCTION TO LOGISTIC REGRESSION
# =======================================
# - Despite its name, Logistic Regression is a CLASSIFICATION algorithm, not regression.
# - It is the foundational algorithm for binary classification (predicting one of two
#   outcomes, e.g., Yes/No, True/False, 1/0).
#
# - How it works (simplified):
#   1. It calculates a weighted sum of the input features (like linear regression).
#   2. It passes this result through a "sigmoid" or "logistic" function.
#   3. The sigmoid function squashes the output to be a probability between 0 and 1.
#   4. A threshold (typically 0.5) is used to convert this probability into a
#      class prediction (e.g., if probability > 0.5, predict class 1).


# --- Visualize the Sigmoid Function ---
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


z = np.linspace(-10, 10, 100)
plt.figure(figsize=(8, 4))
plt.plot(z, sigmoid(z))
plt.title("The Sigmoid (Logistic) Function")
plt.xlabel("Input Value (z)")
plt.ylabel("Output Probability")
plt.axhline(0.5, color="red", linestyle="--", label="Decision Boundary (0.5)")
plt.legend()
# We'll show all plots at the end.


# =======================================
# 2. STEP 1: CREATE A SYNTHETIC DATASET
# =======================================
# - We'll use scikit-learn's `make_classification` to create a dataset of points
#   that are well-suited for a binary classification task.

print("--- Step 1: Creating Data ---")
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=42,
    n_clusters_per_class=1,
)

# --- Visualize the data ---
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", edgecolors="k")
plt.title("Synthetic Classification Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

print(f"Created a dataset with {X.shape[0]} samples.")
print("-" * 30)


# =======================================
# 3. STEP 2 & 3: SPLIT DATA AND TRAIN THE MODEL
# =======================================
print("--- Step 2 & 3: Splitting and Training ---")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Instantiate and fit the model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
print("Logistic Regression model trained successfully.")
print("-" * 30)


# =======================================
# 4. STEP 4: MAKE PREDICTIONS
# =======================================
# - Logistic regression can provide both hard class predictions and soft probability predictions.
print("--- Step 4: Making Predictions ---")
# `.predict()` gives the final class prediction (0 or 1)
y_pred = model.predict(X_test)

# `.predict_proba()` gives the probability for each class [prob_of_0, prob_of_1]
y_proba = model.predict_proba(X_test)

print("Sample Predictions:")
for i in range(5):
    print(
        f"Sample {i}: Actual={y_test[i]}, Predicted={y_pred[i]}, Probabilities=[{y_proba[i][0]:.2f}, {y_proba[i][1]:.2f}]"
    )
print("-" * 30)


# =======================================
# 5. STEP 5: VISUALIZE THE DECISION BOUNDARY
# =======================================
# - The best way to understand what a classifier has learned is to visualize its
#   "decision boundary"—the line that separates the different classes.
print("--- Step 5: Visualizing the Decision Boundary ---")
fig_boundary, ax = plt.subplots(figsize=(10, 6))

# Create a mesh grid
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# Predict on every point of the grid
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Create a contour plot to color the regions
ax.contourf(xx, yy, Z, alpha=0.3, cmap="viridis")

# Overlay the actual test data points
ax.scatter(
    X_test[:, 0], X_test[:, 1], c=y_test, cmap="viridis", edgecolors="k", marker="o"
)
ax.set_title("Logistic Regression Decision Boundary")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")

print("Generated a plot showing the model's decision boundary.")
print("-" * 30)


# =======================================
# 6. STEP 6: EVALUATE THE MODEL
# =======================================
# - We'll cover classification metrics in detail later, but let's look at accuracy.
print("--- Step 6: Evaluating the Model ---")
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.3f}")
# Accuracy = (Number of correct predictions) / (Total number of predictions)


# --- Display all plots ---
print("\nDisplaying plots. Close the windows to end the script.")
plt.show()

# --- End of File ---
