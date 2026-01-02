# The Hessian

In the previous lesson, you learned about the second derivative and its usefulness in optimization. That was all for functions of one variable. Now we will see how this concept extends to functions of multiple variables.

For multivariable functions, the second derivative is not a single number but a **matrix** full of second-order partial derivatives, called the **Hessian matrix**.

Let's compare the progression from one to two variables:

| Concept | One Variable | Two Variables |
| :--- | :--- | :--- |
| **Function** | $f(x)$ | $f(x, y)$ |
| **1st Derivative**| $f'(x)$ (a scalar) | $\nabla f = \begin{bmatrix} f_x \\ f_y \end{bmatrix}$ (a vector) |
| **2nd Derivative**| $f''(x)$ (a scalar) | **The Hessian** (a matrix) |

## Calculating Second-Order Partial Derivatives

To understand the Hessian, let's start with a function $f(x, y) = 2x^2 + 3y^2 - xy$.

First, we find its first-order partial derivatives (the gradient):
* $f_x = \frac{\partial f}{\partial x} = 4x - y$  

* $f_y = \frac{\partial f}{\partial y} = 6y - x$

Now, we can take the derivative of *each* of these results with respect to *each* of the variables again. This gives us four **second-order partial derivatives**:

1.  **$f_{xx} = \frac{\partial}{\partial x}(f_x) = \frac{\partial}{\partial x}(4x - y) = 4$**  

2.  **$f_{xy} = \frac{\partial}{\partial y}(f_x) = \frac{\partial}{\partial y}(4x - y) = -1$**  

3.  **$f_{yx} = \frac{\partial}{\partial x}(f_y) = \frac{\partial}{\partial x}(6y - x) = -1$**  

4.  **$f_{yy} = \frac{\partial}{\partial y}(f_y) = \frac{\partial}{\partial y}(6y - x) = 6$**

Notice that the "mixed" partial derivatives, $f_{xy}$ and $f_{yx}$, are the same. This is almost always the case for the functions we encounter in machine learning.

## The Hessian Matrix

The Hessian matrix, often denoted as `H` or `∇²f`, is the matrix that organizes all these second-order partial derivatives.

For a function of two variables, the Hessian is a 2x2 matrix:

$$ H = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix} $$

For our example function, $f(x, y) = 2x^2 + 3y^2 - xy$, the Hessian matrix is:

$$ H = \begin{bmatrix} 4 & -1 \\ -1 & 6 \end{bmatrix} $$

The Hessian matrix gives us a lot of information about the function's curvature at a given point and is very useful in advanced optimization methods, such as Newton's method for multiple variables.