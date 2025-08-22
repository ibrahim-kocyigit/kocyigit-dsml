# Data Visualization Cheat Sheet: A Decision Tree

This guide helps you choose the right plot for your analysis. Start by identifying how many variables you want to analyze, then follow the path based on their data types.

---

## 📍 I want to analyze ONE variable... (Univariate Analysis)

### ...and my variable is **Numerical** (e.g., `age`, `price`, `temperature`)

* **Goal: Understand the distribution of the data.**
    * **Plot:** **Histogram**
    * **Use Case:** To see the frequency of values within specific ranges (bins). Excellent for understanding the shape of your data (e.g., normal, skewed).
    * **Tool:** `sns.histplot()`

* **Goal: See a smoothed version of the distribution.**
    * **Plot:** **KDE Plot** (Kernel Density Estimate)
    * **Use Case:** To visualize the probability density of the data. Often overlaid on a histogram.
    * **Tool:** `sns.kdeplot()`

* **Goal: Identify outliers and see a statistical summary.**
    * **Plot:** **Box Plot** (or Box-and-Whisker Plot)
    * **Use Case:** To quickly see the median, quartiles, and range of the data, and to easily spot potential outliers.
    * **Tool:** `sns.boxplot()`

### ...and my variable is **Categorical** (e.g., `city`, `product_type`, `gender`)

* **Goal: See the frequency of each category.**
    * **Plot:** **Count Plot** / **Bar Chart**
    * **Use Case:** To count and compare the number of observations in each discrete category.
    * **Tools:** `sns.countplot()`, `plt.bar()`

---

## 📍 I want to analyze TWO variables... (Bivariate Analysis)

### ...and I have **Numerical vs. Numerical** data.

* **Goal: See the relationship and correlation between the two variables.**
    * **Plot:** **Scatter Plot**
    * **Use Case:** The classic plot for visualizing how one numerical variable changes with respect to another. Essential for spotting linear or non-linear trends.
    * **Tool:** `sns.scatterplot()`

* **Goal: See the relationship over a continuous interval, like time.**
    * **Plot:** **Line Plot**
    * **Use Case:** To track the change of a numerical variable over time or another continuous sequence.
    * **Tool:** `sns.lineplot()`

### ...and I have **Numerical vs. Categorical** data.

* **Goal: Compare the distribution of the numerical variable across the different categories.**
    * **Plot:** **Box Plot** or **Violin Plot**
    * **Use Case:** Excellent for comparing the spread, median, and outliers of a numerical variable for each category side-by-side. Violin plots provide more detail on the shape of the distribution.
    * **Tools:** `sns.boxplot()`, `sns.violinplot()`

* **Goal: Compare the average (or another central tendency) of the numerical variable across categories.**
    * **Plot:** **Bar Plot**
    * **Use Case:** To show the mean value of a numerical variable for each category, along with a confidence interval.
    * **Tool:** `sns.barplot()`

### ...and I have **Categorical vs. Categorical** data.

* **Goal: See the frequency of each combination of categories.**
    * **Plot:** **Heatmap** on a Crosstabulation
    * **Use Case:** To create a grid that shows the number of observations for each pair of categories.
    * **Tools:** `pd.crosstab()`, `sns.heatmap()`

---

## 📍 I want to analyze THREE OR MORE variables... (Multivariate Analysis)

### ...and I have **two Numerical variables and one Categorical variable.**

* **Goal: See the relationship between the numerical variables, separated by category.**
    * **Plot:** **Scatter Plot** with a `hue` parameter
    * **Use Case:** A standard scatter plot where the color (`hue`), size, or style of the points is determined by the third, categorical variable.
    * **Tool:** `sns.scatterplot(hue='categorical_column')`

### ...and I have **many Numerical variables.**

* **Goal: See all pairwise relationships in a single view.**
    * **Plot:** **Pair Plot**
    * **Use Case:** Creates a grid of scatter plots for every pair of numerical variables and a histogram for each variable on the diagonal. The ultimate tool for a quick overview of a dataset.
    * **Tool:** `sns.pairplot()`

* **Goal: See the correlation between all numerical variables.**
    * **Plot:** **Heatmap** of a Correlation Matrix
    * **Use Case:** To visualize the strength and direction of the linear relationship between every pair of numerical variables.
    * **Tools:** `df.corr()`, `sns.heatmap()`