# Stage 6: Data Preparation

_"This stage encompasses all activities to construct the data set that will be used in the subsequent modeling stage. Data preparation activities include data cleaning (dealing with missing or invalid data) and combining data from multiple data sources."_ — John B. Rollins

_"In a process called feature engineering, data scientists can create additional explanatory variables, also referred to as predictors or features, through a combination of domain knowledge and existing variables."_ — John B. Rollins

---

## Purpose

This is the bridge between *understanding* data and *modeling* it. Every data quality issue and pattern discovered in [Stage 5](./05_data_understanding.md) is now acted upon.

The output of this stage is a **split, cleaned, and feature-engineered dataset** — saved to `/data/processed/` as `train_df` and `test_df`. These DataFrames contain all columns (features + target) so that [Stage 7: Modeling](./07_modeling.md) has full flexibility to select features, encode, and scale differently per model using scikit-learn Pipelines.

**What belongs in this stage (safe before the split or applied using domain rules only):**

- Removing impossible values (domain-rule-based)
- Handling missing values via domain logic (not statistical imputation)
- Feature engineering (creating new columns from existing ones)
- Dropping useless columns (constants, IDs, leaky features)
- Train/test split
- Flagging statistical imputation, encoding, and scaling decisions — but **not executing them**

**What does NOT belong in this stage (moves to [Stage 7](./07_modeling.md) inside Pipelines):**

- Statistical imputation (mean, median, mode) — uses data-derived statistics
- Outlier capping/winsorization (percentile-based) — uses data-derived thresholds
- Encoding categorical variables (one-hot, ordinal, target) — different models need different encodings
- Feature scaling (standard, minmax, robust) — different models need different scaling
- X/y separation — different models may use different feature subsets

> 💡 **Why this separation?** Different candidate models have different preprocessing requirements. Tree-based models (Random Forest, XGBoost) don't need scaling but work well with ordinal encoding. Linear models (Logistic Regression, Ridge) need scaling and one-hot encoding. By deferring these steps to Stage 7, each model gets a tailored Pipeline — and there's zero risk of data leakage from fitting statistics on the test set.

> 💡 **Freelancer's note:** Rollins is right — data preparation is usually the most time-consuming stage. In a typical freelance project, it takes 60–80% of the total effort. Don't rush it. The quality of your preparation directly determines the quality of your models.

---

## Step 1: Handle Impossible Values & Domain-Rule Cleaning

Address data quality issues that can be resolved using **domain knowledge alone** — no data-derived statistics needed. These are safe to apply before the train/test split because the rules come from business logic, not from the data itself.

**Actions:**
- Remove or nullify values that are impossible according to domain rules.
- Handle missing values where a clear business rule exists.
- Document every decision and its justification.

**What's safe here (domain-rule-based):**

| Action | Example | Why It's Safe |
| :--- | :--- | :--- |
| **Nullify impossible values** | `age = -5` → `NaN`, `rating = 11` (scale 1–10) → `NaN` | Uses domain knowledge, not data statistics |
| **Impute with domain logic** | `last_login` → fill with `signup_date` for pre-2024 users | Business rule, not statistical |
| **Fill known defaults** | `country` is `NaN` for a dataset that's all German customers → `"DE"` | Domain knowledge |
| **Flag + nullify** | Create `has_login_date` (0/1), then set original to `NaN` if missing | The flag is a domain-based binary indicator |
| **Drop clearly useless rows** | Rows where the target variable is `NaN` and cannot be derived | Can't train on these regardless |

**What is NOT safe here (defer to Stage 7 Pipelines):**

| Action | Example | Why It Must Wait |
| :--- | :--- | :--- |
| **Impute with mean/median/mode** | `monthly_spend` → fill with median | Median is a data-derived statistic — must be computed on training set only |
| **Cap outliers at percentiles** | Cap at 1st/99th percentile | Percentiles are data-derived — must be computed on training set only |
| **Replace outliers with mean** | `monthly_spend` outliers → replace with mean | Mean is data-derived |

```markdown
## Domain-Rule Cleaning
| Column | Issue | Action | Justification |
| :--- | :--- | :--- | :--- |
| [column] | [What was wrong] | [What you did] | [Why — domain rule used] |

Example:
| age | 3 values < 0 | Set to NaN | Age cannot be negative — data entry error |
| last_login_date | 30% missing (pre-2024 users) | Filled with signup_date | Business rule: pre-2024 users lack tracking, signup_date is the best proxy |
| monthly_spend | 0.4% missing, random | Left as NaN | No domain rule applies — will be imputed statistically in Stage 7 Pipeline |
| rating | 5 values > 10 | Set to NaN | Scale is 1–10, values above are entry errors |
```

> ⚠️ **Key principle:** If the fix requires computing a statistic from the data (mean, median, percentile, mode, frequency), it does **not** belong here. It belongs inside a scikit-learn Pipeline in [Stage 7](./07_modeling.md), where it will be fit on the training set only.

---

## Step 2: Feature Engineering

Create new features that capture information the raw columns don't directly express. This is where domain knowledge meets data — and where the best models are often won.

Feature engineering is safe before the split because you're creating **deterministic transformations** — each row's new value depends only on that row's own data, not on aggregate statistics from other rows.

**Actions:**
- Create new features based on patterns discovered in [Stage 5](./05_data_understanding.md).
- Use domain knowledge from the [Stage 1](./01_business_understanding.md) stakeholder meetings.

**Common Engineering Patterns:**

| Pattern | Example | Applicable To |
| :--- | :--- | :--- |
| **Date extraction** | `signup_date` → `tenure_months`, `signup_quarter` | Any project with dates |
| **Aggregation** | Per-customer: `total_orders`, `avg_order_value` | Transaction-level → customer-level |
| **Interaction** | `price × quantity` = `total_revenue` | When two features combine meaningfully |
| **Binning** | `age` → `age_group` (18–25, 26–35, ...) | When non-linear relationships exist |
| **Ratios** | `support_tickets / tenure_months` = `ticket_rate` | When relative values matter more than absolutes |
| **Boolean flags** | `has_premium_addon`, `is_weekend`, `made_purchase_last_30d` | When a binary signal is cleaner than the raw data |
| **Text extraction** | `email` → `email_domain` → `is_corporate_email` | When text contains categorical signal |

```markdown
## Engineered Features
| New Feature | Derivation | Justification |
| :--- | :--- | :--- |
| [feature_name] | [How it was created] | [Why it should help the model] |

Example:
| tenure_months | (observation_date - signup_date).days / 30 | EDA showed strong correlation with churn |
| ticket_rate | support_tickets / tenure_months | Normalizes ticket count by customer age |
| is_weekend | order_day_of_week in (Sat, Sun) | EDA showed higher churn for weekend signups |
```

> ⚠️ **Note on log-transforms:** A simple `np.log1p(income)` applied row-by-row is safe before the split — it doesn't use any aggregate statistics. However, if you're applying a `PowerTransformer` (which fits parameters from data), that must go inside a Stage 7 Pipeline.

---

## Step 3: Drop Useless Columns

Remove columns that provide no predictive value or would cause problems in modeling.

**Actions:**
- Drop columns identified as useless in [Stage 5](./05_data_understanding.md).
- Drop ID columns, constant columns, and any columns that leak the target.

**What to drop:**

| Reason | Example | How to Identify |
| :--- | :--- | :--- |
| **ID columns** | `customer_id`, `row_index` | Unique per row, no predictive value |
| **Constant columns** | `country` = "DE" for all rows | `df.nunique() == 1` |
| **Near-constant columns** | A column where 99.9% of values are the same | `df[col].value_counts(normalize=True).iloc[0] > 0.999` |
| **Target leakage** | `cancellation_date` when predicting churn | Directly reveals the target — would not exist at prediction time |
| **High missing (no fix)** | Column with 80% missing and no imputation strategy | Discussed in Stage 5 |
| **Redundant after engineering** | `signup_date` after creating `tenure_months` | Original no longer needed |

```markdown
## Dropped Columns
| Column | Reason |
| :--- | :--- |
| [column] | [Why it was dropped] |

Example:
| customer_id | ID column — no predictive value (saved separately for joining results) |
| country | Constant — all values are "DE" |
| cancellation_date | Target leakage — directly reveals churn status |
| signup_date | Redundant — replaced by tenure_months |
```

> 💡 **Tip:** If you need `customer_id` later (e.g., to join predictions back to customer records), save it separately before dropping it from the modeling dataset.

---

## Step 4: Train/Test Split

Separate the data into training and testing sets. This is done **before** any statistical preprocessing (imputation, encoding, scaling) to prevent data leakage.

**Actions:**
- Apply the split strategy defined in [Stage 2](./02_analytic_approach.md).
- Keep both splits as **complete DataFrames** (`train_df`, `test_df`) — do not separate into X/y yet.
- Verify the split is correct (shapes, class proportions if stratified).

**Why `train_df` / `test_df` instead of `X_train` / `X_test` / `y_train` / `y_test`?**

In [Stage 7](./07_modeling.md), different candidate models may use:
- Different feature subsets
- Different encoding strategies (one-hot for linear models, ordinal for trees)
- Different scaling (StandardScaler for Logistic Regression, none for XGBoost)

Keeping complete DataFrames gives Stage 7 full flexibility to define X and y per model.

```markdown
## Train/Test Split
* **Split Strategy:** [From Stage 2]
  Example: "80/20 stratified split (random_state=42)"
  Example: "Time-based split — train on data before 2025-01, test on 2025-01 onward."

* **Shapes:**
  - train_df: [rows × cols]
  - test_df:  [rows × cols]

* **Class Distribution (if classification):**
  - Train: [class 0: X%, class 1: Y%]
  - Test:  [class 0: X%, class 1: Y%]

* **Target Column:** [Name — still present in both DataFrames]
  Example: "churned"
```

> ⚠️ **Critical rule:** Everything after this step — statistical imputation, outlier capping, encoding, scaling — must be computed on `train_df` only and applied to both `train_df` and `test_df`. This is handled inside scikit-learn Pipelines in [Stage 7](./07_modeling.md).

---

## Step 5: Plan Preprocessing for Stage 7

You won't execute these steps here, but documenting the plan now — based on your [Stage 5 EDA findings](./05_data_understanding.md) — ensures a smooth transition to modeling.

**Actions:**
- For each column that still needs statistical preprocessing, document the planned strategy.
- Note which strategies differ by model type.

### Missing Values (Statistical Imputation)

| Column | Missing % | Planned Strategy | Notes |
| :--- | :--- | :--- | :--- |
| [column] | [%] | [mean / median / mode / KNN / etc.] | [Will be inside Pipeline] |
| monthly_spend | 0.4% (after domain cleaning) | Median imputation | Skewed distribution — median is more robust |
| city | 2% | Mode imputation | Most common value |

### Outlier Handling (Data-Derived)

| Column | Outlier Description | Planned Strategy | Notes |
| :--- | :--- | :--- | :--- |
| [column] | [What was flagged] | [Cap / Winsorize / Log-transform via PowerTransformer] | [Will be inside Pipeline] |
| monthly_spend | 12 values > $10,000 | Keep for tree models, cap at 99th percentile for linear models | Strategy differs by model type |
| sale_price | Heavy right skew | PowerTransformer (Yeo-Johnson) for linear models | Trees handle skew naturally |

> ⚠️ **Note on outlier handling:** Capping at a percentile, replacing with mean/median, or fitting a PowerTransformer all use data-derived statistics. These **must** be fit on the training set only, inside a Pipeline. Removing obvious errors (e.g., `age = -5` → NaN) was already handled in Step 1 using domain rules.

### Encoding

| Column | Cardinality | Planned Encoding | Notes |
| :--- | :--- | :--- | :--- |
| [column] | [unique values] | [One-Hot / Ordinal / Target / Binary] | [May differ by model] |
| plan_type | 3 | One-Hot for linear models, Ordinal for trees | Different models, different encodings |
| city | 342 | Target Encoding for all models | Too many categories for one-hot |
| risk_level | 3 (ordered) | Ordinal for all models | Natural order: Low=0, Medium=1, High=2 |

### Scaling

| Scaler | When to Use | Planned For |
| :--- | :--- | :--- |
| `StandardScaler` | Features roughly normal | Logistic Regression, SVM, KNN |
| `RobustScaler` | Features have outliers | Linear models when outliers are kept |
| None | Tree-based models | Random Forest, XGBoost |

> 📚 **Reference:** All of these preprocessing steps will be implemented inside scikit-learn Pipelines in [Stage 7: Modeling](./07_modeling.md). See [Machine Learning with Python — Introduction](../03_specializations/02_machine_learning_with_python/01_introduction_to_machine_learning/) for Pipeline construction.

```markdown
## Preprocessing Plan for Stage 7
* **Statistical Imputation Needed:** [List columns and strategies]
* **Outlier Capping Needed:** [List columns and strategies — note model-specific differences]
* **Encoding Needed:** [List columns and strategies — note model-specific differences]
* **Scaling Needed:** [Which scaler for which model type]
* **All above will be implemented inside scikit-learn Pipelines in Stage 7.**
```

---

## Step 6: Save Processed Data & Document

Save the train and test DataFrames and document every transformation for reproducibility.

**Actions:**
- Save `train_df` and `test_df` to `/data/processed/`.
- Document the full transformation chain from this stage.

```markdown
## Final Output
* **Processed Data Location:** /data/processed/
* **Files:**
  - train_df: /data/processed/train.parquet
  - test_df:  /data/processed/test.parquet

* **Final Shape:** train_df [rows × cols], test_df [rows × cols]
* **Target Column:** [Name — present in both files]

* **Transformation Summary (this stage only):**
  1. Domain-rule cleaning: [per Step 1 log]
  2. Engineered features: [list from Step 2]
  3. Dropped columns: [list from Step 3]
  4. Train/test split: [per Step 4]

* **Deferred to Stage 7 (inside Pipelines):**
  - Statistical imputation (mean/median/mode)
  - Outlier capping (percentile-based)
  - Categorical encoding (one-hot, ordinal, target)
  - Feature scaling (standard, minmax, robust)
  - X/y separation (per model's feature set)
```

---

## Checklist

Before moving to [Stage 7: Modeling](./07_modeling.md), confirm:

- [ ] Impossible values are removed using domain rules (not data-derived statistics).
- [ ] Missing values with clear domain-rule fixes are handled.
- [ ] Engineered features are created and justified.
- [ ] Useless columns are dropped (IDs, constants, leaky features).
- [ ] Train/test split is performed — both saved as complete DataFrames.
- [ ] Statistical preprocessing (imputation, capping, encoding, scaling) is **planned but not executed** — deferred to Stage 7 Pipelines.
- [ ] No data leakage exists in any transformation applied before the split.
- [ ] Processed data is saved to `/data/processed/` as `train.parquet` and `test.parquet`.
- [ ] Every transformation is documented and reproducible.

---

**Next:** [Modeling](./07_modeling.md) — Building per-model Pipelines and training the candidate models on the prepared data.