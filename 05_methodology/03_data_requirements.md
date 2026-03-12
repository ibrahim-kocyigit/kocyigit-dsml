# Stage 3: Data Requirements

_"The chosen analytic approach determines the data requirements. Specifically, the analytic methods to be used require certain data content, formats and representations, guided by domain knowledge."_ — **John B. Rollins**

---

## Purpose

In [Stage 2](./02_analytic_approach.md), you defined *what type of problem* you're solving and *which algorithms* you'll try. Now you need to define **what data those algorithms need** — before anyone touches a database or opens a CSV.

This stage produces a **data shopping list**: the specific fields, sources, formats, and timeframes required to build the features and target variable for your model. It's the blueprint that makes [Stage 4: Data Collection](./04_data_collection.md) targeted and efficient instead of a wild goose chase.

> 💡 **Freelancer's note:** This stage is especially important when working with clients. They often say *"We have lots of data."* Your job is to translate that into *"I need these specific fields, from these specific sources, covering this specific time period."* The more precise you are now, the less back-and-forth later.

---

## Step 1: Identify the Target Variable

For supervised problems, the target variable was named in [Stage 2](./02_analytic_approach.md). Now define it precisely: where it comes from, how it's calculated, and what its values mean.

For unsupervised problems, there is no target — skip to Step 2.

**Actions:**
- Define the exact target variable name, type, and business definition.
- Clarify how the target is derived if it doesn't exist as a raw column (e.g., "churned" may need to be calculated from the last activity date).
- Confirm the target definition with the domain expert.

```markdown
## Target Variable Definition
* **Name:** [Column name]
* **Type:** [Binary (0/1), Multi-class (A/B/C), Continuous, etc.]
* **Definition:** [Precise business definition of this variable]

  Example (classification): "churn — 1 if the customer had zero activity in the 30 days
  following the observation date, 0 otherwise."

  Example (regression): "sale_price — the final transaction price of the property in USD,
  as recorded in the county assessor's database."

* **Known Issues:** [Any ambiguity, edge cases, or labeling concerns]
  Example: "Customers who downgraded to the free tier are counted as churned per the
  business sponsor's definition, even though they technically still have an account."
```

> ⚠️ **Common pitfall:** A vague target definition leads to a model that predicts the wrong thing. *"Churned"* means different things in different companies — define it precisely and get stakeholder confirmation.

---

## Step 2: Identify Data Sources

List every internal and external source where the required data might live.

**Actions:**
- Inventory all relevant systems (databases, data warehouses, flat files, APIs).
- For each source, identify the owner or point of contact.
- Note access requirements (credentials, VPN, NDA, data sharing agreements).

```markdown
## Data Sources
| Source | Type | Description | Owner / Contact | Access |
| :--- | :--- | :--- | :--- | :--- |
| [Example: `PostgreSQL — crm_db`] | Internal DB | Customer profiles, subscription history | [Sales Team Lead] | [DB credentials via IT] |
| [Example: `S3: /data/transactions/`] | Internal Files | Daily transaction CSVs | [Engineering Team] | [AWS IAM role] |
| [Example: `Open Weather API`] | External API | Historical weather by region | [Public API] | [Free tier, API key] |
| [Example: `client_export.xlsx`] | Client-provided | Manual export from client's internal tool | [Client PM] | [Email delivery] |
```

> 💡 For freelance projects, the most common scenario is: the client gives you a CSV or Excel export. Still document it here — it forces you to confirm the source, the freshness, and who to ask when you have questions.

---

## Step 3: Define Required Data Fields

This is the core of the data requirements document. List every field you need to build your features and target variable. Think through what the [candidate models from Stage 2](./02_analytic_approach.md) actually need as input.

**Actions:**
- List each required field with its source, type, description, and relevance.
- Mark the target variable explicitly.
- Include fields needed for **joining** tables (keys) and for **filtering** (e.g., date ranges).
- Think about what raw data is needed to **derive** your features (e.g., you need `signup_date` and `observation_date` to calculate `tenure_months`).

```markdown
## Data Field Specifications
| Source | Field Name | Data Type | Description | Example | Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| crm_db | `customer_id` | String | Unique customer identifier | `CUST-8472` | Primary key |
| crm_db | `signup_date` | Date | Date of first subscription | `2023-01-15` | Derive tenure |
| crm_db | `plan_type` | Categorical | Subscription tier (Basic/Premium/Enterprise) | `Premium` | Feature |
| transactions | `monthly_spend` | Float | Average monthly spend over last 6 months | `149.99` | Feature |
| activity_log | `monthly_logins` | Integer | Average monthly logins over last 6 months | `25` | Feature |
| activity_log | `last_activity_date` | Date | Date of most recent platform activity | `2025-12-20` | Derive target |
| — | `churned` | Binary (0/1) | **TARGET** — No activity in 30 days post-observation | `1` | Target variable |
```

> 💡 **Regression example:** For a property valuation project, the fields might include `lot_size_sqft`, `bedrooms`, `year_built`, `zip_code`, `last_renovation_year`, and the target `sale_price`.

> 💡 **Clustering example:** For customer segmentation, the fields might include `total_spend`, `purchase_frequency`, `avg_basket_size`, `days_since_last_purchase` — with no target column.

---

## Step 4: Specify Format, Granularity & Timeframe

Define the technical shape of the data you need.

**Actions:**
- Specify the **granularity** (one row per what?).
- Specify the **timeframe** (how far back?).
- Specify the **delivery format** (CSV, database query, API, etc.).
- Specify the **expected volume** (approximate number of rows).

```markdown
## Format & Granularity
* **Granularity:** [One row per ___]
  Example: "One row per customer, with aggregated features over the last 6 months."
  Example: "One row per property sale transaction."

* **Timeframe:** [How much historical data is needed]
  Example: "All customer activity from 2023-01-01 to 2025-12-31."
  Example: "Property sales from the last 5 years in the Greater Munich area."

* **Format:** [How the data should be delivered]
  Example: "Single CSV file, comma-delimited, UTF-8 encoded."
  Example: "Direct read access to the PostgreSQL database via provided credentials."

* **Expected Volume:** [Approximate size]
  Example: "~50,000 customer records with 15–20 columns."
```

---

## Step 5: Data Privacy & Ethical Considerations

Identify sensitive data and document how it will be handled. This is non-negotiable — even for small freelance projects.

**Actions:**
- Flag any Personally Identifiable Information (PII) in the required fields.
- Document legal constraints (GDPR, CCPA, HIPAA, industry-specific regulations).
- Define the handling protocol (anonymization, pseudonymization, access restrictions).
- Confirm with the client that you're authorized to use this data for this purpose.

```markdown
## Privacy & Ethics Review
* **PII Fields Identified:** [List any fields that contain or could identify individuals]
  Example: "customer_name, email_address, phone_number"

* **Handling Protocol:**
  Example: "All PII will be removed before analysis. customer_id will be pseudonymized
  with a non-reversible hash. Raw data will be stored only locally and deleted after
  project completion."

* **Legal Constraints:**
  Example: "Client confirmed GDPR compliance. Data Processing Agreement (DPA) signed on
  [date]. Data may not be shared with third parties."

* **Authorization:**
  Example: "Client authorized use of this data for this project via email on [date]."
```

> ⚠️ **Freelancer's note:** Always get written confirmation (even an email) that you're authorized to use the data. This protects both you and the client.

---

## Step 6: Documentation & Stakeholder Approval

Package Steps 1–5 into a single data requirements document and get it approved before proceeding to collection.

**Actions:**
- Compile this document with all fields filled in.
- Send to the client / data owner for review — they need to confirm that the data you're requesting actually exists and can be provided.
- Resolve any gaps (missing fields, unavailable sources, access blockers).
- Secure approval.

```markdown
## Approval
* **Date:** [YYYY-MM-DD]
* **Reviewed By:** [Name — Role]
* **Data Gaps Identified:** [Any fields that were requested but don't exist or can't be provided]
* **Status:** [Approved / Pending Data Access]
```

---

## Checklist

Before moving to [Stage 4: Data Collection](./04_data_collection.md), confirm:

- [ ] The target variable is precisely defined (for supervised problems).
- [ ] All data sources are identified with owners and access requirements.
- [ ] Every required field is listed with type, description, and relevance.
- [ ] The granularity, timeframe, format, and expected volume are specified.
- [ ] PII is identified and a handling protocol is documented.
- [ ] Written authorization to use the data is obtained.
- [ ] The client / data owner has confirmed the data exists and can be delivered.

---

**Next:** [Data Collection](./04_data_collection.md) — Acquiring the data defined in this stage.