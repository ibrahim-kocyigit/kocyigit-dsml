# Introduction to Regression

## 1. The Intuitive Idea: Predicting a Number

Regression is a fundamental technique in supervised machine learning. Its core purpose is to model the relationship between a set of input features and a **continuous target variable**.

In simple terms, regression helps us answer the question: **How much?** or **"What will the value be?"**

#### The Process
1. **Collect Data:** Gather a dataset with known features (input) and a known continuous target value (the "correct answer").
2. **Train a Model:** Use a regression algorithm to "learn" the mathematical relationship between the features and the target from this historical data.
3. **Make Predictions:** Use the trained model to predict the target value for new, unseen data where only the features are known.

#### Example: CO2 Emissions
* **Goal:** Predict the CO2 emissions of a new car.
* **Data:** A dataset of existing cars with features like `Engine Size`, `Number of Cylinders`, and `Fuel Consumption`, along with their known `CO2 Emissions`.
* **Prediction:** For a new car, you provide its `Engine Size` and `Cylinders`, and the model predicts its expected `CO2 Emissions`.

## 2. The Main Types of Regression
The complexity of a regression model can be categorized based on the number of input variables.

### Simple Regression
* **Definition:** Uses a **single independent variable** (feature) to predict the dependent (target) variable.
* **Example:** Predicting `CO2 Emissions` using *only* the `Engine Size`.
* **Sub-types:**  
    * **Simple Linear Regression:** Assumes a straight-line relationship between the input and the target.
    * **Simple Non-linear Regression:** Models a curved relationship between the input and the target.

### Multiple Regression
* **Definition:** Uses **more than one independent variable** (multiple features) to predict the target variable.
* **Example:** Predicting `CO2 Emissions` using `Engine Size`, `Number of Cylinders`, *and* `Fuel Consumption`.
* **Sub-types:**  
    * **Multiple Linear Regression:** Assumes a linear combination of the input features can predict the target.
    * **Multiple Non-linear Regression:** Models a more complex, non-linear relationship involving multiple features.

## 3. Real-World Applications of Regression

Regression is used whenever we need to estimate a continuous variable. It has a vast range of applications across many domains.

* **Business & Finance:**  
    * **Sales Forecasting:** Predicting a salesperson's yearly sales based on leads and customer history.
    * **Real Estate:** Estimating the price of a house based on its size, location, and number of bedrooms.
    * **Economics:** Predicting an individual's income based on their education, age, and years of experience.

* **Engineering & Industry:**  
    * **Predictive Maintenance:** Predicting when an industrial machine will require maintenance to prevent failures.

* **Environmental Science:**  
    * **Meteorology:** Estimating the amount of rainfall in a region based on temperature, humidity, and wind speed.
    * **Ecology:** Determining the probability and severity of wildfires based on environmental factors.

* **Healthcare:**  
    * **Epidemiology:** Predicting the spread of an infectious disease.
    * **Clinical Risk:** Estimating a patient's likelihood of developing diseases like diabetes or heart disease based on their health data.

## 4. A Glimpse at Regression Algorithms

There are many different regression algorithms, each with its own strengths and weaknesses. The choice of algorithm depends on the specific problem and the nature of the data.

* **Classical Statistical Models:**  
    * Linear Regression
    * Polynomial Regression
* **Modern Machine Learning Models:**
    * K-Nearest Neighbours (KNN)
    * Support Vector Machines (SVM)
    * Random Forest
    * XGBoost
    * Neural Networks

## 5. Summary
* **Regression** is a supervised learning technique used to predict a **continuous target value** based on one or more input features.
* **Simple Regression** uses one feature, while **Multiple Regression** uses multiple features. Both can model linear or non-linear relationships.
* Regression is a versatile and powerful tool with widespread applications in finance, healthcare, engineering, and many other fields.

---

**Next:** [Simple Linear Regression](./02_simple_linear_regression.md)
