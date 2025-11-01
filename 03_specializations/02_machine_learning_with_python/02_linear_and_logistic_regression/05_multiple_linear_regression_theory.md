# Multiple Linear Regression

## 1. The Intuitive Idea: From a Line to a Plane (and Beyond)

Simple Linear Regression is great, but it's limited to using only *one* feature to make predictions. The real world is more complex. **Multiple Linear Regression** is the natural extension of this idea, allowing us to use **two or more features** to predict a continuous target variable.

- **Simple Linear Regression:** Finds the best-fit *line* through the data in two dimensions.
- **Multiple Linear Regression:**  
    - With two features, it finds the best-fit *plane* in three dimensions.
    - With more than two features, it finds the best-fit *hyperplane* in higher-dimensional space.

**The goal** is the same: To model the linear relationship between our features and the target, but now we can leverage more information to make a better, more nuanced decision.

## 2. The Mathematics: A Linear Combination

The equation for multiple linear regression is a straightforward extension of the simple version. It's a linear combination of all the features.  

$$
\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n
$$

...where:
*   $\hat{y}$ is the **predicted value** of the target.
*   $x_1, x_2, \dots, x_n$ are the **independent variables** (features).
*   $\theta_0$ is the **y-intercept** (or bias).
*   $\theta_1, \theta_2, \dots, \theta_n$ are the **coefficients** (or weights) for each feature. Each $\theta_i$ represents the change in $\hat{y}$ for a one-unit increase in the corresponding feature $x_i$, assuming all other features are held constant.

The machine learning algorithm's job is to find the optimal values for all the theta ($\theta$) parameters that best fit the data.

## 3. Key Assumptions of Multiple Linear Regression

For a multiple linear regression model to be accurate and reliable, several key assumptions about the data must be met. Violating these assumptions can lead to misleading or incorrect conclusions.

1.  **Linearity:** The underlying relationship between the independent variables and the dependent variable is linear. The model can only capture a linear trend, so if the true relationship is curved (non-linear), the model will be a poor fit.

2.  **Independence of Residuals:** The residuals (prediction errors) are independent. This means that the error of one prediction is not correlated with the error of another. This is often a concern in time-series data where consecutive observations might be related.

3.  **Homoscedasticity (Constant Variance):** The residuals have constant variance at every level of the independent variables. In other words, the spread of the errors should be consistent across all predicted values. If the spread increases or decreases (e.g., forming a cone shape in a residual plot), this is called **heteroscedasticity**, and it can make our coefficient estimates less reliable.

4.  **Normality of Residuals:** The residuals are normally distributed. This assumption is important for conducting statistical tests on the coefficients (e.g., determining their significance). While the model can still be predictive without this, the inferences about the coefficients may be invalid.

5.  **No Multicollinearity:** The independent variables are not highly correlated with each other. When two or more features are highly correlated, it becomes difficult for the model to determine the individual effect of each one. This makes the coefficient estimates unstable and hard to interpret. For example, you can't realistically determine the separate effects of `Engine Size` and `Number of Cylinders` if they always change together.

## 4. How the Model is Trained

Just like with simple linear regression, the goal is to find the parameters ($\theta$) that **minimize the Mean Squared Error (MSE)**. There are two primary methods to achieve this:

### 1. Ordinary Least Squares (OLS)

A direct, mathematical approach that uses linear algebra (matrix operations) on the entire dataset to calculate the single best set of coefficients. This is also known as the **Normal Equation**: 

$$
\theta = (X_b^T X_b)^{-1} X_b^T y
$$
    
...where $X_b$ is the feature matrix (with an added column of ones for the intercept $\theta_0$), and $y$ is the vector of target values.

**When to Use:** This method works well for smaller to medium-sized datasets where the computation is feasible.

### 2. Optimization Approach (e.g., Gradient Descent)
An iterative approach. It starts with random values for the coefficients and then repeatedly makes small adjustments to them, each time moving in the direction that reduces the model's error on the training data.

**Cost Function (MSE):**  This is the function we want to minimize:

$$
J(\theta) = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)})^2
$$

**Gradients:** The partial derivatives of the cost function, which tell us the direction of steepest ascent. We move in the opposite direction.

* For the bias/intercept ($\theta_0$):  

$$
\frac{\partial J}{\partial \theta_0} = - \frac{2}{n} \sum_{i=1}^{n} (y^{(i)} - \hat{y}^{(i)})
$$

* For any other coefficient ($\theta_j$ where $j > 0$):

$$
\frac{\partial J}{\partial \theta_j} = -\frac{2}{n} \sum_{i=1}^{n} (y^{(i)} - \hat{y}^{(i)}) x_j^{(i)}
$$

**Update Rule:** How we update the parameters in each iteration.

$$
\theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j}
$$

... where $\alpha$ is the learning rate.

**When to use:** Gradient descent is the preferred method for very large datasets where calculating the OLS solution directly would be too computationally expensive.

## 5. Handling Categorical Variables

Multiple Linear Regression requires all input features to be numerical. So what do we do with categorical variables like "Fuel Type" or "Transmission"? We convert them into numbers.

* **Binary Variables (2 categories):** Convert them into a single numerical feature with values of 0 and 1. This is called creating a **dummy variable**.
    * **Example:** For a `Transmission` feature, "Manual" could become 0 and "Automatic" could become 1.
* **Multi-Class Variables (>2 categories):** Convert them into multiple new boolean (0/1) features, one for each category. This technique is called **One-Hot Encoding**.   
    * **Example:** For a `FuelType` feature with classes "Gas", "Diesel", and "Electric", we would create three new features: `is_Gas`, `is_Diesel`, and `is_Electric`. A gasoline car would have a 1 in the `is_Gas` column and 0s in the others.

## 6. Common Pitfalls in Modeling

Beyond violating the core assumptions, a common challenge in building a multiple regression model is **overfitting**.

*   **What it is:** Adding too many features to your model can cause it to "memorize" the training data, including its noise and random fluctuations. While some features may seem to improve accuracy on the training set, they might not represent a real, underlying relationship.
*   **The Consequence:** The model will perform exceptionally well on the training data but will fail to generalize and make accurate predictions on new, unseen data.
*   **The Solution:** Careful and deliberate feature selection is crucial. Aim for a balanced set of features that are highly correlated with the target variable but uncorrelated with each other.

## 7. Summary

*   Multiple Linear Regression extends simple linear regression by using **two or more features** to predict a continuous target.
*   The model learns a **coefficient for each feature**, representing its independent contribution to the prediction.
*   For the model to be reliable, it must satisfy key assumptions: **linearity, independence, homoscedasticity, normality of residuals, and no multicollinearity**.
*   It's more powerful than simple linear regression but introduces risks like **overfitting** and **multicollinearity**.
*   Careful **feature selection** and handling of **categorical variables** are crucial steps in building a robust and interpretable model.

---

**Next:** [Multiple Linear Regression Implementation](./06_multiple_linear_regression_implementation.py)