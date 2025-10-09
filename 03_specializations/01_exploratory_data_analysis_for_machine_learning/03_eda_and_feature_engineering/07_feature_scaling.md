# Feature Scaling

## Why Scale Features?

- Real-world datasets often have features on very different scales (e.g., price: 0–10, stores: 10,000–50,000).
- Algorithms that rely on distance (like K-Nearest Neighbors) or gradient-based optimization can be biased by features with larger scales.
- Scaling brings features to a comparable range, ensuring fair contribution to the model.

## Example

- Imagine we are using KNN model. If one feature (e.g., age) is measured in seconds and another (e.g., number of surgeries) is a small integer, the large-scale feature will dominate distance calculations.
- Scaling ensures both features influence the model appropriately.

## Common Scaling Methods

### 1. Standard Scaling (Z-score)

- Subtract the mean and divide by the standard deviation.
- Centers data at 0 with unit variance.
- Sensitive to outliers.
    ```python
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)
    ```

### 2. Min-Max Scaling

- Scales all values to the [0, 1] range.
- Subtract the minimum, divide by (max - min).
- Highly sensitive to outliers.
    ```python
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data)
    ```

### 3. Robust Scaling

- Uses the median and interquartile range (IQR) instead of mean and standard deviation.
- More robust to outliers.
    ```python
    from sklearn.preprocessing import RobustScaler
    scaler = RobustScaler()
    scaled = scaler.fit_transform(data)
    ```

## Key Takeaways

- Feature scaling is essential for many machine learning algorithms.
- Choose the scaling method based on your data and sensitivity to outliers:
  - **StandardScaler:** Good for normal distributions, sensitive to outliers.
  - **MinMaxScaler:** Good for bounded data, very sensitive to outliers.
  - **RobustScaler:** Good for data with outliers.

---

**Next:** [Common Variable Transformations in Python](./08_common_variable_transformations_in_python.md)