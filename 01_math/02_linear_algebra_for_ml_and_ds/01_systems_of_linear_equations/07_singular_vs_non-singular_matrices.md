# Singular vs. Non-Singular Matrices

Now that we know the constants in a system of equations don't determine its singularity, we can focus on the most important part: the coefficients of the variables. This leads us directly to the concept of a **matrix**.

A **matrix** is a rectangular grid of numbers that can represent the coefficients of a system. We can then transfer the properties of the system, like singularity, directly to the matrix itself. This is a crucial step in the abstraction that makes linear algebra so powerful.

## From Systems to Matrices (2x2 Example)

Let's revisit our simplified (homogeneous) 2x2 systems from the last lesson. Since we're only interested in singularity, we can ignore the constants.

* **Non-Singular System:**
    * $1a + 1b = 0$
    * $1a + 2b = 0$  

* **Singular System:**
    * $1a + 1b = 0$
    * $2a + 2b = 0$

We can extract the coefficients of `a` and `b` and arrange them in a box, creating a matrix. Each **row** corresponds to an equation, and each **column** corresponds to a variable's coefficients.

The matrix for our **non-singular** system is:

```math
\begin{bmatrix}
1 & 1 \\
1 & 2
\end{bmatrix}
```
<br>

The matrix for our **singular** system is:
```math
\begin{bmatrix}
1 & 1 \\
2 & 2
\end{bmatrix}
```
<br>

## Defining Singularity for Matrices

The connection is very straightforward. We apply the same terminology from the system to its corresponding matrix.

* **Non-Singular Matrix** ✅
    If a system of equations is **non-singular** (has a single unique solution), its matrix of coefficients is called a **non-singular matrix**.

* **Singular Matrix** ⚠️
    If a system of equations is **singular** (has infinitely many solutions or no solution), its matrix of coefficients is called a **singular matrix**.

Based on this:
1. The matrix: 
```math
\begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}
```
... is non-singular.

<br>

2. The matrix $\begin{bmatrix} 1 & 1 \\ 2 & 2 \end{bmatrix}$ is **singular**.

This is a key idea: we can now analyze a matrix on its own to determine these properties, without needing to solve the entire system of equations every time.

## Extending to 3x3 Systems and Matrices

The same principle applies to larger systems. Let's form corresponding matrices for three 3x3 systems by taking the coefficients of `a`, `b`, and `c`:

**System 1 (Non-Singular):**
* $a + b + c = 10$
* $a + 2b + c = 15$
* $a + b + 2c = 12$
* **Matrix 1:**
$
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 2
\end{bmatrix}
$

**System 2 (Singular):**
* $a + b + c = 10$
* $a + b + 2c = 15$
* $a + b + 3c = 20$
* **Matrix 2:**
$
\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 2 \\
1 & 1 & 3
\end{bmatrix}
$

**System 3 (Singular):**
* $a + b + c = 10$
* $2a + 2b + 2c = 20$
* $3a + 3b + 3c = 30$

* **Matrix 4:**
$
\begin{bmatrix}
1 & 1 & 1 \\
2 & 2 & 2 \\
3 & 3 & 3
\end{bmatrix}
$  

---

## Classifying the 3x3 Matrices

Based on our analysis of the original systems, we can now classify these matrices directly:

* **Matrix 1** is **non-singular** because its corresponding system had a unique solution.
* **Matrix 2** is **singular** because its system was redundant.
* **Matrix 3** is **singular** because its system was also redundant.

From now on, we can focus on the properties of the matrix itself to understand the nature of the system it represents.