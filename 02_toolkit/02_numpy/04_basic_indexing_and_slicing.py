import numpy as np

# =======================================
# 1. INDEXING AND SLICING 1-D ARRAYS
# =======================================
# - This works very similarly to Python lists.
# - Indexing: Access a single element using `arr[index]`.
# - Slicing: Access a range of elements using `arr[start:stop:step]`.

# Create a sample 1-D array
arr_1d = np.arange(10)  # An array from 0 to 9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("--- 1-D Array Indexing and Slicing ---")
print(f"Original 1-D array: {arr_1d}")

# --- Indexing ---
print(f"Element at index 3: {arr_1d[3]}")
print(f"Last element: {arr_1d[-1]}")

# --- Slicing ---
print(f"First 4 elements: {arr_1d[:4]}")
print(f"Elements from index 5 onwards: {arr_1d[5:]}")
print(f"Elements from index 2 to 6: {arr_1d[2:7]}")
print(f"Reversed array: {arr_1d[::-1]}")
print("-" * 30)


# =======================================
# 2. NUMPY SLICES ARE VIEWS, NOT COPIES
# =======================================
# - CRITICAL CONCEPT: Unlike Python lists, slices of NumPy arrays are "views"
#   into the original array's memory.
# - Modifying a slice will modify the original array.
# - This is a performance feature to avoid copying large amounts of data.
# - If you need a copy, use the `.copy()` method.

print("--- Slices are Views ---")
print(f"Original array before slicing: {arr_1d}")

# Create a slice of the first 5 elements
arr_slice = arr_1d[:5]
print(f"Slice of the array: {arr_slice}")

# Modify an element in the slice
print("\nModifying the first element of the slice to 99...")
arr_slice[0] = 99

print(f"Slice after modification: {arr_slice}")
print(f"ORIGINAL array is also modified: {arr_1d}")  # Note the change in the original

# --- To create a copy, use .copy() ---
arr_1d[0] = 0  # Reset the original array
arr_copy = arr_1d[:5].copy()
arr_copy[0] = 100
print("\n--- Slices as Copies (using .copy()) ---")
print(f"Original array: {arr_1d}")
print(f"Copy of slice after modification: {arr_copy}")
print(f"Original array is NOT modified this time.")
print("-" * 30)


# =======================================
# 3. INDEXING AND SLICING 2-D ARRAYS (MATRICES)
# =======================================
# - NumPy's real power shines with multi-dimensional arrays.
# - Use comma-separated indices: `arr[row, column]`.

# Create a sample 2-D array (3 rows, 4 columns)
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("--- 2-D Array Indexing and Slicing ---")
print("Original 2-D array:\n", arr_2d)

# --- Accessing a single element ---
# Get the element at row 1, column 2 (value is 7)
element = arr_2d[1, 2]
print(f"\nElement at [1, 2]: {element}")

# This is the preferred NumPy way. The chained `arr_2d[1][2]` also works but is less efficient.

# --- Slicing a single row or column ---
# Get the entire first row (index 0)
first_row = arr_2d[0, :]  # or more simply arr_2d[0]
print(f"First row: {first_row}")

# Get the entire third column (index 2)
third_col = arr_2d[:, 2]
print(f"Third column: {third_col}")


# --- Slicing a sub-matrix ---
# Get the top-right 2x2 sub-matrix
# Rows 0 and 1, columns 2 and 3
sub_matrix = arr_2d[:2, 2:]  # Rows 0-1, Columns 2-3
print("\nTop-right 2x2 sub-matrix:\n", sub_matrix)
print("-" * 30)


# =======================================
# 4. ASSIGNING VALUES WITH SLICING
# =======================================
# - You can use slicing to modify sections of an array.

# Create a 4x4 array of zeros
zeros = np.zeros((4, 4))
print("--- Assigning with Slicing ---")
print("Original zeros array:\n", zeros)

# Set a 2x2 sub-region to all 1s
zeros[1:3, 1:3] = 1
print("\nArray after setting a 2x2 sub-region to 1s:\n", zeros)

# Set an entire row using a 1-D array
zeros[0, :] = [5, 6, 7, 8]
print("\nArray after setting the first row:\n", zeros)

# --- End of File ---
