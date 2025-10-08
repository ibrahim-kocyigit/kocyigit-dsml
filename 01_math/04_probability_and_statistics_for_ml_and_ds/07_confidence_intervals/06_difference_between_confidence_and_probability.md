# Difference Between Confidence and Probability

When you compute a sample estimate ($\bar{x}$) and calculate a 95% confidence interval, it is correct to say: **"The confidence interval contains the true population parameter 95% of the time (in repeated sampling)."**

It is **incorrect** to say: **"There is a 95% probability that the population parameter falls within the confidence interval."**

## Why Is This?

The population parameter (e.g., $\mu$) is **fixed but unknown**.  
- It does **not** have a probability distribution; it is not random.
- For a given population, $\mu$ is always the same value.
- For any specific interval, $\mu$ is either in the interval or not—there is no probability involved.

The **sample mean** ($\bar{x}$), on the other hand, **does** have a probability distribution.
- The value of $\bar{x}$ changes depending on the sample taken.
- The confidence interval is constructed around $\bar{x}$, and its location changes with each sample.

## The Meaning of Confidence

The **confidence level** (e.g., 95%) refers to the **long-run success rate** of the method:
- If you repeated the sampling process many times and constructed a confidence interval from each sample, about 95% of those intervals would contain the true mean.
- The confidence is about the process, not about any single interval.

For any specific interval you construct, the population mean is either inside it or not—there is no probability attached to this fact.

## Summary

- **Confidence** refers to the reliability of the interval construction method over many samples.
- **Probability** does **not** apply to the fixed population parameter being in a specific interval.

---

**Next:** [Unknown Standard Deviation](./07_unknown_standard_deviation.md)