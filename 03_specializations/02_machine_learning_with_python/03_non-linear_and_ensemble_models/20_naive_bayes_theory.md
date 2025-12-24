# Naive Bayes

## 1. The Intuitive Idea: Probability, Not Just Boundaries

The **Naive Bayes Classifier** is a supervised learning algorithm that takes a different approach than models like SVM or Logistic Regression. Instead of trying to find a geometric boundary (a line or curve) to separate classes, it is a **probabilistic classifier**.

It asks a simple question: *"Given these features, what is the probability that this data point belongs to Class A versus Class B?"*

It is most famous for its dominance in text classification, particularly for **spam filtering**:
* A geometric model looks for a "line" between spam and ham.
* Naive Bayes calculates: "This email contains the words 'free', 'winner', and 'cash'. The probability of this combination appearing in a spam email is 95%. Therefore, it is Spam."

## 2. The Mathematics: Bayes' Theorem

The engine behind this model is **Bayes' Theorem**, a fundamental theorem in probability theory that describes the probability of an event, based on prior knowledge of conditions that might be related to the event.

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

## 3. Key Assumptions

1. **Feature Independence:** This is the big one. We assume that the presence of one feature (e.g., the word "President") is unrelated to the presence of another (e.g., the word "White House"), given the class. In reality, this is almost never true (words are correlated!), but the model performs surprisingly well despite this violation.
2. **IID:** Independent and Identically Distributed samples.

## 4. How the Model is Trained

Unlike SVM or Logistic Regression, Naive Bayes **does not use optimization algorithms** like Gradient Descent. There is no iterative "learning."

Training is simply **counting**.  

### Step 1: Calculate Priors $P(y)$
We calculate the frequency of each class in the training data.

$$
P(\text{Spam}) = \frac{\text{Count(Spam emails)}}{\text{Total emails}}
$$

### Step 2: Calculate Likelihoods $P(x_i | y)$
We calculate the frequency of every feature for every class.

$$
P(\text{"cash"} | \text{Spam}) = \frac{\text{Count("cash" in Spam)}}{\text{Total words in Spam}}
$$

#### The Zero-Frequency Problem (and Laplace Smoothing)
What if a new email contains a word, say "Bitcoin", that we never saw in our Spam training data?
*   $P(\text{"Bitcoin"} | \text{Spam}) = 0$
*   Because we multiply probabilities, this single zero would turn the entire probability score to **0**.

To fix this, we use **Laplace Smoothing (Additive Smoothing)**. We add a small number (usually $\alpha=1$) to the count of every word, ensuring no probability is ever truly zero.

$$
P(x_i | y) = \frac{\text{count}(x_i, y) + \alpha}{\text{count}(y) + \alpha \cdot d}
$$

*   $\alpha$: Smoothing parameter (usually 1).
*   $d$: The number of distinct features (vocabulary size).

## 5. Model-Specific Considerations (Variants)

Different types of data require different versions of Naive Bayes:

1. **Multinomial Naive Bayes:** Used for **discrete counts**. This is the standard for text classification (counting word frequencies).
2. **Gaussian Naive Bayes:** Used for **continuous features** (e.g., height, weight). It assumes the features follow a normal (Gaussian) distribution. It calculates likelihoods using the Gaussian Probability Density Function (PDF) instead of simple counting.
3. **Bernoulli Naive Bayes:** Used for **binary features** (e.g., the word is present/absent, rather than count).

## 6. Common Pitfalls

* **Correlated Features:** If you have two features that are identical (e.g., "price_in_dollars" and "price_in_euros"), Naive Bayes will "double count" their importance, which can skew the probability. Feature selection is important.
* **Zero Probability:** Always remember to use smoothing (like Laplace smoothing) if calculating from scratch, otherwise unknown categories will break the model. 
* **Numerical Underflow:** When implementing from scratch, multiplying many small probabilities (e.g., $0.001 \times 0.002 \dots$) results in tiny numbers that computers round to zero.
    * **Solution:** Compute everything in **Log Space**. Instead of $A \cdot B$, calculate $\log(A) + \log(B)$

## 7. Summary
*   **Naive Bayes** is a probabilistic classifier based on **Bayes' Theorem**.
*   It assumes **independence** between features to simplify the math (the "Naive" part).
*   Training involves **counting frequencies** to estimate Prior and Likelihood probabilities.
*   **Laplace Smoothing** is required to handle unseen features (zero probabilities).
*   It is extremely fast, works well with high-dimensional data (like text), and is a strong baseline for classification tasks.

---

**Next:** [Naive Bayes Implementation](./21_naive_bayes_implementation.py)