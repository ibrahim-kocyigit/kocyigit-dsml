# Common Variable Transformations in Python

## 1. Continuous Numerical Features

- **Scaling Methods:**
  - **Standard Scaling:** Use `StandardScaler` from `sklearn.preprocessing`.
  - **Min-Max Scaling:** Use `MinMaxScaler` from `sklearn.preprocessing`.
  - **Robust Scaling:** Use `RobustScaler` from `sklearn.preprocessing`.

    ```python
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    ```

## 2. Nominal (Unordered Categorical) Features

- **Binary Encoding:** For two categories (e.g., True/False).
- **One-Hot Encoding:** For multiple categories (e.g., red, blue, green).
  - Use `LabelEncoder`, `LabelBinarizer`, `OneHotEncoder` from `sklearn.preprocessing`.
  - Or use `pd.get_dummies()` from pandas.

    ```python
    from sklearn.preprocessing import OneHotEncoder
    import pandas as pd

    # Using pandas
    dummies = pd.get_dummies(data['color'])

    # Using sklearn
    encoder = OneHotEncoder()
    encoded = encoder.fit_transform(data[['color']])
    ```

## 3. Ordinal (Ordered Categorical) Features

- **Ordinal Encoding:** Assign integers based on order (e.g., low=1, medium=2, high=3).
  - Use `OrdinalEncoder` from `sklearn.preprocessing`.
  - Or use `DictVectorizer` if you want to map specific values.

    ```python
    from sklearn.preprocessing import OrdinalEncoder

    encoder = OrdinalEncoder(categories=[['low', 'medium', 'high']])
    encoded = encoder.fit_transform(data[['rating']])
    ```

## Summary of Section

- **Feature Engineering & Variable Transformation:**  
  - Use polynomial and log transformations to create or adjust features for linear relationships.
- **Feature Encoding:**  
  - Use one-hot encoding for nominal data, ordinal encoding for ordered categories.
- **Feature Scaling:**  
  - Standardize or normalize continuous features to ensure comparability and improve model performance.
