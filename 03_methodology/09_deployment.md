# Stage 9: Deployment
_"Once a satisfactory model has been developed and is approved by the business sponsors, it is deployed into the production environment or a comparable test environment. Usually it is deployed in a limited way until its performance has been fully evaluated. Deployment may be as simple as generating a report with recommendations, or as involved as embedding the model in a complex workflow and scoring process managed by a custom application. Deploying a model into an operational business process usually involves additional groups, skills and technologies from within the enterprise. For example, a sales group may deploy a response propensity model through a campaign management process created by a development team and administered by a marketing group."_ - **John B. Rollins**

## Step 1: Determine Deployment Type
Determine the appropriate deployment method for the model. This depends on the business requirements and how the model's predictions will be used. Options include:

* **Batch Prediction:** Generate predictions on a schedule (e.g., daily, weekly) for a large dataset.
* **Real-time Prediction:** Generate predictions on demand for individual requests (e.g., via a REST API).
* **Embedded Model:** Integrate the model directly into an existing application or system.
* **Report/Dashboard:** Generate a report or dashboard with recommendations based on the model's output.

## Step 2: Create Deployment Artifacts
Prepare the necessary artifacts for deployment. This may include:

* The trained model file (from `models/`).
* Code to load the model and generate predictions (`src/modeling/predict.py`).
* Any required data preprocessing steps (from `src/features.py`).
* A requirements file (`requirements.txt`) specifying the necessary Python packages.
* Configuration files (if needed).
* A containerization setup (e.g., Dockerfile) if deploying as a container.

## Step 3: Deploy the Model
Deploy the model according to the chosen deployment type. This might involve:

* Setting up a batch prediction pipeline using a scheduler (e.g., cron, Airflow).
* Creating a REST API using a framework like Flask or FastAPI.
* Integrating the model into an existing application.
* Creating a report or dashboard using a tool like Tableau or Power BI.

## Step 4: Monitor Model Performance
After deployment, continuously monitor the model's performance in the production environment. Track key metrics and set up alerts for any significant degradation in performance.

## Step 5: Document Deployment Process
Document the entire deployment process, including the deployment type, artifacts, steps taken, and monitoring setup.

---

### Files to Create

1.  `reports/09_deployment.md`: Document the deployment process, including the chosen deployment type, the steps taken, and the monitoring setup.
2.  `models/`: Ensure the final deployed model is in this directory.
3. `requirements.txt`: You should specify the necessary packages.
4.  `Dockerfile` (Optional): If deploying as a container, create a Dockerfile to define the container image.
5. Any additional scripts or configuration files needed for the specific deployment method. These might be located in a new `deployment/` directory at the project root, *if* they are substantial and not already covered by existing files (like `predict.py`). This keeps deployment-specific logic separate.
6. `Makefile`: Include command for deployment.