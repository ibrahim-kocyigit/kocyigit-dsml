import pandas as pd
import os

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Introduction to "Group By"
# 2. Performing a Simple Group By
# 3. Grouping and Selecting a Single Column
# 4. Grouping By Multiple Columns
# 5. The `.agg()` Method for Multiple Aggregations


# =======================================
# 1. INTRODUCTION TO "GROUP BY"
# =======================================
# - The "group by" operation is one of the most powerful features in Pandas.
# - It is used for splitting data into groups based on some criteria, applying
#   a function to each group independently, and then combining the results.
# - This process is often referred to as "Split-Apply-Combine"

# --- Setup: Load the data and create a 'TotalPrice' column ---
DATA_FOLDER = "pandas_data"
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")

try:
    df = pd.read_csv(file_path, parse_dates=["OrderDate"])
    # Create a TotalPrice column for more meaningful aggregations
    df["TotalPrice"] = df["Price"] * df["Quantity"]
    print("--- Sample DataFrame with TotalPrice ---")
    print(df)
except FileNotFoundError:
    print(f"Error: The data file was not found at '{file_path}'")
    print("Please run '04_reading_and_writing_data.py' first to create it.")
    df = pd.DataFrame()  # Create an empty df to avoid further errors

print("-" * 30)


# =======================================
# 2. PERFORMING A SIMPLE GROUP BY
# =======================================
# - The `.groupby()` method itself doesn't compute anything; it returns a `DataFrameGroupBy` object.
# - This object contains all the information about the groups. To get a result,
#   you must chain an aggregation method to it (e.g., .sum(), .mean()).
print("--- Simple Group By ---")

# Group the DataFrame by the 'Category' column
category_groups = df.groupby("Category")

# Now, apply aggregation functions to the groups
# This calculates the sum of all numerical columns for each category
category_sum = category_groups.sum(numeric_only=True)
print("Sum of numerical columns by Category:\n", category_sum)

# Calculate the mean of all numerical columns for each category
category_mean = category_groups.mean(numeric_only=True)
print("\nMean of numerical columns by Category:\n", category_mean)

# .size() counts the number of rows in each group
category_size = category_groups.size()
print("\nSize (number of items) of each Category:\n", category_size)
print("-" * 30)


# =======================================
# 3. GROUPING AND SELECTING A SINGLE COLUMN
# =======================================
# - For efficiency, you can select a column *before* aggregating.
# - This is useful when you only care about the statistics of one specific column.
print("--- Grouping on a Single Column ---")

# Calculate the total revenue ('TotalPrice') for each product
# The result is a Pandas Series
product_revenue = df.groupby("Product")["TotalPrice"].sum()
print("Total revenue per Product:\n", product_revenue)

# Find the average price for each category
avg_price_per_category = df.groupby("Category")["Price"].mean()
print("\nAverage price per Category:\n", avg_price_per_category)
print("-" * 30)


# =======================================
# 4. GROUPING BY MULTIPLE COLUMNS
# =======================================
# - You can pass a list of column names to group by multiple levels.
# - This results in a DataFrame with a MultiIndex.
print("--- Grouping by Multiple Columns ---")
# Group by both 'Category' and 'Product'
multi_group = df.groupby(["Category", "Product"])

# Calculate the total quantity sold for each combination
quantity_by_group = multi_group["Quantity"].sum()
print("Total quantity sold by Category and Product:\n", quantity_by_group)
print("-" * 30)


# =======================================
# 5. THE `.agg()` METHOD FOR MULTIPLE AGGREGATIONS
# =======================================
# - The `.agg()` method is a flexible way to apply multiple aggregation functions at once.
# - You can apply different functions to different columns.
print("--- The .agg() Method ---")

# Group by category and apply multiple aggregations
aggregations = df.groupby("Category").agg(
    # Pass a dictionary where keys are columns and values are the functions to apply
    {
        "Price": "mean",  # Calculate the mean of the Price column
        "Quantity": "sum",  # Calculate the sum of the Quantity column
        "TotalPrice": [
            "sum",
            "max",
        ],  # Apply multiple functions to the TotalPrice column.
    }
)
print("Multiple aggregations by Category:\n", aggregations)


# --- End of File ---
