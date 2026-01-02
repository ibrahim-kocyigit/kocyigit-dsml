# Newton's Method for Two Variables

Let's conclude by learning how to apply Newton's method to optimize functions of many variables. As you'll see, the Hessian matrix is the key component.

Recall the update rule for Newton's method for a function of one variable, which we can write using the inverse of the second derivative:

$$ x_{k+1} = x_k - (f''(x_k))^{-1} \cdot f'(x_k) $$

This form generalizes beautifully to multiple variables. The **first derivative** `f'` becomes the **gradient vector** `∇f`, and the **second derivative** `f''` becomes the **Hessian matrix** `H`.

**Newton's Method Update Rule (for multiple variables):**

$$ \begin{bmatrix} x_{k+1} \\ 
y_{k+1} \end{bmatrix} = \begin{bmatrix} x_k \\ 
y_k \end{bmatrix} - [H(x_k, y_k)]^{-1} \cdot \nabla f(x_k, y_k) 
$$

Let's use this method to find the minimum of the complex, non-quadratic function:

$$ f(x, y) = x^4 + 0.8y^4 + 4x^2 + 2y^2 - xy - 0.2x^2y $$

The minimum for this function is at `(0, 0)`.

## The Components: Gradient and Hessian

First, we need to calculate the gradient vector and the Hessian matrix for our function.

**1. The Gradient (First Derivatives):**

$$ 
\nabla f = \begin{bmatrix} 4x^3 + 8x - y - 0.4xy \\ 
3.2y^3 + 4y - x - 0.2x^2 \end{bmatrix} 
$$

**2. The Hessian (Second Derivatives):**

$$ 
H = \begin{bmatrix} 12x^2 + 8 - 0.4y & -1 - 0.4x \\ 
-1 - 0.4x & 9.6y^2 + 4 \end{bmatrix} 
$$

Unlike our previous simple example, both the gradient and the Hessian change depending on our current `(x, y)` position. This means we must recalculate them at every step of the algorithm.

## Iterations in Detail

Let's perform the first few iterations by hand to see the process in detail.

* **Starting Point:** Let's choose `(x₀, y₀) = (4, 4)`.

### Iteration 1 (Finding x₁, y₁):
1.  **Calculate the Gradient at (4, 4):** 

$$
\nabla f(4, 4) = \begin{bmatrix} 277.6 \\ 
213.6 \end{bmatrix}
$$  

2.  **Calculate the Hessian at (4, 4):** 

$$
H(4, 4) = \begin{bmatrix} 198.4 & -2.6 \\ 
-2.6 & 157.6 \end{bmatrix}
$$  

3.  **Calculate the Inverse of the Hessian:** 

$$
[H(4, 4)]^{-1} \approx \begin{bmatrix} 0.00504 & 0.00008 \\ 
0.00008 & 0.00634 \end{bmatrix}
$$  

4.  **Apply the update rule:**

$$
\begin{bmatrix} x_1 \\ 
y_1 \end{bmatrix} = \begin{bmatrix} 4 \\ 
4 \end{bmatrix} - [H]^{-1} \begin{bmatrix} 277.6 \\ 
213.6 \end{bmatrix} \approx \begin{bmatrix} 2.582 \\ 
2.623 \end{bmatrix}
$$

In one step, we've moved significantly closer to the true minimum at `(0, 0)`.

### Iteration 2 (Finding x₂, y₂):
Now, we repeat the entire process from our new point, `(x₁, y₁) ≈ (2.582, 2.623)`.
1.  **Calculate the Gradient at (2.582, 2.623):** $ \nabla f \approx \begin{bmatrix} 84.2 \\ 64.3 \end{bmatrix} $  

2.  **Calculate the Hessian at (2.582, 2.623):** $ H \approx \begin{bmatrix} 87.0 & -2.03 \\ -2.03 & 70.0 \end{bmatrix} $  

3.  **Calculate the Inverse of the Hessian:** $ [H]^{-1} \approx \begin{bmatrix} 0.0115 & 0.0003 \\ 0.0003 & 0.0143 \end{bmatrix} $  

4.  **Apply the update rule:**
    $$ \begin{bmatrix} x_2 \\ y_2 \end{bmatrix} = \begin{bmatrix} 2.582 \\ 2.623 \end{bmatrix} - [H]^{-1} \begin{bmatrix} 84.2 \\ 64.3 \end{bmatrix} \approx \begin{bmatrix} 1.590 \\ 1.669 \end{bmatrix} $$

### Iteration 3 (Finding x₃, y₃):
Repeating the process again from `(x₂, y₂) ≈ (1.590, 1.669)` yields:
$$ \begin{bmatrix} x_3 \\ y_3 \end{bmatrix} \approx \begin{bmatrix} 0.916 \\ 0.998 \end{bmatrix} $$

### Final Convergence:
As we continue this process, the steps get smaller and smaller, rapidly converging on the solution. After 8 iterations, the position is:
$$ \begin{bmatrix} x_8 \\ y_8 \end{bmatrix} \approx \begin{bmatrix} 4.15 \times 10^{-17} \\ -2.05 \times 10^{-17} \end{bmatrix} $$
This is an exceptionally small number, practically equal to the true minimum at **(0, 0)**.