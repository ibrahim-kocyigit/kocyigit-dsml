# Stage 7: Modeling

_"Starting with the first version of the prepared data set, the modeling stage focuses on developing predictive or descriptive models according to the previously defined analytic approach. With predictive models, data scientists use a training set (historical data in which the outcome of interest is known) to build the model. The modeling process is typically highly iterative as organizations gain intermediate insights, leading to refinements in data preparation and model specification. For a given technique, data scientists may try multiple algorithms with their respective parameters to find the best model for the available variables."_ - **John B. Rollins**

## Step 1: Split Data
* Split the processed data (from `data/processed`) into training, validation, and test sets.  The training set is used to train the model, the validation set is used for hyperparameter tuning, and the test set is used for a final, unbiased evaluation of the model's performance.  Common splits are 70/15/15 or 80/10/10.

## Step 2: Select Model(s)
* Based on the analytic approach (Stage 2) and the nature of the prepared data, select one or more specific model types to train (e.g., Logistic Regression, Random Forest, Gradient Boosting Machine, Neural Network).

## Step 3: Train Model(s)
* Train the selected model(s) using the training data.  This involves fitting the model's parameters to the data.

## Step 4: Tune Hyperparameters
* Use the validation set to tune the hyperparameters of the model(s). Hyperparameters are settings that control the learning process and model architecture, and they are not learned from the data.  Examples include the learning rate, the number of trees in a random forest, or the number of layers in a neural network.  Use techniques like cross-validation, grid search, or random search to find the optimal hyperparameter settings.

## Step 5: Select Best Model
* Based on the performance on the validation set, select the best-performing model and hyperparameter combination.  Choose appropriate evaluation metrics based on the problem type (e.g., accuracy, precision, recall, F1-score for classification; RMSE, MAE, R-squared for regression).

## Step 6: Save Trained Model(s)
* Save the trained model(s), including the best hyperparameters, to the `models` directory. This allows you to load and reuse the model later without retraining. Use a serialization format like pickle or joblib.

## Step 7: Document all steps
* Document every action you took in this stage.
* Add a summary of the stage report to the main project `README.md`