# Training the Model with Gradient Descent

## Gradient Descent

> **Note:** [Gradients](../../../01_math/03_calculus_for_ml_and_ds/03_gradients/) and [gradient descent](../../../01_math/03_calculus_for_ml_and_ds/04_gradient_descent/) are already covered in great detail in the **Calculus for Machine Learning and Data Science** course, which is a part of the Math pillar in this repository.

- In previous videos, you saw how different choices of parameters $w$ and $b$ affect the cost function $J(w, b)$.
- **Goal:** Find the values of $w$ and $b$ that minimize $J(w, b)$.

### What is Gradient Descent?

- **Gradient descent** is an algorithm to systematically find the minimum of a function (such as the cost function in linear regression).
- It is widely used in machine learning, including for training neural networks (deep learning).

### How Gradient Descent Works

1. **Initialize** the parameters (e.g., $w = 0$, $b = 0$).
2. **Iteratively update** the parameters to reduce the cost $J(w, b)$.
3. At each step, move in the direction of the **steepest descent** (the direction where $J$ decreases the fastest).

- For a cost function $J(w, b)$, you can visualize the surface as a 3D landscape (like hills and valleys).
- Gradient descent is like standing on a hill and always taking a small step in the direction that goes downhill the fastest.
- Repeat this process until you reach a valley (a minimum of the cost function).

### Local Minima

- For simple cost functions (like linear regression with squared error), the cost surface is bowl-shaped and has a single minimum (global minimum).
- For more complex functions (e.g., neural networks), there may be multiple valleys (local minima).
- Where you end up depends on your starting point.

### Summary

- Gradient descent is a general algorithm for minimizing functions.
- It is a foundational tool in machine learning for training models by minimizing their cost functions.

---