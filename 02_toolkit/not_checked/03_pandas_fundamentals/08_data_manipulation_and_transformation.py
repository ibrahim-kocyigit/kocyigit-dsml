# 08_data_manipulation_and_transformation.py

import pandas as pd
import os

# =======================================
# 1. INTRODUCTION AND SETUP
# =======================================
# - After cleaning data, the next step is often to manipulate and transform it.
# - This can involve creating new columns (features), renaming existing ones for clarity,
#   applying custom functions, or reordering the data.

# --- Load the sample dataset ---
DATA_FOLDER = "pandas_data"
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")

try:
    df = pd.read_csv(file_path, parse_dates=['OrderDate'])
    print("--- Original Sales DataFrame ---")
    print(df.head())
except FileNotFoundError:
    print(f"Error: The data file was not found at '{file_path}'")
    print("Please run '04_reading_and_writing_data.py' first to create it.")
    df = pd.DataFrame() # Create an empty df to avoid further errors

print("-" * 30)


# =======================================
# 2. ADDING AND REMOVING COLUMNS
# =======================================
# - These are fundamental DataFrame manipulation tasks.
if not df.empty:
    print("--- Adding and Removing Columns ---")

    # --- Adding a New Column ---
    # A common task is to create a new column based on existing ones (feature engineering).
    # Let's create a 'TotalPrice' column.
    df['TotalPrice'] = df['Price'] * df['Quantity']
    print("DataFrame with new 'TotalPrice' column:\n", df.head())


    # --- Removing Columns with `.drop()` ---
    # The `.drop()` method is used to remove rows or columns.
    # To remove columns, we specify `columns=[list_of_columns]`.
    # By default, it returns a new DataFrame. Use `inplace=True` to modify the original.
    df_dropped = df.drop(columns=['Category', 'OrderDate'])
    print("\nDataFrame after dropping 'Category' and 'OrderDate' columns:\n", df_dropped.head())
    print("-" * 30)


# =======================================
# 3. APPLYING FUNCTIONS (`.map()` and `.apply()`)
# =======================================
# - These methods allow you to apply custom functions to your data.
if not df.empty:
    print("--- Applying Functions ---")

    # --- `.map()` - For mapping values in a Series ---
    # - Used to substitute each value in a Series, often with a dictionary.
    # Let's map the 'Category' strings to numerical IDs.
    category_mapping = {'Electronics': 1, 'Accessories': 2}
    df['Category_ID'] = df['Category'].map(category_mapping)
    print("DataFrame with new 'Category_ID' column from .map():\n", df.head())


    # --- `.apply()` - For applying a function to a Series or DataFrame ---
    # - More flexible than .map(). Can be used with lambda functions.
    # - Let's create a 'DiscountPrice' by applying a 10% discount function to the 'Price' column.
    def apply_discount(price):
        return price * 0.9

    df['DiscountPrice'] = df['Price'].apply(apply_discount)
    # Using a lambda function for the same result:
    # df['DiscountPrice'] = df['Price'].apply(lambda p: p * 0.9)
    print("\nDataFrame with new 'DiscountPrice' column from .apply():\n", df[['Product', 'Price', 'DiscountPrice']].head())
    print("-" * 30)


# =======================================
# 4. SORTING DATA (`.sort_values()`)
# =======================================
# - Used to sort a DataFrame by one or more columns.
if not df.empty:
    print("--- Sorting Data ---")

    # --- Sort by a single column in descending order ---
    df_sorted_by_price = df.sort_values(by='Price', ascending=False)
    print("DataFrame sorted by Price (descending):\n", df_sorted_by_price)


    # --- Sort by multiple columns ---
    # Sorts by 'Category' first (ascending), then by 'TotalPrice' (descending) within each category.
    df_multi_sort = df.sort_values(
        by=['Category', 'TotalPrice'],
        ascending=[True, False]
    )
    print("\nDataFrame sorted by Category (asc) and then TotalPrice (desc):\n", df_multi_sort)
    print("-" * 30)


# =======================================
# 5. RENAMING COLUMNS (`.rename()`)
# =======================================
# - Used to change the labels of columns or the index.
if not df.empty:
    print("--- Renaming Columns ---")
    # The .rename() method is flexible for changing labels.
    # It takes a dictionary mapping {old_name: new_name}.
    df_renamed = df.rename(columns={
        'TotalPrice': 'Revenue',
        'OrderDate': 'Date'
    })
    print("DataFrame with renamed columns:\n", df_renamed.head())


# --- End of File ---