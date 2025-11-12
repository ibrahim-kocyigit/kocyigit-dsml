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

Logistic Regression solves this by taking the output of a linear equation and passing it through a special "squashing" function called the **Sigmoid function** (or logistic function).

#### Linear Equation:

$$
z = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n
$$ 

#### Sigmoid Function:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

The sigmoid function takes any real number $z$ and maps it to a value between 0 and 1, which can be interpreted as a probability.

<img src="./images/1102.png" alt="Sigmoid Function Curve" width="500"/>

The output, $\hat{p} = \sigma(z)$, is our predicted **probability**.

$$
\hat{p} = P(y=1 | x)
$$

This is read as "the probability that the target `y` is 1, given the input features `X`."

## 3. Key Assumptions of Logistic Regression

Logistic Regression has its own set of assumptions, which are different from Linear Regression.

1. **Binary Outcome:** The target variable is binary or dichotomous. Logistic regression is designed for 2-class problems. (For more than two classes, you would use its extension, Softmax Regression).

2. **Independence of Observations:** The observations in the dataset are independent of each other. This is the same as in Linear Regression and is mainly a concern for time-series data.

3. **Linearity of Log-Odds:** This is the key assumption. Logistic Regression does not assume a linear relationship between the features and the target variable. Instead, it assumes a linear relationship between the features and the **log-odds** of the outcome. The log-odds is the logarithm of the odds ratio: $log(\frac {p}{(1-p)})$.