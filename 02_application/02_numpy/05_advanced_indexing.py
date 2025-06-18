import numpy as np

# =======================================
# 1. INTRODUCTION TO ADVANCED INDEXING
# =======================================
# - Advanced indexing goes beyond simple integers and slices.
# - It allows us to select elements based on complex conditions (boolean indexing)
#   or specific lists of indices (fancy indexing).
# - IMPORTANT: Unlike basic slicing which creates a view, advanced indexing
#   always returns a *copy* of the data. Modifying the new array will not
#   affect the original.

# Create a sample array to work with
# seed for reproducibility
np.random.seed(42)
arr = np.random.randint(0, 50, size=(4, 5))  # 4x5 array of random ints from 0-49

print("--- Original Sample Array ---")
print(arr)
print("-" * 30)


# =======================================
# 2. BOOLEAN INDEXING (MASKING)
# =======================================
# - This is a very powerful technique for filtering data.
# - You use a boolean array (a "mask") to select elements from another array.

print("--- Boolean Indexing ---")
# --- Step 1: Create a boolean condition ---
# This comparison is done element-wise and returns a boolean array of the same shape.
is_greater_than_20 = arr > 20

print("The boolean mask (arr > 20):\n", is_greater_than_20)

# --- Step 2: Use the mask to index the original array ---
# This selects only the elements where the mask is True.
print("\nElements greater than 20:\n", arr[is_greater_than_20])


# --- Combining boolean conditions ---
# Use bitwise operators `&` (and), `|` (or), and `~` (not).
# Note: Standard Python `and`, `or` do not work for element-wise comparisons.
print("\nElements between 10 and 30:")
between_10_and_30 = arr[(arr > 10) & (arr < 30)]
print(between_10_and_30)


# --- Using boolean indexing to modify values ---
# This is a very common and powerful pattern.
# Let's replace all odd numbers with -1
arr_copy = arr.copy()  # Work on a copy
arr_copy[arr_copy % 2 != 0] = -1  # Replace where condition is True
print("\nArray with odd numbers replaced by -1:\n", arr_copy)
print("-" * 30)


# =======================================
# 3. FANCY INDEXING (INTEGER ARRAY INDEXING)
# =======================================
# - Using lists or arrays of integers to select data.

# --- Fancy Indexing in 1-D ---
arr_1d = np.arange(10, 20)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
indices_to_get = [1, 4, 7, 8]
print("--- Fancy Indexing ---")
print(f"Original 1-D array: {arr_1d}")
print(f"Selecting elements at indices {indices_to_get}: {arr_1d[indices_to_get]}")


# --- Fancy Indexing in 2-D ---
# Create a clear 4x4 array for this example
arr_2d = np.arange(16).reshape(4, 4)
print("\nOriginal 2-D array:\n", arr_2d)

# --- Selecting specific rows ---
# Get rows with index 0 and 3
selected_rows = arr_2d[[0, 3]]
print("\nSelecting rows 0 and 3:\n", selected_rows)

# --- Selecting specific elements by coordinates ---
# To select elements at (row, col) pairs, pass a tuple of two lists/arrays:
# ([row_indices], [col_indices])
# Let's get elements at (0, 1), (2, 3), and (3, 0)
selected_elements = arr_2d[([0, 2, 3]), ([1, 3, 0])]
print("\nSelecting elements at (0,1), (2,3), and (3,0):", selected_elements)
print("-" * 30)


# =======================================
# 4. REMINDER: ADVANCED INDEXING CREATES COPIES
# =======================================
# - Remember that boolean and fancy indexing return a copy of the data, not a view.

print("--- View vs. Copy Reminder ---")
print("Original array:\n", arr)

# Get a new array using a boolean mask
bool_selection = arr[arr > 30]
print(f"\nBoolean selection: {bool_selection}")

# Modify the first element of the new array
bool_selection[0] = 999
print(f"Modified selection: {bool_selection}")

# The original array remains unchanged
print("Original array after modifying the copy:\n", arr)
