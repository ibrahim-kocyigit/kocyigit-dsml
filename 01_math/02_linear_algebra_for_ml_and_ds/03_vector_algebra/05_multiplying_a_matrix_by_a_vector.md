# Multiplying a Matrix by a Vector

In this lesson, we will learn how to multiply a matrix and a vector. This operation is fundamental to linear algebra and is precisely how we represent a system of linear equations in a compact form.

---

## From a Single Equation to a Dot Product

Recall that the dot product is the sum of the products of corresponding entries. A single linear equation can be expressed as a dot product.

For example, the equation for the total cost of fruit:  

$$
2a + 4b + c = 28
$$

...can be written as the dot product of a **row vector** of quantities and a **column vector** of unknown prices:  

$$
\begin{bmatrix} 2 & 4 & 1 \end{bmatrix} \cdot \begin{bmatrix} a \\ b \\ c \end{bmatrix} = 28
$$

---

## From a System of Equations to Multiple Dot Products

Now, imagine we have a system of three equations. Each equation can be expressed as its own dot product.

**System of Equations:**
1.  $a + b + c = 10$
2.  $a + 2b + c = 15$
3.  $a + b + 2c = 12$

**As Dot Products:**
1.  $\begin{bmatrix} 1 & 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} a \\ b \\ c \end{bmatrix} = 10$
2.  $\begin{bmatrix} 1 & 2 & 1 \end{bmatrix} \cdot \begin{bmatrix} a \\ b \\ c \end{bmatrix} = 15$
3.  $\begin{bmatrix} 1 & 1 & 2 \end{bmatrix} \cdot \begin{bmatrix} a \\ b \\ c \end{bmatrix} = 12$

---

## The Final Step: Matrix-Vector Multiplication

Writing out three separate dot products is clumsy. Since the column vector of variables $(a, b, c)$ is the same in each equation, we can combine the row vectors into a single **matrix**.

This gives us the **matrix-vector product**, which is simply a stack of dot products:

$$
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 2
\end{bmatrix}
\begin{bmatrix} a \\ b \\ c \end{bmatrix}
=
\begin{bmatrix} 10 \\ 15 \\ 12 \end{bmatrix}
$$

This is the standard, compact way to represent a system of linear equations: **$Xw = y$**.

---

## A Note on Dimensions

For matrix-vector multiplication to be defined, the **number of columns in the matrix** must equal the **number of components (rows) in the vector**.

- A **3x3** matrix can be multiplied by a **3x1** vector. ✅
- A **4x3** matrix can be multiplied by a **3x1** vector. ✅
- A **3x3** matrix **cannot** be multiplied by a **2x1** vector. ❌

The result of the multiplication will be a new vector whose length is equal to the **number of rows** in the matrix.

---

**Next:** []