# Logistic Regression: Inference

## 1. The Intuitive Idea: Is the Relationship Real?

In the last lecture, we fit a logistic regression model and found a relationship between age and the probability of completing a cartwheel in our sample of 25 people. Our model produced an S-shaped curve suggesting that, in our sample, the probability of success changes with age.

<img src="./images/0603.png" width="500">

But the critical question remains: Is this relationship real, or could it just be due to random chance in our small sample? If we took a different sample of 25 people, we might get a different curve.

The goal of **inference** is to use our sample data to make a conclusion about the **true, underlying relationship in the entire population**. Specifically, we want to answer the question: "Is there a statistically significant relationship between age and the log-odds of completing a cartwheel in the population?" This boils down to testing if the true population slope, $\beta_1$, is different from zero.

## 2. The Theoretical Framework: Inference for the Slope

Just as with linear regression, we use confidence intervals and hypothesis tests to make inferences about the slope parameter. The mechanics are very similar, with one minor difference: we use a Z-distribution instead of a t-distribution because the theory for these models relies on large sample properties.

We'll use the output from our statistical software to get the key numbers we need.

<img src="./images/0701.png" width="500">

### Confidence Interval for the Slope ($\beta_1$)
A confidence interval gives us a range of plausible values for the true population slope.

**The Formula:**  

$$
\text{CI} = \text{Best Estimate} \pm (\text{Critical Value} \times \text{Standard Error})
$$

$$
\text{CI} = b_1 \pm (z^* \times SE(b_1))
$$

**The Numbers (from the output):**
*   Sample slope ($b_1$): `0.2096`
*   Standard Error $SE(b_1)$: `0.171`
*   Critical Value $z^*$: For a 95% confidence interval, $z^*$ is `1.96`.

**The Calculation:**  

$$
\text{95 CI} = 0.2096 \pm (1.96 \times 0.171)
$$

$$
\text{95 CI} = 0.2096 \pm 0.335
$$

$$
\text{95 CI} = [-0.126, 0.545]
$$

This matches the interval provided directly in the software output.

**The Interpretation:** We are 95% confident that the true population slope for the effect of age on the log-odds of cartwheel completion is somewhere between -0.126 and 0.545.

### Hypothesis Testing for the Slope ($\beta_1$)
A hypothesis test gives us a formal "yes" or "no" answer to whether the slope is significantly different from zero.

**The Hypotheses:**
*   **Null Hypothesis ($H_0$):** There is no linear relationship between age and the log-odds of success. The true slope is zero. ($\beta_1 = 0$)
*   **Alternative Hypothesis ($H_A$):** There *is* a linear relationship. The true slope is not zero. ($\beta_1 \neq 0$)

**The Test Statistic (Z-statistic):**
This measures how many standard errors our sample slope is from the null value of 0.  

$$
Z = \frac{b_1 - 0}{SE(b_1)}
$$

**The Calculation:**  

$$
Z = \frac{0.2096}{0.171} \approx 1.225
$$

This also matches the `z` value in our output.

**The P-value:**
The p-value is the probability of observing a sample slope as extreme as ours (or more extreme) if the null hypothesis were true. The output gives us:
*   `p = 0.221`

**The Decision:**
We compare our p-value to a chosen significance level (alpha), typically $\alpha = 0.05$.
*   Since $0.221 > 0.05$, we **fail to reject the null hypothesis**.

**The Conclusion:** We do not have sufficient statistical evidence to conclude that there is a significant relationship between age and the probability of successfully completing a cartwheel in the population.

## 3. Connecting the Confidence Interval and the Hypothesis Test

The confidence interval and the hypothesis test are two sides of the same coin. They should always lead to the same conclusion.

*   Our 95% confidence interval is `[-0.126, 0.545]`.
*   Does this interval contain the null hypothesis value of 0? **Yes, it does.**
*   Because 0 is considered a plausible value for the true slope based on our confidence interval, we cannot reject the null hypothesis at the $\alpha = 0.05$ level.

This confirms the result of our hypothesis test perfectly.

## 4. Key Takeaways

*   Logistic regression is used for binary outcomes (Success/Failure, Yes/No).
*   It models the **log-odds** of success as a linear function of the predictors.
*   Inference for logistic regression (confidence intervals and hypothesis tests) follows the same logic and structure as linear regression, but uses the Z-distribution.
*   The goal is to determine if the relationship observed in the sample is strong enough to make a claim about the population.
*   In our cartwheel example, despite seeing a trend in our sample, the relationship was not statistically significant, meaning we cannot conclude that age is a reliable predictor of cartwheel success in the broader population based on this data.


---

**Next:** [Logistic Regression: Further Reading](./08_logictic_regression--further_reading.pdf)