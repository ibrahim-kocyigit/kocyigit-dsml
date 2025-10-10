# Data Management and Manipulation

## What is Data Management?

- Data management includes all steps of data processing after collection but before analysis.
- Most statistical software works with **rectangular arrays** (tables): rows = cases, columns = variables.

## Example: Rectangular Data Set

| ID     | Age | State | Expenditures |
|--------|-----|-------|--------------|
| 132414 | 33  | OK    | 375          |
| 454543 | 25  | LA    | 1450         |
| ...    | ... | ...   | ...          |

- Each row is a case (e.g., a person), each column is a variable.

## Best Practices for Data Management

- **Never modify source data files**; always preserve the original data.
- **Write scripts** (e.g., in Python) to generate analysis files from source data.
  - Makes updates and reproducibility easier.
- **Use clear, interpretable variable names.**
  - Avoid names that are too short or too long.
  - Use only letters, numbers (not as the first character), and underscores.
  - Avoid whitespace in variable names (e.g., use `birth_date` instead of `birth date`).
- **Missing values:** Most software recognizes blank, `NA`, or `.` as missing.

## Working with Spreadsheet Software

- Good for quick data overviews, but limited for advanced management/analysis.
- Formatting (font, color) is ignored by statistical software.
- Each sheet is usually imported as a separate dataset.
- Python can read Excel files, but text/CSV is preferred for exchange and archiving.

## Databases and Other Tools

- **Databases (e.g., SQL):** Useful for large-scale data management.
- **Open-source binary formats:** HDF5, Apache Parquet, Apache Arrow — faster and more efficient than text/CSV.
- **Big data tools:** Hadoop, Spark for very large datasets.

## Data Files for Storage and Exchange

- **Text/CSV:** Most universal format; data is delimited by comma or tab.
- **Compression:** Large datasets can be compressed (e.g., gzip) for faster reading and reduced storage.
- **Proprietary formats:** (e.g., SAS7BDAT, DTA) can sometimes be read by Python/Pandas.
- **XML/JSON:** Useful for non-rectangular data, but larger and slower to process.

## Repeated Measures Data: Wide vs. Long Format

- **Repeated measures:** Multiple measurements per subject.
- **Wide format:** One row per subject, columns for each measurement.
- **Long format:** One row per measurement, includes subject ID and measurement time.

### Example: Wide Format

| ID | Birth_state | BMI_25 | BMI_30 | BMI_40 |
|----|-------------|--------|--------|--------|
| 1  | OK          | 26     | 26     | 27     |
| 2  | MI          | 23     | 22     | 28     |

### Example: Long Format

| ID | Birth_state | Age | BMI |
|----|-------------|-----|-----|
| 1  | OK          | 25  | 26  |
| 1  | OK          | 30  | 26  |
| 1  | OK          | 40  | 27  |
| 2  | MI          | 25  | 23  |
| 2  | MI          | 30  | 22  |
| 2  | MI          | 40  | 28  |

- **Wide format:** Easier for data entry when all subjects have the same number of measurements.
- **Long format:** More flexible and better for many statistical analyses (e.g., regression).

## Specialized Data Formats

- Other layouts exist for graphs (networks), images, geospatial data, or text data.

---

**Next:** []()