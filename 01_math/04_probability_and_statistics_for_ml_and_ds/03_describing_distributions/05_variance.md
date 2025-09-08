# Variance

In the last lessons, we learned about the expected value (or mean). While the mean tells us a lot about the center of a distribution, it doesn't tell the whole story. Two distributions can have the exact same mean but look completely different.

This difference is captured by a new measure called **variance**, which describes how spread out a distribution is.

### Two Games: Same Mean, Different Spread
Let's consider two different coin-flipping games.

* **Game 1:** You flip a fair coin. Heads, you win 1 dollar. Tails, you lose 1 dollar.
    * The expected value is `E[X₁] = (1 * 0.5) + (-1 * 0.5) = 0`.
* **Game 2:** You flip a fair coin. Heads, you win **100** dollars. Tails, you lose **100** dollars.
    * The expected value is `E[X₂] = (100 * 0.5) + (-100 * 0.5) = 0`.

Both games have the same expected value of 0. On average, you would break even playing either game. However, Game 2 is clearly much riskier. Its outcomes are far more spread out. We need a way to quantify this difference in spread, and that's the job of the variance.

## Calculating Variance

To quantify spread, our first instinct might be to calculate the average **deviation** from the mean, `X - E[X]`. However, because the mean is the balancing point, the positive and negative deviations always cancel out, and the average deviation is always zero.

The standard approach is to use the **squared deviation**, `(X - E[X])²`. This makes all deviations positive and heavily penalizes outcomes that are far from the mean.

**Definition:** The **variance**, denoted as `Var(X)` or `σ²`, is the expected value (or average) of the squared deviation.

> $$ \text{Var}(X) = E[(X - E[X])^2] $$

Let's calculate the variance for our two games:
* **Game 1:** The squared deviations are $(-1-0)^2=1$ and $(1-0)^2=1$.
    * `Var(X₁) = (1 * 0.5) + (1 * 0.5) = 1`

* **Game 2:** The squared deviations are $(-100-0)^2=10000$ and $(100-0)^2=10000$.
    * `Var(X₂) = (10000 * 0.5) + (10000 * 0.5) = 10000`

The variance successfully captures the massive difference in the spread of the two games.

## Alternative Formula for Variance

While the definition above is intuitive, an alternative formula is often easier for calculations:

> $$ \text{Var}(X) = E[X^2] - (E[X])^2 $$
In words: The variance is the expected value of the square of the variable, minus the square of the expected value.

## Properties of Variance

Variance has a very important property related to scaling and shifting a random variable.

**Rule:** For any random variable `X` and any constants `a` and `b`:  

> $$ \text{Var}(aX + b) = a^2\text{Var}(X) $$

Let's break this down:
* **Adding a constant `b` does not change the variance.** Shifting a distribution left or right changes its mean, but it does **not** change its spread.
* **Multiplying by a constant `a` scales the variance by `a²`.** If you double the value of all outcomes, you are also doubling their deviations from the mean. Since variance is based on the *squared* deviation, the total variance increases by a factor of $2^2 = 4$.