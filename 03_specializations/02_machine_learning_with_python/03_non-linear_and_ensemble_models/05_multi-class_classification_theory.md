# Multi-Class Classification

## 1. The Intuitive Idea: Choosing from a List of Options
We've used [Logistic Regression](../02_linear_and_logistic_regression/08_logistic_regression_theory.md) to answer "yes" or "no" questions (**Binary Classification**). But what if the question has more than two possible answers?

* Does this image contain a *cat*, a *dog*, or a *bird*?
* Which medication (*Drug A*, *Drug B*, or *Drug C*) is best for this patient?
* Is this news article about *sports*, *politics*, or *technology*?

This is **Multi-Class Classification**. The goal is to train a model that can predict a single categorical label from a list of **three or more** possible outcomes. It learns the patterns that associate input features with a specific class and then assigns a label to new, unseen data.

## 2. The Mathematics: Strategies for Multiple Choices
How do we predict one category out of many? There are two main approaches: adapting binary classifiers for multi-class problems, or using an algorithm that is natively multi-class.

### 2.1. Adapting Binary Classifiers (OvA and OvO)
Many powerful algorithms (like Support Vector Machines) are inherently binary. We can cleverly adapt them using two primary strategies:

#### One-vs-Rest (OvR) a.k.a. One-vs-All (OvA)
This is the most common strategy.

* **The Idea:** For `k` classes, train `k` separate binary classifiers.
* **Training:**  
    1. **Classifier 1:** Learns to distinguish **Class A** vs. **[Not A]** (i.e., B, C, etc.)
    2.  **Classifier 2:** Learns to distinguish **Class B** vs. **[Not B]** (i.e., A, C, etc.).
    3.  ...and so on for all `k` classes.
* **Prediction:** For a new data point, get a prediction score (e.g., a probability) from all `k` classifiers. The final predicted class is the one whose classifier gives the highest score.

$$
\text{Prediction} = \underset{i \in \{1, ..., k\}}{\arg\max} (\text{classifier}_i(x))
$$

<img src="./images/0501.png" alt="One-vs-All Diagram" width="800"/>

#### One-vs-One (OvO)
* **The Idea:** Train a separate binary classifier for every possible *pair* of classes.
* **Training:** For `k` classes, you train `k * (k-1) / 2` classifiers. 
    1.  **Classifier 1:** Learns **Class A** vs. **Class B**.
    2.  **Classifier 2:** Learns **Class A** vs. **Class C**.
    3.  **Classifier 3:** Learns **Class B** vs. **Class C**.
    4.  ...and so on.
*   **Prediction:** For a new data point, every classifier makes a prediction. The final predicted class is the one that "wins" the most head-to-head contests (i.e., receives the most votes).

### 2.2. Native Multi-Class Algorithms (Softmax Regression)
Some algorithms are naturally designed for multi-class problems. The most direct extension of Logistic Regression is **Softmax Regression** (also called Multinomial Logistic Regression).

Instead of the Sigmoid function, which outputs one probability, Softmax takes a vector of scores and outputs a **probability distribution** - a set of probabilities for each class that all sum to 1.

$$
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{k} e^{z_j}} \quad \text{for } i=1, ..., k
$$

* The model computes a score `z` for each class.
* The Softmax function then converts these scores into probabilities.
* The class with the highest probability is the final prediction.

## 3. Key Assumptions
Multi-class classification is a *type of problem*, not a single algorithm. The assumptions therefore depend entirely on the **underlying model** being used.

1. **Inherited Assumptions:** If you use an OvR strategy with Logistic Regression, each of your `k` binary classifiers inherits all the assumptions of Logistic Regression (e.g., linearity of log-odds, no high multicollinearity).
2. **Independence of Observations:** This is a nearly universal assumption. The data points should be independent of one another. This is often violated in time-series data.
3. **Mutually Exclusive Classes:** The model assumes that each sample belongs to only one class. If a sample can belong to multiple classes at once (e.g., a movie being classified as both "Action" and "Comedy"), this is a different problem called **Multi-Label Classification**.

## 4. How the Models are Trained
Training also depends on the strategy.

### 4.1. For OvA and OvO Strategies:
The process is simple: you just train multiple independent binary classifiers. For an OvR model with `k` classes, you would run the training algorithm for a binary classifier `k` times on `k` different versions of the dataset.

### 4.2. For Native Multi-Class Algorithms (Softmax Regression):
The training process is analogous to Logistic Regression but scaled up.

#### Cost Function: Cross-Entropy Loss
This is the multi-class generalization of Log Loss. It measures the difference between the predicted probability distribution and the true distribution (where the correct class has a probability of 1 and all others are 0).

$$
J(\theta) = - \frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{k} y_j^{(i)} \log(\hat{p}_j^{(i)})
$$

... where $y_j$ is 1 if the sample $i$ belongs to class $j$ and 0 otherwise, and $\hat{p}_j$ is the predicted probability for that class.

#### Optimization Algorithm: Gradient Descent
The model uses Gradient Descent to find the parameters ( $\theta$ ) that minimize the Cross-Entropy Loss, iteratively adjusting the weights to improve the predicted probabilities.

## 5. Model-Specific Considerations

### 5.1. Choosing a Strategy: OvA vs. OvO
* **OvA (or OvR)** is simple and is the default in `scikit-learn`. It scales well as the number of classes grows, as it only requires `k` classifiers.
* **OvO** requires training `k * (k-1) / 2` classifiers, which can be computationally expensive if `k` is large. However, it can be more efficient for algorithms (like kernelized SVMs) that don't scale well with the size of the dataset, because each classifier is trained on a smaller subset of the data (only two classes at a time).

### 5.2. Algorithms with Native Support
Some algorithms are inherently multi-class and do not require OvA/OvO:
* Decision Trees & Random Forests
* Naive Bayes
* Neural Networks
* Gradient Boosting models like XGBoost and LightGBM

## 6. Common Pitfalls: Unbalanced Classes
This is a major issue in multi-class problems, just as it is in binary ones. If one class (e.g., "No Disease") is far more common than others, a naive model can achieve high accuracy by simply always predicting the majority class.

#### The Solution:
* **Use Better Metrics:** Do not rely on Accuracy. Use metrics like **macro/weighted F1-Score**, **Precision**, and **Recall**, or a **Confusion Matrix**.
* **Resample the Data:** Use techniques like SMOTE (oversampling) or random undersampling.
* **Use Class Weights:** Many algorithms allow you to pass a `class_weight='balanced'` parameter to automatically penalize errors on the minority classes more heavily during training.

## 7. Summary
* **Multi-Class Classification** is a supervised learning task for predicting a category from **three or more** possible options.
* Binary classifiers can be adapted using **One-vs-Rest (OvR)** or **One-vs-All (OvO)** strategies.
* Some algorithms, like **Softmax Regression** and **Decision Trees**, are natively multi-class.
* The assumptions depend on the underlying algorithm being used.
* Native multi-class models are typically trained by minimizing **Cross-Entropy Loss**. 
* Beware of **unbalanced classes** and use appropriate evaluation metrics beyond simple accuracy.

---

**Next:** [Multi-Class Classification Implementation](./06_multi-class_classification_implementation.py)