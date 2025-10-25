# Other Types of Dependent (Target) Variables

## 1. Multinomial Data
Multinomial dependent data refers to situations where the outcome variable (dependent variable) can take on more than two distinct, unordered categories. Unlike binary data (where outcomes are limited to two possibilities), multinomial data can capture more complex categorical scenarios. Common examples include survey responses with multiple answer choices, types of medical treatments chosen, or, as in the example you mentioned, the type of contraceptive method used by women.

### Key Features of Multinomial Data
- **Categorical Outcomes:** The dependent variable consists of more than two categories, such as “pill,” “IUD,” “sterilization,” etc.
- **Unordered Categories:** The categories do not have a natural order (contrast with ordinal data).
- **Count or Frequency Data:** You may model the counts of cases in each category or the probabilities of falling into each category.

### Analysis Approaches

There are several statistical methods for analyzing multinomial dependent data:

1. **Multinomial Logistic Regression:**  
   - The most common modeling approach, which generalizes logistic regression to cases where the outcome has more than two categories.
   - The model estimates the probability of the outcome being in each category, given a set of predictor variables.
   - One category is chosen as a reference, and the model compares the log-odds of each other category to this reference.

2. **Chi-Square Tests:**  
   - Used for simple analysis when you want to test if the distribution of counts in categories differs by groups or predictors.
   - Useful for contingency tables involving multinomial outcomes.

3. **Latent Class Analysis:**  
   - Identifies subgroups within the data based on patterns of responses in multinomial variables.

4. **Generalized Linear Models (GLMs):**  
   - The multinomial logistic regression is a type of GLM for categorical data.

### Example: Contraceptive Method Choice

In section 6.1.1 (as you referenced), the authors present a dataset where the dependent variable is the type of contraceptive chosen by women. Each woman’s choice falls into one of several categories (e.g., pill, IUD, sterilization, none), and predictors might include age, education, number of children, etc. Analyzing such data with multinomial logistic regression allows researchers to understand how these predictors influence the probability of choosing each contraceptive method.

### Practical Considerations

- **Interpretation:** Coefficients from multinomial logistic regression represent the change in log-odds of choosing a category (relative to the reference) for a unit change in the predictor.
- **Model Fitting:** Multinomial models require sufficient sample size in each category for reliable estimation.
- **Software:** Most statistical software (R, Python’s statsmodels, SAS, SPSS) provide functions for multinomial regression.

---

**In summary:**  
Multinomial dependent data expands categorical analysis beyond two categories, allowing researchers to model and interpret complex choices or outcomes. Multinomial logistic regression is the primary method for analysis, providing insights into how predictors influence category selection.

If you need code examples or more specific details on analysis techniques, let me know!

## 2. Ordinal Data
Ordinal data is categorical data where there is natural order of categories, but the distance between categories is unknown:  [Further Reading](https://stats.oarc.ucla.edu/other/mult-pkg/whatstat/what-is-the-difference-between-categorical-ordinal-and-interval-variables/).

## 3. Count Data
Count data are data that take on the values of non-negative integers (0, 1, 2, ...). Examples of count dependent variables can be the number of steps a person takes in a day, number of deaths in a country in a given year, or the number of goals scored by a footballer. [This resource](https://stats.idre.ucla.edu/stata/seminars/regression-models-with-count-data/) shows some examples of count dependent variables and methods for analyzing it.

## 4. Time-to-Event Data
Time-to-event data describes how long it takes for an event occur. One of the most common examples is time until death being used as an outcome to assess the effectiveness of a new therapy or treatment. [This resource](https://www.sciencedirect.com/science/article/pii/S1556086421021146#:~:text=Time%2Dto%2Devent%20data%E2%80%94,experience%20the%20event%20of%20interest.) gives an overview of time-to-event data with examples.

---

**Next:** [Should We Use Survey Weights When Fitting Models?](./02_should_we_use_survey_weights_when_fitting_models.md)