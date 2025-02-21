# Matplotlib Cheat Sheet

* [1. Importing Libraries](#1-importing-libraries)
* [2. Basic Plotting with Matplotlib](#2-basic-plotting-with-matplotlib)
* []()
* []()
* []()
* []()
* []()
* []()


## 1. Importing Libraries
```python
# Import pyplot module using an alias
import matplotlib.pyplot as plt

# Import seaborn and set the default theme
import seaborn as sns
sns.set_theme()

# Import pandas using its common alias
import pandas as pd

# Apply the fivethirtyeight predefined style
import matplotlib.style as style
style.use('fivethirtyeight')
```


## 2. Basic Plotting with Matplotlib
**Line Plot**
```python
# Plot a basic line graph
plt.plot(x_values, y_values)
plt.show()

# Plot multiple graphs on the same figure
plt.plot(x_values_1, y_values_1)
plt.plot(x_values_2, y_values_2)
plt.show()

# Plot graphs in separate figures
plt.plot(x_values_1, y_values_1)
plt.show()
plt.plot(x_values_2, y_values_2)
plt.show()

# Customize line color and style
plt.plot(x_values, y_values, color='blue', linestyle='--')
plt.show()
```
**Scatter Plot**
```python
# Create a scatter plot of points
plt.scatter(x_values, y_values)
plt.show()

# Customize point color and size
plt.scatter(x_values, y_values, c='red', s=100)
plt.show()
```
**Bar Plot**
```python
# Create a vertical bar chart
plt.bar(x=x_values, height=heights)
plt.show()

# Create a stacked bar chart
plt.bar(x, height, bottom=previous_heights)
plt.show()

# Create a horizontal bar chart
plt.barh(y=y_values, width=widths)
plt.show()

# Customize bar colors and borders
plt.bar(x, width, color='purple', edgecolor='black')
plt.show()
```
**Histogram**
```python
# Create a histogram for a dataset
plt.hist(data_column)
plt.show()

# Customize bin count and color
plt.hist(data_column, bins=30, color='orange')
plt.show()
```
**Area Plot**
```python
# Create an area plot shaded between y1 and y2
plt.fill_between(x, y1=lower, y2=upper)
plt.show()
```
**Pie Chart**
```python
# Create a pie chart with percentages
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
```

## Section
****
```python

```

## Section
****
```python

```

## Section
****
```python

```

## Section
****
```python

```

## Section
****
```python

```

## Section
****
```python

```

## Section
****
```python

```

---

__Source: []()__