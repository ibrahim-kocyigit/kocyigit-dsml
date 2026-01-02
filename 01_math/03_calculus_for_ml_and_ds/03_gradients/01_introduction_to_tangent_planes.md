# Introduction to Tangent Planes

In the previous modules, we learned everything about functions of one variable. Now, we will extend those concepts to functions with two or more variables.

The most important concept to generalize is the derivative.
* In one dimension, the derivative at a point gives us the slope of the **tangent line**.
* In two dimensions (for a function with two inputs), the derivative at a point gives us the **tangent plane**.

This concept of a tangent plane is the foundation for optimizing functions of multiple variables, which is the core of how most machine learning models are trained using algorithms like **Gradient Descent**.

## From Tangent Line to Tangent Plane

Recall the function $f(x) = x^2$. Its graph is a 2D parabola. At any point, we can find a unique tangent line that just "touches" the curve, and the slope of this line is the derivative.

Now, consider a function of two variables, such as $f(x, y) = x^2 + y^2$. This function's graph is a 3D surface (a paraboloid). Instead of a tangent line, we now have a **tangent plane** that touches the surface at a single point.

How do we find this plane? The key idea is to "slice" the 3D surface to turn the problem back into a simple 2D derivative problem that we already know how to solve.

![](./images/0101.png)

## The "Slicing" Method

To find the tangent plane at a point, like `(2, 4)`, we can find two different tangent lines at that point and then combine them to form a plane.

1.  **Slice 1 (Fix y=4):** Imagine we slice our 3D surface with the plane `y = 4`. The intersection of these two surfaces is a simple 2D parabola.
    * Our function becomes: $f(x, 4) = x^2 + 4^2 = x^2 + 16$.
    * We can now take the derivative of this with respect to `x`: $f'(x) = 2x$.
    * At our point where `x=2`, the slope of the tangent line in this direction is $2(2) = 4$.  

2.  **Slice 2 (Fix x=2):** Now imagine we slice the surface with the plane `x = 2`. The intersection is another 2D parabola.
    * Our function becomes: $f(2, y) = 2^2 + y^2 = 4 + y^2$.
    * We can take the derivative of this with respect to `y`: $f'(y) = 2y$.
    * At our point where `y=4`, the slope of the tangent line in this direction is $2(4) = 8$.

Since we have two distinct tangent lines that cross at our point of interest, they uniquely define the **tangent plane** to the surface at that point.

This process of finding the derivative by fixing all other variables is the core idea behind **partial derivatives**, which we will explore next.


---

**Next:** [Partial Derivatives](./02_partial_derivatives.md)
