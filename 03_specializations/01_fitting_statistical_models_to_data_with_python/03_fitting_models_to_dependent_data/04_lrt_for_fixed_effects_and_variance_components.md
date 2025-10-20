# Likelihood Ratio Tests for Fixed Effects and Variance Components

## 1. The Intuitive Idea: Is the More Complicated Model Worth It?

Imagine you have two competing models to explain your data.
*   **The "Full" Model:** A more complex model with all the bells and whistles (predictors and random effects) you think might be important.
*   **The "Reduced" Model:** A simpler, **nested** version of the full model, where some of the bells and whistles have been removed (i.e., their parameters have been set to zero).

The **Likelihood Ratio Test (LRT)** is a formal statistical procedure to answer one simple question: **"Is the full model significantly better at explaining the data than the simpler, reduced model?"**

Think of it like deciding whether to add an expensive feature to a car. The LRT helps you determine if the improvement in performance (how well the model "fits" the data) is statistically significant enough to justify the added complexity (the extra parameters). If removing the feature makes the car run significantly worse, then the feature was important.

## 2. The Theoretical Framework: Comparing Model Likelihoods

The LRT works by comparing the **log-likelihood** values from the two models. The log-likelihood is a measure of how "likely" the observed data is, given the fitted model. For technical reasons, we almost always work with the **-2 log-likelihood** (`-2LL`).

*   A **lower** `-2LL` value indicates a **better** model fit.
*   The full model will *always* have a `-2LL` that is less than or equal to the nested model's `-2LL`.

The **test statistic** for the LRT is the difference between these two values:  

$$
\text{Test Statistic} = (-2LL_{\text{reduced}}) - (-2LL_{\text{full}})
$$

This difference will always be positive. A large difference means that removing the parameters had a big negative impact on the model's fit, suggesting the parameters were important.

We then compare this test statistic to a **chi-square ($\chi^2$) distribution** to get a p-value.

### Testing Fixed Effects
This is the most straightforward application of the LRT.
*   **Goal:** To test if a single predictor or a group of predictors are statistically significant.
*   **Procedure:**
    1.  Fit the **Full Model** with all predictors.
    2.  Fit the **Reduced Model** without the predictor(s) you want to test.
    3.  Calculate the difference in their `-2LL` values.
    4.  Compare this difference to a $\chi^2$ distribution with degrees of freedom (`df`) equal to the number of predictors you removed.

### Testing Variance Components (Random Effects)
This is more complex, especially when testing if a variance is zero. This is a "boundary" hypothesis because a variance cannot be negative.
*   **Goal:** To test if a random effect (like a random intercept or random slope) is necessary.
*   **The Problem:** The standard chi-square distribution is not the correct reference distribution when testing if a variance is zero.
*   **The Solution:** We compare our test statistic to a **mixture of chi-square distributions**. The exact mixture depends on what you are testing.

## 3. Example: Testing for Random Slopes in the ESS Case Study

Let's walk through the example of testing if the random slopes for interviewers are a necessary part of our model.

*   **Research Question:** Is there significant variability in the slopes among interviewers?
*   **Null Hypothesis ($H_0$):** The variance of the random slopes is zero. The random slopes are not needed.
*   **Alternative Hypothesis ($H_A$):** The variance of the random slopes is greater than zero.

#### Step 1: Fit the Full Model (Reference Model)  
This is the model that includes both random intercepts and random slopes for the interviewers. We use **Restricted Maximum Likelihood (REML)** estimation, which is preferred for testing variance components.
*   `-2 REML log-likelihood` = **7143.3**

#### Step 2: Fit the Reduced Model (Nested Model)  
This is a simpler model that only has random intercepts for the interviewers (the random slopes are removed).
*   `-2 REML log-likelihood` = **7166.8**
*   *Observation:* The `-2LL` went up, which means the fit got worse after we removed the random slopes. But is it *significantly* worse?

#### Step 3: Calculate the Test Statistic  

$$
\text{Test Statistic} = 7166.8 - 7143.3 = 23.5
$$

#### Step 4: Calculate the p-value using the Correct Distribution
Because we are testing a variance component against zero, we must use a special mixture of chi-square distributions. For testing a random slope (which involves both a variance and a covariance term), the appropriate reference distribution is a 50/50 mixture of a $\chi^2$ distribution with 1 degree of freedom and a $\chi^2$ distribution with 2 degrees of freedom.

The calculation looks like this:

p_value = 0.5 * P(chi-square(df=1) > 23.5) + 0.5 * P(chi-square(df=2) > 23.5)

The result of this calculation is:
*   `p = 4.57e-06` which is essentially **p < 0.001**.

#### Step 5: Make a Conclusion
The p-value is extremely small. Therefore, we **reject the null hypothesis**.

We have very strong evidence that the variance of the random interviewer slopes is not zero. This confirms that the random slopes are a statistically significant and necessary component of our model. The more complex model is justified.

## 4. Key Takeaways

*   The Likelihood Ratio Test (LRT) is a fundamental tool for comparing nested statistical models.
*   It helps us formally decide whether a set of fixed effects (predictors) or random effects (variance components) significantly improves the model fit.
*   The test statistic is the difference in the `-2 log-likelihood` values between a full and a reduced model.
*   When testing **fixed effects**, we use a standard chi-square distribution.
*   When testing if a **variance component is zero**, we must use a more complex **mixture of chi-square distributions** to get an accurate p-value. 


---

**Next:** [Multilevel Logistic Regression Models](./05_multilevel_logisctic_regression_models.md)