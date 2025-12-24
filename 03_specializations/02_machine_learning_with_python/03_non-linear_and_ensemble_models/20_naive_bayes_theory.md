# Naive Bayes

## 1. The Intuitive Idea: Probability, Not Just Boundaries

The **Naive Bayes Classifier** is a supervised learning algorithm that takes a different approach than models like SVM or Logistic Regression. Instead of trying to find a geometric boundary (a line or curve) to separate classes, it is a **probabilistic classifier**.

It asks a simple question: *"Given these features, what is the probability that this data point belongs to Class A versus Class B?"*

It is most famous for its dominance in text classification, particularly for **spam filtering**:
* A geometric model looks for a "line" between spam and ham.
* Naive Bayes calculates: "This email contains the words 'free', 'winner', and 'cash'. The probability of this combination appearing in a spam email is 95%. Therefore, it is Spam."

## 2. The Mathematics: Bayes' Theorem

The engine behing this model is **Bayes' Theorem**, a fundamental theorem in probability theory that describes the probability of an event, based on prior knowledge of conditions that might be related to the event.

$$
P(y | X) = \frac{P(X | y) \cdot P(y)}{P(X)}
$$

...where...

* **$P(y|X)$**: