# Classification with a Perceptron: Calculating Derivatives

We now know that our goal is to find the optimal weights and bias for our classification perceptron by minimizing the **log-loss** function using **Gradient Descent**.

To do this, we need to calculate the partial derivatives of the loss `L` with respect to each of our model's parameters: `w₁`, `w₂`, and `b`.

Let's trace how a change in a single weight, like `w₁`, affects the final loss. It's not a direct relationship; there is a chain of dependencies.

$$ w_1 \quad \longrightarrow \quad z \quad \longrightarrow \quad \hat{y} \quad \longrightarrow \quad L $$

* A change in `w₁` affects the summation `z`.
* A change in `z` affects the sigmoid output `ŷ`.
* A change in `ŷ` affects the final loss `L`.

To find the overall effect of `w₁` on `L`, we can use the **chain rule**.

## Breaking Down the Derivatives with the Chain Rule

We can break down our complex problem into smaller, simpler derivatives:
* $\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w_1}$  

* $\frac{\partial L}{\partial w_2} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w_2}$  

* $\frac{\partial L}{\partial b} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial b}$

Our task is to find each of these individual components and multiply them together.

## Calculating the Component Derivatives

**Reference Formulas:**
* **Log-Loss:** $L(y, \hat{y}) = -[y \ln(\hat{y}) + (1-y) \ln(1-\hat{y})]$
* **Prediction:** $\hat{y} = \sigma(z)$
* **Summation:** $z = w_1x_1 + w_2x_2 + b$

**1. Derivative of Loss w.r.t. Prediction ($\frac{\partial L}{\partial \hat{y}}$):**
Taking the derivative of the log-loss function with respect to `ŷ` gives:

$$ \frac{\partial L}{\partial \hat{y}} = - \left[ \frac{y}{\hat{y}} - \frac{1-y}{1-\hat{y}} \right] = \frac{\hat{y}-y}{\hat{y}(1-\hat{y})} $$

**2. Derivative of Prediction w.r.t. Summation ($\frac{\partial \hat{y}}{\partial z}$):**
This is the derivative of the sigmoid function, which we already know has a beautiful form:

$$ \frac{\partial \hat{y}}{\partial z} = \sigma'(z) = \sigma(z)(1-\sigma(z)) = \hat{y}(1-\hat{y}) $$

**3. Derivatives of Summation w.r.t. Parameters:**
These are simple partial derivatives:

* $\frac{\partial z}{\partial w_1} = x_1$  

* $\frac{\partial z}{\partial w_2} = x_2$  

* $\frac{\partial z}{\partial b} = 1$


## Assembling the Final Gradient

Now we can multiply our components together. Let's start with the derivative with respect to `w₁`.

$$ \frac{\partial L}{\partial w_1} = \underbrace{\left(\frac{\hat{y}-y}{\hat{y}(1-\hat{y})}\right)}_{\frac{\partial L}{\partial \hat{y}}} \cdot \underbrace{(\hat{y}(1-\hat{y}))}_{\frac{\partial \hat{y}}{\partial z}} \cdot \underbrace{(x_1)}_{\frac{\partial z}{\partial w_1}} $$

Notice the beautiful cancellation! The denominator `ŷ(1-ŷ)` cancels out perfectly with the derivative of the sigmoid function.

$$ \frac{\partial L}{\partial w_1} = (\hat{y}-y)x_1 $$

The same cancellation happens for the other two parameters.

**The Final Gradient Components:**

* $\frac{\partial L}{\partial w_1} = (\hat{y}-y)x_1$  

* $\frac{\partial L}{\partial w_2} = (\hat{y}-y)x_2$  

* $\frac{\partial L}{\partial b} = (\hat{y}-y)$

The term `(ŷ - y)` is simply the **error** in our prediction. The derivative is just the error, scaled by the corresponding input. If the error is small, the derivatives are small, and the weights don't need to change much.

## The Final Gradient Descent Step

We can now write out the complete update rules for a single step of gradient descent for our classification perceptron.

* $w_1 \leftarrow w_1 - \alpha \cdot ((\hat{y}-y)x_1)$
* $w_2 \leftarrow w_2 - \alpha \cdot ((\hat{y}-y)x_2)$
* $b \leftarrow b - \alpha \cdot (\hat{y}-y)$

By repeating these simple update steps, the algorithm will find the optimal weights and bias for our classification problem.



---

**Next:** [Classification with a Neural Network: Introduction](./08_classification_with_a_neural_network--introduction.md)
