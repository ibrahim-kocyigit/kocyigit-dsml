import numpy as np

np.info()  # Get help information for an array, function, class, or module.


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


# ----------------- SAVING & LOADING TEXT FILES ----------------- #
np.loadtxt("myfile.txt")  # Load data from a text file.
np.genfromtxt(
    "my_file.csv", delimiter=","
)  # Load data from a text file, with missing values handled as specified.
np.savetxt("myarray.txt", a, delimiter=" ")  # Save an array to a text file.


# -------------------- INSPECTING YOUR ARRAY -------------------- #
a.shape  # Array dimensions
len(a)  # Length of array
b.ndim  # Number of array dimensions
e.size  # Number of array elements
b.dtype  # Data type of array elements
b.dtype.name  # Name of data type
b.astype(int)  # Convert an array to a different type


# ------------------------- ARRAY MATHS ------------------------- #
g = a - b  # Subtraction
np.subtract(a, b)  # Subtraction
b + a  # Addition
np.add(b, a)  # Addition
a / b  # Division
np.divide(a, b)  # Division
a * b  # Multiplication
np.multiply(a, b)  # Multiplication
np.exp(b)  # Exponentiation
np.sqrt(b)  # Square root
np.sin(a)  # Print sines of an array
np.cos(b)  # Element-wise cosine
np.log(a)  # Element-wise natural logratihm
f.dot(g)  # Dot product
f @ g  # Dot product
np.dot(f, g)  # Dot product


# ------------------------- COMPARISON -------------------------- #
a == b  # Element-wise comparison. Returns array of bools.
a < 2  # Element-wise comparison. Returns array of bools.
np.array_equal(a, b)  # Array-wise comparison. Returns bool.


# --------------------- AGGREGATE FUNCTIONS --------------------- #
a.sum()  # Array-wise sum
a.min()  # Array-wise minimum value
b.max(axis=0)  # Maximum value of an array row
b.cumsum(axis=1)  # Cumulative sum of the elements as an array
