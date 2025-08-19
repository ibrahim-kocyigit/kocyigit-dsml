# 10_integrating_pandas_with_matplotlib.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# =======================================
# 1. THE STANDARD DATA SCIENCE WORKFLOW
# =======================================
# - In practice, data rarely starts in a format that's ready for plotting.
# - The standard workflow is a powerful combination:
#   1. Load and Prepare Data: Use Pandas to load, clean, and filter data.
#   2. Aggregate Data: Use Pandas' `.groupby()` or other methods to summarize the
#      data into a plottable form.
#   3. Visualize Data: Use Matplotlib's Object-Oriented interface to create a
#      customized, publication-quality plot from the aggregated data.
#
# - While `df.plot()` is great for quick exploration, this Pandas -> Matplotlib
#   workflow gives you ultimate control over the final visualization.

# --- Setup: Load our sample sales data ---
DATA_FOLDER = "pandas_data"
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")

try:
    df = pd.read_csv(file_path, parse_dates=['OrderDate'])
    df['TotalPrice'] = df['Price'] * df['Quantity']
    print("--- Loaded and Prepared Sample DataFrame ---")
    print(df.head())
except FileNotFoundError:
    print(f"Error: The data file was not found at '{file_path}'")
    print("Please run '04_reading_and_writing_data.py' first to create it.")
    df = pd.DataFrame()

print("-" * 30)


# =======================================
# 2. EXAMPLE 1: BAR CHART OF AGGREGATED DATA
# =======================================
# - Goal: Create a bar chart showing total revenue per product category.

if not df.empty:
    print("--- Plot 1: Bar Chart from GroupBy ---")
    # --- Step 1: Aggregate data with Pandas ---
    category_revenue = df.groupby('Category')['TotalPrice'].sum()
    print("Data to plot:\n", category_revenue)

    # --- Step 2: Visualize with Matplotlib ---
    fig1, ax1 = plt.subplots(figsize=(8, 6))

    ax1.bar(
        category_revenue.index,  # x-values are the categories (the Series index)
        category_revenue.values, # y-values are the aggregated revenues
        color=['#4c72b0', '#55a868'] # A custom color scheme
    )
    ax1.set_title('Total Revenue by Product Category', fontsize=16)
    ax1.set_ylabel('Total Revenue (USD)', fontsize=12)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    print("Generated Bar Chart.")
    print("-" * 30)


# =======================================
# 3. EXAMPLE 2: SCATTER PLOT OF RELATIONSHIPS
# =======================================
# - Goal: Investigate the relationship between the price of an item and its quantity sold.

if not df.empty:
    print("--- Plot 2: Scatter Plot ---")
    # --- Step 1: Data is already prepared in columns ---
    # No aggregation needed for this plot type.

    # --- Step 2: Visualize with Matplotlib ---
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    
    # We can even use a third variable to control the size of the points
    point_sizes = df['Quantity'] * 50 # Make quantity visually apparent

    ax2.scatter(
        df['Price'],
        df['TotalPrice'],
        s=point_sizes, # s = size
        alpha=0.6,     # alpha = transparency
        edgecolors='w' # Add a white edge to markers
    )
    ax2.set_title('Revenue vs. Price (Sized by Quantity)', fontsize=16)
    ax2.set_xlabel('Unit Price (USD)', fontsize=12)
    ax2.set_ylabel('Total Revenue (USD)', fontsize=12)
    ax2.grid(True, linestyle=':', alpha=0.7)
    print("Generated Scatter Plot.")
    print("-" * 30)


# =======================================
# 4. EXAMPLE 3: TIME SERIES PLOT
# =======================================
# - Goal: Plot the total sales revenue over time.

if not df.empty:
    print("--- Plot 3: Time Series Plot ---")
    # --- Step 1: Aggregate data by date ---
    daily_revenue = df.groupby('OrderDate')['TotalPrice'].sum()
    print("Data to plot:\n", daily_revenue)

    # --- Step 2: Visualize with Matplotlib ---
    fig3, ax3 = plt.subplots(figsize=(10, 6))

    ax3.plot(
        daily_revenue.index,
        daily_revenue.values,
        marker='o',
        linestyle='--'
    )
    ax3.set_title('Daily Sales Revenue', fontsize=16)
    ax3.set_xlabel('Date', fontsize=12)
    ax3.set_ylabel('Total Revenue (USD)', fontsize=12)
    ax3.grid(True)
    
    # Improve date formatting on the x-axis
    fig3.autofmt_xdate()
    print("Generated Time Series Plot.")


# --- Display all created figures ---
if not df.empty:
    print("\nDisplaying all plots. This concludes the Matplotlib curriculum!")
    plt.show()
else:
    print("DataFrame is empty, no plots to display.")

# --- End of File ---