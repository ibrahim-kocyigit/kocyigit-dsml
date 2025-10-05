# Relationship between MAP, MLE and Regularization

- **Maximum Likelihood Estimation (MLE)** finds the model parameters that maximize the probability of the observed data.

- **Maximum a Posteriori Estimation (MAP)** finds the model parameters that maximize the probability of the observed data *and* the prior probability of the model (incorporates prior beliefs).

- **Regularization** penalizes complex models to prevent overfitting, often by adding a term to the loss function that discourages large coefficients.

## How They Connect

- In model selection, each model generates the data with some probability ($P(\text{data} \mid \text{model})$).
- Simpler models are more likely a priori; complex models are less likely.
- MAP estimation multiplies the likelihood of the data by the prior probability of the model:
  $$
  P(\text{data} \mid \text{model}) \times P(\text{model})
  $$
- In regression, regularization adds a penalty to the loss function, which is equivalent to incorporating a prior on the model parameters.

## Mathematical Connection

- **MLE:** Maximizes $P(\text{data} \mid \text{model})$ (likelihood).
- **MAP:** Maximizes $P(\text{data} \mid \text{model}) \times P(\text{model})$ (likelihood $\times$ prior).
- Taking the logarithm turns products into sums:
  $$
  \log P(\text{data} \mid \text{model}) + \log P(\text{model})
  $$
- In regression, this becomes:
  $$
  \text{Loss} + \text{Regularization term}
  $$

... where the regularization term comes from the log prior.


## Example: Linear Regression with Regularization

- Suppose model coefficients are drawn from a standard normal distribution.
- The likelihood of each coefficient $a_i$ is:
  $$
  \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2} a_i^2}
  $$
- The log prior for all coefficients is $-\frac{1}{2} \sum a_i^2$.
- The log likelihood for the data is $-\frac{1}{2} \sum d_i^2$ (where $d_i$ are residuals).
- Maximizing the sum of log likelihood and log prior is equivalent to minimizing:
  $$
  \sum d_i^2 + \sum a_i^2
  $$

... which is "square loss + regularization term".

## Summary

- **MAP estimation with a Gaussian prior on coefficients leads to L2 regularization (Ridge regression).**
- Maximizing the probability of the model (prior) is the same as minimizing the sum of squares of the coefficients.
- Maximizing the conditional probability of the data given the model is the same as minimizing the square loss.
- Regularization in machine learning is a Bayesian concept: it encodes prior beliefs about model simplicity.

---

**Next:** [Confidence Intervals: Overview](../07_confidence_intervals/01_confidence_intervals--overview.md)