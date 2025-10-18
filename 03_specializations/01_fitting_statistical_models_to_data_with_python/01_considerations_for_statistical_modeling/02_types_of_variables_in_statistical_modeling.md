# Types of Variables in Statistical Modeling

## 1. The Intuitive Idea: Assigning Roles to Variables

In basic data analysis, we often classify variables by their format: `categorical` (like gender or region) or `continuous` (like age or blood pressure). When we move into statistical modeling, we introduce a new, more important classification based on the **role** each variable plays in our research question.

Think of it like casting a play:
*   **The Dependent Variable (DV):** This is the main character. It's the phenomenon we are trying to understand, explain, or predict. The entire story (our model) revolves around it.
*   **The Independent Variables (IVs):** These are the supporting actors. They are the factors we believe influence or have a relationship with our main character (the DV).
*   **The Control Variables:** These are like background characters or stage settings. They aren't the focus of our story, but we need to account for them to get a clear and accurate view of the relationship between the main character and the supporting actors.

The research question always dictates which variable gets which role. There is nothing inherent to "age" or "blood pressure" that makes one a DV and the other an IV; it all depends on what you are trying to study.

## 2. The Theoretical Framework: Defining the Roles

Let's formalize these roles.

### Dependent Variable (DV)
*   **Other Names:** Outcome, Response, Endogenous Variable.
*   **Definition:** The variable of primary interest whose variation we want to model.
*   **The Goal:** We specify a probability distribution for the DV (e.g., Normal, Binomial) and model its parameters (like the mean or variance) as a function of the independent variables.
*   **Example:** In the model `Mean Blood Pressure = f(age, BMI, gender)`, **blood pressure** is the dependent variable.

### Independent Variable (IV)
*   **Other Names:** Predictor, Covariate, Regressor, Exogenous Variable.
*   **Definition:** A variable used to predict or explain the distribution of the dependent variable.
*   **The Goal:** To estimate the relationship between the IVs and the DV. The choice of IVs should always be driven by theory and subject-matter knowledge.

A crucial distinction for IVs is how they are collected:
*   **Manipulated IVs (Experiments):** In a randomized experiment, the researcher controls the IV, such as assigning participants to a "treatment" or "control" group. This allows for stronger **causal inference**.
*   **Observed IVs (Observational Studies):** The researcher simply observes and records the value of the IV without intervention (e.g., a person's age or gender). In this case, it's much harder to claim causality; our focus is on describing **associations** or **relationships**.

### Control Variable
*   **Definition:** A special type of IV that is included in the model to adjust for potential **confounding**. A confounder is a third variable that is related to *both* our main IV and our DV, muddying their true relationship.
*   **The Goal:** By including a control variable, we can statistically "hold it constant" to get a clearer, more accurate estimate of the relationship between our primary IV and the DV.
*   **Example:** We want to study the relationship between `gender` (IV) and `blood pressure` (DV). We know that `weight` is related to both gender (males tend to weigh more) and blood pressure. `Weight` is a confounder. By including `weight` in our model as a control variable, we can answer the question: "For a male and a female of the *exact same weight*, what is the difference in their blood pressure?" This isolates the gender effect from the weight effect.

## 3. Practical Considerations for Modeling

### Handling Different Types of Independent Variables
How we incorporate an IV into a model depends on its type:
*   **Continuous IVs (e.g., Age):** We estimate a **functional relationship**. This could be a straight line (linear) or a curve (e.g., the quadratic `age + age^2` relationship from the previous lecture).
*   **Categorical IVs (e.g., Race, Region):** We **compare groups**. The numeric codes used to store these variables (e.g., 1=North, 2=South) are arbitrary and have no mathematical meaning. It is incorrect to plot them like a continuous variable. Instead, the model estimates a separate effect for each category, allowing us to compare the DV's distribution across the groups.

### The Critical Issue of Missing Data
Before fitting any model, you must investigate missing data.

*   **Listwise Deletion:** This is the default behavior in most statistical software (including Python libraries). If a single case (or row) has a missing value on *any* variable included in the model (DV or IV), that **entire case is dropped** from the analysis.
*   **The Danger: Bias.** This can be a huge problem. If the cases that get dropped are systematically different from the ones that are kept, our model's estimates will be biased and may not reflect the true population.
    *   **Example:** Imagine we are modeling income. People with very high or very low incomes might be less likely to report it. Listwise deletion would drop these people, and our model would be fit only on the middle-income group, giving us a completely misleading picture of the overall relationship.
*   **How to Check for Bias:**
    1.  Identify the cases that would be dropped due to missing data.
    2.  On a variable that is fully observed for everyone (e.g., `gender`), compare the distribution between the "dropped" group and the "kept" group.
    3.  If there's a significant difference (e.g., the dropped group is 80% female while the kept group is 50% female), you have evidence of systematic differences, and listwise deletion is likely introducing bias.
*   **Potential Solutions:** If bias is suspected, more advanced techniques like **imputation** (predicting and filling in the missing values) may be necessary.

### What's Next?
The way we collect data has profound implications for how we model it. In the next lecture, we will explore how different **study designs** (e.g., cross-sectional, longitudinal, clustered) affect the properties of our data and require specific modeling choices to ensure our analysis is valid.

---

**Next:** [Study Designs and Their Implications for Modeling](./03_study_designs_and_their_implications_for_modeling.md)