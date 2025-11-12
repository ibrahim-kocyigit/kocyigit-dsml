# Logistic Regression

## 1. The Intuitive Idea: Predicting a Probability for Yes/No Questions

So far, we've used regression to predict continuous values (like the price of a house). But what if we want to answer a "yes" or "no" question?
* Will a customer *churn* or *not churn*?
* Is an email *spam* or *not spam*?
* Is a tumor *malignant* or *benign*?

This is a **classification** problem. **Logistic Regression** is a fundamental machine learning algorithm used for **binary classification** (problems with two possible outcomes, typically represented as 0 and 1).

Instead of predicting the class directly, logistic regression predicts the **probability** that an observation belongs to the positive class (class '1'). It does this through a guided process of trial and error, where the model's objective is to find a set of parameters that minimizes its prediction error on the data it has seen.

## 2. The Mathematics: The Sigmoid Function

If we try to fit a standard linear regression line to a binary (0/1) outcome, the line will predict values below 0 and above 1, which makes no sense for a probability.

<img src="./images/1101.png" alt="Linear Regression on a classification problem" width="600"/>

Logistic Regression solves this by taking the output of a linear equation and passing it through a special "squashing" function called the **Sigmoid function** (or logistic function).

**Linear Equation:**  

$$
z = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n 
$$

**Sigmoid Function ($\sigma$):**  

$$
\sigma(z) = \frac{1}{1 + e^{-z}} 
$$

The sigmoid function takes any real number `z` and maps it to a value between 0 and 1, which can be interpreted as a probability.

<img src="./images/1102.png" alt="Sigmoid Function Curve" width="500"/>

The output, $\hat{p} = \sigma(z)$, is our predicted **probability**.  

$$
\hat{p} = P(y=1 | X) 
$$

This is read as "the probability that the target `y` is 1, given the input features `X`."

## 3. Key Assumptions of Logistic Regression

Logistic Regression has its own set of assumptions, which are different from Linear Regression.

1.  **Binary Outcome:** The target variable is binary or dichotomous. Logistic regression is designed for 2-class problems. (For more than two classes, you would use its extension, Softmax Regression).

2.  **Independence of Observations:** The observations in the dataset are independent of each other. This is the same as in Linear Regression and is mainly a concern for time-series data.

3.  **Linearity of Log-Odds:** This is the key assumption. Logistic Regression does not assume a linear relationship between the features and the target variable (`y`). Instead, it assumes a linear relationship between the features and the **log-odds** of the outcome. The log-odds is the logarithm of the odds ratio: `log(p / (1-p))`.

4.  **No High Multicollinearity:** The independent variables should not be highly correlated with each other. This is the same as in Multiple Linear Regression and can make the model's coefficients unstable and difficult to interpret.
    > **What to do if it's violated?**
    > *   Remove one of the highly correlated features.
    > *   Combine the correlated features into a single new feature.
    > *   Use regularization (L1 or L2), which is built into many logistic regression implementations.

## 4. How the Model is Trained

Training is an iterative process where the model "learns" the best parameters ($\theta$) by trying to minimize its prediction error. This follows a simple loop:
1. **Initialize Parameters:** Start with a random guess for the parameters ($\theta$).
2. **Make Predictions:** Use the current parameters and the sigmoid function to predict the probability for every observation.
3. **Measure the Error:** Compare the predicted probabilities to the actual classes using a **cost function** called **Log Loss**.
4. **Update the Parameters:** Adjust the parameters in a direction that reduces the error, using an algorithm called **Gradient Descent**.
5. **Repeat:** Continue this loop until the error is minimized or a set number of iterations is reached.

### The Cost Function: Log Loss (or Binary Cross-Entropy)
The Log Loss function measures how well the predicted probabilities match the actual class labels. It is designed to heavily penalize confident but wrong predictions.

The formula for Log Loss for a single observation is:
`Cost(ŷ, y) = -[ y * log(ŷ) + (1-y) * log(1-ŷ) ]`

*   **If the actual class is 1 (`y=1`):** The cost is `-log(ŷ)`. If our prediction `ŷ` is close to 1 (correct), the cost is low. If `ŷ` is close to 0 (incorrect), the cost is very high.
*   **If the actual class is 0 (`y=0`):** The cost is `-log(1-ŷ)`. If our prediction `ŷ` is close to 0 (correct), the cost is low. If `ŷ` is close to 1 (incorrect), the cost is very high.

### The Optimization Algorithm: Gradient Descent
To adjust the parameters to minimize the Log Loss, we use **Gradient Descent**. Imagine the cost function as a hilly landscape; Gradient Descent's job is to find the lowest point.

*   **Gradient:** At any point, the "gradient" points in the direction of the steepest **ascent** (uphill).
*   **Descent:** To find the minimum, we take a step in the **opposite direction** of the gradient (downhill).
*   **Learning Rate:** The size of our step is controlled by the learning rate. A small learning rate is slow but steady, while a large one is faster but risks overshooting the minimum.

**Stochastic Gradient Descent (SGD)** is a faster, more common variation that uses a small, random subset of data (a "mini-batch") for each step, making it much more efficient for large datasets.

## 5. Model-Specific Considerations

### The Decision Boundary
Once the model is trained and can predict a probability, we need a rule to turn that probability into a final class prediction (0 or 1). This is done using a **decision boundary** (or threshold).

The standard threshold is 0.5:
*   If $\hat{p} \ge 0.5$, predict class **1**.
*   If $\hat{p} < 0.5$, predict class **0**.

This threshold can be adjusted to make the model more or less sensitive to one class, depending on the business problem (e.g., if false negatives are much worse than false positives).

### Interpretability
The coefficients ($\theta_j$) in a trained logistic regression model can be interpreted, but not as directly as in linear regression. A positive coefficient means that an increase in that feature will increase the log-odds of the outcome, thereby increasing the probability of the outcome being 1.

## 6. Common Pitfalls

### 1. Unbalanced Classes
If one class is much more common than the other (e.g., 99% "No Churn" and 1% "Churn"), a naive model can achieve 99% accuracy by simply predicting "No Churn" every time. This model is useless.
> **The Solution:**
> *   **Use Better Metrics:** Don't use accuracy. Use metrics like Precision, Recall, F1-Score, or look at the ROC AUC score.
> *   **Resample the Data:** Use techniques like over-sampling the minority class (e.g., SMOTE) or under-sampling the majority class.
> *   **Use Class Weights:** Many logistic regression implementations have a `class_weight` parameter that you can set to automatically give more importance to the minority class during training.

### 2. Assuming Linearity
A common mistake is forgetting that the model's power comes from the sigmoid transformation. While the *log-odds* are linear, the relationship between the features and the actual probabilities is not. If the true decision boundary between the classes is highly non-linear, a simple logistic regression model may perform poorly.

## 7. Summary
*   **Logistic Regression** is a classification algorithm that predicts the **probability** of an observation belonging to one of two classes.
*   It uses the **Sigmoid function** to map a linear combination of features to a probability between 0 and 1.
*   The model is trained by minimizing the **Log Loss** cost function, typically using an optimization algorithm like **Gradient Descent**.
*   A **decision boundary** (threshold) is used to convert the predicted probabilities into a final class label (0 or 1).
*   It assumes a linear relationship between the features and the **log-odds** of the outcome.
*   It's a powerful, interpretable, and widely used baseline model for binary classification, but care must be taken with **unbalanced classes**.

---

**Next:** [Logistic Regression Implementation](./12_logistic_regression_implementation.py)