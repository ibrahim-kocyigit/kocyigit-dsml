# Interpreting Results: Steps and Common Misconceptions in Hypothesis Testing

Let's sum up the steps involved in hypothesis testing:

### Step 1: State Your Hypotheses

- **Null Hypothesis ($H_0$):** The baseline assumption (e.g., the population mean height is 66.7).
- **Alternative Hypothesis ($H_1$):** The statement you wish to prove (e.g., the population mean height is greater than 66.7).

### Step 2: Design the Test

- **Choose the test statistic** (e.g., sample mean, z-statistic, t-statistic, etc.).
- **Set the significance level ($\alpha$):** Commonly $\alpha = 0.05$.
  - $\alpha$ is the maximum probability of making a Type I error (rejecting $H_0$ when it is true).
  - Choose $\alpha$ to be small, but remember that lowering $\alpha$ increases the risk of Type II errors for a fixed sample size.

### Step 3: Compute the Observed Statistic

- Calculate the value of your test statistic from your sample data (e.g., observed sample mean = 68.442).


### Step 4: Make a Decision

- **Decision rule:** If the p-value is less than $\alpha$, reject $H_0$ and accept $H_1$.
- If the p-value is greater than $\alpha$, do **not** reject $H_0$.


## Important Reminders and Common Misconceptions

- **Type I Error:** Rejecting $H_0$ when it is actually true (controlled by $\alpha$).
- **Type II Error:** Failing to reject $H_0$ when $H_1$ is actually true.

- **Trade-off:** For a fixed sample size, reducing $\alpha$ increases the probability of a Type II error ($\beta$).

### Interpreting the p-value

- **The p-value is NOT** the probability that $H_0$ is true.
- **The p-value IS** the probability of observing data as extreme as (or more extreme than) your sample, assuming $H_0$ is true.
- A small p-value means your data is unlikely under $H_0$, so you have evidence against $H_0$.

### Interpreting Test Conclusions

- **Rejecting $H_0$:** There is enough evidence to support $H_1$.
- **Not rejecting $H_0$:** There is **not enough evidence** to support $H_1$; this does **not** mean $H_0$ is true.
  - Example: In the spam email analogy, not enough evidence to call an email spam does **not** guarantee it is ham.

### Wording of the Conclusion

- “There is statistically significant evidence at the ${\alpha}=$ {_insert_value here_} significance level that {_insert H1 here_}.”
- “There is not statistically significant evidence at the ${\alpha}=$ {_insert_value here_} significance level that {_insert H1 here_}.”

---

**Next:** [t-Distribution](./08_t-distribution.md)