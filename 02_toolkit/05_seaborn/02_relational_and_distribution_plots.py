import seaborn as sns
import matplotlib.pyplot as plt

# =======================================
# 1. INTRODUCTION
# =======================================
# - This lesson covers two key goals of visualization:
#   1. Relational Plots: To understand the relationship between two variables.
#   2. Distribution Plots: To understand how a single variable is distributed.
# - We will use Seaborn's high-level functions to create these plots with minimal code.

# --- Apply the default Seaborn theme ---
sns.set_theme(style="whitegrid")


# =======================================
# 2. RELATIONAL PLOTS WITH `sns.scatterplot()`
# =======================================
# - Used to visualize the relationship between two numerical variables.
# - The `hue` parameter is a key feature, adding a third dimension by coloring
#   points based on a categorical variable.

print("--- Loading 'penguins' dataset for relational plots ---")
penguins_df = sns.load_dataset("penguins")
print(penguins_df.head())

# --- Create a new figure for our scatter plot ---
plt.figure(figsize=(10, 6))

# Use `hue` to color points by species. Seaborn handles the colors and legend automatically.
sns.scatterplot(
    data=penguins_df,
    x="flipper_length_mm",
    y="bill_length_mm",
    hue="species",  # Color points by the 'species' column
    size="body_mass_g",  # Vary point size by the 'body_mass_g' column
    style="island",  # Vary point marker style by the 'island' column
    alpha=0.7,  # Set transparency
)
plt.title("Penguin Bill Length vs. Flipper Length")
print("\nGenerated a scatter plot with hue, size, and style encoding.")
print("-" * 30)


# =======================================
# 3. RELATIONAL PLOTS WITH `sns.lineplot()`
# =======================================
# - Ideal for showing the relationship between two variables where the x-axis
#   variable is continuous (like time).
# - Key Feature: It automatically aggregates data. If there are multiple y-values
#   for a single x-value, it plots the mean and a shaded confidence interval.

print("--- Loading 'flights' dataset for line plot ---")
flights_df = sns.load_dataset("flights")
print(flights_df.head())

# --- Create a new figure for our line plot ---
plt.figure(figsize=(10, 6))

# Plot the number of passengers over the years.
# The shaded area represents the confidence interval (by default, 95%).
sns.lineplot(data=flights_df, x="year", y="passengers")
plt.title("Airline Passengers Over Time")
print("\nGenerated a line plot with an automatic confidence interval.")
print("-" * 30)


# =======================================
# 4. DISTRIBUTION PLOTS WITH `sns.histplot()`
# =======================================
# - A histogram visualizes the distribution of a single numerical variable
#   by grouping data into bins and counting the frequency.

print("--- Loading 'tips' dataset for distribution plots ---")
tips_df = sns.load_dataset("tips")
print(tips_df.head())

# --- Create a new figure for our histogram ---
plt.figure(figsize=(10, 6))

# Use `kde=True` to overlay a Kernel Density Estimate curve.
# Use `hue` to see separate distributions for 'time' (Lunch/Dinner).
sns.histplot(data=tips_df, x="total_bill", kde=True, hue="time")
plt.title("Distribution of Total Bill Amounts by Time of Day")
print("\nGenerated a histogram with KDE and hue.")
print("-" * 30)


# =======================================
# 5. DISTRIBUTION PLOTS WITH `sns.kdeplot()`
# =======================================
# - A Kernel Density Estimate (KDE) plot creates a smoothed representation
#   of a variable's distribution.

# --- Create a new figure for our KDE plot ---
plt.figure(figsize=(10, 6))

# Use `fill=True` to get a shaded plot.
# Use `hue` to compare distributions.
sns.kdeplot(data=tips_df, x="tip", hue="smoker", fill=True)
plt.title("Distribution of Tip Amounts for Smokers vs. Non-Smokers")
print("\nGenerated a KDE plot.")


# --- Display all created plots ---
print("\nDisplaying all plots. Close the plot windows to end the script.")
plt.tight_layout()
plt.show()

# --- End of File ---
