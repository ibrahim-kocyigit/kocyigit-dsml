# Back to "Bayesics"

Let's revisit our popcorn example:

We observed popcorn on the floor and considered three possible scenarios:
- Watching movies (high probability of popcorn)
- Playing board games (medium probability)
- Taking a nap (low probability)

We chose "movies" because it had the highest probability of generating the evidence.

## But There's More to the Story

Suppose now the candidates are:
- Watching movies (high probability of popcorn)
- Popcorn throwing contest (very high probability of popcorn)

A popcorn throwing contest almost guarantees popcorn on the floor, so it seems like the winner.  

But intuitively, watching movies is a much more likely event than a popcorn contest.

## Prior Probability Matters

Even though a contest is more likely to produce popcorn, it's much less likely to happen in general. We should consider both:

1. The probability of the evidence given the scenario: $P(\text{popcorn} \mid \text{scenario})$
- The probability of the scenario itself ($P(\text{scenario})$)

So, we multiply them:

$$
P(\text{popcorn} \mid \text{movies}) \cdot P(\text{movies})
$$

$$
P(\text{popcorn} \mid \text{contest}) \cdot P(\text{contest})
$$

The scenario with the highest product is the most likely overall.

## Connection to Bayes' Rule

This approach resembles Bayes' theorem:

$$
P(A \mid B) \cdot P(B) = P(A \cap B)
$$

We're maximizing the probability that both the evidence and the scenario occur together, not just the conditional probability.

**Key takeaway:**  

>To make better decisions, we have to consider both how likely the evidence is given a scenario and how likely the scenario is in general.

---

**Next:** [Frequentist vs. Bayesian](./08_frequentist_vs_bayesian.md)