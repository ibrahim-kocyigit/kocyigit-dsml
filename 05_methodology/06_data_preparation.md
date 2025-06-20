# Stage 6: Data Preparation
_"This stage encompasses all activities to construct the data set that will be used in the subsequent modeling stage. Data preparation activities include data cleaning (dealing with missing or invalid values, eliminating duplicates, formatting properly), combining data from multiple sources (files, tables, platforms) and transforming data into more useful variables._

_"In a process called feature engineering, data scientists can create additional explanatory variables, also referred to as predictors or features, through a combination of domain knowledge and existing structured variables... Data preparation is usually the most time-consuming step in a data science project."_ - **John B. Rollins**

## Purpose
The goal of this stage is to execute all necessary cleaning, transformation, and feature engineering tasks to create the final, high-quality dataset that will be fed into the machine learning models. This is the bridge between raw, messy data and clean, structured features.


## Step 1: Data Cleaning
Address all data quality issues that were identified during the Data Understanding stage.

* **Action:** Apply cleaning techniques to the dataset.
* **Toolkit Connection:** This step heavily utilizes the `03_Pandas` library for data manipulation.

> **Data Cleaning Log:**
>
> * **Handling Missing Values:**
>   * *[Describe the strategy used. Example: "Missing values in the `Price` column were imputed using the median of the product's category, as discovered in Stage 5."]*
>
> * **Correcting Data Types:**
>   * *[Describe any type corrections. Example: "The `OrderID` column, initially loaded as an integer, was converted to a string object to prevent it from being treated as a numerical feature."]*
>
> * **Handling Outliers:**
>   * *[Describe the outlier handling strategy. Example: "Outliers in the `TotalPrice` column were capped at the 99th percentile to reduce the effect of extreme values."]*
>
> * **Removing Duplicates:**
>   * *[State the result of duplicate checks. Example: "A check for duplicate rows was performed and 12 fully duplicated rows were removed from the dataset."]*


## Step 2: Feature Engineering
Create new, potentially more informative features from the existing data.

* **Action:** Engineer new variables to improve model performance.
* **Guiding Questions:**
    * Can we extract useful information from a date (e.g., day of the week, month, quarter)?
    * Can we create interaction features (e.g., `price * quantity`)?
    * Can we create categorical features from numerical ones (e.g., "Age Bins")?
    * Can we combine several features to create a more powerful one (e.g., a "loyalty score")?

> **New Features Created:**
>
> | New Feature Name | Derivation / Formula | Justification |
> | :--- | :--- | :--- |
> | `TotalPrice` | `df['Price'] * df['Quantity']` | *Represents the total revenue for each transaction.* |
> | `OrderDayOfWeek`| `df['OrderDate'].dt.day_name()` | *To check if sales patterns differ on certain days of the week.* |
> | `IsWeekend` | `df['OrderDayOfWeek'].isin(['Saturday', 'Sunday'])` | *A binary feature to potentially capture a weekend effect.*|


## Step 3: Data Structuring and Final Selection
Combine different data sources (if necessary) and select the final set of features for modeling.

* **Action:** Perform any final merges or joins and drop any columns that will not be used in the model.

> **Data Structuring Summary:**
>
> * **Joins/Merges:** *[Describe any joins. Example: "The `sales` data was left-merged with the `customer_demographics` data on `customer_id`."]*
> * **Columns Dropped:** *[List columns that were removed and why. Example: "Dropped the original `Price` and `Quantity` columns as `TotalPrice` is now the primary feature of interest."]*


## Step 4: Final Dataset Split
Separate the clean, prepared data into the final feature matrix (`X`) and target vector (`y`), and then perform the train-test split.

* **Action:** Create the final training and testing sets.
* **Toolkit Connection:** This step uses `sklearn.model_selection.train_test_split` from the `03_specialization/02_scikit-learn_fundamentals` section.

> **Final Data Output:**
>
> * **Features Matrix (`X`):** *[List the final columns included in X.]*
> * **Target Vector (`y`):** *[Name the target column.]*
> * **Data Split:** *[Describe the split. Example: "The final dataset was split into a training set (70%) and a testing set (30%) using a stratified split on the target variable."]*
> * **Final Shapes:** `X_train: (rows, cols)`, `X_test: (rows, cols)`, `y_train: (rows,)`, `y_test: (rows,)`


## Step 5: Final Review
Conclude the data preparation stage. The output of this stage is the clean dataset that will be used for all subsequent modeling and evaluation.

* **Action:** Prepare a brief summary report of all data preparation steps. This documentation is critical for reproducibility.
* **Action:** Add a summary of this stage to the main project `README.md`.

> **Stage Summary:**
>
> * ***Status:*** *[Completed]*
> * ***Output:*** *[Describe the final dataset. Example: "The final dataset contains 5,250 training samples and 2,250 test samples, with 15 features ready for modeling. The data is stored at `/data/processed/clean_data.csv`."]*