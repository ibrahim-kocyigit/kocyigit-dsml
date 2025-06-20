# Stage 4: Data Collection

*"In the initial data collection stage, data scientists identify and gather the available data resources—structured, unstructured and semi-structured—relevant to the problem domain. Typically, they must choose whether to make additional investments to obtain less-accessible data elements. It may be best to defer the investment decision until more is known about the data and the model. If there are gaps in data collection, the data scientist may have to revise the data requirements accordingly and collect new and/or more data."* - **John B. Rollins**


## Purpose

The goal of this stage is to gather the data specified in the Stage 3 Data Requirements document. This involves writing and executing scripts to query databases, access APIs, or process raw files, and then consolidating the raw data into an accessible location for the project.


## Step 1: Develop Data Collection Scripts

Write the necessary scripts to extract data from the sources identified in the previous stage.

  * **Action:** Write and version-control all scripts used for data extraction.
  * **Guiding Questions:**
      * What SQL query is needed to pull customer transaction history?
      * What Python script is required to access a necessary third-party API?
      * How will credentials and API keys be managed securely?
  * **Toolkit Connection:** This step heavily utilizes skills from the `02_Toolkit` pillar, such as `pandas.read_sql` or Python's `requests` library.

> **Scripts and Queries Log:**
>
>   * ***Customer Profile Data:*** *[Link to `/scripts/sql/get_customer_profiles.sql`]*
>   * ***Transaction Data:*** *[Link to `/scripts/python/get_transaction_logs.py`]*
>   * ***External Data:*** *[Link to `/scripts/python/get_external_data.py`]*


## Step 2: Execute Data Collection & Store Raw Data

Run the developed scripts and save the raw, unaltered output to a designated storage location.

  * **Action:** Execute the collection scripts.
  * **Guiding Questions:**
      * Where will the raw data be stored (e.g., a specific project folder like `/data/raw/`, a cloud storage bucket)?
      * What naming convention will be used for the raw files to ensure clarity and versioning (e.g., `YYYY-MM-DD_source_data.csv`)?

> **Execution Log:**
>
>   * ***Status:*** *[Completed / In Progress]*
>   * ***Date of Collection:*** *[e.g., 2025-06-20]*
>   * ***Raw Data Location:*** *[e.g., `/data/raw/`]*


## Step 3: Initial Data Ingestion and Verification

Perform a quick, high-level check to ensure the collected data is readable and appears correct. This is a sanity check, not a deep analysis.

  * **Action:** Load each raw data file into a Pandas DataFrame.
  * **Guiding Questions:**
      * Does the data load without errors?
      * Do the number of rows and columns seem reasonable?
      * By glancing at the first few rows (`.head()`) and the data types (`.info()`), does the data match expectations?

> **Initial Verification Output (`df.info()`):**
>
> ```
> > [Paste the output of df.info() for the primary raw dataset here to provide a quick summary of columns, non-null counts, and data types.]
> ```
>
> **Initial Verification Output (`df.head()`):**
>
> ```
> > [Paste the output of df.head() here.]
> ```


## Step 4: Document the Collected Data

Maintain a clear log of the datasets that have been collected. This is crucial for reproducibility.

  * **Action:** Fill out a log for each dataset acquired.

> **Data Collection Log:**
>
> | Source Name | Data Location/File | Date Collected | Version/Timestamp | Notes |
> | :--- | :--- | :--- | :--- | :--- |
> | *CRM DB* | `/data/raw/2025-06-20_customer_profiles.csv`| *2025-06-20* | *2025-06-20 19:30* | *Contains all active customer profiles.* |
> | *Sales Logs* | `/data/raw/2025-06-20_transactions.parquet`| *2025-06-20* | *2025-06-20 19:30* | *Transaction data for the last 24 months.*|


## Step 5: Final Review

Conclude the data collection phase. If significant data gaps were discovered that cannot be filled, it may be necessary to revisit Stage 2 (Analytic Approach) or Stage 3 (Data Requirements).

  * **Action:** Prepare a brief summary report of the data collection process.
  * **Action:** Add a summary of this stage to the main project `README.md`.

> **Stage Summary:**
>
>   * ***Status:*** *[Completed]*
>   * ***Key Findings:*** *[Note any successes or discovered gaps. Example: "Successfully collected customer profile and transaction data. The proposed external API was found to be deprecated; an alternative source needs to be identified or the analytic approach must be adjusted to proceed without this data."]*