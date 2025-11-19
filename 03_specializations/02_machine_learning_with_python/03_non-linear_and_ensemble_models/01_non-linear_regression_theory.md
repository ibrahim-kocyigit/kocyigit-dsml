# Non-linear Regression 

## 1. The Intuitive Idea: Modeling the Curves of the Real World

We've established that Linear Regression is a powerful tool for modeling straight-line relationships. However, many real-world phenomena are not linear. As one variable increases, the other might increase at an accelerating rate, level off, or follow a complex wave-like pattern.

**Non-linear Regression** is the broad category of techniques used to model these more complex, curved relationships between features and a target variable. Instead of fitting a single best-fit line, the goal is to fit a curve that accurately captures the nuances of the data.

<img src="./images/1401.png" alt="A non-linear relationship" width="600"/>

## 2. Common Approaches to Non-linear Regression

"Non-linear Regression" is not a single algorithm but a class of them. There are several distinct approaches to solving this problem:

### 2.1. Feature Transformation: Polynomial Regression
This is the simplest approach. We create new, non-linear features from our existing ones (e.g., $x^2, x^3$) and then fit a standard **Multiple Linear Regression** model to these new features. Although the resulting curve is non-linear with respect to the original feature, the model is still *linear in its parameters*, making it a special case.

*   **How it Works:** Transforms the feature space.
*   **Pros:** Easy to implement, leverages the simplicity of linear models.
*   **Cons:** Prone to overfitting with high degrees, not suitable for all curve shapes.
*   **See also:** [Polynomial Regression Theory](./08_polynomial_regression_theory.md)

### 2.2. Algorithmic Approaches: Decisio Trees, SVMs, etc.
These are models that are inherently capable of capturing non-linear patterns without requiring manual feature transformation.

**Decision Tree Regression:** Works by recursively splitting