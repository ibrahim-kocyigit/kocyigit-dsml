# Handling Missing Values and Outliers

## Handling Missing Data

- **Models cannot handle blank values**—every feature and label must have information.
- **Options for handling missing data:**
  1. **Remove rows (or columns) with missing values**
     - **Pros:** Quick and simple; no need to guess replacement values.
     - **Cons:** If many rows are removed, you may lose too much data or introduce bias (if missingness is not random).
  2. **Impute missing values**
     - Replace nulls with the mean, median, or a more complex estimate.
     - **Pros:** Retains all rows/columns, preserving data for modeling.
     - **Cons:** Introduces uncertainty, as imputed values are only estimates.
  3. **Mask missing values as their own category**
     - Treat missingness as potentially informative (e.g., survey question left blank may indicate something meaningful).
     - **Pros:** No data loss; missingness itself may be useful.
     - **Cons:** Assumes all missing values are similar, which may not be true; adds uncertainty.

- **Best practice:**  
  - Assess your dataset and choose the method that best fits the context and the nature of your missing data.

## Handling Outliers

- **Outlier:** An observation that is very different from most others (e.g., sales values of 10–50, but one week is 3,000).
- **Impact:** Outliers can skew model predictions and affect averages, especially in small datasets.
- **Not all outliers are bad:** Some may provide valuable insights—investigate before removing.

## Detecting Outliers

- **Visualization:**
  - **Histogram / Density Plot:** See the distribution and spot unusual values.
    ```python
    import seaborn as sns
    sns.displot(data, bins=30)
    ```
  - **Box Plot:** Shows median, interquartile range (IQR), and outliers.
    ```python
    sns.boxplot(x=data)
    ```

- **Mathematical Approach (IQR method):**
    ```python
    import numpy as np

    q25 = np.percentile(data, 25)
    q75 = np.percentile(data, 75)
    iqr = q75 - q25
    min_val = q25 - 1.5 * iqr
    max_val = q75 + 1.5 * iqr
    outliers = [x for x in data if x < min_val or x > max_val]
    ```
  - Values outside `[min_val, max_val]` are considered outliers.

- **Other methods:**  
  - Use residuals (standardized, deleted, studentized) for more advanced outlier detection (More on this in our next lesson).

---

**Next:** [Handling Missing Values and Outliers Using Residuals](./05_handling_missing_values_and_outliers_using_residuals.md)