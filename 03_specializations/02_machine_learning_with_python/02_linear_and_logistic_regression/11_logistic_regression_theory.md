# Logistic Regression

## 1. The Intuitive Idea: Predicting a Probability for Yes/No Questions

So far, we've used regression to predict continuous values (like the price of a house). But what if we want to answer a "yes" or "no" question?
* Will a customer *churn* or *not churn*?
* Is an email *spam* or *not spam*?
* Is a tumor *malignant* or *benign*?

This is a **classification** problem. **Logistic Regression** is a fundamental machine learning algorithm used for **binary classification** (problems with two possible outcomes, typically represented as 0 and 1).

Instead of predicting the class directly, logistic regression predicts the **probability** that an observation belongs to the positive class (class '1').

## 2. The Mathematics: The Sigmoid Function

If we try to fit a standard linear regression line to a binary (0/1) outcome, the line will predict values below 0 and above 1, which makes no sense for a probability. 

<img src="./images/1101.png" alt="Linear Regression on a classification problem" width="600"/>

L