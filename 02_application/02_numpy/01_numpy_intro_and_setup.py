import time

# =======================================
# 1. WHAT IS NUMPY?
# =======================================
# - NumPy stands for "Numerical Python".
# - It is the fundamental package for scientific and numerical computing in Python.
# - The core of NumPy is its powerful N-dimensional array object, the `ndarray`.
# - It provides high-performance, grid-like data structures and tools for working with them.


# =======================================
# 2. INSTALLATION AND IMPORT CONVENTION
# =======================================
# - To install NumPy, run this command in your terminal:
#   `pip install numpy`
#
# - The universal community convention for importing NumPy is:
import numpy as np


# =======================================
# 3. WHY USE NUMPY? (PERFORMANCE & CONVENIENCE)
# =======================================
# - NumPy arrays are more efficient than Python lists in several key ways:
#   1. Performance: NumPy operations are implemented in C, making them much faster
#      than equivalent operations on Python lists, which require explicit loops.
#   2. Memory: NumPy arrays are more compact and use less memory because they
#      store data of a single type (e.g., all integers or all floats).
#   3. Convenience: NumPy allows for "vectorized" operations, where you can
#      perform an operation on an entire array at once, leading to cleaner code.

# --- Performance Demonstration: Python List vs. NumPy Array ---
# Let's compare squaring every number in a large sequence.

list_size = 10_000_000

# Python List method
print("--- Performance Comparison ---")
py_list = list(range(list_size))
start_time = time.perf_counter()
py_list_squared = [x**2 for x in py_list]
end_time = time.perf_counter()
py_time = end_time - start_time
print(f"Time taken with Python list: {py_time:.4f} seconds.")


# NumPy Array method
np_array = np.arange(list_size)
start_time = time.perf_counter()
np_array_squared = np_array**2  # This is a fast, vectorized operation
end_time = time.perf_counter()
np_time = end_time - start_time
print(f"Time taken with NumPy array: {np_time:.4f} seconds.")

# Compare the results
print(f"\nNumPy was approximately {py_time / np_time:.2f} times faster.")
print("-" * 30)


# =======================================
# 4. THE `ndarray` OBJECT
# =======================================
# - The `ndarray` is the heart of NumPy. We will explore it in detail in the next lesson.
# - For now, let's create a simple one from a Python list.

# A simple Python list
my_list = [1, 2, 3, 4, 5]

# Creating a NumPy array from the list
my_array = np.array(my_list)

print("--- The ndarray ---")
print(f"Python list: {my_list}")
print(f"NumPy array: {my_array}")

# Check the type
print(f"Type of my_list: {type(my_list)}")
print(f"Type of my_array: {type(my_array)}")  # Note the type is numpy.ndarray

# --- End of File ---
