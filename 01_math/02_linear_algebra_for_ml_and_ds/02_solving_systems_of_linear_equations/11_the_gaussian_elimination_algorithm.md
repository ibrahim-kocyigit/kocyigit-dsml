# The Gaussian Elimination Algorithm

We are now ready to formalize the elimination method into a powerful, step-by-step algorithm called **Gaussian Elimination**. This is the same process we've been doing, but structured so that it can be followed by hand or implemented in code to solve any system of linear equations.

A key difference is that to solve a system, we can no longer ignore the constants on the right-hand side of the equations. We need to include them in our matrix.

## The Augmented Matrix

To solve a system, we first create an **augmented matrix**. This is done by taking the standard coefficient matrix and adding a final column that holds the constant values from the right-hand side of the equations. A vertical line is often used to separate the coefficients from the constants.

Let's solve the system of equations from the video lecture:

**System of Equations:**
1.  $2a - b + c = 1$
2.  $2a + 2b + 2c = -2$
3.  $4a - 2b + 3c = -1$

**Augmented Matrix:**  

$$
\left[
\begin{array}{ccc|c}
2 & -1 & 1 & 1 \\
2 & 2 & 2 & -2 \\
4 & -2 & 3 & -1
\end{array}
\right]
$$

We can now apply our row operations to this entire augmented matrix to solve the system.

## Phase 1: Forward Elimination (to REF)

The first phase is to transform the matrix into **row echelon form (REF)**. We do this by selecting a **pivot** on the diagonal of each row, setting it to 1, and then using it to create zeros in all the cells below it.

### Step 1: Process the First Pivot (Row 1)

**Initial Matrix:**  

$$
\left[
\begin{array}{ccc|c}
2 & -1 & 1 & 1 \\
2 & 2 & 2 & -2 \\
4 & -2 & 3 & -1
\end{array}
\right]
$$

1.  **Normalize the pivot:** The first pivot is `2`. We divide the entire first row by 2. ($R1 = R1 / 2$)

$$
\left[
\begin{array}{ccc|c}
1 & -0.5 & 0.5 & 0.5 \\
2 & 2 & 2 & -2 \\
4 & -2 & 3 & -1
\end{array}
\right]
$$

2.  **Eliminate below the pivot:**
    * $R2 = R2 - 2 \times R1$
    * $R3 = R3 - 4 \times R1$

$$
\left[
\begin{array}{ccc|c}
1 & -0.5 & 0.5 & 0.5 \\
0 & 3 & 1 & -3 \\
0 & 0 & 1 & -3
\end{array}
\right]
$$

### Step 2: Process the Second Pivot (Row 2)

The first column is done. The next pivot is the `3` in Row 2.

1.  **Normalize the pivot:** $R2 = R2 / 3$

$$
\left[
\begin{array}{ccc|c}
1 & -0.5 & 0.5 & 0.5 \\
0 & 1 & 1/3 & -1 \\
0 & 0 & 1 & -3
\end{array}
\right]
$$

2.  **Eliminate below the pivot:** The value below is already `0`, so this step is complete.

### Step 3: Process the Third Pivot (Row 3)

The final pivot is the `1` in Row 3. It is already normalized, and there are no rows below it. The forward elimination phase is complete, and the matrix is now in **Row Echelon Form**.

## Phase 2: Back Substitution (to RREF)

The second phase is to transform the REF matrix into **reduced row echelon form (RREF)** by creating zeros *above* the pivots, starting from the bottom row and working up.

### Step 4: Use the Third Pivot to Clear Above

1.  **Clear Row 2:** $R2 = R2 - (1/3) \times R3$
2.  **Clear Row 1:** $R1 = R1 - 0.5 \times R3$

$$
\left[
\begin{array}{ccc|c}
1 & -0.5 & 0 & 2 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & -3
\end{array}
\right]
$$

### Step 5: Use the Second Pivot to Clear Above

1.  **Clear Row 1:** $R1 = R1 + 0.5 \times R2$

$$
\left[
\begin{array}{ccc|c}
1 & 0 & 0 & 2 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & -3
\end{array}
\right]
$$

The matrix is now in **Reduced Row Echelon Form**.

### Step 6: Read the Solution

The final augmented column gives us the solution directly: **a = 2, b = 0, c = -3**.

## The Singular Case

If the matrix is singular, the algorithm stops when you get a row of zeros in the coefficient part. To interpret the result, you just need to look at the constant in that row:

* **If the constant is also 0:** The equation is $0 = 0$. The system is redundant and has **infinitely many solutions**.
* **If the constant is not 0:** The equation is $0 = 4$ (for example). This is a contradiction, and the system has **no solution**.

---

**Next:** []