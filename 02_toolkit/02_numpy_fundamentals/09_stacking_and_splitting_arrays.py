import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Introduction
# 2. Stacking Arrays (Joining)
# 3. Splitting Arrays


# =======================================
# 1. INTRODUCTION
# =======================================
# - In data analysis, it's common to combine multiple datasets or
#   split a single dataset into parts (e.g., for training and testing)
# - NumPy provides several straightforward functions for stacking (joining)
#   and splitting arrays.

# --- Create two sample arrays to work with ---
np.random.seed(42)
arr1 = np.random.randint(10, size=(2, 3))  # A 2x3 array
arr2 = np.random.randint(10, size=(2, 3))  # Another 2x3 array

print("--- Sample Arrays ---")
print("Array 1:\n", arr1)
print("\nArray 2:\n", arr2)
print("-" * 30)


# =======================================
# 2. STACKING ARRAYS (JOINING)
# =======================================
# - Combining multiple arrays into a single, larger one.


# --- `np.vstack()` (Vertical Stack) ---
# - Stacks arrays on top of each other (row-wise).
# - The arrays must have the same number of columns.
v_stacked = np.vstack((arr1, arr2))

print("--- Stacking Arrays ---")
print("Vertically stacked (vstack):\n", v_stacked)
print("Shape of vstacked array:", v_stacked.shape)  # (4, 3)


# --- `np.hstack()` (Horizontal Stack) ---
# - Stacks arrays next to each other (column-wise).
# - The arrays must have the same number of rows.
h_stacked = np.hstack((arr1, arr2))
print("\nHorizontally stacked (hstack):\n", h_stacked)
print("Shape of hstacked array:", h_stacked.shape)  # (2, 6)


# --- `np.concatenate() (The General Method)` ---
# - `vstack` and `hstack` are just convenient wrappers around `concatenate`.
# - The `axis` parameter controls the direction of the join:
#   - `axis=0`: Joins along the rows (like vstack).
#   - `axis=1`: Joins along the columns (like hstack).
concat_axis0 = np.concatenate((arr1, arr2), axis=0)
print("\nConcatenate with axis=0 (same as vstack):\n", concat_axis0)

concat_axis1 = np.concatenate((arr1, arr2), axis=1)
print("\nConcatenate with axis=1 (same as hstack):\n", concat_axis1)
print("-" * 30)


# =======================================
# 3. SPLITTING ARRAYS
# =======================================
# - Breaking one large array into several smaller sub-arrays.

# --- Create a larger array to split ---
large_arr = np.arange(24).reshape(6, 4)  # A 6x4 array

print("--- Splitting Arrays ---")
print("Large array to be split (6x4):\n", large_arr)


# --- `np.vsplit()` (Vertical Split) ---
# - Splits an array into multiple sub-arrays vertically (row-wise).

# Split into 3 equal sub-arrays:
v_split_equal = np.vsplit(large_arr, 3)  # returns a list of arrays
print("\nVertically split into 3 equal arrays:")
for arr in v_split_equal:
    print(f"{arr}\n---")

# Split at specific rows.
# To split at rows at indices 1 and 3, use `[1, 3]`. This creates 3 sub-array:
v_split_unequal = np.vsplit(large_arr, [1, 3])
print("Vertically split at rows 1 and 3:")
for arr in v_split_unequal:
    print(arr, "\n--")


# --- `np.hsplit()` (Horizontal Split) ---
# - Splits an array horizontally (column-wise).

# Split into 2 equal sub-arrays:
h_split_equal = np.hsplit(large_arr, 2)
print("Horizontally split into 2 equal arrays:")
for arr in h_split_equal:
    print(arr, "\n--")


# --- `np.array_split()` (The General Method) ---
# - `vsplit` and `hsplit` require the split to result in equal-sized arrays.
# - `array_split` is more flexible and does NOT require equal splits.
uneven_arr = np.arange(7)
print(f"\nSplitting an uneven array: {uneven_arr}")

uneven_split = np.array_split(uneven_arr, 3)  # Split a 7-element array into 3 parts.
print("Result of `array_split`:")
for arr in uneven_split:
    print(arr)


# --- End of File ---
