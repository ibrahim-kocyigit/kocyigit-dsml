import numpy as np

# =======================================
# 1. INTRODUCTION TO AGGREGATIONS
# =======================================
# - Aggregation is the process of reducing an array to a single summary value
#   (e.g., the sum, mean, or standard deviation).
# - NumPy's aggregation functions are very fast and are a cornerstone of data analysis.

# Create a sample 2-D array for our examples
np.random.seed(0)
arr = np.random.randint(0, 20, size=(3, 5))  # A 3x5 array of random ints from 0-19

print("--- Sample Array ---")
print(arr)
print("-" * 30)


# =======================================
# 2. BASIC AGGREGATE FUNCTIONS
# =======================================
# - These functions can be called as methods on an array object (`arr.sum()`)
#   or as top-level NumPy functions (`np.sum(arr)`).
# - By default, they operate on the entire array.

print("--- Basic Aggregate Functions (on the entire array) ---")

# Sum of all elements
print(f"Sum of all elements: {arr.sum()}")

# Mean (average) of all elements
print(f"Mean of all elements: {arr.mean():.2f}")

# Standard deviation (a measure of spread)
print(f"Standard deviation: {arr.std():.2f}")

# Variance (the square of the standard deviation)
print(f"Variance: {arr.var():.2f}")

# Minimum and maximum values
print(f"Minimum value: {arr.min()}")
print(f"Maximum value: {arr.max()}")
print("-" * 30)


# =======================================
# 3. THE `axis` PARAMETER (THE KEY CONCEPT)
# =======================================
# - The `axis` parameter allows you to perform aggregations along a specific dimension.
# - For a 2-D array (a matrix):
#   - `axis=0`: Aggregates "down the columns". Collapses the rows.
#   - `axis=1`: Aggregates "across the rows". Collapses the columns.

print("--- Aggregations Along Axes ---")
print("Original array:\n", arr)

# --- Summing along axes ---
# Sum down the columns (axis=0) -> results in 1 value for each column
col_sums = arr.sum(axis=0)
print(f"\nSum of each column (axis=0): {col_sums}")
print(f"Shape of the result: {col_sums.shape}")

# Sum across the rows (axis=1) -> results in 1 value for each row
row_sums = arr.sum(axis=1)
print(f"\nSum of each row (axis=1): {row_sums}")
print(f"Shape of the result: {row_sums.shape}")


# --- Finding the max value along axes ---
col_max = arr.max(axis=0)
print(f"\nMax value in each column (axis=0): {col_max}")

row_max = arr.max(axis=1)
print(f"\nMax value in each row (axis=1): {row_max}")
print("-" * 30)


# =======================================
# 4. OTHER USEFUL STATISTICAL FUNCTIONS
# =======================================

# --- Cumulative Sum (`.cumsum()`) ---
# - Calculates the cumulative sum of the elements.
arr_1d = np.arange(5)
print("--- Other Useful Functions ---")
print(f"1-D array: {arr_1d}")
print(f"Cumulative sum of 1-D array: {arr_1d.cumsum()}")

# It also works along axes
print(f"\nCumulative sum down columns (axis=0):\n{arr.cumsum(axis=0)}")


# --- `argmin` and `argmax` ---
# - These find the *index* of the minimum or maximum element, not the value itself.
print(f"\nOriginal array:\n{arr}")
print(f"Index of the minimum value in the flattened array: {arr.argmin()}")
print(f"Index of the maximum value in each column (axis=0): {arr.argmax(axis=0)}")


# --- `np.percentile()` ---
# - Computes the q-th percentile of the data. This is a function, not a method.
# - The 50th percentile is the median.
print(
    f"\nThe 50th percentile (median) of the entire array is: {np.percentile(arr, 50)}"
)
print(f"The 90th percentile of the entire array is: {np.percentile(arr, 90)}")

# --- End of File ---
