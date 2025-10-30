# Stage 2: Clues from the Analytic Approach Stage

## 1. The Target Variable: What is the Goal?

This is the first and most important question.

*   **Clue:** Is the target variable **continuous** (e.g., price, temperature) or **categorical** (e.g., spam/ham, disease/no-disease)?
*   **How to Check:** Look at the data type (`df[target].dtype`) and the number of unique values (`df[target].nunique()`).
*   **Model Implication:**
    *   **Continuous:** It's a **regression** problem. Your potential models are Linear/Polynomial Regression, SVM (SVR), KNN Regressor, Decision Tree/Random Forest Regressor, XGBoost Regressor.
    *   **Categorical:** It's a **classification** problem. Your potential models are Logistic Regression, SVM (SVC), KNN Classifier, Decision Tree/Random Forest Classifier, Naive Bayes, XGBoost Classifier.

*   **Clue:** If it's a classification problem, are the classes **balanced** or **imbalanced**?
*   **How to Check:** Use `df[target].value_counts().plot(kind='bar')`.
*   **Model/Hyperparameter Implication:**
    *   **Balanced:** Most models will work well out of the box. Accuracy is a reasonable (though not complete) metric.
    *   **Imbalanced:** This is a huge red flag!
        *   **Model Choice:** Tree-based models (Random Forest, XGBoost) often handle imbalance better than distance-based models.
        *   **Hyperparameters:** Use `class_weight='balanced'` in models like Logistic Regression, SVM, and Random Forest.
        *   **Evaluation:** Do NOT trust accuracy. Use Precision, Recall, F1-Score, and the Confusion Matrix.

---

# Stage 5: Clues from the Exploratory Data Analysis (EDA) Stage

---

## 2. Feature vs. Target Relationships: What are the Patterns?

This is where you decide between simple and complex models.

*   **Clue:** Is the relationship between numerical features and the target **linear** or **non-linear**?
*   **How to Check:** Create **scatter plots** of each key feature against the target variable.
*   **Model Implication:**
    *   **Linear:** A **Linear Regression** (for regression) or **Logistic Regression** (for classification) is a fantastic starting point and baseline. SVM with a `'linear'` kernel is also a strong choice.
    *   **Non-Linear (Curved):** Simple linear models will fail.
        *   **Regression:** Try **Polynomial Regression**. Or, move directly to more powerful models that capture non-linearity automatically, like **SVM with a non-linear kernel (RBF)**, **Decision Trees**, or **Random Forest/XGBoost**.
        *   **Classification:** **SVM (RBF kernel)**, **KNN**, **Decision Trees**, and **Random Forest/XGBoost** are all excellent choices.

---

## 3. Feature Properties: What is the Nature of the Data?

This dictates the preprocessing steps, which are vital for certain models.

*   **Clue:** Do the numerical features have **different scales**?
*   **How to Check:** Use `df.describe()` and look at the `min`, `max`, and `std` for each column. Are some in the 10s and others in the 100,000s?
*   **Model Implication:**
    *   **Models that are sensitive to scale (MUST scale features):**
        *   **Linear/Logistic Regression** (with regularization)
        *   **SVM**
        *   **K-Nearest Neighbors (KNN)**
        *   **Naive Bayes** (if using Gaussian NB)
    *   **Models that are not sensitive to scale (scaling optional but can be good practice):**
        *   **Decision Trees**
        *   **Random Forest**
        *   **XGBoost**

*   **Clue:** Are there significant **outliers**?
*   **How to Check:** Use **box plots** (`sns.boxplot(data=df)`).
*   **Model Implication:**
    *   **Sensitive to Outliers:** Linear/Logistic Regression and SVM can be pulled off-course by extreme outliers. You may need to remove or cap them.
    *   **Robust to Outliers:** Tree-based models like **Decision Trees**, **Random Forest**, and **XGBoost** are naturally robust to outliers.

---

## 4. Feature vs. Feature Relationships: Is There Redundancy?

*   **Clue:** Are your numerical features highly **correlated with each other** (multicollinearity)?
*   **How to Check:** Create a **correlation matrix heatmap** (`sns.heatmap(df.corr(), annot=True)`). Look for bright red or bright blue cells between feature pairs (not the target).
*   **Model Implication:**
    *   **Linear/Logistic Regression:** High multicollinearity makes the model's coefficients unstable and difficult to interpret. It's best to remove one of the highly correlated features.
    *   **Tree-Based Models (Random Forest, XGBoost):** These are much less affected by multicollinearity. They will naturally select one of the correlated features at a split, effectively ignoring the other.

---

## 5. Dataset Size and Dimensionality

*   **Clue:** How large is the dataset (rows and columns)?
*   **How to Check:** `df.shape`
*   **Model Implication:**
    *   **Small Dataset (< 10k rows):** Most models work. **SVM** can be very effective. High-variance models might overfit, so simpler models or strong regularization are good.
    *   **Medium Dataset (10k - 100k rows):** **Random Forest** and **XGBoost** often shine here.
    *   **Large Dataset (> 100k rows):** **XGBoost** and **LightGBM** are designed for this scale. Logistic Regression is also extremely fast. KNN and SVM (with non-linear kernels) can become very slow.
    *   **High Dimensionality (many columns):** **Naive Bayes** works surprisingly well. Tree-based models are also strong. It's crucial to perform feature selection.

---

## Summary Table: From Clue to Action

| EDA Clue | How to Find It | Model/Hyperparameter Implication |
| :--- | :--- | :--- |
| **Imbalanced Classes** | `value_counts()` | Use `class_weight='balanced'`. Trust F1/Precision/Recall over Accuracy. |
| **Linear Patterns** | Scatter Plots | Start with Linear/Logistic Regression as a baseline. |
| **Non-Linear Patterns** | Scatter Plots | Use SVM (RBF), KNN, or Tree-based models (Random Forest, XGBoost). |
| **Different Feature Scales**| `describe()` | **Must Scale** for SVM, KNN, Linear/Logistic Regression. |
| **Outliers** | Box Plots | Tree-based models are robust. For others, consider outlier removal. |
| **Multicollinearity** | Correlation Heatmap | Problematic for interpreting Linear/Logistic Regression. Less of an issue for trees. |
| **Large Dataset** | `df.shape` | Favor scalable models like XGBoost, LightGBM, Logistic Regression. |

