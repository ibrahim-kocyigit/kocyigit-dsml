# Handling Missing Values and Outliers Using Residuals

## What are Residuals?

- **Residual:** The difference between the actual value and the predicted value from your model.
  - Residuals represent where the model fails to predict accurately.
  - Useful for detecting outliers after fitting a model.

## Approaches for Using Residuals to Detect Outliers

1. **Standardized Residuals**
   - Residual divided by the standard error.
   - Standardizes the residuals so you can compare them across different scales of outcome variables.
   - Helps identify outliers regardless of the range of the target variable.

2. **Deleted Residuals**
   - Remove an observation from the dataset, refit the model, and see how the prediction changes.
   - If removing a point causes a large change, that point may be an influential outlier.

3. **Studentized Residuals (Externally Studentized)**
   - Like deleted residuals, but also standardized.
   - Remove an observation, refit the model, calculate the residual, and standardize it.
   - Provides a more robust measure for identifying outliers.

## What to Do After Detecting Outliers

- **Remove the outlier:**  
  - Eliminates its effect, but you may lose important information (entire row).
- **Assign a different value:**  
  - Replace the outlier with a more reasonable value, but may lose the original information.
- **Transform the feature:**  
  - Apply a transformation (e.g., log) to reduce the impact of outliers.
- **Predict the value:**  
  - Use similar observations or regression to estimate what the value should have been.
  - More complex, may require more data and effort.
- **Keep the outlier:**  
  - Use models that are robust to outliers (to be discussed in later courses).

## Recap

- Residuals help identify outliers after modeling.
- Several strategies exist for handling outliers: removal, replacement, transformation, prediction, or keeping them.
- Data cleaning is essential for building reliable models.

---

**Next:** [Introduction to Exploratory Data Analysis](../03_eda_and_feature_engineering/01_introduction_to_exploratory_data_analysis.md)