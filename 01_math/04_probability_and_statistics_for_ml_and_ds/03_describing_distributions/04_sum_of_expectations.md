# The Sum of Expectations

A simple but powerful property of expected values is that they add together. This is known as the **Linearity of Expectation**.

**The Sum Rule:** For any two random variables `X` and `Y`, the expected value of their sum is the sum of their individual expected values:
```math
E[X + Y] = E[X] + E[Y]
```
<br>

This rule is incredibly powerful because it is **always true**, regardless of the distributions of the variables and whether they are independent or dependent.

**A Simple Example: A Two-Part Game**
Imagine a game where you first flip a coin and win 1 dollar for heads (0 for tails), and then you roll a die and win the amount shown. What is your total expected winning?

* **Game 1 (Coin):** `X_coin`. The expected value is `E[X_coin] = (1 * 0.5) + (0 * 0.5) = 0.5` dollars.
* **Game 2 (Die):** `X_die`. The expected value is `E[X_die] = (1+2+3+4+5+6)/6 = 3.5` dollars.

Using the sum rule, your total expected winning is:
```math
E[X_{total}] = E[X_{coin}] + E[X_{die}] = 0.5 + 3.5 = 4 \text{ dollars}
```
<br>

## A Non-Trivial Example: The Name Matching Problem

The sum rule can help us solve very difficult problems in a simple way.

**The Problem:** Imagine you have a bag with the unique names of all 8 billion people in the world. You randomly hand one name back to each person. What is the **expected number of people** who will receive their own name correctly?

The answer, believe it or not, is **1**. Let's see why.

## Solving the Problem for 3 People

Let's simplify the problem to just three people: Aisha, Beto, and Cameron. There are $3! = 6$ possible ways to hand out the names.

| Assignment (Aisha, Beto, Cameron) | Aisha gets... | Beto gets... | Cameron gets... | **Number of Matches** |
| :--- | :--- | :--- | :--- | :---: |
| 1 | **Aisha** | **Beto** | **Cameron** | **3** |
| 2 | **Aisha** | Cameron | Beto | **1** |
| 3 | Beto | Aisha | **Cameron** | **1** |
| 4 | Beto | Cameron | Aisha | **0** |
| 5 | Cameron | Aisha | Beto | **0** |
| 6 | Cameron | **Beto** | Aisha | **1** |

The possible number of matches are {3, 1, 1, 0, 0, 1}. The expected (average) number of matches is:
```math
E[\text{Matches}] = \frac{3+1+1+0+0+1}{6} = \frac{6}{6} = 1
```
<br>

This direct calculation works, but it would be impossible for 8 billion people.

## The Simpler Way: Using the Sum of Expectations

Let `Matches` be the random variable for the total number of correct assignments. We can break this down.

Let `A` be a random variable that is 1 if Aisha gets her name right, and 0 otherwise.
Let `B` be a random variable that is 1 if Beto gets his name right, and 0 otherwise.
Let `C` be a random variable that is 1 if Cameron gets his name right, and 0 otherwise.

The total number of matches is simply: `Matches = A + B + C`.

Now, we can use the sum rule:
```math
E[\text{Matches}] = E[A] + E[B] + E[C]
```
<br>

What is the expected value for Aisha, `E[A]`?
* Aisha has a 1/3 chance of getting her name right (`A=1`) and a 2/3 chance of getting it wrong (`A=0`).
```math
E[A] = (1 \cdot \frac{1}{3}) + (0 \cdot \frac{2}{3}) = \frac{1}{3}
```
<br>

The same logic applies to Beto and Cameron: $E[B] = 1/3$ and $E[C] = 1/3$.

Therefore, the total expected number of matches is:
```math
E[\text{Matches}] = \frac{1}{3} + \frac{1}{3} + \frac{1}{3} = 1
```
<br>

## Scaling Up to 8 Billion People

This technique scales perfectly. For `n` people, the total number of matches is the sum of the match variables for each person: `Matches = P₁ + P₂ + ... + Pₙ`.

The probability of any single person getting their name right is `1/n`. Therefore, the expected number of matches for any single person is also `1/n`.

Using the sum rule:
```math
E[\text{Matches}] = E[P_1] + E[P_2] + \dots + E[P_n]
```
```math
= \underbrace{\frac{1}{n} + \frac{1}{n} + \dots + \frac{1}{n}}_{n \text{ times}} = n \cdot \frac{1}{n} = 1
```
<br>

This is why the expected number of matches is always 1, no matter how many people there are.