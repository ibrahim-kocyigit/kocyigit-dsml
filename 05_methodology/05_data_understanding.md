# Stage 5: Data Understanding

_"After the original data collection, data scientists typically use descriptive statistics and visualization techniques to understand the data content, assess data quality and discover initial insights about the data. Additional data collection may be necessary to fill gaps."_ — **John B. Rollins**

---

## Purpose

You have data. Now you need to **understand** it before doing anything with it.

This stage is Exploratory Data Analysis (EDA) — the systematic process of examining your `/data/interim/` dataset from [Stage 4](./04_data_collection.md) using descriptive statistics and visualizations. The goal is to answer three questions:

1. **What's in the data?** — Shape, types, distributions, ranges, categories.
2. **What's wrong with the data?** — Missing values, outliers, inconsistencies, class imbalance.
3. **What's interesting in the data?** — Patterns, correlations, separability, surprises.

The answers directly inform what you'll do in [Stage 6: Data Preparation](./06_data_preparation.md) — you can't decide how to handle missing values until you know where they are and why. You can't decide whether to scale features until you see their ranges.

> 💡 **Freelancer's note:** This is often the most valuable stage for the client. A well-crafted EDA summary — with clear charts and plain-language insights — can be a standalone deliverable. Even if the modeling stage hasn't started, the client already sees value.

---

## Step 1: First Look

Load the interim dataset and get a structural overview. No visualizations yet — just numbers.

**Actions:**
- Load the interim dataset from `/data/interim/`.
- Run structural checks to understand the shape and types of the data.

**Toolkit:**

| Method | What It Shows |
| :--- | :--- |
| `df.shape` | Number of rows and columns |
| `df.info()` | Column names, dtypes, non-null counts |
| `df.head()` / `df.sample(5)` | Actual values — sanity check |
| `df.dtypes.value_counts()` | Balance of numeric vs. categorical vs. other types |
| `df.duplicated().sum()` | Number of duplicate rows |

> 📚 **Reference:** See [Pandas Fundamentals](../02_toolkit/03_pandas_fundamentals/) for all inspection methods.

```markdown
## First Look
* **Dataset:** [Path to interim file]
* **Shape:** [Rows × Columns]
* **Column Types:** [X numeric, Y categorical, Z datetime]
* **Duplicates:** [Count]
* **Observations:** [Anything surprising — unexpected columns, wrong types, etc.]
```

---

## Step 2: Missing Value Assessment

Understand the extent and pattern of missing data. This is critical because your handling strategy in [Stage 6](./06_data_preparation.md) depends entirely on *why* data is missing.

**Actions:**
- Calculate the percentage of missing values per column.
- Identify whether missingness is **random** or **systematic**.
- Decide which columns are usable and which may need to be dropped.

**Toolkit:**

| Method | What It Shows |
| :--- | :--- |
| `df.isnull().sum()` | Absolute missing count per column |
| `df.isnull().mean() * 100` | Missing percentage per column |
| `msno.matrix(df)` | Visual pattern of missingness (requires `missingno` library) |

```markdown
## Missing Values
| Column | Missing Count | Missing % | Pattern / Notes |
| :--- | :--- | :--- | :--- |
| [column_name] | [count] | [%] | [Random / Systematic / Notes] |

Example:
| last_login_date | 14,498 | 30.0% | Systematic — all missing for customers who signed up before the tracking system was added (pre-2024). |
| monthly_spend | 212 | 0.4% | Appears random — scattered across all segments. |

* **Decision Preview:** [How you plan to handle these in Stage 6]
  Example: "last_login_date will be imputed with signup_date for pre-2024 users.
  monthly_spend will be imputed with median."
```

---

## Step 3: Descriptive Statistics

Compute summary statistics to get a quantitative overview of every column.

**Actions:**
- Generate `df.describe()` for numerical features (count, mean, std, min, quartiles, max).
- Generate `df.describe(include=['object', 'category'])` for categorical features.
- Look for signals: extreme ranges, zero standard deviation, unexpected min/max values.

**What to look for:**

| Signal | What It Means | Example |
| :--- | :--- | :--- |
| `min` or `max` far from quartiles | Potential outliers | `income`: Q3 = $80k, max = $12M |
| `std = 0` | Constant column — no information | `country` = "DE" for all rows |
| `count` < total rows | Missing values (confirms Step 2) | |
| `unique = 1` for categorical | Useless feature — drop it | |
| Large gap between `mean` and `50%` (median) | Skewed distribution | `mean = $150k`, `median = $65k` |

> 📚 **Reference:** See [Fitting Statistical Models — Considerations for Statistical Modeling](../03_specializations/01_fitting_statistical_models_to_data_with_python/01_considerations_for_statistical_modeling/) for the statistical theory behind distributions and summary statistics.

```markdown
## Descriptive Statistics Summary
* **Numerical Features:** [Paste or summarize df.describe() output]
* **Categorical Features:** [Paste or summarize df.describe(include='object') output]

## Key Observations
* [List 3–5 notable findings from the statistics]
  Example: "monthly_spend ranges from $0 to $12,450 — the max is likely an outlier."
  Example: "plan_type has 3 categories: Basic (60%), Premium (30%), Enterprise (10%)."
  Example: "tenure_months has a std of 14.2, meaning high variance in customer age."
```

---

## Step 4: Univariate Analysis

Examine each variable **individually** to understand its distribution.

**Actions:**
- Visualize the target variable distribution (class balance for classification, spread for regression).
- Visualize numerical features: histograms, KDE plots, boxplots.
- Visualize categorical features: count plots, value counts bar charts.

**What to look for:**

| For | Look For | Implication |
| :--- | :--- | :--- |
| **Target (classification)** | Class imbalance (e.g., 95% / 5%) | May need resampling, class weights, or a different metric — revisit [Stage 2](./02_analytic_approach.md) |
| **Target (regression)** | Skewed distribution | May need log-transform |
| **Numerical features** | Skewness, outliers, multimodality | Informs scaling/transformation choices in Stage 6 |
| **Categorical features** | High cardinality (too many categories) | May need grouping or encoding strategy |

> 📚 **Reference:** See [Matplotlib Fundamentals](../02_toolkit/04_matplotlib_fundamentals/) and [Seaborn Fundamentals](../02_toolkit/05_seaborn_fundamentals/) for `histplot`, `kdeplot`, `countplot`, and `boxplot`.

```markdown
## Univariate Analysis

## Target Variable
* **Distribution:** [Balanced / Imbalanced / Skewed / Normal]
  Example (classification): "churned: 85% No, 15% Yes — moderately imbalanced."
  Example (regression): "sale_price is right-skewed with a long tail above $500k."

## Feature Distributions
* [List 3–5 key findings per feature type]
  Example: "monthly_spend is right-skewed — consider log-transform."
  Example: "plan_type: Basic dominates at 60%, Enterprise is only 10%."
  Example: "age appears normally distributed, centered around 35."
```

---

## Step 5: Bivariate Analysis

Examine **pairs of variables** — especially the relationship between each feature and the target.

**Actions:**
- Compute and visualize the correlation matrix for numerical features.
- Visualize feature-vs-target relationships (boxplots, scatter plots, grouped bar charts).
- Check for multicollinearity (features that are highly correlated with *each other*).

**What to look for:**

| Analysis | Method | What It Reveals |
| :--- | :--- | :--- |
| Numeric ↔ Numeric | Correlation heatmap (`df.corr()`) | Linear relationships, multicollinearity |
| Numeric ↔ Target (classification) | Boxplot per class, violin plot | Feature separability across classes |
| Numeric ↔ Target (regression) | Scatter plot | Linear/non-linear relationship with target |
| Categorical ↔ Target (classification) | Grouped bar chart, crosstab | Category-level differences in target rate |
| Categorical ↔ Target (regression) | Boxplot per category | Differences in target distribution per group |

> 📚 **Reference:** See [Seaborn Fundamentals](../02_toolkit/05_seaborn_fundamentals/) for `heatmap`, `boxplot`, `scatterplot`, and `catplot`.

```markdown
## Bivariate Analysis

### Correlation Matrix
* **Highly correlated pairs (|r| > 0.7):**
  Example: "monthly_spend and total_transactions: r = 0.89 — likely multicollinear."

### Feature-Target Relationships
* [List key findings about how features relate to the target]
  Example (classification): "Boxplot shows churned customers have significantly lower
  monthly_spend (median $40 vs. $120 for retained)."
  Example (regression): "Scatter plot shows a clear positive linear relationship between
  lot_size and sale_price (r = 0.72)."

### Multicollinearity Concerns
* [List any pairs that may cause issues]
  Example: "monthly_spend and total_transactions are highly correlated. Consider dropping
  one or combining them in Stage 6."
```

---

## Step 6: EDA Findings Summary

Consolidate everything from Steps 1–5 into a structured summary. This becomes the input for [Stage 6: Data Preparation](./06_data_preparation.md) — every decision you make there should trace back to something you discovered here.

**Actions:**
- Summarize key insights (patterns, relationships, surprises).
- Summarize data quality issues (missing values, outliers, imbalance, multicollinearity).
- List implications for the next stage — what needs to be done in Data Preparation.

```markdown
## EDA Summary

### Key Insights
* [2–3 business-relevant patterns discovered]
  Example: "Customers on the Basic plan churn at 3x the rate of Premium customers."
  Example: "Properties built after 2010 sell for 25% more on average, controlling for size."

### Data Quality Issues
| Issue | Columns Affected | Severity | Planned Action (Stage 6) |
| :--- | :--- | :--- | :--- |
| Missing values | last_login_date (30%) | Medium | Impute with signup_date for pre-2024 |
| Outliers | monthly_spend (12 extreme values) | Low | Keep — appear to be legitimate high-value customers |
| Class imbalance | churned (85/15 split) | High | Apply SMOTE or class weights |
| Multicollinearity | monthly_spend ↔ total_transactions | Medium | Drop total_transactions |
| High cardinality | city (342 unique values) | Medium | Group into top 20 + "Other" |

## Revised Assumptions
* [Any initial assumptions from Stage 1 or Stage 2 that were challenged or confirmed]
  Example: "Stage 1 assumed customer tenure would be a strong predictor. EDA confirms this —
  churned customers have a median tenure of 4 months vs. 18 months for retained."
```

> 💡 **Freelancer's tip:** Share this summary with the client — even before modeling begins. A clear *"Here's what your data tells us"* builds trust and demonstrates progress. The client doesn't need to wait for a model to get value.

---

## Checklist

Before moving to [Stage 6: Data Preparation](./06_data_preparation.md), confirm:

- [ ] The interim dataset is loaded and structurally inspected.
- [ ] Missing values are quantified per column with patterns identified.
- [ ] Descriptive statistics are computed for all features.
- [ ] The target variable distribution is visualized (imbalance / skewness assessed).
- [ ] Key feature distributions are visualized (outliers, skewness, cardinality).
- [ ] Feature-target relationships are explored (separability, correlation).
- [ ] Multicollinearity is checked among features.
- [ ] All findings are summarized with planned actions for Stage 6.
- [ ] A non-technical summary is prepared for the client (optional but recommended).

---

**Next:** [Data Preparation](./06_data_preparation.md) — Transforming the data into a model-ready format based on everything discovered here.