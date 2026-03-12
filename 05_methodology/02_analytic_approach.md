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

