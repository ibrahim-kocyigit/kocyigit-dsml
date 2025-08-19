# 12_basic_plotting.py

import pandas as pd
import os
import matplotlib.pyplot as plt # The primary plotting library in Python

# =======================================
# 1. INTRODUCTION TO PLOTTING
# =======================================
# - Data visualization is a critical part of data analysis for understanding trends,
#   patterns, and outliers in your data.
# - Pandas has a built-in `.plot()` accessor that makes creating simple plots
#   directly from a DataFrame or Series very easy.
# - IMPORTANT: Pandas' plotting functions are a convenient wrapper around the
#   powerful `matplotlib` library. To use them, you must have matplotlib installed:
#   `pip install matplotlib`

# --- Setup: Load data and create a 'TotalPrice' column ---
DATA_FOLDER = "pandas_data"
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")

try:
    df = pd.read_csv(file_path, parse_dates=['OrderDate'])
    df['TotalPrice'] = df['Price'] * df['Quantity']
    print("--- Sample DataFrame for Plotting ---")
    print(df)
except FileNotFoundError:
    print(f"Error: The data file was not found at '{file_path}'")
    print("Please run '04_reading_and_writing_data.py' first to create it.")
    df = pd.DataFrame() # Create an empty df to avoid further errors

print("-" * 30)

# =======================================
# 2. THE `.plot()` ACCESSOR AND LINE PLOTS
# =======================================
# - The `.plot()` method is the main interface for creating plots.
# - The `kind` parameter specifies the type of plot. The default is a line plot.
# - Line plots are best for visualizing data over a continuous interval, like time.
if not df.empty:
    print("--- Creating Plots ---")
    # To make a meaningful line plot, let's group sales by date
    daily_revenue = df.groupby('OrderDate')['TotalPrice'].sum()
    print("Aggregated daily revenue for line plot:\n", daily_revenue)

    # Create a line plot
    daily_revenue.plot(
        kind='line',
        title='Daily Sales Revenue',
        xlabel='Date',
        ylabel='Total Revenue (USD)',
        figsize=(8, 5), # Set the figure size (width, height in inches)
        grid=True,
        legend=True
    )
    # plt.show() # In a script, this command displays the plot. We'll call it once at the end.
    print("\nGenerated a line plot for daily sales revenue.")
    print("-" * 30)


# =======================================
# 3. COMMON PLOT TYPES
# =======================================
# - You can create many different types of plots by changing the `kind` parameter.
if not df.empty:
    # --- Bar Plot (`kind='bar'`) ---
    # - Good for comparing quantities across different categories.
    product_quantity = df.groupby('Product')['Quantity'].sum()
    product_quantity.plot(
        kind='bar',
        title='Total Quantity Sold per Product',
        xlabel='Product',
        ylabel='Total Quantity',
        color=['skyblue', 'salmon', 'lightgreen', 'gold'] # You can specify colors
    )
    print("Generated a bar plot for product quantities.")


    # --- Histogram (`kind='hist'`) ---
    # - Good for understanding the distribution of a single numerical variable.
    df['Price'].plot(
        kind='hist',
        title='Distribution of Product Prices',
        bins=8 # The number of bars in the histogram
    )
    print("Generated a histogram for product prices.")


    # --- Scatter Plot (`kind='scatter'`) ---
    # - Good for visualizing the relationship between two numerical variables.
    # - Requires specifying the x and y columns.
    df.plot(
        kind='scatter',
        x='Price',
        y='TotalPrice',
        title='Price vs. Total Revenue'
    )
    print("Generated a scatter plot for price vs. total revenue.")
    print("-" * 30)


# =======================================
# 4. DISPLAYING THE PLOTS
# =======================================
# - When running a Python script, plots are created in the background.
# - To actually see them, you must call `plt.show()`.
# - This command opens an interactive window to display all the plots you've created.
# - In environments like Jupyter Notebook, plots often appear automatically ("inline").
if not df.empty:
    print("--- Displaying Plots ---")
    print("Calling `plt.show()` to display all generated plots...")
    print("Close the plot window(s) to end the script.")
    plt.tight_layout() # Adjusts plots to prevent labels from overlapping
    plt.show()
else:
    print("DataFrame is empty, no plots to display.")

print("\nThis concludes the Pandas for Data Analysis curriculum!")
# --- End of File ---