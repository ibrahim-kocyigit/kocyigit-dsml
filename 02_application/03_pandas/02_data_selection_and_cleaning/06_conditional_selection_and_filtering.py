import pandas as pd
import os

# =======================================
# 1. INTRODUCTION AND SETUP
# =======================================
# - Filtering—selecting rows that meet certain criteria—is one of the most common tasks in data analysis.
# - Pandas uses a powerful technique called "boolean indexing" or "masking" for this.

# --- Load the sample dataset ---
DATA_FOLDER = "pandas_data"
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")

try:
    # We parse the 'OrderDate' column as dates right away.
    # For this lesson, we'll use the default integer index.
    df = pd.read_csv(file_path, parse_dates=["OrderDate"])
    print("--- Sample Sales DataFrame ---")
    print(df)
except FileNotFoundError:
    print(f"Error: The data file was not found at '{file_path}'")
    print("Please run '04_reading_and_writing_data.py' first to create it.")
    df = pd.DataFrame()  # Create an empty df to avoid further errors

print("-" * 30)


# =======================================
# 2. THE LOGIC OF BOOLEAN INDEXING
# =======================================
# - This is a two-step process:
#   1. Create a logical condition on a Series (a column). This produces a new
#      Series of `True`/`False` values, called a "boolean mask".
#   2. Use this mask to index the DataFrame, which returns only the rows where the mask is `True`.
if not df.empty:
    print("--- Boolean Indexing Logic ---")

    # --- Step 1: Create the boolean mask ---
    # Let's find all rows where the Category is 'Electronics'.
    mask = df["Category"] == "Electronics"
    print("The boolean mask for `df['Category'] == 'Electronics'`:\n", mask)
    print(f"Type of the mask: {type(mask)}")

    # --- Step 2: Apply the mask to the DataFrame ---
    # This is typically done in a single, idiomatic line.
    electronics_df = df[df["Category"] == "Electronics"]
    print("\nDataFrame filtered for 'Electronics':\n", electronics_df)
    print("-" * 30)


# =======================================
# 3. FILTERING WITH MULTIPLE CONDITIONS
# =======================================
# - To combine conditions, you MUST use:
#   - `&` for `and`
#   - `|` for `or`
#   - `~` for `not`
# - Each individual condition MUST be wrapped in parentheses `()`.
if not df.empty:
    print("--- Filtering with Multiple Conditions ---")

    # --- Example with `&` (AND) ---
    # Find all sales in the 'Electronics' category with a price over $100.
    high_value_electronics = df[(df["Category"] == "Electronics") & (df["Price"] > 100)]
    print(
        "High-value electronics (Category == 'Electronics' AND Price > 100):\n",
        high_value_electronics,
    )

    # --- Example with `|` (OR) ---
    # Find all sales that are either a 'Laptop' OR have a quantity of 3 or more.
    laptops_or_high_qty = df[(df["Product"] == "Laptop") | (df["Quantity"] >= 3)]
    print(
        "\nLaptops OR high quantity sales (Product == 'Laptop' OR Quantity >= 3):\n",
        laptops_or_high_qty,
    )
    print("-" * 30)


# =======================================
# 4. COMMON FILTERING METHODS
# =======================================
# - Pandas provides convenient methods to simplify common filtering tasks.
if not df.empty:
    print("--- Common Filtering Methods ---")

    # --- `.isin()` for checking against a list of values ---
    # Find all sales for 'Laptop' or 'Webcam'.
    products_of_interest = ["Laptop", "Webcam"]
    isin_filter_df = df[df["Product"].isin(products_of_interest)]
    print("Using `.isin(['Laptop', 'Webcam'])`:\n", isin_filter_df)

    # --- `.between()` for checking a numerical range (inclusive) ---
    # Find all sales where the price was between $50 and $300.
    between_filter_df = df[df["Price"].between(50, 300)]
    print("\nUsing `.between(50, 300)` on Price:\n", between_filter_df)

    # --- String methods with the `.str` accessor ---
    # The `.str` accessor lets you apply string methods to an entire Series.
    # Find all products that contain the letter 'o'.
    str_contains_df = df[
        df["Product"].str.contains("o", case=False)
    ]  # case=False makes it case-insensitive
    print("\nUsing `.str.contains('o')` on Product:\n", str_contains_df)
    print("-" * 30)


# =======================================
# 5. THE `.query()` METHOD
# =======================================
# - An alternative way to filter using a string expression.
# - Can be more readable for complex conditions.
if not df.empty:
    print("--- The .query() Method ---")
    # This is equivalent to the `&` example above.
    query_result = df.query('Category == "Electronics" and Price > 100')
    print(
        "Result of `df.query('Category == \"Electronics\" and Price > 100')`:\n",
        query_result,
    )
