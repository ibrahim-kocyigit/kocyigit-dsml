# Bayesian Approaches Case Study: Part III

## 1. The Intuitive Idea: Fixing a Flawed Model

In Part II, we built a simple linear model and, through a series of diagnostic checks, found it to be flawed. It systematically mispredicted certain groups and failed to capture the full shape of the data.

This lecture is about **model iteration**. We will take the lessons learned from our first attempt and build a more complex, and hopefully more accurate, model. This process of dignosing, improving, and re-evaluating is the very essence of applied statistical modeling. As the saying goes, "All models are wrong, but some are useful." Our goal is to make our model *more useful*.

## 2. The Roadmap for Improvement: The Two Key Upgrades

Based on the deficiencies we identified, we will make two major upgrades to our model.

### Upgrade 1: Add a Hierarchical (Multilevel) Structure
* **The Problem:** Our first model was a "one-size-fits-all" approach, assuming the relationship between a mother's IQ and her child's IQ was the same for everyone.
* **The Solution:** We will now allow this relationship to vary across different groups of mothers. We'll create six distinct groups by combining two variables:
    1. `momHS`: Whether the mother attended high school (Yes/No).
    2. `momIQ`: Binned into three levels (Low: <85, Medium: 85-115, High: >115).
* **The Effect:** Our new model will fit a separate intercept (`β₀`) and separate slopes (`β₁`, `β₂`) for each of these six groups. This is a **hierarchical model**.

### Upgrade 2: Use a Skew-Normal Error Distribution
* **The Problem:** Our first model assumed normally distributed errors, which caused it to completely miss the "left tail" of low-IQ children in the real data.
* **The Solution:** We will replace the `Normal` distribution for our model's errors with a `Skew-Normal` distribution. This distribution has an extra parameter that allows it to be non-symmetrical, giving the model the flexibility to capture the observed left-skew in the data.

<img src="./images/0701.png" alt="" width="600"/>

## 3. Conceptualizing the Hierarchical Model
