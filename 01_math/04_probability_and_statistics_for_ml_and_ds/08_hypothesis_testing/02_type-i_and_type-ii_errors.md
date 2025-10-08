# Type I and Type II Errors

Ideally, we would always make perfect decisions when testing hypotheses. However, due to randomness and limited information, errors are inevitable. In hypothesis testing, there are two possible actions (e.g., send an email to spam or to the inbox), and each action can be right or wrong.

## The Two Types of Errors

### Type I Error (False Positive)
- **Definition:** Rejecting the null hypothesis ($H_0$) when it is actually true.
- **Example:** Sending a regular (ham) email to the spam box.
- **Impact:** Type I errors are often considered more severe, especially in cases like email filtering, where losing a good email is worse than letting a spam email through.

### Type II Error (False Negative)
- **Definition:** Failing to reject the null hypothesis ($H_0$) when the alternative hypothesis ($H_1$) is actually true.
- **Example:** Allowing a spam email into the inbox by incorrectly classifying it as ham.

## Decision Table

| Ground Truth      | Decision: Reject $H_0$ | Decision: Do Not Reject $H_0$ |
|-------------------|------------------------|-------------------------------|
| $H_0$ is true     | Type I Error           | Correct Decision              |
| $H_1$ is true     | Correct Decision       | Type II Error                 |

## Significance Level ($\alpha$)

- The **significance level** ($\alpha$) is the maximum probability of committing a Type I error that you are willing to tolerate.
- Typical values for $\alpha$ are 0.05 or 0.01.
    - $\alpha = 0.05$ means you are willing to incorrectly send a ham email to the spam box 5% of the time.
- If $\alpha = 0$, you never make a Type I error, but you will make many Type II errors.
- If $\alpha = 1$, you always reject $H_0$, making a Type I error every time $H_0$ is true.
- **Trade-off:** Lowering $\alpha$ reduces Type I errors but increases Type II errors (for a fixed sample size).

## Summary

- **Type I Error:** Rejecting $H_0$ when it is true (false positive).
- **Type II Error:** Not rejecting $H_0$ when $H_1$ is true (false negative).
- **Significance level ($\alpha$):** The maximum probability of a Type I error you are willing to accept; it sets the threshold for rejecting $H_0$.

---

**Next:** 