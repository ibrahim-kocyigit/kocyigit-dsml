# Maximum Likelihood Estimation for the Gaussian Population

In the last lesson, you got an intuition of what the Maximum Likelihood Estimation (MLE) should look like for the mean and variance of a Gaussian population.  

Here, we derive both results mathematically.

## Mathematical Formulation

Suppose you have $n$ samples $X = (X_1, X_2, \ldots, X_n)$ from a Gaussian distribution with mean $\mu$ and variance $\sigma^2$:

$$
X_i \sim \text{i.i.d. } N(\mu, \sigma^2)
$$

The likelihood for $\mu$ and $\sigma$ given the data $x = (x_1, x_2, \ldots, x_n)$ is:

$$
L(\mu, \sigma; x) = \prod_{i=1}^n f_{X_i}(x_i) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{1}{2} \frac{(x_i - \mu)^2}{\sigma^2}\right)
$$

This simplifies to:

$$
L(\mu, \sigma; x) = \frac{1}{(\sqrt{2\pi})^n \sigma^n} \exp\left(-\frac{1}{2} \frac{\sum_{i=1}^n (x_i - \mu)^2}{\sigma^2}\right)
$$

## Log-Likelihood

Maximizing the likelihood is equivalent to maximizing the log-likelihood:

$$
\ell(\mu, \sigma) = \log(L(\mu, \sigma; x))
$$

Using logarithm properties, we get:

$$
\ell(\mu, \sigma) = -\frac{n}{2}\log(2\pi) - n\log(\sigma) - \frac{1}{2} \frac{\sum_{i=1}^n (x_i - \mu)^2}{\sigma^2}
$$

## Finding the MLE

Take the partial derivatives of the log-likelihood and set them to zero.

### For $\mu$:

$$
\frac{\partial}{\partial \mu} \ell(\mu, \sigma) = \frac{1}{\sigma^2} \left( \sum_{i=1}^n x_i - n\mu \right)
$$

Set to zero:

$$
\sum_{i=1}^n x_i - n\mu = 0 \implies \hat{\mu} = \frac{1}{n} \sum_{i=1}^n x_i = \bar{x}
$$

### For $\sigma$:

$$
\frac{\partial}{\partial \sigma} \ell(\mu, \sigma) = -\frac{n}{\sigma} + \frac{\sum_{i=1}^n (x_i - \mu)^2}{\sigma^3}
$$

Set to zero and substitute $\mu = \hat{\mu}$:

$$
-\frac{n}{\sigma} + \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{\sigma^3} = 0
$$

$$
\implies n\sigma^2 = \sum_{i=1}^n (x_i - \bar{x})^2
$$

$$
\implies \hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2
$$

$$
\implies \hat{\sigma} = \sqrt{ \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 }
$$

**Note:**  The MLE for the standard deviation uses $1/n$ as the normalizing constant, while the unbiased sample standard deviation uses $1/(n-1)$.

## Example

Suppose you have the following 10 measurements (heights of 18-year-olds in the US):

| 66.75 | 70.24 | 67.19 | 67.09 | 63.65 |
|-------|-------|-------|-------|-------|
| 64.64 | 69.81 | 69.79 | 73.52 | 71.74 |

- **MLE for the mean:**

$$
\hat{\mu} = \frac{66.75 + 70.24 + 67.19 + 67.09 + 63.65 + 64.64 + 69.81 + 69.79 + 73.52 + 71.74}{10} = 68.442
$$

- **MLE for the standard deviation:**

$$
\hat{\sigma} = \sqrt{ \frac{1}{10} \left[ (66.75-68.442)^2 + (70.24-68.442)^2 + \ldots + (71.74-68.442)^2 \right] } = 2.954
$$

---

**Next:** [Maximum Likelihood Estimation: Linear Regression](./05_mle--linear_regression.md)