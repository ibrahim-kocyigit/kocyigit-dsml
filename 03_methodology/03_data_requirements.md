# Stage 3: Data Requirements
_"The chosen analytic approach determines the data requirements. Specifically, the analytic methods to be used require certain data content, formats and representations, guided by domain knowledge."_ - **John B. Rollins**

## Step 1: Identify Required Data Content
Based on the chosen analytic approach (from Stage 2), list the *specific* data elements (variables/features) required to build the model. What information is needed for each input and for the target variable (if applicable)? Be as precise as possible.

## Step 2: Determine Data Formats and Representations
Specify the required data types (e.g., numerical, categorical, text, date/time) and formats (e.g., CSV, JSON, database tables) for each data element. Consider any specific representations needed (e.g., one-hot encoding for categorical variables, specific date/time formats).

## Step 3: Define Data Sources
Identify the potential sources for each required data element. Where does this data reside? Is it in internal databases, external APIs, flat files, or other systems?

## Step 4: Assess Data Availability and Accessibility
For each data source, assess its availability and accessibility. Is the data readily available, or will it require special requests or approvals? Are there any known limitations or restrictions on accessing the data?

## Step 5: Document Data Requirements and Gaps
Document the data requirements, including content, formats, sources, and availability. Identify any potential gaps between the required data and the available data.

---

### Files to Create

1.  `reports/03_data_requirements.md`: This Markdown file will contain the detailed data requirements, including the list of required data elements, their formats and representations, potential sources, availability assessment, and identified data gaps.
2.  `references/`: If there are any existing data dictionaries, schemas, or documentation related to the identified data sources, place them here.