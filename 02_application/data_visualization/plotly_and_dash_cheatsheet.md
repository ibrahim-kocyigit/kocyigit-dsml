# Plotly and Dash Cheat Sheet

## Plotly Express
```python
import plotly.express as gx

# Create a scatter plot
px.scatter(dataFrame, x='column_x', y='column_y', title='title')

# Create a line plot
px.line()

# Create a bar plot
px.bar()

# Create a sunburst plot
px.sunburst(dataFrame, path=['col_1', 'col_2', ...], values='column')

# Create a histogram
px.hist(x=array_like)

# Create a bubble chart
px.scatter(dataFrame, x='column_x', y='column_y', size='column_size', hover_name='hover_text')

# Create a pie chart
px.pie(values=x_array_like, names=y_array_like)
```

## Plotly Graph Objects  
```python
import plotly.graph_objects as go

# Create a scatter plot
go.Scatter(x=x_array_like, y=y_array_like, mode='markers')

# Create a line plot
go.Scatter(x=x_array_like, y=y_array_like, mode='lines')

# Add additional traces to an existing figure
fig.add_trace(go.Scatter(x=x_array_like, y=y_array_like))

# Update the layout of a figure, such as title, axis labels, and annotations
fig.update_layout(title='Title', xaxis_title='X-axis Title', yaxis_title='Y-axis Title')
```

## Dash
```python
from dash import Dash, dcc, html, Input, Output


```