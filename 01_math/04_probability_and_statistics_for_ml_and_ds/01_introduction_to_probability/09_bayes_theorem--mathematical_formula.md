# Bayes' Theorem - The Mathematical Formula

In the last lesson, we used intuition and a population breakdown to solve the rare disease problem. Now, let's solve the exact same problem using the formal rules of probability to derive **Bayes' Theorem**.

Our goal is to find the probability that you are sick, given that you tested sick: **P(Sick | Diagnosed Sick)**.

Let's start by defining our events and listing the information we were given:

* **Event A:** The person is actually sick.
* **Event A':** The person is healthy (the complement of A).
* **Event B:** The person is diagnosed as sick (tests positive).

**Known Probabilities:**
1.  The probability of being sick is 1 in 10,000.
    * $P(A) = 0.0001$
2.  The probability of being healthy is the complement.
    * $P(A') = 1 - P(A) = 0.9999$
3.  The test is 99% effective. This gives us two conditional probabilities:
    * The probability of testing positive *given that* you are sick (True Positive Rate): $P(B|A) = 0.99$
    * The probability of testing positive *given that* you are healthy (False Positive Rate): $P(B|A') = 0.01$

## Deriving Bayes' Theorem

Our starting point is the formula for conditional probability:
```math
P(A|B) = \frac{P(A \cap B)}{P(B)}
```
<br>

In our terms:
```math
P(\text{Sick} | \text{Diag. Sick}) = \frac{P(\text{Sick} \cap \text{Diag. Sick})}{P(\text{Diag. Sick})}
```
<br>
Our task is to find the values for the numerator and the denominator.

### Step 1: The Numerator, $P(A \cap B)$
We can use the **General Product Rule** to find the probability of being sick AND being diagnosed sick:
```math
P(A \cap B) = P(A) \cdot P(B|A)
```
<br>

### Step 2: The Denominator, $P(B)$
How do we find the overall probability of being diagnosed sick? A person can be diagnosed sick in two mutually exclusive ways:
1.  They are sick AND are correctly diagnosed sick.
2.  They are healthy AND are incorrectly diagnosed sick.

The total probability of being diagnosed sick is the sum of the probabilities of these two scenarios (using the sum rule for disjoint events):
```math
P(B) = P(A \cap B) + P(A' \cap B)
```
<br>

We can now apply the General Product Rule to each of these terms:
```math
P(B) = (P(A) \cdot P(B|A)) + (P(A') \cdot P(B|A'))
```
<br>

### Step 3: Assembling Bayes' Theorem
Now we can substitute our expressions for the numerator and the denominator back into the original conditional probability formula.

> $$ P(A|B) = \frac{P(A) \cdot P(B|A)}{P(A) \cdot P(B|A) + P(A') \cdot P(B|A')} $$

## Solving the Problem with the Formula

Let's plug our known numbers into Bayes' Theorem to find the probability that you are sick given that you tested positive.

* **Numerator:** 
```math
P(A) \cdot P(B|A) = (0.0001) \times (0.99) = 0.000099
```
* **Denominator:**
    * Part 1 (True Positives):
    ```math
    P(A) \cdot P(B|A) = 0.000099
    ```
     
    * Part 2 (False Positives): $ P(A') \cdot P(B|A') = (0.9999) \times (0.01) = 0.009999 $
    * Total Denominator = $0.000099 + 0.009999 = 0.010098$  

* **Final Probability:**
```math
P(A|B) = \frac{0.000099}{0.010098} \approx 0.0098
```
<br>

The result is approximately **0.98%**, the exact same answer we found intuitively by breaking down the population. This formula may look complicated, but it's just a combination of the simpler probability rules we've already learned.