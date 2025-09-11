# Sample Variance

Variance measures how spread out your data is—it tells you how far points are from their mean. Let's look at two example datasets of heights (in cm) for five people:

- **smaller_var:** [158, 159, 160.5, 161, 161.5]  
  (points are close to the mean)
- **larger_var:** [151, 154, 159, 166, 170]  
  (points are farther from the mean)

Both datasets have a mean of 160, but their variances are different.

![](./images/0401.png)

## Population Variance

The formula for population variance ($\sigma^2$) is:
$$
\sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2
$$
where $\mu$ is the population mean and $N$ is the population size.

For both datasets, $\mu = 160$.

- **smaller_var:**  
  $\sigma^2 = \frac{(158-160)^2 + (159-160)^2 + (160.5-160)^2 + (161-160)^2 + (161.5-160)^2}{5} = \frac{4 + 1 + 0.25 + 1 + 2.25}{5} = \frac{8.5}{5} = 1.7$
- **larger_var:**  
  $\sigma^2 = \frac{(151-160)^2 + (154-160)^2 + (159-160)^2 + (166-160)^2 + (170-160)^2}{5} = \frac{81 + 36 + 1 + 36 + 100}{5} = \frac{254}{5} = 50.8$

## Estimating Variance from a Sample

In practice, you rarely have access to the whole population. Instead, you estimate variance from a sample.

### Naive Sample Variance

If you use the sample mean and divide by the sample size $n$, you get:
```math
\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2
```
<br>

... where $\bar{x}$ is the sample mean.

However, this estimator is **biased**—it tends to underestimate the true population variance.

### Unbiased Sample Variance

To correct for this bias, divide by $n-1$ instead of $n$:
```math
s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2
```
<br>

This is called the **unbiased sample variance** and is the most common estimator in statistics.

## Why Divide by $n-1$?

Using $n-1$ in the denominator corrects for the bias introduced by using the sample mean instead of the population mean.  
- For small samples, the difference between dividing by $n$ and $n-1$ is significant.
- For large samples, the difference is negligible.

## Example Calculation

Suppose you have three cards labeled 1, 2, and 3. You draw one card at random.

- **Population mean:**  
  $\mu = \frac{1 + 2 + 3}{3} = 2$

- **Population variance:**  
  $\sigma^2 = \frac{(1-2)^2 + (2-2)^2 + (3-2)^2}{3} = \frac{1 + 0 + 1}{3} = \frac{2}{3}$

Now, suppose you draw two cards (with replacement), so $n = 2$.  

Let's look at all possible samples of size 2:

| Sample | Sample Mean | Naive Variance (divide by $n$) | Unbiased Variance (divide by $n-1$) |
|--------|-------------|-------------------------------|-------------------------------------|
| (1,1)  | 1           | 0                             | 0                                   |
| (1,2)  | 1.5         | 0.25                          | 0.5                                 |
| (1,3)  | 2           | 1                             | 2                                   |
| (2,1)  | 1.5         | 0.25                          | 0.5                                 |
| (2,2)  | 2           | 0                             | 0                                   |
| (2,3)  | 2.5         | 0.25                          | 0.5                                 |
| (3,1)  | 2           | 1                             | 2                                   |
| (3,2)  | 2.5         | 0.25                          | 0.5                                 |
| (3,3)  | 3           | 0                             | 0                                   |

Now, average the variances across all samples:

- **Average naive variance (divide by $n$):**  
  $(0 + 0.25 + 1 + 0.25 + 0 + 0.25 + 1 + 0.25 + 0) / 9 = 3 / 9 = 0.33$

- **Average unbiased variance (divide by $n-1$):**  
  $(0 + 0.5 + 2 + 0.5 + 0 + 0.5 + 2 + 0.5 + 0) / 9 = 6 / 9 = 0.67$

The true population variance is $2/3 \approx 0.67$.

This shows that using $n$ in the denominator underestimates the variance, while using $n-1$ gives an unbiased estimate (matches the true value).

## Summary

- Use the population variance formula if you have all data.
- Use the unbiased sample variance ($s^2$) if you only have a sample.
- Dividing by $n-1$ gives a better estimate of the true population variance.

---

**Next:** []()