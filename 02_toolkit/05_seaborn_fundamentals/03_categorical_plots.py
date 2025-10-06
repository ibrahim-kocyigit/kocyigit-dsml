import seaborn as sns
import matplotlib.pyplot as plt


# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Introduction
# 2. Categorical Scatter Plots
# 3. Categorical Distribution Plots
# 4. Categorical Estimate Plots


# =======================================
# 1. INTRODUCTION
# =======================================
# - A very common analysis task is to compare a numerical variable across different
#   groups or categories. Seaborn excels at this with a rich family of functions.
# - We can think of these plots in three families:
#   1. Categorical Scatter Plots: Show every data point (e.g., `stripplot`, `swarmplot`).
#   2. Categorical Distribution Plots: Show an abstract summary of the distribution
#      for each category (e.g., `boxplot`, `violinplot`).
#   3. Categorical Estimate Plots: Show a central tendency estimate (like the mean)
#      and its confidence interval (e.g., `barplot`, `pointplot`).

# --- Setup: Load the "tips" dataset and apply a theme ---
sns.set_theme(style="ticks", palette="pastel")
tips_df = sns.load_dataset("tips")

print("--- Using the 'tips' dataset for categorical plots ---")
print(tips_df.head())
print("-" * 30)


# =======================================
# 2. CATEGORICAL SCATTER PLOTS
# =======================================
# - These plots show every single data point, which helps visualize the
#   underlying distribution of observations.

# Create a figure with two subplots side-by-side
fig1, axes = plt.subplots(1, 2, figsize=(14, 6))
fig1.suptitle("Categorical Scatter Plots")

# --- `sns.stripplot()` ---
# - The most basic categorical scatter plot. Points can overlap.
sns.stripplot(data=tips_df, ax=axes[0], x="day", y="total_bill")
axes[0].set_title("stripplot")

# --- `sns.swarmplot()` ---
# - An improvement that adjusts points so they don't overlap.
# - Gives a better sense of the distribution. (Note: doesn't scale to very large data).
sns.swarmplot(data=tips_df, ax=axes[1], x="day", y="total_bill", hue="smoker")
axes[1].set_title("swarmplot (with hue)")

print("Generated Categorical Scatter Plots (stripplot, swarmplot).")


# =======================================
# 3. CATEGORICAL DISTRIBUTION PLOTS
# =======================================
# - These plots show an abstract summary of the distribution for each category.

fig2, axes = plt.subplots(1, 2, figsize=(14, 6))
fig2.suptitle("Categorical Distribution Plots")

# --- `sns.boxplot()` ---
# - Shows the quartiles of the dataset while the whiskers extend to show the
#   rest of the distribution. Points beyond the whiskers are potential outliers.
sns.boxplot(data=tips_df, ax=axes[0], x="day", y="total_bill", hue="time")
axes[0].set_title("boxplot (with hue)")

# --- `sns.violinplot()` ---
# - Combines a boxplot with a Kernel Density Estimate (KDE).
# - It shows more detail about the shape of the distribution (e.g., if it's bimodal).
sns.violinplot(
    data=tips_df, ax=axes[1], x="day", y="total_bill", hue="time", split=True
)
axes[1].set_title("violinplot (with hue and split)")

print("Generated Categorical Distribution Plots (boxplot, violinplot).")


# =======================================
# 4. CATEGORICAL ESTIMATE PLOTS
# =======================================
# - The plots show an estimate of central tendency (by default, the mean)
#   and its confidence interval for each category.

fig3, axes = plt.subplots(1, 2, figsize=(14, 6))
fig3.suptitle("Categorical Estimate & Count Plots")

# --- `sns.barplot()` ---
# - IMPORTANT: This shows the *mean* for each category, not the sum or count.
# - The black lines on the bars represent the confidence interval.
sns.barplot(data=tips_df, ax=axes[0], x="day", y="total_bill")
axes[0].set_title("barplot (showing mean total bill)")

# --- `sns.countplot()` ---
# - A special case that simply counts the number of occurrences in each category.
# - It's like a histogram for categorical data. Notice you only provide `x`.
sns.countplot(data=tips_df, ax=axes[1], x="day")
axes[1].set_title("countplot (showing number of tips per day)")

print("Generated Categorical Estimate and Count Plots (barplot, countplot).")


# --- Display all created plots ---
print("\nDisplaying all plots. Close the plot windows to end the script.")
plt.tight_layout(rect=(0, 0, 1, 0.96))  # Adjust for suptitles
plt.show()

# --- End of File ---
