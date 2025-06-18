import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# =======================================
# 1. WHY IS FEATURE SCALING NECESSARY?
# =======================================
# - Many machine learning algorithms perform better when numerical input features
#   are on a similar scale.
# - The Problem: If features have vastly different scales (e.g., 'Age' from 20-70
#   and 'Salary' from 40,000-150,000), the feature with the larger scale can
#   dominate the learning process.
# - Algorithms sensitive to feature scaling include:
#   - Distance-based algorithms: K-Nearest Neighbors (KNN), Support Vector Machines (SVM), Clustering.
#   - Gradient-based algorithms: Linear Regression, Logistic Regression, Neural Networks.
# - Note: Tree-based algorithms (like Decision Trees, Random Forests) are generally
#   not sensitive to feature scaling.


# =======================================
# 2. CREATING A SAMPLE DATASET
# =======================================
# - Let's create a dataset where the need for scaling is obvious.

np.random.seed(42)
data = {
    "Age": np.random.randint(18, 65, 100),
    "EstimatedSalary": np.random.randint(40000, 150000, 100),
    "Purchased": np.random.randint(0, 2, 100),
}
df = pd.DataFrame(data)

print("--- Original Sample Data (first 5 rows) ---")
print(df.head())
print("\nDescription of original data scales:")
print(df.describe())
print("-" * 30)


# =======================================
# 3. METHOD 1: STANDARDIZATION (`StandardScaler`)
# =======================================
# - Standardization rescales data to have a mean (μ) of 0 and a standard deviation (σ) of 1.
# - This is also known as creating a "z-score". The formula is: z = (x - μ) / σ
# - It's a very common and robust scaling method. It does not bound values to a
#   specific range, which can be good if you have outliers.

print("--- Method 1: Standardization with StandardScaler ---")
# Select only the numerical features to scale
features = ["Age", "EstimatedSalary"]
X = df[features]

# 1. Instantiate the scaler
scaler_std = StandardScaler()

# 2. Fit to the data and transform it
X_standardized = scaler_std.fit_transform(X)

# The result is a NumPy array, let's put it back into a DataFrame for readability
df_standardized = pd.DataFrame(X_standardized, columns=features)

print("Standardized data (first 5 rows):\n", df_standardized.head())
print("\nDescription of standardized data:")
# Note how mean is ~0 and std dev is ~1 for both columns.
print(df_standardized.describe().round(2))
print("-" * 30)


# =======================================
# 4. METHOD 2: NORMALIZATION (`MinMaxScaler`)
# =======================================
# - Normalization (specifically Min-Max scaling) rescales data to a fixed range, usually [0, 1].
# - The formula is: X_norm = (X - X_min) / (X_max - X_min)
# - Useful for algorithms that don't assume any particular distribution, like some neural networks.
# - It can be sensitive to outliers because the min and max values determine the scaling.

print("--- Method 2: Normalization with MinMaxScaler ---")
# 1. Instantiate the scaler
scaler_minmax = MinMaxScaler()

# 2. Fit and transform
X_normalized = scaler_minmax.fit_transform(X)

df_normalized = pd.DataFrame(X_normalized, columns=features)
print("Normalized data (first 5 rows):\n", df_normalized.head())
print("\nDescription of normalized data:")
# Note how min is 0 and max is 1 for both columns.
print(df_normalized.describe().round(2))
print("-" * 30)


# =======================================
# 5. IMPORTANT: FITTING ON TRAINING DATA ONLY
# =======================================
# - CRITICAL BEST PRACTICE: To prevent "data leakage", you must only learn the
#   scaling parameters (mean, std, min, max) from your training data.
# - The testing data is supposed to be unseen. You use the scaler that was "fit"
#   on the training data to transform the test data.
#
# - The Correct Workflow:
#   1. Split your data into training and testing sets.
#   2. Call `scaler.fit_transform()` on the TRAINING data.
#   3. Call `scaler.transform()` (ONLY .transform, not .fit_transform) on the TESTING data.

print("--- Correct Workflow: Fitting Only on Training Data ---")
X_train, X_test = train_test_split(X, test_size=0.3, random_state=42)
scaler = StandardScaler()

# Fit and transform on the training data
X_train_scaled = scaler.fit_transform(X_train)

# ONLY transform the test data
X_test_scaled = scaler.transform(X_test)

print(f"Original X_train shape: {X_train.shape}")
print(f"Scaled X_train shape: {X_train_scaled.shape}")
print(f"Scaled X_test shape: {X_test_scaled.shape}")
print("This prevents the model from 'peeking' at the test set's distribution.")

# --- End of File ---
