# Bayes' Theorem - A Spam Filter Example

Let's apply Bayes' theorem to another classic example: building a simple spam filter.

**Scenario:**
We have a dataset of 100 emails.
* **20 emails are Spam.**
* **80 emails are Not Spam** (often called "Ham").

Without any other information, our best guess for a new email is that it has a 20% chance of being spam. This is our **prior probability**.

To build a better model, we need to use features from the email's content. Let's analyze the presence of the word "lottery".

**New Information (Our Evidence):**
* Out of the 20 Spam emails, **14 contain the word "lottery."**
* Out of the 80 Ham emails, **10 contain the word "lottery."**

**The Core Question:**
If we receive a *new* email that contains the word "lottery," what is the probability that it is actually spam? In other words, we want to find **P(Spam | "lottery")**.

## The Intuitive Solution (Reducing the Sample Space)

When we are given the evidence that an email contains the word "lottery," our world shrinks. We no longer care about the emails that *don't* contain the word.

1.  **Find the new sample space:** How many emails in total contain the word "lottery"?
    * $14 (\text{from spam}) + 10 (\text{from ham}) = 24$ emails.  

2.  **Find the number of favorable outcomes:** Within this new sample space of 24 emails, how many are actually spam?
    * **14** emails.  

3.  **Calculate the probability:**

```math
P(\text{Spam} | \text{lottery}) = \frac{\text{Number of spam emails with "lottery"}}{\text{Total number of emails with "lottery"}} = \frac{14}{24} = \frac{7}{12} \approx 0.583
```
<br>

So, after seeing the word "lottery," our belief that the email is spam has increased from our prior probability of 20% to a new **posterior probability** of 58.3%.

This process of updating our belief based on new evidence is exactly what Bayes' theorem formalizes.

## The Formal Solution (Using Bayes' Theorem)

Let's solve the same problem using the formula.

**Events:**
* **A:** The email is Spam.
* **B:** The email contains the word "lottery".

**Bayes' Theorem:**
```math
P(A|B) = \frac{P(A) \cdot P(B|A)}{P(A) \cdot P(B|A) + P(A') \cdot P(B|A')}
```
<br>

Let's calculate each component from our initial data:
* **$P(A)$ (Prior):** The overall probability of an email being spam.
    * $P(\text{Spam}) = \frac{20}{100} = 0.2$  

* **$P(A')$ (Complement):** The overall probability of an email being ham.
    * $P(\text{Not Spam}) = \frac{80}{100} = 0.8$  

* **$P(B|A)$ (Likelihood):** The probability of seeing the word "lottery" *given that* the email is spam.
    * Out of 20 spam emails, 14 have the word. $P(\text{lottery}| \text{Spam}) = \frac{14}{20} = 0.7$  

* **$P(B|A')$ (Likelihood of Complement):** The probability of seeing the word "lottery" *given that* the email is ham.
    * Out of 80 ham emails, 10 have the word. $P(\text{lottery}| \text{Not Spam}) = \frac{10}{80} = 0.125$

Now, we plug these values into the formula:
```math
P(\text{Spam} | \text{"lottery"}) = \frac{(0.2) \cdot (0.7)}{(0.2) \cdot (0.7) + (0.8) \cdot (0.125)}
```
```math
= \frac{0.14}{0.14 + 0.1} = \frac{0.14}{0.24} \approx 0.583
```
<br>

The formal calculation gives us the exact same result as our intuitive method.