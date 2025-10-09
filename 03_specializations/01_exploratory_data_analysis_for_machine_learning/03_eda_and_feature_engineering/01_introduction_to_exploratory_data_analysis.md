# Introduction to Exploratory Data Analysis (EDA)

- EDA is the process of analyzing datasets to summarize their main characteristics, often using visual methods and statistical summaries.
- Think of EDA as your "initial conversation" with the data—getting to know its structure, quality, and patterns before modeling.

## Why is EDA Useful?

- Helps determine if the data makes sense, needs further cleaning, or if more data is required.
- Identifies patterns, trends, and potential issues (e.g., outliers, missing values).
- Sometimes, insights from EDA are as important as those from modeling.

## Common EDA Techniques

### Statistical Summaries

- **Average (mean), median, min, max**, etc.
- **Correlations** between columns

### Visualizations

- **Histograms:** Show distribution of a variable
- **Scatter plots:** Show relationships between two variables
- **Box plots:** Show distribution and identify outliers

- **Tools:**  
  - Use `pandas` for data wrangling and summary statistics.
  - Use `matplotlib` and `seaborn` for visualizations.

## Example: EDA for Job Applicants

- Calculate average interview scores, possibly by city or job function.
- Find the most common words in application materials (mode).
- Analyze correlations between technical assessments and years of experience, possibly broken down by experience type.

## Sampling from DataFrames

- **Why sample?**
  - For large datasets, sampling can make analysis faster and more manageable.
  - Useful for creating training and testing sets.
  - Stratified sampling ensures that important proportions (e.g., rare outcomes) are preserved in the sample.

- **How to sample in pandas:**
    ```python
    # Take a random sample of 5 rows from a DataFrame
    sample = data.sample(n=5, replace=False)
    # Show the last three columns of the sample
    print(sample.iloc[:, -3:])
    ```

## Summary

- EDA is a crucial first step in any data analysis or machine learning workflow.
- Use both statistical and visual techniques to understand your data.
- Sampling helps manage large datasets and maintain important proportions in your analysis.

---

**Next:** [EDA with Visualization](./02_eda_with_visualization.md)