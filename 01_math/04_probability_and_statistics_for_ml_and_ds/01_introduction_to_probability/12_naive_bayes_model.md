# Bayes' Theorem - The Naive Bayes Model

In the previous lesson, we used Bayes' theorem to build a simple spam filter based on the presence of a single word, "lottery." But what happens when we want to use multiple words, like "lottery" and "winning," to make a better prediction?

The direct approach would be to calculate:
```math
P(\text{Spam} | \text{"lottery" AND "winning"})
```
<br>

To do this, we would need to find the number of spam emails that contain *both* words and the total number of emails that contain *both* words. For 100 words, we might not have any emails in our dataset that contain all 100, making this calculation impossible.

This is where the **Naive Bayes** model comes in. It solves this problem by making a "naive," but very powerful, assumption.

## The Naive Assumption: Feature Independence

The core idea of the Naive Bayes classifier is to **assume that all features (in this case, the presence of words) are independent of each other.**

This means we assume that the probability of seeing the word "winning" is not affected by whether the word "lottery" is also present. In reality, this is not true (words are often dependent), but this simplifying assumption makes the math much easier and, surprisingly, often leads to a very effective model.

Because we assume independence, we can use the **product rule**. The probability of seeing both "lottery" AND "winning" in a spam email is simply the product of their individual probabilities:
```math
P(\text{lottery} \cap \text{winning} | \text{Spam}) \approx P(\text{lottery} | \text{Spam}) \cdot P(\text{winning} | \text{Spam})
```
<br>

This allows us to calculate the probability of seeing many words together without needing to find a single email that contains all of them.

## A Worked Example

Let's use this assumption to calculate $P(\text{Spam} | \text{"lottery" AND "winning"})$ using the following probabilities:

**1. Priors (from the previous lesson):**
* $P(\text{Spam}) = 0.2$
* $P(\text{Ham}) = 0.8$

**2. Likelihoods for "lottery":**
* $P(\text{lottery} | \text{Spam}) = \frac{14}{20} = 0.7$
* $P(\text{lottery} | \text{Ham}) = \frac{10}{80} = 0.125$

**3. Likelihoods for "winning":**
* $P(\text{winning} | \text{Spam}) = \frac{15}{20} = 0.75$
* $P(\text{winning} | \text{Ham}) = \frac{8}{80} = 0.1$

Now, we apply Bayes' theorem, but we use our naive assumption to calculate the likelihood of seeing both words.

**Numerator:** 
```math
P(\text{Spam}) \cdot P(\text{lottery} \cap \text{winning} | \text{Spam})
```
```math
\approx P(\text{Spam}) \cdot P(\text{lottery} | \text{Spam}) \cdot P(\text{winning} | \text{Spam})
```
```math
= 0.2 \times 0.7 \times 0.75 = 0.105
```
<br>

**Denominator** (The total probability of seeing both words):
```math
\approx [P(\text{Spam}) \cdot P(\text{lottery}|S) \cdot P(\text{winning}|S)] + [P(\text{Ham}) \cdot P(\text{lottery}|H) \cdot P(\text{winning}|H)]
```
```math
= (0.2 \cdot 0.7 \cdot 0.75) + (0.8 \cdot 0.125 \cdot 0.1)
```
```math
= 0.105 + 0.01 = 0.115
```
<br>

**Final Posterior Probability:**
```math
P(\text{Spam} | \text{lottery} \cap \text{winning}) = \frac{\text{Numerator}}{\text{Denominator}} = \frac{0.105}{0.115} \approx 0.913
```
<br>

By combining the evidence from two words, our belief that the email is spam has increased dramatically, from 20% to **91.3%**. This is the power of the Naive Bayes algorithm.


---

**Next:** [Probability in Machine Learning](./13_probability_in_machine_learning.md)