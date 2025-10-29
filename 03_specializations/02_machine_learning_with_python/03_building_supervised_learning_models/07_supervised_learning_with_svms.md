# Supervised Learning with SVMs

## 1. The Core Idea: Finding the Best Dividing Line

**Support Vector Machines (SVM)** are powerful class of supervised learning algorithms used for classification and regression. The primary goal of an SVM is to find the optimal **hyperplane** that best separates the classes in a dataset.

* **Hyperplane:** In simple terms, this is the decision boundary.
    * In a 2D feature space, the hyperplane is a **line**.
    * In a 3D feature spance, the hyperplane is a **plane**.
    * In higher dimensions, it's called a hyperplane.

The SVM doesn't just find *any* line that separates the classes; it finds the one that is as far away as possible from the closest data points of each class.

## 2. The Goal: Maximizing the Margin

The core intuition of SVM is to find the hyperplane that has the **maximum margin**.

* **Margin:** The distance between the hyperplane and the nearest data point from either class. Think of it as the width of the "street" separating two classes. A wider street is better.
* **Support Vectors:** These are the data points that are closest to the hyperplane and lie on the edge of the margin. They are the most critical points in the dataset because they "support" or define the position of the hyperplane. If you were to move a support vector, the hyperplane would move with it.

<img src="./images/0701.png" alt="SVM Margin and Support Vectors" width="600"/>

By maximizing the margin, the SVM creates a decision boundary that is more robust and more likely to generalize well to new, unseen data.

## 3. Handling Real-World Data: The Soft Margin

