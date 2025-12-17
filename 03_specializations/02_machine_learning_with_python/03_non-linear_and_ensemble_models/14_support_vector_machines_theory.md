# Support Vector Machines (SVM)

## 1. The Intuitive IDea: The Widest Possible Street

**Support Vector Machines** are a powerful class of supervised learning algorithms used for classification and regression. While simple linear classifiers (like Logistic Regression) find *a* line that separates classes, SVM reaches for the *best* line.

Imagine you are trying to draw a line on a floor to separate red balls from the blue balls. You could draw many lines that work, but the safest line is the one that has the most clearance on both sides.

* **Hyperplane:** The decision boundary (a line in 2D, a plane in 3D, etc.).
* **Margin:** The distance between the hyperplane and the nearest data points from either class. Think of this as the width of the "street" separating the classes.
* **Support Vectors:** The specific data points that define the edge of the street. These are the "hardest" points to classify.

<img src="./images/1401.png" alt="SVM Margin and Support Vectors" width="500"/>

The goal of SVM is **Margin Maximization**: finding the hyperplane that creates the widest possible street. This makes the model more robust and better at generalizing to new data.

## 2. The Mathematics: Defining the Boundary

To implement SVM from scratch, we need to define the hyperplane mathematically.

### The Linear Model
Just like Linear Regression, the hyperplane is defined by a weight vector $w$ and a bias $b$. The prediction ruse for a data point $x$ is:

$$
f(x) = w \cdot x - b
$$

*   If $w \cdot x - b \geq 0$, we predict **Class +1**.
*   If $w \cdot x - b < 0$, we predict **Class -1**.

> **Note:** Unlike Logistic Regression which uses 0 and 1, SVMs typically use target labels $y \in \{-1, 1\}$.
