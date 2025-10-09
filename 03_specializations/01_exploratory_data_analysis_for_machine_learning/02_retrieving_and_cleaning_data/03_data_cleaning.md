# Data Cleaning

## Why Is Data Cleaning Important?

- **Data-driven decisions:** Analytics and models rely on clean, accurate data.
- **Observations:** Each row (observation) must accurately represent the relationship between features and targets.
- **Labels:** Output variables (labels) must be correct—mislabeling (e.g., in ImageNet) can mislead models.
- **Algorithms:** Models assume data reflects the real world; errors in data lead to unreliable models.
- **Features:** Incorrectly recorded features (e.g., transaction amounts, locations) can disrupt tasks like fraud detection.
- **Model assumptions:** Models hypothesize relationships based on the data provided; messy data leads to unreliable outcomes.

> **Bottom line:** Messy data leads to "garbage-in, garbage-out"—unreliable results and poor model performance.


## Common Data Quality Challenges

- **Lack of data:** Not enough relevant data for modeling; may require collecting or acquiring more data.
- **Too much data:** Data spread across many environments/databases becomes a data engineering challenge.
- **Bad data:** Even with data available, poor quality (errors, inconsistencies) is a major barrier—60% of business leaders cite data quality as a challenge.

> **First step for any ML/AI project:** Ensure data is ready and of high quality.

## What Makes Data Messy?

- **Duplicates:**  
  - Extra copies of observations can overweight certain patterns (e.g., a fraudulent transaction duplicated 200 times).
  - Not all duplicates are bad—sometimes, identical observations are valid (e.g., two identical flowers in the iris dataset).
- **Inconsistent text and typos:**  
  - Spelling errors, extra spaces, inconsistent capitalization can split what should be a single category into many.
- **Missing data:**  
  - Some missingness is inevitable, but too much in key fields can make features unusable.
- **Outliers:**  
  - Extreme values can skew features and make it hard to model true relationships.
- **Data sourcing issues:**  
  - Combining data from multiple systems (on-premises, cloud, different databases) can lead to mismatches and inconsistencies.

## Handling Duplicates

- Investigate whether duplicate observations are valid or should be removed.
- For some datasets (e.g., iris), duplicates may be natural and should be kept.
- For others (e.g., duplicate images), they may add noise and should be removed.
- Always review features and filter data carefully—avoid over-filtering and keep access to original data for reference.

## Summary

- Clean data is the foundation of reliable machine learning.
- Addressing duplicates, inconsistencies, missing data, and outliers is essential before modeling.
- The next step: handling missing values and outliers.

---

**Next:** [Handling Missing Values and Outliers](./04_handling_missing_values_and_outliers.md)