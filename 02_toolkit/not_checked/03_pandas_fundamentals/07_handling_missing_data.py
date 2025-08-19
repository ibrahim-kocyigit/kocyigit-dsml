# 07_handling_missing_data.py

import pandas as pd
import numpy as np
import os

# =======================================
# 1. INTRODUCTION AND SETUP
# =======================================
# - Real-world data is often messy and contains missing values.
# - Pandas represents missing values as `np.nan` (Not a Number).
# - Most calculations and machine learning algorithms cannot handle missing values,
#   so they must be identified and handled first.

# --- Load the sample dataset ---
DATA_FOLDER = "pandas_data"
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")

try:
    df_clean = pd.read_csv(file_path)
    # --- For this lesson, we will programmatically create a "messy" DataFrame ---
    df = df_clean.copy()
    # Introduce some np.nan values for demonstration
    df.loc[2, 'Price'] = np.nan
    df.loc[4, 'Category'] = np.nan
    df.loc[5, 'Price'] = np.nan
    df.loc[5, 'Quantity'] = np.nan

    print("--- Messy DataFrame with Missing Values (NaN) ---")
    print(df)

except FileNotFoundError:
    print(f"Error: The data file was not found at '{file_path}'")
    print("Please run '04_reading_and_writing_data.py' first to create it.")
    df = pd.DataFrame() # Create an empty df to avoid further errors

print("-" * 30)


# =======================================
# 2. FINDING MISSING DATA
# =======================================
# - Pandas provides easy methods to check for the presence of `NaN`.
if not df.empty:
    print("--- Finding Missing Data ---")

    # --- `.isnull()` or `.isna()` ---
    # These return a boolean DataFrame of the same shape.
    print("Boolean mask from .isnull():\n", df.isnull())

    # --- `.isnull().sum()` ---
    # This is a very common idiom to count missing values in each column.
    print("\nSum of missing values per column:\n", df.isnull().sum())

    # --- Filtering for rows with missing data ---
    # Find all rows where 'Price' is null.
    missing_price_rows = df[df['Price'].isnull()]
    print("\nRows where 'Price' is missing:\n", missing_price_rows)
    print("-" * 30)


# =======================================
# 3. HANDLING MISSING DATA: DROPPING
# =======================================
# - The simplest strategy is to drop rows or columns with missing values.
# - Be careful, as this can lead to significant data loss.
if not df.empty:
    print("--- Dropping Missing Data with .dropna() ---")
    print("Original shape:", df.shape)

    # --- Drop any ROW containing at least one `NaN` (default behavior) ---
    df_dropped_rows = df.dropna()
    print("\nDataFrame after dropping any row with NaN:\n", df_dropped_rows)
    print("Shape after dropping rows:", df_dropped_rows.shape)

    # --- Drop any COLUMN containing at least one `NaN` ---
    df_dropped_cols = df.dropna(axis=1)
    print("\nDataFrame after dropping any column with NaN:\n", df_dropped_cols)
    print("Shape after dropping columns:", df_dropped_cols.shape)
    print("-" * 30)


# =======================================
# 4. HANDLING MISSING DATA: FILLING
# =======================================
# - Filling (or "imputing") missing values is often preferred over dropping them.
if not df.empty:
    print("--- Filling Missing Data with .fillna() ---")

    # --- Strategy 1: Fill with a scalar value (e.g., 0) ---
    df_filled_zero = df.fillna(0)
    print("DataFrame after filling all NaNs with 0:\n", df_filled_zero)


    # --- Strategy 2: Fill with a calculated value (e.g., the mean) ---
    # This is a very common strategy for numerical columns.
    df_filled_mean = df.copy() # Work on a copy
    price_mean = df_filled_mean['Price'].mean()
    print(f"\nCalculated mean price: {price_mean:.2f}")
    df_filled_mean['Price'] = df_filled_mean['Price'].fillna(price_mean)
    print("DataFrame after filling missing Prices with the mean:\n", df_filled_mean)


    # --- Strategy 3: Forward Fill (`ffill`) ---
    # This propagates the last valid observation forward. Useful for time-series data.
    df_ffill = df.copy()
    df_ffill['Price'] = df_ffill['Price'].fillna(method='ffill')
    print("\nDataFrame after forward-filling 'Price':\n", df_ffill)


    # --- Strategy 4: Filling different columns with different values ---
    fill_values = {'Category': 'Unknown', 'Quantity': 0}
    df_filled_specific = df.fillna(value=fill_values)
    print("\nDataFrame after filling specific columns with different values:\n", df_filled_specific)

# --- End of File ---