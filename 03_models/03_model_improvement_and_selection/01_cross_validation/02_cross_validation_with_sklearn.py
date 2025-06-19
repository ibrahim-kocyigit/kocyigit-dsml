import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# =======================================
# 1. THE LIMITATION OF A SINGLE TRAIN-TEST SPLIT
# =======================================
# - In previous lessons, we used a single `train_test_split` to evaluate our models.
# - The Problem: The resulting performance score (e.g., accuracy) can be heavily
#   dependent on which data points *randomly* ended up in the training vs. the testing set.
# - You might have gotten a "lucky" split, resulting in an overly optimistic score,
#   or an "unlucky" split with a pessimistic score. A single score is not always reliable.
#
# - The Solution: Cross-Validation (CV).
# - CV is a more robust evaluation technique that involves training and evaluating
#   a model on multiple, different splits of the data to get a more stable and
#   reliable estimate of its performance on unseen data.


# =======================================
# 2. K-FOLD CROSS-VALIDATION EXPLAINED
# =======================================
# - K-Fold CV is the most common type of cross-validation. The process is as follows:
#   1. The dataset is split into 'k' equal-sized subsets, called "folds" (e.g., k=5 or k=10).
#   2. The model is trained and evaluated 'k' times.
#   3. In each iteration, one different fold is held out as the test set, and the
#      remaining k-1 folds are used for training.
#   4. The performance score from each iteration is recorded.
#
# - Example with k=5:
#   Iteration 1: [TEST ] [TRAIN] [TRAIN] [TRAIN] [TRAIN] -> Score 1
#   Iteration 2: [TRAIN] [TEST ] [TRAIN] [TRAIN] [TRAIN] -> Score 2
#   Iteration 3: [TRAIN] [TRAIN] [TEST ] [TRAIN] [TRAIN] -> Score 3
#   Iteration 4: [TRAIN] [TRAIN] [TRAIN] [TEST ] [TRAIN] -> Score 4
#   Iteration 5: [TRAIN] [TRAIN] [TRAIN] [TRAIN] [TEST ] -> Score 5
#
# - The final result is the average and standard deviation of these 'k' scores. This gives
#   a much better picture of the model's expected performance and its stability.


# =======================================
# 3. IMPLEMENTING CV WITH `cross_val_score`
# =======================================
# - Scikit-Learn's `cross_val_score` function makes performing K-Fold CV very easy.

# --- Step 1: Create a sample dataset ---
X, y = make_classification(n_samples=100, n_features=20, random_state=42)

# --- Step 2: Instantiate the model ---
model = LogisticRegression()

print("--- Implementing 5-Fold Cross-Validation ---")
# --- Step 3: Use `cross_val_score` ---
# - We pass the model instance, the ENTIRE dataset (X and y), and specify `cv`.
# - `cv=5` means we are performing 5-fold cross-validation.
# - `scoring` specifies which metric to calculate in each fold.
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")

print(f"Scores for each of the 5 folds: {scores.round(3)}")
print(f"\nAverage CV Accuracy: {scores.mean():.3f}")
print(f"Standard Deviation of CV Accuracy: {scores.std():.3f}")
print(
    f"\nThis means our model's performance is expected to be around {scores.mean():.2f} ± {scores.std():.2f}."
)
print("-" * 30)


# =======================================
# 4. CV vs. TRAIN-TEST SPLIT: WHEN TO USE WHAT?
# =======================================
# - This is a common point of confusion. They serve different purposes.
#
# - Cross-Validation is used for:
#   - Robust Model Evaluation: Getting a reliable estimate of a model's performance.
#   - Model Selection: Comparing different models (e.g., Logistic Regression vs. Random Forest)
#     to see which one performs better on average.
#   - Hyperparameter Tuning: Finding the best settings for a model (topic of the next lesson).
#   - You perform CV on your *training data*.
#
# - Train-Test Split is used for:
#   - Final Evaluation: After you have used CV to select your best model and its best
#     hyperparameters, you do a final training run on the *entire* training set.
#   - You then evaluate this final model ONCE on the held-back, completely unseen test set.
#     This score is the final result you report.
#
# --- The Combined Workflow ---
# 1. `train_test_split` the entire dataset ONCE to create a final hold-out test set.
# 2. Use `cross_val_score` on the TRAINING portion to select and tune your best model.
# 3. Train your final chosen model on the ENTIRE training portion.
# 4. Report the final performance by evaluating on the hold-out test set.

print("--- Summary of Roles ---")
print("Cross-Validation: Used during development to reliably choose the best model.")
print(
    "Train-Test Split: Used to create a final, unseen hold-out set for the final report."
)

# --- End of File ---
