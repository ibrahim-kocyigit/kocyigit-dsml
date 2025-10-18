# Multilevel Models: Introduction

## Introduction to Dependent Data

### The Need for Specialized Models
- **Previous focus:** Regression models for **independent observations**
- **This week:** Models for **dependent data** where observations are correlated
- **Sources of correlation:**
  - **Clustered data:** Observations from same neighborhood, school, clinic
  - **Longitudinal data:** Repeated measurements from same individuals over time

### Why Correlation Matters
- People in same cluster share characteristics (attitudes, socioeconomic status)
- Repeated measurements from same person are naturally correlated
- Models must **reflect these correlations** to provide valid inference

## What are Multilevel Models?

### Core Concept
**Multilevel models** are a general class of statistical models for dependent data where:
- Regression coefficients are allowed to **randomly vary** across higher-level clusters
- We estimate both **fixed effects** (overall relationships) and **random effects** (cluster-specific variations)

### Key Distinction from Previous Models
| **Standard Regression** | **Multilevel Models** |
|-------------------------|----------------------|
| Fixed coefficients for all observations | Coefficients vary across clusters |
| Assumes independent observations | Explicitly models within-cluster correlation |
| One-level structure | Hierarchical data structure |

## 3. Mathematical Formulation

### Level 1 Equation (Observation Level)
\[
y_{ij} = \beta_{0j} + \beta_{1j}x_{ij} + e_{ij}
\]
where:
- $y_{ij}$: Dependent variable for observation $i$ in cluster $j$
- $\beta_{0j}$, $\beta_{1j}$: **Cluster-specific** coefficients (random)
- $x_{ij}$: Predictor variable
- $e_{ij}$: Observation-level error term

### Level 2 Equations (Cluster Level)
**For random intercept:**
\[
\beta_{0j} = \gamma_{00} + u_{0j}
\]
**For random slope:**
\[
\beta_{1j} = \gamma_{10} + u_{1j}
\]

### Combined Model
\[
y_{ij} = \underbrace{\gamma_{00} + \gamma_{10}x_{ij}}_{\text{Fixed part}} + \underbrace{u_{0j} + u_{1j}x_{ij} + e_{ij}}_{\text{Random part}}
\]

## 4. Random Effects Interpretation

### Distributional Assumptions
- **Random effects:** $u_{0j} \sim N(0, \tau_0^2)$, $u_{1j} \sim N(0, \tau_1^2)$
- **Errors:** $e_{ij} \sim N(0, \sigma^2)$

### Variance Components
- $\tau_0^2$: **Between-cluster variance** in intercepts
- $\tau_1^2$: **Between-cluster variance** in slopes
- $\sigma^2$: **Within-cluster variance** (residual error)

## 5. Expanded Inference Capabilities

### Types of Inferences Enabled
1. **Fixed effects:** Relationships between predictors and outcomes (same as standard regression)
2. **Variance components:** How much coefficients vary across clusters
3. **Explanatory modeling:** Using cluster-level predictors to explain between-cluster variance

### Example Research Questions
- "How much of the unexplained variance in patient satisfaction is due to hospital characteristics?"
- "Do different drug users follow different long-term trends in substance use?"

## 6. When to Use Multilevel Models

### Four Necessary Conditions
1. **Clustered data structure:** Multiple correlated observations per cluster
2. **Random sampling of clusters:** Clusters represent larger population (not fixed categories like gender)
3. **Need to model within-cluster correlation:** Study design creates dependencies
4. **Explicit interest in between-cluster variance:** Want to estimate how much coefficients vary

### Inappropriate Uses
- Fixed categorical variables (gender, race) as "clusters"
- When clusters represent entire population of interest
- When within-cluster correlation is negligible

## 7. Advantages of Multilevel Models

### Statistical Efficiency
- Estimate **one variance parameter** instead of many cluster-specific coefficients
- Particularly advantageous with **many clusters**

### Shrinkage Effect
- Clusters with **smaller sample sizes** have less influence on variance estimates
- Estimates "shrink" toward overall mean, providing more stable inference
- Prevents small clusters from having disproportionate influence

## 8. Explaining Between-Cluster Variance

### Adding Cluster-Level Predictors
**Extended Level 2 Equations:**
\[
\beta_{0j} = \gamma_{00} + \gamma_{01}T_j + u_{0j}
\]
\[
\beta_{1j} = \gamma_{10} + \gamma_{11}T_j + u_{1j}
\]
where $T_j$ is a cluster-level predictor

### Interpretation
- $\gamma_{01}$, $\gamma_{11}$: How cluster-level predictors explain between-cluster variance
- Can test hypotheses about these parameters
- Enables statements like: "45% of between-subject variance is explained by predictor T"

## 9. Key Concepts Summary

### Multilevel Model Components
- **Fixed effects:** Overall average relationships ($\gamma$ parameters)
- **Random effects:** Cluster-specific deviations ($u$ parameters)
- **Variance components:** Quantify between-cluster variability ($\tau^2$ parameters)

### Unique Capabilities
1. **Model correlation** due to study design
2. **Estimate between-cluster variance** in coefficients
3. **Explain between-cluster variance** with cluster-level predictors
4. **Handle unbalanced data** efficiently via shrinkage

## 10. Looking Ahead

### Next Topics
1. **Visualization** of multilevel models
2. **Implementation** for different variable types (continuous, binary, count)
3. **Examples** and applications
4. **Alternative approaches** for dependent data without random effects

### Important Reminder
Multilevel models require **explicit research interest** in estimating between-cluster variance. Other approaches exist for dependent data when this specific interest is absent.