# Lecture Notes: What Do We Mean by Fitting Models to Data?

## 1. The Intuitive Idea: Creating a "Mathematical Recipe" for Data

At its heart, "fitting a model to data" is about creating a simplified, mathematical description—a recipe—that explains the key patterns in our data.

It's crucial to remember the direction: **We fit models *to* data, not data *to* models.**

Think of it like this:
*   **The Data:** A complex, messy, real-world phenomenon we've observed and measured (e.g., the test scores of 200 students).
*   **The Model:** A clean, theoretical framework or equation we propose based on our subject-matter knowledge (e.g., "I believe test performance generally follows a bell curve").
*   **Fitting:** The process of taking our theoretical model and tuning its parameters so that it best represents the real-world data we've collected. We are finding the specific "bell curve" (its center and its spread) that is the most plausible origin for our observed student scores.

### Why Bother Fitting Models?
We do this for three main reasons:
1.  **Estimation:** To estimate the fundamental properties of our data. For example, what is the *average* test performance for all students? How much do scores typically *vary*?
2.  **Inference (Summarizing Relationships):** To understand and make formal statements about how different variables relate to each other. For example, is there a statistically significant relationship between age and test performance?
3.  **Prediction:** To use the patterns we've found to make educated guesses about future or unseen data. For example, given a new student's age, what is their most likely test score?

## 2. The Theoretical Framework: Parametric Modeling

In this course, we focus on **parametric models**. This means we start by making an assumption about the shape of our data's probability distribution, and this distribution is defined by a set of parameters.

The most common example is assuming a variable follows a **Normal Distribution**. A normal distribution is fully defined by two parameters:
*   The mean ($\mu$), which sets its center.
*   The variance ($\sigma^2$), which sets its spread.

When we "fit a normal model" to our data, we are using the data to find the most likely values for $\mu$ and $\sigma^2$. These estimates, denoted $\hat{\mu}$ and $\hat{\sigma}^2$, become our concise summary of the data's distribution.

### Example: Modeling Test Performance

Let's walk through the lecture's example to see these ideas in action.

*   **Research Question:** What is the relationship between a college student's age and their performance on a test?
*   **Theory:** We have a hunch that the relationship is **curvilinear**. Performance is highest for students of an average age and lower for both younger and older students (an "inverted U-shape").
*   **The Data:** 200 observations. `performance` (our outcome) and standardized `age` (our predictor).

Before modeling, we always explore the data visually.

1.  **Distribution of Performance:** A histogram and a Normal Q-Q plot show that the `performance` scores, by themselves, look roughly like a bell curve. This gives us confidence that assuming a Normal distribution is reasonable.
    {{ Insert screenshot of the histogram and Q-Q plot for performance here }}

2.  **Relationship between Age and Performance:** A scatter plot of `performance` vs. `age` visually confirms our theory. We can see the inverted U-shape.
    {{ Insert screenshot of the scatter plot of performance vs. age here }}

### Modeling Approach 1: The Mean-Only Model (Unconditional)

This is the simplest possible model. It ignores all predictors and just aims to describe the overall distribution of the outcome.

**The Model:**
We state that each student's performance score is the overall mean plus some random, individual error.
$$
\text{Performance}_i = M + E_i
$$
**The Parameters:**
1.  $M$: The marginal (overall) mean of test performance.
2.  $\sigma^2$: The variance of the errors ($E_i$), which represents the variance in test performance across all students.

**The Assumption:**
We assume the errors are normally distributed with a mean of 0.
$$
E_i \sim N(0, \sigma^2)
$$
**The Fit:**
After fitting the model, we get estimates:
*   Estimated Mean ($\hat{M}$): 4.57 points.
*   Estimated Variance ($\hat{\sigma}^2$): 1.82.

This model gives us a basic description, but it completely ignores our theory about age.

### Modeling Approach 2: The Quadratic Model (Conditional)

This model incorporates our theory about the curvilinear relationship with age.

**The Model:**
We state that performance is a quadratic function of age, plus some random error. This is a **linear regression model** (it's linear in the *parameters* a, b, and c).
$$
\text{Performance}_i = a + b(\text{age}_i) + c(\text{age}_i^2) + e_i
$$
**The Parameters:**
1.  $a$: The intercept. The predicted performance for a student with average age (since age is standardized, `age=0` is the mean).
2.  $b$: The linear coefficient for age.
3.  $c$: The quadratic coefficient for age. A negative `c` will produce the inverted U-shape we expect.
4.  $\sigma^2$: The variance of the errors ($e_i$). This is now the *conditional* variance—the unexplained variability in performance *after* accounting for age.

**The Assumption:**
$$
e_i \sim N(0, \sigma^2)
$$
**The Fit:**
The software gives us estimates for our parameters:
*   $\hat{a} = 5.11$
*   $\hat{b} = 0.24$
*   $\hat{c} = -0.26$
*   $\hat{\sigma}^2 = 1.29$

Notice that the error variance (1.29) is smaller than in the mean-only model (1.82). This is a good sign! It means our predictor, `age`, has successfully explained a portion of the total variance in test performance.

## 3. The Importance of Assessing Model Fit

Fitting a model is easy; fitting a *good* model is the challenge. We must always check if our model's assumptions hold and if it provides a reasonable description of the data. The primary tool for this is **residual analysis**.

A **residual** is the difference between the observed value and the value predicted by the model.
$$
\text{residual}_i = \text{Observed}_i - \text{Predicted}_i
$$
If our model is good, the residuals should be nothing but random noise, showing no discernible patterns.

### Checking the Fit of the Quadratic Model
1.  **Normality of Residuals:** A Q-Q plot of the residuals shows they fall on a straight line, confirming our assumption that the errors are normally distributed.
    {{ Insert screenshot of the Q-Q plot of residuals for the conditional model here }}

2.  **Constant Variance & Mean of Zero:** We plot the residuals against the predicted values. The plot shows the points are symmetrically scattered around 0 with a consistent vertical spread. This confirms our assumptions of zero mean and constant variance for the errors.
    {{ Insert screenshot of the residuals vs. fitted values plot for the conditional model here }}

### What a Bad Fit Looks Like: The Misspecified Model

Imagine we ignored our theory and fit a simple *linear* model (`Performance = a + b*age`).

1.  **Visual Fit:** The straight line clearly misses the curve in the data.
    {{ Insert screenshot of the scatter plot with the poor linear fit line here }}

2.  **Residual Plot:** The plot of residuals vs. predicted values shows a clear, systematic U-shaped pattern. This is a massive red flag. When your residuals have a pattern, it means your model has failed to capture a key feature of the data (in this case, the curvilinear relationship).
    {{ Insert screenshot of the residuals vs. fitted values plot for the misspecified linear model here }}

This confirms that the quadratic model was a much better choice, and it illustrates why assessing model fit is a critical, non-negotiable step in the modeling process.