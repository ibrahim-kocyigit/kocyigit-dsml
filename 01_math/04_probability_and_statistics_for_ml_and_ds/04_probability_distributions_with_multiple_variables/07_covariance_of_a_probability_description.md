# Covariance of a Probability Distribution

The expected value and variance tell us a lot about a single random variable, but they don't capture the relationship *between* two variables. Consider three different games:

* **Game 1:** You and a friend play. Either you both win 1 dollar, or you both lose 1 dollar. (Perfectly correlated)
* **Game 2:** If you win 1 dollar, your friend loses 1 dollar, and vice versa. (Perfectly negatively correlated)
* **Game 3:** There are four equally likely outcomes: (Win, Win), (Win, Lose), (Lose, Win), and (Lose, Lose). (Uncorrelated)

If we analyze each player's outcomes separately, we'll find that for all three games, the expected value is 0 and the variance is 1 for both players. These measures fail to tell the games apart. To see the difference, we must look at both players at the same time using **covariance**.

![](./images/0701.png)

## Calculating Covariance for a Distribution

The formula for the covariance of a dataset can be adapted for a probability distribution. It's the weighted average of the product of deviations, where the weights are the probabilities.


```math
\text{Cov}(X, Y) = E[(X - \mu_x)(Y - \mu_y)] = \sum (x_i - \mu_x)(y_i - \mu_y) \cdot P(X=x_i, Y=y_i)
```
<br>

Let's calculate this for our three games. In all cases, $\mu_x = 0$ and $\mu_y = 0$, so the formula simplifies to $E[XY]$.

* **For Game 1:** The possible outcomes are `(1, 1)` and `(-1, -1)`, each with probability 0.5.
```math
\text{Cov}(X, Y) = (1 \cdot 1 \cdot 0.5) + ((-1) \cdot (-1) \cdot 0.5) = 0.5 + 0.5 = 1
```
<br>

* **For Game 2:** The outcomes are `(1, -1)` and `(-1, 1)`, each with probability 0.5.
```math
\text{Cov}(X, Y) = (1 \cdot -1 \cdot 0.5) + ((-1) \cdot 1 \cdot 0.5) = -0.5 + -0.5 = -1
```
<br>

* **For Game 3:** The outcomes are `(1, 1)`, `(1, -1)`, `(-1, 1)`, and `(-1, -1)`, each with probability 0.25.
```math
\text{Cov}(X, Y) = (1 \cdot 1 \cdot 0.25) + (1 \cdot -1 \cdot 0.25) + (-1 \cdot 1 \cdot 0.25) + (-1 \cdot -1 \cdot 0.25)
```
```math
= 0.25 - 0.25 - 0.25 + 0.25 = 0
```


## Alternative Formula

Just like with variance, there is an alternative and often simpler formula for covariance.

```math
\text{Cov}(X, Y) = E[XY] - E[X]E[Y]
```
<br>

Let's apply this to the **call center example** from the previous lesson.
* We calculated the means: $E[X] = 4.903$ and $E[Y] = 5.280$.
* Let's assume we calculate the expected value of the product, $E[XY]$, to be 18.014.

Then the covariance is:
```math
\text{Cov}(X, Y) = 18.014 - (4.903 \cdot 5.280) = 18.014 - 25.888 \approx -7.87
```
<br>

The negative covariance confirms our intuition that as wait time (`X`) increases, customer satisfaction (`Y`) tends to decrease.


---

**Next** []()