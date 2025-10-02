# Bayesian Statistics: Full Worked Example

We will work through a complete Bayesian update with coin flips, starting from a non-informative prior and then updating with additional data. We will:
- Derive the likelihood for observed coin flips.
- Choose a prior and compute the posterior using Bayes’ theorem.
- Compare MAP vs. MLE.
- Perform sequential updating with a second batch of data.
- Visualize priors and posteriors and summarize results.

---

## 1) Setup: Model, Data, and Bayes’ Theorem

- Parameter (unknown coin bias): $\theta \in (0,1)$.
- Data: $\mathbf{x} = (x_1,\dots,x_n)$ where each $x_i \in \{0,1\}$.
- Conditional model: $x_i \mid \theta \sim \text{Bernoulli}(\theta)$, independent across flips.

Likelihood for $h$ heads and $t$ tails (with $h+t=n$):
$$
p(\mathbf{x}\mid \theta)=\theta^{h}(1-\theta)^{t}.
$$

Bayes’ theorem (continuous $\theta$, discrete $\mathbf{x}$):
$$
p(\theta \mid \mathbf{x})=\frac{p(\mathbf{x}\mid \theta)\,p(\theta)}{p(\mathbf{x})}
\propto p(\mathbf{x}\mid \theta)\,p(\theta).
$$

---

## 2) Prior Choice and Conjugacy

Choose a non-informative (uniform) prior on $(0,1)$:
$$
\theta \sim \text{Beta}(\alpha,\beta)\quad \text{with } \alpha=\beta=1.
$$

Conjugacy fact (Beta–Bernoulli):
- If $\theta \sim \text{Beta}(\alpha,\beta)$ and observe $h$ heads, $t$ tails,
- Then posterior $\theta \mid \mathbf{x} \sim \text{Beta}(\alpha+h,\beta+t)$.

Beta pdf and normalizing constant:
$$
\text{Beta}(a,b)\text{ pdf: } f(\theta)=\frac{\theta^{a-1}(1-\theta)^{b-1}}{B(a,b)},\quad
B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}.
$$

---

## 3) Round 1: 10 Flips (8 Heads, 2 Tails)

- Data: $h=8$, $t=2$, $n=10$.
- Prior: $\text{Beta}(1,1)$.

Posterior:
$$
\theta \mid \mathbf{x}_{1:10} \sim \text{Beta}(1+8,\,1+2)=\text{Beta}(9,3).
$$
Posterior pdf (up to constant):
$$
p(\theta \mid \mathbf{x}_{1:10}) \propto \theta^{8}(1-\theta)^2.
$$
Normalizing constant here is $1/B(9,3)=\dfrac{11!}{8!\,2!}$, consistent with $8!\cdot 2!/11!$ in the denominator.

Posterior summaries:
- Mean: $E[\theta \mid \mathbf{x}]=\dfrac{9}{9+3}=\dfrac{9}{12}=0.75$.
- Variance: $Var[\theta \mid \mathbf{x}]=\dfrac{9\cdot 3}{(12)^2(13)}=\dfrac{27}{1872}\approx 0.0144$.
- MAP (mode, since $a>1,b>1$): $\dfrac{9-1}{9+3-2}=\dfrac{8}{10}=0.8$.

Check via calculus (argmax of log-posterior):
$$
\ell(\theta)=8\ln\theta + 2\ln(1-\theta) \Rightarrow \frac{d\ell}{d\theta}=\frac{8}{\theta}-\frac{2}{1-\theta}=0
\Rightarrow 8(1-\theta)=2\theta \Rightarrow \theta=0.8.
$$

MLE comparison:
- With $h=8$, $n=10$, frequentist MLE $\hat{\theta}_{\text{MLE}}=h/n=0.8$.
- Under uniform prior, MAP = MLE.

---

## 4) Round 2: Add 10 Flips (6 Heads, 4 Tails)

Sequential update uses the Round 1 posterior as the new prior.

- New data: $h=6$, $t=4$.
- Prior now: $\text{Beta}(9,3)$.

Posterior:
$$
\theta \mid \mathbf{x}_{1:20} \sim \text{Beta}(9+6,\,3+4)=\text{Beta}(15,7).
$$
Posterior pdf (up to constant):
$$
p(\theta \mid \mathbf{x}_{1:20}) \propto \theta^{14}(1-\theta)^6.
$$

Posterior summaries:
- Mean: $E[\theta \mid \mathbf{x}]=\dfrac{15}{15+7}=\dfrac{15}{22}\approx 0.6818$.
- Variance: $Var[\theta \mid \mathbf{x}]=\dfrac{15\cdot 7}{(22)^2(23)}=\dfrac{105}{11132}\approx 0.0094$.
- MAP: $\dfrac{15-1}{15+7-2}=\dfrac{14}{20}=0.7$.

Frequentist comparison:
- Over all 20 flips, $h=14$, $n=20 \Rightarrow \hat{\theta}_{\text{MLE}}=0.7$.
- Batch vs. sequential: $\text{Beta}(1+14,1+6)=\text{Beta}(15,7)$ matches the sequential result.

---

## 5) Why Normalizing Constants Can Be Ignored for MAP
For maximizing the posterior w.r.t. $\theta$,
$$
p(\theta \mid \mathbf{x})=\frac{p(\mathbf{x}\mid \theta)\,p(\theta)}{p(\mathbf{x})}
\propto p(\mathbf{x}\mid \theta)\,p(\theta).
$$
The denominator $p(\mathbf{x})$ is a constant in $\theta$, so it does not affect the location of the maximum (MAP). Likewise, constant priors do not change the argmax.

---

## 6) MLE vs. MAP
- With non-informative (uniform) prior, MAP = MLE.
- With informative priors, MAP deviates from MLE, especially with small sample sizes.
- As $n$ grows, MAP and MLE typically converge (under regularity conditions).

---

## 7) General Beta–Bernoulli Update Rule
Given prior $\theta \sim \text{Beta}(\alpha,\beta)$ and data with $h$ heads and $t$ tails:
- Posterior: $\theta \mid \mathbf{x}\sim \text{Beta}(\alpha+h, \beta+t)$
- Posterior mean: $E[\theta\mid \mathbf{x}]=\dfrac{\alpha+h}{\alpha+\beta+h+t}$
- Posterior MAP (if $\alpha+h>1$ and $\beta+t>1$): $\dfrac{\alpha+h-1}{\alpha+\beta+h+t-2}$

---

## 8) Summary Table

| Stage | Prior | Data $(h,t)$ | Posterior | Mean | MAP |
|------:|:------|:-------------|:----------|:-----|:----|
| Round 1 | $\text{Beta}(1,1)$ | $(8,2)$ | $\text{Beta}(9,3)$ | $9/12=0.75$ | $0.8$ |
| Round 2 | $\text{Beta}(9,3)$ | $(6,4)$ | $\text{Beta}(15,7)$ | $15/22\approx 0.6818$ | $0.7$ |

---

## 9) Python: Plot Priors and Posteriors

This script:
- Computes Beta pdfs using the Gamma function (no SciPy required).
- Plots the initial prior, Round 1 posterior, and Round 2 posterior.
- Marks MAP points and MLEs.

It also saves the figure to ./images/beta_updates.png for inclusion in your repo.

```python
import numpy as np
import matplotlib.pyplot as plt
from math import gamma
import os

def beta_norm(a, b):
    return gamma(a)*gamma(b)/gamma(a+b)

def beta_pdf(theta, a, b):
    # theta may be scalar or numpy array
    B = beta_norm(a, b)
    return (theta**(a-1) * (1-theta)**(b-1)) / B

# Parameters
a0, b0 = 1, 1          # prior
h1, t1 = 8, 2          # round 1 data
a1, b1 = a0+h1, b0+t1  # posterior after round 1

h2, t2 = 6, 4          # round 2 data
a2, b2 = a1+h2, b1+t2  # posterior after round 2

# MAPs (valid if a,b > 1)
def beta_map(a, b):
    if a > 1 and b > 1:
        return (a-1)/(a+b-2)
    return np.nan

map0 = beta_map(a0, b0)  # undefined for Beta(1,1)
map1 = beta_map(a1, b1)  # 0.8
map2 = beta_map(a2, b2)  # 0.7

# MLEs
mle1 = h1/(h1+t1)        # 0.8
mle_all = (h1+h2)/(h1+h2+t1+t2)  # 14/20=0.7

theta = np.linspace(1e-4, 1-1e-4, 2000)
pdf0 = beta_pdf(theta, a0, b0)
pdf1 = beta_pdf(theta, a1, b1)
pdf2 = beta_pdf(theta, a2, b2)

fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), sharey=True)

# Prior
axes[0].plot(theta, pdf0, label=f"Beta({a0},{b0}) prior", color="tab:gray")
axes[0].set_title("Prior: Beta(1,1)")
axes[0].set_xlabel(r"$\theta$")
axes[0].set_ylabel("Density")
axes[0].grid(alpha=0.3)

# Posterior after Round 1
axes[1].plot(theta, pdf1, label=f"Posterior Beta({a1},{b1})", color="tab:blue")
axes[1].axvline(map1, color="tab:blue", linestyle="--", label=f"MAP={map1:.2f}")
axes[1].axvline(mle1, color="tab:orange", linestyle=":", label=f"MLE={mle1:.2f}")
axes[1].set_title(f"Posterior 1: Beta({a1},{b1})")
axes[1].set_xlabel(r"$\theta$")
axes[1].grid(alpha=0.3)
axes[1].legend()

# Posterior after Round 2
axes[2].plot(theta, pdf2, label=f"Posterior Beta({a2},{b2})", color="tab:green")
axes[2].axvline(map2, color="tab:green", linestyle="--", label=f"MAP={map2:.2f}")
axes[2].axvline(mle_all, color="tab:orange", linestyle=":", label=f"MLE (20 flips)={mle_all:.2f}")
axes[2].set_title(f"Posterior 2: Beta({a2},{b2})")
axes[2].set_xlabel(r"$\theta$")
axes[2].grid(alpha=0.3)
axes[2].legend()

plt.tight_layout()

# Save to images folder
os.makedirs("images", exist_ok=True)
out_path = os.path.join("images", "beta_updates.png")
plt.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"Saved figure to {out_path}")
plt.show()
```

Rendered figure:
![](./images/beta_updates.png)

If you cannot run the code, insert a screenshot placeholder:
{insert screenshot of prior and posterior Beta distributions across rounds here}

---

## 10) Worked Derivations (Step-by-Step)

- Likelihood for $h$ heads, $t$ tails:
  $$
  p(\mathbf{x}\mid \theta)=\theta^{h}(1-\theta)^t.
  $$

- Posterior with uniform prior ($\alpha=\beta=1$):
  $$
  p(\theta\mid \mathbf{x}) \propto \theta^{h}(1-\theta)^{t} \cdot 1 = \theta^{h}(1-\theta)^{t}.
  $$
  Recognize as $\text{Beta}(h+1, t+1)$.

- Normalizing constant for Round 1:
  $$
  p(\theta\mid \mathbf{x})=\frac{\theta^{8}(1-\theta)^2}{B(9,3)},\quad
  B(9,3)=\frac{\Gamma(9)\Gamma(3)}{\Gamma(12)}=\frac{8!\,2!}{11!}.
  $$

- MAP via derivative (Round 2):
  $$
  \ell(\theta)=14\ln\theta+6\ln(1-\theta)
  \Rightarrow \frac{d\ell}{d\theta}=\frac{14}{\theta}-\frac{6}{1-\theta}=0
  \Rightarrow 14(1-\theta)=6\theta \Rightarrow \theta=0.7.
  $$

---

## 11) Practical Notes

- Order of flips does not matter for the Bernoulli likelihood; only $h$ and $t$ matter.
- Sequential vs. batch updating produce the same posterior for conjugate models (like Beta–Bernoulli).
- Covariates or time trends would break i.i.d. assumptions and require different modeling.

---

## 12) Practice Exercises

1) Start with $\theta \sim \text{Beta}(2,2)$ and observe $h=3$, $t=1$.  
   - Compute the posterior parameters, mean, and MAP.

2) Suppose you first observe $h=5$, $t=5$ and then $h=4$, $t=1$.  
   - Show that sequential updating equals a single batch update.

3) Derive the posterior predictive probability that the next flip is heads after Round 2.  
   - Hint: For Beta–Bernoulli, $P(\text{head next}\mid \text{data})=\dfrac{\alpha'}{\alpha'+\beta'}$ with $\alpha',\beta'$ the posterior parameters.

4) Prove that with prior $\text{Beta}(\alpha,\beta)$ the MAP is $(\alpha-1)/(\alpha+\beta-2)$ when $\alpha,\beta>1$.

5) Explore the sensitivity of MAP to the prior by comparing $\text{Beta}(1,1)$ vs. $\text{Beta}(4,2)$ for the same Round 1 data.

---

## 13) Key Takeaways

- Bayes’ theorem updates beliefs by combining the likelihood and the prior; for Bernoulli data with a Beta prior, the posterior is also Beta.
- With a uniform prior, MAP equals MLE; with informative priors, MAP shifts toward prior beliefs.
- As data grows, MAP and MLE typically converge (under regularity conditions).
- Sequential and batch updates are equivalent in conjugate settings like Beta–Bernoulli.
- Normalizing constants can be ignored for MAP because they do not affect the argmax.

---

## References
- [Beta distribution](https://en.wikipedia.org/wiki/Beta_distribution)
- [Conjugate prior](https://en.wikipedia.org/wiki/Conjugate_prior)
- [Maximum a posteriori estimation](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation)

---

**Next:** [Beta-Binomial Predictive Distribution](./beta_binomial_predictive.md)