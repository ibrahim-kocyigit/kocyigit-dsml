# Stage 4: Data Collection

_"In the initial data collection stage, data scientists identify and gather the available data resources—structured, unstructured and semi-structured—relevant to the problem domain. Typically, they must choose whether to make additional investments to obtain less-accessible data elements. It may be best to defer the investment decision until more is known about the data and the model. If there are gaps in data collection, the data scientist may have to revise the data requirements accordingly and collect new and/or more data."_ - **John B. Rollins**

## Purpose

The goal of this stage is to gather the data specified in the Stage 3 Data Requirements by executing a foundational **Extract, Transform, and Load (ETL)** process. This involves pulling data from one or more sources, applying initial, lightweight transformations to standardize it, and loading the result into a clean, versionable "interim" dataset. This interim dataset serves as the reliable and consistent starting point for all subsequent analytical stages.

Our process uses a two-tiered staging area:
1.  **Raw (`/data/raw/`)**: A "write-once" layer that holds an exact, untouched copy of the source data.
2.  **Interim (`/data/interim/`)**: A layer that holds the cleaned and standardized data after the initial ETL, ready for analysis.

## Step 1: Extract
The first phase involves extracting the data from the source system(s). The goal is to get the data out of its original location and into our project's first staging area (`/data/raw/`) with as little modification as possible to create a perfect mirror of the source.

* **Action:** Write and execute scripts to pull data from all required sources (databases, APIs, libraries, etc.).
* **Action:** Save the output directly to the `/data/raw/` directory. The schema, content, and format should be identical to the source to ensure a "source of truth" is maintained.

```markdown
### Raw Data Extraction Log
* **Data Source:** `sklearn.datasets.load_iris()`
* **Raw Storage Location:** `/data/raw/2025-11-21_iris_raw.csv`
* **Author:** ibrahim-kocyigit
* **Timestamp (UTC):** 2025-11-21 09:55:56
* **Notes:** Saved the original iris data with its native column names like 'sepal length (cm)'.
```

## Step 2: Transform
In the **Transform** phase, a series of rules or functions are applied to the extracted raw data to prepare it for loading into the `interim` layer. For this initial ETL process, transformations are lightweight and focused on two key areas: **data quality** and **standardization**.

*   **Action:** Load the raw data from `/data/raw/`.
*   **Action:** Apply programmatic, rule-based data cleaning and validation to fix objectively invalid data.
*   **Action:** Apply basic schema and type corrections for standardization.

#### Guiding Questions for Transformation:
*   **Data Quality (Fixing Invalid Data):**
    *   Are there placeholder values (e.g., -999, "N/A", "null") that should be converted to a standard `NaN`?
    *   Are there values that are physically impossible or nonsensical based on business rules (e.g., `age < 0`, `rating > 5`)? These data entry errors should be corrected or nullified here.
*   **Standardization (Applying Schema):**
    *   Do column names need to be renamed to a consistent project format (e.g., `snake_case`)?
    *   Do any data types need immediate, obvious correction (e.g., a date field stored as an object, a number as a string)?

```markdown
### Initial Transformation Log
* **Data Quality Actions:** [Describe any cleaning actions. Example: "Converted -999 in `age` column to nulls."]
* **Columns Renamed:** [Describe schema changes. Example: "`sepal length (cm)` -> `sepal_length`", "`sepal width (cm)` -> `sepal_width`"]
* **Data Types Corrected:** [Example: "No type corrections were necessary at this stage."]
* **Validation:** [Example: "Confirmed that the dataset contains 150 rows and the expected number of columns after transformations."]
```

## Step 3: Load
The final phase of the ETL process is to load the transformed data into its target destination. In our methodology, this target is the `/data/interim/` directory, which makes the clean data available for the Data Understanding stage.

* **Action:** Save the transformed, clean DataFrame to the `/data/interim/` directory.
* **Action:** Use a clear, versioned naming convention for the output file.

```markdown
### Interim Data Load Log
* **Interim Data Location:** `/data/interim/iris_multi_class_v1.parquet`
* **Author:** ibrahim-kocyigit
* **Timestamp (UTC):** 2025-11-21 10:15:00
```

## Step 4: Verification
After the ETL process is complete, we perform a final sanity check to verify that the data in the `interim` staging area is correct and ready for use.

* **Action:** Load the `interim` data file into a Pandas DataFrame.
* **Action:** Perform a quick verification using `.info()` and `.head()` to ensure the schema, data types, and content match the transformations applied in Step 2.

## Step 5: Document the Data Lineage
Maintain a clear log of the datasets that have been created. This is crucial for reproducibility and understanding the data's journey.

```markdown
### Data Lineage Log
| Layer | Source Data | Destination File | ETL Script Location | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Raw | `sklearn.datasets.load_iris()` | `/data/raw/2025-11-21_iris_raw.csv` | `labs/07_multi_class_lab.ipynb` | Stores the untouched, original data. |
| Interim | `/data/raw/2025-11-21_iris_raw.csv` | `/data/interim/iris_multi_class_v1.parquet` | `labs/07_multi_class_lab.ipynb` | Standardized column names; corrected invalid values. |
```

## Step 6: Final Review
Conclude the data collection stage. The primary deliverable is the `interim` dataset, which is now the official starting point for all subsequent project stages.

* **Action:** Prepare a brief summary report of the ETL process.
* **Action:** Add a summary of this stage to the main project `README.md`.

```markdown
### Data Collection Review
* **Status:** Completed
* **Key Findings:** The ETL process was completed successfully. The original Iris data was extracted to `/data/raw/`, its columns were renamed to snake_case, and the resulting clean dataset was loaded to `/data/interim/`. The interim data has been verified and is ready for Stage 5.
```

---

**Next:** [Data Understanding](./05_data_understanding.md)