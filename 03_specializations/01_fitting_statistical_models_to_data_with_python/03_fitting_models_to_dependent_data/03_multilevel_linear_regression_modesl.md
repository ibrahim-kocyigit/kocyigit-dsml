# Lecture Notes: Multilevel Linear Regression Models

## 1. The Intuitive Idea: From One Model to Many Names

In the last lesson, we introduced the core idea of multilevel models. It's worth remembering that you'll see this same concept called by many different names across various fields. Don't let it confuse you; they all refer to the same fundamental approach of modeling data that is grouped or clustered.

*   **Mixed-Effects Models:** The most common name in statistics. It's called "mixed" because it includes both **fixed effects** (the average, overall relationships) and **random effects** (the cluster-specific deviations from that average).
*   **Hierarchical Linear Models (HLM):** Common in social sciences, emphasizing the hierarchical, nested structure of the data (e.g., students nested in classrooms, nested in schools).
*   **Random Coefficient / Varying Coefficient Models:** These names highlight the key feature: the model coefficients (intercepts and slopes) are not fixed constants but are allowed to randomly vary across clusters.

For this lesson, we'll focus on how to apply these models to a **continuous outcome variable**, like a test score, a satisfaction rating, or a physical measurement.

## 2. The Theoretical Framework: A Deeper Dive

Let's revisit the combined model equation, but now with a clearer distinction between the fixed and random parts. Our goal is to model a continuous outcome $Y_{ij}$ (for person `i` in cluster `j`).

$$
Y_{ij} = \underbrace{(\gamma_{00} + \gamma_{10}X_{ij})}_\text{Fixed Part} + \underbrace{(u_{0j} + u_{1j}X_{ij} + e_{ij})}_\text{Random Part}
$$

*   **Fixed Part:** This is the average line for the entire population.
    *   $\gamma_{00}$: The average intercept across all clusters.
    *   $\gamma_{10}$: The average slope across all clusters.
    *   These are the **fixed effects**, the constant parameters we want to estimate.

*   **Random Part:** This captures all sources of variability and deviation.
    *   $u_{0j}$: The **random intercept effect** for cluster `j`. (How much does cluster `j`'s intercept differ from the average?)
    *   $u_{1j}$: The **random slope effect** for cluster `j`. (How much does cluster `j`'s slope differ from the average?)
    *   $e_{ij}$: The individual-level error. (The remaining unexplained variance for person `i` within cluster `j`).

### Key Assumptions: Where does the "randomness" come from?

Because the random effects are random variables, we must define their probability distributions.

1.  **Level 1 Errors ($e_{ij}$):** We assume the individual errors are normally distributed with a mean of 0 and a constant variance, $\sigma^2_e$. This is the *within-cluster* variance.
    $$
    e_{ij} \sim N(0, \sigma^2_e)
    $$
2.  **Level 2 Random Effects ($u_j$):** We assume the random effects for the intercept ($u_{0j}$) and slope ($u_{1j}$) are drawn from a **bivariate normal distribution**. This means we're not just defining their individual variances, but also the relationship *between* them.
    $$
    \begin{pmatrix} u_{0j} \\ u_{1j} \end{pmatrix} \sim N \left( \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \mathbf{D} \right)
    $$
    The mean is a vector of zeros, indicating that the "average" cluster has no deviation from the fixed effects. The interesting part is the **variance-covariance matrix, D**:
    $$
    \mathbf{D} = \begin{pmatrix} \sigma^2_{u0} & \sigma_{u01} \\ \sigma_{u01} & \sigma^2_{u1} \end{pmatrix}
    $$
    *   $\sigma^2_{u0}$: The variance of the random intercepts. (How much do the starting points vary across clusters?)
    *   $\sigma^2_{u1}$: The variance of the random slopes. (How much do the relationships/trends vary across clusters?)
    *   $\sigma_{u01}$: The **covariance** between the intercepts and slopes. This is a crucial term. A non-zero covariance means the intercept and slope for a cluster are related. For example, a negative covariance might mean that clusters with higher starting points (intercepts) tend to have flatter growth (slopes).

## 3. The Main Goal: Explaining Between-Cluster Variance

A primary reason for using multilevel models is to see if we can explain *why* some clusters have higher intercepts or steeper slopes than others. We do this by adding cluster-level predictors to the Level 2 equations.

Let's walk through the example from the lecture. Imagine we have a longitudinal study where `j` represents subjects.

**Step 1: Fit a model with random intercepts.**
The Level 2 equation for the intercept is simple:
$$ \beta_{0j} = \gamma_{00} + u_{0j} $$
We fit this model and find the variance of the random intercepts. Let's say the estimated variance is $\hat{\sigma}^2_{u0} = 2.0$. This number represents the total between-subject variability in the intercepts that our model hasn't explained yet.

**Step 2: Add a subject-level predictor.**
Now, let's add a predictor that is specific to the subject, like `Male_j` (where 1=Male, 0=Female), to the Level 2 equation:
$$ \beta_{0j} = \gamma_{00} + \gamma_{01}(\text{Male}_j) + u_{0j} $$
We are testing if gender can help explain some of that variability in intercepts.

**Step 3: Compare the variance.**
After fitting the new model, we look at the new estimate for the random intercept variance. Let's say it has dropped to $\hat{\sigma}^2_{u0} = 1.0$.

**Step 4: Calculate "Proportion of Variance Explained" (PVE).**
The drop in variance means our new predictor is doing some work! We can quantify how much:
$$
\text{PVE} = \frac{(\text{Initial Variance} - \text{Final Variance})}{\text{Initial Variance}} = \frac{(2.0 - 1.0)}{2.0} = 0.50
$$
We can conclude that **"50% of the between-subject variance in the intercepts is explained by gender."** This is a powerful and direct conclusion that standard regression cannot provide.

## 4. Estimation and Hypothesis Testing

*   **Estimation:** The parameters (fixed effects like $\gamma_{00}$ and variance components like $\sigma^2_{u0}$) are estimated using **Maximum Likelihood Estimation (MLE)**. The intuition is simple: MLE finds the parameter values that make the data we actually observed the "most likely" or "most probable."

*   **Hypothesis Testing:** To test if our random effects are necessary, we use a **Likelihood Ratio Test (LRT)**.
    *   **The Question:** Is the model significantly better *with* the random effects than *without* them?
    *   **The Process:** We compare the likelihood value of the full model (with random effects) to a simpler model (e.g., a standard linear regression without them). The LRT tells us if the improvement in model fit is statistically significant, justifying the more complex model. A significant result for a variance component means there is meaningful variation across clusters that should be modeled.

## 5. Case Study: Interviewer Effects in the European Social Survey (ESS)

This example provides a fantastic, real-world application of these concepts.

*   **The Data:** Survey data where `observations` (respondents) are clustered within `interviewers`.
*   **The Research Question:** Do different interviewers influence the responses they collect? Specifically, does the relationship between "trust in police" (predictor) and "perceived helpfulness of others" (outcome) vary from one interviewer to another?
*   **The Model:** A multilevel linear model with random intercepts and random slopes for the interviewers.

### Key Findings
1.  **Fixed Effects (The Average Story):** The analysis found a significant positive relationship. On average, people with higher trust in the police also tend to believe others are more helpful.
2.  **Random Effects (The Interviewer Story):** Both the variance of the random intercepts ($\hat{\sigma}^2_{u0} = 0.696$) and the variance of the random slopes ($\hat{\sigma}^2_{u1} = 0.012$) were found to be statistically significant.
    *   **Interpretation:** This is the crucial finding. It means that interviewers are *not* interchangeable. There is meaningful, non-zero variability among interviewers in both the baseline "helpfulness" scores they record (intercepts) and the strength of the "trust-helpfulness" relationship they find (slopes).

### Model Diagnostics: Finding the "Why"
Good analysis doesn't stop at finding an effect; it investigates it. Diagnostics help us check assumptions and find outliers.

1.  **Level 1 Residuals:** We check if the within-cluster errors are normally distributed and have constant variance.
    *   The QQ plot showed residuals falling on a straight line, suggesting the normality assumption is met.
    {{ Insert screenshot of the QQ plot of residuals here }}
    *   The residuals vs. fitted plot showed no clear pattern (like a funnel), supporting the constant variance assumption.
    {{ Insert screenshot of the residuals vs. fitted values plot here }}

2.  **Level 2 Random Effects (EBLUPs):** We examine the predicted random effects for each interviewer to see if any are outliers.
    *   The QQ plot for the random intercepts showed one interviewer (ID 4976) with an unusually low intercept.
    {{ Insert screenshot of the QQ plot for random intercept EBLUPs here }}
    *   The QQ plot for the random slopes showed another interviewer (ID 7519) with an unusual slope.
    {{ Insert screenshot of the QQ plot for random slope EBLUPs here }}

3.  **Investigating the Outliers:**
    *   **The Outlier Intercept (ID 4976):** A plot of this interviewer's data revealed they collected an unusually large number of low "helpfulness" scores. This could be due to their interviewing style or the specific group they surveyed.
    {{ Insert screenshot of the data plot for interviewer 4976 here }}
    *   **The Outlier Slope (ID 7519):** This was a classic data cleaning issue! A plot of their data showed one extreme data point. It turned out that the value `88`, a code for missing data, was accidentally treated as a real value. This single point artificially flattened the regression line for that interviewer, making their slope an outlier. This highlights the critical importance of descriptive statistics and data cleaning before modeling.
    {{ Insert screenshot of the data plot for interviewer 7519 showing the outlier point here }}

### Conclusions & Next Steps
The variance among interviewers is real, but it needs to be re-evaluated after fixing the data cleaning issue. If the variance remains, it adds uncertainty to our overall estimates. A next step would be to add interviewer-level predictors (like their response rate or attitudes) to the Level 2 model to try and *explain* this variance.