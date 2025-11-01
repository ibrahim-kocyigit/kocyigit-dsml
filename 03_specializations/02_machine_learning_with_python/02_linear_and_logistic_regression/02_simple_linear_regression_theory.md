# Simple Linear Regression

## 1. The Intuitive Idea: Drawing the Best Straight Line

Simple Linear Regression is a supervised learning technique used to model the relationship between two variables by fitting a straight line to the observed data.

* **The Goal:** To use a **single independent variable** (feature) to predict a **single continuous dependent variable** (target).
* **The Analogy:** Imagine plotting your data on a scatter plot. Simple Linear Regression is the process of finding the one straight line that best "cuts through" the cloud of data points, capturing the general trend.

### Example: CO2 Emissions
* **Independent Variable (x):** `Engine Size`
* **Dependent Variable (y):** `CO2 Emissions`
* A scatter plot shows that as `Engine Size` increases, `CO2 Emissions` also tend to increase in a roughly linear fashion. Our goal is to find the line that best represents this relationship.

<img src="./images/0201.png" alt="Scatter plot with best-fit line" width="500"/>

## 2. The Mathematics of the Line

The relationship is modeled using the simple equation for a straight line:

$$ \hat{y} = \theta_0 + \theta_1 x_1 $$

Where:

*   $\hat{y}$ (y-hat) is the **predicted value** of the target variable. It's the value on the regression line for a given `x`.
*   $x_1$ is the single **independent variable** or feature (e.g., `Engine Size`).
*   $\theta_0$ is the **y-intercept** of the line. It's also known as the "bias." It's the predicted value of `y` when `x` is zero.
*   $\theta_1$ is the **slope** of the line. It's also known as the "coefficient" for the feature `x₁`. It represents the change in `y` for a one-unit increase in `x`.

The machine learning algorithm's job is to find the optimal values for the parameters $\theta_0$ and $\theta_1$ that create the "best-fit" line.

## 3. Key Assumptions and What to Do When They're Violated

For a simple linear regression model to be accurate and reliable, several assumptions about the data should be met. The best tool to check these is a simple **scatter plot** of the two variables.

1.  **Linearity:** The underlying relationship between the independent variable (`x`) and the dependent variable (`y`) is linear. The model can only capture a straight-line trend.
    > **What to do if it's violated?**
    > *   **Apply Transformations:** You can sometimes transform one or both variables (e.g., using a logarithm `log(x)` or square root `sqrt(x)`) to make the relationship linear.
    > *   **Use a Different Model:** If the relationship is clearly curved (e.g., a "U" shape), you need a more complex model, like **Polynomial Regression**.

2.  **Independence of Residuals:** The residuals (prediction errors) are independent. This means the error for one data point doesn't influence the error for another. This is mainly a concern for time-series data.
    > **What to do if it's violated?**
    > *   **Use Time-Series Models:** If your data is collected over time (e.g., daily stock prices), you should use models designed for sequential data, like ARIMA.

3.  **Homoscedasticity (Constant Variance):** The spread (or variance) of the residuals is constant across all values of the independent variable `x`.
    > **What to do if it's violated?**
    > *   **Look for a "Cone Shape":** If the scatter plot fans out like a cone or megaphone, you have **heteroscedasticity**. This means the model's predictions are less reliable for certain ranges of `x`.
    > *   **Transform the Target Variable:** A common fix is to apply a transformation to the dependent variable (`y`), such as taking its logarithm (`log(y)`) or square root, which can help stabilize the variance.

4.  **Normality of Residuals:** The residuals are normally distributed around the regression line. This is most important for statistical inference (e.g., calculating confidence intervals for the coefficients).
    > **What to do if it's violated?**
    > *   **Check for Outliers:** This is often caused by a few significant outliers.
    > *   **Don't Panic (with large datasets):** For larger datasets, this assumption is less critical for getting good coefficient estimates, thanks to the Central Limit Theorem.

## 4. How the Model is Trained: Ordinary Least Squares (OLS)

How does the algorithm find the best line? It aims to find the line that is "closest" to all the data points simultaneously. This is done by minimizing the prediction error.

### Residual Error
For any single data point, the residual is the **vertical distance** between the actual value (`y`) and the value predicted by the line (`ŷ`). It's the measure of our model's error for that one point.

`Error = Actual Value - Predicted Value`

### Mean Squared Error (MSE)
To find the total error for the whole dataset, we can't just average the residuals (because positive and negative errors would cancel out). Instead, we square each residual and then calculate the average. This is the **Mean Squared Error (MSE)**.

### Ordinary Least Squares (OLS)
The goal of the linear regression algorithm is to find the specific values of $\theta_0$ and $\theta_1$ that **minimize the MSE**. This method is called **Ordinary Least Squares (OLS)**. For simple linear regression, this can be solved directly with formulas.

#### Step 1. Calculate the Slope ($\theta_1$)

$$ \theta_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} $$

#### Step 2. Calculate the Intercept ($\theta_0$)

$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$

Where $\bar{x}$ and $\bar{y}$ are the mean (average) values of the `x` and `y` variables, respectively.

## 5. Model-Specific Considerations
Simple Linear Regression has no major model-specific considerations like handling categorical variables, as it only works with a single numerical input. Its primary advantage is its simplicity.

*   **No Hyperparameter Tuning:** The OLS solution is calculated directly from the data; there are no complex parameters to tune.
*   **Fast:** It is computationally inexpensive, making it a great first model to try.

## 6. Common Pitfalls: Sensitivity to Outliers

The biggest pitfall of Simple Linear Regression is its **sensitivity to outliers**.

*   **What it is:** An outlier is a data point that is very far away from the general cloud of points.
*   **The Consequence:** Because OLS minimizes *squared* errors, a single outlier will have a huge squared error. This can dramatically pull the best-fit line towards the outlier, skewing the slope and intercept and making the model a poor representation of the overall trend.
*   **The Solution:**
    *   First, investigate the outliers. Are they data entry errors? If so, correct or remove them.
    -   If they are genuine but extreme values, you might report your model's results both with and without the outliers to show their impact.
    -   Consider using a more robust regression model that is less sensitive to outliers.

## 7. Summary
*   Simple Linear Regression models the relationship between **one feature** and **one continuous target** by fitting a straight line.
*   The goal is to find the line that **minimizes the Mean Squared Error (MSE)**. This is achieved using the **Ordinary Least Squares (OLS)** method.
*   For OLS to be reliable, the data should satisfy key assumptions, primarily a **linear relationship** and **homoscedasticity**.
*   The method is fast and interpretable but can only model linear trends and is highly **sensitive to outliers**.

---

**Next:** [Simple Linear Regression Implementation](./03_simple_linear_regression_implementation.py)