# 6. Pandas Visualization Cheat Sheet

```python
import pandas as pd
import matplotlib.pyplot as plt

# Apply the fivethirtyeight predefined style
import matplotlib.style as style
style.use('fivethirtyeight')
```

**Line Plot (Series)**
```python
# Create a line plot from a Series
Series.plot.line(color='green', linestyle='--')
plt.show()
```
**Line Plot (DataFrame)**
```python
# Create a line plot from a DataFrame
DataFrame.plot.line(x='column_1', y='column_2')
plt.show()
```
**Scatter Plot (DataFrame)**
```python
# Create a scatter plot from a DataFrame
DataFrame.plot.scatter(x='column_1', y='column_2', color='red', s=50)
plt.show()
```
**Histogram (Series)**
```python
# Create a histogram from a Series
Series.plot.hist(bins=20)
plt.show()

# Create a cumulative histogram
Series.plot.hist(cumulative=True, bins=30)
plt.show()
```
**Bar Plot (Series)**
```python
# Create a vertical bar chart from a Series
Series.plot.bar()
plt.show()

# Create a horizontal bar chart from a Series
Series.plot.barh()
plt.show()

# Customize bar colors and borders
Series.plot.bar(color='orange', edgecolor='black')
plt.show()
```
**Box Plot**
```python
# Create a boxplot to visualize data distributions
DataFrame.plot.box()
plt.show()
```
**Multiple Plot by Category**
```python
# Create one plot per category
DataFrame.plot.line(x='col_x', y='col_y', by='col_category') # Works with .hist() and .box() too
plt.show()
```

---

##### __Source: [Dataquest](https://www.dataquest.io/cheat-sheet/matplotlib-cheat-sheet/)__