# Data Visualization

* [1. Importing Libraries](#1-importing-libraries)
* [2. Basic Plotting with Matplotlib](#2-basic-plotting-with-matplotlib)
* [3. Customization](#3-customization)
* [4. Grid Charts](#4-grid-charts)
* [5. Advanced Plot Customization](#5-advanced-plot-customization)
* [6. Pandas Visualization](#6-pandas-visualization)
* [7. Seaborn Visualizations](#7-seaborn-visualizations)


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

## 3. Customization
**Title**
```python
# Add a title to the plot
plt.title('Title')

# Customize title size and color
plt.title('Custom Title', fontsize=16, color='green')
```
**X and Y Labes**
```python
# Add a label to the x-axis
plt.xlabel('X-axis Label')

# Add a label to the y-axis
plt.ylabel('Y-axis Label')
```
**Legend**
```python
# Add a legend to the plot
plt.plot(x_values1, y_values1, label='Label 1') # Label will be showed in the legend
plt.plot(x_values2, y_values2, label='Label 2') # Label will be showed in the legend
plt.legend()
plt.show()

# Customize legend position and font size
plt.legend(loc='upper right', fontsize=10) 
plt.show()
```
**Grid**
```python
# Add gridlines to the plot
plt.grid(True)
```
**Set Ticks**
```python
# Customize the tick labels on the x-axis
plt.xticks(ticks=x_values, labels=labels)

# Rotate the x-axis tick labels
plt.xticks(rotation=45)

# Customize the tick labels on the y-axis
plt.yticks(ticks=y_values, labels=labels)

# Rotate the y-axis tick labels
plt.yticks(rotation=30)
```
**Tick Label Format**
```python
# Change scientific notation to plain text
plt.ticklabel_format(axis='both', style='plain')
```
**Colorbar**
```python
# Use a colormap in the scatter plot
plt.scatter(x, y, c=values, cmap='viridis')
plt.colorbar()

# Use a different colormap
plt.scatter(x, y, c=values, cmap='coolwarm')
plt.colorbar()
```
**Annotate**
```python
# Add text and an arrow annotation on the plot
plt.annotate(
    'Text', xy=(x, y),
     xytext=(x_offset, y_offset),
     arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

## 4. Grid Charts
**Figure**
```python
# Create two subplots in a 1-row, 2-column grid
plt.figure(figsize=(8, 3))
plt.subplot(1, 2, 1)
plt.subplot(1, 2, 2)
plt.show()
```
**Subplot**
```python
# Create a 3-row, 2-column grid of subplots
plt.figure(figsize=(10, 12))
for i in range(1, 7):
    plt.subplot(3, 2, i)
    plt.plot(x_values, y_values)
plt.show()
```
**Subplots**
```python
# Create a grid of 4 vertically stacked subplots
fig, axes = plt.subplots(nrows=4, ncols=1)

# Create a 2x2 grid of subplots and assign plots to specific axes
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].plot(x_values1, y_values1)
axes[1, 1].plot(x_values2, y_values2)
plt.show()
```

## 5. Advanced Plot Customization
**Subplots**
```python
# Create a bar chart using the object-oriented approach
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x, height)
plt.show()
```
**Spines**
```python
# Remove all borders (spines) from the plot
for location in ['left', 'right', 'bottom', 'top']:
    ax.spines[location].set_visible(False)
```
**Tick Customizations**
```python
# Hide specific ticks and change tick colors
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')

# Move x-tick labels to the top of the plot
ax.xaxis.tick_top()

# Set custom tick locations on the x-axis
ax.set_xticks([0, 150, 300])

# Set custom tick labels on the x-axis
ax.set_xticklabels(['0', '150', '300'])
```
**Text**
```python
# Add custom text to a specific position on the plot
ax.text(x, y, 'Sample Text', fontsize=12, color='blue')
```
**Add Vertical and Horizontal Lines to Axes**
```python
# Add a vertical line at a specified x-position with customization
ax.axvline(x=5, color='red', linewidth=2)

# Add a horizontal line at a specified y-position with customization
ax.axhline(y=3, color='green', linestyle='--')
```

## 6. Pandas Visualization
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

## 7. Seaborn Visualizations
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