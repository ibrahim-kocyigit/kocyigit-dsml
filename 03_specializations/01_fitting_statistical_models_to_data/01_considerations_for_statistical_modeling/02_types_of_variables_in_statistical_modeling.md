# 2. Types of Variables in Statistical Modeling

## 2.1. Review of Variable Types

### 2.1.1. Categorical Variables
* Take on a small number of discrete values
* **Examples:** gender, race/ethnicity, political party preference, region, binary indicators
* **Key Question:** Are the categories ordered or simply discrete values?

### 2.1.2. Continuous Variables
* Take on many possible values
* **Examples:** height, age, income, blood pressure
* **Key Questions:**
  * What does the distribution look like?
  * What's the shape, center, and spread?
  * Is the variable normally distributed?

## 2.2. Key Dichotomy in Modeling: Dependent vs. Independent Variables

### 2.2.1. Dependent Variables (DVs)
* **Also called:** outcome variables, response variables, endogenous variables, variables of interest
* **Definition:** The variables we are interested in modeling
* **Objective:** Model distributional features of DVs as a function of independent variables
* The distributions of dependent variables **depend** on the values of independent variables

### 2.2.2. Independent Variables (IVs)
* **Also called:** predictor variables, covariates, regressors, exogenous variables
* **Definition:** Variables used to predict values on the dependent variables
* **Objective:** Examine distributions of DVs **conditional on** the values of IVs

## 2.3. Modeling Dependent Variables

* Research questions define what the DV is and what the IVs are
* Process involves:
  1. Selecting a reasonable distribution for the DV
  2. Defining the parameters of that distribution as functions of the IVs

**Example:** Assume blood pressure is normally distributed, where:
- Mean blood pressure depends on: age, BMI, and gender
- These three variables serve as independent variables

## 2.4. Characteristics of Independent Variables

### 2.4.1. Types of IVs:
* **Manipulated:** Assigned by investigator (e.g., treatment vs. control in randomized experiments)
* **Observed:** Simply measured in observational studies

### 2.4.2. Implications for Inference:
* **Randomized experiments:** More power for **causal inference**
* **Observational studies:** Focus on **describing relationships** (causal inference more difficult)

### 2.4.3. Handling Different Types of IVs:
* **Continuous IVs:** Estimate functional relationships (e.g., curvilinear relationship between age and test performance)
* **Categorical IVs:** Compare groups defined by categories
  * **Best practice:** Avoid estimating functional relationships when numeric codes have no inherent meaning
  * **Example:** Race coded as 1,2,3,4,5 - these numbers are arbitrary labels

## 2.5. Control Variables and Confounding

### 2.5.1. The Confounding Problem
* In observational studies, groups may not be balanced on other variables
* **Example:** Males generally weigh more than females
* If analyzing gender's relationship with a weight-related DV, weight becomes a **confounding variable**

### 2.5.2. Solution: Include Control Variables
* Add confounding variables as additional independent variables
* **Purpose:** "Adjust for" or "control for" the confounding variable
* **Interpretation:** Estimate relationship between primary IV and DV **given a fixed value** of the control variable

**Example:** To study gender-blood pressure relationship:
- Include weight as a control variable
- Estimate: "Given the same weight, what's the difference in blood pressure between males and females?"

## 2.6. Missing Data Considerations

### 2.6.1. Listwise Deletion
* **Default in most software** (including Python)
* Cases with **any missing data** on **any variable** used in the model are dropped entirely
* **Risk:** If dropped cases are systematically different, estimates may be **biased**

### 2.6.2. Handling Missing Data
1. **Compare missing vs. non-missing cases** on fully observed variables
   - Use techniques to check for systematics differences (e.g., Chi-Square tests)
2. **Consider imputation** if evidence of systematic missingness
   - Predict missing values using other variables in dataset
