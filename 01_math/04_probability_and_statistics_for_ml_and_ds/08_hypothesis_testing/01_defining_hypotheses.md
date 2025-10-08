# Defining Hypotheses

Hypothesis testing is a statistical method used to determine whether a belief or claim about a population is likely to be true or false based on sample data. One important application of hypothesis testing is **A/B testing**.

Imagine you have an email spam detector that classifies emails as either "ham" (not spam) or "spam". By default, we assume all emails are ham. This is because it's generally worse to delete a good email than to let a spam email slip through.

- **Null Hypothesis ($H_0$): The email is ham (not spam).** This is the base assumption, representing "no effect" or "no difference".
- **Alternative Hypothesis ($H_1$): The email is spam.** This is the statement we are trying to find evidence for.

In other words...

- The **null hypothesis** ($H_0$) is the baseline or default position.
- The **alternative hypothesis** ($H_1$) is the competing claim, usually the one you are interested in proving.
- The goal of hypothesis testing is to use data and evidence to decide between these two hypotheses.

## Key Properties of Hypotheses

- The null and alternative hypotheses are **mutually exclusive**: an email cannot be both ham and spam at the same time.
- Hypotheses must be **testable** and have a true/false answer.

## Decision Making in Hypothesis Testing

- If there is **enough evidence** against the null hypothesis ($H_0$), we **reject $H_0$** and accept the alternative hypothesis ($H_1$).
- If there is **not enough evidence** to reject $H_0$, we **do not accept $H_1$**—we simply fail to reject $H_0$. This does **not** mean $H_0$ is true, only that we don't have enough evidence to prove otherwise.

For example, in spam detection, we usually set the null hypothesis ($H_0$) as "the email is ham (not spam)" and the alternative hypothesis ($H_1$) as "the email is spam." 

When we test an email, we are not trying to prove it is spam directly. Instead, we look for enough evidence (such as sender information, email size, certain keywords or phrases etc.) to reject the idea that it is ham. If the evidence is strong enough, we reject $H_0$ and classify the email as spam. If not, we continue to treat the email as ham—not because we have proven it is ham, but because we lack sufficient evidence to say otherwise.

> This subtle distinction is key: hypothesis testing is about assessing whether the evidence is strong enough to reject the default assumption, not about proving the alternative is true.

---

**Next:** [Type I and Type II Errors](./02_type-i_and_type-ii_errors.md)