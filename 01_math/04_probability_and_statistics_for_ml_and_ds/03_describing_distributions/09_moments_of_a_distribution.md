# Moments of a Distribution

The **mean** (expected value) and **variance** paint a very good picture of a distribution's center and spread. However, there are more subtle characteristics of a distribution's shape that these two measures don't capture.

To describe these finer details, we use the **moments** of a distribution.

### What are Moments?
You've already seen the first two moments, though we didn't call them that. In general, the **k-th moment** of a random variable `X` is the expected value of `X` raised to the k-th power, `E[Xᵏ]`.

#### First Moment (k=1): $E[X]$
This is simply the **mean** of the distribution. It tells us about the central location.

#### Second Moment (k=2): $E[X^2]$
This is not the variance, but it is directly used to calculate the variance: $\text{Var}(X) = E[X^2] - (E[X])^2$. It is related to the **spread**.

#### Third Moment (k=3): $E[X^3]$
This is used to calculate the **skewness** of a distribution.

#### Fourth Moment (k=4):** $E[X^4]$
This is used to calculate the **kurtosis** of a distribution.

### General Formula (Discrete Case):
The k-th moment is the weighted average of each outcome raised to the k-th power:
```math
E[X^k] = \sum x_i^k \cdot P(X=x_i)
```
<br>

In this lesson, we will focus on what the third and fourth moments tell us about a distribution's shape.