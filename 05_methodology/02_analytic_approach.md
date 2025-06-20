# Stage 2: Analytic Approach
_"Once the business problem has been clearly stated, the data scientist can define the analytic approach to solving the problem. This stage entails expressing the problem in the context of statistical and machine-learning techniques, so the organization can identify the most suitable ones for the desired outcome. For example, if the goal is to predict a response such as “yes” or “no,” then the analytic approach could be defined as building, testing and implementing a classification model."_ - **John B. Rollins**


## Purpose
The goal of this stage is to reframe the business problem defined in Stage 1 into a formal data science and machine learning framework. This involves selecting the type of problem, proposing candidate algorithms, and defining the technical success metrics for evaluation.


## Step 1: Frame the Problem
Based on the project objectives, determine the appropriate family of machine learning techniques to use.

* **Action:** Select the analytical paradigm that aligns with the business goal.
* **Guiding Questions:**
    * Are we trying to predict a discrete category (e.g., "churn" / "no churn," "cat" / "dog")? -> **Classification**
    * Are we trying to predict a continuous quantity (e.g., price, sales amount, temperature)? -> **Regression**
    * Are we trying to discover natural groupings in the data without a predefined outcome? -> **Clustering**
    * Are we trying to find a simpler underlying structure in high-dimensional data? -> **Dimensionality Reduction**

> **ML Problem Framing:**
>
> * ***Type of Problem:*** *[Insert one: Supervised Classification, Supervised Regression, Unsupervised Clustering, etc.]*
> * ***Brief Justification:*** *[Explain why this framing fits the business objective. Example: "Since the business objective is to predict whether a customer will churn (a 'yes' or 'no' outcome), this is a supervised binary classification problem."]*


## Step 2: Identify Candidate Models
List potential algorithms that could solve the problem. It's good practice to start with a simple, interpretable baseline model and then list more complex candidates.

* **Action:** Propose a set of candidate algorithms to explore.
* **Guiding Questions:**
    * What is the simplest model that could solve this problem (e.g., Logistic/Linear Regression)? This will be our baseline.
    * Based on the solution requirements from Stage 1, is model interpretability important? (Consider Decision Trees, Linear Models).
    * Is raw predictive performance the top priority? (Consider Ensembles like Random Forest, or Gradient Boosting).
    * What are the assumptions of each candidate model? (e.g., linearity, feature independence).

> **Candidate Models:**
>
> 1.  **Baseline Model:** *[Example: Logistic Regression, due to its simplicity and high interpretability.]*
> 2.  **Candidate 2:** *[Example: Random Forest Classifier, to capture potential non-linear interactions between features.]*
> 3.  **Candidate 3:** *[Example: Gradient Boosting (XGBoost), for potentially higher predictive performance.]*


## Step 3: Define Technical Success Metrics
Translate the business success criteria from Stage 1 into specific, quantitative model evaluation metrics.

* **Action:** Select the primary and secondary metrics that will be used to evaluate and compare the candidate models.
* **Guiding Questions:**
    * If this is a classification problem, is the dataset imbalanced? If so, accuracy is not a good metric.
    * Does the business care more about minimizing False Positives (use **Precision**) or minimizing False Negatives (use **Recall**)?
    * Do we need a balanced measure? (Use **F1-Score** or **AUC**).
    * If this is a regression problem, are large errors especially bad? (Use **RMSE**). Is a simple, interpretable error measure better? (Use **MAE**).

> **Evaluation Metrics:**
>
> * **Primary Metric:** *[Example: AUC (Area Under the ROC Curve), as it provides a single, aggregate measure of performance across all classification thresholds.]*
> * **Secondary Metric:** *[Example: Recall, because the business cost of failing to identify a customer who will churn (a False Negative) is very high.]*
> * **Acceptance Threshold:** *[Example: The final model must achieve an AUC of at least 0.80 on the hold-out test set to be considered for deployment.]*


## Step 4: Outline the Experimental Design
Define the strategy for training and validating the models to ensure the results are robust and unbiased.

* **Action:** Document the plan for model validation.

> **Validation Strategy:**
>
> * The dataset will be split into a training set (70%) and a final hold-out test set (30%) using a stratified split to preserve class proportions.
> * During model selection and hyperparameter tuning, **5-fold cross-validation** will be performed on the training set to get a robust estimate of each model's performance.
> * The final, chosen model will be trained on the entire training set and evaluated once on the hold-out test set to produce the final reported metrics.


## Step 5: Documentation and Validation
Finalize the analytic approach and ensure all stakeholders understand the plan.

* **Action:** Prepare the final draft of this "Analytic Approach" document.
* **Action:** Distribute the document for review by technical leads and relevant business sponsors.
* **Action:** Add a summary of this stage to the main project `README.md`.

> **Validation Summary:**
>
> * ***Date Approved:*** *[Insert Date]*
> * ***Approved By:*** *[List Stakeholders]*