import matplotlib.pyplot as plt
import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Introduction
# 2. Scatter Plot (`plt.scatter`)
# 3. Bar Chart (`plt.bar`)
# 4. Histogram (`plt.hist`)
# 5. Pie Chart (`plt.pie`)


# =======================================
# 1. INTRODUCTION
# =======================================
# - While `plt.plot()` is versatile for creating line graphs, `pyplot` provides
#   dedicated functions for other common plot types that are often more convenient.
# - We will cover four key types:
#   - Scatter Plot: For showing relationships between two numerical variables.
#   - Bar Chart: For comparing quantities across categories.
#   - Histogram: For showing the distribution of a single variable.
#   - Pie Chart: For showing parts of a whole.


# =======================================
# 2. SCATTER PLOT (`plt.scatter`)
# =======================================
# - Used to visualize the relationship between two numerical variables.
# - Each point represents an individual observation.

# --- Prepare Data ---
# Let's create some correlated data
np.random.seed(42)
x_scatter = np.random.rand(50) * 10
y_scatter = 2 * x_scatter + 1 + np.random.rand(50) * 2  # y = 2x + 1 + noise

# --- Create Plot ---
plt.figure(figsize=(8, 6))  # Create a new figure
plt.scatter(x=x_scatter, y=y_scatter, color="crimson")
plt.title("Relationship Between Two Variables")
plt.xlabel("Independent Variable (x)")
plt.ylabel("Dependent Variable (y)")
plt.grid(True)


# =======================================
# 3. BAR CHART (`plt.bar`)
# =======================================
# - Used to compare quantities across different discrete categories.

# --- Prepare Data ---
categories = ["Electronics", "Clothing", "Groceries", "Books"]
sales = [12000, 8500, 22000, 6300]

# --- Create Plot ---
plt.figure(figsize=(8, 6))
plt.bar(categories, sales, color="skyblue")
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales (USD)")


# =======================================
# 4. HISTOGRAM (`plt.hist`)
# =======================================
# - Used to visualize the distribution of a single numerical variable.
# - It groups data into "bins" and shows the frequency of observations in each bin.

# --- Prepare Data ---
# Create 1000 random data points from a normal distribution
data_hist = np.random.randn(1000)

# --- Create Plot ---
plt.figure(figsize=(8, 6))
plt.hist(data_hist, bins=30, color="lightgreen", edgecolor="black")
plt.title("Distribution of a Dataset")
plt.xlabel("Value")
plt.ylabel("Frequency")


# =======================================
# 5. PIE CHART (`plt.pie`)
# =======================================
# - Used to show the proportion of different categories as slices of a whole.
# - Best for a small number of categories.

# --- Prepare Data ---
sizes = [45, 25, 20, 10]  # Must sum to 100 for percentages
labels = ["Work", "Sleep", "Eat", "Leisure"]
explode = (0, 0.1, 0, 0)  # "Explode" the 2nd slice (Sleep)

# --- Create Plot ---
plt.figure(figsize=(8, 8))
# `autopct` formats the percentage on each slice.
plt.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", startangle=90)
plt.axis("equal")  # Ensures the pie chart is circular.
plt.title("Daily Activity Proportions")


# --- Display all plots at once at the end of the script ---
print("Displaying 4 different plot types. Close the plot windows to end the script.")
plt.show()


# --- End of File ---
