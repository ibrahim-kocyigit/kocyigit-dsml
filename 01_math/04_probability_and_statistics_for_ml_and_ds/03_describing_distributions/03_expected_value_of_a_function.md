# Expected Value of a Function

You have now learned how to find the expected value of a random variable `X`. But what if you're interested in the expected value of a *function* of that variable, like `X²` or `2X - 5`?

Luckily, the process is very similar.

**Rule:** To find the expected value of a function `g(X)`, you calculate a weighted average where you sum the values of `g(x)` multiplied by the probability of `x`.

```math
E[g(X)] = \sum g(x) \cdot P(X=x)
```
<br>

You simply replace `x` with `g(x)` in the original expected value formula.

## Example 1: The Squared Payoff Game

Imagine a game where you roll a fair six-sided die. The payoff you receive is the **square** of the number you roll.

**Question:** What is a fair price to pay to play this game?

To answer this, we need to find the expected payoff, which is the expected value of the random variable $g(X) = X^2$.

* **Possible Outcomes (X):** {1, 2, 3, 4, 5, 6}
* **Probability of each outcome, P(X=x):** 1/6 for each.
* **Payoff for each outcome, g(x) = x²:** {1, 4, 9, 16, 25, 36}

Now, we calculate the weighted average of the **payoffs**:
```math
E[X^2] = (1 \cdot \frac{1}{6}) + (4 \cdot \frac{1}{6}) + (9 \cdot \frac{1}{6}) + (16 \cdot \frac{1}{6}) + (25 \cdot \frac{1}{6}) + (36 \cdot \frac{1}{6})
```
```math
= \frac{1+4+9+16+25+36}{6} = \frac{91}{6} \approx 15.17
```
<br>

The fair price to play this game is approximately 15.17 dollars.

## Example 2: Linearity of Expectation

Let's consider a new game. You roll a die, and your payoff is **twice the number you roll, minus a 5 dollar fee**.

* **The function is:** $g(X) = 2X - 5$
* **The payoffs for rolls 1-6 are:** {-3, -1, 1, 3, 5, 7}

**Question:** What is your average (expected) winning/loss for this game?

We can calculate the expected value of the payoffs directly:
```math
E[2X - 5] = \frac{-3 + (-1) + 1 + 3 + 5 + 7}{6} = \frac{12}{6} = 2
```
<br>

On average, you can expect to win 2 dollars per game.

Notice something interesting when we rearrange the calculation:
```math
E[2X - 5] = \frac{(2 \cdot 1 - 5) + (2 \cdot 2 - 5) + \dots + (2 \cdot 6 - 5)}{6}
```
```math
= \frac{2(1+2+3+4+5+6) - (6 \cdot 5)}{6}
```
```math
= 2 \cdot \left(\frac{1+2+3+4+5+6}{6}\right) - 5
```
```math
= 2 \cdot E[X] - 5
```
<br>

The expected value of the roll of a fair die, `E[X]`, is 3.5. So, $2 \cdot (3.5) - 5 = 7 - 5 = 2$. This gives us the same result.

This reveals a very important property called the **Linearity of Expectation**.

**Rule:** For any random variable `X` and any constants `a` and `b`:  
```math
E[aX + b] = aE[X] + b
```
<br>

This rule is extremely useful as it often allows us to simplify complex expected value calculations.


---

**Next:** [The Sum of Expectations](./04_sum_of_expectations.md)