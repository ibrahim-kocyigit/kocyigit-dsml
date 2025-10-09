# Feature Encoding 

## Why Encode Features?

- Many machine learning models require all input features to be numeric.
- Categorical (non-numeric) features must be encoded before modeling.

## Types of Categorical Data

- **Nominal:** Categories with no inherent order (e.g., color: red, blue, green; marital status: married, single).
- **Ordinal:** Categories with a meaningful order (e.g., temperature: cold, warm, hot; rating: low, medium, high).

## Common Encoding Methods

### 1. Binary Encoding

- For variables with only two categories (e.g., yes/no, true/false).
- Encode as 0 and 1.

### 2. One-Hot Encoding

- For nominal variables with more than two categories.
- Creates a new binary column for each category.
- Example:  
  - Original column: `color` (red, blue, green)
  - After one-hot encoding: `red`, `blue`, `green` columns with 0/1 values.

### 3. Ordinal Encoding

- For ordinal variables (ordered categories).
- Assigns integer values to each category (e.g., low=1, medium=2, high=3).
- Be cautious: This assumes equal spacing between categories, which may not always be appropriate.

## Choosing an Encoding Method

- Use **binary or one-hot encoding** for nominal data.
- Use **ordinal encoding** for ordered categories, but consider if the numeric relationship makes sense for your problem.

## Key Takeaways

- Encoding transforms categorical features into numeric values for modeling.
- The choice of encoding depends on whether the data is nominal or ordinal.
- Practice and experimentation will help you decide the best approach for your dataset.

---

**Next:** [Feature Scaling](./07_feature_scaling.md)