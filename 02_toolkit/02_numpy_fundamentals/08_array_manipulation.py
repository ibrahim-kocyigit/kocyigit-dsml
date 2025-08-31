import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Reshaping Arrays
# 2. Transposing Arrays
# 3. Flattening Arrays: `.ravel()` vs. `.flatten()`
# 4. Adding a New Axis / Dimension


# =======================================
# 1. RESHAPING ARRAYS
# =======================================
# - The most common manipulation task is changing the shape of an array.
# - The `.reshape()` method allows you to do this without changing the array's data.
# - The new shape must have the same total size as the original array.
#   (e.g., an array of size 12 can be reshaped to (3, 4), (4, 3), (2, 6), etc.)

# Start with a 1-D array of 12 elements
arr = np.arange(12)

print("--- Reshaping Arrays ---")
print("Original 1-D array (size 12):\n", arr)

# Reshape it to a 3x4 matrix
arr_3x4 = arr.reshape(3, 4)
print("\nReshaped to 3x4:\n", arr_3x4)

# Reshape it to a 4x3 matrix
arr_4x3 = arr.reshape(4, 3)
print("\nReshaped to 4x3:\n", arr_4x3)

# --- The `-1` trick for reshaping ---
# You can use -1 for one dimension, and NumPy will automatically calculate its size.
# Reshape to have two rows; NumPy calculates the number of columns needed.
arr_2_rows = arr.reshape(2, -1)
print("\nReshaped to (2, -1), resulting shape is:", arr_2_rows.shape)
print(arr_2_rows)
print("-" * 30)


# =======================================
# 2. TRANSPOSING ARRAYS
# =======================================
# - Transposing flips an array over its diagonal; it swaps rows and columns.
# - This is a special kind of reshape.
# - It's accessed using the `.T` attribute.

# Use the 3x4 array from the previous example
print("--- Transposing Arrays ---")
print("Original 3x4 array:\n", arr_3x4)
print("Original shape:", arr_3x4.shape)

# Transpose the array
transposed_arr = arr_3x4.T
print("\nTransposed array:\n", transposed_arr)
print("Transposed shape:", transposed_arr.shape)  # Shape is now (4, 3)
print("-" * 30)


# =======================================
# 3. FLATTENING ARRAYS: `.ravel()` vs `.flatten()`
# =======================================
# - "Flattening" an array means converting a multi-dimensional array into a 1-D array.
# - There are two main ways to do this, with one critical difference.
#
# - `.ravel()`: Returns a VIEW of the original array whenever possible.
#   It's generally faster and more memory-efficient.
#   Modifying the raveled array might change the original array.
#
# - `.flatten()`: ALWAYS returns a COPY of the array's data.
#   The new array is completely independent of the original.

print("--- Flattening Arrays: .ravel() vs .flatten() ---")
# Use the 3x4 array again
print("Original 3x4 array:\n", arr_3x4)

# --- Using .ravel() (a view) ---
raveled_view = arr_3x4.ravel()
print(f"\nRaveled array: {raveled_view}")
# Modify the view
raveled_view[0] = 99
print(f"Raveled array after modification: {raveled_view}")
print("Original array IS MODIFIED by the .ravel() view:\n", arr_3x4)

# Reset the original array for the next demo
arr_3x4[0, 0] = 0

# --- Using .flatten() (a copy) ---
flattened_copy = arr_3x4.flatten()
print(f"\nFlattened array: {flattened_copy}")
# Modify the copy
flattened_copy[0] = 100
print(f"Flattened array after modification: {flattened_copy}")
print("Original array is NOT MODIFIED by the .flatten() copy:\n", arr_3x4)
print("-" * 30)


# =======================================
# 4. ADDING A NEW AXIS / DIMENSION
# =======================================
# - Sometimes you need to add a "dummy" dimension to make an array compatible
#   for broadcasting or with a machine learning model's input shape.
# - The `np.newaxis` object is used for this.

print("--- Adding a New Axis ---")
# Start with a 1-D array
vec = np.array([1, 2, 3])
print(f"Original vector: {vec}")
print(f"Original shape: {vec.shape}")  # Shape is (3,)

# --- Convert to a column vector ---
# Use `np.newaxis` in the column's position
col_vec = vec[:, np.newaxis]
print(f"\nColumn vector:\n{col_vec}")
print(f"Column vector shape: {col_vec.shape}")  # Shape is now (3, 1)

# --- Convert to a row vector ---
# Use `np.newaxis` in the row's position
row_vec = vec[np.newaxis, :]
print(f"\nRow vector:\n{row_vec}")
print(f"Row vector shape: {row_vec.shape}")  # Shape is now (1, 3)


# --- End of File ---
