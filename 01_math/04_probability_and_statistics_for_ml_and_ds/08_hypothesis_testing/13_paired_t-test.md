# Paired t-test

- Used when comparing two related (paired) groups, not independent groups.
- Example: Measuring the same subjects before and after a treatment (e.g., weight before and after a training program).

## How It Works

1. **Pair the Data:** Each subject has two measurements (e.g., before and after).
2. **Calculate Differences:** For each pair, compute the difference $D_i = X_i - Y_i$.
3. **Analyze the Differences:** The test focuses on the mean of these differences ( $\bar{D}$ ).

## Test Statistic

- If the original measurements are from a normal distribution, the differences $D$ are also normally distributed.
- The sample mean of the differences ($\bar{D}$) is used.
- Since the population standard deviation is unknown, use the sample standard deviation.
- The test statistic is:  

$$
t = \frac{\bar{D}}{s_D / \sqrt{n}}
$$

... where $s_D$ is the sample standard deviation of the differences, and $n$ is the number of pairs.
- The statistic follows a t-distribution with $n-1$ degrees of freedom.

## Hypotheses

- **Null hypothesis ($H_0$):** The mean difference is zero ($\mu_D = 0$), i.e., no effect.
- **Alternative hypothesis ($H_1$):** The mean difference is not zero (can be one-sided or two-sided).

## Example

- 10 participants measured before and after a training program.
- Compute differences for each participant.
- Suppose:
  - Sample mean of differences ($\bar{D}$) = 1.09
  - Sample standard deviation ($s_D$) = 1.485
  - Test statistic ($t$) = 2.321
- For a right-tailed test ($H_1: \mu_D > 0$), with significance level $\alpha = 0.05$:
  - p-value = 0.0227
  - Since p-value $<$ 0.05, reject $H_0$: conclude the training program is effective for weight loss.

## Key Insight

- The paired t-test reduces to a one-sample t-test on the differences.
- All results for the one-sample t-test apply here.

---

**Next:** [ML Application: A/B Testing](./14_ml_application--a-b_testing.md)