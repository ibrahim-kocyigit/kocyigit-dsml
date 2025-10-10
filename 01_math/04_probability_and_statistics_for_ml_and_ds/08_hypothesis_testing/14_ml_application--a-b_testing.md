# ML Application: A/B Testing

A/B testing is a practical application of two-sample hypothesis testing, commonly used to compare two versions of a product, website, or process.

## What is A/B Testing?

- **A/B testing** compares two groups (A and B) to determine if a change (e.g., a new website design) leads to a significant difference in a key metric (e.g., conversion rate, average purchase).
- Subjects are randomly assigned to either group A (control) or group B (variation).

## Example 1: Comparing Mean Purchases

- **Scenario:** Test if moving the "Buy Now" button increases purchase amounts.
- **Design:** 80 customers see design A, 20 see design B.
- **Results:**
  - Group A: 
  
  $\bar{x}_A = \$50$, $s_A = \$10$
  
  - Group B: $\bar{x}_B = \$55$, $s_B = \$15$
- **Hypotheses:**
  - $H_0$: Mean purchase for A and B are the same ($\mu_A = \mu_B$)
  - $H_1$: Mean purchase for B is higher ($\mu_B > \mu_A$)
- **Test:** Two-sample t-test (assume normality or large $n$)
- **Observed statistic:** $t = -1.414$, degrees of freedom $\approx 23.38$
- **p-value:** $0.085$
- **Decision:** Since $p > 0.05$, do not reject $H_0$ (no significant difference).

---

## A/B Testing vs. T-tests

- **A/B testing** is a methodology: it includes experiment design, randomization, measurement, and statistical analysis.
- **T-tests** (and other statistical tests) are tools used within A/B testing to compare means, proportions, etc.
- The choice of test depends on the metric and data type (means, proportions, etc.).

---

## Example 2: Comparing Conversion Rates (Proportions)

- **Scenario:** Test if a new website design increases conversion rate.
- **Design:** 80 customers in group A, 20 in group B.
  - Group A: 20 conversions ($x_A = 20$)
  - Group B: 8 conversions ($x_B = 8$)
- **Hypotheses:**
  - $H_0$: Conversion rates are equal ($p_A = p_B$)
  - $H_1$: Conversion rate for B is higher ($p_B > p_A$)
- **Test:** Compare proportions using a z-test for two proportions.
- **Test statistic:** Standardize the difference in sample proportions using pooled estimate $\hat{p} = \frac{x_A + x_B}{n_A + n_B}$
- **Observed statistic:** $z = -1.336$
- **p-value:** $0.091$
- **Decision:** Since $p > 0.05$, do not reject $H_0$ (no significant difference).

---

## Key Steps in A/B Testing

1. **Propose a variation** to test (e.g., new design).
2. **Randomly assign** subjects to groups.
3. **Measure outcomes** (e.g., mean purchase, conversion rate).
4. **Choose appropriate metrics** and statistical tests.
5. **Analyze results** and make a decision.

---

## Summary

- A/B testing is a structured approach to comparing two versions of a product or process.
- It uses statistical tests (t-tests, z-tests, etc.) to determine if observed differences are significant.
- The methodology includes experiment design, randomization, measurement, and statistical inference.

---



