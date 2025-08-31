import numpy as np
import os

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1.


# =======================================
# 1. INTRODUCTION TO FILE I/O IN NUMPY
# =======================================
# - It's crucial to be able to save your work—arrays, results of computations, etc.—to disk.
# - This allows you to load them back later without having to re-run your code.

# --- Setup a folder for our saved files ---
FOLDER_NAME = "numpy_saved_files"
os.makedirs(FOLDER_NAME, exist_ok=True)


# =======================================
# 2. BINARY FORMAT: `.npy` AND `.npz`
# =======================================
# ... (rest of the comments are the same)

# --- Create a sample array to save ---
arr_to_save = np.arange(24).reshape(4, 6)
print("--- Binary Format (.npy) ---")
print("Original array to save:\n", arr_to_save)

# --- Saving a SINGLE array with `np.save()` ---
# Now we use our new, absolute path
file_path_npy = os.path.join(FOLDER_NAME, "single_array.npy")
np.save(file_path_npy, arr_to_save)
print(f"\nArray saved to '{file_path_npy}'")

# --- Loading an array with `np.load()` ---
loaded_array = np.load(file_path_npy)
print("\nLoaded array from .npy file:\n", loaded_array)
print(
    f"Are original and loaded arrays equal? {np.array_equal(arr_to_save, loaded_array)}"
)


# --- Saving MULTIPLE arrays with `np.savez()` ---
arr_a = np.array([1, 2, 3])
arr_b = np.array([[4, 5], [6, 7]])
file_path_npz = os.path.join(FOLDER_NAME, "multiple_arrays.npz")
np.savez(file_path_npz, vector=arr_a, matrix=arr_b)
print(f"\nMultiple arrays saved to '{file_path_npz}'")

# --- Loading from a .npz file ---
loaded_archive = np.load(file_path_npz)
print("\nLoaded arrays from .npz archive:")
print("Vector 'vector':", loaded_archive["vector"])
print("Matrix 'matrix':\n", loaded_archive["matrix"])
print("-" * 30)


# =======================================
# 3. TEXT FORMAT: `.csv` AND `.txt`
# =======================================
# ... (rest of the comments are the same)

# --- Create a sample array to save as text ---
arr_to_save_text = np.arange(0.0, 5.0, 0.5).reshape(2, 5)
print("--- Text Format (.csv) ---")
print("Original array to save as text:\n", arr_to_save_text)

# --- Saving with `np.savetxt()` ---
file_path_csv = os.path.join(FOLDER_NAME, "my_data.csv")
np.savetxt(
    file_path_csv,
    arr_to_save_text,
    fmt="%.2f",
    delimiter=",",
    header="col1,col2,col3,col4,col5",
)
print(f"\nArray saved to '{file_path_csv}'")


# --- Loading with `np.loadtxt()` ---
loaded_from_text = np.loadtxt(file_path_csv, delimiter=",", skiprows=1)
print("\nLoaded array from .csv file:\n", loaded_from_text)
print("-" * 30)

# --- End of File ---
