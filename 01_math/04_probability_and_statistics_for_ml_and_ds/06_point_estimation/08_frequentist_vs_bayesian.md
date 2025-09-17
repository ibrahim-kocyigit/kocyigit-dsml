# Frequentist vs. Bayesian

Frequentist versus Bayesian is an age-old debate in statistics between two broad philosophies. The root difference lies in how they interpret probabilities.

## A Story: The Coin Toss

A frequentist and a Bayesian walk into a bar. They find a coin and want to know its probability of landing heads. They toss the coin 10 times and get 8 heads and 2 tails.

- **Frequentist:**  
  The probability of heads is $0.8$ (just the observed frequency).

- **Bayesian:**  
  From experience, coins are almost always fair, so they believe the probability should be around $0.5$. Seeing the evidence, they adjust their belief a little, but still think the coin is likely fair.

## The Role of Priors

The big difference is that Bayesians introduce the idea of a **prior**—a belief about the model before seeing any data. After seeing data, they update their belief (the prior) to form a **posterior**.

Frequentists have no concept of priors; they rely only on the evidence.

## Interpreting Probability

- **Frequentists:**  
  Probabilities represent long-term frequencies of events (what happens if you repeat the experiment infinitely many times).

- **Bayesians:**  
  Probabilities represent degrees of belief or certainty about an event.

## Summary of Approaches

- **Frequentist:**  
  Find the model with the greatest likelihood of generating the observed data.

- **Bayesian:**  
  Update prior beliefs about the model based on the observed data.

If you thought a coin was balanced, but after tossing it 10 times you see 8 heads, a Bayesian would reconsider their prior assumption, while a frequentist would just report the observed frequency.

So far, all the point estimations we've seen (including MLE) follow a frequentist approach.  

Now we'll dig deeper into the Bayesian approach and see how using priors affects predictions.

---

**Next:** [Bayesian Statistics: MAP Estimation](./09_bayesian_statistics--map.md)