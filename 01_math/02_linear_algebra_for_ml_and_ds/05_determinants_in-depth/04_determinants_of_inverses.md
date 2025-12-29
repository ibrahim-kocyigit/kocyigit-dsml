# The Determinant of an Inverse

There is a very simple and powerful rule that connects the determinant of a matrix to the determinant of its inverse.

**Rule:** The determinant of an inverse matrix is the reciprocal of the determinant of the original matrix.

$$
\det(A^{-1}) = \frac{1}{\det(A)} 
$$

This makes intuitive sense. If a transformation `A` scales the area of a space by a factor of 5, then the inverse transformation `A⁻¹` must scale it back down by a factor of 1/5 to return the space to its original state.

Let's look at some examples to verify this:

#### Example 1:

$$
A = \begin{bmatrix} 3 & 1 \\ 
1 & 2 \end{bmatrix} \implies \det(A) = 5 
$$

$$
A^{-1} = \begin{bmatrix} 0.4 & -0.2 \\ -0.2 & 0.6 \end{bmatrix} \implies \det(A^{-1}) = 0.2 
$$

We can see that $0.2 = \frac{1}{5}$. The rule holds.

#### Example 2 (Singular Matrix):

$$
B = \begin{bmatrix} 1 & 1 \\ 
2 & 2 \end{bmatrix} \implies \det(B) = 0 
$$

This matrix is singular and **has no inverse**. Notice that the formula $\frac{1}{\det(B)}$ would result in division by zero, which is undefined. The rule is consistent.

## The Algebraic Proof

Why is this rule always true? We can prove it easily using the rules we already know.

1.  **Start with the definition of an inverse:**

$$
A \cdot A^{-1} = I 
$$  

(A matrix multiplied by its inverse is the identity matrix)

2.  **Take the determinant of both sides:**  

$$
\det(A \cdot A^{-1}) = \det(I) 
$$  


3.  **Apply the product rule for determinants** to the left side:  

$$
\det(A) \cdot \det(A^{-1}) = \det(I) 
$$

4.  **The determinant of the identity matrix is always 1.** The identity transformation doesn't change the area of the unit square at all, so its area scaling factor is 1. Therefore:  

$$
\det(A) \cdot \det(A^{-1}) = 1 
$$

5.  **Solve for the determinant of the inverse** by dividing both sides by $\det(A)$:  

$$
\det(A^{-1}) = \frac{1}{\det(A)} 
$$  

This simple proof confirms our rule.

---

**Next:** [Basis in Linear Algebra](../06_eigenvalues_and_eigenvectors/01_basis_in_linear_algebra.md)