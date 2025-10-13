# 6. Plotting Predictions and Prediction Uncertainty

## The Importance of Visualizing Uncertainty

- Most statistical modeling focuses on estimating the **mean function** (point estimates)
- **Visualization of uncertainty** is often as important, or more important, than the prediction itself
- Never blindly fit models without examining standard errors and uncertainty

## A Cautionary Tale: Two Datasets, Same Model

### The Scenario
- Two different datasets with identical linear regression results:
  - **Equation:** $y = a + bx$
  - **Parameter estimates:** $\hat{a} = 5.43$, $\hat{b} = 2.97$ (same for both datasets)

### The Critical Difference

![](./images/0601.png)

**Dataset 1:** Points cluster tightly around regression line  
**Dataset 2:** Points show wide dispersion around regression line

## Key Insight: Same Estimates, Different Uncertainties

### Prediction Uncertainty Matters
- Both models yield identical point predictions
- **Uncertainty bands** reveal dramatically different stories:
  - **Dataset 1:** Narrow confidence bands → High certainty about slope
  - **Dataset 2:** Wide confidence bands → Low certainty about slope

![](./images/0601.png)

### Practical Implications
If prediction tolerance is "plus or minus 10":
- **Dataset 1:** Comfortable making predictions
- **Dataset 2:** Hesitant to make predictions due to high uncertainty

## Tools for Assessing Uncertainty

### Method 1: Plot Your Data
- **Visual inspection** of point dispersion around regression line
- Examine **confidence bands** for slope parameters
- Direct visualization of prediction uncertainty

### Method 2: Examine Standard Errors
**Standard errors** quantify uncertainty in parameter estimates:

| Parameter | Dataset 1 SE | Dataset 2 SE |
|-----------|--------------|--------------|
| Intercept ($a$) | 0.92 | 3.36 |
| Slope ($b$) | 0.15 | 0.56 |

**Interpretation:** Smaller standard errors → Better parameter resolution → More reliable predictions

## Statistical Interpretation of Standard Errors

### Definition
- Given that model assumptions are met, **standard errors** indicate how far we expect our estimates to deviate from the true parameter values

### Key Points
- Every statistical model has different methods for calculating standard errors
- Always verify how uncertainty is calculated in your chosen modeling approach
- High variance in estimates suggests caution in prediction

## Best Practices for Modeling

#### 1. Always Plot Prediction Bounds
- Visualize uncertainty intervals alongside point estimates
- Essential for proper inference and decision-making

#### 2. Check Data Variance
- Plot your data to assess point dispersion
- Visual inspection can reveal issues not apparent from summary statistics alone

#### 3. Determine Estimate Variance
- Calculate and examine standard errors for all parameters
- Use caution with models showing high variance in parameter estimates

## The Signal vs. Noise Distinction

### Critical Modeling Principle
> "We want to make sure that we're modeling signal, not just noise"

**High variance estimates** may indicate:
- Insufficient data
- Poor model specification
- High inherent variability in the process
- Model capturing random noise rather than true relationships

### Ideal Scenario Preference
Always prefer the scenario with **lower variance estimates** (like Dataset 1) when making predictions, as it provides:
- Better parameter resolution
- More reliable predictions
- Greater confidence in model conclusions

---

**Next:** []()