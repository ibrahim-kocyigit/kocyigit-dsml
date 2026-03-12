# Stage 8: Evaluation

_"During model development and before deployment, the data scientist evaluates the model to understand its quality and ensure that it properly and fully addresses the business problem. Model evaluation entails computing various diagnostic measures and other outputs such as tables and graphs, enabling the data scientist to interpret the model's quality and its efficacy in solving the problem. For a predictive model, data scientists use a testing set, which is independent of the training set but follows the same probability distribution and has a known outcome."_ — **John B. Rollins**

---

## Purpose

In [Stage 7](./07_modeling.md), you selected a champion model based on cross-validation scores from the training set. Those scores are **optimistic estimates** — the model was tuned to perform well on that data.

This stage produces the **final, unbiased performance estimate** by evaluating the champion model on the holdout test set — data it has never seen. The results are then translated into business terms and used to make a **go/no-go decision** for deployment.

> 💡 **Freelancer's note:** This is the stage where you earn or lose the client's trust. A clear evaluation report — with honest metrics, visual diagnostics, and a plain-language business impact statement — shows professionalism. Don't hide poor performance; explain what it means and what the options are.

---

## Step 1: Final Training on Full Training Set

Retrain the champion model (with the best hyperparameters from [Stage 7](./07_modeling.md)) on the **entire** training set. During cross-validation, the model only ever trained on 80% of the training data (in each fold). Now it gets all of it.

**Actions:**
- Load the champion model configuration (algorithm + best hyperparameters).
- Fit on the complete `X_train`, `y_train`.
- This is the model that will be evaluated and potentially deployed.

```markdown
## Final Training
* **Champion Model:** [Algorithm + hyperparameters]
  Example: "XGBoost (n_estimators=300, max_depth=10, learning_rate=0.05)"

* **Trained On:** Full training set ([N] rows × [M] features)
* **Date:** [YYYY-MM-DD]
```

---

## Step 2: Holdout Test Set Evaluation

Evaluate the champion model on `X_test`, `y_test` — the data held back since [Stage 6, Step 5](./06_data_preparation.md). This produces the **only scores you should report** as the model's expected real-world performance.

**Actions:**
- Generate predictions (`y_pred`) and probability scores (`y_pred_proba` for classification).
- Compute the primary and secondary metrics from [Stage 2](./02_analytic_approach.md).
- Compare test scores to CV scores from Stage 7 — they should be close.

**Interpreting the CV vs. Test Gap:**

| Scenario | What It Means | Action |
| :--- | :--- | :--- |
| Test ≈ CV (within 1–2%) | Model generalized well | ✅ Proceed with confidence |
| Test slightly below CV (3–5%) | Minor overfitting to training data | ⚠️ Acceptable — report test score as the true estimate |
| Test far below CV (> 5%) | Significant overfitting | ❌ Investigate — may need to simplify the model, add regularization, or revisit [Stage 6](./06_data_preparation.md) |
| Test above CV | Unusual — possible data leakage or lucky split | ⚠️ Investigate — check for leakage in preprocessing |

```markdown
## Test Set Performance
| Metric | CV Score (Stage 7) | Test Set Score | Gap | Meets Threshold? |
| :--- | :--- | :--- | :--- | :--- |
| [Primary] | [value ± std] | [value] | [diff] | [Yes / No] |
| [Secondary] | [value ± std] | [value] | [diff] | [Yes / No] |

Example (classification):
| AUC-ROC | 0.86 ± 0.01 | 0.84 | -0.02 | ✅ Yes (threshold: 0.75) |
| Recall | 0.82 ± 0.03 | 0.79 | -0.03 | ⚠️ Borderline (threshold: 0.80) |
| Precision | 0.71 ± 0.04 | 0.69 | -0.02 | ✅ Yes |

Example (regression):
| RMSE | 36,500 ± 2,200 | 38,100 | +1,600 | ✅ Yes (threshold: < 40,000) |
| R² | 0.83 ± 0.02 | 0.81 | -0.02 | ✅ Yes (threshold: > 0.75) |
| MAE | 24,300 ± 1,800 | 25,900 | +1,600 | ✅ Yes |
```

---

## Step 3: Diagnostic Visualizations

Numbers tell part of the story. Visualizations reveal *where* the model succeeds and *where* it fails. Different problem types need different diagnostics.

### Classification Diagnostics

| Visualization | What It Shows | When It Matters |
| :--- | :--- | :--- |
| **Confusion Matrix** | TP, FP, TN, FN breakdown | Always — shows the error distribution |
| **ROC Curve** | True Positive Rate vs. False Positive Rate | When the threshold can be tuned |
| **Precision-Recall Curve** | Precision vs. Recall at each threshold | Imbalanced datasets (preferred over ROC) |
| **Classification Report** | Per-class precision, recall, F1 | Multi-class problems |
| **Threshold Analysis** | Metrics at different probability cutoffs | When the business cost of FP ≠ FN |

### Regression Diagnostics

| Visualization | What It Shows | When It Matters |
| :--- | :--- | :--- |
| **Actual vs. Predicted Scatter** | How close predictions are to reality | Always — ideal is the 45° line |
| **Residual Plot** | Prediction errors vs. predicted values | Always — errors should be random (no pattern) |
| **Residual Distribution** | Whether errors are normally distributed | When assumptions of normality matter |
| **Error by Segment** | Performance broken down by category | When some segments matter more than others |

### Clustering Diagnostics

| Visualization | What It Shows | When It Matters |
| :--- | :--- | :--- |
| **Silhouette Plot** | Cluster cohesion per sample | Evaluating cluster quality |
| **Cluster Profiles** | Mean feature values per cluster | Business interpretation of each segment |
| **2D/3D Scatter (PCA)** | Visual separation of clusters | Communicating results to stakeholders |

> 📚 **Reference:** See [Machine Learning with Python — Evaluating and Validating Models](../03_specializations/02_machine_learning_with_python/05_evaluating_and_validating_machine_learning_models/) for implementation of these diagnostics. See [Matplotlib Fundamentals](../02_toolkit/04_matplotlib_fundamentals/) and [Seaborn Fundamentals](../02_toolkit/05_seaborn_fundamentals/) for visualization techniques.

```markdown
## Diagnostic Visualizations
* [List visualizations produced and key takeaways from each]

Example (classification):
* **Confusion Matrix:** 79% of actual churners correctly identified (TP=158, FN=42).
  Most false negatives are customers with tenure > 12 months — the model underperforms
  on long-tenure churn.
* **ROC Curve:** AUC = 0.84. Curve is well above the random baseline.
* **Threshold Analysis:** Lowering the threshold from 0.5 to 0.4 increases Recall from
  0.79 to 0.85, at the cost of Precision dropping from 0.69 to 0.58. Recommended for
  the business use case (cost of missing a churner >> cost of a false alarm).
```

---

## Step 4: Business Impact Translation

Translate the technical metrics into **business language** that the client can act on. This is the bridge between data science and business value.

**Actions:**
- Map model performance to the business objectives from [Stage 1](./01_business_understanding.md).
- Quantify the impact in business terms (money, time, customers, decisions).
- Be honest about limitations and risks.

```markdown
## Business Impact Statement

### What the Model Achieves
* [Translate the primary metric into a business outcome]
  Example: "The model correctly identifies 79% of customers who will churn in the next
  30 days. For a client base of 50,000, this means ~395 of the estimated 500 monthly
  churners are flagged in advance for the retention team."

### Projected Impact
* [Quantify the value]
  Example: "If the retention campaign converts 30% of flagged customers (industry average),
  the model prevents ~118 churns per month, worth approximately $59,000/month in retained
  revenue (at $500 avg monthly spend)."

### What the Model Does NOT Do
* [Be honest about limitations]
  Example: "The model underperforms on long-tenure customers (tenure > 12 months). These
  churners are harder to predict — their patterns differ from short-tenure churn. A
  separate model or rule-based approach may be needed for this segment."

### Error Costs
* [What happens when the model is wrong]
  Example: "False Positives (21%): A non-churning customer receives a retention offer.
  Cost: minor discount ($10–20). False Negatives (21%): A churning customer is missed.
  Cost: $500/month in lost revenue. The asymmetry justifies optimizing for Recall."
```

> 💡 **Freelancer's tip:** This section is what the client remembers. They won't remember "AUC = 0.84." They will remember "The model catches 4 out of 5 churning customers before they leave, saving an estimated $59k/month."

---

## Step 5: Go / No-Go Decision

Present the evaluation results to the stakeholder and get a formal decision on whether to proceed to deployment.

**Actions:**
- Present the test set results, diagnostics, and business impact statement.
- Compare the results against the [acceptance threshold from Stage 2](./02_analytic_approach.md).
- Get a formal go/no-go decision.

**Decision Framework:**

| Test Result | Recommendation |
| :--- | :--- |
| Meets all thresholds, consistent with CV | ✅ **Go** — proceed to [Stage 9: Deployment](./09_deployment.md) |
| Meets primary threshold, borderline on secondary | ⚠️ **Conditional Go** — deploy with monitoring and a plan to improve |
| Below thresholds but still better than current process | ⚠️ **Discuss** — may still be worth deploying vs. the status quo |
| Significantly below thresholds or unstable | ❌ **No-Go** — iterate on [Stage 6](./06_data_preparation.md) or [Stage 7](./07_modeling.md), or revisit [Stage 2](./02_analytic_approach.md) |

```markdown
## Deployment Decision
* **Decision:** [Go / Conditional Go / No-Go]
* **Justification:** [Tie the decision to the acceptance thresholds and business impact]
  Example: "The model meets the AUC threshold (0.84 > 0.75) and is borderline on Recall
  (0.79 vs. 0.80 threshold). Given the significant business impact and the client's
  acceptance of threshold adjustment with monitoring, the decision is Conditional Go."

* **Conditions (if applicable):**
  Example: "Deploy with weekly Recall monitoring. If Recall drops below 0.70 on live data,
  trigger retraining (see Stage 10: Feedback)."

* **If No-Go — Next Steps:**
  Example: "Return to Stage 6 to engineer features for long-tenure customers. Re-enter
  the modeling cycle."

* **Signed Off By:** [Name — Role]
* **Date:** [YYYY-MM-DD]
```

---

## Step 6: Save Final Model & Evaluation Report

Save the final evaluated model and package the evaluation as a deliverable.

**Actions:**
- Save the final model (retrained on full training set) to the models directory.
- Export the evaluation report (this document, filled in) as a project deliverable.
- If the decision is Go, this model artifact is what gets deployed in [Stage 9](./09_deployment.md).

> 📚 **Reference:** See [Model Persistence](../04_mlops/01_model_persistence/) for saving the model with metadata, and [Monitoring and Maintenance](../04_mlops/06_monitoring_and_maintenance/) for setting up the monitoring plan referenced in the Conditional Go scenario.

```markdown
## Final Artifacts
* **Model File:** [Path]
  Example: "models/champion_xgboost_final_v1.joblib"

* **Evaluation Report:** [Path or location]
  Example: "reports/08_evaluation_report.md"

* **Status:** [Ready for Deployment / Requires Iteration]
```

---

## Checklist

Before moving to [Stage 9: Deployment](./09_deployment.md), confirm:

- [ ] Champion model is retrained on the full training set.
- [ ] Test set evaluation is complete with all primary and secondary metrics.
- [ ] CV vs. Test gap is assessed (no significant overfitting).
- [ ] Diagnostic visualizations are produced and interpreted.
- [ ] Business impact is quantified in client-friendly language.
- [ ] Model limitations and error costs are documented honestly.
- [ ] A go/no-go decision is obtained from the stakeholder.
- [ ] The final model artifact is saved and ready for deployment.

---

**Next:** [Deployment](./09_deployment.md) — Delivering the model to its end-users.