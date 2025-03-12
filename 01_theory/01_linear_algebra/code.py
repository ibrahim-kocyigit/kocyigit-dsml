import numpy as np

vector = np.array([1, 2, 3, 4, 5, 6], dtype=np.dtype(float))
ones_vector = np.ones(3)  # [1., 1., 1.]
zeros_vector = np.zeros(3)  # [0., 0., 0.]
rand_vector = np.random.rand(3)  # Sample: [0.76387422, 0.17717271, 0.90420804]

matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.dtype(float))
ones_matrix = np.ones((3, 3))
zeros_matrix = np.zeros((3, 3))
rand_matrix = np.random.rand(3, 3)
matrix_with_reshape = np.reshape(vector, (2, 3))

### Stacking
features = np.array([[1, 1], [2, 2]], dtype=np.dtype(float))
targets = np.array([3, 3], dtype=np.dtype(float))
augmented = np.hstack((features, targets.reshape(-1, 1)))
vertical_stacked = np.vstack((features, targets))

### Getting Info
matrix.ndim  # 2 --dimensions
matrix.shape  # (2, 3) --(rows, columns)
matrix.size  # 6 --(elements)


# -------- MATH OPERATIONS -------- #

vector_1 = np.array([2, 4, 6], dtype=np.dtype(float))
vector_2 = np.array([1, 3, 5], dtype=np.dtype(float))

addition = np.add(vector_1, vector_2)  # [ 3.,  7., 11.]
subtraction = np.subtract(vector_1, vector_2)  # [1., 1., 1.]
multiplication = np.multiply(vector_1, vector_2)  # [ 2., 12., 30.]
multiplication_with_scalar = np.multiply(vector_1, 3)  # [ 6., 12., 18.]
dot_product = np.dot(vector_1, vector_2)  # 44.0

matrix_1 = np.array([[4, 9, 9], [9, 1, 6], [9, 2, 3]])
matrix_2 = np.array([[2, 2], [5, 7], [4, 4]])

matrix_multiplication = np.dot(matrix_1, matrix_2)


# -------- SYSTEMS OF EQUATIONS -------- #
A = np.array([[-1, 3], [3, 2]], dtype=np.dtype(float))
b = np.array([7, 1], dtype=np.dtype(float))

# Determinant
determinant_A = np.linalg.det(A)

# Solution
x = np.linalg.solve(A, b)


# -------- LINEAR TRANSFORMATION AS MATRICES -------- #

# A is the transformation matrix, v the input vector, w the result of the transformation:


def L(v):
    A = np.array([[3, 0], [0, 0], [0, -2]])
    w = np.dot(A, v)
    return w


v = np.array([[3], [5]])
w = L(v)

# -------- COMMON TRANSFORMATION MATRICES (2D) -------- #
# For 3D transformations, use 3x3 matrices. For higher dimensions, extend the matrices accordingly.

### Scaling:
# A = np.array([[sx, 0], [0, sy]])  # Scales x by sx and y by sy
#   e.g., A = np.array([[2, 0], [0, 1]])  # Horizontal Scaling (Dilation) by 2
#   e.g., A = np.array([[1, 0], [0, 0.5]]) # Vertical Scaling (Contraction) by 0.5
#   e.g., A = np.array([[2, 0], [0, 2]]) # Uniform scaling by 2

### Reflection:
# A = np.array([[-1, 0], [0, 1]])  # Reflection about y-axis
# A = np.array([[1, 0], [0, -1]])  # Reflection about x-axis
# A = np.array([[-1, 0], [0, -1]]) # Reflection through the origin (rotation by 180 degrees)
# A = np.array([[0, 1], [1, 0]]) # Reflection about the line y=x
# A = np.array([[0, -1], [-1, 0]]) # Reflection about the line y=-x

### Rotation:
# A = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])  # Rotation counterclockwise by theta (in radians)
#   e.g., theta = np.pi / 2  # 90 degrees
#   e.g., theta = np.pi  # 180 degrees
#   e.g., theta = np.pi / 4 # 45 degrees
# Remember to convert degrees to radians for rotations using np.radians() if needed.

### Shearing:
# A = np.array([[1, shx], [0, 1]])  # Shear along x-axis by shx
# A = np.array([[1, 0], [shy, 1]])  # Shear along y-axis by shy
#   e.g., A = np.array([[1, 0.5], [0, 1]]) # Shear along x-axis by 0.5

### Projection:
# A = np.array([[1, 0], [0, 0]]) # Projection onto x-axis
# A = np.array([[0, 0], [0, 1]]) # Projection onto y-axis

### Identity:
# A = np.array([[1, 0], [0, 1]])  # No transformation (leaves the vector unchanged)
