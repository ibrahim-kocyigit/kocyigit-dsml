# On the Number of Eigenvectors

Does an *n* x *n* matrix always have *n* distinct eigenvectors? The answer is **no**. Sometimes, a matrix can have fewer eigenvectors than its dimension. This happens when we have **repeated eigenvalues**. Let's explore two examples to see how this works.

## Example 1: Repeated Eigenvalue, Full Set of Eigenvectors

Let's analyze the following 3x3 matrix:  

```math
A = \begin{bmatrix}
2 & 0 & 0 \\
-1 & 4 & -0.5 \\
0 & 0 & 2
\end{bmatrix}
```
<br>

### Step 1: Find the Eigenvalues

We solve the characteristic equation, $\det(A - \lambda I) = 0$. For a triangular matrix like this, the determinant is the product of the diagonal entries.  

```math
\det(A - \lambda I) = (2-\lambda)(4-\lambda)(2-\lambda) = (2-\lambda)^2(4-\lambda) = 0 
```
<br>

The roots of this polynomial give us our eigenvalues:
* $\lambda_1 = 4$
* $\lambda_2 = 2$
* $\lambda_3 = 2$

Notice that the eigenvalue `2` is repeated.

### Step 2: Find the Eigenvectors

**For λ₁ = 4:** We solve the system $(A - 4I)v = 0$. This leads to the equations $x_1=0$ and $x_3=0$, while $x_2$ can be any number. We can choose the simplest eigenvector:    

$$
v_1 = \begin{bmatrix} 0 \\ 
1 \\ 
0 \end{bmatrix} 
$$

**For the repeated λ = 2:** We solve the system $(A - 2I)v = 0$. This leads to the single equation $-x_1 + 2x_2 - 0.5x_3 = 0$. This equation has two "free variables," meaning we can choose two variables and the third will be determined. This allows us to find **two linearly independent eigenvectors** that satisfy this equation. For example:

* If we choose $x_2=1, x_3=0$, then $x_1=2$. This gives us 

$$
v_2 = \begin{bmatrix} 2 \\ 
1 \\ 
0 \end{bmatrix} 
$$  

* If we choose $x_2=1, x_3=2$, then $x_1=1$. This gives us 

$$
v_3 = \begin{bmatrix} 1 \\ 
1 \\ 
2 \end{bmatrix} 
$$

**Conclusion for Example 1:** Even though the eigenvalue `2` was repeated, we were still able to find **three** distinct, linearly independent eigenvectors. This set of vectors can form an **eigenbasis** for the 3D space.

---

## Example 2: Repeated Eigenvalue, Fewer Eigenvectors

Now let's change just one value in the matrix and see what happens.  

$
B = \begin{bmatrix}
2 & 0 & 0 \\
-1 & 4 & -0.5 \\
4 & 0 & 2
\end{bmatrix}
$

### Step 1: Find the Eigenvalues
The characteristic polynomial is the same as before, so the eigenvalues are also the same: $\lambda_1 = 4$, $\lambda_2 = 2$, $\lambda_3 = 2$.

### Step 2: Find the Eigenvectors

* **For λ₁ = 4:**
    The process is similar to before, and we find the same eigenvector:    $ v_1 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} $

* **For the repeated λ = 2:**
    We solve the system $(B - 2I)v = 0$. This leads to a different set of equations, which simplify to two constraints: $x_1=0$ and $x_3=4x_2$. Now, we only have **one free variable**. Once we choose a value for $x_2$, the other variables are fixed.
    * If we choose $x_2=1$, then $x_1=0$ and $x_3=4$. This gives the eigenvector $ v_2 = \begin{bmatrix} 0 \\ 1 \\ 4 \end{bmatrix} $.
    * Any other choice for $x_2$ will just give us a scaled version of this same vector (e.g., if $x_2=0.5$, we get `(0, 0.5, 2)`). We cannot find a second, linearly independent eigenvector for this eigenvalue.

**Conclusion for Example 2:**
For this matrix, we only found **two** distinct eigenvectors. Since we need three linearly independent vectors to span 3D space, this set of eigenvectors **cannot** form an eigenbasis.

---
## Summary of Rules

The number of distinct eigenvectors you can find depends on the eigenvalues. For an *n* x *n* matrix:
* If all *n* eigenvalues are **different**, you are guaranteed to find *n* linearly independent eigenvectors.
* If an eigenvalue is **repeated *k* times**, you may find anywhere from 1 to *k* linearly independent eigenvectors for that eigenvalue. You are not guaranteed to find *k* of them.