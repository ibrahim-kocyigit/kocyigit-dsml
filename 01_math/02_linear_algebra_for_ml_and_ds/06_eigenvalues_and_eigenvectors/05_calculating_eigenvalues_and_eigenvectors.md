# Calculating Eigenvalues and Eigenvectors

Now that we know what eigenvectors and eigenvalues are, how do we find them for a given matrix? The process involves a clever trick using the determinant.

Let's start with our transformation matrix:  

```math
A = \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}  
```
<br>

We are looking for special vectors `v` and scalars `λ` that satisfy the eigenvector equation:  

$$
Av = \lambda v 
$$  

We can rewrite this equation by bringing everything to one side:  

$$ 
Av - \lambda v = 0 
$$  

To factor out the vector `v`, we need to introduce the identity matrix `I`. We can rewrite `λv` as `λIv`:  

$$
Av - \lambda Iv = 0 
$$  

$$
(A - \lambda I)v = 0 
$$  

This is the most important equation for finding eigenvalues. Let's analyze what it means.

## The Key Insight: Singularity

The equation $(A - \lambda I)v = 0$ is a system of linear equations. We are looking for a **non-zero** vector `v` that solves this system.

If the matrix $(A - \lambda I)$ were non-singular, the only solution to this equation would be the trivial one: 

$$
v = \begin{bmatrix} 0 \\ 
0 \end{bmatrix}
$$

But eigenvectors must be non-zero! Therefore, for a non-zero solution `v` to exist, the matrix $(A - \lambda I)$ **must be singular**.

And what do we know about singular matrices? Their determinant is zero.

**Rule:** To find the eigenvalues (`λ`) of a matrix `A`, we must solve the equation: 

$$
\det(A - \lambda I) = 0 
$$

## Step 1: Find the Eigenvalues

Let's apply this rule to our matrix `A`.

1.  **First, calculate the matrix $(A - \lambda I)$:**  

```math
(A - \lambda I) = \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix} - \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2-\lambda & 1 \\ 0 & 3-\lambda \end{bmatrix}
```
<br>

2.  **Next, calculate its determinant:**

```math
\det(A - \lambda I) = (2-\lambda)(3-\lambda) - (1)(0) = (2-\lambda)(3-\lambda)
```
<br>

3.  **Finally, set the determinant to zero and solve for `λ`:**

```math
(2-\lambda)(3-\lambda) = 0
```
<br>

This equation is true if either `2 - λ = 0` or `3 - λ = 0`.

The solutions are $\boldsymbol{\lambda_1 = 2}$ and $\boldsymbol{\lambda_2 = 3}$.

These are the two **eigenvalues** of our matrix `A`. The equation we solved is called the **characteristic polynomial**.

## Step 2: Find the Eigenvectors

Now that we have the eigenvalues, we can find the corresponding eigenvector for each one by plugging it back into the equation $(A - \lambda I)v = 0$.

### For λ₁ = 2:

We are solving $(A - 2I)v = 0$:  

```math
\begin{bmatrix} 2-2 & 1 \\ 0 & 3-2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\implies
\begin{bmatrix} 0 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
```
<br>

This gives us the system of equations:
* $0x + 1y = 0 \implies y=0$
* $0x + 1y = 0 \implies y=0$

The only constraint is that `y` must be 0. The variable `x` can be anything. So, any vector of the form `(k, 0)` is an eigenvector. Let's pick the simplest one where `k=1`.
* The eigenvector for $\lambda_1 = 2$ is 

$$
\boldsymbol{v_1 = \begin{bmatrix} 1 \\ 
0 \end{bmatrix}}
$$

### For λ₂ = 3:

We are solving $(A - 3I)v = 0$:  

```math
\begin{bmatrix} 2-3 & 1 \\ 0 & 3-3 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\implies
\begin{bmatrix} -1 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
```
<br>

This gives us the system of equations:
* $-x + y = 0 \implies x=y$
* $0x + 0y = 0$ (This provides no information)

The only constraint is that `x` must equal `y`. So, any vector of the form `(k, k)` is an eigenvector. Let's pick the simplest one where `k=1`.
* The eigenvector for $\lambda_2 = 3$ is 

$$
\boldsymbol{v_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}}
$$

These are the same eigenvectors we identified geometrically in the last lesson.

> ⚠️ **A Note on Non-Square Matrices:** This entire process relies on calculating a determinant. Since the determinant is only defined for **square matrices**, eigenvalues and eigenvectors are also only defined for square matrices.

---

**Next:** [On the Number of Eigenvectors](./06_on_the_number_of_eigenvectors.md)