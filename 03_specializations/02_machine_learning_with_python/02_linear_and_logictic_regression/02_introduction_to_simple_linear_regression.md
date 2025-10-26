# Introduction to Simple Linear Regression

## 1. The Intuitive Idea: Drawing the Best Straight Line

Simple Linear Regression is a supervised learning technique used to model the relationship between two variables by fitting a straight line to the observed data.

**The Goal:** To use a **single independent variable:** (feature) to predict a **single continuous dependent variable** (target).

**The Analogy:** Imagine plotting your data on a scatter plot. Simple Linear Regression is the process of finding the one straight line that best "cuts through" the cloud of data points, capturing the general trend.

**Example: CO2 Emissions:**
* **Independent Variable (x):** `Engine Size`
* **Dependent Variable (y):** `CO2 Emissions`
* A scatter plot shows that as `Engine Size` increases, `CO2 Emissions` also tend to increase in a roughly linear fashion. Our goal is to find the line that best represents this relationship.

<img src="./images/0201.png" alt="Scatter plot with best-fit line" width="500"/>

## 2. The Mathematics of the Line

The relationship is modeled using the simple equation for a straight line:

$$ \hat{y} = \theta_0 + \theta_1 x_1 $$

Where:

*   $ \hat{y} $ (y-hat) is the **predicted value** of the target variable. It's the value on the regression line for a given `x`.
*   $ x_1 $ is the single **independent variable** or feature (e.g., `Engine Size`).
*   $ \theta_0 $ is the **y-intercept** of the line. It's also known as the "bias." It's the predicted value of `y` when `x` is zero.
*   $ \theta_1 $ is the **slope** of the line. It's also known as the "coefficient" for the feature `x₁`. It represents the change in `y` for a one-unit increase in `x`.