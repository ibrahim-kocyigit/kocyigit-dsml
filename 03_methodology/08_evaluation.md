# Stage 8: Evaluation
_"During model development and before deployment, the data scientist evaluates the model to understand its quality and ensure that it properly and fully addresses the business problem. Model evaluation entails computing various diagnostic measures and other outputs such as tables and graphs, enabling the data scientist to interpret the model’s quality and its efficacy in solving the problem. For a predictive model, data scientists use a testing set, which is independent of the training set but follows the same probability distribution and has a known outcome. The testing set is used to evaluate the model so it can be refined as needed. Sometimes the final model is applied also to a validation set for a final assessment._

_"In addition, data scientists may assign statistical significance tests to the model as further proof of its quality. This additional proof may be instrumental in justifying model implementation or taking actions when the stakes are high—such as an expensive supplemental medical protocol or a critical airplane flight system."_ - **John B. Rollins**

## Step 1: Load Trained Model
Load the best-performing trained model (from `models/`) that was selected in Stage 7.

## Step 2: Load Test Data
Load the test dataset (which was set aside in Stage 7 and has *not* been used for training or hyperparameter tuning).

## Step 3: Generate Predictions
Use the loaded model to generate predictions on the test data.

## Step 4: Evaluate Performance
Evaluate the model's performance on the test data using the same evaluation metrics used during model selection (in Stage 7). This provides an unbiased estimate of how well the model is likely to generalize to new, unseen data. Calculate confidence intervals for the evaluation metrics, if appropriate.

## Step 5: Assess Business Objectives
Evaluate whether the model's performance on the test set meets the business objectives and solution requirements defined in Stage 1. Is the model "good enough" to be deployed?

## Step 6: Document Results
Thoroughly document the evaluation results, including the performance metrics, confidence intervals (if applicable), and an assessment of whether the model meets the business objectives.

---

### Files to Create

1.  `reports/08_evaluation.md`: This Markdown file will contain the complete evaluation results, including performance metrics on the test set, confidence intervals, and a discussion of whether the model meets the business objectives.
2.  `notebooks/5.0-yourinitials-model_evaluation.ipynb`: Create a Jupyter notebook to perform the model evaluation on the test set. This notebook should load the trained model, load the test data, generate predictions, calculate evaluation metrics, and provide a clear assessment of the model's performance.
3. `Makefile`: Update it with commands to evaluate the model.