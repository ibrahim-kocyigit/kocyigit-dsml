# Polynomial and Non-Linear Regression

## 1. The Intuitive Idea: Beyond the Straight Line

So far, we've focused on linear regression, which tries to fit a straight line to our data. However, real-world data is rarely so simple. Often, the relationship between our features and the target follows a curve. 

If we try to fit a straight line to data that is clearly curved, our model will be too simplistic and will make poor decisions. This is known as **underfitting**.

<img src="./images/0601.png" alt="Linear vs Non-linear fit" width="400"/>

**Non-Linear Regression** is a broad category of methods used to model these curved, non-linear relationships between variables.

## 2. Polynomial Regression: The "Linear" Trick

Polynomial regression is one of the simplest and most common ways to model non-linear relationships. Instead of fitting a straight line, we fit a polynomial curve (like a quadratic or cubic curve) to the data.

The model equation looks like this:  

$$ \hat{y} = \theta_0 + \theta_1 x + \theta_2 x^2 + \dots + \theta_n x^n $$

Where:
*   $\hat{y}$ is the predicted value.
*   $x$ is the original independent variable.
*   $x^2, x^3, \dots, x^n$ are the new polynomial features.
*   $n$ is the degree of the polynomial.

<img src="./images/0602.png" alt="" width="800"/>

### The Trick: Transforming it into a Linear Problem

How do we solve this? We can transform this into a **Multiple Linear Regression** problem with a clever trick: we treat each polynomial term as a *new, separate feature*.

Let's say we have a cubic model ($n=3$):  

$$ \hat{y} = \theta_0 + \theta_1 x + \theta_2 x^2 + \theta_3 x^3 $$

We can define new features:
*   $x_1 = x$
*   $x_2 = x^2$
*   $x_3 = x^3$

Now, our equation becomes:  

$$ \hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 $$

This is just a standard multiple linear regression equation! We can use the exact same `LinearRegression` model from scikit-learn to find the optimal coefficients ($\theta_0, \theta_1, \theta_2, \theta_3$). Because of this, polynomial regression is often considered a special case of linear regression.

### The Danger of Polynomial Regression: Overfitting

Given enough data points, you can always find a polynomial of a sufficiently high degree that passes perfectly through every single point. However, this is not a good thing.

**Overfitting** happens when the model becomes too complex and starts to "memorize" the training data, including its random noise and fluctuations, instead of learning the underlying trend.

<img src="./images/0603.png" alt="" width="500"/>

An overfit model will have an amazing score on the data it was trained on, but it will fail miserably at predicting new, unseen data. The goal is to find a curve that captures the general trend without being overly complex.

## 3. "True" Non-Linear Regression Models

While polynomial regression is powerful, some relationships can't be modeled effectively with polynomials. These require the "true" non-linear regression models, where the relationship between the parameters ($\theta$) and the feature is not linear.

These models cannot be solved with the simple OLS method. Instead, they require more advanced optimization algorithms (like Gradient Descent) to iteratively find the best parameters.

Common examples include:

* **Exponential Growth:** Describes phenomena that increase at an ever-faster rate.
    * **Example:** The growth of China's GDP from 1960 to 2014, or how an investment grows with compound interest.
    * **Model:** $\hat{y} = \theta_0 + \theta_1 e^{\theta_2 x}$
* **Logarithmic Growth:** Describes phenomena that exhibit diminishing returns, where growth slows down over time.
    * **Example:** The relationship between hours worked and productivity. The first few hours are highly productive, but each additional hour adds less and less benefit.
    * **Model:** $\hat{y} = \theta_0 + \theta_1 \log(x)$
* **Periodic (Sinusoidal) Patterns:** Describes cyclical or seasonal phenomena.
    * **Example:** Monthly average temperature or rainfall, which follows a yearly circle.
    * **Model:** $\hat{y} = \theta_0 + \theta_1 \sin(\theta_2 x + \theta_3)$

<img src="./images/0604.png" alt="" width="800"/>

## 4. How to Choose the Right Model
How do you know which type of regression to use?

1. **Visualize Your Data:** The first and most important step is to create a **scatter plot** of your target variable against your independent variable(s). Visually inspect the plot to see if the relationship looks linear, curved (polynomial), exponential, logarithmic, or something else entirely.
2. **Model and Evaluate:** Try fitting a few different types of models and compare their evaluation metrics (like R² and RMSE) on a held-out test set. The model that performs best on the *test set* is likely the best choice.
3. **Consider Other ML Models:** For very complex relationships, you might not be able to find a simple mathematical equation. In these cases, you can turn to more flexible machine learning models that can learn complex patterns automatically, such as:
    * k-Nearest Neighbours (KNN)
    * Support Vector Machines (SVM)
    * Decision Trees & Random Forests
    * Neural Networks

## 5. Summary
*   When the relationship between variables is not a straight line, we need **non-linear regression**.
*   **Polynomial Regression** is a common technique that fits a curved line by creating new polynomial features ($x^2, x^3$, etc.) and solving it as a multiple linear regression problem.
*   Be wary of **overfitting** when using high-degree polynomials. The goal is to capture the trend, not the noise.
*   Some relationships are inherently non-linear (e.g., **exponential**, **logarithmic**) and require specialized models and optimization techniques.
*   **Visualizing your data** with a scatter plot is the best first step to determine what kind of model might be appropriate.

---

**Next:** [Introduction to Logistic Regression](./07_introduction_to_logistic_regression.md)