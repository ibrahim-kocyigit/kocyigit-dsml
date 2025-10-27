# Multiple Linear Regression

## 1. The Intuitive Idea: From a Line to a Plane (and Beyond)

Simple Linear Regression is great, but it's limited to using only *one* feature to make predictions. The real world is more complex. **Multiple Linear Regression** is the natural extension of this idea, allowing us to use **two or more independent variables** (features) to predict a single continuous target variable.

* **Simple Linear Regression:** Finds the best-fit *line* through the data in two dimensions.
* **Multiple Linear Regression:**  
    * With two features, it finds the best-fit *plane* in three dimensions.
    * With more than two features, it finds the best-fit *hyperplane* in higher-dimensional space.

The goal is the same: to model the linear relationship between our features and the target, but now we can leverage more information to make a better decision.

## 2. The Mathematics: A Linear Combination

The equation for multiple linear regression is a straightforward extension of the simple version. It's a linear combination of all the features.

$$ \hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n $$

Where:
*   $\hat{y}$ is the **predicted value** of the target.
*   $x_1, x_2, \dots, x_n$ are the **independent variables** (features).
*   $\theta_0$ is the **y-intercept** (or bias).
*   $\theta_1, \theta_2, \dots, \theta_n$ are the **coefficients** (or weights) for each feature. Each $\theta_i$ represents the change in $\hat{y}$ for a one-unit increase in the corresponding feature $x_i$, assuming all other features are held constant.