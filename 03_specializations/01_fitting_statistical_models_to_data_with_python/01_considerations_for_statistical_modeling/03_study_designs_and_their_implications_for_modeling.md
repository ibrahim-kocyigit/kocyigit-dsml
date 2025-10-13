# Study Designs and Their Implications for Modeling

## Study Designs

Study design refers to the planning and structuring of data collection and analysis in research. It ranges from exploratory analysis of available data to highly planned, hypothesis-driven studies.

### Examples of Study Design in Different Fields

- **Clinical trials** (medicine)
- **Reliability and quality assurance** (manufacturing)
- **Observational studies** (human health)
- **Public opinion surveys**
- **Administrative or incidental data studies**
- **Market research**
- **Agricultural field trials**

## Types and Classifications of Study Design

Studies may not fit perfectly into one category, but some key distinctions include:

### 1. Exploratory vs. Confirmatory Studies

- **Exploratory:**  
  - Analyze data without a pre-specified hypothesis.
  - Useful for discovering patterns, but risk of overfitting, multiple testing, and p-hacking.
- **Confirmatory:**  
  - Start with a specific, falsifiable hypothesis.
  - Data is collected and analyzed to test this hypothesis.

### 2. Comparative vs. Non-Comparative Studies

- **Comparative:**  
  - Aim to contrast two or more groups or quantities.
  - Examples: Comparing crop yields with different fertilizers, voter preferences, or ad click rates.
- **Non-Comparative:**  
  - Focus on estimating or predicting absolute quantities.
  - Examples: Predicting stock prices, estimating blood pressure reduction after treatment.

### 3. Observational vs. Experimental Studies

- **Observational:**  
  - Data arises naturally; groups are formed by self-selection.
  - Example: Comparing health outcomes between smokers and non-smokers.
  - Used when random assignment is impractical or unethical.
- **Experimental:**  
  - Researcher assigns treatments or interventions to groups.
  - Example: Randomly assigning fertilizer to plots in a field, or exposing users to different versions of an ad.
  - Involves manipulation and random assignment.

## Key Concepts

- **Random Assignment:**  
  - Central to experiments; helps ensure groups are comparable.
- **Self-Selection:**  
  - Common in observational studies; can introduce bias.
- **Bias:**  
  - Systematic errors in measurement or sampling; more likely in observational studies.
- **Power Analysis:**  
  - Used to assess whether a study is likely to detect meaningful effects, given its design and sample size.


## Core Principle

**Different study designs generate different types of data**, and this has **critical implications** for the models we fit. Understanding **how data were generated** is essential before fitting statistical models.

## Common Study Designs and Their Modeling Implications

### Simple Random Samples (SRS)

* **Key Property:** Observations are **Independent and Identically Distributed (i.i.d.)**
* **Characteristics:**
  - All values are independent of each other
  - All values arise from identical distribution
  - Zero correlation between any two randomly selected observations

**Example:** Measuring happiness scale in SRS
- Assume happiness $\sim N(\mu, \sigma^2)$ with independent observations
- Standard error calculations assume independence

**Advantage:** More unique statistical information → **Smaller standard errors** → More precise estimates

**Modeling Approach:** Can model differences between groups (e.g., different means by gender) while maintaining independence assumption **within groups**

### Clustered Samples

* **Examples:** Hospitals, clinics, schools, neighborhoods
* **Key Property:** Observations **within clusters are correlated**
  - Observations from same cluster tend to be similar

<img src="./images/0301.jpg" width="500">

**Example:** Happiness measurements from selected neighborhoods
- Observations within same neighborhood are correlated
- Must account for within-cluster correlation in models

**Implication:** Less unique independent information → **Higher standard errors**

**Modeling Approach:** Include additional parameters to capture within-cluster correlation

### Longitudinal Studies

* **Key Property:** Repeated measures from **same units over time** are correlated
* **Characteristics:**
  - Within-unit correlation across time points
  - Values for same individual tend to be consistently high/low
**Modeling Approach:** Must account for within-unit correlation, similar to clustered samples

<img src="./images/0302.png" width="500">


## Critical Dichotomy in Modeling

### Independent Data
* Observations completely independent of each other
* May or may not arise from common distribution
* **Examples:** Simple random samples

### Dependent Data
* Observations correlated due to study design features
* **Examples:** Clustered samples, longitudinal measurements
* **Requires:** Special modeling approaches to account for correlation

## Modeling Philosophy

> The **best possible model** should reflect important study design features that affect the distributional properties of our variables of interest.

**Key considerations when specifying models:**
1. Were observations generated independently?
2. Is there natural clustering in the data?
3. Are there repeated measurements over time?
4. How do these features affect correlation structure?

---

**Next:** [Objectives of Model Fitting: Inference vs. Prediction](./04_objectives_of_model_fitting--inference_vs_prediction.md)