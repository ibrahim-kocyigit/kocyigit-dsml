# Bayesian Statistics: Full Worked Example

We will work through a complete Bayesian update with coin flips, starting from a non-informative prior and then updating with additional data. We will:
- Derive the likelihood for observed coin flips.
- Choose a prior and compute the posterior using Bayes’ theorem.
- Compare MAP vs. MLE.
- Perform sequential updating with a second batch of data.

## Setup: Model, Data, and Bayes’ Theorem

- **Parameter** (unknown coin bias): $\theta \in (0,1)$.
- **Data:** $\mathbf{x} = (x_1,\dots,x_n)$ where each $x_i \in \{0,1\}$.
- **Conditional model:** $x_i \mid \theta \sim \text{Bernoulli}(\theta)$, independent across flips.
- **Likelihood** for $h$ heads and $t$ tails (with $h+t=n$):

$$
p_{X|\Theta=\theta}(x)=\theta^{h}(1-\theta)^{t}
$$

- Bayes’ theorem (continuous $\theta$, discrete $\mathbf{x}$):  

$$
f_{\Theta|X=x}(\theta) = \frac{p_{X|\Theta=\theta}(x) \, f_\Theta(\theta)}{p_X(x)}
$$
- The proportionality version of the Bayes' Theorem which omits the denominator (_because it does not affect the location of the maximum (MAP). Likewise, constant priors do not change the argmax._):  

$$
f_{\Theta|X=x}(\theta) \propto p_{X|\Theta=\theta}(x) \, f_\Theta(\theta)
$$

**where...**  
- $\Theta$ is the random variable for the parameter (continuous)
- $X$ is the random variable for the data (discrete)
- $f_{\Theta|X=x}(\theta)$ is the posterior density of $\theta$ given $X = x$
- $p_{X|\Theta=\theta}(x)$ is the likelihood (probability of data $x$ given parameter $\theta$)
- $f_\Theta(\theta)$ is the prior density of $\theta$
- $p_X(x)$ is the marginal probability of the data (normalizing constant)
- $\propto$ means “is proportional to.”


## Prior Choice and Conjugacy

- Choose a non-informative (uniform) prior on $(0,1)$:  

$$
\theta \sim \text{Beta}(\alpha,\beta)\quad \text{with } \alpha=\beta=1.
$$
- Conjugacy fact (Beta–Bernoulli):
  -  If $\theta \sim \text{Beta}(\alpha,\beta)$ and observe $h$ heads, $t$ tails,
  - Then posterior $\theta \mid \mathbf{x} \sim \text{Beta}(\alpha+h,\beta+t)$.

- Beta pdf:   

$$
\text{Beta}(a,b)\text{ pdf: } f(\theta)=\frac{\theta^{a-1}(1-\theta)^{b-1}}{B(a,b)}
$$

- Normalizing constant:  

$$
\quad
B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}
$$

## Round 1: 10 Flips (8 Heads, 2 Tails)

- Data: $h=8$, $t=2$, $n=10$.
- Prior: $\text{Beta}(1,1)$.
- Posterior:  

$$
\theta \mid \mathbf{x}_{1:10} \sim \text{Beta}(1+8,\,1+2)=\text{Beta}(9,3).
$$

- Posterior pdf (up to constant):  

$$
p(\theta \mid \mathbf{x}_{1:10}) \propto \theta^{8}(1-\theta)^2.
$$

(Normalizing constant here is... 

$$
1/B(9,3)=\dfrac{11!}{8!\,2!}
$$

... consistent with $8!\cdot 2!/11!$ in the denominator.)

### Posterior summaries

#### Mean:
$$
E[\theta \mid \mathbf{x}] = \frac{\alpha}{\alpha + \beta}
$$
For $\alpha = 9$, $\beta = 3$:
$$
E[\theta \mid \mathbf{x}] = \frac{9}{9 + 3} = \frac{9}{12} = 0.75
$$

#### Variance:
$$
\{Var}[\theta \mid \mathbf{x}] = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}
$$

For $\alpha = 9$, $\beta = 3$:  

$$
\{Var}[\theta \mid \mathbf{x}] = \frac{9 \cdot 3}{(12)^2 \cdot 13} = \frac{27}{1872} \approx 0.0144
$$

#### MAP (mode, for $\alpha > 1$, $\beta > 1$):
$$
\text{Mode}[\theta \mid \mathbf{x}] = \frac{\alpha - 1}{\alpha + \beta - 2}
$$
For $\alpha = 9$, $\beta = 3$:
$$
\text{Mode}[\theta \mid \mathbf{x}] = \frac{9 - 1}{9 + 3 - 2} = \frac{8}{10} = 0.8
$$

> Note: The mean, variance, and MAP formulas apply to any Beta($\alpha$, $\beta$) posterior, not just this specific case.

Calculation of MAP via calculus (argmax of log-posterior):  

$$
\ell(\theta) = (h)\ln\theta + (t)\ln(1-\theta)=8\ln\theta + 2\ln(1-\theta) 
$$

$$
\Rightarrow \frac{d\ell}{d\theta}=\frac{8}{\theta}-\frac{2}{1-\theta}=0
$$

$$
\Rightarrow 8(1-\theta)=2\theta 
$$

$$
\Rightarrow \theta=0.8
$$

#### MLE comparison:
$$
\hat{\theta}_{\text{MLE}} = \frac{h}{n} = \frac{8}{10} = 0.8 = \hat{\theta}_{\text{MAP}}
$$

> **Conclusion:** When you use a uniform prior, the Bayesian MAP estimate for $\theta$ (coin bias) matches the frequentist MLE, since the prior doesn’t influence the result.

## Round 2: Add 10 Flips (6 Heads, 4 Tails)

Sequential update uses the Round 1 posterior as the new prior.

- New data: $h=6$, $t=4$.
- Prior now: $\text{Beta}(9,3)$.
- Posterior:  

$$
\theta \mid \mathbf{x}_{1:20} \sim \text{Beta}(9+6,\,3+4)=\text{Beta}(15,7).
$$

- Posterior pdf (up to constant):  

$$
p(\theta \mid \mathbf{x}_{1:20}) \propto \theta^{14}(1-\theta)^6.
$$

### Posterior summaries
#### Mean: 
$$
E[\theta \mid \mathbf{x}]=\dfrac{15}{15+7}=\dfrac{15}{22}\approx 0.6818
$$

#### Variance:
$$
Var[\theta \mid \mathbf{x}]=\dfrac{15\cdot 7}{(22)^2(23)}=\dfrac{105}{11132}\approx 0.0094
$$

#### MAP: 
$$
\dfrac{15-1}{15+7-2}=\dfrac{14}{20}=0.7
$$

#### Frequentist comparison:
- Over all 20 flips, $h=14$, $n=20 \Rightarrow \hat{\theta}_{\text{MLE}}=0.7$.
- Batch vs. sequential: $\text{Beta}(1+14,1+6)=\text{Beta}(15,7)$ matches the sequential result.

## Key Takeaways

- Bayes’ theorem updates beliefs by combining the likelihood and the prior; for Bernoulli data with a Beta prior, the posterior is also Beta.
- With non-informative (uniform) prior, MAP = MLE.
- With informative priors, MAP deviates from MLE, especially with small sample sizes.
- As $n$ grows, MAP and MLE typically converge (under regularity conditions).
- Order of flips does not matter when we try to estimate the coin bias (parameter $\theta$); only $h$ and $t$ matter. When updating the posterior (using Bayes’ rule), the binomial coefficient appears in both the likelihood and the marginal likelihood (normalization), so it cancels out in calculations where we only care about 
θ (e.g., estimating posterior summaries or MAP).
- Sequential vs. batch updating produce the same posterior for conjugate models (like Beta–Bernoulli).
- Covariates or time trends would break i.i.d. assumptions and require different modeling.
- Normalizing constants can be ignored for MAP because they do not affect the argmax.

**Next:** [Relationship between MAP, MLE and Regularization](./12_relationship_between_map_mle_and_regularization.md)