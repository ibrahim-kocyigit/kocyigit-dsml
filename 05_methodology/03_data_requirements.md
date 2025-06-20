# Stage 3: Data Requirements
_"The chosen analytic approach determines the data requirements. Specifically, the analytic methods to be used require certain data content, formats and representations, guided by domain knowledge."_ - **John B. Rollins**


## Purpose
The goal of this stage is to create a detailed specification of all the data needed to execute the analytic approach defined in Stage 2. This involves translating the proposed models and features into a concrete list of required data fields, formats, sources, and entities. This plan ensures that the data collection process is targeted and efficient.


## Step 1: Identify Data Sources
List all potential internal and external sources where the required data might reside.

* **Action:** Brainstorm and document all potential data sources.
* **Guiding Questions:**
    * Which internal databases (e.g., CRM, ERP, transactional databases) hold the necessary information?
    * Is relevant data available in flat files (CSVs, Excel spreadsheets) or data warehouses?
    * Are there third-party APIs that can provide valuable external data?
    * Who are the owners or subject matter experts for each data source?

> **Potential Data Sources:**
>
> | Source System | Description | Owner / Contact |
> | :--- | :--- | :--- |
> | *[Example: `PostgreSQL CRM_DB`]* | *[Customer relationship management database containing user profiles.]* | *[Sales Team Lead]* |
> | *[Example: `S3 Bucket: /sales_logs`]* | *[CSV files with daily transaction records.]* | *[Engineering Team]* |
> | *[Example: `External Weather API`]* | *[API for historical weather data by region.]* | *[External Vendor]* |


## Step 2: Define Required Data Fields
This is the core of the data requirements document. List every specific piece of information needed to create the features and the target variable for the model.

* **Action:** Create a detailed table of all required data fields.

> **Data Field Specifications:**
>
> | Data Entity | Field Name | Expected Data Type | Description & Business Rule | Example | Relevance to Objective |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | *Customer* | `customer_id` | *String* | *Unique identifier for each customer.* | `CUST-8472` | *Primary key for joining.* |
> | *Customer* | `signup_date` | *Date* | *The date the customer first subscribed.* | `2023-01-15` | *Needed to calculate customer tenure.* |
> | *Subscription*| `plan_type` | *String* | *The customer's current subscription tier ('Basic', 'Premium').* | `Premium` | *A key feature for the churn model.*|
> | *Usage* | `monthly_logins` | *Integer* | *Average number of logins per month over the last 6 months.* | `25` | *Hypothesized to correlate with engagement.*|
> | *Churn* | `churn_status` | *Boolean (0/1)* | **(Target Variable)** *Whether the customer churned in the last 30 days.* | `1` | *The outcome we are predicting.* |


## Step 3: Specify Data Formats and Granularity
Define the scope and technical format of the required data.

* **Action:** Detail the necessary level of detail, time frame, and format.

> **Format and Granularity:**
>
> * **Granularity:** *[Specify the level of detail. Example: "Data should be at the individual customer-month level."]*
> * **Timeframe:** *[Specify the historical depth needed. Example: "We require the last 24 months of customer activity data."]*
> * **Format:** *[Specify the expected format for data delivery. Example: "Data should be delivered as a single CSV file with comma delimiters and UTF-8 encoding."]*


## Step 4: Outline Data Privacy and Ethical Considerations
Identify any sensitive information and the rules governing its use. This is a critical step for responsible data science.

* **Action:** Document any Personally Identifiable Information (PII) or other sensitive data fields.
* **Guiding Questions:**
    * Does the data contain PII (e.g., names, email addresses, phone numbers)?
    * What are the legal or ethical constraints on using this data (e.g., GDPR, CCPA)?
    * Are there any data anonymization or aggregation requirements before use?

> **Privacy & Ethics Review:**
>
> * ***Sensitive Data Identified:*** *[List any PII fields.]*
> * ***Constraints & Requirements:*** *[Describe the handling protocol. Example: "All PII must be removed from the dataset before analysis. Customer IDs will be replaced with a non-reversible hash."]*


## Step 5: Documentation and Validation
Finalize the data requirements and get approval from data owners and stakeholders.

* **Action:** Prepare the final draft of this "Data Requirements" document.
* **Action:** Distribute for review by data engineers, database administrators, and relevant domain experts.
* **Action:** Add a summary of this stage to the main project `README.md`.

> **Validation Summary:**
>
> * ***Date Approved:*** *[Insert Date]*
> * ***Approved By:*** *[List Data Owners/SMEs]*