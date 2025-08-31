import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Introduction to Linear Algebra
# 2. Dot Product and Matrix Multiplication
# 3. Matrix Properties & Operations (`np.linalg`)
# 4. Solving Systems of Linear Equations


# =======================================
# 1. INTRODUCTION TO LINEAR ALGEBRA
# =======================================
# - Linear algebra is the branch of mathematics concerning vector spaces and linear mappings.
# - It is a fundamental building block for many data science and machine learning algorithms.
# - NumPy provides a powerful and convenient environment for these operations, primarily
#   through the `np.linalg` submodule.

# --- Create two sample matrices to work with ---
np.random.seed(0)
A = np.random.randint(0, 10, size=(2, 3))  # A 2x3 matrix
B = np.random.randint(0, 10, size=(3, 2))  # A 3x2 matrix

print("--- Sample Matrices ---")
print("Matrix A (2x3):\n", A)
print("\nMatrix B (3x2):\n", B)
print("-" * 30)


# =======================================
# 2. DOT PRODUCT & MATRIX MULTIPLICATION
# =======================================

# --- Dot Product of two 1-D arrays (vectors) ---
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
# Dot product = (1*4) + (2*5) + (3*6) = 4 + 10 + 18 = 32
dot_product = np.dot(v1, v2)
print("--- Dot Product & Matrix Multiplication ---")
print(f"Dot product of {v1} and {v2} is: {dot_product}")


# --- Matrix Multiplication of two 2-D arrays (matrices) ---
# - The number of columns in the first matrix must equal the number of rows in the second.
# - Shape rule: (m, n) @ (n, p) -> (m, p)
# - In our case: A (2, 3) @ B (3, 2) -> (2, 2)

# The `@` operator is the modern, preferred syntax for matrix multiplication.
matrix_product = A @ B
print("\nMatrix product of A @ B (2x2):\n", matrix_product)

# `np.dot()` also works for matrix multiplication on 2-D arrays.
matrix_product_dot = np.dot(A, B)
print("\nResult using np.dot(A, B) is the same:\n", matrix_product_dot)
print("-" * 30)


# =======================================
# 3. MATRIX PROPERTIES & OPERATIONS (`np.linalg`)
# =======================================
# - The `np.linalg` submodule contains a host of linear algebra functions.

# Create a square matrix for these examples
C = np.array([[1, 2], [3, 4]])

print("--- Matrix Properties (using a square matrix) ---")
print("Matrix C (2x2):\n", C)

# --- Transpose ---
# Swaps rows and columns.
print("\nTranspose of C (.T):\n", C.T)

# --- Determinant ---
# A scalar value that provides important information about the matrix.
# If the determinant is 0, the matrix is "singular" and has no inverse.
det_C = np.linalg.det(C)
print(f"\nDeterminant of C: {det_C:.1f}")  # 1*4 - 2*3 = -2.0

# --- Inverse ---
# The inverse of C is a matrix C_inv such that C @ C_inv = Identity Matrix.
# Only non-singular square matrices have an inverse.
inv_C = np.linalg.inv(C)
print("\nInverse of C:\n", inv_C)

# --- Verification: C @ C_inv should be the identity matrix ---
# Due to floating point inaccuracies, the result is very close to, but not exactly, identity.
identity = np.eye(2)
print("\nC @ C_inv (should be close to identity):\n", (C @ inv_C).round(2))
print("Identity matrix:\n", identity)
print("-" * 30)


# =======================================
# 4. SOLVING SYSTEMS OF LINEAR EQUATIONS
# =======================================
# - A very common application of linear algebra.
# - We can solve a system of equations in the form `Ax = b`, where:
#   - `A` is the matrix of coefficients.
#   - `x` is the vector of unknown variables.
#   - `b` is the vector of constants.

# Consider the system:
# 2x + 3y = 8
# 4x + 1y = 6

# Coefficient matrix A
A_system = np.array([[2, 3], [4, 1]])

# Constant vector b
b_system = np.array([8, 6])

print("--- Solving a System of Linear Equations ---")
print("System: Ax = b")
print("Matrix A:\n", A_system)
print("Vector b:\n", b_system)

# The `np.linalg.solve()` function is the preferred way to solve this.
# It's faster and more numerically stable than calculating the inverse yourself.
x = np.linalg.solve(A_system, b_system)  # Returns the solution vector [x, y]

print(f"\nSolution vector x (values for x and y): {x}")
print(f"Solution: x = {x[0]:.1f}, y = {x[1]:.1f}")

# --- Verification ---
# Check if A @ x equals b
print(f"Verification (A @ x): {A_system @ x}")  # Should be [8., 6.]


# --- End of File ---
