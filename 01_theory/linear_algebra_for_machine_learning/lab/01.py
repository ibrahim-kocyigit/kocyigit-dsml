# Step 1: Import NumPy
# Import the NumPy library here.

import numpy as np

# Step 2: Define Scalars
# Define two scalars, a and b, with values 5 and 3, respectively.

a = 5
b = 3

# Step 3: Create Vectors
# Create two vectors, u and v, each with 3 elements:
# u = [1, 2, 3]
# v = [4, 5, 6]

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

# Step 4: Vector Addition
# Add the two vectors u and v element-wise.

vector_sum = u + v
print(vector_sum)

# Step 5: Scalar Multiplication
# Multiply the vector u by the scalar a.

vector_mult = a * u
print(vector_mult)

# Step 6: Create Matrices
# Create two matrices, A and B, with the following values:
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Step 7: Matrix Addition
# Add the two matrices A and B element-wise.

matrix_add = A + B
print(matrix_add)

# Step 8: Scalar Multiplication of Matrices
# Multiply the matrix A by the scalar b.

matrix_mult = b * A
print(matrix_mult)

# Step 9: Real-World Example - Feature Scaling
# Create a dataset of house features with the following values:
# Size (in square meters): [150, 120, 200]
# Number of bedrooms: [3, 2, 4]
# Age (in years): [10, 20, 5]

X = np.array([[150, 3, 10], [120, 2, 20], [200, 4, 5]], dtype=float)
print(X)

# Step 10: Scale the Size and Age Features
# Scale the Size and Age features to the range [0, 1] using the formula:
# x_scaled = (x - x_min) / (x_max - x_min)

size_min = X[:, 0].min()
size_max = X[:, 0].max()

size_scaled = (X[:, 0] - size_min) / (size_max - size_min)
X[:, 0] = size_scaled

age_min = X[:, 2].min()
age_max = X[:, 2].max()

age_scaled = (X[:, 2] - age_min) / (age_max - age_min)
X[:, 2] = age_scaled

print(X)

# Bonus: Write a function for scaling


def scale_feature(X: np.ndarray, column: int) -> np.ndarray:
    """
    Scales the specified column of the dataset X to the range [0, 1].
    """

    x_min = X[:, column].min()
    x_max = X[:, column].max()
    X[:, column] = (X[:, column] - x_min) / (x_max - x_min)

    return X


X = np.array([[150, 3, 10], [120, 2, 20], [200, 4, 5]], dtype=float)
print(X)

X_scaled = scale_feature(X, 0)
X_scaled = scale_feature(X_scaled, 2)
