# Seaborn Cheat Sheet

```python
# Import seaborn and set the default theme
import seaborn as sns
sns.set_theme()
```

**Relational Plot**
```python
# Create a relational plot with multiple attributes
sns.relplot(data=data, x='column_x', y='column_y', hue='column_hue', size='column_size', style='column_style')

# Create subplots for relational plots based on a column
sns.relplot(data=data, x='column_x', y='column_y', hue='column_hue', col='col_var')
plt.show()
```
**Heatmap**
```python
# Create a heatmap with annotations
sns.heatmap(data, annot=True, cmap='coolwarm')

# Create a heatmap with line spacing and custom colors
sns.heatmap(data, annot=True, linewidths=0.5, cmap='Blues')
```
**Pair Plots**
```python
# Create pair plots for all combinations of features
sns.pairplot(data)

```
**Violin Plot**
```python
# Create a violin plot to visualize data distribution
sns.violinplot(x='x_var', y='y_var', data=data)
```
**Joint Plot**
```python
sns.jointplot(x='x_var', y='y_var', data=data, kind='reg')
```

---

##### __Source: [Dataquest](https://www.dataquest.io/cheat-sheet/matplotlib-cheat-sheet/)__