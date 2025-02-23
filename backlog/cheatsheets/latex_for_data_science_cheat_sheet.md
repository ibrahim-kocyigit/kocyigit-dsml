# LaTeX for Data Science Cheatsheet

## 1. **Basic Math Notation**

### Scalars
- Plain text: `5`, `-3.2`, `π`
- LaTeX:
  ```latex
  5, -3.2, \pi
  ```

### Vectors
- Plain text: `v = [1, 2, 3]`
- LaTeX:
  ```latex
  \mathbf{v} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
  ```

### Matrices
- Plain text: `A = [[1, 2], [3, 4]]`
- LaTeX:
  ```latex
  \mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
  ```

### Summation
- Plain text: `sum from i=1 to n of x_i`
- LaTeX:
  ```latex
  \sum_{i=1}^{n} x_i
  ```

### Product
- Plain text: `product from i=1 to n of x_i`
- LaTeX:
  ```latex
  \prod_{i=1}^{n} x_i
  ```

### Fractions
- Plain text: `(a + b) / (c + d)`
- LaTeX:
  ```latex
  \frac{a + b}{c + d}
  ```

### Exponents and Subscripts
- Plain text: `x squared`, `x_i`
- LaTeX:
  ```latex
  x^2, x_i
  ```

---

## 2. **Probability and Statistics**

### Probability
- Plain text: `P(A)`, `P(A | B)`
- LaTeX:
  ```latex
  P(A), P(A \mid B)
  ```

### Expected Value
- Plain text: `E[X]`
- LaTeX:
  ```latex
  \mathbb{E}[X]
  ```

### Variance
- Plain text: `Var(X)`
- LaTeX:
  ```latex
  \text{Var}(X)
  ```

### Standard Deviation
- Plain text: `σ`
- LaTeX:
  ```latex
  \sigma
  ```

### Normal Distribution
- Plain text: `X ~ N(μ, σ²)`
- LaTeX:
  ```latex
  X \sim \mathcal{N}(\mu, \sigma^2)
  ```

---

## 3. **Linear Algebra**

### Dot Product
- Plain text: `u · v`
- LaTeX:
  ```latex
  \mathbf{u} \cdot \mathbf{v}
  ```

### Cross Product
- Plain text: `u × v`
- LaTeX:
  ```latex
  \mathbf{u} \times \mathbf{v}
  ```

### Matrix Multiplication
- Plain text: `A * B`
- LaTeX:
  ```latex
  \mathbf{A} \mathbf{B}
  ```

### Transpose
- Plain text: `A^T`
- LaTeX:
  ```latex
  \mathbf{A}^\top
  ```

### Inverse
- Plain text: `A^(-1)`
- LaTeX:
  ```latex
  \mathbf{A}^{-1}
  ```

### Determinant
- Plain text: `det(A)`
- LaTeX:
  ```latex
  \det(\mathbf{A})
  ```

---

## 4. **Calculus**

### Derivative
- Plain text: `df/dx`
- LaTeX:
  ```latex
  \frac{df}{dx}
  ```

### Partial Derivative
- Plain text: `∂f/∂x`
- LaTeX:
  ```latex
  \frac{\partial f}{\partial x}
  ```

### Integral
- Plain text: `∫ f(x) dx`
- LaTeX:
  ```latex
  \int f(x) \, dx
  ```

### Gradient
- Plain text: `∇f`
- LaTeX:
  ```latex
  \nabla f
  ```

### Hessian Matrix
- Plain text: `H(f)`
- LaTeX:
  ```latex
  \mathbf{H}(f)
  ```

---

## 5. **Machine Learning**

### Loss Function
- Plain text: `L(θ)`
- LaTeX:
  ```latex
  \mathcal{L}(\theta)
  ```

### Hypothesis
- Plain text: `h_θ(x)`
- LaTeX:
  ```latex
  h_\theta(x)
  ```

### Regularization
- Plain text: `λ ||θ||²`
- LaTeX:
  ```latex
  \lambda \|\theta\|^2
  ```

### Gradient Descent Update
- Plain text: `θ = θ - α ∇L(θ)`
- LaTeX:
  ```latex
  \theta = \theta - \alpha \nabla \mathcal{L}(\theta)
  ```

---

## 6. **Miscellaneous**

### Greek Letters
- Plain text: `α`, `β`, `γ`, `θ`, `μ`, `σ`
- LaTeX:
  ```latex
  \alpha, \beta, \gamma, \theta, \mu, \sigma
  ```

### Inequalities
- Plain text: `x > y`, `x ≤ y`
- LaTeX:
  ```latex
  x > y, x \leq y
  ```

### Set Notation
- Plain text: `x ∈ R`
- LaTeX:
  ```latex
  x \in \mathbb{R}
  ```

---

## 7. **Examples**

### Example 1: Linear Regression
- Plain text: `y = θ₀ + θ₁x₁ + θ₂x₂ + ... + θₙxₙ`
- LaTeX:
  ```latex
  y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n
  ```

### Example 2: Probability Density Function (PDF)
- Plain text: `f(x) = (1 / √(2πσ²)) * exp(-(x-μ)² / (2σ²))`
- LaTeX:
  ```latex
  f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right)
  ```

