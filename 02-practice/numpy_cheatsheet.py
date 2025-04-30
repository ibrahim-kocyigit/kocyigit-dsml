import numpy as np

# ----------------------- CREATING ARRAYS ----------------------- #
a = np.array([1, 2, 3])
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)

# Initial Placeholders
np.zeros((3, 4))  # Create a 3-by-4 zero-matrix
np.ones((2, 3, 4), dtype=np.int16)
d = np.arange(10, 25, 5)  # Create an array of evenly spaced values (step value)
e = np.linspace(0, 2, 9)  # Create an array of evenly spaced values (number of samples)
f = np.eye(2)  # Create a 2x2 identity matrix
np.random.random((2, 2))  # Create a 2x2 array with random values
np.empty((3, 2))  # Create a 3x2 empty array

# ----------------------------- I/O ----------------------------- #
# Saving & Loading on Disk
np.save("my_array", a)  # Save an array to a binary file in NumPy .npy format.
np.savez(
    "array.npz", a, b
)  # Saves several arrays into a single file in uncompressed .npz format.
np.load(
    "my_array.npy"
)  # Loads arrays or pickled objects from .npy, .npz or pickled files.

# ----------------- Saving & Loading Text Files ----------------- #
np.loadtxt("myfile.txt")  # Load data from a text file.
np.genfromtxt(
    "my_file.csv", delimiter=","
)  # Load data from a text file, with missing values handled as specified.
np.savetxt("myarray.txt", a, delimiter=" ")  # Save an array to a text file.
