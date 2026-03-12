# Stage 10: Feedback

_"By collecting results from the implemented model, the organization gets feedback on the model's performance and its impact on the environment in which it was deployed. For example, feedback could take the form of response rates to a promotional campaign targeting a group of customers identified by the model as high-potential responders. Analyzing this feedback enables data scientists to refine the model to improve its accuracy and usefulness. They can automate some or all of the feedback-gathering and model assessment, refinement and redeployment steps to speed up the process of model refreshing for better outcomes."_ — **John B. Rollins**

---

## Purpose

A deployed model is not a finished product — it's a **living system**. The world changes, the data changes, and the model's performance degrades. This stage closes the lifecycle loop by monitoring, measuring, and deciding what happens next.

For some projects, this stage is brief — a one-time report doesn't need monitoring. For recurring predictions (APIs, batch pipelines, dashboards), this stage defines the ongoing maintenance contract between you and the client.

> 💡 **Freelancer's note:** The scope of this stage should be agreed upon in [Stage 1](./01_business_understanding.md). Is this a one-time project (deliver and done)? Or an ongoing engagement (deliver, monitor, retrain)? This distinction affects pricing, contract terms, and your time commitment.

---

## Step 1: Determine Feedback Scope

Not every project needs a full monitoring pipeline. Match the feedback approach to the deployment strategy from [Stage 9](./09_deployment.md).

| Deployment Type | Feedback Scope | What You Track |
| :--- | :--- | :--- |
| **One-time report** | Minimal | Client satisfaction, whether recommendations were acted on |
| **Batch predictions (recurring)** | Moderate | Prediction accuracy over time, data drift |
| **Real-time API** | Full | Latency, throughput, prediction accuracy, data drift, concept drift |
| **Interactive dashboard** | Moderate | Usage metrics, client feedback, whether inputs stay within training range |
| **Code handoff** | Minimal | Client feedback, support requests |

```markdown
## Feedback Scope
* **Deployment Type:** [From Stage 9]
* **Feedback Level:** [Minimal / Moderate / Full]
* **Monitoring Period:** [Duration of the engagement]
  Example: "3 months post-deployment, with monthly performance reviews."
  Example: "One-time delivery — feedback collected via a single follow-up meeting."
* **Responsible Party:** [Who monitors — you, the client, or both?]
  Example: "Freelancer monitors for the first 3 months, then hands off to the client's
  data team with documentation."
```

---

## Step 2: Set Up Monitoring & Logging

For projects that require ongoing monitoring, implement the systems to capture what you need.

**Actions:**
- Set up logging for predictions and (if applicable) true outcomes.
- Define alerts for when performance drops below acceptable thresholds.
- Keep it proportional — a simple CSV log may be enough for a batch pipeline; a full API needs structured logging.

**What to Monitor:**

| Category | What to Track | How |
| :--- | :--- | :--- |
| **Model performance** | Primary metric (AUC, RMSE, etc.) over time | Compare predictions to actual outcomes once available |
| **Data drift** | Input feature distributions shifting from training data | Statistical tests (KS test, PSI) or simple distribution plots |
| **Concept drift** | Relationship between features and target changing | Performance degradation even without data drift |
| **System health** | Latency, uptime, error rate | API logging, health checks |
| **Usage** | Prediction volume, user engagement | Request logs, dashboard analytics |

> 📚 **Reference:** See [Monitoring and Maintenance — Logging and Error Handling](../04_mlops/06_monitoring_and_maintenance/) for structured logging implementation, and [Data and Model Drift Concepts](../04_mlops/06_monitoring_and_maintenance/) for drift detection techniques.

```markdown
## Monitoring Setup
* **Logging Method:** [How predictions and outcomes are captured]
  Example: "Each prediction is logged to a CSV file with timestamp, input features,
  predicted class, and predicted probability."
  Example: "FastAPI middleware logs all requests/responses to a structured JSON log file."

* **Drift Detection:** [Method and frequency]
  Example: "Monthly: compare the distribution of input features against the training set
  using a KS test. Alert if p-value < 0.05 for any feature."

* **Alerts:** [What triggers an alert]
  Example: "Primary metric (Recall) drops below 0.70 on live data for two consecutive
  months → trigger retraining review."
```

---

## Step 3: Collect True Outcomes

For supervised models, you eventually learn whether the prediction was correct. Design the pipeline to capture this feedback.

**Actions:**
- Identify the **feedback delay** — how long until the true outcome is known.
- Set up a process to join predictions with actual outcomes.

**Feedback Delay Examples:**

| Problem | Feedback Delay | How to Collect |
| :--- | :--- | :--- |
| Churn prediction | 30 days (observation window) | Join prediction logs with subscription status 30 days later |
| Fraud detection | Minutes to days | Join with dispute/investigation results |
| Property valuation | Weeks to months | Compare prediction with actual sale price |
| Customer segmentation | N/A (unsupervised) | Validate via A/B test or domain expert review |
| Demand forecasting | 1 period ahead | Compare forecast with actual sales next period |

```markdown
## Outcome Collection
* **Feedback Delay:** [How long until the true outcome is known]
  Example: "30 days — we know if the customer actually churned one month after the prediction."

* **Collection Method:** [How predictions are matched to outcomes]
  Example: "A monthly script joins prediction_log.csv with crm_export.csv on customer_id.
  The result is saved to feedback/YYYY-MM_outcomes.csv."

* **First Feedback Available:** [Date]
  Example: "2026-04-12 — 30 days after the first live predictions on 2026-03-12."
```

---

## Step 4: Track Live Performance

Once true outcomes are available, compute the same metrics from [Stage 2](./02_analytic_approach.md) and [Stage 8](./08_evaluation.md) on live data. Track them over time.

**Actions:**
- Compute primary and secondary metrics on each feedback batch.
- Compare against the Stage 8 test set baseline.
- Plot performance over time to detect trends.

```markdown
## Live Performance Log
| Period | Primary Metric | Secondary Metric | Data Volume | Status |
| :--- | :--- | :--- | :--- | :--- |
| Stage 8 Test Set (baseline) | [value] | [value] | [N rows] | ✅ Baseline |
| [Month 1] | [value] | [value] | [N rows] | [✅ / ⚠️ / ❌] |
| [Month 2] | [value] | [value] | [N rows] | [✅ / ⚠️ / ❌] |
| [Month 3] | [value] | [value] | [N rows] | [✅ / ⚠️ / ❌] |

Example:
| Stage 8 Baseline | AUC: 0.84 | Recall: 0.79 | 9,665 rows | ✅ Baseline |
| April 2026 | AUC: 0.83 | Recall: 0.78 | 8,200 rows | ✅ Stable |
| May 2026 | AUC: 0.82 | Recall: 0.76 | 8,500 rows | ⚠️ Slight dip |
| June 2026 | AUC: 0.77 | Recall: 0.68 | 7,900 rows | ❌ Below threshold |

* **Trend:** [Stable / Gradual decline / Sudden drop]
* **Investigation:** [If declining, what changed?]
  Example: "June drop coincides with a major pricing change. New customer behavior is
  not represented in the training data — this is concept drift."
```

---

## Step 5: Measure Business Impact

Compare the **projected** business impact from [Stage 8](./08_evaluation.md) with the **actual** impact measured in production.

**Actions:**
- Work with the client to quantify the real business value generated.
- Compare against the projection from Stage 8.
- Document whether the project achieved its [Stage 1 objectives](./01_business_understanding.md).

```markdown
## Business Impact Assessment

## Projected vs. Actual
| Metric | Projected (Stage 8) | Actual | Status |
| :--- | :--- | :--- | :--- |
| [Business metric] | [projected value] | [actual value] | [Met / Not Met] |

Example:
| Monthly churners prevented | ~118 | 95 | ⚠️ Below projection |
| Monthly retained revenue | ~$59,000 | $47,500 | ⚠️ Below projection |
| Retention campaign conversion | 30% improvement | 22% improvement | ⚠️ Below projection |

* **Assessment:** [Did the project deliver on its business objectives?]
  Example: "The model delivered measurable value (~$47.5k/month) but below the projected
  $59k. The gap is attributed to the June performance drop (concept drift from pricing
  change). A retrained model is expected to close this gap."

## Client Feedback
* [Qualitative feedback from the client]
  Example: "The retention team reports the churn scores are useful and have changed how
  they prioritize outreach. They request adding a 'churn reason' column to the output."
```

> 💡 **Freelancer's tip:** This section is your **portfolio evidence**. A clear *"The model saved the client ~$47.5k/month"* is worth more than any technical description. Document it well — with the client's permission, this becomes a case study.

---

## Step 6: Decide Next Action

Based on Steps 4 and 5, make a formal decision about what happens next.

**Decision Framework:**

| Situation | Action | Where to Re-Enter the Methodology |
| :--- | :--- | :--- |
| Performance stable, business value delivered | **No action** — continue monitoring | Stay in Stage 10 |
| Performance gradually declining | **Retrain** on recent data | Re-enter at [Stage 4](./04_data_collection.md) (collect new data) → Stage 6 → Stage 7 |
| Sudden performance drop | **Investigate** — data issue or concept drift? | Diagnose first, then retrain or rebuild |
| Fundamental change in business problem | **Rebuild** — new analytic approach needed | Re-enter at [Stage 2](./02_analytic_approach.md) |
| Model no longer needed | **Decommission** | Archive artifacts and documentation |
| Client requests new features/capabilities | **New iteration** — scope expansion | Re-enter at [Stage 1](./01_business_understanding.md) |

> 📚 **Reference:** See [Model Retraining Strategies](../04_mlops/06_monitoring_and_maintenance/) for scheduled vs. triggered retraining approaches.

```markdown
## Next Action Decision
* **Decision:** [No Action / Retrain / Rebuild / Decommission / New Iteration]
* **Justification:** [Why this decision was made]
  Example: "Performance dropped below the Recall threshold (0.68 < 0.70) in June due
  to concept drift from a pricing change. Decision: Retrain the model including Q2 2026
  data. Re-enter the methodology at Stage 4 (Data Collection)."

* **Re-Entry Point:** [Which stage to return to]
* **Target Date:** [When the next cycle begins]
* **Signed Off By:** [Name — Role]
* **Date:** [YYYY-MM-DD]
```

---

## Step 7: Archive & Close the Cycle

Whether you're retraining, rebuilding, or closing the project, archive everything from this cycle.

**Actions:**
- Archive the current model version, its performance logs, and the business impact report.
- If the engagement is ending, conduct a final handoff meeting with the client.
- If retraining, version the new model as v2.0 and begin the next cycle.

```markdown
## Cycle Archive
* **Model Version:** [v1.0]
* **Lifecycle Period:** [Start date — End date]
* **Final Performance:** [Primary metric on last feedback batch]
* **Total Business Impact:** [Cumulative value delivered]
  Example: "Over the 3-month monitoring period, the model prevented an estimated
  280 churns, retaining ~$140,000 in revenue."

* **Artifacts Archived:**
  - [ ] Model file (models/champion_xgboost_v1.0.joblib)
  - [ ] Evaluation report (reports/08_evaluation_report.md)
  - [ ] Performance logs (feedback/performance_log.csv)
  - [ ] Business impact report (reports/10_business_impact.md)

* **Status:** [Closed / Transitioning to v2.0]
```

---

## Checklist

Before closing this cycle (or re-entering the methodology for the next iteration), confirm:

- [ ] Feedback scope is defined and matches the deployment type.
- [ ] Monitoring and logging are operational (if applicable).
- [ ] True outcomes are being collected and matched to predictions.
- [ ] Live performance is tracked over time and compared to the Stage 8 baseline.
- [ ] Business impact is measured and compared to projections.
- [ ] A formal decision is made: no action, retrain, rebuild, or decommission.
- [ ] If re-entering the methodology, the re-entry point and timeline are documented.
- [ ] All artifacts from this cycle are archived.

---

**This is the final stage of the methodology.** The lifecycle is a loop — if you retrain or rebuild, you re-enter at the appropriate stage and carry the lessons learned from this cycle forward.

