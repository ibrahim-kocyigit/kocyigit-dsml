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

1.  **Binary Outcome:** The target variable is binary or dichotomous. Logistic regression is designed for 2-class problems.
    > **What to do if it's violated?**
    > *   **Use a Multiclass Model:** If your target has more than two categories (e.g., "Low", "Medium", "High"), use a model designed for multiclass classification. The direct extension of logistic regression is **Multinomial Logistic Regression** (often called Softmax Regression). Other popular choices are Decision Trees, Random Forests, or Gradient Boosting models.

2.  **Independence of Observations:** The observations in the dataset are independent of each other. This is often violated in time-series data or clustered data.
    > **What to do if it's violated?**
    > *   **For Time-Series Data:** Use models specifically designed for sequential data, such as ARIMA, LSTMs, or other Recurrent Neural Networks (RNNs).
    > *   **For Clustered Data:** (e.g., students from the same school), use models that can account for this dependency, such as mixed-effects models or Generalized Estimating Equations (GEE).

3.  **Linearity of Log-Odds:** This is the key assumption. Logistic Regression assumes a linear relationship between the features and the **log-odds** of the outcome.
    > **What to do if it's violated?**
    > *   **Feature Engineering:** Create new features that have a linear relationship with the log-odds. This can include polynomial features (e.g., `x^2`), interaction terms (e.g., `x1 * x2`), or other non-linear transformations.
    > *   **Use a More Complex Model:** Switch to a non-linear classification model like a Support Vector Machine (SVM) with a non-linear kernel (e.g., RBF), a Decision Tree, or a neural network. These models can learn complex, non-linear decision boundaries automatically.

4.  **No High Multicollinearity:** The independent variables should not be highly correlated with each other, as this can make the model's coefficients unstable and hard to interpret.
    > **What to do if it's violated?**
    > *   **Remove One of the Correlated Features:** The simplest solution. Keep the one that is more strongly correlated with the target variable.
    > *   **Combine the Features:** Create a new feature by combining the correlated ones (e.g., create an average).
    > *   **Use Regularization:** Techniques like Ridge (L2) or Lasso (L1) regression are very effective. Most scikit-learn implementations include regularization by default, which helps mitigate the effects of multicollinearity.
## 4. How the Model is Trained

Training is an iterative process where the model "learns" the best parameters ($\theta$) by trying to minimize its prediction error. This follows a simple loop:
1. **Initialize Parameters:** Start with a random guess for the parameters ($\theta$).
2. **Make Predictions:** Use the current parameters and the sigmoid function to predict the probability for every observation.
3. **Measure the Error:** Compare the predicted probabilities to the actual classes using a **cost function** called **Log Loss**.
4. **Update the Parameters:** Adjust the parameters in a direction that reduces the error, using an algorithm called **Gradient Descent**.
5. **Repeat:** Continue this loop until the error is minimized or a set number of iterations is reached.

### The Cost Function: Log Loss (or Binary Cross-Entropy)
The Log Loss function measures how well the predicted probabilities (`p_hat`) match the actual class labels (`y`). The total cost over the entire dataset of `n` observations is the average of the loss for each observation.

$$
J(\theta) = - \frac{1}{n} \sum_{i=1}^{n} [y^{(i)} \log(\hat{p}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{p}^{(i)})]
$$

This function is designed to heavily penalize confident but wrong predictions. If the actual class `y` is 1, the cost is `-log(p_hat)`; if `y` is 0, the cost is `-log(1-p_hat)`. In both cases, the cost is low if the prediction is correct and high if it is incorrect.

### The Optimization Algorithm: Gradient Descent
To adjust the parameters to minimize the Log Loss, we use **Gradient Descent**. It works by calculating the gradient (the direction of steepest *ascent*) of the cost function and taking a small step in the opposite direction (steepest *descent*).

**Gradients (Partial Derivatives):**  
The gradient of the cost function `J` with respect to a single parameter `θ_j` is calculated as:  

$$
\frac{\partial J}{\partial \theta_j} = \frac{1}{n} \sum_{i=1}^{n} (\hat{p}^{(i)} - y^{(i)}) x_j^{(i)}
$$

**The Update Rule:**  
In each iteration of Gradient Descent, every parameter `θ_j` is updated simultaneously using the following rule, where `α` (alpha) is the learning rate:  

$$
\theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j}
$$

**Vectorized Implementation:**  
For a much faster implementation (e.g., in NumPy), we use the vectorized form, which processes all observations at once.

*   **Predictions (`p_hat`):**  

$$
\hat{p} = \sigma(X\theta)
$$

*   **Gradient (`dw`):**  

$$
dw = \frac{1}{n} X^T (\hat{p} - y)
$$

*   **Update Rule:**
    
$$
\theta := \theta - \alpha \cdot dw
$$

...where `X` is the feature matrix, `y` is the vector of true labels, and `θ` is the vector of parameters.

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