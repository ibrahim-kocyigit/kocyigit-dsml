# Data Preprocessing in Pandas

**1. Load CSV data:**
```python
# Read data from a CSV file into a Pandas DataFrame
pd.read_csv('filename.csv')
```
**2. Displaying First/Last n Rows:**
```python
# Show the first n rows of the DataFrame
df.head(n)

# Show the last n rows of the DataFrame
df.tail(n)
```
**3. Summary Statistics:**
```python
# Generate descriptive statistics for numerical columns
df.describe()
```
**4. Checking for Null Values:**
```python
# Check for null values in the DataFrame
df.isnull()
```
**5. Handling Missing Values:**
```python
# Drop rows with missing values
df.dropna()

# Fill missing values with a specified value
df.fillna(value)
```
**6. Removing Duplicates:**
```python
# Remove duplicate rows
df.drop_duplicates()
```
**7. Renaming Columns:**
```python
# Rename one or more columns
df.rename(columns={'old_name': 'new_name'})
```
**8. Selecting Columns:**
```python
# Select a single column
df['column_name']

# Select multiple columns
df[['col1', 'col2']]
```
**9. Filtering Rows:**
```python
# Filter rows based on a condition
df[df['column'] > value]
```
**10. Applying Functions to Columns:**
```python
# Apply a function to transform values in a column
df['column'].apply(function_name)
```
**11. Creating New Columns:**
```python
# Create a new column with values derived from existing ones
df['new_column'] = expression
```
**12. Grouping and Aggregating:**
```python
# Group rows by a column and apply aggregate functions
df.groupby('column').agg({'col1': 'sum', 'col2': 'mean'})
```
**13. Sorting Rows:**
```python
# Sort rows based on a column
df.sort_values('column', ascending=True/False)
```
**14. Selecting Rows by Index:**
```python
# Select rows based on integer index
df.iloc[index]

# Select rows in a specified range
df.iloc[start:end]
```
**15. Selecting Rows by Label:**
```python
# Select rows based on label/index name
df.loc[label]

# Select rows in a specified label/index range
df.loc[start:end]
```