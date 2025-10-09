# Grouping Data for EDA

## Grouping and Plotting with Pandas

- **GroupBy:**  
  - Use `groupby` on your DataFrame to aggregate data by a target column (e.g., species).
  - Calculate the mean for each feature (petal length, petal width, sepal length, sepal width) by group.
  - Use `.plot()` to visualize the grouped data. By default, this creates a line plot.
  - You can customize colors, labels, font size, and figure size for clarity.

    ```python
    grouped = data.groupby('species').mean()
    grouped.plot(
        color=['red', 'blue', 'black', 'green'],
        fontsize=10,
        figsize=(4, 4)
    )
    plt.show()
    ```

- **Interpretation:**  
  - X-axis: Categories (e.g., setosa, versicolor, virginica)
  - Y-axis: Mean values for each feature, color-coded

## Seaborn Visualizations

### Pair Plot

- **Purpose:** Visualize pairwise relationships and distributions for all features, colored by category.
- **Usage:**
    ```python
    import seaborn as sns
    sns.pairplot(data, hue='species', height=2)
    plt.show()
    ```
- **Interpretation:**  
  - Scatter plots for each feature pair, histograms on the diagonal.
  - Colors indicate different species or categories.

### Hexbin Plot (Joint Plot)

- **Purpose:** Show density of points and marginal distributions for two variables.
- **Usage:**
    ```python
    sns.jointplot(x='sepal_length', y='sepal_width', data=data, kind='hex')
    plt.show()
    ```
- **Interpretation:**  
  - Darker hexagons indicate higher density of points.
  - Marginal histograms show distributions of each variable.

### Facet Grid

- **Purpose:** Create separate plots for each category (e.g., species) to compare distributions.
- **Usage:**
    ```python
    g = sns.FacetGrid(data, col='species', margin_titles=True)
    g.map(plt.hist, 'sepal_width')
    plt.show()
    ```
- **Interpretation:**  
  - Each column shows the distribution for a different category.
  - Useful for comparing feature distributions across groups.

## Key Takeaways

- Grouping and aggregating data with Pandas helps summarize and visualize differences between categories.
- Seaborn provides powerful tools for visualizing relationships, distributions, and group comparisons.
- These techniques are essential for effective exploratory data analysis (EDA).

---

**Next:** [Feature Engineering and Variable Transformation: Background](./04_feature_engineering_and_transformation--background.md)