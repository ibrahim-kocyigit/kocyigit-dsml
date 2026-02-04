# Data Leakage and Other Pitfalls

## 1. What is Data Leakage?
**Data Leakage** occurs when your model's training data includes information that would **not be available in the real world** at the moment of prediction.

It is one of the most dangerous pitfalls in machine learning because it **deceives you**. Your model will perform amazingly well during training and testing (high accuracy, low error), but will fail miserably when deployed to production.

### Common Sources of Leakage

1. **Future Information:** Using tomorrow's data to predict todays outcome. For example, predicting if a user will churn, but including a feature like `account_closed_date`.
2. **Global Statistics:** Creating features using statistics (like mean or variance) calculated from the *entire* dataset (Train + Test) instead of just the Training set. For example, when you replace missing values with the mean of the *whole* column, you "leak" information about the test set values into the training set.

## 2. Mitigating Data Leakage
To prevent leakage, you must enforce strict separation between your datasets.

### 2.1. The Golden Rules of Preprocessing

**Fit on Train, Transform on Test:** Any data preprocessing pipeline (scaling, imputing, PCA) must be "fit" only on the Training data. The learned parameters (like mean and standard deviation) are then applied to transform the Test data.

### 2.2. Pipelines in Cross-Validation
When using Cross-Validation, it's easy to accidentally leak data if you preprocess the *entire* dataset before splitting it into folds.

**Solution:** Use a **Pipeline** inside your Grid Search. The pipeline ensures that for each fold of cross-validation, the preprocessing steps (scaling, PCA) are re-fitted *only* on that fold's training data.

### 2.3. Time-Series Split
If your data is temporal (time-dependent), a random train-test split causes leakage because the model can learn from the "future" random points to predict "past" points. 

**Solution:** Use **Time-Series Split**. This way the training set always precedes the test set in time and the training window expands over time, but never "peeks" into the future.

## 3. Interpreting Feature Importance
Most models (like Random Forests or Linear Regression) provide a "Feature Importance" score. While useful, these can be misleading.

### Pitfalls in Interpretation

1. **Correlation $\neq$ Causation:** A feature might be highly important for prediction (e.g., "carrying an umbrella" predicts "rain"), but it does not cause the outcome.
2. **Redundancy (Multicollinearity):** If two features are highly correlated (e.g., `square_feet` and `number_of_rooms`), the model might split the importance between them, making both less important than they actually are.
3. **Scale Sensitivity:** For models like Linear Regression (without scaling), a feature with large values (e.g., Salary) will have a tiny coefficient compared to a feature with small values (e.g., Age), even if it's important.
4. **Interactions:** Some features are only important when combined with others. A model that looks at features individually might miss these synergies.

## 4. Other Common Modeling Pitfalls

* **Metric Misinterpretation:** Optimizing for Accuracy when you have imbalanced classes (e.g., fraud detection) leads to useless models.
* **Class Imbalance:** Failing to address imbalance (via SMOTE or class weights) biases predictions toward the majority class.
* **Blind Automation:** Relying entirely on AutoML tools without understanding the data can lead to deploying models that rely on spurious correlations or leaked features.
* **Invalid "What-If" Scenarios:** If your model lacks causual features, you cannot use it to simulate outcomes (e.g., "What if we lower the price?"). The model predicts *correlations*, not the result of interventions.

## 5. Summary
* **Data Leakage** is essentially "cheating" by giving the model answers it shouldn't have.
* **Prevention:** Always split data *before* preprocessing. Use **Pipelines** for cross-validation. Use **Time-Series Split** for temporal data.
* **Feature Importance** is nuanced. Be wary of redundancy and correlation vs. causation.
* **Pitfalls:** Watch out for class imbalance, metric selection, and blind reliance on automation.

---

**Next:** [Machine Learning Pipelines and GridSearchCV Lab](./11_machine_learning_pipelines_and_gridsearchcv_lab.ipynb)
