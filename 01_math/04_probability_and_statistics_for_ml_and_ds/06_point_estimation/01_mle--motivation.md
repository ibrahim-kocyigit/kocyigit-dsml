# Maximum Likelihood Estimation: Motivation

Maximum likelihood estimation (MLE) is a fundamental concept in machine learning for training models. The idea behind MLE is simple:  

> Given some evidence (data), you want to find the scenario (model or parameters) that most likely produced that evidence.

## Everyday Example

Imagine you walk into a living room and see popcorn on the floor next to the couch. Which event is more likely to have happened?
- People watching a movie
- People playing board games
- Somebody taking a nap

You reason:
- Probability of popcorn after movies: **high**
- Probability after board games: **medium**
- Probability after nap: **low**

You infer that watching movies is the most likely scenario, because it has the highest probability of producing popcorn on the floor.

## Maximizing Conditional Probability

What you did was maximize the conditional probability:
- Probability of popcorn **given** movies is high
- Probability of popcorn **given** board games is medium
- Probability of popcorn **given** nap is low

You picked the scenario that made the evidence most likely—this is **maximum likelihood**.

## MLE in Machine Learning

In machine learning, you have data and several models that could have generated it. You estimate:
- Probability of data **given** Model 1: $P(\text{Data} \mid \text{Model}_1)$
- Probability of data **given** Model 2: $P(\text{Data} \mid \text{Model}_2)$
- Probability of data **given** Model 3: $P(\text{Data} \mid \text{Model}_3)$

You pick the model that gives the highest probability—the model most likely to have produced the data.

## Connection to Linear Regression

Linear regression also fits into this framework.  

Imagine you have data points and three possible models (lines). If you can generate points based on a line, the model that makes the observed points most likely is the one you pick.

This is the essence of maximum likelihood estimation:  

> **Choose the model or parameters that maximize the probability of observing your data.**

---

**Next:** []()