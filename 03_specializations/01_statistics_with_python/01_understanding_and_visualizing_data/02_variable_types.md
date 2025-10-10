# Variable Types

The type of variable determines how you can summarize, analyze, and visualize your data.

## Quantitative (Numeric) Variables

- **Definition:** Numeric, measurable quantities where arithmetic operations make sense.
- **Subtypes:**
  - **Continuous:** Can take any value within an interval (e.g., BMI, height, weight, time).
  - **Discrete:** Countable, finite set of values (e.g., number of children in a household).

## Categorical (Qualitative) Variables

- **Definition:** Classifies individuals/items into groups.
- **Subtypes:**
  - **Ordinal:** Categories have a natural order or ranking (e.g., class rank: freshman, sophomore, junior, senior).
  - **Nominal:** No inherent order among categories (e.g., race, marital status).

## Examples from NHANES

| Variable           | Description                        | Type         | Subtype/Notes                                                                 |
|--------------------|------------------------------------|--------------|-------------------------------------------------------------------------------|
| **BMI**            | Height-to-weight ratio (numeric)   | Quantitative | Continuous (average makes sense)                                              |
| **Race**           | Coded as 1–5 for categories        | Categorical  | Nominal (average does not make sense)                                         |
| **Age**            | Age at survey time                 | Quantitative | Discrete (reported as integer), often modeled as continuous (e.g., 8.5 years) |
| **Adult Indicator**| 1 if 18 or older, 0 otherwise      | Categorical  | Nominal (coded as 1/0, could also be A/M)                                     |

## Key Takeaways

- **Quantitative variables:** Continuous or discrete, arithmetic operations are meaningful.
- **Categorical variables:** Ordinal (ordered) or nominal (unordered), arithmetic operations are not meaningful.
- The same real-world concept (e.g., age) can sometimes be represented as different variable types depending on context or coding.

---

**Next:** [Study Design](./03_study_design.md)