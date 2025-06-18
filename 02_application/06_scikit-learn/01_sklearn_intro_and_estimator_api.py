import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# =======================================
# 1. WHAT IS SCIKIT-LEARN?
# =======================================
# - Scikit-Learn (`sklearn`) is Python's most popular and comprehensive library
#   for "classical" machine learning algorithms.
# - It focuses on:
#   - Classification, Regression, Clustering, Dimensionality Reduction
#   - Model selection and evaluation
#   - Data preprocessing
# - It does NOT focus on deep learning (that's for libraries like TensorFlow or PyTorch).
# - It is built on top of NumPy, SciPy, and Matplotlib.


# =======================================
# 2. INSTALLATION AND IMPORTS
# =======================================
# - To install Scikit-Learn, run this command in your terminal:
#   `pip install scikit-learn`
#
# - Imports are typically done from specific submodules, e.g.,
#   `from sklearn.module import Class`


# =======================================
# 3. THE CORE OF SCIKIT-LEARN: THE ESTIMATOR API
# =======================================
# - Scikit-Learn's greatest strength is its consistent and simple API. All algorithms
#   (called "estimators") follow the same pattern.
# - This makes it incredibly easy to swap between different models.
#
# --- The Standard Workflow ---
# 1. Choose a model class and import it.
# 2. Instantiate the model class, setting any "hyperparameters".
# 3. Prepare your data into a features matrix `X` (2D) and a target vector `y` (1D).
# 4. "Fit" the model to your data by calling the `.fit(X, y)` method.
# 5. Apply the trained model to new data:
#    - For supervised learning, use `.predict(X_new)`.
#    - For preprocessing/unsupervised learning, use `.transform(X_new)` or `.fit_transform(X)`.


# =======================================
# 4. A SIMPLE DEMONSTRATION OF THE API
# =======================================
print("--- A Simple API Demonstration ---")
# --- Step 1 & 3: Choose Model and Prepare Data ---
# We'll use a simple linear regression model and create some trivial data.
# Relationship: y = 2x
X = np.array([[1], [2], [3], [4], [5]])  # Features must be a 2D array
y = np.array([2, 4, 6, 8, 10])  # Target is a 1D array

# --- Step 2: Instantiate the model ---
model = LinearRegression()
print(f"1. Instantiated model: {model}")

# --- Step 4: Fit the model to the data ---
# This is the "learning" step. The model finds the best line to fit the data.
model.fit(X, y)
print("\n2. Model has been fitted (trained).")

# --- After fitting, the model has learned attributes (note the trailing underscore) ---
print(f"   - Learned slope (coefficient): {model.coef_[0]:.1f}")
print(f"   - Learned intercept: {model.intercept_:.1f}")

# --- Step 5: Predict on new, unseen data ---
X_new = np.array([[6], [7]])
predictions = model.predict(X_new)
print(f"\n3. Predicting on new data {X_new.flatten()}: {predictions.round(1)}")
print("-" * 30)


# =======================================
# 5. PREVIEW: THE TRANSFORMER API
# =======================================
# - Preprocessing steps (like scaling data) also follow the same API pattern.
# - They use `.fit()` to learn from the data (e.g., learn the mean and std dev)
#   and `.transform()` to apply the transformation.
# - `.fit_transform()` is a convenient shortcut that does both steps at once.
# - NOTE: This will be covered in detail in the next lesson.

print("--- Preview of the Transformer API ---")
# Create some sample data with different scales
data_to_scale = np.array([[0], [10], [50], [100]])
print("Original data:\n", data_to_scale)

# 1. Instantiate the transformer
scaler = StandardScaler()

# 2. Fit to the data and transform it
# This scales the data to have a mean of 0 and a standard deviation of 1.
scaled_data = scaler.fit_transform(data_to_scale)
print("\nData after applying StandardScaler:\n", scaled_data.round(2))


# --- End of File ---
