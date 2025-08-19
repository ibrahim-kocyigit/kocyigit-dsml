# 01_seaborn_intro_and_setup.py

# =======================================
# 1. WHAT IS SEABORN?
# =======================================
# - Seaborn is a Python data visualization library based on Matplotlib.
# - It provides a high-level interface for drawing attractive and informative
#   statistical graphics that are difficult to create with Matplotlib alone.
# - Key Idea: Seaborn uses Matplotlib to draw its plots. This means you can still
#   use Matplotlib functions to fine-tune Seaborn plots.


# =======================================
# 2. INSTALLATION AND IMPORT CONVENTIONS
# =======================================
# - To install Seaborn, run this command in your terminal:
#   `pip install seaborn`
#
# - The universal community conventions for importing are:
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# =======================================
# 3. SEABORN'S KEY ADVANTAGES
# =======================================
# - Works seamlessly with Pandas DataFrames.
# - Has built-in themes and color palettes for creating beautiful plots with minimal code.
# - Simplifies the creation of complex statistical plots (e.g., plots showing
#   distributions, relationships, and categorical data).


# =======================================
# 4. SETTING THE VISUAL STYLE WITH `sns.set_theme()`
# =======================================
# - One of Seaborn's biggest draws is its ability to instantly improve plot aesthetics.
# - Let's see the difference it makes on a standard Matplotlib plot.

# --- First, a default Matplotlib plot ---
plt.figure() # Create a new figure
x = [1, 2, 3, 4]
y = [1, 4, 2, 5]
plt.plot(x, y)
plt.title("Default Matplotlib Style")


# --- Now, apply a Seaborn theme and create the same plot ---
# `sns.set_theme()` applies a beautiful default style to all subsequent plots.
sns.set_theme(style="darkgrid", palette="viridis")

plt.figure() # Create another new figure
plt.plot(x, y)
plt.title("Matplotlib Plot with Seaborn's 'darkgrid' Theme")

print("--- Seaborn's Theming ---")
print("Two plot windows will be shown: one with default Matplotlib style,")
print("and one with an improved style applied by a single Seaborn command.")
print("-" * 30)


# =======================================
# 5. LOADING BUILT-IN DATASETS
# =======================================
# - Seaborn comes with several classic datasets, which are perfect for learning and practice.
# - `sns.load_dataset()` downloads a dataset (if needed) and returns it as a Pandas DataFrame.
# - This allows our tutorials to be fully self-contained.

print("--- Loading a Built-in Dataset ---")
# Let's load the "tips" dataset, which contains data on restaurant tips.
tips_df = sns.load_dataset("tips")

# Inspect the loaded DataFrame
print("The 'tips' dataset has been loaded as a Pandas DataFrame.")
print("First 5 rows:\n", tips_df.head())
print("\nDataFrame Info:")
tips_df.info()
print("-" * 30)


# =======================================
# 6. YOUR FIRST SEABORN PLOT
# =======================================
# - Seaborn functions typically take a `data` argument (the DataFrame) and then
#   you specify the columns to plot using their string names for `x` and `y`.

print("--- Creating a simple Seaborn scatter plot ---")
plt.figure(figsize=(8, 6)) # Create a new figure for our plot

# Create a scatter plot to see the relationship between the total bill and the tip amount
sns.scatterplot(data=tips_df, x="total_bill", y="tip")

plt.title("Relationship between Total Bill and Tip Amount")
# Note: Seaborn often automatically adds axis labels from the column names!

print("A scatter plot of the 'tips' dataset has been generated.")


# --- Display all created plots ---
plt.tight_layout()
plt.show()

# --- End of File ---