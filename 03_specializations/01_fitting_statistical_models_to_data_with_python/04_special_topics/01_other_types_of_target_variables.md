# Other Types of Dependent (Target) Variables

## 1. The Intuitive Idea: Beyond Continuous and Binary Outcomes
So far in this course, we have focused on two main types of dependent variables:

1. **Continuous:** A measurement on a continuous scale (e.g. blood pressure, math achievement score). We use **Linear Regression**.
2. **Binary:** A "Yes/No" or "Success/Failure" outcome (e.g., smoker vs. non-smoker, honors program enrollment). We use **Logistic Regression**.

However, real-world data is much richer and more varied. What if our outcome is a choice between three different brands? Or a ranking on a 1-to-5 scale? Or the number of times an event occurs?

This lecture introduces four common types of dependent variables that go beyond the simple linear/logistic framework. For each type, specialized statistical models are required to properly analyze the data. The key takeaway is that the nature of your dependent variable dictates the type of model you must use.

## 2. A Gallery of Common Dependent Variable Types

### Multinomial Data

* **What it is:** A categorical variable with **more than two unordered categories**.
* **The Question it Answers:** "Which one did they choose?"
* **Examples:**  
    * Which brand of smartphone does a person own (Apple, Samsung, Google, Other)?
    * Which contraceptive method did a woman choose (Pill, IUD, Condom, None)?
    * Which political party did a person vote for?
* **Key feature:**  The categories have no intrinsic order or ranking. Choosing "Apple" is not inherently "higher" or "lower" than choosing "Samsung."
* **Appropriate Models:** Multinomial Logistic Regression.

### Ordinal Data

* **What it is:** A categorical variable with **more than two ordered categories**.
* **The Question it Answers:** "What is the level or rank?"
* **Examples:**  
    * Survey responses on a Likert scale (e.g., "Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree").
    * A patient's condition rated as "Poor", "Fair", "Good", "Excellent".
    * Cancer staging (Stage I, II, III, IV).
* **Key Feature:** The categories have a clear, natural order, but the distance between them is not uniform or known. The "gap" between "Good" and "Excellent" is not necessarily the same as the gap between "Poor" and "Fair".
* **Appropriate Models:** Ordinal Logistic Regression (also known as Proportional Odds Model).

### Count Data

* **What it is:** A variable that represents the number of times an event occurs. It can only take on **non-negative integer values** (0, 1, 2, 3, ...).
* **The Question it Answers:** "How many are there?"
* **Examples:**  
    * The number of steps a person takes in a day.
    * The number of traffic accidents at an intersection in a month.
    * The number of goals scored by a footballer in a season.
* **Key Feature:** The data is discrete and cannot be negative. The distribution of count data is often skewed, with many observations at low values.
* **Appropriate Models:** Poisson Regression, Negative Binomial Regression.

### Time-to-Event Data (Survival Data)
* **What it is:** A variable that measures the **duration until a specific event of interest occurs**.
* **The Question it Answers:** "How long did it last?" or "How long until it happened?"
* **Examples:**  
    * The time from a cancer diagnosis until death.
    * The time until a machine part fails.
    * The time a user remains subscribed to a service before churning.
* **Key Feature:** This data type has a unique challenge called **censoring**. For many subjects, the event may not have occurred by the end of the study (e.g., the patient is still alive, the machine part is still working). Our model must be able to correctly handle this "incomplete" information.
* **Appropriate Models:** Survival Analysis techniques like Kaplan-Meier curves and Cox Proportional Hazards Models.

# 3. Summary
The world of statistical modeling extends far beyond linear and logistic regression. Recognizing the type of your dependent variable is the first and most critical step in choosing an appropriate analysis. Using a standard linear regression model on count data, for example, would be inappropriate and lead to flawed conclusions.

| Data Type | Description | Example | Common Model |
| :--- | :--- | :--- | :--- |
| **Multinomial** | Categorical, >2 unordered groups | Brand Choice | Multinomial Logistic Regression |
| **Ordinal** | Categorical, >2 ordered groups | Survey Scale | Ordinal Logistic Regression |
| **Count** | Non-negative integers | Number of Visits | Poisson Regression |
| **Time-to-Event** | Duration until an event | Time to Failure | Cox Proportional Hazards |

---

**Next:** [Should We Use Survey Weights When Fitting Models?](./02_should_we_use_survey_weights_when_fitting_models.md)