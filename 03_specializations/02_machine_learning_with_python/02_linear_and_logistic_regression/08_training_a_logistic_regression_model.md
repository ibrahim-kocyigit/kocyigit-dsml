# Training A Logistic Regression Model

## 1. The Intuitive Idea: How a Model "Learns"

We know that a logistic regression model uses a linear equation and a sigmoid function to make predictions. But how does it find the right parameters ($\theta$) for that linear equation?

The answer is through a process of **training**, which is essentially a guided form of trial and error. The model's objective is to find the set of parameters that **minimizes the prediction error** on the training data.

## 2. The Training Loop

The training process for logistic regression (and many other machine learning models) follows an iterative loop:

1. **Initialize Parameters:** Start with an initial guess for the parameters ($\theta$). These can be random values or all zeros.
2. **Make Predictions:** Use the current parameters to predict the probability of the positive class (class '1') for every observation in the training data.
3. **Measure the Error:** Compare the model's predicted probabilities to the actual classes (0s and 1s) using a **cost function**. This function calculates a single number that represents how "wrong" the model currently is.
4. **Update the Parameters:** Adjust the parameters ($\theta$) in a direction that will *reduce* the error (the cost function).
5. **Repeat:** Go back to step 2 and repeat the process. Continue this loop until the error is sufficiently small or a maximum number of iterations is reached.

## 3. The Cost Function: Log Loss (or Binary Cross-Entropy)
For logistic regression, the most common cost function is **Log Loss**, also known as Binary Cross-Entropy. Its job is to measure how well the predicted probabilities mathc the actual class labels.

The formula for Log Loss for a single obervation is: `Cost(ŷ, y) = -[ y * log(ŷ) + (1-y) * log(1-ŷ) ]`

Where:
* `y` is the actual class (0 or 1).
* `ŷ` (y-hat) is the predicted probability of the class being 1.

Let's break down how it works:

#### Case 1: The actual class is 1 (`y=1`)
* The formula simplifies to `Cost = -log(ŷ)`.
* If our prediction `ŷ` is close to 1 (a confident, correct prediction), the `log(ŷ)` is close to 0, so the cost is very low.
* If our prediction `ŷ` is close to 0 (a confident, *incorrect* prediction), `log(ŷ)` approached negative infinity, so the cost becomes very high. **Log Loss heavily penalizes confident but wrong predictions.**

#### Case 2: The actual class is 0 (`y=0`)
* The formula simplifies to `Cost = -log(1-ŷ)`.
* If our prediction `ŷ` is close to 0 (a confident, correct prediction), `(1-ŷ)` is close to 1, `log(1-ŷ)` is close to 0, and the cost is very low.
* If our prediction `ŷ` is close to 1 (a confident, *incorrect* prediction), `(1-ŷ)` is close to 0, `log(1-ŷ)` approaches negative infinity, and the cost becomes very high.

The total Log Loss for the entire dataset is simply the average of this cost across all observations. The goal of training is to find the parameters ($\theta$) that minimize this average Log Loss.

## 4. The Optimization Algorithm: Gradient Descent

How do we actually adjust the parameters to minimize the Log Loss? The most popular method is **Gradient Descent**.

Imagine the cost function as a 3D surface, like a hilly landscape, where the lowers point represents the minimum error.

<img src="./images/0801.png" alt="Gradient Descent visualization" width="600"/>

* **Gradient:** At any point on this surface, the "gradient" is a vector that points in the direction of the **steepest ascent** (uphill).
* **Descent:** To find the minimum, we want to go downhill. So on each iteration, Gradient Descent calculates the gradient and takes a step in the **opposite direction** (the direction of steepest *descent*).
* **Learning Rate:** The size of the step we take is controlled by a parameter called the learning rate.
    * A small learning rate leads to slow but steady progress.
    * A large learning rate can speed things up, but it risks "overshooting" the minimum and failing to converge.
* The process repeats, taking step after step downhill until the slope becomes flat, indicating we have arrived at a minimum.

### Stochastic Gradient Descent (SGD): A Faster Variation

Standard Gradient Descent calculates the gradient using the **entire training dataset** for every single step. This is computationally expensive and very slow on large datasets.

**Stochastic Gradient Descent (SGD)** offers a faster alternative:
* **How it works:** Instead of using the whole dataset, SGD estimates the gradient using only a **small, random subset of the data** (a "mini-batch") for each step.
* **Advantages:**  
    * **Much Faster:** It's computationally cheaper, allowing for many more updates in the same amount of time.
    * **Avoids Local Minima:** The "noisy" steps caused by using a random subset can help the algorith to "jump out" of shallow local minima and find a better, more global minimum.
* **Disadvantages:**
    * The path to minimum is less direct and can "wander around" the minimum before settling. This can be improved by gradually descreasing the learning rate as the algorithm gets closer to the solution.

## 5. Summary

*   Training a logistic regression model means finding the optimal parameters ($\theta$) that **minimize a cost function**.
*   The standard cost function for logistic regression is **Log Loss**, which heavily penalizes confident but incorrect predictions.
*   **Gradient Descent** is the optimization algorithm used to find the minimum of the cost function. It iteratively takes steps in the direction of the steepest descent.
*   **Stochastic Gradient Descent (SGD)** is a faster, more scalable version of Gradient Descent that uses random subsets of the data for each step, making it ideal for large datasets.

---

**Next:** [Lab: Logistic Regression](./09_lab--logistic_regression.ipynb)