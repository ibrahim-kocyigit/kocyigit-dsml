# Stage 5: Data Understanding

_"After the original data collection, data scientists typically use descriptive statistics and visualization techniques to understand the data content, assess data quality and discover initial insights about the data. Additional data collection may be necessary to fill gaps."_ - **John B. Rollins**

## Step 1: Load the Raw Data
Load the raw data files (collected in Stage 4) into your analytical environment (e.g., Python with pandas). Utilize functions from `{{cookiecutter.module_name}}.dataset` if applicable, to ensure consistency and reproducibility.

## Step 2: Perform Initial Data Inspection
Examine the basic structure of the data. Determine the number of rows (observations) and columns (features). Print the first few rows of the data to get a visual sense of the content.

## Step 3: Calculate Descriptive Statistics
Calculate descriptive statistics for each variable. For numerical variables, this includes measures like mean, median, standard deviation, min, max, and quartiles. For categorical variables, this includes frequency counts and unique value counts.

## Step 4: Create Data Visualizations
Generate visualizations to understand the distribution of individual variables and the relationships between variables. This includes histograms, box plots, scatter plots, and bar charts (for categorical variables). Use libraries like `matplotlib`, `seaborn`, or `plotly`. Store generated figures in `reports/figures`.

## Step 5: Assess Data Quality
Identify any data quality issues, such as missing values, outliers, inconsistencies, or unexpected values. Note these issues for further investigation and potential data cleaning in Stage 6.

## Step 6: Discover Initial Insights
Based on the descriptive statistics and visualizations, formulate initial insights and hypotheses about the data. Are there any interesting patterns, relationships, or anomalies? Do these insights align with the business understanding (Stage 1) and analytic approach (Stage 2)?

## Step 7: Document Findings
Document all findings, including descriptive statistics, visualizations, data quality issues, and initial insights.

