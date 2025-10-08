# Confidence Intervals for Proportion

Previously, we learned how to compute confidence intervals for a sample mean (e.g., average height). The formula was:

$$
\text{Confidence Interval} = \bar{x} \pm \text{Margin of Error}
$$

... where:

$$
\text{Margin of Error} = z \times \frac{\sigma}{\sqrt{n}}
$$

But what if we want a confidence interval for a **proportion** instead of a mean?

Suppose you want to estimate the proportion of adults who own a car in Statistopia.  
- You sample $n = 30$ people.
- Out of those, $x = 24$ own a car.

The **sample proportion** ($\hat{p}$) is:

$$
\hat{p} = \frac{x}{n} = \frac{24}{30} = 0.80
$$

## Confidence Interval for a Proportion

The confidence interval for a proportion is similar in form:

$$
\text{Confidence Interval} = \hat{p} \pm \text{Margin of Error}
$$

But the **margin of error** is calculated differently:

$$
\text{Margin of Error} = z \times \sqrt{ \frac{\hat{p}(1 - \hat{p})}{n} }
$$

...where $z$ is the critical value for your confidence level (e.g., 1.96 for 95%).

## Step-by-Step Example

Let's calculate a 95% confidence interval for the car ownership proportion:

- $\hat{p} = 0.80$
- $n = 30$
- $z = 1.96$ (for 95% confidence)

**Calculate the margin of error:**  

$$
\text{Margin of Error} = 1.96 \times \sqrt{ \frac{0.8 \times 0.2}{30} } \approx 1.96 \times \sqrt{0.00533} \approx 1.96 \times 0.073 = 0.14
$$

**Construct the confidence interval:**  

$$
0.80 \pm 0.14 \implies [0.66, 0.94]
$$

## Interpretation

We are 95% confident that the true proportion of adults who own a car in Statistopia is between **66% and 94%**.

## Summary

- For proportions, use:  

$$
\hat{p} \pm z \sqrt{ \frac{\hat{p}(1 - \hat{p})}{n} }
$$

- The main difference from the mean case is in the formula for the standard error.
- The critical value $z$ depends on the desired confidence level.

---

**Next:** [Defining Hypotheses](../08_hypothesis_testing/01_defining_hypotheses.md)