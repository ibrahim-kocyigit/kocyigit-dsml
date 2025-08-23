import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. What is Broadcasting?
# 2. The Rules of Broadcasting
# 3. Broadcasting Examples
# 4. Practical Application: Data Normalization


# =======================================
# 1. WHAT IS BROADCASTING?
# =======================================
# - Broadcasting is the powerful mechanism that allows NumPy to perform arithmetic
#   operations on arrays of *different* shapes.
# - When operating on two arrays, NumPy compares their shapes element-wise.
#   It starts with the trailing (rightmost) dimensions and works its way left.
# - In essence, the smaller array is "broadcast" across the larger array
#   so that they have compatible shapes. This is done without making extra copies of the data.
# - We've already seen a simple case: operations between an array and a scalar.

arr = np.array([1, 2, 3])
# Here, the scalar `5` is "broadcast" to the shape of `arr`
result = arr + 5  # Conceptually becomes [1, 2, 3] + [5, 5, 5]
print(f"--- Simple Broadcasting (Array + Scalar) ---")
print(f"Result of [1, 2, 3] + 5: {result}")
print("-" * 30)


# =======================================
# 2. THE RULES OF BROADCASTING
# =======================================
# Two dimensions are compatible when:
# 1. They are equal, OR
# 2. One of them is 1.
#
# If these conditions are not met, a `ValueError: operands could not be broadcast together` is raised.
#
# When comparing array shapes, NumPy works from right to left.
#
# Let's see this in action:
# A: (4, 3)     # A 4x3 matrix
# B: (   3)     # A 1x3 vector
#
# 1. Compare rightmost dimensions: 3 and 3. They are equal. OK.
# 2. Compare next dimensions: 4 and (no dimension). NumPy "stretches" B to match A.
# Resulting shape: (4, 3)


# =======================================
# 3. BROADCASTING EXAMPLES
# =======================================
print("--- Broadcasting Examples ---")

# --- Example 1: Adding a 1-D array to a 2-D array ---
# This is a very common operation
matrix = np.ones((3, 3))  # A 3x3 matrix of all 1s
row_vector = np.array([1, 2, 3])

print("Original matrix:\n", matrix)
print("Original row vector:\n", row_vector)

# The shape of `matrix` is (3, 3). The shape of `row_vector` is (3, ).
# Broadcasting effectively stretches row vector into a (3, 3) matrix:
# [[1, 2, 3],
#  [1, 2, 3],
#  [1, 2, 3]]
# ...and then adds it to the original matrix.
result_matrix = matrix + row_vector
print("\nResult of matrix + row_vector:\n", result_matrix)


# --- Example 2: Adding a column vector to a 2-D array ---
# To add a column, we must give it a shape of (n, 1)
column_vector = np.array([[10], [20], [30]])  # Shape is (3, 1)

print("\nOriginal matrix:\n", matrix)
print("Original column vector (shape 3x1):\n", column_vector)

# Here, `column_vector` is stretched horizontally to match the matrix's shape.
result_matrix_2 = matrix + column_vector
print("\nResult of matrix + column_vector:\n", result_matrix_2)


# --- Example 3: An incompatible shape ---
incompatible_vector = np.array([1, 2])  # Shape is (2,)
try:
    # matrix (3, 3) + incompatible_vector (2,)
    # Comparing rightmost dimensions: 3 vs 2. They are not equal, and neither is 1.
    # This will fail.
    result_matrix_3 = matrix + incompatible_vector
    print(result_matrix_3)
except ValueError as e:
    print(f"\nTrying to add a (3,3) and a (2,) array gives a ValueError:\n{e}")

print("-" * 30)


# =======================================
# 4. PRACTICAL APPLICATION: DATA NORMALIZATION
# =======================================
# - Broadcasting is frequently used in data science and machine learning.
# - A common task is "centering" data by subtracting the mean of each feature (column).

# Create a sample data matrix (4 samples, 3 features)
np.random.seed(0)
data = np.random.randint(0, 20, size=(4, 3))

print("--- Practical Example: Centering Data ---")
print("Original data:\n", data)

# Calculate the mean of each feature (column)
# `axis=0` means calculate the mean down the columns
# The result is a 1-D array with shape (3,).
feature_means = data.mean(axis=0)
print(f"\nMean of each feature (column): {feature_means}")
print(f"Shape of means vector: {feature_means.shape}")

# Subtract the means from the data.
# This works because of broadcasting!
# data (4, 3) - feature_means (3, ) -> broadcast to (4, 3)
centered_data = data - feature_means

print("\nCentered data (data - means):\n", centered_data)

# We can verify the new means are very close to zero
print(f"\nNew means of centered data: {centered_data.mean(axis=0).round(2)}")


# --- End of File ---
