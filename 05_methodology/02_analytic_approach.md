# Stage 2: Analytic Approach

_"Once the business problem has been clearly stated, the data scientist can define the analytic approach to solving the problem. This stage entails expressing the problem in the context of statistical and machine-learning techniques, so the organization can identify the most suitable ones for the desired outcome. For example, if the goal is to predict a response such as "yes" or "no," then the analytic approach could be defined as building, testing and implementing a classification model."_ — **John B. Rollins**


---

## Purpose

This is the stage where you translate the business problem from [Stage 1](./01_business_understanding.md) into an **analytical framework**. You're answering: *"What type of data science problem is this, what algorithms could solve it, and how will we measure whether they work?"*

Everything here is still a **plan** — no data has been touched yet. But the decisions you make now shape the entire project: what data you need ([Stage 3](./03_data_requirements.md)), how you prepare it ([Stage 6](./06_data_preparation.md)), and how you evaluate the result ([Stage 8](./08_evaluation.md)).

> 💡 **Freelancer's note:** This stage is where you demonstrate technical credibility to the client. You're saying: *"Here's your problem in business terms. Here's how it maps to a known class of analytical problems. Here are the algorithms I'll try, and here's how I'll measure success."*

---

## Step 1: Frame the Problem Type

Map the business objective from [Stage 1](./01_business_understanding.md) to the correct analytical paradigm.

**Actions:**
- Determine whether this is a supervised or unsupervised problem.
- Identify the specific problem type.
- If supervised, identify the **target variable** (what we're predicting).

**Decision Guide:**

| Business Question | Problem Type | Target Variable |
| :--- | :--- | :--- |
| *"Will this customer churn?"* | Supervised — Binary Classification | `churned` (yes/no) |
| *"What category does this belong to?"* | Supervised — Multi-class Classification | `category` (A/B/C/...) |
| *"How much will this cost?"* | Supervised — Regression | `price` (continuous) |
| *"How many units will we sell?"* | Supervised — Regression | `units_sold` (continuous) |
| *"Are there natural customer segments?"* | Unsupervised — Clustering | None (discovered by the algorithm) |
| *"Which features matter most?"* | Unsupervised — Dimensionality Reduction | None |
| *"Is this transaction fraudulent?"* | Supervised — Binary Classification (imbalanced) | `is_fraud` (yes/no) |
| *"What drives customer satisfaction?"* | Statistical Inference — Regression | `satisfaction_score` (continuous) |

> 💡 Some projects combine multiple types. A customer segmentation project (clustering) may be followed by a churn prediction model (classification) trained separately per segment. Document this if applicable.

```markdown
## ML Problem Framing
* **Type of Problem:** [Supervised Classification / Supervised Regression / Unsupervised Clustering / etc.]
* **Target Variable:** [The column we're predicting, or "N/A" for unsupervised]
* **Justification:** [Why this framing fits the business objective.

  Example (classification): "The business objective is to predict whether a customer will
  churn (yes/no). This is a supervised binary classification problem."

  Example (regression): "The business objective is to estimate property values. Since the
  target is a continuous dollar amount, this is a supervised regression problem."

  Example (clustering): "The business wants to discover natural customer segments. Since
  there is no predefined target variable, this is an unsupervised clustering problem."]
```

---

## Step 2: Identify Candidate Models

Select a set of algorithms to explore. Always start with a **simple baseline** — it anchors your expectations and gives you a reference point for every subsequent model.

**Actions:**
- Choose a baseline model (simple, interpretable, fast).
- Choose 2–3 candidate models of increasing complexity.
- Consider the [interpretability requirement](./01_business_understanding.md) from Stage 1.

**Algorithm Reference:**

| Problem Type | Baseline | Candidates | When Interpretability Matters |
| :--- | :--- | :--- | :--- |
| **Binary Classification** | Logistic Regression | Random Forest, XGBoost, SVM | Logistic Regression, Decision Tree |
| **Multi-class Classification** | Logistic Regression (OvR) | Random Forest, XGBoost, KNN | Decision Tree, Logistic Regression |
| **Regression** | Linear Regression | Ridge/Lasso, Random Forest, XGBoost | Linear/Ridge Regression |
| **Clustering** | K-Means | DBSCAN, Hierarchical Clustering | K-Means |

> 📚 **Reference:** You can also use the [Candidate Models Tree](../03_specializations/02_machine_learning_with_python/candidate_models_tree.png) as an alternative to the table above. After listing the candidate model(s), check the [Candidate Models Guide](../03_specializations/02_machine_learning_with_python/candidate_models_guide.md) to confirm that model assumptions and your dataset characteristics are compatible.

```markdown
## Candidate Models
1. **Baseline:** [Algorithm — why]
   Example: "Logistic Regression — simple, fast, highly interpretable. Sets the performance floor."

2. **Candidate 2:** [Algorithm — why]
   Example: "Random Forest — captures non-linear feature interactions, robust to outliers."

3. **Candidate 3:** [Algorithm — why]
   Example: "XGBoost — typically highest predictive performance for tabular data."

* **Interpretability Note:** [Does the client need to understand WHY the model makes each prediction?
  If yes, prioritize Logistic Regression / Decision Trees, or plan to add SHAP explanations
  for complex models.]
```

---

## Step 3: Define Technical Success Metrics

Translate the **business success criteria** from [Stage 1](./01_business_understanding.md) into **quantitative model metrics**. This is where business language becomes data science language.

**Actions:**
- Choose a primary metric (the one you optimize for).
- Choose secondary metrics (additional perspectives on performance).
- Set an acceptance threshold (the minimum performance for deployment).

### Metric Selection Guide

#### Classification

| Situation | Primary Metric | Why |
| :--- | :--- | :--- |
| Balanced classes, general performance | **Accuracy** | Straightforward, easy to explain |
| Imbalanced classes | **AUC-ROC** or **F1-Score** | Accuracy is misleading when classes are skewed |
| Missing a positive is very costly (e.g., fraud, disease) | **Recall** | Minimizes False Negatives |
| False alarms are very costly (e.g., spam filter, legal) | **Precision** | Minimizes False Positives |
| Need a single balanced measure | **F1-Score** | Harmonic mean of Precision and Recall |


#### Regression

| Situation | Primary Metric | Why |
| :--- | :--- | :--- |
| General performance | **RMSE** | Penalizes large errors more heavily |
| Outliers are expected and shouldn't dominate | **MAE** | Robust to outliers |
| Need a relative measure (% error) | **MAPE** | Interpretable as percentage |
| Need to explain variance captured | **R²** | "The model explains X% of the variance" |

#### Clustering

| Situation | Metric | Why |
| :--- | :--- | :--- |
| No ground-truth labels | **Silhouette Score** | Measures cluster cohesion vs. separation |
| Need to choose number of clusters | **Elbow Method (Inertia)** | Visual heuristic for optimal k |
| Business validation | **Domain expert review** | Do the clusters make business sense? |


> 📚 **Reference:** See [Machine Learning with Python — Evaluating and Validating Models](../03_specializations/02_machine_learning_with_python/05_evaluating_and_validating_machine_learning_models/) for detailed coverage of these metrics.


```markdown
## Evaluation Metrics
* **Primary Metric:** [Metric — why it maps to the business objective]
  Example: "Recall — the business cost of missing a churning customer (False Negative) far
  outweighs the cost of a false alarm (False Positive)."

* **Secondary Metric(s):** [Additional metrics for a fuller picture]
  Example: "AUC-ROC for overall discrimination, Precision to monitor false alarm rate."

* **Acceptance Threshold:** [Minimum performance for deployment]
  Example: "The final model must achieve Recall ≥ 0.80 and AUC ≥ 0.75 on the holdout test
  set to be considered for deployment."
```

> ⚠️ **Common pitfall:** Don't set the threshold arbitrarily. Tie it to the business impact. If the current manual process catches 60% of churning customers, a model with 80% Recall is a meaningful improvement.

---

## Step 4: Outline the Validation Strategy

Define how you will train, validate, and test models to ensure results are **robust and unbiased**. This plan is executed in [Stage 7: Modeling](./07_modeling.md) and [Stage 8: Evaluation](./08_evaluation.md).

**Actions:**
- Define the train/test split strategy.
- Define the cross-validation approach for model selection.
- Consider whether stratification is needed (imbalanced classification).
- Consider whether time-based splitting is needed (time-series data).

```markdown
## Validation Strategy
* **Split:** [Train/Test ratio and method]
  Example: "80/20 stratified split to preserve class proportions."
  Example: "Time-based split — train on data before 2025-01, test on 2025-01 onward."

* **Cross-Validation:** [CV strategy for model selection and hyperparameter tuning]
  Example: "5-fold stratified cross-validation on the training set."

* **Final Evaluation:** [How the chosen model will be evaluated]
  Example: "The selected model will be retrained on the full training set and evaluated
  once on the holdout test set. These are the final reported metrics."
```

> ⚠️ **Critical rule:** The holdout test set is touched **exactly once** — at the very end, after all model selection and tuning is complete. If you evaluate on it during development, it's no longer a fair test.

---

## Step 5: Documentation & Stakeholder Communication

Package this stage into a clear document and communicate the plan to stakeholders. They don't need to understand every algorithm, but they should understand the *type* of approach you're taking and how you'll measure success.

**Actions:**
- Compile this Analytic Approach document (this file, filled in).
- Present a non-technical summary to the business sponsor: *"We're building a classification model to predict churn. We'll try three algorithms and pick the one that best catches at-risk customers. Here's how we'll measure that."*
- Get acknowledgment before proceeding to data work.

```markdown
## Approval
* **Date:** [YYYY-MM-DD]
* **Reviewed By:** [Name — Role]
* **Status:** [Approved / Pending Revisions]
```

---

## Checklist

Before moving to [Stage 3: Data Requirements](./03_data_requirements.md), confirm:

- [ ] The business problem is mapped to a specific problem type (classification, regression, clustering, etc.).
- [ ] The target variable is identified (for supervised problems).
- [ ] A baseline model and 2–3 candidate models are selected with justification.
- [ ] The primary evaluation metric is chosen and tied to the business objective.
- [ ] An acceptance threshold is set, grounded in business impact.
- [ ] The validation strategy (split, CV, final evaluation) is documented.
- [ ] The stakeholder understands the approach at a high level.

---

**Next:** [Data Requirements](./03_data_requirements.md) — Defining what data is needed to execute this analytic approach.