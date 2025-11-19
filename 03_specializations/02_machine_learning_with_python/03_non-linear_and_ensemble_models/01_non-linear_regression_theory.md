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

### 2.2. Algorithmic Approaches: Decision Trees, SVMs, etc.
These are models that are inherently capable of capturing non-linear patterns without requiring manual feature transformation.

* **Decision Tree Regression:** Works by recursively splitting the data into smaller segments and predicting the average value for each segment. The resulting "curve" is actually a step function, which can approximate any shape.
* **Support Vector Machines (SVM) with Kernels:** An SVM can be used for regression (SVR). By using a non-linear "kernel" (like the Radial Basis Function or RBF kernel), it can find a best-fit curve in a higher dimensional space.
* **Neural Networks:** These models, composed of interconnected "neurons" with non-linear activation functions, are universal function approximators. They can learn extremely complex and intricate non-linear relationships, given enough data.

## 3. Key Assumptions (General Principles)
Since this is a category of models, there is no single set of assumptions. However, some general principles apply:

1. **No Assumed Functional Form:** Unlike linear regression, most true non-linear models (like Decision Trees of Neural Networks) do not assume a specific mathematical relationship (like a line or a parabola) between the features and the target. They learn the relationship directly from the data.
2. **Independence of Residuals:** This assumption still generally holds, especially for non-time-series data. The error for one prediction should not be correlated with the error for another.
3. **Homoscedasticity is Still Desirable:** While some models are more robust to non-constant variance (heteroscedasticity) than linear regression, having a consistent error variance across the feature space is still a sign of a well-behaved model.

## 4. How the Models are Trained
Training methods vary widely depending on the model:

* **Polynomial Regression:** Trained using Ordinary Least Squares (OLS) or Gradient Descent, just like Multiple Linear Regression.
* **Decision Trees:** Trained using a greedy, recursive partitioning algorithm that seeks to minimize the variance or Mean Squared Error (MSE) within each leaf node.
* **Support Vector Regression (SVR):** Trained by finding a curve that has the maximum number of data points within a specified margin or "tube" around it, while balancing this with error minimization.
* **Neural Networks:** Trained using Gradient Descent (often with advanced optimizers like Adam) to minimize a cost function like MSE by adjusting the weights of the network's connections.

## 5. Model-Specific Considerations
Choosing the right non-linear model involves understanding their trade-offs:

* **Interpretability vs. Performance:** A **Decision Tree** is highly interpretable (you can see the splits), while a **Neural Network** is often a "black box" but can achieve higher performance on very complex tasks. **Polynomial Regression** lies somewhere in between.
* **Hyperparameter Tuning:** Non-linear models often have critical hyperparameters that need to be tuned.
    * **Polynomial Regression:** The `degree` of the polynomial.
    * **Decision Trees:** The `max_depth` or `min_samples_leaf`.
    * **SVR:** The `C` (regularization) and `gamma` (kernel coefficient) parameters.
    * **Neural Networks:** The number of layers, number of neurons, learning rate, etc.

## 6. Common Pitfalls: The Danger of Overfitting
The single biggest risk with all non-linear models is **overfitting**. Because these models are so flexible, they have the power to "memorize" the training data, including its random noise.

* **What it is:** The model learns the training data too well, capturing noise instead of the underlying signal.
* **The Consequence:** The model performs brilliantly on the training data but fails to generalize to new, unseen data, making it useless in practice.
* **The Solution:**  
    * **Keep it Simple:** Start with a simpler model (or lower complexity) first.
    * **Use a Test Set:** Always evaluate your final model on a held-out test set. A large gap between training performance and test performance is a clear sign of overfitting. 
    * **Cross Validation:** Use cross-validation during hyperparameter tuning to get a robust estimate of the model's generalization performance.
    * **Regularization:** Use techniques that penalize model complexity, such as Ridge/Lasso for polynomial models or pruning for decision trees.

## 7. Summary
* **Non-linear Regression:** is a category of models used when the relationship between features and a target is curved, not a straight line.
* There are different approaches, including transforming features (**Polynomial Regression**) or using inherently non-linear algorithms (**Decision Trees, SVMs, Neural Networks**).
* These models are powerful and flexible but come with a high risk of **overfitting**.
* Choosing the right model involves a trade-off between **performance** and **interpretability**.
* Rigorous evaluation using a **test set** and **cross-validation** is essential to prevent overfitting and build a model that generalizes well.

---

**Next:** [Classification Theory](./02_classification_theory.md)