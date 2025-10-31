# Polynomial Regression

## 1. The Intuitive Idea: When a Straight Line Isn't Enough

We've seen that Linear Regression is powerful, but it has a major limitation: it can only model a straight-line relationship. What happens when our data follows a curve?

<img src="./images/0801.png" alt="Linear vs Non-linear fit" width="500"/>

If we try to fit a linear model to data that is clearly curved, our model will be too simplistic and will make poor predictions. This is known as **underfitting**. 

**Polynomial Regression** is a powerful technique that allows us to use a linear model to fit non-linear data. Instead of fitting a straight line, we fit a polynomial curve (like a quadratic or cubic curve) that can better capture the underlying pattern.

## 2. The Mathematics: Creating New Features

The model equation for polynomial regression looks like this:

$$
\hat{y} = \theta_0 + \theta_1 x + \theta_2 x^2 + \dots + \theta_n x^n 
$$

...where:
* $\hat{y}$ is the predicted value.
* $x$ is the original independent variable.
* $x^2, x^3, \dots, x^n$ are the new polynomial features we create.
* $n$ is the **degree** of the polynomial, which determines the complexity of the curve.

<img src="./images/0802.png" alt="Polynomial degrees" width="800"/>

### The Trick: How We Solve It With Linear Regression

This looks like a non-linear equation, but here's the clever trick: we can transform this into a **Multiple Linear Regression** problem by treating each polynomial term as a *new, separate feature*.

Let's say we want to fit a cubic model (degree `n=3`):

$$
\hat{y} = \theta_0 + \theta_1 x + \theta_2 x^2 + \theta_3 x^3 
$$

We can define a new set of features:
* $x_1 = x$
* $x_2 = x^2$
* $x_3 = x^3$

Now, our equation becomes:

$$
\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3
$$

This is just a standard Multiple Linear Regression equation! We can use the exact same methods (Ordinary Least Squares or Gradient Descent) to find the optimal coefficients ($\theta_0, \theta_1, \theta_2, \theta_3$). The model is still **linear in its parameters**, even though it is modeling a **non-linear relationship** in the original feature space.

## 3. The Danger of High-Degree Polynomials: Overfitting
Given enough data points, you can always find a polynomial of sufficiently high degree that passes perfectly through every single point. However, this is not a good thing.

**Overfitting** happens when the model becomes too complex and starts to "memorize" the training data, including its random noise and fluctuations, instead of learning the underlying trend.

<img src="./images/0803.png" alt="Overfitting with a high-degree polynomial" width="500"/>

An overfit model will have an amazing score on the data it was trained on, but it will **fail miserably** at predicting new, unseen data. The goal is to find a polynomial degree that is complex enough to capture the general trend without being so complex that it models the noise.

## 4. How to Choose the Right Degree

1. **Visualize Your Data:** The first and most important step is to create a **scatter plot** of your target variable against your independent variable. A visual inspection will often give you a good sense of whether a quadratic (one bend), cubic (two bends), or a more complex curve is needed.
2. **Model and Evaluate:** Try fitting models with a few different degrees (e.g., 2, 3, 4) and compare their evaluation metrics (like R² and RMSE) on a held-out **test set**. The degree that performs best on the *test set* (not the training set) is likely the best choice.

## 5. Summary 
*   When the relationship between variables is not a straight line, we need a more flexible model.
*   **Polynomial Regression** fits a curved line by creating new polynomial features ($x^2, x^3$, etc.) and then solving it as a Multiple Linear Regression problem.
*   The **degree** of the polynomial is a critical hyperparameter that controls the complexity of the curve.
*   Be wary of **overfitting** when using high-degree polynomials. The goal is to capture the trend, not the noise.
*   **Visualizing your data** with a scatter plot is the best first step to determine if polynomial regression is appropriate.

---

**Next:** [Implementation: Polynomial Regression](./09_implementation--polynomial_regression.py)