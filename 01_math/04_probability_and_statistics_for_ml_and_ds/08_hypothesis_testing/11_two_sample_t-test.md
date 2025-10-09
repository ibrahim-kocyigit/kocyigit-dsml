# Two Sample t-Test

So far, all the hypothesis testing we've done has involved one sample from one population. But what if we want to compare samples from **two different populations**? For example, suppose you want to compare the heights of 18-year-olds in the US and Argentina.

---

## Example: Comparing Two Populations

- **US sample:** 10 heights, sample mean $\bar{x} = 68.442$ inches, sample standard deviation $s_x = 3.113$
- **Argentina sample:** 9 heights, sample mean $\bar{y} = 65.949$ inches, sample standard deviation $s_y = 3.106$

**Goal:** Determine if the population mean height in the US is different from (or greater/less than) that in Argentina.

---

## Hypotheses

You can define three types of hypotheses:

- **Right-tailed:** $H_0: \mu_{US} = \mu_{AR}$, $H_1: \mu_{US} > \mu_{AR}$
- **Left-tailed:** $H_0: \mu_{US} = \mu_{AR}$, $H_1: \mu_{US} < \mu_{AR}$
- **Two-tailed:** $H_0: \mu_{US} = \mu_{AR}$, $H_1: \mu_{US} \neq \mu_{AR}$

Or, equivalently, in terms of the difference: $H_0: \mu_{US} - \mu_{AR} = 0$

---

## Assumptions

- The two samples are independent (no overlap between groups).
- Each measurement is independent within each group.
- Heights in both countries are normally distributed.

---

## The Test Statistic

The difference between the sample means, $\bar{x} - \bar{y}$, is itself a random variable. If both populations are normal, the difference is also normal (if variances are known). When variances are **unknown**, we estimate them with the sample standard deviations.

The test statistic is:

$$
t = \frac{\bar{x} - \bar{y}}{\sqrt{\frac{s_x^2}{n_x} + \frac{s_y^2}{n_y}}}
$$

- $n_x = 10$ (US sample size)
- $n_y = 9$ (Argentina sample size)
- $s_x, s_y$ are the sample standard deviations

This statistic follows a **t-distribution** with degrees of freedom calculated by a somewhat complex formula (software will compute it for you). In this example, the degrees of freedom is approximately **16.8**.

---

## Example Calculation

- $\bar{x} = 68.442$, $s_x = 3.113$, $n_x = 10$
- $\bar{y} = 65.949$, $s_y = 3.106$, $n_y = 9$

**Observed statistic:**

$$
t = \frac{68.442 - 65.949}{\sqrt{\frac{3.113^2}{10} + \frac{3.106^2}{9}}} = 1.7459
$$

---

## Right-Tailed Test

- **Null hypothesis:** $\mu_{US} - \mu_{AR} = 0$
- **Alternative hypothesis:** $\mu_{US} - \mu_{AR} > 0$
- **Significance level:** $\alpha = 0.05$
- **Degrees of freedom:** $\approx 16.8$

**p-value:** Probability under $H_0$ that $t$ is greater than 1.7459  
$p = 0.0495$

**Decision:** $p < 0.05$  
$\rightarrow$ **Reject $H_0$**. There is evidence that the US mean is greater than the Argentina mean.

---

## Two-Tailed Test

- **Null hypothesis:** $\mu_{US} - \mu_{AR} = 0$
- **Alternative hypothesis:** $\mu_{US} - \mu_{AR} \neq 0$

**p-value:** Probability under $H_0$ that $|t|$ is greater than 1.7459  
$p = 0.0991$

**Decision:** $p > 0.05$  
$\rightarrow$ **Do not reject $H_0$**. There is not enough evidence to conclude the means are different.

---

## Summary

- The two-sample t-test allows you to compare the means of two independent groups.
- The test statistic uses the difference in sample means, the sample standard deviations, and the sample sizes.
- The p-value is interpreted as in one-sample tests: compare to $\alpha$ to make your decision.

---

**Next:** [Two Sample Test for Proportions](./12_two_sample_test_for_proportions.md)