# Feature Engineering and Variable Transformation: Background

Welcome to the next section of the course! Here, we'll cover **feature engineering** and **variable transformation**—key steps before moving on to modeling.

## Why Feature Engineering and Transformation?

- After retrieving, cleaning, and exploring your data, raw features often need adjustment to optimize model performance.
- Many machine learning models make assumptions about the data (e.g., linear relationships in linear regression).
- Transforming variables (e.g., log transformation) can help with issues like outliers and non-normal distributions.

## Feature Encoding

- All model inputs must be numerical.
- Categorical data must be encoded (e.g., one-hot encoding, label encoding) before being used in models.

## Feature Scaling

- Real-world data features often have different scales (e.g., income in thousands, age in years).
- Scaling features (e.g., normalization, standardization) is important for many algorithms to perform well.

## Example: Linear Regression Assumptions

Linear regression assumes a linear relationship between predictors (features) and the target variable.

**Example model:**  

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2
$$

- $x_1$: cast budget  
- $x_2$: marketing budget  
- $y$: box office returns  
- $\beta_0, \beta_1, \beta_2$: parameters learned by the model

If the relationship is not linear, we can transform features (e.g., log, square root) to better fit model assumptions.

## Key Takeaway

- Feature engineering and transformation are essential steps to prepare your data for modeling and to ensure your models can learn effectively from the data.

---

**Next:** [Variable Transformation](./05_variable_transformation.md)