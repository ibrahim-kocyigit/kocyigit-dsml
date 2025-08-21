import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Creating Arrays from Python Lists
# 2. Intrinsic Array Creation (From Scratch)
# 3. Creating Arrays with Ranges
# 4. Creating Arrays with Random Data


# =======================================
# 1. CREATING ARRAYS FROM PYTHON LISTS
# =======================================
# - The most basic way to create an array is using `np.array()` on a Python list or tuple.

# --- 1-D Array (Vector) ---
list_1d = [1, 2, 3, 4]
array_1d = np.array(list_1d)

# --- 2-D Array (Matrix) ---
# Created from a list of lists. Note that inner lists must have the same length.
list_2d = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(list_2d)

print("--- Creating Arrays from Lists ---")
print("1-D Array:\n", array_1d)
print("\n2-D Array:\n", array_2d)
print("-" * 30)


# =======================================
# 2. INTRINSIC ARRAY CREATION (FROM SCRATCH)
# =======================================
# - NumPy provides functions to create arrays without needing to start with a Python list.
# - These are useful for creating arrays of a specific size and initial value.

# --- Create an array of all zeros ---
# The argument is a tuple specifying the shape (rows, columns).
zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns

# --- Create an array of all ones ---
ones_array = np.ones((3, 2))  # 3 rows, 2 columns

# --- Create an array filled with a specific value ---
full_array = np.full((2, 4), fill_value=7)  # 2x4 array filled with 7s

# --- Create an identity matrix ---
# An identity matrix has 1s on the diagonal and 0s elsewhere.
identity_matrix = np.eye(3)  # A 3x3 identity matrix.

print("--- Intrinsic Array Creation ---")
print("Zeros array (2x3):\n", zeros_array)
print("\nOnes array (3x2):\n", ones_array)
print("\nFull array (2x4 with 7s):\n", full_array)
print("\nIdentity matrix (3x3):\n", identity_matrix)
print("-" * 30)


# =======================================
# 3. CREATING ARRAYS WITH RANGES
# =======================================
# - Functions for creating arrays with sequences of numbers.

# --- `np.arange()` ---
# - Similar to Python's built-in `range()`, but returns a NumPy array.
# - Can use floating-point steps.
# - Syntax: `np.arange(start, stop, step)`
range_array = np.arange(
    0, 10, 2
)  # Start at 0, go up to (but not including) 10, in steps of 2

# --- `np.linspace()` ---
# - Creates an array with a specified number of points, evenly spaced
#   between a start and end value. The endpoint IS included.
# - Syntax: `np.linspace(start, stop, num_points)`
linspace_array = np.linspace(0, 1, 5)  # 5 points from 0 to 1 (inclusive)

print("--- Creating Arrays with Ranges ---")
print("`arange(0, 10, 2)`:\n", range_array)
print("\n`linspace(0, 1, 5)`:\n", linspace_array)
print("-" * 30)


# =======================================
# 4. CREATING ARRAYS WITH RANDOM DATA
# =======================================
# - The `np.random` submodule is crucial for simulations, modeling, and machine learning.

# --- Reproducibility with `np.random.seed()` ---
# Setting a "seed" ensures that the "random" numbers generated are the same
# every time the code runs. This is critical for reproducible results.
np.random.seed(42)

# --- `np.random.rand(rows, cols)` ---
# - Random values from a uniform distribution over [0, 1).
rand_array = np.random.rand(2, 3)  # A 2x3 array of random floats

# --- `np.random.randn(rows, cols)` ---
# - Random values from the standard normal ("Gaussian") distribution (mean 0, variance 1).
randn_array = np.random.randn(2, 3)  # A 2x3 array of random floats from normal dist.

# --- `np.random.randint(low, high, size)` ---
# - Random integers from `low` (inclusive) to `high` (exclusive).
randint_array = np.random.randint(
    0, 10, size=(3, 4)
)  # A 3x4 array of random ints from 0-9

print("--- Creating Random Arrays (with seed=42) ---")
print("`rand(2, 3)` (Uniform distribution):\n", rand_array)
print("\n`randn(2, 3)` (Normal distribution):\n", randn_array)
print("\n`randint(0, 10, size=(3, 4))`:\n", randint_array)


# --- End of File ---
