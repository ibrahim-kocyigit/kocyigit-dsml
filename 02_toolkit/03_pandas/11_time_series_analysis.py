import pandas as pd
import os

# =======================================
# 1. INTRODUCTION AND SETUP
# =======================================
# - Pandas was originally developed for financial time series analysis and has
#   incredibly powerful, built-in tools for working with dates and times.
# - The key to unlocking these features is to use a `DatetimeIndex`.

# --- Load the sample dataset with a DatetimeIndex ---
DATA_FOLDER = "pandas_data"
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")

try:
    # We instruct pandas to parse 'OrderDate' as dates and set it as the index.
    df = pd.read_csv(file_path, parse_dates=["OrderDate"], index_col="OrderDate")
    print("--- Sample Sales DataFrame with DatetimeIndex ---")
    print(df)
    print(f"\nType of the index: {type(df.index)}")  # Note the DatetimeIndex type

except FileNotFoundError:
    print(f"Error: The data file was not found at '{file_path}'")
    print("Please run '04_reading_and_writing_data.py' first to create it.")
    df = pd.DataFrame()  # Create an empty df to avoid further errors

print("-" * 30)


# =======================================
# 2. TIME-BASED INDEXING AND SELECTION
# =======================================
# - With a DatetimeIndex, you can select and slice data in intuitive ways.
if not df.empty:
    print("--- Time-Based Indexing ---")

    # --- Select all data for a specific day ---
    print("Sales on 2025-01-15:\n", df.loc["2025-01-15"])

    # --- Select all data for a specific year or month ---
    # Pandas is smart enough to interpret partial date strings.
    print("\nAll sales in January 2025:\n", df.loc["2025-01"])

    # --- Slicing a date range ---
    start_date = "2025-01-16"
    end_date = "2025-01-17"
    print(
        f"\nSales between {start_date} and {end_date}:\n", df.loc[start_date:end_date]
    )
    print("-" * 30)


# =======================================
# 3. RESAMPLING TIME SERIES DATA
# =======================================
# - Resampling is the process of converting a time series from one frequency to another.
# - Downsampling: Decreasing the frequency (e.g., daily to monthly). Requires aggregation.
# - Upsampling: Increasing the frequency (e.g., daily to hourly). Requires filling/interpolation.

# - The `.resample()` method works like .groupby() - you must chain an aggregation to it.
# - Common Frequency Rules: 'D' (Day), 'W' (Week), 'M' (Month End), 'Q' (Quarter End), 'Y' (Year End)
if not df.empty:
    print("--- Resampling Data ---")
    # Our data is at a daily level. Let's downsample it to see total sales PER DAY.
    # This will group all orders on the same day together.
    daily_sales = df[["Price", "Quantity"]].resample("D").sum()
    print("Total daily sales (resampled to 'D' frequency):\n", daily_sales)

    # Note: Days with no sales (like Jan 16th in the original data) still appear
    # in the resampled index, with an aggregated value of 0.
    print("-" * 30)


# =======================================
# 4. TIME SHIFTS AND ROLLING WINDOWS
# =======================================
# - These are common techniques for time series feature engineering.

# --- To better demonstrate, let's create a simple, continuous time series ---
# A DataFrame with sales data for 7 consecutive days
date_range = pd.date_range(start="2025-01-01", periods=7, freq="D")
sales_data = pd.DataFrame({"Sales": [10, 15, 12, 18, 20, 25, 22]}, index=date_range)

print("--- Time Shifts and Rolling Windows ---")
print("New sample time series data:\n", sales_data)

# --- Shifting (`.shift()`) ---
# - Shifts data forward or backward by a specified number of periods.
# - Useful for calculating period-over-period changes.
sales_data["Previous_Day_Sales"] = sales_data["Sales"].shift(1)
print("\nData with previous day's sales (using .shift(1)):\n", sales_data)


# --- Rolling Windows (`.rolling()`) ---
# - Calculates statistics over a "sliding window" of a fixed size.
# - Used for things like moving averages to smooth out data.
# - `.rolling(window=N)` creates a rolling view. You must chain an aggregation to it.
sales_data["3-Day_Moving_Avg"] = sales_data["Sales"].rolling(window=3).mean()
print("\nData with 3-day moving average (using .rolling(3).mean()):\n", sales_data)
# Note: The first two values are NaN because there are not enough preceding data points
# to fill the window of size 3.

# --- End of File ---
