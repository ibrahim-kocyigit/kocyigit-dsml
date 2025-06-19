import seaborn as sns
import matplotlib.pyplot as plt

# =======================================
# 1. FIGURE-LEVEL VS. AXES-LEVEL FUNCTIONS
# =======================================
# - So far, we have mostly used "axes-level" functions (e.g., `scatterplot`,
#   `histplot`). These functions draw onto a single Matplotlib `Axes` and don't
#   affect the rest of the figure.
#
# - Seaborn also has "figure-level" functions (`relplot`, `displot`, `catplot`).
#   These are more powerful because they create and manage the entire figure,
#   including making it easy to create multiple subplots ("facets") based on your data.
# - They use a `FacetGrid` object under the hood.

# --- Setup: Apply a theme for our plots ---
sns.set_theme(style="ticks", palette="deep")


# =======================================
# 2. `sns.relplot()`: RELATIONAL PLOT GRIDS
# =======================================
# - `relplot()` is the figure-level interface for `scatterplot()` and `lineplot()`.
# - Its key feature is the ability to create subplots using the `col` and `row` parameters.

print("--- Loading 'tips' dataset for relplot ---")
tips_df = sns.load_dataset("tips")

# --- Create a scatter plot faceted by the 'time' column ---
# This will create two subplots: one for 'Lunch' and one for 'Dinner'.
sns.relplot(
    data=tips_df,
    x="total_bill",
    y="tip",
    col="time",  # Create columns of subplots based on the 'time' category
    hue="smoker",  # Still use hue to color points within each subplot
    style="smoker",  # Use different markers for smoker/non-smoker
)
print("Generated a relational plot faceted by 'time'.")


# --- Facet on both columns and rows for a full grid ---
sns.relplot(
    data=tips_df,
    x="total_bill",
    y="tip",
    col="time",
    row="sex",  # Create rows of subplots based on the 'sex' category
    hue="smoker",
)
print("Generated a relational plot faceted by both 'time' and 'sex'.")
print("-" * 30)


# =======================================
# 3. `sns.displot()`: DISTRIBUTION PLOT GRIDS
# =======================================
# - `displot()` is the figure-level interface for distribution plots like
#   `histplot`, `kdeplot`, and `ecdfplot`.

print("--- Loading 'penguins' dataset for displot ---")
penguins_df = sns.load_dataset("penguins")

# --- Compare flipper length distributions for each species ---
# This creates three histograms, one for each species, in separate columns.
sns.displot(
    data=penguins_df,
    x="flipper_length_mm",
    col="species",  # Facet by species
)
print("\nGenerated a distribution plot faceted by 'species'.")


# --- Change the kind of plot to KDE ---
sns.displot(
    data=penguins_df,
    x="flipper_length_mm",
    col="species",
    kind="kde",  # Change the plot type to KDE
    fill=True,
)
print("Generated a KDE distribution plot faceted by 'species'.")
print("-" * 30)


# =======================================
# 4. `sns.catplot()`: CATEGORICAL PLOT GRIDS
# =======================================
# - `catplot()` is the figure-level interface for the entire family of categorical plots
#   (e.g., `boxplot`, `violinplot`, `barplot`, etc.).
# - This makes it incredibly easy to compare categorical data across different facets.

print("--- Using 'tips' dataset for catplot ---")

# --- Compare the distribution of total_bill on different days, faceted by smoker status ---
sns.catplot(
    data=tips_df,
    x="day",
    y="total_bill",
    col="smoker",
    kind="box",  # We can easily change the plot kind
)
print("\nGenerated a categorical box plot faceted by 'smoker'.")

# --- Let's see the same data, but with a different kind of plot ---
# Simply change the `kind` parameter to get a different view of the same data.
sns.catplot(data=tips_df, x="day", y="total_bill", col="smoker", kind="violin")
print("Generated a categorical violin plot of the same data.")


# --- Display all created plot grids ---
print("\nDisplaying all plots. Close the plot windows to end the script.")
plt.show()

# --- End of File ---
