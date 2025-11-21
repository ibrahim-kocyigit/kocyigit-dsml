# Stage 4: Data Collection

*"In the initial data collection stage, data scientists identify and gather the available data resources... Typically, they can perform a mini-ETL process to get the data into a single location."* - John B. Rollins

## Purpose

The goal of this stage is to gather the data specified in the Stage 3 Data Requirements document. This involves writing and executing an initial **Extract, Transform, and Load (ETL)** process. The process begins by mirroring the source data into a `raw` storage layer and then producing a clean, standardized, and versionable `interim` dataset that will serve as the reliable starting point for all subsequent analysis.

## Step 1: Extract and Store Raw Data
First, we **Extract** the data from its original source and store it in an untouched, "raw" format. This creates a perfect, versionable mirror of the source system at the time of collection.

* **Action:** Write scripts to pull data from all sources (databases, APIs, libraries).
* **Action:** Save the output directly to a `/data/raw/` or `/data/external/` directory **without any modifications**. The schema and content should be identical to the source.
* **Guiding Questions:**
    * What SQL query, API call, or library function is needed to get the data?
    * What is the native format of the source data (e.g., JSON, raw CSV, Parquet)?
    * How are credentials and API keys managed securely?

```markdown
### Raw Data Storage Log
* **Data Source:** [Example: `sklearn.datasets.load_iris()`]
* **Raw Storage Location:** [Example: `/data/raw/2025-11-21_iris_raw.csv`]
* **Notes:** [Example: "Saved the original iris data with its native column names like 'sepal length (cm)'."]
```

## Step 2: Perform Initial Transformation
This is the **Transform** step. Here, we perform lightweight, essential transformations on the raw data to create a standardized and analysis-friendly version.

* **Action:** Load the raw data from `/data/raw/` or `/data/external/` and apply basic schema and type corrections.
* **Guiding Questions:**
    * Do column names need to be renamed to a consistent format (e.g., `snake_case`)?
    * Do any data types need immediate, obvious correction (e.g., a date field stored as an object)?
    * Are there any columns that are definitively out of scope and can be dropped?

```markdown
### Initial Transformation Log
* **Columns Renamed:** [Example: "`sepal length (cm)` -> `sepal_length`"]
* **Data Types Corrected:** [Example: "No type corrections were necessary at this stage."]
* **Columns Dropped:** [Example: "No columns were dropped."]
```

## Step 3: Load Interim Data
This is the **Load** step, where the transformed data is saved to an `interim` storage layer. This file becomes the clean, reliable starting point for all subsequent stages of the project.

* **Action:** Save the transformed DataFrame to the `/data/interim/` directory.
* **Guiding Questions:**
    * What is the clear, versioned name for this interim dataset (e.g., `iris_multi_class_v1.csv`)?
    * What is the most appropriate file format for analytical work (e.g., CSV, Parquet)?

```markdown
### Interim Data Load Log
* **Interim Data Location:** [Example: `/data/interim/iris_multi_class_v1.csv`]
* **Author:** ibrahim-kocyigit
* **Timestamp:** 2025-11-21 09:42:41
```

## Step 4: Initial Data Ingestion and Verification
Perform a quick, high-level check to ensure the final `interim` data is readable and appears correct. This is a sanity check, not a deep analysis.

* **Action:** Load the `interim` data file into a new Pandas DataFrame and perform a quick verification.
* **Guiding Questions:**
    * Does the interim file load without errors?
    * Do the number of rows and columns seem reasonable?
    * By glancing at `.head()` and `.info()`, do the schema and data types match the transformations applied in Step 2?

## Step 5: Document the Data Lineage
Maintain a clear log of the datasets that have been created. This is crucial for reproducibility and understanding the data's journey.

* **Action:** Fill out a log that tracks the data from its raw state to its interim state.

```markdown
### Data Lineage Log
| Layer | Source Data | Destination File | ETL Script | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Raw | `sklearn.datasets.load_iris()` | `/data/raw/2025-11-21_iris_raw.csv` | `labs/07_multi_class_lab.ipynb` | Stores the untouched, original data. |
| Interim | `/data/raw/2025-11-21_iris_raw.csv` | `/data/interim/iris_multi_class_v1.csv` | `labs/07_multi_class_lab.ipynb` | Standardized column names and types. |
```

## Step 6: Final Review
Conclude the data collection phase. If significant data gaps were discovered, it may be necessary to revisit previous stages. The primary deliverable of this stage is the `interim` dataset.

* **Action:** Prepare a brief summary report of the ETL process.
* **Action:** Add a summary of this stage to the main project `README.md`.

```markdown
### Data Collection Review
* **Status:** [Completed]
* **Key Findings:** The ETL process was completed successfully. The original Iris data was extracted, its columns were renamed to snake_case, and the resulting clean dataset was saved to `/data/interim/`. The interim data has been verified and is ready for Stage 5.
```

---

**Next:** [Data Understanding](./05_data_understanding.md)