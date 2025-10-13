# 4. Objectives of Model Fitting: Inference vs. Prediction

## 4.1. Two Main Objectives in Model Fitting

### 4.1.1. Objective 1: Making Inference
- **Focus:** Understanding relationships between variables in the dataset
- **Goal:** Test hypotheses and draw conclusions about population parameters
- **Key Question:** "Is there a significant relationship between X and Y?"

### 4.1.2. Objective 2: Making Predictions
- **Focus:** Forecasting future outcomes based on historical data
- **Goal:** Generate accurate forecasts for new observations
- **Key Question:** "What value of Y can we expect given specific values of X?"

## 4.2. Inference: Testing Relationships Between Variables

### 4.2.1. Example Revisited: Age vs. Test Performance
**Model:** Performance follows a quadratic relationship with age:

$\text{Performance} = a + b \cdot \text{Age} + c \cdot \text{Age}^2 + E$

...where $E\sim N(0, \sigma^2)$

**Parameter Estimates:**
- $\hat{a} = 5.11$ (SE = 0.10)
- $\hat{b} = 0.24$ (SE = 0.06) 
- $\hat{c} = -0.26$ (SE = 0.03)

Once we've calculated the parameter estimates we can...
- test hypotheses about whether parameters are equal to 0, or...
- form confidence intervals for these parameters to determine whether or not the value of 0 is contained within the confidence interval

### 4.2.2. Hypothesis Testing for Parameters

**Test Statistic Formula:**  

$$
t = \dfrac{\text{Estimate} - 0}{\text{Standard Error}}
$$

**Example Calculation for parameter $b$:**  

$$
t = \dfrac{0.24}{0.06} = 4.0
$$

**Interpretation:**
- A test statistic of 4.0 indicates the estimate is 4 standard errors above zero
- Very unlikely to observe such a large estimate if the null hypothesis ($b = 0$) were true
- **Conclusion:** Strong evidence to reject $H_0: b = 0$

### 4.2.3. Interpreting Parameter Significance

**Parameter a ($\hat{a} = 5.11$, $t = 51.1$):**
- Mean test performance when age equals the overall mean
- Significantly different from zero → Performance is nonzero at average age

**Parameter b ($\hat{b} = 0.24$, $t = 4.0$):**
- Initial rate of increase in test performance when standardized age = 0
- Positive and significant → Initial positive relationship with age

**Parameter c ($\hat{c} = -0.26$, $t = -8.67$):**
- Non-linear acceleration in performance as function of age
- Negative and significant → Performance decreases after initial acceleration
- **Key Insight:** If c were not significant, relationship would be linear rather than curvilinear

## 3. Prediction: Forecasting Future Outcomes

### Making Predictions from Fitted Model
**Prediction Equation:**

$$
\hat{\text{Performance}} = 5.11 + 0.24 \times \text{Age} - 0.26 \times \text{Age}^2
$$

**Example:** Predicting performance when standardized age = 1:
$\hat{\text{Performance}} = 5.11 + 0.24 \times 1 - 0.26 \times 1^2 = 5.09$

{{insert screenshot showing scatter plot with fitted quadratic curve and prediction at age=1 here}}

### Importance of Accounting for Uncertainty

**Key Points:**
1. All predictions have associated uncertainty
2. Poorer model fit → Greater prediction uncertainty
3. Including relevant predictors reduces uncertainty
4. Must report uncertainty when making predictions

**Comparison:**
- **Simple model** (no predictors): Same prediction for everyone, high uncertainty
- **Complex model** (with predictors): Different predictions based on X values, lower uncertainty

## 4. Critical Distinctions Between Objectives

| **Inference** | **Prediction** |
|---------------|----------------|
| Focus on parameter estimates | Focus on outcome forecasts |
| Test hypotheses about relationships | Generate point estimates and intervals |
| Interpret coefficients and significance | Assess prediction accuracy |
| Understand underlying mechanisms | Practical forecasting applications |

## 5. Looking Ahead

### Upcoming Topics:
1. **Estimation methods** for model parameters
2. **Hypothesis testing** and confidence intervals
3. **Prediction techniques** and uncertainty quantification
4. **Model assessment** and quality evaluation
5. **Frequentist vs. Bayesian inference** approaches

### Key Reminder:
Always assess overall quality of model fit regardless of whether primary objective is inference or prediction.