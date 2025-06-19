import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn import metrics

# =======================================
# 1. PARAMETERS vs. HYPERPARAMETERS
# =======================================
# - It's critical to understand the difference between these two terms.
#
# - Model Parameters: These are values that the model *learns* from the data
#   during the `.fit()` process. You do not set these manually.
#   - Example: The coefficients (`.coef_`) in a Linear Regression.
#
# - Hyperparameters: These are settings or "dials" that you, the user, set
#   *before* training to control the learning process itself.
#   - Example: `n_neighbors` in KNN, `max_depth` in a Decision Tree, `C` and `gamma` in an SVM.
#
# - The Goal of Tuning: To find the combination of hyperparameter values that
#   results in the model with the best performance on unseen data.


# =======================================
# 2. SETUP: CREATE DATA AND SPLIT
# =======================================
# - We'll create a classification dataset and use a Support Vector Machine (SVM),
#   as its performance is highly dependent on its hyperparameters.

X, y = make_classification(
    n_samples=500, n_features=10, n_informative=5, random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("--- Data Prepared for Hyperparameter Tuning ---")
print(f"Training set shape: {X_train.shape}")
print("-" * 30)


# =======================================
# 3. METHOD 1: GRID SEARCH (`GridSearchCV`)
# =======================================
# - Grid Search is an exhaustive search over a specified grid of hyperparameter values.
# - How it works:
#   1. You define a "parameter grid" (a dictionary) of values to test.
#   2. `GridSearchCV` tries every single possible combination of these values.
#   3. For EACH combination, it performs k-fold cross-validation.
#   4. It identifies the combination that produced the best average cross-validation score.

print("--- Method 1: GridSearchCV ---")
# --- Step 1: Define the parameter grid ---
# We want to test different values for 'C', 'gamma', and 'kernel'.
param_grid = {"C": [0.1, 1, 10, 100], "gamma": [1, 0.1, 0.01, 0.001], "kernel": ["rbf"]}
# Total fits = 4 (C) * 4 (gamma) * 1 (kernel) * 5 (cv folds) = 80 fits.

# --- Step 2: Instantiate GridSearchCV ---
# `cv=5`: Use 5-fold cross-validation.
# `verbose=2`: Prints detailed updates as it runs.
grid_search = GridSearchCV(
    estimator=SVC(),
    param_grid=param_grid,
    cv=5,
    verbose=2,
    n_jobs=-1,  # Use all available CPU cores
)

# --- Step 3: Fit the grid search object on the training data ---
print("Fitting GridSearchCV... (This may take a moment)")
grid_search.fit(X_train, y_train)

# --- Step 4: Inspect the results ---
print("\nGridSearchCV results:")
print(f"Best Hyperparameters Found: {grid_search.best_params_}")
print(f"Best Cross-Validation Score (Accuracy): {grid_search.best_score_:.3f}")

# The `best_estimator_` attribute is a ready-to-use model with the best found hyperparameters.
best_model_grid = grid_search.best_estimator_
print(f"Best estimator object: {best_model_grid}")
print("-" * 30)


# =======================================
# 4. METHOD 2: RANDOMIZED SEARCH (`RandomizedSearchCV`)
# =======================================
# - Problem with Grid Search: Can be very slow if the search space is large.
# - Randomized Search: Instead of trying all combinations, it samples a fixed number
#   (`n_iter`) of random combinations from the specified parameter distributions.
# - It's often much faster and can find a "good enough" or even better combination
#   in less time.

print("--- Method 2: RandomizedSearchCV ---")
# --- Step 1: Define the parameter distributions ---
# For continuous values, we can specify distributions to sample from.
from scipy.stats import uniform

param_dist = {
    "C": uniform(loc=0, scale=100),  # Sample uniformly from 0 to 100
    "gamma": ["scale", "auto", 0.1, 0.01],
    "kernel": ["rbf", "poly"],
}

# --- Step 2: Instantiate RandomizedSearchCV ---
# `n_iter=20`: Perform 20 random searches.
# Total fits = 20 (n_iter) * 5 (cv folds) = 100 fits.
random_search = RandomizedSearchCV(
    estimator=SVC(),
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    verbose=2,
    random_state=42,
    n_jobs=-1,
)

# --- Step 3: Fit the randomized search object ---
print("\nFitting RandomizedSearchCV... (This may take a moment)")
random_search.fit(X_train, y_train)

# --- Step 4: Inspect the results ---
print("\nRandomizedSearchCV results:")
print(f"Best Hyperparameters Found: {random_search.best_params_}")
print(f"Best Cross-Validation Score (Accuracy): {random_search.best_score_:.3f}")
print("-" * 30)


# =======================================
# 5. FINAL EVALUATION ON THE TEST SET
# =======================================
# - After finding the best model via cross-validation and tuning, we do one final
#   evaluation on our held-back, completely unseen test set.

print("--- Final Evaluation on the Test Set ---")
# Let's use the best model found by GridSearchCV
final_predictions = best_model_grid.predict(X_test)
final_accuracy = metrics.accuracy_score(y_test, final_predictions)

print(f"Final accuracy on the unseen test set: {final_accuracy:.3f}")

# --- End of File ---
