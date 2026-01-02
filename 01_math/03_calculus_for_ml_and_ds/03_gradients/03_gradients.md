# Gradients

Now that you know how to calculate partial derivatives, you already know the components of the **gradient**. The gradient is simply a convenient way to condense all the partial derivatives of a function into a single **vector**.

Recall our function $f(x, y) = x^2 + y^2$. We found two partial derivatives:

* The partial derivative with respect to `x`: $\frac{\partial f}{\partial x} = 2x$  

* The partial derivative with respect to `y`: $\frac{\partial f}{\partial y} = 2y$

The gradient of `f` is the vector that contains these two partial derivatives as its components.

$$ \text{gradient of } f = \begin{bmatrix} 2x \\ 
2y \end{bmatrix} $$


## Gradient Notation

The gradient is denoted by the symbol **∇** (called "nabla"). The gradient of a function `f` is written as **∇f**.

In general, for a function with *n* variables, $f(x_1, x_2, \dots, x_n)$, the gradient is a vector of its *n* partial derivatives:

$$ \nabla f = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ 
\frac{\partial f}{\partial x_2} \\ 
\vdots \\ 
\frac{\partial f}{\partial x_n} \end{bmatrix} $$

This gradient vector is a complete description of the slope of the tangent plane (or hyperplane in higher dimensions) at any given point.

## Exercise

Find the gradient of the function $f(x, y) = x^2 + y^2$ at the point **(2, 3)**.

**Solution:**
1.  First, find the general formula for the gradient:

$$ \nabla f = \begin{bmatrix} 2x \\ 
2y \end{bmatrix} $$

2.  Next, substitute the values `x=2` and `y=3` into the formula:

$$ \nabla f(2, 3) = \begin{bmatrix} 2(2) \\ 
2(3) \end{bmatrix} = \begin{bmatrix} 4 \\ 
6 \end{bmatrix} $$

The gradient of the function at the point (2, 3) is the vector **(4, 6)**.


---

**Next:** [Gradients and Maxima/Minima](./04_gradients_and_maxima_minima.md)
