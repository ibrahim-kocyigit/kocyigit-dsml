import numpy as np

# =======================================
# 1. WHAT IS VECTORIZATION?
# =======================================
# - Vectorization is the process of applying an operation to an entire array at once,
#   rather than element by element in a Python loop.
# - This is the core reason for NumPy's speed. The loops are executed in fast,
#   pre-compiled C code instead of slower, interpreted Python.
# - We saw a practical demo of this in the first lesson.


# =======================================
# 2. ELEMENT-WISE ARITHMETIC OPERATIONS
# =======================================
# - Standard arithmetic operators work element-wise on NumPy arrays.
# - The arrays must have the same shape or be "broadcastable" (topic of the next lesson).

# Create two sample arrays of the same shape
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[10, 20, 30], [40, 50, 60]])

print("--- Element-wise Arithmetic ---")
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

# --- Operations between two arrays ---
print("\nArray 1 + Array 2:\n", arr1 + arr2)
print("\nArray 1 * Array 2:\n", arr1 * arr2)


# --- Operations with a scalar (a single number) ---
# This is a simple form of broadcasting.
print("\nArray 1 * 3:\n", arr1 * 3)
print(
    "\n1 / Array 1 (as float):\n", 1 / arr1.astype(float)
)  # Convert to float to see fractions
print("\nArray 1 ** 2 (squared):\n", arr1**2)
print("-" * 30)


# =======================================
# 3. UNIVERSAL FUNCTIONS (UFUNCS)
# =======================================
# - A ufunc is a function that performs fast, element-wise operations on `ndarray` objects.
# - The arithmetic operators we just used are actually convenient wrappers for ufuncs.
#   (e.g., `+` is a shortcut for `np.add`).

arr = np.arange(1, 10).reshape(3, 3)
print("--- Universal Functions (ufuncs) ---")
print("Original array for ufuncs:\n", arr)

# --- Unary Ufuncs (operate on one array) ---
print("\nSquare root (`np.sqrt`):\n", np.sqrt(arr))
print("\nExponential e^x (`np.exp`):\n", np.exp(arr))
print("\nNatural logarithm (`np.log`):\n", np.log(arr))


# --- Binary Ufuncs (operate on two arrays) ---
# These are the explicit function calls for the operators we saw earlier
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 2, 6])
print(f"\nArray A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"Element-wise maximum (`np.maximum`): {np.maximum(arr_a, arr_b)}")
print(f"Element-wise addition (`np.add`): {np.add(arr_a, arr_b)}")
print("-" * 30)


# =======================================
# 4. CONDITIONAL LOGIC WITH `np.where()`
# =======================================
# - `np.where()` is the vectorized equivalent of a ternary expression (`x if condition else y`).
# - It's a powerful tool for creating a new array based on a condition.
# - Syntax: `np.where(condition, value_if_true, value_if_false)`

# Create a sample 3x3 array with random positive and negative numbers
np.random.seed(42)
data = np.random.randn(3, 3)

print("--- Conditional Logic with `np.where()` ---")
print("Original data:\n", data)

# Create a new array, replacing positive values with 1 and non-positive values with -1
# The condition `data > 0` produces a boolean array mask.
result = np.where(data > 0, 1, -1)
print("\nResult of `np.where(data > 0, 1, -1)`:\n", result)

# It can also be used to selectively choose values from two other arrays
arr_positives = np.full_like(data, 100)  # Array full of 100s
arr_negatives = np.full_like(data, -100)  # Array full of -100s
selective_result = np.where(data > 0, arr_positives, arr_negatives)
print("\nResult of selecting from two other arrays:\n", selective_result)
