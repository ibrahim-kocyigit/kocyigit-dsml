# Support Vector Machines (SVM)

## 1. The Intuitive Idea: The Widest Possible Street

**Support Vector Machines** are a powerful class of supervised learning algorithms used for classification and regression. While simple linear classifiers (like Logistic Regression) find *a* line that separates classes, SVM reaches for the *best* line.

Imagine you are trying to draw a line on a floor to separate red balls from the blue balls. You could draw many lines that work, but the safest line is the one that has the most clearance on both sides.

* **Hyperplane:** The decision boundary (a line in 2D, a plane in 3D, etc.).
* **Margin:** The distance between the hyperplane and the nearest data points from either class. Think of this as the width of the "street" separating the classes.
* **Support Vectors:** The specific data points that define the edge of the street. These are the "hardest" points to classify.

<img src="./images/1401.png" alt="SVM Margin and Support Vectors" width="500"/>

The goal of SVM is **Margin Maximization**: finding the hyperplane that creates the widest possible street. This makes the model more robust and better at generalizing to new data.

## 2. The Mathematics: Defining the Boundary

To implement SVM from scratch, we need to define the hyperplane mathematically.

### 2.1. The Linear Model
Just like Linear Regression, the hyperplane is defined by a weight vector $w$ and a bias $b$. The prediction ruse for a data point $x$ is:

$$
f(x) = w \cdot x - b
$$

*   If $w \cdot x - b \geq 0$, we predict **Class +1**.
*   If $w \cdot x - b < 0$, we predict **Class -1**.

> **Note:** Unlike Logistic Regression which uses 0 and 1, SVMs typically use target labels $y \in \{-1, 1\}$.

### 2.2. The Margin Condition
We want our data points not just be on the correct side of the hyperplane, but to be *outside the street*. Mathematically, for a sample $i$ to be correctly classified and outside the margin, we enforce:

$$
y_i (w \cdot x_i - b) \geq 1
$$

* $w \cdot x_i - b$: This is the "score" or distance from the hyperplane.
* $y_i$: This is the true label (-1 or 1).
* If the multiplication is $\geq 1$, it means the point is correctly classified and safely outside the margin.

## 3. Key Assumptions

1. **Linear Separability (initially):** The standard SVM assumes the data can be separated by a linear boundary (though we can fix this with kernels later).
2. **Feature Scaling is Critical:** Because SVM tries to maximize pyhsical distance (Euclidean distance), features with large scales will dominate the margin.
**You must normalize/standardize data** (e.g., `StandardScaler`) before training an SVM.
3. **ID:** Independent and Identically Distributed data.

## 4. How the Model is Trained (Primal Form)

To train the model, we need to find the optimal $w$ and $b$. This involves two competing goals:

1. **Maximize the Margin:** In math terms, this is equivalent to minimizing the magnitude of the weights, $||w||^2$.
2. **Minimize Errors:** Ensure points are on the correct side of the margin.

### 4.1. The Cost Function: Hinge Loss

We combine these gloals into a single cost function using **Hinge Loss**.

$$
J(w, b) = \lambda ||w||^2 + \frac{1}{n} \sum_{i=1}^{n} \max(0, 1 - y_i(w \cdot x_i - b))
$$

**$\lambda ||w||^2$** is the regularization term. Minimizing $w$ maximizes the margin. $\lambda$ is a hyperparameter that controls how much we care about having a wide margin versus classifying points correctly. 

**$\max(0, 1 - y_i(w \cdot x_i - b))$** is the Hinge Loss. 
* If a point is correctly classified and outside the margin (score > 1), the value is negative, so the `max` takes **0**. There is no penalty.
* If a point is inside the margin or misclassified (score < 1), the term is positive. The cost increases linearly the further "wrong" the point is.

### 4.2. Optimization: Gradient Descent

