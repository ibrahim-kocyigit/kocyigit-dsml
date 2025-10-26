# Bayesian Approaches Case Study: Part I

## 1. The Intuitive Idea: Beyond a Single Answer

In the Frequentist world, we use methods like Maximum Likelihood to find the **single best value** for each model parameter (e.g., the slope is `0.47`).

The Bayesian framework offers a more flexible and powerful alternative. Instead of a single point estimate, it produces a **full probability distribution** for every parameter in the model. This inherent flexibility allows Bayesian models to naturally handle a wide range of complex problems within a single, unified framework, including:
* Variable selection and regularization (similar to Lasso/Ridge regression).
*  Models where the number of parameters exceeds the number of observations.
* Complex dependency and hierarchical structures (multilevel models).

This case study will walk through the Bayesian workflow to provide an intuition for how these models are built and interpreted, focusing on the practical application rather than the deep mathematical theory.

## 2. The Bayesian Modeling Workflow
A Bayesian analysis can be broken into three fundamental steps, which form a cyclical process of learning:

1. **Establish a Belief (Set Up the Model):** This is where we define our initial understanding of the problem. It involves two key components:
    * **The Likelihood:** This is the model structure we assume for the data (e.g., a linear regression model).
    * **The Priors:** We must assign a probability distribution to *every single parameter* in our model, representing our belief about the parameter *before* seeing the data.
2. **Update the Belief (Fit the Model to Data):** We use the collected data and the rules of probability (specifically Bayes' Theorem) to update our initial priors. This process generates the **posterior distribution** for each parameter. A critical part of this step is model checking, ensuring the fitted model is a reasonable representation of the data.

3. **Evaluate and Use the Belief (Interpret the Posterior):** We analyze the resulting posterior distributions to answer our research questions, make predictions, and quantify our uncertainty. This updated belief (the posterior) can then serve as the prior for a future analysis.

## 3. Case Study: Predicting a Child's IQ

To make this process concrete, we will analyze a dataset from the **National Longitudinal Survey of Youth (NLSY)**.

* **Dataset:** 434 observations.
* **Research Question:** Can we predict a child's IQ score based on characteristics of their mother?
* **Independent Variables:** `momIQ` (mother's IQ), `momAge` (mother's age at birth), and `momHS` (whether the mother attended high school).

For simplicity, we will start with a basic linear regression model, excluding the `momHS` variable for now.

$$
\text{kidScore} = \beta_0 + \beta_1 \cdot \text{momIQ} + \beta_2 \cdot \text{momAge} + \epsilon
$$

## 4. Step 1 in Practice: Setting the Priors

This is the most significant departure from a Frequentist analysis. We must explicitly state our beliefs about each parameter (`β₀`, `β₁`, `β₂`, and the error term `ε`) in the form of a probability distribution.

**The Goal:** To express our initial knowledge (or lack thereof) about the parameters. If we are very uncertain, we use a "weak" or "uninformative" prior with a large variance. If we have strong prior knowledge from previous studies, we can use a "strong" or "informative" prior with a small variance.

Here are the priors chosen for this analysis, along with the relationship:

*   **For the Intercept (`β₀`):**
    *   **Prior:** `Normal(mean=0, sd=20)`
    *   **Reasoning:** The predictor variables (`momIQ`, `momAge`) will be centered before modeling. When predictors are centered, the intercept represents the mean outcome when all predictors are at their average value. A prior centered at 0 is a natural starting point, and the large standard deviation (`sd=20`) makes this a **weak prior**, meaning we are very uncertain and will let the data speak for itself.

*   **For the Mother's IQ Slope (`β₁`):**
    *   **Prior:** `Normal(mean=1, sd=5)`
    *   **Reasoning:** Our starting hypothesis is that a child's IQ is strongly related to their mother's IQ. A slope of `1` would mean a one-to-one relationship. We express our uncertainty about this with a moderately large standard deviation (`sd=5`). This is still a **weakly informative prior**; it allows the data to easily overwhelm our initial guess but gently "regularizes" the estimate, discouraging extreme values.

*   **For the Mother's Age Slope (`β₂`):**
    *   **Prior:** `Normal(mean=0, sd=5)`
    *   **Reasoning:** Our initial belief is that the mother's initial age at birth has little to no effect on the child's IQ *after* accounting for the mother's own IQ. We center our prior at `0`. Again, we use a standard deviation of `5` to express some uncertainty, allowing the data to pull the estimate away from zero if there is a real effect.

*   **For the Model Error (`ε`):**  
    * We also need a prior for the overall error of the model (how far predictions are from the real data). This is typically a distribution defined only for positive values, like a Half-Cauch distribution.

#### Subjectivity of Priors: A Feature, Not a Bug
A common criticism of Bayesian analysis is that choosing priors is subjective. The Bayesian framework forces the analyst to be transparent about their assumptions. By stating priors explicitly, our initial beliefs are brought to the forefront of the analysis, where they can be debated and challenged. An analyst with different domain expertise might choose different priors, and the framework allows for this.

## 5. Technical Considerations
* **Computation:** The mathematics behind Bayesian updating can quickly become intractable. Modern Bayesian analysis relies on specialized software (like **STAN**) that uses sophisticated sampling algorithms (like **Markov Chain Monte Carlo, or MCMC**) to approximate the posterior distributions. Instead of a perfect mathematical curve, our result is often a histogram built from thousands of samples, which serves as an excellent approximation of the true posterior.
* **Data Centering:** The predictors were centered before fitting. This is a common and recommended practice in regression modeling as it makes the intercept term more interpretable.

---

**Next:** [Bayesian Approaches Case Study: Part II](./06_bayesian_approaches_case_study_part_2.md)