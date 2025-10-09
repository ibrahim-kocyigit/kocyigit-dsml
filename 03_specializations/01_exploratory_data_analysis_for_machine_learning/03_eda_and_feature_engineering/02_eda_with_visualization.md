# EDA with Visualization

## Data Visualization Libraries

- **Matplotlib:**  
  - The foundational plotting library in Python.
  - Highly flexible and feature-rich for creating custom plots and graphs.
- **Pandas Plotting:**  
  - Convenient wrapper around matplotlib for quick plotting from DataFrames.
  - Easier and faster for simple plots, but less flexible than raw matplotlib.
- **Seaborn:**  
  - Built on top of matplotlib.
  - Provides beautiful, statistical plots with shorthand methods (e.g., pair plots, regression plots).
  - Once imported, Seaborn's style is applied to matplotlib plots as well.

## Creating Plots

### Scatter Plots with Matplotlib

```python
import matplotlib.pyplot as plt

plt.plot(data['sepal_length'], data['sepal_width'], ls='', marker='o', label='sepal')
plt.plot(data['petal_length'], data['petal_width'], ls='', marker='o', label='petal')
plt.legend()
plt.show()
```
- Use `ls=''` for no lines, `marker='o'` for dots.
- Multiple calls to `plt.plot` overlay different data.

### Histograms

```python
plt.hist(data['sepal_length'], bins=20)
plt.show()
```
- Shows the distribution of a single variable.

### Object-Oriented Matplotlib

```python
fig, ax = plt.subplots()
ax.barh(range(10), data['sepal_width'][:10])
ax.set_yticks(range(1, 11))
ax.set_yticklabels(range(1, 11))
ax.set(xlabel='x label', ylabel='y label', title='title')
plt.show()
```
- More control over plot elements.

### Pandas Plotting

```python
data.groupby('species').mean().plot(
    color=['red', 'blue', 'black', 'green'],
    fontsize=10,
    figsize=(4, 4)
)
plt.show()
```
- Quick way to plot group statistics.

### Seaborn Visualizations

- **Pair Plot:**
    ```python
    import seaborn as sns
    sns.pairplot(data, hue='species', height=2)
    plt.show()
    ```
    - Shows scatter plots and histograms for all feature pairs, colored by category.

- **Hexbin Plot (Joint Plot):**
    ```python
    sns.jointplot(x='sepal_length', y='sepal_width', data=data, kind='hex')
    plt.show()
    ```
    - Shows density of points and marginal histograms.

- **Facet Grid:**
    ```python
    g = sns.FacetGrid(data, col='species', margin_titles=True)
    g.map(plt.hist, 'sepal_width')
    plt.show()
    ```
    - Creates separate plots for each category.

---

**Next:** [Grouping Data for EDA](./03_grouping_data_for_eda.md)