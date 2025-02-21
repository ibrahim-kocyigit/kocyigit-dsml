# Folium Cheat Sheet

```python
import folium
```

**Map**
```python
# Create a map object with specified center coordinates and zoom level
map = folium.Map(location=[lat, lon], zoom_start=n)
```

**Marker**
```python
# Add a marker to the map with custom icon, popup, and tiles
# Tiles as Stamen Toner
folium.Marker(location=[lat, lon], popup='Marker Popup', tiles='Stamen Toner').add_to(map)

# Tiles as Stamen Terrain
folium.Marker(location=[lat, lon], popup='Marker Popup', tiles='Stamen Terrain').add_to(map)
```

**Circle**
```python
# Add a circle to the map with specified radius, color, and fill opacity
folium.features.CircleMarker(location=[lat, lon], radius=n, color='red', fill_opacity=n).add_to(map)
```

**Choropleth**
```python
# Create a choropleth map based on a GeoJSON file and a specified data column
folium.Choropleth(geo_data='path/to/geojson_file', data=df, columns=['region', 'value_column'], key_on='feature.properties.id', fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2, legend_name='Legend').add_to(map)
```