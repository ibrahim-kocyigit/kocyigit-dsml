# Stage 6: Data Preparation

_"This stage encompasses all activities to construct the data set that will be used in the subsequent modeling stage. Data preparation activities include data cleaning (dealing with missing or invalid values, eliminating duplicates, formatting properly), combining data from multiple sources (files, tables, platforms) and transforming data into more useful variables._

_"In a process called feature engineering, data scientists can create additional explanatory variables, also referred to as predictors or features, through a combination of domain knowledge and existing structured variables... Data preparation is usually the most time-consuming step in a data science project."_ — **John B. Rollins**

---

## Purpose

This is the bridge between *understanding* data and *modeling* it. Every data quality issue and pattern discovered in [Stage 5](./05_data_understanding.md) is now acted upon.

The output of this stage is a **model-ready dataset** — clean, engineered, encoded, split, and scaled — saved to `/data/processed/` and ready to be fed directly into the [candidate models from Stage 2](./02_analytic_approach.md).

> 💡 **Freelancer's note:** Rollins is right — this is usually the most time-consuming stage. In a typical freelance project, data preparation takes 60–80% of the total effort. Don't rush it. The quality of your model is bounded by the quality of the data you feed it.

---

## Step 1: Handle Missing Values

Address the missing value issues identified in [Stage 5, Step 2](./05_data_understanding.md). The strategy depends on *why* data is missing and *how much* is missing.

**Actions:**
- For each column with missing values, apply the strategy you planned in Stage 5.
- Document every decision and its justification.

**Common Strategies:**

| Strategy | When to Use | Example |
| :--- | :--- | :--- |
| **Drop rows** | Very few missing values (< 1%), random | `df.dropna(subset=['monthly_spend'])` |
| **Drop column** | > 50% missing, no good imputation strategy | `df.drop(columns=['rarely_tracked_field'])` |
| **Impute with median** | Numerical, skewed distribution | `df['income'].fillna(df['income'].median())` |
| **Impute with mean** | Numerical, roughly normal distribution | `df['age'].fillna(df['age'].mean())` |
| **Impute with mode** | Categorical | `df['plan_type'].fillna(df['plan_type'].mode()[0])` |
| **Impute with domain logic** | Business rule applies | `last_login` → fill with `signup_date` for pre-2024 users |
| **Flag + impute** | Missingness itself is informative | Create `has_login_date` (0/1), then impute the column |

> ⚠️ **Data leakage warning:** If you impute with mean/median, compute the statistic on the **training set only** and apply it to both train and test. Best handled inside a scikit-learn Pipeline (see Step 5).

```markdown
## Missing Value Handling
| Column | Missing % | Strategy | Justification |
| :--- | :--- | :--- | :--- |
| [column] | [%] | [Strategy] | [Why this strategy was chosen] |

Example:
| monthly_spend | 0.4% | Drop rows | Very few missing, random pattern |
| last_login_date | 30% | Flag + impute with signup_date | Systematic — pre-2024 users lack tracking |
| city | 2% | Impute with mode ("Munich") | Most common value, low missingness |
```

---

## Step 2: Handle Outliers

Address the outlier issues identified in [Stage 5](./05_data_understanding.md). Not all outliers need to be removed — some are legitimate data points.

**Actions:**
- For each column with flagged outliers, decide: keep, cap, or remove.
- Document the decision and its business justification.

**Common Strategies:**

| Strategy | When to Use | Example |
| :--- | :--- | :--- |
| **Keep** | Outliers are real and informative | High-value customers — they're just wealthy |
| **Cap (winsorize)** | Extreme values distort the model but the direction matters | Cap at 1st/99th percentile |
| **Remove** | Clear data entry errors | `age = 200`, `price = -50` |
| **Log-transform** | Right-skewed distribution with a long tail | `df['income'] = np.log1p(df['income'])` |

```markdown
## Outlier Handling
| Column | Outlier Description | Strategy | Justification |
| :--- | :--- | :--- | :--- |
| [column] | [What was flagged] | [Strategy] | [Why] |

Example:
| monthly_spend | 12 values > $10,000 | Keep | Legitimate high-value Enterprise customers |
| age | 3 values > 120 | Remove | Clear data entry errors |
| sale_price | Heavy right skew | Log-transform | Normalizes the distribution for regression |
```

---

## Step 3: Feature Engineering

Create new features that capture information the raw columns don't directly express. This is where domain knowledge meets data — and where the best models are often won.

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
| log_income | np.log1p(income) | Normalizes the heavy right skew |
```

---

## Step 4: Encode Categorical Variables

Machine learning models require numerical input. Convert all categorical columns to numbers.

**Actions:**
- Choose the right encoding strategy per column.
- Be aware of the cardinality and ordinality of each categorical feature.

**Encoding Reference:**

| Encoding | When to Use | Method | Notes |
| :--- | :--- | :--- | :--- |
| **Label Encoding** | Ordinal categories (natural order) | `OrdinalEncoder` | e.g., Low < Medium < High |
| **One-Hot Encoding** | Nominal categories, low cardinality | `OneHotEncoder` / `pd.get_dummies()` | e.g., plan_type: Basic, Premium, Enterprise |
| **Target Encoding** | High cardinality (many unique values) | `TargetEncoder` | e.g., city (342 unique values) — encode as mean target per city |
| **Binary Encoding** | Binary categories | Map to 0/1 | e.g., is_active: Yes → 1, No → 0 |
| **Frequency Encoding** | When frequency itself is informative | `value_counts()` mapping | e.g., rare categories get low values |

```markdown
## Categorical Encoding
| Column | Cardinality | Encoding | Notes |
| :--- | :--- | :--- | :--- |
| [column] | [unique values] | [Method] | [Any notes] |

Example:
| plan_type | 3 | One-Hot | Basic, Premium, Enterprise |
| city | 342 | Target Encoding | Too many categories for one-hot |
| risk_level | 3 (ordered) | Ordinal | Low=0, Medium=1, High=2 |
| is_active | 2 | Binary | Yes=1, No=0 |
```

> 📚 **Reference:** See [Machine Learning with Python — Introduction](../03_specializations/02_machine_learning_with_python/01_introduction_to_machine_learning/) for encoding strategies in the scikit-learn workflow.

---

## Step 5: Train/Test Split

Separate the data into training and testing sets **before** any scaling or transformation that could leak test-set information into the training process.

**Actions:**
- Define `X` (feature matrix) and `y` (target vector).
- Apply the split strategy defined in [Stage 2](./02_analytic_approach.md).
- Verify the split is correct (shapes, class proportions if stratified).

```markdown
## Train/Test Split
* **Features (X):** [List final columns]
  Example: "tenure_months, monthly_spend, plan_type_Premium, plan_type_Enterprise,
  ticket_rate, is_weekend"

* **Target (y):** [Column name]
  Example: "churned"

* **Split Strategy:** [From Stage 2]
  Example: "80/20 stratified split (random_state=42)"

* **Shapes:**
  - X_train: [rows, cols]
  - X_test:  [rows, cols]
  - y_train: [rows]
  - y_test:  [rows]

* **Class Distribution (if classification):**
  - Train: [class 0: X%, class 1: Y%]
  - Test:  [class 0: X%, class 1: Y%]
```

> ⚠️ **Critical rule:** Everything after this step — scaling, encoding fit, imputation fit — is computed on `X_train` only and applied to both `X_train` and `X_test`. This prevents data leakage.

---

## Step 6: Feature Scaling & Final Preprocessing

Apply scaling and transformations to the numerical features. Fit on training data only.

**Actions:**
- Choose the scaler based on EDA findings from [Stage 5](./05_data_understanding.md).
- Fit on `X_train`, transform both `X_train` and `X_test`.
- Consider building a **scikit-learn Pipeline** to bundle all preprocessing steps for reproducibility and deployment.

**Scaler Selection Guide:**

| Scaler | When to Use | Behavior |
| :--- | :--- | :--- |
| `StandardScaler` | Features are roughly normal | Centers to mean=0, std=1 |
| `MinMaxScaler` | Need bounded range [0, 1] | Scales to min=0, max=1 |
| `RobustScaler` | Features have significant outliers | Uses median and IQR — robust to outliers |
| `PowerTransformer` | Heavily skewed features | Maps to approximately normal distribution |

> 📚 **Reference:** See [Model Persistence — Pickle and Joblib](../04_mlops/01_model_persistence/) for why saving the full Pipeline (preprocessing + model) is critical for deployment.

```markdown
## Preprocessing Log
* **Scaler:** [Which scaler and why]
  Example: "StandardScaler — features are roughly normal, no extreme outliers after
  handling in Step 2."

* **Pipeline:** [Whether a scikit-learn Pipeline was used]
  Example: "Built a Pipeline: OrdinalEncoder → StandardScaler → LogisticRegression.
  This ensures all preprocessing is reproducible and portable."

* **Data Leakage Check:**
  - [ ] Scaler was fit on X_train only
  - [ ] Encoder was fit on X_train only
  - [ ] Imputer was fit on X_train only (if applicable)
  - [ ] X_test was only transformed, never fit
```

---

## Step 7: Save Processed Data & Document

Save the final model-ready datasets and document every transformation for reproducibility.

**Actions:**
- Save `X_train`, `X_test`, `y_train`, `y_test` to `/data/processed/`.
- If using a Pipeline, save the fitted Pipeline object (for later use in [Deployment](./09_deployment.md)).
- Document the full transformation chain.

```markdown
## Final Output
* **Processed Data Location:** /data/processed/
* **Files:**
  - X_train: /data/processed/X_train.parquet
  - X_test:  /data/processed/X_test.parquet
  - y_train: /data/processed/y_train.parquet
  - y_test:  /data/processed/y_test.parquet

* **Final Shape:** X_train [rows × cols], X_test [rows × cols]

* **Transformation Summary:**
  1. Missing values: [handled per Step 1 log]
  2. Outliers: [handled per Step 2 log]
  3. Engineered features: [list from Step 3]
  4. Encoding: [per Step 4 log]
  5. Split: [per Step 5]
  6. Scaling: [per Step 6]
```

---

## Checklist

Before moving to [Stage 7: Modeling](./07_modeling.md), confirm:

- [ ] All missing values are handled with documented justification.
- [ ] Outliers are addressed (kept, capped, removed, or transformed).
- [ ] Engineered features are created and justified.
- [ ] All categorical variables are encoded numerically.
- [ ] Train/test split is performed before any scaling.
- [ ] Scaling is fit on X_train only and applied to both X_train and X_test.
- [ ] No data leakage exists in the preprocessing pipeline.
- [ ] Processed data is saved to `/data/processed/`.
- [ ] Every transformation is documented and reproducible.

---

**Next:** [Modeling](./07_modeling.md) — Training the candidate models on the prepared data.