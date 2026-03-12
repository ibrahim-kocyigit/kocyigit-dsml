# Stage 4: Data Collection

_"In the initial data collection stage, data scientists identify and gather the available data resources—structured, unstructured and semi-structured—relevant to the problem domain. Typically, they must choose whether to make additional investments to obtain less-accessible data elements. It may be best to defer the investment decision until more is known about the data and the model. If there are gaps in data collection, the data scientist may have to revise the data requirements accordingly and collect new and/or more data."_ — **John B. Rollins**

---

## Purpose

In [Stage 3](./03_data_requirements.md), you defined *what data you need*. Now you acquire it.

This stage follows an **ELT (Extract, Load, Transform)** process — the natural workflow for a data scientist working in Python:

1. **Extract** — Pull data from the source(s).
2. **Load** — Save an exact, untouched copy to `/data/raw/`. This is your immutable source of truth.
3. **Transform** — Apply lightweight standardization to produce a clean `/data/interim/` dataset ready for exploration.

### Why ELT (not ETL)?

For a freelancer working in Pandas, **ELT is the better pattern**:

| | ETL (Extract → Transform → Load) | ELT (Extract → Load → Transform) |
| :--- | :--- | :--- |
| **Raw data preserved?** | Only if you add an extra step | **Yes — always.** Raw is saved first. |
| **Can I re-transform?** | Need to re-extract from source | **Yes — raw copy is always there.** |
| **Where does transformation happen?** | In a separate pipeline before loading | **In your analysis environment (Pandas, notebook)** |
| **Best for** | Data engineering pipelines, warehouses | **Data science projects, freelance work** |

The key advantage: if your cleaning logic was wrong, or if the client changes requirements, you don't need to go back to the source. You just re-transform from `/data/raw/`.

### Project Directory Structure

```
data/
├── raw/          # Untouched source data. Write-once. Never modify.
├── interim/      # Standardized data after initial cleaning. Starting point for analysis.
└── processed/    # Final model-ready datasets (created in Stage 6: Data Preparation)
```

---

## Step 1: Extract

Pull the data from the source(s) identified in [Stage 3](./03_data_requirements.md). The goal is to get the data out of its original location with **zero modification**.

**Actions:**
- Write and execute extraction scripts (database queries, API calls, file downloads).
- For each source, save the output exactly as received — same schema, same encoding, same format.
- If the client provides a file, save it as-is with a date prefix.

**Common Extraction Patterns:**

| Source Type | Method | Example |
| :--- | :--- | :--- |
| Client-provided file | Copy to `/data/raw/` | `cp client_export.xlsx data/raw/2026-03-12_client_export.xlsx` |
| SQL database | `pd.read_sql()` → save to CSV/Parquet | Query the database, save result |
| REST API | `requests.get()` → save JSON/CSV | Fetch paginated results, save response |
| Python library | `sklearn.datasets`, `seaborn.load_dataset()` | Load and save directly |
| Web scraping | `BeautifulSoup` / `requests` | Parse HTML, save structured output |

> 📚 **Reference:** See [Pandas Fundamentals — Reading and Writing Data](../02_toolkit/03_pandas_fundamentals/) for `pd.read_csv()`, `pd.read_excel()`, `pd.read_sql()`, and `pd.read_json()`.

```markdown
## Extraction Log
| Source | Method | Raw File | Date | Notes |
| :--- | :--- | :--- | :--- | :--- |
| [Source name] | [How extracted] | [Path in /data/raw/] | [YYYY-MM-DD] | [Any notes] |

Example:
| crm_db | pd.read_sql() | /data/raw/2026-03-12_customers.csv | 2026-03-12 | 48,327 rows extracted |
| client email | Manual save | /data/raw/2026-03-12_transactions.xlsx | 2026-03-12 | Received from client PM |
| Open Weather API | requests.get() | /data/raw/2026-03-12_weather.json | 2026-03-12 | Munich region, last 24 months |
```

---

## Step 2: Load (Raw)

Save the extracted data to `/data/raw/` — the **immutable** layer. This copy is never modified. It exists so you can always go back to the original source data without re-extracting.

**Actions:**
- Verify that each raw file is saved with a clear, dated naming convention.
- Confirm the raw files match the source (row counts, column counts, encoding).
- Do **not** rename columns, fix types, or clean anything at this stage.

**Naming Convention:**

```
/data/raw/{YYYY-MM-DD}_{source_description}.{ext}

Examples:
/data/raw/2026-03-12_customers.csv
/data/raw/2026-03-12_transactions.xlsx
/data/raw/2026-03-12_weather.json
```

> ⚠️ **Rule:** The `/data/raw/` directory is **write-once**. Once a file is saved here, it is never edited. If you receive updated data from the client, save it as a new file with a new date.

---

## Step 3: Transform (Raw → Interim)

Now that the raw data is safely stored, apply **lightweight, rule-based transformations** to produce a standardized interim dataset. This is not the full feature engineering — that happens in [Stage 6: Data Preparation](./06_data_preparation.md). Here you're only fixing objective issues.

**Actions:**
- Load from `/data/raw/`.
- Apply standardization and basic data quality fixes.
- Save the result to `/data/interim/`.

### What belongs in this transform:

| Category | Actions | Examples |
| :--- | :--- | :--- |
| **Column standardization** | Rename to consistent format | `sepal length (cm)` → `sepal_length_cm` |
| **Type corrections** | Fix obviously wrong dtypes | Date stored as string → `pd.to_datetime()` |
| **Placeholder cleanup** | Convert sentinel values to NaN | `-999`, `"N/A"`, `"null"`, `""` → `np.nan` |
| **Impossible values** | Nullify data entry errors | `age = -5` → `NaN`, `rating = 11` (scale 1–10) → `NaN` |
| **Joining** | Merge multiple raw sources into one table | Join customers + transactions on `customer_id` |
| **Filtering** | Apply the timeframe from Stage 3 | Keep only rows where `date >= '2024-01-01'` |

### What does NOT belong here (save for [Stage 6](./06_data_preparation.md)):

- Feature engineering (creating new columns from existing ones)
- Handling missing values (imputation strategies)
- Encoding categorical variables
- Scaling/normalization
- Train/test splitting

```markdown
## Transformation Log
* **Columns Renamed:** [List changes]
  Example: "sepal length (cm) → sepal_length_cm, species (int) → species"

* **Types Corrected:** [List changes]
  Example: "signup_date: object → datetime64, monthly_spend: object → float64"

* **Placeholders Cleaned:** [List changes]
  Example: "Converted -999 in age column to NaN (47 values affected)"

* **Invalid Values Removed:** [List changes]
  Example: "Set 3 rows with negative monthly_spend to NaN"

* **Sources Joined:** [If applicable]
  Example: "Joined customers.csv and transactions.csv on customer_id (left join, 48,327 → 48,327 rows)"

* **Rows After Transform:** [Count]
* **Columns After Transform:** [Count]
```

---

## Step 4: Load (Interim) & Verify

Save the transformed data to `/data/interim/` and verify it's correct.

**Actions:**
- Save to `/data/interim/` with a clear, versioned name.
- Prefer **Parquet** format for interim data (preserves dtypes, compressed, fast to read).
- Verify with `.info()`, `.head()`, `.shape`, and a quick spot-check against raw.

**Naming Convention:**

```
/data/interim/{project_name}_v{version}.parquet

Examples:
/data/interim/churn_prediction_v1.parquet
/data/interim/property_valuation_v1.parquet
/data/interim/customer_segmentation_v1.parquet
```

```markdown
## Interim Dataset
* **File:** [Path]
  Example: "/data/interim/churn_prediction_v1.parquet"

* **Shape:** [Rows × Columns]
  Example: "48,327 rows × 14 columns"

* **Verification:**
  - [ ] `.info()` shows correct dtypes (no unexpected objects)
  - [ ] `.head()` looks reasonable
  - [ ] Row count matches expectation from extraction
  - [ ] Target variable is present and correctly defined
```

---

## Step 5: Document Data Lineage

Maintain a clear record of how data flows from source to interim. This is your reproducibility trail — if anyone (including future-you) needs to understand where the data came from and what happened to it, this table tells the full story.

```markdown
## Data Lineage
| Layer | Source | Destination | Script | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Raw | [Original source] | [/data/raw/ path] | [Script path] | [Untouched source data] |
| Interim | [/data/raw/ path] | [/data/interim/ path] | [Script path] | [What transformations were applied] |

Example:
| Raw | crm_db (PostgreSQL) | /data/raw/2026-03-12_customers.csv | notebooks/01_collection.ipynb | 48,327 rows, untouched |
| Raw | Client email (xlsx) | /data/raw/2026-03-12_transactions.xlsx | notebooks/01_collection.ipynb | As received from client |
| Interim | /data/raw/*.csv + *.xlsx | /data/interim/churn_prediction_v1.parquet | notebooks/01_collection.ipynb | Joined, renamed, types fixed, placeholders cleaned |
```

---

## Step 6: Gap Assessment

Compare what you collected against the [Data Requirements from Stage 3](./03_data_requirements.md). Are there gaps?

**Actions:**
- Cross-reference the Stage 3 field specifications against what's actually in the interim dataset.
- Document any missing fields, insufficient timeframes, or quality issues.
- Decide: proceed with what you have, or go back to the client/source for more data.

```markdown
## Gap Assessment
| Required Field (Stage 3) | Status | Notes |
| :--- | :--- | :--- |
| [Field name] | ✅ Available | [In interim dataset] |
| [Field name] | ⚠️ Partial | [Only 18 months available, 24 months requested] |
| [Field name] | ❌ Missing | [Client does not track this. Will attempt proxy.] |

* **Decision:** [Proceed with gaps / Request additional data / Revise Stage 3 requirements]
```

> 💡 **Freelancer's note:** Gaps are normal. The client said they had 24 months of data but only 18 months exist. A field you expected isn't tracked. Document it, decide whether it's a blocker, and communicate the impact to the client: *"Without field X, we can't build feature Y, which may reduce model performance by approximately Z."*

---

## Checklist

Before moving to [Stage 5: Data Understanding](./05_data_understanding.md), confirm:

- [ ] All sources from Stage 3 have been extracted.
- [ ] Raw data is saved to `/data/raw/` — untouched, dated, write-once.
- [ ] Lightweight transformations are applied (rename, types, placeholders, joins).
- [ ] Interim dataset is saved to `/data/interim/` in Parquet format.
- [ ] Interim dataset is verified (`.info()`, `.head()`, row count, target present).
- [ ] Data lineage is documented (source → raw → interim).
- [ ] Gaps are assessed and communicated to the client if necessary.

---

**Next:** [Data Understanding](./05_data_understanding.md) — Exploring and understanding the collected data.