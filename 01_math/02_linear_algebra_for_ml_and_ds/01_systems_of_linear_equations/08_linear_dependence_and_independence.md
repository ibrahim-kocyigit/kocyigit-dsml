# Linear Dependence and Independence

We've connected the singularity of a system to its number of solutions and its geometric picture. Now, we'll learn a way to determine if a matrix is **singular** or **non-singular** just by looking at its internal structure.

The core idea is **linear dependence**. A matrix is singular if its rows are "dependent" on each other, meaning at least one row contains redundant information that can be constructed from the other rows.

## Simple Case: One Row is a Multiple of Another

Let's go back to our basic 2x2 singular and non-singular matrices.

* **Non-Singular Matrix:**
```math
\begin{bmatrix}
1 & 1 \\
1 & 2
\end{bmatrix}
```
<br>

* **Singular Matrix:**
```math
\begin{bmatrix}
1 & 1 \\
2 & 2
\end{bmatrix}
```
<br>

For the **singular matrix**, it's easy to see a relationship between the rows:
$ \text{Row 2} = 2 \times \text{Row 1} $

Because the second row can be perfectly predicted from the first, it offers no new information. The rows are said to be **linearly dependent**. This dependency is the reason the matrix is **singular**.

In contrast, for the **non-singular matrix**, you can't multiply the first row by any single number to get the second row. Each row provides unique information. The rows are **linearly independent**.

## A More General Definition of Linear Dependence

**Linear dependence** isn't limited to one row being a simple multiple of another. A row can also be a more complex combination of *multiple* other rows.

Consider this singular matrix:
```math
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
1 & 1 & 0
\end{bmatrix}
```
<br>

Here, the relationship is:
$ \text{Row 3} = \text{Row 1} + \text{Row 2} $

Since the third row is just the sum of the first two, it is redundant. The information was already there. This makes the rows **linearly dependent** and the matrix **singular**.

## More Complex Examples of Dependence

The relationships can sometimes be more subtle.

### Example 1: Highly Redundant Matrix

```math
\begin{bmatrix}
1 & 1 & 1 \\
2 & 2 & 2 \\
3 & 3 & 3
\end{bmatrix}
```
<br>

This matrix is highly singular. It has multiple dependencies, including:
* $\text{Row 2} = 2 \times \text{Row 1}$
* $\text{Row 3} = 3 \times \text{Row 1}$
* $\text{Row 3} = \text{Row 1} + \text{Row 2}$

### Example 2: Subtle Dependence

This matrix is also singular, but the relationship is less obvious.
```math
\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 2 \\
1 & 1 & 3
\end{bmatrix}
```
<br>

The dependency here is that the second row is the *average* of the first and third rows:
```math
\frac{\text{Row 1} + \text{Row 3}}{2} = \text{Row 2}
```
<br>

This is still a form of linear combination ($0.5 \times R_1 + 0.5 \times R_3 = R_2$), so the rows are **linearly dependent**.

---

## Linear Independence

Now, let's look again at our standard non-singular 3x3 matrix:
```math
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 2
\end{bmatrix}
```
<br>

For this matrix, it is **impossible** to find any combination of two rows that produces the third. No row can be written as a combination of the others. Each row contributes unique, essential information.

Because no row depends on the others, the rows are **linearly independent**, which is why the matrix is **non-singular**.

*(Note: While it's easy to spot a dependency if you find one, it can be difficult to prove that no dependency exists just by looking. We'll learn formal methods for this soon!)*

## Summary: The Key Connection

This gives us our most direct definition of singularity yet.

* **Linearly Dependent Rows** ⛓️
    * **What it means:** At least one row is redundant and can be formed from a combination of the others.
    * **Result:** The matrix is **SINGULAR**.

* **Linearly Independent Rows** ✅
    * **What it means:** Every row provides unique, essential information that cannot be constructed from the other rows.
    * **Result:** The matrix is **NON-SINGULAR**.