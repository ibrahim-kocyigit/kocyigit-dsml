import numpy as np

# ----------- Creating Arrays ----------- #
a = np.array([1, 2, 3])
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)

# Initial Placeholders
np.zeros((3, 4))  # creates a 3-by-4 zero-matrix
np.ones((2, 3, 4), dtype=np.int16)
d = np.arange(10, 25, 5)  # creates an array of evenly spaced values (step value)
e = np.linspace(0, 2, 9)  # creates an array of evenly spaced values (number of samples)
f = np.eye(2)  # creates a 2x2 identity matrix
np.random.random((2, 2))  # creates a 2x2 array with random values
np.empty((3, 2))  # creates a 3x2 empty array

# ----------- I/O ----------- #
# Saving & Loading on Disk
np.save("my_array", a)  # saves an array to a binary file in NumPy .npy format.
np.savez(
    "array.npz", a, b
)  # saves several arrays into a single file in uncompressed .npz format.
np.load(
    "my_array.npy"
)  # loads arrays or pickled objects from .npy, .npz or pickled files.
