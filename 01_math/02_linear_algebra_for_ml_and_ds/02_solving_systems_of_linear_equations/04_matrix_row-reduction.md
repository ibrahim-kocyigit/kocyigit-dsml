# Matrix Row-Reduction (Gaussian Elimination)

The process of manipulating equations to find a solution has a direct parallel when working with matrices. **Matrix row-reduction**, also known as **Gaussian elimination**, consists of applying the exact same manipulations (multiplying by constants, adding/subtracting rows) to the rows of a matrix.

The goal is to transform a complex matrix into a much simpler, standardized form from which we can extract useful information, such as the solution to the system or whether the matrix is singular.

## From System to Simplified Matrix

Let's trace the journey of a system and its corresponding matrix through this simplification process.

**Original System:**
* $5a + b = 17$
* $4a - 3b = 6$

**Original Matrix:**  

$$
\begin{bmatrix}
5 & 1 \\
4 & -3
\end{bmatrix}
$$

After performing elimination steps (as we did in the previous lesson), we arrived at an intermediate system and its corresponding matrix.

**Intermediate Matrix (Row Echelon Form):**  

$$
\begin{bmatrix}
1 & 0.2 \\
0 & 1
\end{bmatrix}
$$

This form is called **row echelon form**. A key feature is that it has ones on the main diagonal and zeros *below* the diagonal.

Finally, after back-substitution, we arrived at the solved system.

**Solved System:**
* $1a + 0b = 3$
* $0a + 1b = 2$

**Final Matrix (Reduced Row Echelon Form):**  

$$
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$

This is the **identity matrix**, and it's called the **reduced row echelon form**. It has ones on the diagonal and zeros everywhere else.

## Row Reduction on a Singular System

What happens when we apply this process to a singular matrix?

**Original System:**
* $5a + b = 11$
* $10a + 2b = 22$

**Original Matrix:**  

$$
\begin{bmatrix}
5 & 1 \\
10 & 2
\end{bmatrix}
$$

As we saw, subtracting twice the first equation from the second results in `0 = 0`. Applying the same logic to the matrix (e.g., subtracting twice the first row from the second row after normalization) results in a row of zeros.

**Row Echelon Form of the Singular Matrix:**  

$$
\begin{bmatrix}
1 & 0.2 \\
0 & 0
\end{bmatrix}
$$

The presence of a **row of all zeros** is the key indicator that the original matrix was **singular**.

## The General Structure of Row Echelon Form

A matrix is in **row echelon form** if it follows these rules:
1.  The first non-zero number in each row (called the "leading entry" or "pivot") is a 1.
2.  All entries in a column below a leading entry are zeros.
3.  The leading entry of each row is to the right of the leading entry of the row above it.

This results in a general structure that looks like a staircase of ones, with zeros below it.

**General Form:**  

$$
\begin{bmatrix}
1 & * & * & * \\
0 & 1 & * & * \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

*(Where `*` can be any number)*

For 2x2 matrices, this means there are only three possible row echelon forms:

1.  **Non-Singular:**

    $$
    \begin{bmatrix} 1 & * \\ 0 & 1 \end{bmatrix}
    $$

2.  **Singular (One leading 1):**  

    $$
    \begin{bmatrix} 1 & * \\ 0 & 0 \end{bmatrix}
    $$

3.  **Singular (Zero leading 1s):**  

    $$
    \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}
    $$

---

**Next:** []