import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# =======================================
# 1. WHY ENCODE CATEGORICAL DATA?
# =======================================
# - Machine learning algorithms are based on mathematical equations and can only
#   work with numerical data.
# - Categorical data, represented as text (e.g., 'Red', 'Green', 'Blue' or 'Söke',
#   'İzmir'), cannot be fed directly into the models.
# - Encoding is the process of converting these text-based categories into a
#   numerical format that the algorithm can understand.


# =======================================
# 2. CREATING A SAMPLE DATASET
# =======================================
# - Let's create a dataset with both nominal (no order) and ordinal (ordered) categories.
data = {
    "Color": ["Red", "Green", "Blue", "Green", "Red"],
    "Size": ["S", "M", "L", "M", "S"],  # Ordinal: S < M < L
    "City": ["İstanbul", "Ankara", "İzmir", "Ankara", "İstanbul"],  # Nominal
    "Price": [10.0, 20.0, 30.0, 25.0, 12.0],
}
df = pd.DataFrame(data)

print("--- Original Sample Data with Categorical Features ---")
print(df)
print("\nData types before encoding:\n", df.dtypes)
print("-" * 30)


# =======================================
# 3. METHOD 1: ONE-HOT ENCODING
# =======================================
# - This is the most common and robust method for nominal features (where categories have no order).
# - It creates new binary (0 or 1) columns for each unique category.
# - This avoids creating a false sense of order (e.g., it doesn't assume İzmir < İstanbul).

# --- Approach A: Scikit-Learn's `OneHotEncoder` ---
# - This is the preferred method when building a model pipeline.
print("--- One-Hot Encoding with Scikit-Learn ---")
# Select the nominal categorical columns to encode
nominal_cols = ["Color", "City"]
X_nominal = df[nominal_cols]

# 1. Instantiate the encoder
# `sparse_output=False` returns a standard NumPy array, which is easier to inspect.
ohe = OneHotEncoder(sparse_output=False)

# 2. Fit and transform the data
X_encoded = ohe.fit_transform(X_nominal)

# 3. Get the new feature names and create a DataFrame
new_col_names = ohe.get_feature_names_out(nominal_cols)
df_encoded = pd.DataFrame(X_encoded, columns=new_col_names)

print("Result of OneHotEncoder (as a new DataFrame):\n", df_encoded)


# --- Approach B: Pandas' `pd.get_dummies()` ---
# - A very convenient one-liner for a similar result. Great for exploratory analysis.
print("\n--- One-Hot Encoding with Pandas' get_dummies() ---")
# It automatically finds string columns and encodes them, then joins back to the original df.
df_dummies = pd.get_dummies(df, columns=["Color", "City"], dtype=int)
print("Result of pd.get_dummies():\n", df_dummies)
print("-" * 30)


# =======================================
# 4. A NOTE ON ORDINAL DATA (AND `LabelEncoder`)
# =======================================
# - Ordinal data has a meaningful order (e.g., S < M < L).
# - `LabelEncoder` converts each category to an integer (S->0, M->1, L->2).
# - WARNING: Using `LabelEncoder` on FEATURES is often DANGEROUS. Most models will
#   incorrectly assume a mathematical relationship (e.g., that L is twice as much as M).
# - The best way to handle ordinal features is to create an explicit mapping.

print("--- Handling Ordinal Data ---")
# --- The Correct Approach: Manual Mapping ---
size_mapping = {"S": 1, "M": 2, "L": 3}
df["Size_Encoded"] = df["Size"].map(size_mapping)
print("Correctly encoded ordinal data using a manual map:\n", df)


# --- When is `LabelEncoder` used? ---
# - `LabelEncoder` is primarily intended for encoding the TARGET VARIABLE (`y`)
#   in classification problems, not the input features (`X`).
y_target = df["Color"]
le = LabelEncoder()
y_encoded = le.fit_transform(y_target)
print("\nExample of LabelEncoder on a target variable 'y':")
print(f"Original target: {y_target.values}")
print(f"Encoded target:  {y_encoded}")
print(f"Classes learned by encoder: {le.classes_}")

# --- End of File ---
