# Introduction to Bayesian

## 1. The Intuitive Idea: What is a "Probability"?

At the heart of statistics lie two major philosophical frameworks: **Frequentist** and **Bayesian**. While this course primarily uses the Frequentist approach, understanding the Bayesian alternative is crucial for a complete statistical education.

The entire difference between these two schools of thought boils down to how they answer one simple question: **"What is a probability?"**

* **The Frequentist Answer:** A probability is a **long-run frequency**. It's an objective property of the world. If you flip a fair coin a million times, it will land on heads about 50% of the time. The probability is in the coin, not in your head.
* **The Bayesian Answer:** A probability is a **degree of belief**. It's a subjective measure of your confidence or uncertainty about a statement, which can be updated as you get new information. The probability is in your mind, not in the world.

This philosophical split leads to profound differences in how we approach statistical problems.

## 2. The World Cup Example: Probability of a Past Event

Let's illustrate the difference with a simple question:

**"What is the probability that France won the 2018 FIFA World Cup?"**

* **Frequentist View:** This question is nonsensical. The event has already happened. The outcome is a fixed fact. France either won or they didn't. Therefore the probability is either 1 (100%) if they won, or 0 (0%) if they didn't. There is no "in-between". A Frequentist can only talk about the probability of a future, repeatable event.

* **Bayesian View:** This question is perfectly valid. If you don't know the answer for certain, you can assign a probability that reflects your degree of belief.
    * If you're a huge football fan, you might say, "I'm 99% sure it was France."
    * If you vaguely remember but aren't certain, your might say, "I'm about 60% confident it was France."
    * If you have no idea, you might say, "There were 32 teams, so maybe I have a 1/32 chance of guessing correctly.

In the Bayesian world, it is perfectly acceptable to make probability statements about parameters of fixed events because probability is a measure of your knowledge _about_ them.

## 3. The Chocolate Bag Example: Updating Beliefs with New Data

This is the second core principle of Bayesian statistics: **as you gather new data, you update your beliefs.**

**The Setup:**  
* **Bag A:** Contains two silver chocolates (S/S).
* **Bag B:** Contains one silver and one purple chocolate (S/P).
* I randomly pick one bag (you don't know which) and put it behind my back.

**The Prior Belief:**  
Before any new information, what is the probability that I am holding Bag A (S/S)?
* Both Frequentists and Bayesians agree here. Since the choice was random, there is a 50% chance I have Bag A and a 50% chance I have Bag B. This initial belief is called the **prior probability**. 

**The New Data:**  
I reach into the bag I'm holding and pull out **one silver chocolate**.

**The Update (The Bayesian Step):**  
A Bayesian uses this new piece of data to **update their belief**.
* There were three possible ways I could have drawn a silver chocolate in total:
    1. From Bag A (S/S), I could have drawn the first silver chocolate.
    2. From Bag A (S/S), I could have drawn the second silver chocolate.
    3. From Bag B (S/P), I could have drawn the one silver chocolate.
* Given that I *did* draw a silver chocolate, two of the three equally likely possibilities come from Bag A.
* Therefore, my updated belief (called the **posterior probability**) is now:
    * Probability I have Bag A (S/S) = 2/3 (or ≈67%)
    * Probability I have Bag B (S/P) = 1/3 (or ≈33%)

My confidence that I am holding the S/S bag has increased from 50% to 67% based on the new evidence.

**The Frequentist Stance:**  
A strict Frequentist would argue that the bag behind my back is *already* either Bag A or Bag B. It is a fixed reality. The probability is either 100% or 0%. The act of drawing a chocolate doesn't change the physical bag itself.

## 4. Summary: Frequentist vs. Bayesian
| Feature | Frequentist Statistics | Bayesian Statistics |
| :--- | :--- | :--- |
| **What is Probability?** | The long-run frequency of a repeatable event. An objective property of the world. | A degree of belief or confidence about a statement. A subjective property of your knowledge. |
| **Model Parameters** | Are fixed, unknown constants. We compute confidence intervals that have a 95% chance of *containing* the true parameter. | Are random variables that we can have beliefs about. We compute credible intervals that contain the parameter with 95% probability. |
| **Core Idea** | Design procedures with good long-run performance (e.g., confidence intervals, p-values). | Start with a prior belief, collect data, and update that belief to arrive at a posterior belief. |

This course has been focusing on the Frequentist framework, but it's important to know that the Bayesian framework exists as a powerful and increasingly popular alternative for statistical reasoning and modeling.

---

**Next:** [Bayesian Approaches to Statistics and Modeling](./04_bayesian_approaches_to_statistics_and_modeling.md)