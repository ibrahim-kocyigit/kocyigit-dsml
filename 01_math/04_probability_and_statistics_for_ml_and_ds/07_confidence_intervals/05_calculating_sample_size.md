# Calculating Sample Size

In the previous example, we calculated a 95% confidence interval for the mean height of adults in Statistopia using a sample of 49 people. The margin of error was 7 cm, giving an interval of [163 cm, 177 cm]. But what if we want a more precise estimate, say a margin of error of only 3 cm?

## How to Find the Required Sample Size

To achieve a smaller margin of error, we need a larger sample. The question is: **What is the minimum sample size needed to achieve a desired margin of error?**

Recall the formula for the margin of error (MOE):

$$
\text{MOE} = z_{1-\alpha/2} \times \frac{\sigma}{\sqrt{n}}
$$

We want the margin of error to be no more than 3 cm. So, set up the inequality:

$$
3 \geq 1.96 \times \frac{25}{\sqrt{n}}
$$

Now, solve for $n$:

1. Divide both sides by $1.96$:
   $$
   \frac{3}{1.96} \geq \frac{25}{\sqrt{n}}
   $$
2. Multiply both sides by $\sqrt{n}$:
   $$
   \frac{3}{1.96} \sqrt{n} \geq 25
   $$
3. Divide both sides by $\frac{3}{1.96}$:
   $$
   \sqrt{n} \geq \frac{25 \times 1.96}{3}
   $$
4. Square both sides:
   $$
   n \geq \left(\frac{25 \times 1.96}{3}\right)^2 \approx 266.78
   $$

Since you can't sample a fraction of a person, round up to the next whole number:

**Minimum sample size needed: $n = 267$**

## General Formula

For any desired margin of error (MOE):

$$
n \geq \left( \frac{z_{1-\alpha/2} \cdot \sigma}{\text{MOE}} \right)^2
$$

- $z_{1-\alpha/2}$: critical value for your confidence level (e.g., 1.96 for 95%)
- $\sigma$: population standard deviation
- MOE: desired margin of error

Plug in your values to find the required sample size for your study.