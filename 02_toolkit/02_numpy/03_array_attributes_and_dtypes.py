import numpy as np

# =======================================
# 1. INTRODUCTION TO ARRAY ATTRIBUTES
# =======================================
# - Once you have created a NumPy array, it's essential to know how to inspect its properties.
# - These attributes describe the array's structure, size, and data type.
# - We will create a sample array to use for our inspection.

# A 3x4 array (3 rows, 4 columns)
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("--- Sample 2D Array ---")
print(array_2d)
print("-" * 30)


# =======================================
# 2. FUNDAMENTAL ARRAY ATTRIBUTES
# =======================================
# - These attributes provide key information about the array's dimensions and size.

# --- `.ndim`: Number of Dimensions ---
# - Returns the number of axes (dimensions) of the array.
# - A vector is 1-D, a matrix is 2-D, etc.
print(f"Number of dimensions (.ndim): {array_2d.ndim}")

# --- `.shape`: Shape of the Array ---
# - Returns a tuple representing the size of the array in each dimension.
# - For a 2-D array, it's (number_of_rows, number_of_columns).
print(f"Shape of the array (.shape): {array_2d.shape}")

# --- `.size`: Total Number of Elements ---
# - Returns the total number of elements in the array.
# - This is the product of the shape tuple's elements (e.g., 3 * 4 = 12).
print(f"Total size of the array (.size): {array_2d.size}")
print("-" * 30)


# =======================================
# 3. UNDERSTANDING DATA TYPES (`dtype`)
# =======================================
# - Unlike Python lists, all elements in a NumPy array must have the SAME data type.
# - The `.dtype` attribute tells you what this data type is.
# - NumPy usually infers the data type upon creation.

# --- Type Inference ---
# An array of integers
int_array = np.array([1, 2, 3])

# If even one number is a float, the entire array becomes float to accommodate it.
float_array = np.array([1.0, 2, 3])

print("--- Data Types (dtype) ---")
print(f"Data type of our sample 2D array: {array_2d.dtype}")  # e.g., int32 or int64
print(f"Data type of int_array: {int_array.dtype}")
print(f"Data type of float_array: {float_array.dtype}")  # e.g., float64
print("-" * 30)


# =======================================
# 4. SPECIFYING AND CHANGING `dtype`
# =======================================
# - You can explicitly set the data type on creation or change it later.

# --- Specifying `dtype` on Creation ---
# Create an array and specify that its elements should be 64-bit floats.
specific_dtype_array = np.array([1, 2, 3], dtype=np.float64)
print("--- Specifying and Changing dtypes ---")
print(f"Array created with dtype=np.float64: {specific_dtype_array}")
print(f"Its dtype is: {specific_dtype_array.dtype}")


# --- Changing `dtype` with `.astype()` ---
# - The `.astype()` method creates a NEW array with the specified data type.
# - It does not modify the original array.
original_array = np.array([0, 1.2, 2.7, 3.5])
print(f"\nOriginal float array: {original_array}")

# Convert the float array to an integer array
# Note that the decimal part is TRUNCATED (not rounded).
int_copy = original_array.astype(np.int32)
print(f"Array converted to int32: {int_copy}")

# Convert an integer array to a boolean array
# 0 becomes False, all non-zero numbers become True.
bool_copy = int_copy.astype(np.bool_)
print(f"Array converted to bool: {bool_copy}")
print("-" * 30)


# =======================================
# 5. MEMORY CONSIDERATIONS
# =======================================
# - Choosing the right `dtype` can save a lot of memory, which is critical for large datasets.
# - For example, `int64` uses 8 bytes per element, while `int8` uses only 1 byte.
# - If you know your data will not exceed a certain range (e.g., 0-255), you can
#   use a smaller data type to be more memory-efficient.

large_array_64 = np.ones(1_000_000, dtype=np.float64)  # 1 million 64-bit floats
large_array_32 = np.ones(1_000_000, dtype=np.float32)  # 1 million 32-bit floats

# .nbytes shows the total bytes consumed by the array's data.
print("--- Memory Usage ---")
print(f"Memory of float64 array: {large_array_64.nbytes / 1e6} MB")  # Approx 8 MB
print(f"Memory of float32 array: {large_array_32.nbytes / 1e6} MB")  # Approx 4 MB

# --- End of File ---
