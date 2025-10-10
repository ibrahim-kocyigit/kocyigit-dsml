# Test for proportions

In the videos, you learned how to perform hypothesis testing for the mean of a Gaussian population. Another very useful example is testing for a population proportion $p$.

Imagine that you have a coin, but you don't know whether it's fair or not. The proportion you are interested in is $p = P(H)$, where $H$ denotes getting heads. A possible set of hypotheses for this problem is:

$$
\begin{align*}
H_0 &: p = 0.5 \quad \text{(the coin is fair)} \\
H_1 &: p \neq 0.5 \quad \text{(the coin is not fair)}
\end{align*}
$$

Imagine you toss the coin $20$ times, and $7$ of those tosses result in heads. Your random sample consists of a single random variable $X$, where $X = $ number of heads in $20$ coin flips. This variable follows a Binomial distribution: $X \sim \mathrm{Binomial}(20, p)$.

A good estimate for the population proportion $p$ is the relative frequency of heads observed in your sample:

$$
\hat{p} = \frac{X}{20}
$$

In this example, $\hat{p} = \frac{7}{20} = 0.35$.

Remember that under certain conditions, the Central Limit Theorem states that  

$$
\hat{p} \sim N\left(p, \sqrt{\frac{p(1-p)}{20}}\right)
$$

or equivalently,  

$$
Z = \frac{\frac{X}{20} - p}{\sqrt{\frac{p(1-p)}{20}}} \sim N(0, 1)
$$

$Z$ will be your test statistic. If $H_0$ is true ($p = 0.5$), then your test statistic becomes  

$$
Z = \frac{\frac{X}{20} - 0.5}{\sqrt{\frac{0.5(1-0.5)}{20}}} = \frac{\frac{X}{20} - 0.5}{0.5/\sqrt{20}} \sim N(0, 1)
$$

Consider a significance level $\alpha = 0.05$. To make a decision, you need to get the p-value for your observed statistic. With the observed sample $x = 7$, the observed statistic is  

$$
z = \frac{\frac{7}{20} - 0.5}{0.5/\sqrt{20}} = -1.3416
$$

The p-value is then the probability that $|Z| > |z|$:  

$$
\text{p-value} = P(|Z| > |z|) = P(|Z| > 1.3416) = 0.1797
$$

![](./images/1001.png)

**Conclusion:** Since the p-value is bigger than the significance level of 0.05, you do not have enough evidence to reject the null hypothesis that $p = 0.5$.

## General Case Formulas

Let:

- $p$ = population proportion of individuals in a particular category (e.g., probability of the coin landing heads)
- $p_0$ = population proportion under the null hypothesis (e.g., $p_0 = 0.5$)
- $x$ = observed number of individuals in the sample from the specified category (e.g., number of heads)
- $n$ = sample size (e.g., number of coin tosses)
- $\hat{p} = \dfrac{x}{n}$ = sample proportion for the observed sample $x$

The test statistic for comparing proportions is:

$$
Z = \frac{\frac{X}{n} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} \sim N(0, 1)
$$

The observed statistic is:

$$
z = \frac{\frac{x}{n} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
$$

Depending on the type of hypothesis, the p-value is calculated differently. For a right-tailed test:

$$
\begin{align*}
H_0 &: p = p_0 \\
H_1 &: p > p_0
\end{align*}
$$

the p-value is:

$$
\text{p-value} = P(Z > z)
$$

![](./images/1002.png)

For a left-tailed test:

$$
\begin{align*}
H_0 &: p = p_0 \\
H_1 &: p < p_0
\end{align*}
$$

the p-value is:

$$
\text{p-value} = P(Z < z)
$$

![](./images/1003.png)

For a two-tailed test:

$$
\begin{align*}
H_0 &: p = p_0 \\
H_1 &: p \neq p_0
\end{align*}
$$

the p-value is:

$$
\text{p-value} = P(|Z| > |z|)
$$

![](./images/1004.png)

## Assumptions and Conditions for Validity

For the results of the test for proportions to be valid, the following conditions must be satisfied:

1. **Independence:** The population size should be at least 20 times larger than the sample size ($N \geq 20n$). This ensures that the sampled observations are independent. However, in experiments like coin tossing, where independence is inherent, this condition can be relaxed.

2. **Binary Outcomes:** Each individual in the population must fall into one of two categories (e.g., "success" or "failure", "heads" or "tails").

3. **Sample Size Adequacy:** The sample size must be large enough for the normal approximation to be valid under the null hypothesis. Specifically:
    - $np_0 > 10$
    - $n(1 - p_0) > 10$

    These conditions ensure that both the expected number of successes and failures are sufficiently large for the Central Limit Theorem to apply.

If these conditions are not met, the results of the hypothesis test may not be reliable.

---

**Next:** [Two Sample t-Test](./11_two_sample_t-test.md)