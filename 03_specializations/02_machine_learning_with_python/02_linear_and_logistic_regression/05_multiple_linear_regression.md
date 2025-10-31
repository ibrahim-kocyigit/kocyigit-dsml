# Multiple Linear Regression

## 1. The Intuitive Idea: From a Line to a Plane (and Beyond)

Simple Linear Regression is great, but it's limited to using only *one* feature to make predictions. The real world is more complex. **Multiple Linear Regression** is the natural extension of this idea, allowing us to use **two or more independent variables** (features) to predict a single continuous target variable.

* **Simple Linear Regression:** Finds the best-fit *line* through the data in two dimensions.
* **Multiple Linear Regression:**  
    * With two features, it finds the best-fit *plane* in three dimensions.
    * With more than two features, it finds the best-fit *hyperplane* in higher-dimensional space.

**The goal** is the same: To model the linear relationship between our features and the target, but now we can leverage more information to make a better decision.

## 2. The Mathematics: A Linear Combination

The equation for multiple linear regression is a straightforward extension of the simple version. It's a linear combination of all the features.

$$ \hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n $$

...where:
*   $\hat{y}$ is the **predicted value** of the target.
*   $x_1, x_2, \dots, x_n$ are the **independent variables** (features).
*   $\theta_0$ is the **y-intercept** (or bias).
*   $\theta_1, \theta_2, \dots, \theta_n$ are the **coefficients** (or weights) for each feature. Each $\theta_i$ represents the change in $\hat{y}$ for a one-unit increase in the corresponding feature $x_i$, assuming all other features are held constant.

The machine learning algorithm's job is to find the optimal values for all the data ( $\theta$ ) parameters.

## 3. How to Train the Model: Finding the Best Parameters
Just like with simple linear regression, the goal is to find the parameters that **minimize the Mean Squared Error (MSE)**. There are two primary methods to achieve this:

### 1. Ordinary Least Squares (OLS)

A direct, mathematical approach that uses linear algebra (matrix operations) on the entire dataset to calculate the single best set of coefficients. This is also known as the **Normal Equation**: 

$$
\theta = (X^T X)^{-1} X^T y
$$
    
...where $X$ is the feature matrix (with an added column of ones for the intercept $\theta_0$), and $y$ is the vector of target values.

**When to Use:** This method works well for smaller to medium-sized datasets where the computation is feasible.


### 2. Optimization Approach (e.g., Gradient Descent)
An iterative approach. It starts with random values for the coefficients and then repeatedly makes small adjustments to them, each time moving in the direction that reduces the model's error on the training data. It continues this process until the error is minimized.

**Cost Function (MSE):**  This is the function we want to minimize:

$$
J(\theta) = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2
$$

**Gradients:** The partial derivatives of the cost function, which tell us the direction of steepest ascent. We move in the opposite direction.

* For the bias/intercept ($\theta_0$):  

$$
\frac{\partial J}{\partial \theta_0} = \frac{2}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})
$$

* For any other coefficient ($\theta_j$ where $j > 0$):

$$
\frac{\partial J}{\partial \theta_j} = \frac{2}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)}
$$

**Update Rule:** How we update the parameters in each iteration.

$$
\theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j}
$$

... where $\alpha$ is the learning rate.

**When to use:** Gradient descent is the preferred method for very large datasets where calculating the OLS solution directly would be too computationally expensive.


## 4. Handling Categorical Variables

Multiple Linear Regression requires all input features to be numerical. So what do we do with categorical variables like "Fuel Type" or "Transmission"? We convert them into numbers.

* **Binary Variables (2 categories):** Convert them into a single numerical feature with values of 0 and 1. This is called creating a **dummy variable**.
    * **Example:** For a `Transmission` feature, "Manual" could become 0 and "Automatic" could become 1.
* **Multi-Class Variables (>2 categories):** Convert them into multiple new boolean (0/1) features, one for each category. This technique is called **One-Hot Encoding**.   
    * **Example:** For a `FuelType` feature with classes "Gas", "Diesel", "Electric", we would create three new features: `is_Gas`, `is_Diesel`, and `is_Electric`. A gasoline car would have a 1 in the `is_Gas` column, and 0s in the others.

## 5. The Pitfalls of Multiple Linear Regression
While powerful, multiple linear regression comes with some important caveats.

#### Pitfall 1: Overfitting
* **What it is:** Adding too many features to your model can cause it to "memorize" the training data, including its noise and random fluctuations.
* **The Conseuqence:** The model will perform exceptionally well on the training data but will fail to generalize and make accurate predictions on new, unseen data.

#### Pitfall 2: Multicollinearity
* **What it is:** This occurs when two or more independent variables in your model are highly correlated with each other (e.g. `Engine Size` and `Number of Cylinders` are likely highly correlated). When this happens, the variables are no longer truly independent.
* **The Consequences:**
    1. It becomes difficult for the model to determine the individual effect of each correlated feature. The coefficient estimates can become unstable and hard to interpret.
    2. It makes "what-if" scenarios unreliable. You can't realistically ask "What happens if I change `Engine Size` while holding `Cylinders` constant?" because in the real world, they change together.
* **The Solution:** Before finalizing your model, perform a correlation analysis and remove, redundant, highly correlated features.

## 6. A Balanced Approach to Feature Selection

To build a robust multiple regression model, you should aim for a balanced set of features that are:
1. Uncorrelated with each other (to avoid multicollinearity).
2. Highly correlated with the target variable (so they are good predictors).
3. Understandable and controllable (if possible, for interpretability).


## 7. Summary

*   Multiple Linear Regression extends simple linear regression by using **two or more features** to predict a continuous target.
*   The model learns a **coefficient for each feature**, representing its independent contribution to the prediction.
*   It's more powerful than simple linear regression but introduces risks like **overfitting** and **multicollinearity**.
*   Careful **feature selection** is crucial to building a reliable and interpretable model.
*   The model can be trained using **OLS** (for smaller data) or optimization methods like **Gradient Descent** (for larger data).

---

**Next:** [Implementation: Multiple Linear Regression](./06_implementation--multiple_linear_regression.py)