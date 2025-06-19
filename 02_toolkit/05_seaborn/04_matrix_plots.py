import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# =======================================
# 1. INTRODUCTION TO MATRIX PLOTS
# =======================================
# - Matrix plots are used to visualize 2D, matrix-like data where individual
#   values are represented by color.
# - Their primary use cases are for visualizing correlation matrices and showing
#   patterns in data over two variables (e.g., time vs. categories).
# - We will cover `sns.heatmap` and the more advanced `sns.clustermap`.

# --- Apply a theme ---
sns.set_theme(style="white")


# =======================================
# 2. HEATMAPS (`sns.heatmap`)
# =======================================
# - The most common tool for visualizing a grid of data.
# - To create a heatmap, the data often needs to be in a 2D matrix format,
#   where both the rows and columns have meaningful labels. A pivot table is
#   a perfect way to prepare data for this.

print("--- Preparing data for Heatmap using a pivot table ---")
# Load the 'flights' dataset
flights_df = sns.load_dataset("flights")

# Use pandas `.pivot_table()` to create a matrix
flights_pivot = flights_df.pivot_table(
    index="month", columns="year", values="passengers"
)
print("Flights data pivoted into a Year x Month matrix:\n", flights_pivot.head())

# --- Create the Heatmap ---
plt.figure(figsize=(12, 8))
sns.heatmap(
    data=flights_pivot,
    annot=True,  # Display the data value in each cell
    fmt="d",  # Format the annotations as integers
    cmap="YlGnBu",  # Specify the color map
    linewidths=0.5,  # Add lines between cells
)
plt.title("Airline Passengers per Month (1949-1960)", fontsize=16)
print("\nGenerated a heatmap of airline passenger data.")
print("-" * 30)


# =======================================
# 3. HEATMAP OF A CORRELATION MATRIX
# =======================================
# - One of the most frequent use cases for a heatmap is to visualize the
#   correlation between many numerical variables in a dataset.

print("--- Creating a heatmap of a correlation matrix ---")
# Load the 'penguins' dataset
penguins_df = sns.load_dataset("penguins")

# Select only numerical columns for correlation calculation
# In modern pandas, this can be done directly
numerical_cols = penguins_df.select_dtypes(include=np.number)

# Calculate the correlation matrix using pandas `.corr()`
correlation_matrix = numerical_cols.corr()
print("Correlation matrix of penguin measurements:\n", correlation_matrix)

# --- Create the Correlation Heatmap ---
plt.figure(figsize=(10, 7))
sns.heatmap(
    data=correlation_matrix,
    annot=True,
    fmt=".2f",  # Format annotations to 2 decimal places
    cmap="coolwarm",  # Use a diverging colormap for correlations
    vmin=-1,
    vmax=1,  # Set the color bar limits from -1 to 1
)
plt.title("Correlation Matrix of Penguin Measurements", fontsize=16)
print("\nGenerated a heatmap of a correlation matrix.")
print("-" * 30)


# =======================================
# 4. CLUSTERMAPS (`sns.clustermap`)
# =======================================
# - A clustermap is a more advanced heatmap. It uses hierarchical clustering
#   to reorder the rows and columns, placing similar rows and columns together.
# - This can automatically reveal patterns and subgroups in your data.
# - It returns a `ClusterGrid` object, not a standard Axes.

print("--- Creating a clustermap ---")
# `sns.clustermap` creates its own figure.
# `standard_scale=1` normalizes the data within the columns, making patterns more visible.
g = sns.clustermap(flights_pivot, cmap="viridis", standard_scale=1, figsize=(10, 8))
g.fig.suptitle(
    "Clustermap of Airline Passengers (Clustered by Similarity)", y=1.02, fontsize=16
)
print("Generated a clustermap, which reorders rows/columns to show patterns.")


# --- Display all created plots ---
print("\nDisplaying all plots. Close the plot windows to end the script.")
plt.tight_layout()
plt.show()

# --- End of File ---
