import torch
import numpy as np

### WHAT IS A SCALAR?
# in base Python:
x = 25

# in PyTorch:
x_pt = torch.tensor(25)
x_float_pt = torch.tensor(25, dtype=torch.float)


# WHAT IS A VECTOR?
# in NumPy:
x = np.array([25, 2, 5])
x[0]  # Out: 25 // NumPy is zero-indexed
type(x[0])  # numpy.int64 // Not base Python

z = np.zeros(3)  # Out: array([0., 0., 0.])

# in PyTorch:
x_pt = torch.tensor([25, 2, 5])


### WHAT IS A VECTOR TRANSPOSITION?
x_T = x.T
print(x_T)  # Out: array([25,  2,  5]) // Becase x was 1 dimensional
x_T.shape  # Out: (3,2)

y = np.array([[25, 2, 5]])  # Nested, so 2D array
y_T = y.T
print(
    y_T
)  # Out: // Now it's a column vector, which is also a matrix with only one column
"""
[[25]
 [ 2]
 [ 5]]
"""
y_T.shape  # Out: (3, 1)

print(y_T.T)  # Out: [[25  2  5]]


### WHAT IS NORM OF A VECTOR?
x = np.array([25, 2, 5])
norm_x = (25**2 + 2**2 + 5**2) ** (1 / 2)  # Out: 25.573423705088842
norm_np_x = np.linalg.norm(x)  # Out: 25.573423705088842

### WHAT OTHER NORMS ARE THERE?
# L1 Norm:
l1_norm_x = np.abs(25) + np.abs(2) + np.abs(5)  # Out: 32

# Squared L2 Norm:
squared_l2_norm_x = 25**2 + 2**2 + 5**2  # Out: 654
print(x.T @ x)  # Out: 654 // @ is dot product. same as: np.dot(x.T, x)

# Max Norm
max_norm_x = np.max([np.abs(25), np.abs(2), np.abs(5)])  # Out: 25

### WHAT ARE ORTHONORMAL VECTORS?
i = np.array([1, 0])  # Standard basis vector i
j = np.array([0, 1])  # Standard basis vector j

print(i @ j)  # Out: 0 // Therefore i and j are orthonormal

### WHAT ARE MATRICES?

# In NumPy:
X = np.array([[25, 2], [5, 26], [3, 7]])
print(X)  # Out:
"""
array([[25,  2],
       [ 5, 26],
       [ 3,  7]])
"""

X.shape  # (3, 2) // 3 rows, 2 columns
X.size  # 6 // 3x2=6 elements in total
X[:, 0]  # Left column
X[0:2, 0:1]  # First column of the first 2 rows

# In PyTorch
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
X_pt[0:2, 0:1]

# WHAT ARE N-TENSORS?
images_pt = torch.zeros([32, 28, 28, 3])
