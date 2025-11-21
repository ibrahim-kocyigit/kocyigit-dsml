# Stage 4: Data Collection

*"In the initial data collection stage, data scientists identify and gather the available data resources—structured, unstructured and semi-structured—relevant to the problem domain. Typically, they can perform a mini-ETL process to get the data into a single location."* - John B. Rollins

## Purpose

The goal of this stage is to gather the data specified in the Stage 3 Data Requirements document. This involves writing and executing an initial **Extract, Transform, and Load (ETL)** process to create a clean, versionable, and raw dataset that will serve as the starting point for the entire project.

## Step 1: Develop Data Extraction Scripts
Write the necessary scripts to **Extract** data from the sources identified in the previous stage.

* **Action:** Write and version-control all scripts used for data extraction.
* **Guiding Questions:**
    * What SQL query is needed to pull customer transaction history?
    * What Python script is required to access a necessary third-party API or a library like scikit-learn?
    * How will credentials and API keys be managed securely?

## Step 2: Perform Initial Transformation
Perform lightweight, essential transformations to standardize the extracted data. This is the **Transform** step. It is NOT the same as the deep data preparation that will happen in Stage 6.

* **Action:** Apply basic schema and type corrections.
* **Guiding Questions:**
    * Do column names need to be renamed to a consistent format (e.g., snake_case)?
    * Do any data types need immediate, obvious correction (e.g., a date field that is clearly a string)?
    * Is there any data that is completely outside the project scope and can be filtered out now?

## Step 3: Load and Store Raw Data
**Load** the transformed data into a designated storage location. This file is the raw, versionable starting point for your analysis.

* **Action:** Execute the collection and transformation scripts and save the output.
* **Guiding Questions:**
    * Where will the raw data be stored (e.g., a project folder like `/data/raw/` or `/data/interim/`)?
    * What naming convention will be used for the raw files to ensure clarity and versioning (e.g., `YYYY-MM-DD_source_data.csv`)?

## Step 4: Initial Data Ingestion and Verification
Perform a quick, high-level check to ensure the collected and stored data is readable and appears correct. This is a sanity check, not a deep analysis.

* **Action:** Load the final raw data file into a Pandas DataFrame and perform a quick verification.
* **Guiding Questions:**
    * Does the data load without errors?
    * Do the number of rows and columns seem reasonable?
    * By glancing at the first few rows (`.head()`) and the data types (`.info()`), does the data match expectations from the ETL process?

```markdown
### Initial Data Ingestion and Verification
```[Paste the output of df.info() for the primary raw dataset here to provide a quick summary of columns, non-null counts, and data types.]```

```[Paste the output of df.head() here.]```
```

## Step 5: Document the Collected Data
Maintain a clear log of the datasets that have been collected. This is crucial for reproducibility.

* **Action:** Fill out a log for each dataset acquired.

```markdown
### Data Collection Log
| Source Name | Raw Data File | Date Collected | ETL Script Location | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Scikit-learn | `/data/interim/iris_multi_class_v1.csv`| 2025-11-21 | `/labs/07_multi_class_lab.ipynb` | Contains all 150 samples with 3 classes. |
| Sales Logs | `/data/raw/2025-06-20_transactions.parquet`| 2025-06-20 | `/scripts/get_transactions.py` | Transaction data for the last 24 months.|
```

## Step 6: Final Review
Conclude the data collection phase. If significant data gaps were discovered that cannot be filled, it may be necessary to revisit Stage 2 (Analytic Approach) or Stage 3 (Data Requirements).

* **Action:** Prepare a brief summary report of the data collection process.
* **Action:** Add a summary of this stage to the main project `README.md`.

```markdown
### Data Collection Review
* **Status:** *[Completed]*
* **Key Findings:** 
  * Summarize the results of the ETL process and initial data verification.
```

---

**Next:** [Data Understanding](./05_data_understanding.md)
