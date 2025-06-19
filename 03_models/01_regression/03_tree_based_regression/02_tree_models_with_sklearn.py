import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# =======================================
# 1. INTRODUCTION TO TREE-BASED MODELS
# =======================================
# - Unlike linear models that try to fit a single line to the data, tree-based
#   models work by splitting the data into smaller and smaller subsets based on
#   feature values, creating a "tree" of decision rules.
# - Key Advantage: They can capture complex, non-linear relationships in the data
#   without requiring manual feature engineering (like creating polynomial features).
# - Key Disadvantage: A single decision tree is very prone to overfitting.
# - The Solution: Ensemble methods like Random Forest, which combine many trees.


# =======================================
# 2. CREATE A NON-LINEAR SYNTHETIC DATASET
# =======================================
# - To see where tree models shine, we'll create a dataset that a linear model
#   would struggle to fit accurately. A sine wave is a perfect example.

print("--- Step 1: Creating Non-Linear Data ---")
np.random.seed(42)
# Create our feature X
X = np.linspace(0, 10, 100).reshape(-1, 1)
# Create our target y based on a sine wave with some noise
y = np.sin(X).ravel() + np.random.normal(0, 0.15, 100)

# --- Visualize the non-linear data ---
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label="Original Data")
plt.title("Sample Non-Linear Dataset")
plt.xlabel("Feature (X)")
plt.ylabel("Target (y)")
plt.legend()
# We will show all plots at the end.

# --- Split data for training and testing ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print(f"Created a dataset with {len(X)} samples.")
print("-" * 30)


# =======================================
# 3. MODEL 1: DECISION TREE REGRESSOR
# =======================================
# - A single decision tree partitions the feature space into rectangular regions and
#   assigns the average target value of the points in that region as the prediction.
# - If grown to its full depth, it will perfectly memorize the training data,
#   leading to high variance and overfitting.
# - We can control its complexity with hyperparameters like `max_depth`.

print("--- Model 1: Decision Tree Regressor ---")
# Instantiate two models to compare: one with controlled depth, one overfit.
dt_reg_controlled = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_reg_overfit = DecisionTreeRegressor(random_state=42)  # No depth limit

# Fit both models
dt_reg_controlled.fit(X_train, y_train)
dt_reg_overfit.fit(X_train, y_train)
print("Trained two Decision Tree models.")
print("-" * 30)


# =======================================
# 4. MODEL 2: RANDOM FOREST REGRESSOR
# =======================================
# - A Random Forest is an "ensemble" method that solves the overfitting problem.
# - How it works (simplified):
#   1. It builds MANY individual decision trees on random subsets of the data.
#   2. The final prediction is the *average* of the predictions from all the trees.
# - This averaging process reduces variance and results in a more robust and accurate model.
# - `n_estimators` is the hyperparameter for the number of trees in the forest.

print("--- Model 2: Random Forest Regressor ---")
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_train, y_train)
print("Trained a Random Forest model.")
print("-" * 30)


# =======================================
# 5. VISUALIZING MODEL PREDICTIONS
# =======================================
# - A plot makes it easy to see how each model fits the non-linear data.

print("--- Visualizing Model Fits ---")
# Create a new figure to compare the fits
fig, ax = plt.subplots(figsize=(12, 7))

# Create a smooth line of X values for plotting the prediction lines
X_line = np.arange(0, 10, 0.1).reshape(-1, 1)

# Get predictions from all models
y_pred_controlled = dt_reg_controlled.predict(X_line)
y_pred_overfit = dt_reg_overfit.predict(X_line)
y_pred_rf = rf_reg.predict(X_line)

# Plot the original data points
ax.scatter(X, y, alpha=0.5, label="Original Data")

# Plot the model prediction lines
ax.plot(
    X_line, y_pred_controlled, color="orange", lw=2, label="Decision Tree (max_depth=5)"
)
ax.plot(
    X_line,
    y_pred_overfit,
    color="red",
    linestyle=":",
    lw=2,
    label="Decision Tree (Overfit)",
)
ax.plot(X_line, y_pred_rf, color="green", lw=2, label="Random Forest")

ax.set_title("Decision Tree vs. Random Forest Regression", fontsize=16)
ax.set_xlabel("Feature (X)")
ax.set_ylabel("Target (y)")
ax.legend()
ax.grid(True)

print(
    "Displaying plots. Note how the Random Forest provides a much smoother and more general fit."
)
plt.show()

# --- End of File ---
