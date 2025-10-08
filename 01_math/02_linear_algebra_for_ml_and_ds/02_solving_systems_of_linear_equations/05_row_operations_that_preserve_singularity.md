# Row Operations That Preserve Singularity

Before we dive into the full process of row reduction, it's important to understand the fundamental manipulations we can perform on a matrix. These are called **row operations**, and they are the exact same operations we used to solve systems of linear equations, just applied to the rows of a matrix.

A critical property of these operations is that they **preserve the singularity** of a matrix. This means:
- If you apply a row operation to a **singular** matrix, the result is still a **singular** matrix.
- If you apply a row operation to a **non-singular** matrix, the result is still a **non-singular** matrix.

Let's explore the three main row operations using an example.

**Example Matrix:**  

$$
A = \begin{bmatrix} 5 & 1 \\ 4 & 3 \end{bmatrix}
$$

First, let's check if this matrix is singular by calculating its determinant:

$$
\det(A) = (5)(3) - (1)(4) = 15 - 4 = 11
$$

Since the determinant is **11** (non-zero), the matrix is **non-singular**.

---

## Operation 1: Switching Rows

The first operation is to simply swap the positions of two rows.

**Original Matrix (det=11):**  

$$
\begin{bmatrix} 5 & 1 \\ 4 & 3 \end{bmatrix}
$$

**After Switching Rows:**

$$
\begin{bmatrix} 4 & 3 \\ 5 & 1 \end{bmatrix}
$$

Let's calculate the determinant of the new matrix:

$$
\det(\text{new}) = (4)(1) - (3)(5) = 4 - 15 = -11
$$

The new determinant is **-11**. Since it's still non-zero, the matrix is still **non-singular**. Notice that switching two rows negates the determinant. If the original determinant had been 0, the new one would also be 0.

---

## Operation 2: Multiplying a Row by a Non-Zero Scalar

The second operation is to multiply all the elements in a single row by a non-zero constant (a scalar).

**Original Matrix (det=11):**

$$
\begin{bmatrix} 5 & 1 \\ 4 & 3 \end{bmatrix}
$$

**After Multiplying Row 1 by 10:**  

$$
\begin{bmatrix} 50 & 10 \\ 4 & 3 \end{bmatrix}
$$

Let's calculate the new determinant:

$$
\det(\text{new}) = (50)(3) - (10)(4) = 150 - 40 = 110
$$

The new determinant is **110**, which is exactly **10 times** the original determinant. Since we multiplied by a non-zero scalar, a non-zero determinant remains non-zero, and a zero determinant would remain zero. This operation preserves singularity.

---

## Operation 3: Adding a Row to Another Row

The final operation is to add one row to another. The row being added remains unchanged, while the row it's added to is replaced by the sum.

**Original Matrix (det=11):**  

$$
\begin{bmatrix} 5 & 1 \\ 4 & 3 \end{bmatrix}
$$

**After Adding Row 2 to Row 1 (New Row 1 = Row 1 + Row 2):**  

_New Row 1 = `[5+4, 1+3]` = `[9, 4]`_  

$$
\begin{bmatrix} 9 & 4 \\ 4 & 3 \end{bmatrix}
$$

Let's calculate the new determinant:

$$
\det(\text{new}) = (9)(3) - (4)(4) = 27 - 16 = 11
$$

Believe it or not, this operation **does not change the determinant at all**. Since the determinant is unchanged, this operation also preserves singularity.

*(Note: This also works for adding a *multiple* of one row to another, which is the most common form of this operation used in Gaussian elimination.)*

---

**Next:** []