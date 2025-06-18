import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.datasets import make_regression
from sklearn import metrics

# =======================================
# 1. WHAT IS REGULARIZATION?
# =======================================
# - The Problem (Overfitting): When a model has many features, a standard Linear
#   Regression might fit the training data too closely, learning the "noise"
#   instead of the underlying pattern. This leads to poor performance on new, unseen data.
#
# - The Solution (Regularization): A technique that adds a "penalty" term to the
#   model's loss function. This penalty discourages the model from learning
#   overly complex patterns or assigning large weights (coefficients) to its features.
#
# - Two Common Types:
#   1. Ridge Regression (L2 Penalty): Shrinks coefficients towards zero. Good for general-purpose regularization.
#   2. Lasso Regression (L1 Penalty): Can shrink some coefficients all the way to
#      exactly zero. This makes it useful for automatic "feature selection".


# =======================================
# 2. CREATE A SYNTHETIC DATASET
# =======================================
# - To see the effect of regularization, we need a dataset where overfitting is a risk.
# - We'll create one with many features, but only a few that are actually useful.

print("--- Step 1: Creating Data ---")
X, y = make_regression(
    n_samples=100,
    n_features=50,  # 50 total features
    n_informative=10,  # ...but only 10 are actually useful
    noise=20,  # Add some noise to the target
    random_state=42,
)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print(f"Created a dataset with {X.shape[1]} features.")
print("-" * 30)


# =======================================
# 3. MODEL 1: STANDARD LINEAR REGRESSION (BASELINE)
# =======================================
# - Let's see how a standard linear model performs on this complex data.

print("--- Model 1: Standard Linear Regression ---")
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lin = lin_reg.predict(X_test)
r2_lin = metrics.r2_score(y_test, y_pred_lin)

print(f"R-squared (R2) Score: {r2_lin:.3f}")
# This score might look good, but the model is likely unstable due to using all 50 features.
print("-" * 30)


# =======================================
# 4. MODEL 2: RIDGE REGRESSION (L2 PENALTY)
# =======================================
# - Ridge adds a penalty proportional to the square of the coefficients.
# - It pushes coefficients to be smaller, leading to a more stable, less overfit model.
# - `alpha` controls the strength of the penalty (higher alpha = stronger penalty).

print("--- Model 2: Ridge Regression (L2) ---")
# We'll use the default alpha=1.0
ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_train, y_train)
y_pred_ridge = ridge_reg.predict(X_test)
r2_ridge = metrics.r2_score(y_test, y_pred_ridge)

print(f"R-squared (R2) Score: {r2_ridge:.3f}")
# The R2 score is often more stable and reliable than the standard linear regression.
print("-" * 30)


# =======================================
# 5. MODEL 3: LASSO REGRESSION (L1 PENALTY)
# =======================================
# - Lasso adds a penalty proportional to the absolute value of the coefficients.
# - Its key feature is that it can force some feature coefficients to be exactly zero,
#   effectively performing automatic feature selection.

print("--- Model 3: Lasso Regression (L1) ---")
# We'll use alpha=1.0 here as well. Finding the best alpha is part of hyperparameter tuning.
lasso_reg = Lasso(alpha=1.0)
lasso_reg.fit(X_train, y_train)
y_pred_lasso = lasso_reg.predict(X_test)
r2_lasso = metrics.r2_score(y_test, y_pred_lasso)

print(f"R-squared (R2) Score: {r2_lasso:.3f}")

# Let's inspect the coefficients to see the feature selection in action
num_zero_coeffs = np.sum(lasso_reg.coef_ == 0)
print(
    f"Number of coefficients forced to zero: {num_zero_coeffs} out of {len(lasso_reg.coef_)}"
)
print("-" * 30)


# =======================================
# 6. VISUALIZING THE COEFFICIENTS
# =======================================
# - A plot makes the effect of regularization on the model's coefficients very clear.

print("--- Visualizing Model Coefficients ---")
fig, ax = plt.subplots(figsize=(14, 7))

models = ["Linear", "Ridge", "Lasso"]
coefficients = [lin_reg.coef_, ridge_reg.coef_, lasso_reg.coef_]

# Create a DataFrame for easy plotting
coef_df = pd.DataFrame(coefficients, index=models).T

coef_df.plot(kind="bar", ax=ax)

ax.set_title("Comparison of Model Coefficients", fontsize=16)
ax.set_ylabel("Coefficient Value")
ax.set_xlabel("Feature Index")
ax.grid(axis="y", linestyle="--", alpha=0.7)

print("Displaying plot comparing the coefficients of the three models.")
print("Note how Ridge shrinks coefficients and Lasso forces many to zero.")
plt.tight_layout()
plt.show()

# --- End of File ---
