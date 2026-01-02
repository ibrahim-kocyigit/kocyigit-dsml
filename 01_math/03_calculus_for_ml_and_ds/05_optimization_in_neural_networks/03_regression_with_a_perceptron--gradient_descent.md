# Regression with a Perceptron: Gradient Descent

Now we know our goal: find the optimal weights (`w₁`, `w₂`) and bias (`b`) that minimize our **loss function**, $L(y, \hat{y}) = \frac{1}{2}(y - \hat{y})^2$. In other words, we want to find the model that makes the smallest mistakes.

To do this, we will use **Gradient Descent**. The algorithm starts with random values for the weights and bias and iteratively updates them by taking small steps in the direction that most steeply decreases the loss.

The update rules for our three parameters are:

* $w_{1, new} = w_{1, old} - \alpha \cdot \frac{\partial L}{\partial w_1}$  

* $ w_{2, new} = w_{2, old} - \alpha \cdot \frac{\partial L}{\partial w_2} $  

* $ b_{new} = b_{old} - \alpha \cdot \frac{\partial L}{\partial b} $

To use these formulas, we first need to calculate the three partial derivatives of the loss function.

## Breaking Down the Derivatives with the Chain Rule

This looks complicated, but we can simplify it using the **chain rule**. The loss `L` is not directly a function of the weights and bias. Instead, `L` depends on the prediction `ŷ`, which in turn depends on the weights and bias.

This creates a chain of dependencies:

$$ w_1, w_2, b \quad \longrightarrow \quad \hat{y} \quad \longrightarrow \quad L $$

We can use the chain rule to find the derivatives we need:

* $ \frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w_1} $  

* $ \frac{\partial L}{\partial w_2} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w_2} $  

* $ \frac{\partial L}{\partial b} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial b} $

Now, our problem is much simpler. We just need to calculate the four individual component derivatives.

## Calculating the Component Derivatives

**Reference Formulas:**
* **Loss Function:** $ L(y, \hat{y}) = \frac{1}{2}(y - \hat{y})^2 $
* **Prediction Function:** $ \hat{y} = w_1x_1 + w_2x_2 + b $

**1. Derivative of Loss with respect to Prediction ($\frac{\partial L}{\partial \hat{y}}$):**
Using the chain rule, the derivative of $\frac{1}{2}(\text{something})^2$ is just the "something," multiplied by the derivative of the inside with respect to `ŷ`.

$$ \frac{\partial L}{\partial \hat{y}} = \frac{1}{2} \cdot 2(y - \hat{y}) \cdot (-1) = -(y - \hat{y}) $$

**2. Derivative of Prediction with respect to Bias ($\frac{\partial \hat{y}}{\partial b}$):**
When differentiating with respect to `b`, the terms `w₁x₁` and `w₂x₂` are treated as constants, so their derivative is zero.
$$ \frac{\partial \hat{y}}{\partial b} = 0 + 0 + 1 = 1 $$

**3. Derivative of Prediction with respect to Weight 1 ($\frac{\partial \hat{y}}{\partial w_1}$):**
When differentiating with respect to `w₁`, the term `w₂x₂ + b` is a constant. The derivative of `w₁x₁` with respect to `w₁` is just `x₁`.
$$ \frac{\partial \hat{y}}{\partial w_1} = x_1 $$

**4. Derivative of Prediction with respect to Weight 2 ($\frac{\partial \hat{y}}{\partial w_2}$):**
Similarly, the derivative with respect to `w₂` is `x₂`.
$$ \frac{\partial \hat{y}}{\partial w_2} = x_2 $$

---
## Assembling the Final Gradient

Now we can plug these simple components back into our chain rule formulas.

* $ \frac{\partial L}{\partial b} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial b} = -(y - \hat{y}) \cdot 1 = -(y - \hat{y}) $  

* $ \frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w_1} = -(y - \hat{y}) \cdot x_1 $  

* $ \frac{\partial L}{\partial w_2} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w_2} = -(y - \hat{y}) \cdot x_2 $

These are the three partial derivatives that form our gradient.

---
## The Final Gradient Descent Step

We can now write out the complete update rules for a single step of gradient descent for linear regression.

* $ w_1 \leftarrow w_1 - \alpha \cdot (-(y - \hat{y}) \cdot x_1) = w_1 + \alpha (y - \hat{y}) x_1 $  

* $ w_2 \leftarrow w_2 - \alpha \cdot (-(y - \hat{y}) \cdot x_2) = w_2 + \alpha (y - \hat{y}) x_2 $  

* $ b \leftarrow b - \alpha \cdot (-(y - \hat{y})) = b + \alpha (y - \hat{y}) $

By repeating these update steps many times for all the points in our dataset, the algorithm will find the optimal weights `w₁`, `w₂`, and bias `b` that result in the smallest possible error and therefore the best possible model.

