# The Dot Product

The **dot product** is a fundamental operation in linear algebra that allows us to combine two vectors to get a single number (a scalar). It has many uses, including a very nice and compact way to express systems of linear equations.

## An Intuitive Example: Calculating Total Cost

Let's start with a simple problem. Imagine you are buying fruit:
- 2 apples
- 4 bananas
- 1 cherry

The prices for each fruit are:
- Apple: 3 dollars
- Banana: 5 dollars
- Cherry: 2 dollars

**Question:** How much does everything cost in total?

To solve this, we can represent our quantities and prices as vectors.

- **Quantity Vector ($q$):**
  
$$
q = \begin{bmatrix} 2 \\
4 \\
1 \end{bmatrix}
$$

- **Price Vector ($p$):**
  
$$
p = \begin{bmatrix} 3 \\ 
5 \\ 
2 \end{bmatrix}
$$

The total cost is found by multiplying the quantity of each fruit by its price and summing the results:
- Cost of apples: $2 \times 3 = 6$ dollars
- Cost of bananas: $4 \times 5 = 20$ dollars
- Cost of cherries: $1 \times 2 = 2$ dollars
- **Total Cost:** $6 + 20 + 2 = 28$ dollars

This operation—multiplying corresponding components and then summing them up—is exactly the **dot product**.

## Formalizing the Dot Product

We can write the operation above more compactly. It's common to write the first vector as a row vector and the second as a column vector.

The dot product of our two vectors is:

$$
\begin{bmatrix} 2 & 4 & 1 \end{bmatrix} \cdot \begin{bmatrix} 3 \\ 5 \\ 2 \end{bmatrix} = (2)(3) + (4)(5) + (1)(2) = 28
$$

## Connection Between Dot Product and L2-Norm

There is a very useful connection between the dot product and the L2-norm (or magnitude) of a vector.

Recall the vector $v = (4, 3)$, whose L2-norm was 5. Notice what happens when we take the dot product of the vector *with itself*:

$$
v \cdot v = (4)(4) + (3)(3) = 16 + 9 = 25
$$

This result, 25, is the square of the L2-norm ($5^2$).

This is always true. The L2-norm of a vector is the **square root of the dot product of the vector with itself**: $||v||_2 = \sqrt{v \cdot v}$

## The Transpose Operation

The operation of converting a column vector into a row vector (or vice-versa) is called the **transpose**. It is denoted by a superscript $T$.

- If... 

$$
v = \begin{bmatrix} 2 \\ 
4 \\ 
1 \end{bmatrix}
$$ 

... then its transpose is 

$$
v^T = \begin{bmatrix} 2 & 4 & 1 \end{bmatrix}
$$

You can also transpose a matrix. This is done by turning each of its columns into a row.

- If $A = \begin{bmatrix} 2 & 7 \\ 4 & 8 \\ 1 & 9 \end{bmatrix}$ (a 3x2 matrix), then its transpose is $A^T = \begin{bmatrix} 2 & 4 & 1 \\ 7 & 8 & 9 \end{bmatrix}$ (a 2x3 matrix).

Notice that the dimensions of the matrix swap.

---

## General Definition of the Dot Product

Given two vectors, $x$ and $y$, with the same number of components ($n$):

$$
x = (x_1, x_2, \dots, x_n)
$$
$$
y = (y_1, y_2, \dots, y_n)
$$

The dot product is the sum of the products of their corresponding components:

$$
x \cdot y = \sum_{i=1}^{n} x_i y_i = x_1y_1 + x_2y_2 + \dots + x_ny_n
$$

Other common notations for the dot product include angled brackets, $\langle x, y \rangle$, or using the transpose to ensure a row vector is multiplied by a column vector, $x^T y$.

---

**Next:** []