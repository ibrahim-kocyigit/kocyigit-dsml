# Stage 8: Evaluation
_"During model development and before deployment, the data scientist evaluates the model to understand its quality and ensure that it properly and fully addresses the business problem. Model evaluation entails computing various diagnostic measures and other outputs such as tables and graphs, enabling the data scientist to interpret the model’s quality and its efficacy in solving the problem. For a predictive model, data scientists use a testing set, which is independent of the training set but follows the same probability distribution and has a known outcome."_ - **John B. Rollins**


## Purpose
The goal of this stage is to rigorously evaluate the final "champion" model selected in Stage 7. We will use the held-back test set—data the model has never seen before—to obtain an unbiased estimate of its performance in the real world. The results will be compared against the project objectives and success criteria to make a final **go/no-go** decision for deployment.


## Step 1: Final Model Training
Before the final evaluation, the champion model (with its optimal hyperparameters found during tuning) is re-trained on the *entire* training dataset.

* **Action:** Take the best model and hyperparameters from Stage 7 and fit the model using all available training data (`X_train`, `y_train`).
* **Justification:** This step ensures the model learns from the maximum amount of data possible before it is finalized.

> **Final Training Log:**
>
> * ***Model:** [Example: Tuned Random Forest Classifier]*
> * ***Date of Training:** [e.g., 2025-06-20]*
> * ***Action:** The champion model was successfully re-trained on the complete training dataset.*


## Step 2: Performance on the Hold-Out Test Set
Use the final trained model to make predictions on the test set (`X_test`) and calculate the final performance metrics.

* **Action:** Generate predictions on `X_test` and compute the primary and secondary metrics defined in Stage 2.
* **Guiding Question:** How does the model's performance on the test set compare to the average performance seen during cross-validation? They should be reasonably close.

> **Final Performance Metrics:**
>
> | Metric | Cross-Validation Score (from Stage 7) | **Final Test Set Score** |
> | :--- | :--- | :--- |
> | *AUC* | *0.85 ± 0.01* | * **0.84** * |
> | *Recall* | *0.78 ± 0.03* | * **0.76** * |
> | *Accuracy*| *0.91 ± 0.01* | * **0.90** * |
>
> **Comment:** *[The model's performance on the unseen test set is consistent with the results from cross-validation, which gives us confidence that the model is stable and has generalized well.]*


## Step 3: Business Impact Analysis
Translate the final technical metrics into tangible business outcomes. This step is critical for communicating the value of the model to stakeholders.

* **Action:** Interpret the model's performance in the context of the business problem defined in Stage 1.
* **Guiding Questions:**
    * Does the model's performance meet the business success criteria?
    * What is the projected impact of this model if deployed (e.g., cost savings, revenue increase, number of customers identified)?
    * What are the risks associated with the model's errors (e.g., the cost of a False Positive vs. a False Negative)?

> **Business Impact Statement:**
>
> * *[Example: "The final model achieves a Recall of 76% on the test set. This translates to successfully identifying an estimated 3 out of every 4 customers who are likely to churn, meeting the primary business objective. The model's performance is projected to enable the retention team to target an additional 200 high-risk customers per month."]*


## Step 4: Final Model Review and Sign-Off
Present the final evaluation results and business impact analysis to the project sponsors and key stakeholders for a final decision on deployment.

* **Action:** Conduct a final model review meeting.
* **Action:** Obtain a formal go/no-go decision for deployment.

> **Deployment Decision:**
>
> * ***Decision:*** *[Go / No-Go for Deployment]*
> * ***Justification:*** *[Example: "The model's performance on the test set met the pre-defined success criteria. The business sponsor has approved moving to the deployment stage."]*
> * ***Next Steps:*** *[e.g., "Proceed to Stage 9 to package the model for production."]*


## Step 5: Final Documentation
Finalize all reports and documentation related to the model's performance.

* **Action:** Prepare the final evaluation report. This is a key project deliverable that documents the model's expected real-world performance.
* **Action:** Add a summary of this stage to the main project `README.md`.