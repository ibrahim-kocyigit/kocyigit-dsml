# Independence

In this lesson, we're going to look at the concept of **independence**.

Two events are **independent** if the occurrence of one event does not affect the probability of the occurrence of the other.

* **Independent Events (Example):** Tossing a coin twice. The result of the first toss has no impact on the result of the second toss.
* **Dependent Events (Example):** Playing a game of chess. The state of the board after the 10th move directly affects all possible outcomes of the 11th move.

Assuming independence, when it is appropriate, is very important in machine learning because it allows us to simplify complex probability calculations.

## The Product Rule for Independent Events

Let's build the intuition for the main rule of independent events.

**Scenario:** A school has 100 kids. 40 of them like to play soccer, and 60 do not. The kids are randomly assigned to two rooms. Room 1 has 30 kids, and Room 2 has 70 kids.

* The probability of a random kid liking soccer is `P(Soccer) = 40 / 100 = 0.4`.
* The probability of a random kid being in Room 1 is `P(Room 1) = 30 / 100 = 0.3`.

**Question:** What is the probability that a randomly selected kid both **likes soccer AND is in Room 1**?

Since the room assignment is random, a kid's preference for soccer has no bearing on which room they are in. The two events are **independent**. Therefore, we would expect the 40% proportion of soccer-liking kids to hold true within Room 1.

The number of kids in Room 1 who like soccer would be 40% of the 30 kids in that room:
`0.40 * 30 = 12 kids`

This means that 12 out of the total 100 kids are in Room 1 and like soccer. The probability is `12 / 100 = 0.12`.

Notice that we could have gotten the same result by simply multiplying the individual probabilities:
`P(Soccer) * P(Room 1) = 0.4 * 0.3 = 0.12`

This leads us to the **Product Rule for Independent Events**.

> $$ P(A \cap B) = P(A) \cdot P(B) $$

## Applying the Product Rule

### Example 1: Five Coin Flips
**Question:** What is the probability of tossing a fair coin five times and getting heads all five times?

Each coin flip is an independent event. The probability of getting heads on any single flip is `P(Heads) = 0.5`.

Using the product rule, the probability of getting five heads in a row is:
```math
P(HHHHH) = P(H) \cdot P(H) \cdot P(H) \cdot P(H) \cdot P(H)
```
```math
= (0.5)^5 = \frac{1}{32} = 0.03125
```

### Example 2: Rolling Two Dice
**Question:** What is the probability of rolling two dice and getting `(6, 6)`?

The outcome of the first die is independent of the outcome of the second.
* The probability of the first die being a 6 is `P(Die 1 = 6) = 1/6`.
* The probability of the second die being a 6 is `P(Die 2 = 6) = 1/6`.

Using the product rule:
$$ P(\text{6 and 6}) = P(\text{Die 1 = 6}) \cdot P(\text{Die 2 = 6}) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36} $$
This matches the result we found by counting the outcomes in the 36-cell sample space.