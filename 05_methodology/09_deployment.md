# Stage 9: Deployment

_"Once a satisfactory model has been developed and is approved by the business sponsors, it is deployed into the production environment or a comparable test environment. Usually it is deployed in a limited way until its performance has been fully evaluated. Deployment may be as simple as generating a report with recommendations, or as involved as embedding the model in a complex workflow and scoring process managed by a custom application."_ — **John B. Rollins**

---

## Purpose

The model passed evaluation in [Stage 8](./08_evaluation.md) and the stakeholder said **Go**. Now you deliver it.

Rollins' quote is key: deployment can be *"as simple as generating a report"* or *"as involved as embedding the model in a complex workflow."* The delivery format was defined in [Stage 1: Solution Requirements](./01_business_understanding.md). This stage is about executing that plan.

> 💡 **Freelancer's note:** As a freelance data scientist, "deployment" is not always a production API on Kubernetes. It might be a Jupyter Notebook export, a scheduled script, a Streamlit app on a free tier, or a CSV emailed every Monday. Match the delivery to the client's actual needs and technical maturity. The [MLOps pillar](../04_mlops/) covers the full spectrum.

---

## Step 1: Choose the Deployment Strategy

Refer back to the [Solution Requirements from Stage 1](./01_business_understanding.md) — specifically the **output format**, **delivery mechanism**, and **cadence**. This determines everything else.

**Deployment Strategy Reference:**

| Client Need | Strategy | Deliverable | MLOps Reference |
| :--- | :--- | :--- | :--- |
| *"Give me a one-time analysis"* | **Report** | Notebook export (HTML/PDF) + summary document | — |
| *"Give me predictions every week"* | **Batch Prediction** | Scheduled script → CSV/database table on a cadence | — |
| *"Our CRM needs to call the model"* | **Real-Time API** | FastAPI service, containerized, deployed to cloud | [API Development](../04_mlops/02_api_development/), [Containerization](../04_mlops/03_containerization/), [Cloud Deployment](../04_mlops/04_cloud_deployment/) |
| *"Our team wants to explore scenarios"* | **Interactive Dashboard** | Streamlit app with sliders/inputs and live predictions | [Interactive Dashboards](../04_mlops/05_interactive_dashboards/) |
| *"We want the model + the code"* | **Code Handoff** | Clean repository with README, requirements.txt, and instructions | [Model Persistence](../04_mlops/01_model_persistence/) |

```markdown
## Deployment Strategy
* **Strategy:** [Report / Batch / API / Dashboard / Code Handoff]
* **Justification:** [How this maps to the Stage 1 solution requirements]
  Example: "The client's retention team needs weekly churn scores pushed to their CRM.
  This requires a batch prediction pipeline that runs every Monday and writes results
  to a shared CSV."

  Example: "The client wants to interactively explore what-if scenarios for property
  pricing. A Streamlit dashboard is the right fit."

  Example: "This is a one-time customer segmentation analysis. The deliverable is an
  HTML report with cluster profiles and a summary presentation."
```

---

## Step 2: Package the Model

Serialize the final model (or full Pipeline) into a portable artifact that can be loaded in the deployment environment.

**Actions:**
- Save the final trained model from [Stage 8](./08_evaluation.md) using joblib.
- If using a scikit-learn Pipeline, save the **full Pipeline** (preprocessing + model) — not just the model.
- Include metadata: training date, data shape, performance metrics, version.

> 📚 **Reference:** See [Model Persistence — Pickle and Joblib](../04_mlops/01_model_persistence/) for serialization best practices and why full Pipeline persistence matters.

```markdown
## Model Artifact
* **File:** [Path and filename]
  Example: "models/churn_pipeline_v1.0.joblib"

* **Contents:** [What's inside]
  Example: "Full scikit-learn Pipeline: OrdinalEncoder → StandardScaler → XGBClassifier"

* **Metadata:**
  - Algorithm: [Name + key hyperparameters]
  - Training date: [YYYY-MM-DD]
  - Training data: [rows × cols]
  - Test AUC: [value]
  - Test Recall: [value]
  - Version: [v1.0]
```

---

## Step 3: Build the Deployment Application

Implement the application that loads the model artifact and delivers predictions according to the strategy from Step 1.

### Actions by strategy

#### Report Delivery
- Export the evaluation notebook as HTML or PDF.
- Write a non-technical summary document.
- Package with the model artifact and data dictionary.

#### Batch Prediction
- Write a Python script that loads the model, reads new data, generates predictions, and saves the output.
- Schedule with cron, Airflow, or a simple cloud scheduler.

#### Real-Time API
- Build a FastAPI application with `/predict` endpoint.
- Define request/response schemas with Pydantic.
- Containerize with Docker.
- Deploy to a cloud platform.

#### Interactive Dashboard
- Build a Streamlit app with input widgets and live predictions.
- Deploy to Streamlit Community Cloud, Railway, or similar.

#### Code Handoff
- Clean and organize the project repository.
- Write a comprehensive README with setup and usage instructions.
- Include `requirements.txt` or `environment.yml`.

> 📚 **Reference:** The entire [MLOps pillar](../04_mlops/) was built for this step — from [API Development](../04_mlops/02_api_development/) through [Containerization](../04_mlops/03_containerization/) to [Cloud Deployment](../04_mlops/04_cloud_deployment/) and [Dashboards](../04_mlops/05_interactive_dashboards/).

```markdown
## Deployment Application
* **Strategy:** [From Step 1]
* **Application Code:** [Path or link]
  Example: "app/main.py (FastAPI), app/schemas.py (Pydantic models)"

* **Containerization:** [If applicable]
  Example: "Dockerfile + docker-compose.yml in /deploy/"

* **Dependencies:** [Path]
  Example: "requirements.txt — pinned versions for reproducibility"

* **Deployment Target:** [Where it runs]
  Example: "Railway (PaaS) — auto-deploys from main branch via GitHub Actions"
  Example: "Client's internal server — Docker image delivered via private registry"
  Example: "Streamlit Community Cloud — free tier, public URL"
  Example: "Email delivery — HTML report sent to client every Monday"
```

---

## Step 4: Test Before Go-Live

Test the deployment end-to-end before the client relies on it.

**Actions:**
- For APIs: test with sample requests (valid and invalid inputs), verify response format and latency.
- For dashboards: test all inputs, verify predictions match the notebook results.
- For batch scripts: run on a sample of new data, verify output format and correctness.
- For reports: proofread, verify all numbers match the evaluation, check formatting.
- If possible, have the client test the deliverable (User Acceptance Testing).

**Testing Checklist by Strategy:**

| Strategy | Test |
| :--- | :--- |
| **API** | Valid request → correct prediction? Invalid request → clear error? Latency acceptable? |
| **Dashboard** | All inputs work? Predictions match evaluation? Visualizations render correctly? |
| **Batch** | Script runs without errors? Output format correct? Row count matches? |
| **Report** | Numbers match evaluation? Visualizations clear? Non-technical summary understandable? |
| **Code Handoff** | Fresh clone → `pip install -r requirements.txt` → runs? README is complete? |

```markdown
## Testing Summary
* **Testing Method:** [Manual / UAT with client / Automated tests]
* **Date:** [YYYY-MM-DD]
* **Results:**
  - [ ] Predictions are correct (spot-checked against evaluation results)
  - [ ] Edge cases handled (invalid input, missing values, out-of-range values)
  - [ ] Output format matches client expectations
  - [ ] Performance is acceptable (latency / runtime)
* **Client Feedback:** [If UAT was conducted]
  Example: "Client confirmed the dashboard meets their needs. Requested adding a
  'download as CSV' button for the predictions table."
* **Status:** [Passed / Passed with minor changes / Failed]
```

---

## Step 5: Go Live

Release the deliverable to the client.

**Actions:**
- Execute the release plan (push to production, send the report, share the dashboard URL).
- Confirm the client can access and use the deliverable.
- Provide a handoff document or walkthrough session.

```markdown
## Release Log
* **Go-Live Date:** [YYYY-MM-DD]
* **Deliverable:** [What was delivered]
  Example: "Churn prediction API deployed to https://churn-api.railway.app"
  Example: "Customer segmentation report delivered via email (PDF + HTML)"
  Example: "Streamlit dashboard live at https://churn-dashboard.streamlit.app"
  Example: "Project repository access granted to client's GitHub organization"

* **Version:** [v1.0]
* **Client Confirmation:** [Client confirmed receipt and access on YYYY-MM-DD]
```

---

## Step 6: Handoff Documentation

Provide the client with everything they need to understand, use, and (if applicable) maintain the deliverable.

**Actions:**
- Write or compile a handoff document covering:

```markdown
## Handoff Document Contents

### 1. What Was Delivered
* [Brief description of the deliverable and what it does]

### 2. How to Use It
* [Step-by-step usage instructions for the end-user]
  Example (API): "Send a POST request to /predict with the customer's features. See
  the Swagger docs at /docs for the full schema."
  Example (Dashboard): "Open the URL, adjust the sliders, click Predict."
  Example (Report): "Open the PDF. Section 3 contains the segmentation results."

### 3. How to Maintain It (if applicable)
* [Instructions for keeping it running]
  Example: "The API auto-deploys from the main branch. To update the model, replace
  models/churn_pipeline_v1.0.joblib and push to main."

### 4. Known Limitations
* [From Stage 8 evaluation — what the model does NOT do well]

### 5. When to Retrain
* [Triggers for retraining — see Stage 10: Feedback]
  Example: "Retrain if Recall drops below 0.70 on live data, or every 6 months,
  whichever comes first."
```

> 📚 **Reference:** See [Monitoring and Maintenance](../04_mlops/06_monitoring_and_maintenance/) for logging, drift detection, and retraining strategies that support the maintenance section of the handoff.

---

## Checklist

Before moving to [Stage 10: Feedback](./10_feedback.md), confirm:

- [ ] Deployment strategy is chosen and justified based on Stage 1 requirements.
- [ ] Model artifact is saved (full Pipeline, versioned, with metadata).
- [ ] Deployment application is built and functional.
- [ ] End-to-end testing is complete (predictions verified, edge cases handled).
- [ ] Client has tested the deliverable (UAT) or confirmed it meets expectations.
- [ ] Deliverable is live and accessible to the client.
- [ ] Handoff documentation is provided (usage, maintenance, limitations, retraining triggers).

---

**Next:** [Feedback](./10_feedback.md) — Monitoring performance and iterating based on real-world results.