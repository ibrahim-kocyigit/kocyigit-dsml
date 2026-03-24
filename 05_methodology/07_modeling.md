# Stage 7: Modeling

_"Starting with the first version of the prepared data set, the modeling stage focuses on developing predictive or descriptive models according to the previously defined analytic approach. With predictive models, data scientists use a training set — historical data in which the outcome of interest is known — for the predictive model to learn. The data scientist uses the training set to build the model and then uses a test set to validate the model."_ — John B. Rollins

---

## Purpose

This is where the plan becomes a model. You take the prepared data from [Stage 6](./06_data_preparation.md), the candidate algorithms from [Stage 2](./02_analytic_approach.md), and systematically train, compare, and tune models to find the best performer.

Stage 6 delivered `train_df` and `test_df` — complete DataFrames with features and target intact. Statistical preprocessing (imputation, encoding, scaling) was deliberately deferred to this stage because **different models need different preprocessing**. Here, each candidate model gets its own scikit-learn Pipeline that bundles the exact preprocessing it needs with the algorithm itself.

The output of this stage is a single **champion model** — a complete Pipeline (preprocessing + algorithm), trained, tuned, and ready for final evaluation on the holdout test set in [Stage 8](./08_evaluation.md).

> 💡 **Freelancer's note:** Resist the urge to jump straight to XGBoost. The baseline model is not a formality — it's your anchor. If a Logistic Regression gets 0.82 AUC and a tuned XGBoost gets 0.84, the simpler model may be the better business decision — cheaper to deploy, easier to explain, and less likely to overfit.

---

## Step 1: Define X and y

Separate features and target from `train_df` and `test_df`. This is done here — not in Stage 6 — because different models may use different feature subsets during experimentation.

**Actions:**
- Define the target column name.
- Define the initial feature set (all columns except target and any reserved columns).
- Separate `X_train`, `y_train`, `X_test`, `y_test`.

```python
TARGET = "churned"

X_train = train_df.drop(columns=[TARGET])
y_train = train_df[TARGET]

X_test = test_df.drop(columns=[TARGET])
y_test = test_df[TARGET]
```

```markdown
## X/y Separation
* **Target Column:** [Name]
  Example: "churned"

* **Initial Feature Set:** [List or count]
  Example: "All 15 columns except churned"

* **Shapes:**
  - X_train: [rows × cols]
  - X_test:  [rows × cols]
  - y_train: [rows]
  - y_test:  [rows]

* **Notes:** [Any columns excluded beyond the target]
  Example: "customer_id was already dropped in Stage 6."
```

> 💡 **Tip:** During experimentation, you may want to try different feature subsets (e.g., drop a multicollinear feature for linear models but keep it for tree models). Having the full DataFrames from Stage 6 makes this easy.

---

## Step 2: Build Per-Model Preprocessing Pipelines

This is the critical step that was deferred from Stage 6. Each candidate model gets its own scikit-learn Pipeline that handles the statistical preprocessing it needs.

**Why per-model Pipelines?**

| Preprocessing Step | Linear Models (LogReg, Ridge, SVM) | Tree-Based Models (RF, XGBoost) |
| :--- | :--- | :--- |
| **Missing value imputation** | Median/mean | Median (or model handles natively) |
| **Outlier capping** | Often beneficial (sensitive to outliers) | Usually unnecessary (splits handle outliers) |
| **Categorical encoding** | One-Hot (nominal), Ordinal (ordinal) | Ordinal / Label (trees split on thresholds) |
| **Feature scaling** | Required (StandardScaler, RobustScaler) | Not needed |

**Actions:**
- For each candidate model from [Stage 2](./02_analytic_approach.md), build a Pipeline using the preprocessing plan from [Stage 6, Step 5](./06_data_preparation.md).
- Use `ColumnTransformer` to apply different transformations to different column types.
- Include imputation, encoding, scaling (where needed), and the model itself — all in one Pipeline.

**Example: Classification with mixed preprocessing**

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# Define column groups
num_features = ["tenure_months", "monthly_spend", "ticket_rate"]
cat_nominal = ["plan_type"]
cat_ordinal = ["risk_level"]

# --- Pipeline for Linear Models (needs scaling + one-hot) ---
linear_preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]), num_features),
    ("cat_nom", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(drop="first", handle_unknown="ignore")),
    ]), cat_nominal),
    ("cat_ord", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder(categories=[["Low", "Medium", "High"]])),
    ]), cat_ordinal),
])

logistic_pipeline = Pipeline([
    ("preprocessor", linear_preprocessor),
    ("model", LogisticRegression()),
])

# --- Pipeline for Tree-Based Models (no scaling, ordinal encoding) ---
tree_preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        # No scaler — trees don't need it
    ]), num_features),
    ("cat_nom", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder(handle_unknown="use_encoded_value",
                                   unknown_value=-1)),
    ]), cat_nominal),
    ("cat_ord", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder(categories=[["Low", "Medium", "High"]])),
    ]), cat_ordinal),
])

rf_pipeline = Pipeline([
    ("preprocessor", tree_preprocessor),
    ("model", RandomForestClassifier()),
])

xgb_pipeline = Pipeline([
    ("preprocessor", tree_preprocessor),
    ("model", XGBClassifier()),
])
```

> 📚 **Reference:** See [Machine Learning with Python — Introduction](../03_specializations/02_machine_learning_with_python/01_introduction_to_machine_learning/) for Pipeline and ColumnTransformer usage.

```markdown
## Preprocessing Pipelines

### Linear Model Pipeline
* **Numerical:** [Imputer] → [Scaler]
  Example: "SimpleImputer(median) → StandardScaler"
* **Categorical (nominal):** [Imputer] → [Encoder]
  Example: "SimpleImputer(most_frequent) → OneHotEncoder(drop='first')"
* **Categorical (ordinal):** [Imputer] → [Encoder]
  Example: "SimpleImputer(most_frequent) → OrdinalEncoder"
* **Outlier Handling:** [If included in pipeline]
  Example: "RobustScaler used instead of StandardScaler to reduce outlier influence"

### Tree-Based Model Pipeline
* **Numerical:** [Imputer] (no scaler)
  Example: "SimpleImputer(median)"
* **Categorical (nominal):** [Imputer] → [Encoder]
  Example: "SimpleImputer(most_frequent) → OrdinalEncoder"
* **Categorical (ordinal):** [Imputer] → [Encoder]
  Example: "SimpleImputer(most_frequent) → OrdinalEncoder"
* **Outlier Handling:** None — trees handle outliers naturally

### Data Leakage Verification
- [ ] All imputers will be fit on X_train only (via Pipeline.fit)
- [ ] All encoders will be fit on X_train only (via Pipeline.fit)
- [ ] All scalers will be fit on X_train only (via Pipeline.fit)
- [ ] X_test will only be transformed, never fit (via Pipeline.predict)
```

> ⚠️ **This is why Pipelines matter:** When you call `pipeline.fit(X_train, y_train)`, every preprocessing step is fit on the training data only. When you call `pipeline.predict(X_test)`, the same fitted transformers are applied to the test data — no leakage, no manual bookkeeping. The Pipeline guarantees correctness.

---

## Step 3: Train the Baseline Model

Train the simple baseline model identified in [Stage 2](./02_analytic_approach.md). This sets the **performance floor** — every subsequent model must beat this to justify its complexity.

**Actions:**
- Train the baseline Pipeline on `X_train`, `y_train`.
- Evaluate using cross-validation on the training set (use the CV strategy from [Stage 2](./02_analytic_approach.md)).
- Record the primary metric, secondary metrics, and training time.

**Why the baseline matters:**

| Scenario | What It Tells You |
| :--- | :--- |
| Baseline already meets the acceptance threshold | You may not need a complex model at all — ship the simple one |
| Baseline performs terribly | The problem may not be solvable with the current features — revisit [Stage 6](./06_data_preparation.md) |
| Baseline is reasonable but below threshold | Good — now you have a clear target to beat |

> 📚 **Reference:** See [Machine Learning with Python — Linear and Logistic Regression](../03_specializations/02_machine_learning_with_python/02_linear_and_logistic_regression/) for Logistic and Linear Regression fundamentals.

```markdown
## Baseline Model
* **Algorithm:** [Name]
  Example: "Logistic Regression (default hyperparameters)"

* **Pipeline:** [Preprocessing summary]
  Example: "SimpleImputer(median) → StandardScaler → OneHotEncoder → LogisticRegression"

* **Cross-Validation Results:**
  | Metric | Mean | Std |
  | :--- | :--- | :--- |
  | [Primary metric] | [value] | [± value] |
  | [Secondary metric] | [value] | [± value] |

  Example:
  | AUC-ROC | 0.78 | ± 0.02 |
  | Recall  | 0.65 | ± 0.04 |

* **Training Time:** [seconds]
* **Notes:** [Observations — interpretability, speed, where it struggles]
  Example: "Fast and interpretable. Recall is below the 0.80 threshold — the model
  misses too many churning customers. More complex models may capture non-linear patterns."
```

---

## Step 4: Train Candidate Models

Train each candidate model from [Stage 2](./02_analytic_approach.md) using its own Pipeline with default hyperparameters. The goal is a fair comparison across algorithms before investing time in tuning.

**Actions:**
- Train each candidate Pipeline on `X_train`, `y_train`.
- Evaluate each using the same cross-validation strategy as the baseline.
- Record all metrics consistently in a comparison table.

**For classification:**

```python
from sklearn.model_selection import cross_validate

pipelines = {
    "Logistic Regression": logistic_pipeline,
    "Random Forest": rf_pipeline,
    "XGBoost": xgb_pipeline,
}

results = {}
for name, pipe in pipelines.items():
    scores = cross_validate(pipe, X_train, y_train, cv=5,
                            scoring=['roc_auc', 'recall', 'precision'])
    results[name] = scores
```

**For regression:**

```python
pipelines = {
    "Linear Regression": linear_pipeline,
    "Ridge": ridge_pipeline,
    "Random Forest": rf_pipeline,
    "XGBoost": xgb_pipeline,
}

for name, pipe in pipelines.items():
    scores = cross_validate(pipe, X_train, y_train, cv=5,
                            scoring=['neg_root_mean_squared_error', 'r2'])
```

> 📚 **Reference:** See [Machine Learning with Python — Non-Linear and Ensemble Models](../03_specializations/02_machine_learning_with_python/03_non-linear_and_ensemble_models/) for Random Forest, XGBoost, SVM, and KNN.

```markdown
## Candidate Model Comparison
| Model | Pipeline | [Primary Metric] (Mean ± Std) | [Secondary Metric] (Mean ± Std) | Training Time | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Logistic Regression (baseline) | Linear pipeline | [value] | [value] | [time] | [notes] |
| Random Forest | Tree pipeline | [value] | [value] | [time] | [notes] |
| XGBoost | Tree pipeline | [value] | [value] | [time] | [notes] |

Example (classification):
| Logistic Regression | Impute→Scale→OneHot→LogReg | AUC: 0.78 ± 0.02 | Recall: 0.65 ± 0.04 | 0.3s | Baseline. Below recall threshold. |
| Random Forest | Impute→Ordinal→RF | AUC: 0.83 ± 0.02 | Recall: 0.76 ± 0.03 | 12s | +5% AUC lift. Approaching recall threshold. |
| XGBoost | Impute→Ordinal→XGB | AUC: 0.84 ± 0.01 | Recall: 0.78 ± 0.03 | 8s | Best out-of-the-box. Close to threshold. |

Example (regression):
| Linear Regression | Impute→Scale→OneHot→LinReg | RMSE: 45,200 ± 3,100 | R²: 0.72 ± 0.03 | 0.1s | Baseline. Reasonable. |
| Ridge | Impute→Scale→OneHot→Ridge | RMSE: 44,800 ± 2,900 | R²: 0.73 ± 0.02 | 0.1s | Marginal improvement. |
| Random Forest | Impute→Ordinal→RF | RMSE: 38,100 ± 2,500 | R²: 0.81 ± 0.02 | 15s | Significant lift. |
| XGBoost | Impute→Ordinal→XGB | RMSE: 36,500 ± 2,200 | R²: 0.83 ± 0.02 | 10s | Best performance. |
```

---

## Step 5: Hyperparameter Tuning

Tune the top 1–2 performing Pipelines from Step 4. Don't tune every model — only the ones that showed the most promise.

**Actions:**
- Define a hyperparameter search space for each Pipeline (both preprocessing and model parameters).
- Use `GridSearchCV` (exhaustive, small spaces) or `RandomizedSearchCV` (large spaces).
- Use the same cross-validation strategy as Steps 3–4.
- Record the best parameters and the performance improvement.

**Tuning Pipeline Parameters:**

When tuning a Pipeline, parameter names use the `step__parameter` convention:

```python
from sklearn.model_selection import RandomizedSearchCV

param_distributions = {
    # Model hyperparameters
    "model__n_estimators": [100, 200, 300, 500],
    "model__max_depth": [5, 10, 15, None],
    "model__min_samples_leaf": [1, 2, 4, 8],
    # Preprocessing hyperparameters (if you want to tune them)
    "preprocessor__num__imputer__strategy": ["mean", "median"],
}

search = RandomizedSearchCV(
    rf_pipeline, param_distributions,
    n_iter=50, cv=5, scoring="roc_auc", random_state=42
)
search.fit(X_train, y_train)
```

**Common Hyperparameters to Tune:**

| Algorithm | Key Hyperparameters |
| :--- | :--- |
| **Logistic Regression** | `C`, `penalty`, `solver` |
| **Random Forest** | `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf` |
| **XGBoost** | `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `colsample_bytree` |
| **Ridge / Lasso** | `alpha` |
| **SVM** | `C`, `kernel`, `gamma` |
| **KNN** | `n_neighbors`, `weights`, `metric` |

> 📚 **Reference:** See [Machine Learning with Python — Evaluating and Validating Models](../03_specializations/02_machine_learning_with_python/05_evaluating_and_validating_machine_learning_models/) for GridSearchCV, RandomizedSearchCV, and cross-validation best practices.

```markdown
## Hyperparameter Tuning

### Model 1: [Name]
* **Method:** [GridSearchCV / RandomizedSearchCV — iterations, CV folds]
  Example: "RandomizedSearchCV, 50 iterations, 5-fold stratified CV"

* **Search Space:**
  Example: "model__n_estimators: [100, 200, 300, 500], model__max_depth: [5, 10, 15, None],
  model__min_samples_leaf: [1, 2, 4, 8]"

* **Best Parameters:** [Dict]
  Example: "{'model__n_estimators': 300, 'model__max_depth': 15, 'model__min_samples_leaf': 2}"

* **Best CV Score:** [Primary metric ± std]
  Example: "AUC: 0.86 ± 0.01 (up from 0.84 default)"

### Model 2: [Name] (if applicable)
* [Same structure]
```

---

## Step 6: Select the Champion Model

Compare all results — baseline, default candidates, and tuned Pipelines — and select the single champion.

**Actions:**
- Create a final comparison table (all Pipelines, all metrics, all stages).
- Select the champion based on the [primary metric and acceptance threshold from Stage 2](./02_analytic_approach.md).
- Consider the tradeoffs: performance vs. interpretability vs. training time vs. deployment complexity.

**Decision Framework:**

| Factor | Favors Simpler Model | Favors Complex Model |
| :--- | :--- | :--- |
| Performance gap vs. baseline | Small (< 3–5%) | Large (> 5–10%) |
| Interpretability requirement | Client needs to understand *why* | Black-box score is acceptable |
| Deployment complexity | API with low latency needed | Batch predictions, latency doesn't matter |
| Data size | Small dataset (risk of overfitting) | Large dataset (complex model can generalize) |
| Maintenance | Freelancer won't maintain it long-term | Ongoing contract with monitoring |

```markdown
## Champion Model Selection

### Final Comparison
| Model | Pipeline | [Primary Metric] | [Secondary Metric] | Training Time | Tuned? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [List all models tested] | [Pipeline summary] | [values] | [values] | [times] | [Yes/No] |

### Decision
* **Champion Model:** [Name and configuration]
  Example: "Tuned XGBoost Pipeline (Impute→Ordinal→XGBClassifier with
  n_estimators=300, max_depth=10, learning_rate=0.05)"

* **Justification:** [Why this model over the others]
  Example: "XGBoost achieved the highest AUC (0.86) and Recall (0.82), meeting the
  Stage 2 acceptance threshold. While less interpretable than Logistic Regression,
  the client accepted a SHAP-based explanation approach (see Stage 1 requirements)."

* **Runner-Up:** [Name — in case the champion fails final evaluation in Stage 8]
  Example: "Random Forest Pipeline (AUC: 0.85, Recall: 0.80) — slightly lower but
  faster and more interpretable. Viable fallback."
```

> ⚠️ **Important:** This model has only been evaluated via cross-validation on the training set. The true, unbiased performance estimate comes from the holdout test set in [Stage 8](./08_evaluation.md).

---

## Step 7: Save the Champion Pipeline & Document

Save the champion Pipeline (preprocessing + model) and optionally the runner-up for evaluation and potential deployment.

**Actions:**
- Save the trained Pipeline object using joblib — this includes all fitted preprocessing steps and the model.
- Document the full experiment log.

> 📚 **Reference:** See [Model Persistence — Pickle and Joblib](../04_mlops/01_model_persistence/) for best practices on saving models with metadata.

> 💡 **Why save the full Pipeline?** When you save just the model, you need to manually replicate the preprocessing at prediction time — and any mismatch means wrong predictions. Saving the full Pipeline guarantees that `pipeline.predict(raw_X)` applies the exact same imputation, encoding, and scaling that was used during training.

```markdown
## Model Artifacts
* **Champion Pipeline Saved To:** [Path]
  Example: "models/champion_xgboost_pipeline_v1.joblib"

* **Pipeline Contents:** [What's inside]
  Example: "ColumnTransformer(SimpleImputer, OrdinalEncoder) → XGBClassifier"

* **Metadata:**
  - Algorithm: [Name + key hyperparameters]
  - Preprocessing: [Summary of Pipeline steps]
  - Training date: [YYYY-MM-DD]
  - Training data shape: [rows × cols]
  - CV primary metric: [value ± std]

### Experiment Summary
| Stage | Models Tried | Pipeline | Best CV Score | Selected |
| :--- | :--- | :--- | :--- | :--- |
| Baseline | [Name] | [Pipeline summary] | [score] | No |
| Default candidates | [Names] | [Pipeline summaries] | [best score] | No |
| Tuned | [Names] | [Pipeline summaries] | [best score] | ✅ [Champion name] |
```

---

## Checklist

Before moving to [Stage 8: Evaluation](./08_evaluation.md), confirm:

- [ ] X and y are separated from `train_df` and `test_df`.
- [ ] Per-model preprocessing Pipelines are built (imputation, encoding, scaling inside Pipelines).
- [ ] All preprocessing steps are fit on `X_train` only (guaranteed by Pipeline architecture).
- [ ] Baseline model is trained and scored via cross-validation.
- [ ] All candidate Pipelines are trained and compared under the same CV strategy.
- [ ] Top 1–2 Pipelines are tuned with documented hyperparameter search.
- [ ] A champion Pipeline is selected with explicit justification.
- [ ] A runner-up Pipeline is identified as a fallback.
- [ ] The champion Pipeline is saved (preprocessing + model in one artifact).
- [ ] All CV scores are clearly labeled as *training-set estimates*, not final performance.
- [ ] The experiment log is documented for reproducibility.

---

**Next:** [Evaluation](./08_evaluation.md) — Final, unbiased evaluation of the champion model on the holdout test set.