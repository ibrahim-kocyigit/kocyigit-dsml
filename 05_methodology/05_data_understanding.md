# Stage 5: Data Understanding

*"After the original data collection, data scientists typically use descriptive statistics and visualization techniques to understand the data content, assess data quality and discover initial insights about the data. Additional data collection may be necessary to fill gaps."* - **John B. Rollins**


## Purpose

The goal of this stage is to conduct Exploratory Data Analysis (EDA) to develop a deep understanding of the data's content, quality, and structure. Through descriptive statistics and visualization, we will identify patterns, detect anomalies, and test initial hypotheses. We start our work from the clean `interim` dataset produced in Stage 4.


## Step 1: Preparation for Exploratory Data Analysis (EDA)

Thanks to the ETL process in Stage 4, we are starting with a clean, standardized `interim` dataset. This first step in Data Understanding is therefore not about initial shaping, but about performing final preparatory checks and minor adjustments to ensure the DataFrame is perfectly suited for the analysis ahead.

* **Action:** Perform final checks and minor adjustments on the DataFrame.
* **Guiding Questions:**
    * Are there any columns that we are **100% sure** are not needed for the project and can be dropped? (Any columns that *might* be useful should be retained for now.)
    * Are there any obvious data type errors that need correction to ensure they are compatible with analytical and visualization libraries (e.g., converting strings to Pandas `category` type)?
    * Are there any obvious outliers that, upon inspection, appear to be data entry errors that may have slipped through the initial ETL?
    * Are there **fully** duplicated rows that can be safely removed?
* **Toolkit Connection:** This step uses basic Pandas functions like `.drop(columns=[])`, `.astype()`, `.to_datetime()`, and `.drop_duplicates()`. Column renaming (`.rename()`) should have already been handled in Stage 4.


```Markdown
### EDA Preparation Report
* [List all preparatory actions taken here. Example: "Converted `class_name` to a category type for more efficient memory usage", "Removed 2 fully duplicated rows", "No columns were dropped at this stage.".]
```


## Step 2: Descriptive Statistics

Compute summary statistics to get a high-level quantitative overview of the dataset.

* **Action:** Generate and analyze descriptive statistics for all numerical and categorical features.
* **Toolkit Connection:** This step primarily uses the `pandas.DataFrame.describe()` method.

```Markdown
### Descriptive Statistics

#### Numerical Feature Summary (`df.describe()`)
```[Paste the output of df.describe() for numerical columns here. Analyze the count, mean, std, min, max, and quartile values for initial insights into scale and spread.]```

#### Categorical Feature Summary (`df.describe(include=['object', 'category'])`)
```[Paste the output of df.describe(include=['object', 'category']) here. Analyze the count, unique values, top (most frequent) category, and frequency.]```
```

## Step 3: Univariate Analysis

Analyze individual variables to understand their own distributions and characteristics.

* **Action:** Create visualizations for key individual variables.
* **Guiding Questions:**
    * How is the target variable distributed?
    * What is the distribution of key numerical features (e.g., normal, skewed, bimodal)?
    * What are the frequency counts of key categorical features?
* **Toolkit Connection:** This step uses `seaborn.histplot`, `seaborn.kdeplot`, and `seaborn.countplot`.

```Markdown
### Univariate Analysis
[Embed or link to key visualizations, e.g., `univariate_plots.png`]

#### Key Observations from Univariate Analysis
* Note any findings. [Example: "The `price` feature is heavily right-skewed, suggesting a log transformation may be necessary in the data preparation stage."]
* [Example: "The target variable `species` is perfectly balanced, with 50 samples for each of the 3 classes."]
```

## Step 4: Bivariate Analysis

Analyze pairs of variables to investigate relationships and correlations.

* **Action:** Create visualizations to explore the relationships between features, and between features and the target variable.
* **Guiding Questions:**
    * How do numerical features correlate with each other? Is there multicollinearity?
    * How does the distribution of a numerical feature change across the different classes of the target variable?
    * Is there a linear or non-linear relationship between key numerical features?
* **Toolkit Connection:** This step uses `seaborn.scatterplot`, `seaborn.boxplot`, and `seaborn.heatmap` on a correlation matrix (`df.corr()`).

```Markdown
### Bivariate Analysis
[Embed or link to key visualizations, e.g., a correlation heatmap and several boxplots.]

#### Key Observations from Bivariate Analysis
* Note any findings. [Example: "There is a strong positive correlation (0.85) between `feature_A` and `feature_B`, suggesting potential multicollinearity."]
* [Example: "The box plot of `sepal_length` by `class_name` shows a clear separation between the species, indicating it will be a strong predictor."]
```

## Step 5: Initial Findings Summary

Consolidate all observations from the EDA into a summary.

* **Action:** Create a bulleted list of the most important insights and data quality issues discovered.

```Markdown
### Exploratory Data Analysis (EDA) Summary

#### Key Insights
* [List 2-3 of the most interesting business-relevant patterns found.]

#### Data Quality Issues
* [List any issues found, e.g., "The `last_login_date` column has 30% missing values." or "Detected significant outliers in the `order_value` column that appear to be natural variation."]

#### Revised Assumptions
* [Note any initial assumptions that were challenged or validated by the data.]
```

## Step 6: Final Review

Conclude the data understanding phase. Based on the findings (especially data quality issues), it may be necessary to revisit previous stages.

* **Action:** Prepare a brief summary report of the EDA findings for both technical and business stakeholders.
* **Action:** Add a summary of this stage to the main project `README.md`.

```Markdown
### Data Understanding Summary

* **Status:** [Completed]
* **Key Finding for Stakeholders:** [Translate one key insight into a simple business statement. Example: "Initial analysis shows that petal length and petal width are extremely strong indicators of the flower's species."]
* **Next Steps:** [Outline next steps. Example: "Proceed to Data Preparation stage. The discovered outliers will be kept, but feature scaling will be necessary due to differing ranges in measurements."]
```

---
**Next:** [Data Preparation](./06_data_preparation.md)