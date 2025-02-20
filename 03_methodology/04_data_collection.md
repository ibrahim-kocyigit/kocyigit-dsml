# Stage 4: Data Collection
_"In the initial data collection stage, data scientists identify and gather the available data resources—structured, unstructured and semi-structured—relevant to the problem domain. Typically, they must choose whether to make additional investments to obtain less-accessible data elements. It may be best to defer the investment decision until more is known about the data and the model. If there are gaps in data collection, the data scientist may have to revise the data requirements accordingly and collect new and/or more data._

_"While data sampling and subsetting are still important, today’s high-performance platforms and in-database analytic functionality let data scientists use much larger data sets containing much or even all of the available data. By incorporating more data, predictive models may be better able to represent rare events such as disease incidence or system failure."_ - **John B. Rollins**

## Step 1: Access Data Sources
Based on the data requirements and identified sources (from Stage 3), access the necessary data sources. This might involve connecting to databases, using APIs, downloading files, or accessing shared storage locations.

## Step 2: Extract Data
Extract the required data elements from each source. This may involve writing SQL queries, using API calls, or scripting file transfers.

## Step 3: Handle Data Retrieval Issues
Address any issues encountered during data retrieval, such as authentication problems, network errors, or data access restrictions. This may require collaboration with IT or data owners.

## Step 4: Store Raw Data
Store the extracted data in the `data/raw` (for internal data) or `data/external` (for external data) directory. Maintain the original format and structure of the data as received from the source. *Do not modify the raw data.* Use descriptive file names that clearly indicate the source and content.

## Step 5: Document the Collection Process
Document the data collection process, including the sources accessed, extraction methods used, any issues encountered, and the location of the raw data files. This documentation should be sufficient for someone else to reproduce the data collection process. Also, document any *failed* attempts to retrieve data, including the reasons for failure.

## Step 6: Manage Configuration and Secrets
Create and use a `.env` file to store sensitive information (API keys, database credentials, etc.) and configuration variables (e.g., database connection strings, API endpoints).  Use the `python-dotenv` package to load these variables into your code.

---

### Files to Create

1.  `reports/04_data_collection.md`: This Markdown file will document the data collection process.
2.  `data/raw/` and/or `data/external`: This directories will contain the raw data files.
3.  `src/dataset.py`: Python file with reusable data extraction functions.
4.  `notebooks/1.0-yourinitials-data_retrieval.ipynb`: Jupyter notebook with the specific data collection code.
5.  `.env`: (In the project root) This file stores secrets and configuration variables. This file should *never* be committed to version control (it should be in `.gitignore`). 
6. `src/config.py`: This file can be used to store configuration that affects the project in other ways. For example, constants, or file paths that might change between development and production. This is *not* for secrets.
7.  `references/`: Place here the document about data collection authorization.