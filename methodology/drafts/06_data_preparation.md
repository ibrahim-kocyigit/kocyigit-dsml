# Stage 6: Data Preparation
_"This stage encompasses all activities to construct the data set that will be used in the subsequent modeling stage. Data preparation activities include data cleaning (dealing with missing or invalid values, eliminating duplicates, formatting properly), combining data from multiple sources (files, tables, platforms) and transforming data into more useful variables._

_"In a process called feature engineering, data scientists can create additional explanatory variables, also referred to as predictors or features, through a combination of domain knowledge and existing structured variables. When text data is available, such as customer call center logs or physicians’ notes in unstructured or semi-structured form, text analytics is useful in deriving new structured variables to enrich the set of predictors and improve model accuracy._

_"Data preparation is usually the most time-consuming step in a data science project. In many domains, some data preparation steps are common across different problems. Automating certain data preparation steps in advance may accelerate the process by minimizing ad hoc preparation time. With today’s high-performance, massively parallel systems and analytic functionality residing where the data is stored, data scientists can more easily and rapidly prepare data using very large data sets."_ - **John B. Rollins**

## Step 1: Data Cleaning
Address the data quality issues identified in Stage 5. This may involve:

*   **Handling Missing Values:** Decide on a strategy for handling missing values (e.g., imputation, removal).
*   **Handling Outliers:** Determine if outliers are genuine or errors, and decide how to handle them (e.g., removal, transformation).
*   **Correcting Inconsistencies:** Resolve any inconsistencies in the data (e.g., different units of measurement, inconsistent capitalization).
*   **Data Type Conversions:** Convert data to correct types for further process.

## Step 2: Data Transformation
Transform the data to make it more suitable for modeling. This may involve:

*   **Scaling/Normalization:** Scale numerical features to a common range (e.g., standardization, min-max scaling).
*   **Encoding Categorical Variables:** Convert categorical variables into a numerical representation (e.g., one-hot encoding, label encoding).
*   **Date/Time Feature Extraction:** Extract relevant features from date/time variables (e.g., day of week, month, year).

## Step 3: Feature Engineering
Create new features from the existing data to potentially improve model performance. This is guided by domain knowledge and the insights gained during data understanding. Combine existing features, create interaction terms, or derive new variables based on business logic.

## Step 4: Data Combination
If data was collected from multiple sources, combine it into a single dataset for modeling. This may involve joining tables or merging dataframes. Ensure that the data is properly aligned and that keys are consistent.

## Step 5: Create Interim and Processed Datasets
*   Store the *intermediate* results of data cleaning and transformation in the `data/interim` directory. This allows you to track the changes made to the data and revert to earlier versions if needed.
*   Create the *final, processed* dataset that will be used for modeling and store it in the `data/processed` directory.

## Step 6: Document all steps
Document every action you took in this stage.
