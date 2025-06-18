import numpy as np
import os

# =======================================
# 1. INTRODUCTION TO FILE I/O IN NUMPY
# =======================================
# - It's crucial to be able to save your work—arrays, results of computations, etc.—to disk.
# - This allows you to load them back later without having to re-run your code.
# - NumPy offers two main ways to do this:
#   1. Binary Format (.npy, .npz): Fast, efficient, and preserves all array info
#      (shape, dtype). Ideal for working within the NumPy/Python ecosystem.
#   2. Text Format (.csv, .txt): Human-readable and widely compatible with other
#      software (like Excel, R), but less efficient and can lose precision.

# --- Setup a folder for our saved files ---
SAVE_FOLDER = "numpy_saved_files"
os.makedirs(SAVE_FOLDER, exist_ok=True)


# =======================================
# 2. BINARY FORMAT: `.npy` AND `.npz`
# =======================================
# - This is the standard and most efficient way to save NumPy data.

# --- Create a sample array to save ---
arr_to_save = np.arange(24).reshape(4, 6)
print("--- Binary Format (.npy) ---")
print("Original array to save:\n", arr_to_save)

# --- Saving a SINGLE array with `np.save()` ---
# The .npy extension is automatically added if not provided.
file_path_npy = os.path.join(SAVE_FOLDER, "single_array.npy")
np.save(file_path_npy, arr_to_save)
print(f"\nArray saved to '{file_path_npy}'")

# --- Loading an array with `np.load()` ---
loaded_array = np.load(file_path_npy)
print("\nLoaded array from .npy file:\n", loaded_array)

# --- Verification ---
print(
    f"Are original and loaded arrays equal? {np.array_equal(arr_to_save, loaded_array)}"
)


# --- Saving MULTIPLE arrays with `np.savez()` ---
# - Saves several arrays into a single, uncompressed `.npz` archive file.
# - You pass the arrays as keyword arguments, which become the names for retrieval.
arr_a = np.array([1, 2, 3])
arr_b = np.array([[4, 5], [6, 7]])
file_path_npz = os.path.join(SAVE_FOLDER, "multiple_arrays.npz")
np.savez(file_path_npz, vector=arr_a, matrix=arr_b)
print(f"\nMultiple arrays saved to '{file_path_npz}'")

# --- Loading from a .npz file ---
# The loaded object acts like a dictionary.
loaded_archive = np.load(file_path_npz)
print("\nLoaded arrays from .npz archive:")
print("Vector 'vector':", loaded_archive["vector"])
print("Matrix 'matrix':\n", loaded_archive["matrix"])
# Note: There is also `np.savez_compressed()` which saves in a compressed format.
print("-" * 30)


# =======================================
# 3. TEXT FORMAT: `.csv` AND `.txt`
# =======================================
# - Useful for exporting data to other programs or for human inspection.

# --- Create a sample array to save as text ---
arr_to_save_text = np.arange(0.0, 5.0, 0.5).reshape(2, 5)
print("--- Text Format (.csv) ---")
print("Original array to save as text:\n", arr_to_save_text)

# --- Saving with `np.savetxt()` ---
file_path_csv = os.path.join(SAVE_FOLDER, "my_data.csv")
# `fmt` controls the number format. '%.2f' is a float with 2 decimal places.
# `delimiter` sets the character to separate values.
# `header` writes a comment string at the top of the file.
np.savetxt(
    file_path_csv,
    arr_to_save_text,
    fmt="%.2f",
    delimiter=",",
    header="col1,col2,col3,col4,col5",
)
print(f"\nArray saved to '{file_path_csv}'")
# You can open this file in a text editor or Excel to see the result.


# --- Loading with `np.loadtxt()` ---
# - We must specify the same delimiter used for saving.
# - We use `skiprows=1` to ignore our header row.
loaded_from_text = np.loadtxt(file_path_csv, delimiter=",", skiprows=1)
print("\nLoaded array from .csv file:\n", loaded_from_text)
print("-" * 30)


# =======================================
# 4. CONCLUSION: WHICH FORMAT TO USE?
# =======================================
# - Use `.npy` / `.npz`:
#   - For speed, efficiency, and perfect data preservation (dtype, shape).
#   - When sharing data with other Python/NumPy users.
#   - For temporary storage or intermediate results.
#
# - Use `.txt` / `.csv`:
#   - For interoperability with non-Python programs (Excel, R, etc.).
#   - When you need the data to be human-readable.

print("This concludes the NumPy for Data Science curriculum!")

# --- End of File ---
