# Linear Regression: Inference

## 1. The Intuitive Idea: From a Sample Line to a "True" Relationship

In the last lecture, we found the best-fitting line for our sample of 25 people. This gave us an estimated slope of `1.1`. But this is just an estimate from one small sample. If we repeated the study with a different group of 25 people, we'd get a slightly different line and a slightly different slope.

The goal of inference is to use our one sample line to make an educated guess about the **true, underlying regression line** for the *entire population*. This "true" line has its own true intercept and true slope, which we can never know for certain. We represent these unknown population parameters with Greek letters to distinguish them from our sample estimates.

*   **Population (True) Model:** $Y = \beta_0 + \beta_1X + \epsilon$
*   **Sample (Estimated) Model:** $\hat{Y} = b_0 + b_1X$

The central question of inference is: "Is the relationship we observed in our sample strong enough to conclude that a real relationship exists in the population?"

For a linear relationship, this boils down to a single question about the true slope, $\beta_1$: **Is $\beta_1$ different from zero?** If the true slope were zero, the line would be flat, meaning the predictor `X` has no linear relationship with the outcome `Y`.

## 2. The Theoretical Framework: Hypothesis Testing for the Slope

We use a formal hypothesis test to answer this question.

*   **Null Hypothesis ($H_0$):** There is no linear relationship. $\beta_1 = 0$.
*   **Alternative Hypothesis ($H_A$):** There is a linear relationship.
    *   Two-sided: $\beta_1 \neq 0$ (The slope is not zero, could be positive or negative).
    *   One-sided: $\beta_1 > 0$ (We have a theory that the slope is specifically positive).

We use the information from our model's output to conduct this test.

| Coefficient | Estimate ($b_1$) | Std. Error | t-value | p-value |
| :--- | :---: | :---: | :---: | :---: |
| `Height` | 1.10 | 0.67 | 1.65 | 0.112 |

Let's break this down:
1.  **Estimate ($b_1$):** Our sample slope is 1.10. It's not zero, but is it *significantly* not zero?
2.  **Standard Error:** This is our measure of uncertainty. It tells us that sample slopes from studies like ours typically vary from the true slope by about 0.67 on average.
3.  **t-value:** This is our test statistic. It measures how many standard errors our estimate is away from the null hypothesis (0). $t = (1.10 - 0) / 0.67 = 1.65$. Our sample slope is 1.65 standard errors above zero.
4.  **p-value:** This is the probability of observing a sample slope as extreme as 1.10 (or more) if the true slope were actually zero.
    *   The output gives a **two-sided p-value** of `0.112`. This is the probability for $H_A: \beta_1 \neq 0$. Since 0.112 is greater than common significance levels (like 0.05), we would fail to reject the null.
    *   Our research question was about a *positive* relationship, so we use a **one-sided test** ($H_A: \beta_1 > 0$). We simply cut the two-sided p-value in half: $p = 0.112 / 2 = 0.056$.
    *   **Conclusion:** With a p-value of 0.056, the result is "marginally significant." It provides some evidence of a positive relationship, but it's not very strong.

### Confidence Intervals: A Range of Plausible Values
Instead of just a yes/no hypothesis test, a confidence interval gives us a range of plausible values for the true population slope, $\beta_1$.

The 95% confidence interval for the slope is `[-0.2, 2.5]`.
*   **Interpretation:** We are 95% confident that the true population slope lies somewhere between -0.2 and 2.5.
*   **Connection to Hypothesis Test:** Because this interval contains the value 0, we cannot reject the null hypothesis that $\beta_1 = 0$ at the 0.05 significance level (for a two-sided test). This confirms our p-value finding.

## 3. Confidence vs. Prediction Intervals

Our model can provide two types of intervals, and it's crucial to understand the difference.

<img src="./images/0201.png" width="500">

*   **Confidence Interval for the Mean Response (Narrower, Inner Bands):** This is an interval for the **average** Y at a given X.
    *   **Question:** "For *all* adults who are 64 inches tall, what is the plausible range for their *average* cartwheel distance?"
    *   It is narrowest at the mean of X because we have the most data and certainty there.

*   **Prediction Interval for an Individual Response (Wider, Outer Bands):** This is an interval for a **single individual's** Y at a given X.
    *   **Question:** "For *one specific* adult who is 64 inches tall, what is the plausible range for *their* cartwheel distance?"
    *   This is always wider because it's much harder to predict for a single person than it is to predict the average of a group. It must account for both the uncertainty in the regression line *and* the natural random scatter of individuals around that line.

## 4. Checking the Assumptions of the Model

All of our inference (p-values, confidence intervals) is only valid if the underlying assumptions of the linear model are met. We check these assumptions by examining the **residuals**.

The key assumptions (often remembered by the acronym **LINE**) are:
1.  **L**inearity: The underlying relationship between X and Y is linear. (We check this with the initial scatter plot).
2.  **I**ndependence: The errors are independent of each other. (Ensured by study design).
3.  **N**ormality: The errors, $\epsilon$, are normally distributed.
    *   **Check:** A Q-Q plot of the residuals. The points should fall along a straight line.

    <img src="./images/0202.png" width="500">

4.  **E**qual Variance (Homoscedasticity): The errors have a constant variance ($\sigma^2$) at all levels of X.
    *   **Check:** A plot of residuals vs. predicted values (or vs. the X variable). We want to see a random, formless cloud of points with a consistent vertical spread. No funnel shapes or curves.

    <img src="./images/0203.png" width="500">

For our cartwheel data, the assumption checks look reasonable.

## 5. Multiple Regression: Adding More Predictors

We can improve our model by adding more predictors. Let's add a categorical variable: `Completed` (1 if they completed the cartwheel, 0 if not).

**The Model:** $\text{Predicted Distance} = b_0 + b_1(\text{Height}) + b_2(\text{Completed})$

**Interpretation of Coefficients (Crucial Difference):**
When you have multiple predictors, you must interpret each coefficient **while holding the other variables constant.**

*   **$b_1$ (Height):** "Comparing two adults *of the same completion status*, for each one-inch increase in height, we estimate the average cartwheel distance increases by 1.26 inches."
*   **$b_2$ (Completed):** "Comparing two adults *of the same height*, those who completed the cartwheel are estimated to have an average distance that is 6 inches longer than those who did not."

Visually, this creates two parallel regression lines—one for completers and one for non-completers—with the same slope but shifted vertically by the value of $b_2$.

![](./images/0204.png)

**Re-evaluating Height:**
After adjusting for completion status, the p-value for the `Height` coefficient is now `0.085 / 2 = 0.0425` (for a one-sided test). By accounting for some of the other noise in the data (completion status), the signal for the height relationship has become stronger and is now statistically significant at the 0.05 level. This is a common and powerful result of multiple regression.

---

**Next:** [Linear Regression: Further Reading](./03_linear_regression--further_reading.pdf)