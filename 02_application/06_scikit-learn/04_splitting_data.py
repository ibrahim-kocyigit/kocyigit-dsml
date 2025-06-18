import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# =======================================
# 1. THE IMPORTANCE OF SPLITTING DATA
# =======================================
# - This is a core principle of machine learning evaluation.
# - The Problem (Overfitting): If you train a model and evaluate it on the same data,
#   it will perform very well because it may have simply "memorized" the data,
#   including its noise. It will fail to generalize to new, unseen data.
#
# - The Solution (Train-Test Split): We partition our data into two sets:
#   1. Training Set: The majority of the data, used to train the model.
#   2. Testing Set: A held-back portion of the data. The model NEVER sees this
#      during training. It's used at the end to get an unbiased evaluation of
#      how well the model performs on new data.
#
# - Analogy: The training set is the textbook and homework problems. The testing set
#   is the final, unseen exam.


# =======================================
# 2. CREATING A SAMPLE DATASET
# =======================================
# - Let's create a simple dataset to demonstrate the split.
# - We need a features matrix `X` and a target vector `y`.

# A features matrix with 10 samples and 2 features
X = np.arange(20).reshape(10, 2)
# A target vector with 10 corresponding labels
y = np.arange(10)

print("--- Original Sample Data ---")
print("Features matrix X (shape {}):\n".format(X.shape), X)
print("\nTarget vector y (shape {}):\n".format(y.shape), y)
print("-" * 30)


# =======================================
# 3. USING `train_test_split`
# =======================================
# - Scikit-Learn's `train_test_split` function is the standard tool for this task.

print("--- Using train_test_split ---")
# --- Basic Split ---
# This function shuffles the data and splits it into four pieces.
X_train, X_test, y_train, y_test = train_test_split(X, y)

print("Default split (usually 75% train, 25% test):")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")


# --- Controlling the Split ---
# - `test_size`: Specifies the proportion of the data to allocate to the test set.
# - `random_state`: A CRITICAL parameter. Setting this to an integer ensures that
#   the *same* random split is generated every time you run the code. This makes
#   your results reproducible.

print("\n--- Split with specified parameters ---")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Split with test_size=0.3 and random_state=42:")
print("X_train:\n", X_train)
print("\nX_test:\n", X_test)
print("-" * 30)


# =======================================
# 4. STRATIFIED SPLITTING FOR CLASSIFICATION
# =======================================
# - The Problem: In classification tasks, if one class is rare, a random split might
#   create a training or testing set with a skewed or non-existent representation of that class.
# - The Solution: Stratified splitting. It ensures that the proportion of each class
#   is the same in both the original dataset, the training set, and the testing set.
# - You do this with the `stratify` parameter.

print("--- Stratified Splitting ---")
# --- Create an imbalanced dataset ---
# A dataset with 90 samples of class 0 and 10 samples of class 1.
X_imbalanced = np.arange(200).reshape(100, 2)
y_imbalanced = np.array([0] * 90 + [1] * 10)

print(f"Original class proportions: {np.bincount(y_imbalanced) / len(y_imbalanced)}")

# --- Perform a stratified split ---
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_imbalanced, y_imbalanced, test_size=0.3, random_state=42, stratify=y_imbalanced
)

print(
    f"\nTraining set class proportions (stratified): {np.bincount(y_train_s) / len(y_train_s)}"
)
print(
    f"Testing set class proportions (stratified):  {np.bincount(y_test_s) / len(y_test_s)}"
)
print("\nNote how the proportions are maintained in both sets.")

# --- End of File ---
