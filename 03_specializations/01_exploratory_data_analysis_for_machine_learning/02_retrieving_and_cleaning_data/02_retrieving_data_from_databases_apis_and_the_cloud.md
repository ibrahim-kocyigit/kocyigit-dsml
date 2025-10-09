# Retrieving Data from Databases, APIs, and the Cloud

## SQL Databases

- **SQL (Structured Query Language):**  
  - Used for highly structured, relational databases with fixed schemas.
  - Common SQL databases: Microsoft SQL Server, PostgreSQL, MySQL, AWS Redshift, Oracle DB, IBM Db2.

- **Python Libraries for SQL:**
  - `sqlite3` (for SQLite)
  - `SQLAlchemy` (works with many SQL databases)
  - `psycopg2` (for PostgreSQL)
  - `ibm_db` (for Db2)

- **Example: Reading from SQLite with Pandas**
    ```python
    import sqlite3
    import pandas as pd

    path = 'data/classic_rock.db'
    con = sqlite3.connect(path)
    query = "SELECT * FROM rock_songs"
    df = pd.read_sql(query, con)
    ```

## NoSQL Databases

- **NoSQL:**  
  - Non-relational databases, more flexible structure.
  - Often store data in JSON format.
  - Types: Document databases (e.g., MongoDB), graph databases, wide column stores.

- **Document Database Example (MongoDB):**
    ```python
    from pymongo import MongoClient
    import pandas as pd

    con = MongoClient()  # Add connection string if needed
    db = con['database_name']
    cursor = db['collection_name'].find({})  # Empty dict for all documents
    df = pd.DataFrame(list(cursor))
    ```

- **Other NoSQL Types:**
  - **Graph databases:** For network/relationship data (e.g., LinkedIn connections).
  - **Wide column families:** Group related columns (e.g., personal vs. professional info).

## APIs and Cloud Data Access

- **APIs (Application Programming Interfaces):**
  - Many data providers (e.g., Twitter, Amazon) offer APIs to access data programmatically.
  - Useful for real-time or regularly updated data.

- **Example: Reading Data from a URL**
    ```python
    import pandas as pd

    data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    df = pd.read_csv(data_url)
    ```

- **Cloud Data Sources:**
  - Data can be stored and accessed from cloud platforms (AWS, GCP, Azure, etc.).
  - Often accessed via APIs, SDKs, or direct URLs.

## Practical Considerations

- Each data source may require different libraries and connection methods.
- Pay attention to data formats, authentication, and arguments for reading functions.
- Always check documentation for specific connection and data retrieval options.

---

**Next:** [Data Cleaning](./03_data_cleaning.md)