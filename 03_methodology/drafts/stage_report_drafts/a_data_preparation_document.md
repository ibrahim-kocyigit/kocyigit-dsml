# Data Preparation Document

## 1. Introduction

*   **Project Name:** [Project Name - e.g., Customer Churn Prediction]
*   **Date:** [Date of creation/last update]
*   **Version:** [Version number, e.g., 1.0]
*   **Document Owner:** [Name and title of the person responsible for this document]
*   **Purpose of Document:** Briefly state the purpose of this document – to detail all data preparation steps performed, including data cleaning, transformation, feature engineering, and data splitting.

## 2. Data Source(s)

* Briefly list data sources.

## 3. Data Cleaning Steps

*   **3.1. Missing Values:**
    *   **Method Used:** Describe the method(s) used to handle missing values (e.g., deletion, imputation - specify the technique).  *Example: "Missing values in the `age` column were imputed using the median. Missing values in the `subscription_end_date` column were filled with a placeholder date of '9999-12-31'."*
    *   **Justification:** Explain *why* you chose the specific method(s). *Example: "Median imputation was chosen for `age` because the distribution is slightly skewed, and median is more robust to outliers than the mean."*
    *   **Columns Affected:** List the specific columns where missing values were handled.
    *   **Code/Scripts:** (Optional, but recommended) Include a reference to the code file(s) or notebook(s) where the data cleaning was performed.  *Example: "See `data_cleaning.ipynb` notebook, section 3.1."*
*   **3.2. Outliers:**
    *   **Method Used:** Describe the method(s) used to identify and handle outliers (e.g., removal, transformation, capping). *Example: "Outliers in the `monthly_usage` column were identified using the IQR method and capped at the 99th percentile."*
    *   **Justification:** Explain your reasoning. *Example: "Capping was chosen to reduce the influence of extreme usage values without removing potentially valid data points."*
    *   **Columns Affected:** List the specific columns.
    *   **Code/Scripts:** (Optional) Reference the relevant code.
*   **3.3. Duplicate Rows:**
    *   **Action Taken:** Describe how duplicate rows were handled (e.g., removed, investigated). *Example: "Duplicate rows were removed based on all columns." or "Duplicate customer IDs were investigated and found to be due to data entry errors; corrected records were retained."*
    *   **Justification:**  Explain your reasoning.
    *   **Number of Duplicates:**  State the number of duplicate rows found and (if applicable) removed.
    *   **Code/Scripts:** (Optional) Reference the relevant code.
*   **3.4. Inconsistent Data:**
    *   **Description of Inconsistencies:**  Describe any inconsistencies found (e.g., different spellings of categorical values, invalid values).
    *   **Method Used:** Describe how the inconsistencies were resolved. *Example: "All variations of 'United States' in the `country` column were standardized to 'USA'."*
    *   **Columns Affected:** List the specific columns.
    *   **Code/Scripts:** (Optional) Reference the relevant code.
* **3.5 Data Type Corrections:**
      * List all data type corrections.
      * **Code/Scripts:** (Optional) Reference the relevant code.

## 4. Data Combination Steps

* **4.1 Merging/Joining:**
  * Describe which data was merged.
  * Describe the method.
  * **Code/Scripts:** (Optional) Reference the relevant code.
* **4.2 Concatenating:**
  * Describe which data was concatenated.
  * Describe the method.
  * **Code/Scripts:** (Optional) Reference the relevant code.

## 5. Data Transformation Steps

*   **5.1. Scaling/Normalization:**
    *   **Method Used:** Describe the scaling/normalization method used (e.g., standardization, min-max scaling, robust scaling). *Example: "Numerical features were standardized using `StandardScaler`."*
    *   **Justification:** Explain why you chose the specific method.
    *   **Columns Affected:**  List the specific columns.
    *   **Code/Scripts:** (Optional) Reference the relevant code.
*   **5.2. Encoding Categorical Variables:**
    *   **Method Used:**  Describe the encoding method used (e.g., one-hot encoding, label encoding, target encoding). *Example: "The `plan_type` column was one-hot encoded using `pd.get_dummies()`."*
    *   **Justification:**  Explain your reasoning.
    *   **Columns Affected:** List the specific columns.
    *   **Code/Scripts:** (Optional) Reference the relevant code.
*   **5.3. Binning/Discretization:**
    *   **Method Used:** Describe the binning method (e.g., equal-width, equal-frequency, custom bins). *Example: "The `age` column was binned into three categories ('Young', 'Middle-Aged', 'Old') using `pd.cut()` with equal-width bins."*
    *   **Justification:** Explain your reasoning.
    *   **Columns Affected:**  List the specific columns.
    *   **Code/Scripts:** (Optional) Reference the relevant code.
*   **5.4. Date/Time Transformations:**
    *   **Features Extracted:** List the specific features extracted from date/time columns (e.g., year, month, day, day of week, hour).
    *   **Code/Scripts:** (Optional) Reference the relevant code.
* **5.5. Other Transformations:**
  * Describe all the other transformations.
  * **Code/Scripts:** (Optional) Reference the relevant code.

## 6. Feature Engineering Steps

*   **6.1. New Features Created:**
    *   **Feature Name:** List the name of each new feature created.
    *   **Description:**  Describe the feature and how it was created.
    *   **Rationale:**  Explain *why* you created the feature and how it might be useful for the model. *Example: "Created a new feature `interaction_ratio` by dividing `customer_service_interactions` by `months_subscribed`. This feature may capture the intensity of customer service needs relative to the subscription length."*
    *   **Code/Scripts:** (Optional) Reference the relevant code.
* **6.2 Feature Selection:**
  * List all the removed features
  * Rationale.

## 7. Data Splitting

*   **Splitting Strategy:** Describe how the data was split into training, validation, and test sets (e.g., random split, stratified split, time-based split). *Example: "The data was split into training (80%), validation (10%), and test (10%) sets using stratified sampling based on the `churn` variable."*
*   **Random State (if applicable):**  State the `random_state` used for reproducibility.
*   **Sizes of Datasets:** Report the number of records in each set (training, validation, test).
*   **Code/Scripts:** (Optional) Reference the relevant code.

## 8. Summary of Prepared Data

*   **Number of Records:**
*   **Number of Features:**
*   **Data Types:**

## 9. Approvals

*   **Data Scientist:** [Signature and Date]
*   **Project Manager (if applicable):** [Signature and Date]
*   **[Other Key Stakeholders]:** [Signature and Date]
