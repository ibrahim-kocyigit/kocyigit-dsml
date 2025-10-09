# Test for proportions

In the videos, you learned how to perform hypothesis testing for the mean of a Gaussian population. Another very useful example is testing for a population proportion $p$.

Imagine that you have a coin, but you don't know whether it's fair or not. The proportion you are interested in is $p = P(H)$, where $H$ denotes getting heads. A possible set of hypotheses for this problem is:

$$
\begin{align*}
H_0 &: p = 0.5 \quad \text{(the coin is fair)} \\
H_1 &: p \neq 0.5 \quad \text{(the coin is not fair)}
\end{align*}
$$

Imagine you toss the coin $20$ times, and $7$ of those tosses result in heads. Your random sample consists of a single random variable $X$, where $X = $ "number of heads in $20$ coin flips". This variable follows a Binomial distribution: $X \sim \mathrm{Binomial}(20, p)$.

A good estimate for the population proportion $p$ is the relative frequency of heads observed in your sample:

$$
\hat{p} = \frac{X}{20}
$$

In this example, $\hat{p} = \frac{7}{20} = 0.35$.



---

**Next:** [Two Sample t-Test](./11_two_sample_t-test.md)