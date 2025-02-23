# PyWaffle Cheat Sheet

```python
from pywaffle import Waffle
```

**Waffle**
```python
# Create a waffle chart based on values and categories
plt.figure(FigureClass=Waffle, rows=20, columns=30, values=df['col'], cmap_name='tab20', legend={'labels': label, 'loc': 'lower left', 'bbox_to_anchor': (0, -0.1), 'ncol': 3})
```

**Legend**
```python
# Add a legend to the waffle chart 
waffle_chart.legend(loc='upper left', bbox_to_anchor=(1, 1))
```

**Title**
```python
# Add a title to the waffle chart
waffle_chart.set_title('Waffle Chart Title')
```

**Labels**
```python
# Add labels to the waffle chart
waffle_chart.set_labels(['Label 1', 'Label 2', ...])
```