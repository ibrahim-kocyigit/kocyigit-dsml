# Stage 7: Modeling
_"Starting with the first version of the prepared data set, the modeling stage focuses on developing predictive or descriptive models according to the previously defined analytic approach. With predictive models, data scientists use a training set (historical data in which the outcome of interest is known) to build the model. The modeling process is typically highly iterative as organizations gain intermediate insights, leading to refinements in data preparation and model specification. For a given technique, data scientists may try multiple algorithms with their respective parameters to find the best model for the available variables."_ - **John B. Rollins**


## Purpose
The goal of this stage is to build, train, and tune the candidate models identified in the Analytic Approach (Stage 2). Using the prepared dataset from Stage 6, we will systematically evaluate our models using cross-validation and select the single "champion" model that best meets the project objectives.


## Step 1: Train Baseline Model
First, we train the simple baseline model identified in Stage 2. This provides a crucial benchmark against which all other, more complex models can be compared.

* **Action:** Train the baseline model using the training data (`X_train`, `y_train`).
* **Action:** Evaluate its performance using 5-fold cross-validation to get a robust score.
* **Models Connection:** This step utilizes code from the `03_specialization` pillar, such as `02_supervised_learning_regression/01_linear_regression/` or `02_supervised_learning_classification/01_logistic_regression/`.

> **Baseline Model Performance:**
>
> * **Model:** *[Example: Logistic Regression]*
> * **Cross-Validation Score (Primary Metric - e.g., AUC):** *[e.g., 0.78 ± 0.02]*
> * **Notes:** *[e.g., "Establishes the minimum acceptable performance. The model is fast and highly interpretable."]*


## Step 2: Train Candidate Models
Train the other, potentially more complex, candidate models. The goal here is to see if more sophisticated algorithms provide a significant performance lift over the baseline.

* **Action:** Train each candidate model on the training data.
* **Action:** Evaluate each using 5-fold cross-validation.

> **Candidate Model Performance Summary:**
>
> | Model Name | CV Score (Mean) | CV Score (Std Dev) | Training Time (s) | Initial Observations |
> | :--- | :--- | :--- | :--- | :--- |
> | *Random Forest* | *[e.g., 0.83]* | *[e.g., 0.02]* | *[e.g., 15.2]* | *[Significant lift over baseline, but slower.]* |
> | *SVM* | *[e.g., 0.81]* | *[e.g., 0.03]* | *[e.g., 45.7]* | *[Good performance but very slow to train.]* |
> | *Gradient Boosting* | *[e.g., 0.84]* | *[e.g., 0.02]* | *[e.g., 20.5]* | *[Highest performance out-of-the-box.]* |


## Step 3: Hyperparameter Tuning
For the most promising models (typically those with the best balance of performance and speed), perform a systematic search for the best hyperparameter settings.

* **Action:** Use `GridSearchCV` or `RandomizedSearchCV` to find the optimal hyperparameters for the top 1-2 candidate models.
* **Models Connection:** This step uses skills from `03_Models/04_Model_Improvement_and_Selection/`.

> **Hyperparameter Tuning Results:**
>
> * **Model Tuned:** *[Example: Random Forest Classifier]*
> * **Tuning Method:** *[e.g., RandomizedSearchCV with 50 iterations and 5-fold CV.]*
> * **Best Parameters Found:** *[e.g., `{'n_estimators': 300, 'max_depth': 12, 'min_samples_leaf': 4}`]*
> * **Best CV Score After Tuning:** *[e.g., 0.85 ± 0.01]*


## Step 4: Final Model Selection
Compare the robust, cross-validated scores of the tuned models and select the single "champion" model that will be used for the final evaluation and potential deployment.

* **Action:** Formally select the champion model and justify the choice.
* **Guiding Questions:**
    * Which model has the best performance on our primary technical metric?
    * Does the performance gain from a complex model justify any loss in interpretability or increase in prediction time?
    * Does the selected model meet the business success criteria outlined in Stage 1 and the technical acceptance threshold from Stage 2?

> **Champion Model Selection:**
>
> * **Selected Model:** *[Example: Tuned Random Forest Classifier]*
> * **Justification:** *[Example: "The tuned Random Forest provided a 7% lift in our primary AUC metric over the baseline and slightly outperformed the Gradient Boosting model. Its feature importance attribute also provides a good level of interpretability, satisfying the business requirement to understand key drivers."]*


## Step 5: Final Review
Conclude the modeling phase. The output of this stage is a single, trained model object and a report justifying its selection.

* **Action:** Prepare a brief summary report of the modeling process, experimental results, and final model selection.
* **Action:** Add a summary of this stage to the main project `README.md`.

> **Stage Summary:**
>
> * ***Status:*** *[Completed]*
> * ***Champion Model:*** *[Example: `Tuned Random Forest`]*
> * ***Expected Performance (from CV):*** *[e.g., `AUC = 0.85 ± 0.01`]*
> * ***Next Steps:*** *[e.g., "Proceed to Stage 8 to perform a final evaluation of the champion model on the held-back test set."]*