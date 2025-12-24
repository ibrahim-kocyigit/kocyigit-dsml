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

* **$P(y | X)$ (Posterior)**: The probability of the class $y$ (e.g., Spam) *given* the features $X$ (the words in the email). This is what we want to find.
* **$P(X | y)$ (Likelihood)**: The probability of seeing these specific features $X$ *given* that the class is $y$ (e.g., "How often do the words 'free cash' appear in spam emails?").
* **$P(y)$ (Prior)**: The overall probability of class $y$ in the dataset (e.g., "What % of all emails are spam?").
* **$P(X)$ (Evidence)**: The probability of seeing the features $X$ anywhere. Since this is the same for all classes, we can ignore it during comparison.

### The "Naive" Assumption
Calculating $P(X|y)$ is hard if we treat all features as connected. The algorithm makes a **"Naive"** simplifying assumption:

**It assumes that all features are independent of each other given the class.**  

Mathematically, this allows us to break the complex Likelihood term into a simple product of individual feature probabilities:

$$
P(X | y) \approx P(x_1 | y) \cdot P(x_2 | y) \cdot \dots \cdot P(x_n | y)
$$

So the final classification rule becomes:

$$
\hat{y} = \underset{y}{\arg\max} \left( P(y) \cdot \prod_{i=1}^{n} P(x_i | y) \right)
$$

## 3. Key Assumptions

1. **Feature Independence:** This is the big one. We assume that the presence of one feature (e.g., the word "President") is unrelated to the presence of another (e.g., the word "White House"), given the class. In reality, this is almost never true (words are correlated!), but the model performs surprisingly well despite this violation.
2. **IID:** Independent and Identically Distributed samples.

## 4. How the Model is Trained

Unlike SVM or Logistic Regression, Naive Bayes **does not use optimization algorithms** like Gradient Descent. There is no iterative "learning."

Training is simply **counting**.  

### Step 1: Calculate Priors $P(y)$