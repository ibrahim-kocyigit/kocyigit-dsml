# Bayes' Theorem - Prior and Posterior

Let's formalize the key components of Bayesian reasoning. The process involves updating our beliefs as we gain new information.

1.  **The Prior Probability: P(A)**  
    * This is our initial belief about an event `A` *before* we've seen any new evidence. It's the most basic piece of information we have.  

2.  **The Event (or Evidence): E**
    * This is a new piece of information that is relevant to our event `A`.  

3.  **The Posterior Probability: P(A|E)**
    * This is our updated belief about event `A` *after* we have taken the new evidence `E` into account. It is a conditional probability.

The posterior is always a better, more refined estimate than the prior because it incorporates more information. Bayes' theorem is the engine that takes us from the prior to the posterior.

## Revisiting Our Examples

Let's look at our previous problems through this new lens.

### Example 1: The Spam Filter
* **Prior:** The initial probability that any given email is spam.
    * $P(\text{Spam}) = \frac{\text{Total Spam Emails}}{\text{Total Emails}} = \frac{20}{100} = 20\%$  
* **Event/Evidence:** We discover that the email contains the word "lottery."  
* **Posterior:** The updated probability that the email is spam, *given that* it contains the word "lottery."
    * $P(\text{Spam} | \text{lottery}) = \frac{\text{Spam emails with "lottery"}}{\text{Total emails with "lottery"}} = \frac{14}{24} \approx 58.3\%$

### Example 2: The Medical Diagnosis
* **Prior:** The initial probability of being sick based on the general population.
    * $P(\text{Sick}) = \frac{1}{10,000} = 0.01\%$
* **Event/Evidence:** You receive a positive test result.
* **Posterior:** The updated probability that you are sick, *given that* you tested positive.
    * $P(\text{Sick} | \text{Positive Test}) \approx 0.98\%$

### Example 3: Two Dice Roll
* **Prior:** The initial probability that the sum of two dice is 10.
    * $P(\text{Sum=10}) = \frac{3}{36} = \frac{1}{12}$
* **Event/Evidence:** You are told that the first die is a 6.
* **Posterior:** The updated probability that the sum is 10, *given that* the first die is a 6.
    * $P(\text{Sum=10} | \text{First=6}) = \frac{1}{6}$

### Example 4: Two Coin Flips
* **Prior:** The initial probability that both coins land on heads.
    * $P(\text{HH}) = \frac{1}{4}$
* **Event/Evidence:** You are told that the first coin landed on heads.
* **Posterior:** The updated probability that both coins are heads, *given that* the first was heads.
    * $P(\text{HH} | \text{First=H}) = \frac{1}{2}$