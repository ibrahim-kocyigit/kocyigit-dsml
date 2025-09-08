# The Bernoulli Distribution

Let's look at the simplest possible case of Binomial distribution: a single trial. This is known as a **Bernoulli trial**, and its distribution is the **Bernoulli Distribution**.

A Bernoulli trial is any experiment that has exactly two possible outcomes: **"success"** or **"failure"**. Therefore, the Binomial distribution with `n=1` trial is, by definition, the Bernoulli distribution:

* **Flipping a coin once:** "Heads" can be success, "Tails" can be failure.
* **Rolling a die once:** "Rolling a 1" can be success, "rolling anything else" can be failure.
* **Medical testing:** A patient can be "sick" (success) or "healthy" (failure).

The Bernoulli distribution is described by a single parameter, **p**, which is the probability of success.

## The Bernoulli PMF

Let's define a random variable `X` for a Bernoulli trial.
* `X = 1` if the outcome is a success.
* `X = 0` if the outcome is a failure.

The Probability Mass Function (PMF) is very simple:
* **P(X = 1) = p**
* **P(X = 0) = 1 - p**

This is the fundamental building block. A **Binomial distribution** simply describes the outcome of performing *n* independent Bernoulli trials.