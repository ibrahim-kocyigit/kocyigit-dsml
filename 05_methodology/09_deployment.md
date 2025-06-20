# Stage 9: Deployment
_"Once a satisfactory model has been developed and is approved by the business sponsors, it is deployed into the production environment or a comparable test environment. Usually it is deployed in a limited way until its performance has been fully evaluated. Deployment may be as simple as generating a report with recommendations, or as involved as embedding the model in a complex workflow and scoring process managed by a custom application."_ - **John B. Rollins**


## Purpose
The goal of this stage is to take the validated champion model from Stage 8 and integrate it into the target business environment. This makes the model's predictions available to end-users or other systems to support decision-making and deliver the project's intended value.


## Step 1: Model Packaging
The first step is to serialize the final, trained model pipeline into a file. This file contains the entire state of our pre-processing steps and the trained model, ready to be loaded into another application.

* **Action:** Save the final model pipeline object to a single, versioned file.
* **Toolkit Connection:** This step uses the skills from `04_MLOps/01_Model_Persistence/`, typically using the `joblib` library.

> **Final Model Artifact:**
>
> * **Model:** *[Example: `Tuned Random Forest Classifier Pipeline`]*
> * **File Name:** *[Example: `churn_model_v1_0.joblib`]*
> * **Location:** *[Example: `/production_assets/`]*
> * **Date Packaged:** *[2025-06-20]*


## Step 2: Select Deployment Strategy
Based on the solution requirements from Stage 1, choose the appropriate method for deploying the model.

* **Action:** Select and document the deployment pattern.

> **Selected Deployment Strategy:**
>
> * *[Choose one and justify. Example: "A **Real-time API Service** was selected because the business needs to get on-demand churn predictions for individual customers from the main CRM application."]*
>
> ---
>
> * **Common Strategies:**
>     * **Batch Prediction:** The model runs on a schedule (e.g., nightly) on a large set of data. The output is a static file or database table of predictions.
>     * **Real-time API Service:** The model is wrapped in an API (e.g., using FastAPI) that can serve single or small-batch predictions on demand.
>     * **Interactive Dashboard:** The model is embedded in a user-facing dashboard (e.g., using Streamlit) for interactive exploration and what-if analysis.


## Step 3: Implement Deployment Application
Develop the application code that will load the model artifact and serve predictions according to the chosen strategy.

* **Action:** Write the application script (e.g., the FastAPI script, the Streamlit app).
* **Action:** Package the application and its dependencies for deployment (e.g., using a `Dockerfile`).
* **Toolkit Connection:** This step heavily utilizes skills from `04_MLOps`, such as `02_API_Development` and `03_Containerization`.

> **Implementation Details:**
>
> * **Application Code:** *[Link to `/deployment_app/main.py`]*
> * **Containerization:** *[Link to `/deployment_app/Dockerfile`]*
> * **Dependencies:** *[Link to `/deployment_app/requirements.txt`]*


## Step 4: Staging and User Acceptance Testing (UAT)
Before releasing to all users, deploy the application to a pre-production or "staging" environment for end-to-end testing.

* **Action:** Deploy the containerized application to a staging server.
* **Action:** Conduct thorough testing, including integration tests and UAT with key business users.
* **Guiding Questions:**
    * Does the API respond correctly to valid and invalid requests?
    * Is the prediction latency within the acceptable limits defined in Stage 1?
    * Do the business users confirm that the output and functionality meet their requirements?

> **UAT Summary:**
>
> * **Status:** *[Passed / Failed]*
> * **Date of UAT:** *[Insert Date]*
> * **Feedback:** *[Summarize feedback from business users. Example: "UAT passed. Users confirmed the output is understandable and meets their needs. Request to add a prediction timestamp to the API response."]*


## Step 5: Production Release
After successful testing, deploy the application to the live production environment.

* **Action:** Execute the production release plan.

> **Production Release Log:**
>
> * **Go-Live Date:** *[2025-XX-XX]*
> * **Environment URL / Location:** *[e.g., `http://api.internal/churn-predictor`]*
> * **Release Version:** *[v1.0]*


## Step 6: Final Documentation
Finalize all documentation related to the deployment process.

* **Action:** Create a deployment guide that includes instructions for running, maintaining, and troubleshooting the application.
* **Action:** Add a summary of this stage to the main project `README.md`.