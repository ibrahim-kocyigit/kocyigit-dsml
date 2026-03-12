# Stage 7: Modeling

_"Starting with the first version of the prepared data set, the modeling stage focuses on developing predictive or descriptive models according to the previously defined analytic approach. With predictive models, data scientists use a training set (historical data in which the outcome of interest is known) to build the model. The modeling process is typically highly iterative as organizations gain intermediate insights, leading to refinements in data preparation and model specification. For a given technique, data scientists may try multiple algorithms with their respective parameters to find the best model for the available variables."_ — **John B. Rollins**

---

## Purpose

This is where the plan becomes a model. You take the prepared data from [Stage 6](./06_data_preparation.md), the candidate algorithms from [Stage 2](./02_analytic_approach.md), and systematically train, compare, tune, and select the best model for the job.

The output of this stage is a single **champion model** — trained, tuned, and ready for final evaluation on the holdout test set in [Stage 8](./08_evaluation.md).

> 💡 **Freelancer's note:** Resist the urge to jump straight to XGBoost. The baseline model is not a formality — it's your anchor. If a Logistic Regression gets 0.82 AUC and a tuned XGBoost gets 0.84, the simpler model may be the better choice for the client (faster, explainable, easier to deploy). Always let the data and the business requirements decide.

---

## Step 1: Train the Baseline Model

Train the simple baseline model identified in [Stage 2](./02_analytic_approach.md). This sets the **performance floor** — every subsequent model must beat this to justify its complexity.

**Actions:**
- Train the baseline model on `X_train`, `y_train`.
- Evaluate using cross-validation on the training set (use the CV strategy from [Stage 2](./02_analytic_approach.md)).
- Record the primary metric, secondary metrics, and training time.

**Why the baseline matters:**

| Scenario | What It Tells You |
| :--- | :--- |
| Baseline already meets the acceptance threshold | You may not need a complex model at all — ship the simple one |
| Baseline performs terribly | The problem may not be solvable with the current features — revisit [Stage 6](./06_data_preparation.md) |
| Baseline is reasonable but below threshold | Good — now you have a clear target to beat |

> 📚 **Reference:** See [Machine Learning with Python — Linear and Logistic Regression](../03_specializations/02_machine_learning_with_python/02_linear_and_logistic_regression/) for Logistic and Linear Regression as baselines.

```markdown
## Baseline Model
* **Algorithm:** [Name]
  Example: "Logistic Regression (default hyperparameters)"

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

## Step 2: Train Candidate Models

Train each candidate model from [Stage 2](./02_analytic_approach.md) with default hyperparameters. The goal is a fair comparison across algorithms before investing time in tuning.

**Actions:**
- Train each candidate on `X_train`, `y_train`.
- Evaluate each using the same cross-validation strategy as the baseline.
- Record all metrics consistently in a comparison table.

**For classification:**

```python
from sklearn.model_selection import cross_validate

models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
    "XGBoost": XGBClassifier(),
}

for name, model in models.items():
    scores = cross_validate(model, X_train, y_train, cv=5,
                            scoring=['roc_auc', 'recall', 'precision'])
```

**For regression:**

```python
models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(),
    "Random Forest": RandomForestRegressor(),
    "XGBoost": XGBRegressor(),
}

for name, model in models.items():
    scores = cross_validate(model, X_train, y_train, cv=5,
                            scoring=['neg_root_mean_squared_error', 'r2'])
```

> 📚 **Reference:** See [Machine Learning with Python — Non-Linear and Ensemble Models](../03_specializations/02_machine_learning_with_python/03_non-linear_and_ensemble_models/) for Random Forest, XGBoost, SVM, and KNN.

```markdown
## Candidate Model Comparison
| Model | [Primary Metric] (Mean ± Std) | [Secondary Metric] (Mean ± Std) | Training Time | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Logistic Regression (baseline) | [value] | [value] | [time] | [notes] |
| Random Forest | [value] | [value] | [time] | [notes] |
| XGBoost | [value] | [value] | [time] | [notes] |

Example (classification):
| Logistic Regression | AUC: 0.78 ± 0.02 | Recall: 0.65 ± 0.04 | 0.3s | Baseline. Below recall threshold. |
| Random Forest | AUC: 0.83 ± 0.02 | Recall: 0.76 ± 0.03 | 12s | +5% AUC lift. Approaching recall threshold. |
| XGBoost | AUC: 0.84 ± 0.01 | Recall: 0.78 ± 0.03 | 8s | Best out-of-the-box. Close to threshold. |

Example (regression):
| Linear Regression | RMSE: 45,200 ± 3,100 | R²: 0.72 ± 0.03 | 0.1s | Baseline. Reasonable. |
| Ridge | RMSE: 44,800 ± 2,900 | R²: 0.73 ± 0.02 | 0.1s | Marginal improvement. |
| Random Forest | RMSE: 38,100 ± 2,500 | R²: 0.81 ± 0.02 | 15s | Significant lift. |
| XGBoost | RMSE: 36,500 ± 2,200 | R²: 0.83 ± 0.02 | 10s | Best performance. |
```

---

## Step 3: Hyperparameter Tuning

Tune the top 1–2 performing models from Step 2. Don't tune every model — only the ones that showed the most promise.

**Actions:**
- Define a hyperparameter search space for each model.
- Use `GridSearchCV` (exhaustive, small spaces) or `RandomizedSearchCV` (large spaces).
- Use the same cross-validation strategy as Steps 1–2.
- Record the best parameters and the performance improvement.

**Common Hyperparameters to Tune:**

| Algorithm | Key Hyperparameters |
| :--- | :--- |
| **Logistic Regression** | `C`, `penalty`, `solver` |
| **Random Forest** | `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf` |
| **XGBoost** | `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `colsample_bytree` |
| **Ridge / Lasso** | `alpha` |
| **SVM** | `C`, `kernel`, `gamma` |
| **KNN** | `n_neighbors`, `weights`, `metric` |

> 📚 **Reference:** See [Machine Learning with Python — Evaluating and Validating Models](../03_specializations/02_machine_learning_with_python/05_evaluating_and_validating_machine_learning_models/) for cross-validation and tuning strategies.

```markdown
## Hyperparameter Tuning

### Model 1: [Name]
* **Method:** [GridSearchCV / RandomizedSearchCV — iterations, CV folds]
  Example: "RandomizedSearchCV, 100 iterations, 5-fold stratified CV"

* **Search Space:**
  Example: "n_estimators: [100, 200, 300, 500], max_depth: [5, 10, 15, None],
  min_samples_leaf: [1, 2, 4, 8]"

* **Best Parameters:** [Dict]
  Example: "{'n_estimators': 300, 'max_depth': 15, 'min_samples_leaf': 2}"

* **Best CV Score:** [Primary metric ± std]
  Example: "AUC: 0.86 ± 0.01 (up from 0.84 default)"

### Model 2: [Name] (if applicable)
* [Same structure]
```

---

## Step 4: Select the Champion Model

Compare all results — baseline, default candidates, and tuned models — and select the single champion model.

**Actions:**
- Create a final comparison table (all models, all metrics, all stages).
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
| Model | [Primary Metric] | [Secondary Metric] | Training Time | Tuned? |
| :--- | :--- | :--- | :--- | :--- |
| [List all models tested] | [values] | [values] | [times] | [Yes/No] |

### Decision
* **Champion Model:** [Name and configuration]
  Example: "Tuned XGBoost (n_estimators=300, max_depth=10, learning_rate=0.05)"

* **Justification:** [Why this model over the others]
  Example: "XGBoost achieved the highest AUC (0.86) and Recall (0.82), meeting the
  Stage 2 acceptance threshold. While less interpretable than Logistic Regression,
  the client accepted a SHAP-based explanation approach (see Stage 1 requirements)."

* **Runner-Up:** [Name — in case the champion fails final evaluation in Stage 8]
  Example: "Random Forest (AUC: 0.85, Recall: 0.80) — slightly lower but faster
  and more interpretable. Viable fallback."
```

> ⚠️ **Important:** This model has only been evaluated via cross-validation on the training set. The true, unbiased performance estimate comes from the holdout test set in [Stage 8](./08_evaluation.md). Do not report CV scores as final performance.

---

## Step 5: Save the Model & Document

Save the champion model (and optionally the runner-up) for evaluation and potential deployment.

**Actions:**
- Save the trained model object using joblib.
- If using a scikit-learn Pipeline, save the full Pipeline (preprocessing + model).
- Document the full experiment log.

> 📚 **Reference:** See [Model Persistence — Pickle and Joblib](../04_mlops/01_model_persistence/) for best practices on saving models with metadata.

```markdown
## Model Artifacts
* **Champion Model Saved To:** [Path]
  Example: "models/champion_xgboost_v1.joblib"

* **Pipeline Saved:** [Yes/No — if yes, includes preprocessing]
  Example: "Yes — full Pipeline (StandardScaler → XGBClassifier)"

* **Metadata:**
  - Algorithm: [Name]
  - Hyperparameters: [Dict]
  - Training date: [YYYY-MM-DD]
  - Training data shape: [rows × cols]
  - CV primary metric: [value ± std]

### Experiment Summary
| Stage | Models Tried | Best CV Score | Selected |
| :--- | :--- | :--- | :--- |
| Baseline | [Name] | [score] | No |
| Default candidates | [Names] | [best score] | No |
| Tuned | [Names] | [best score] | ✅ [Champion name] |
```

---

## Checklist

Before moving to [Stage 8: Evaluation](./08_evaluation.md), confirm:

- [ ] Baseline model is trained and scored via cross-validation.
- [ ] All candidate models are trained and compared under the same CV strategy.
- [ ] Top 1–2 models are tuned with documented hyperparameter search.
- [ ] A champion model is selected with explicit justification.
- [ ] A runner-up model is identified as a fallback.
- [ ] The champion model is saved (ideally as a full Pipeline).
- [ ] All CV scores are clearly labeled as *training-set estimates*, not final performance.
- [ ] The experiment log is documented for reproducibility.

---

**Next:** [Evaluation](./08_evaluation.md) — Final, unbiased evaluation of the champion model on the holdout test set.