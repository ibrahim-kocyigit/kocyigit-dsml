# Lesson 1: Introduction to Linear Algebra

## 1. What is Linear Algebra?
Linear algebra is the branch of mathematics that deals with **vectors**, **matrices**, and **linear transformations**. It is foundational to machine learning and is used in:

- **Data Representation:** Data is often represented as vectors (for individual data points) or matrices (for datasets).
- **Transformations:** Linear algebra is used to rotate, scale, and project data.
- **Algorithms:** Techniques like Principal Component Analysis (PCA), Singular Value Decomposition (SVD), and neural networks rely heavily on linear algebra.

---

## 2. Scalars, Vectors, and Matrices

### Scalars
A **scalar** is a single number (e.g., 5, -3.2, π). Scalars are used to represent quantities like weights, biases, and learning rates in machine learning.

### Vectors
A **vector** is an ordered list of numbers. For example:

```
v = [1, 2, 3]
```

Vectors are used to represent data points, features, or model parameters. They are often denoted with lowercase bold letters (e.g., **v**).

### Matrices
A **matrix** is a 2D array of numbers. For example:

```
A = [[1, 2],
     [3, 4]]
```

Matrices are used to represent datasets, transformations, and weights in neural networks. They are often denoted with uppercase bold letters (e.g., **A**).

---

## 3. Basic Operations

### Vector Addition and Subtraction
Vectors of the same size can be added or subtracted element-wise:

```
u + v = [u₁ + v₁, u₂ + v₂, ..., uₙ + vₙ]
```

### Scalar Multiplication
A vector can be multiplied by a scalar, scaling each element:

```
c · v = [c · v₁, c · v₂, ..., c · vₙ]
```

### Matrix Addition and Subtraction
Matrices of the same size can be added or subtracted element-wise:

```
A + B = [[a₁₁ + b₁₁, a₁₂ + b₁₂],
         [a₂₁ + b₂₁, a₂₂ + b₂₂]]
```

### Scalar Multiplication of Matrices
A matrix can be multiplied by a scalar, scaling each element:

```
c · A = [[c · a₁₁, c · a₁₂],
         [c · a₂₁, c · a₂₂]]
```

---

## Hands-On Project: Basic Operations in Python

Let’s implement these concepts in Python using NumPy.

```python
import numpy as np

# Scalars
a = 5
b = 3

# Vectors
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

# Vector addition
vector_sum = u + v
print("Vector Addition:", vector_sum)

# Scalar multiplication
scalar_mult = a * u
print("Scalar Multiplication:", scalar_mult)

# Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
matrix_sum = A + B
print("Matrix Addition:\n", matrix_sum)

# Scalar multiplication of a matrix
matrix_scalar_mult = b * A
print("Scalar Multiplication of Matrix:\n", matrix_scalar_mult)
```

---

## Real-World Example: Data Representation

In machine learning, datasets are often represented as matrices. For example:

```python
# Example dataset
data = np.array([
    [1, 2, 3],  # Data point 1
    [4, 5, 6],  # Data point 2
    [7, 8, 9]   # Data point 3
])
print("Dataset:\n", data)
```

---

## Summary of Lesson 1
- **Linear algebra** is essential for machine learning.
- **Scalars**, **vectors**, and **matrices** are the building blocks of linear algebra.
- Scalars represent single values like weights and biases.
- Vectors represent data points or features.
- Matrices represent datasets or transformations.
- Basic operations include addition, subtraction, and scalar multiplication.
- These concepts are implemented in Python using NumPy.

---

## Next Steps
1. Practice the hands-on project to solidify your understanding.
2. Move on to **Lesson 2: Vector Operations**, where we’ll explore dot products, cross products, and vector norms.