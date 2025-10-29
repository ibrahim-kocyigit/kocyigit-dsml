# Regression Tree

## 1. The Intuitive Idea: A Decision Tree for Numbers

A **Regression Tree** is a type of Decision Tree used to predict a **continuous** target variable (e.g., price, temperature, salary) instead of a categorical one. It follows the same intuitive, flowchart-like structure as a classification tree, but with two key differences in how it operates.

## 2. Classification Tree vs. Regression Tree
The core distinction lies in what they predict and how they measure success.

| Aspect | Classification Tree | **Regression Tree** |
| :--- | :--- | :--- |
| **Target Variable** | Categorical (e.g., `DrugA`, `DrugB`) | **Continuous** (e.g., `Price`, `CO2EMISSIONS`) |
| **Prediction at Leaf** | **Majority Vote:** The most common class in leaf. | **Average Value:** The mean of all target values in the leaf. |
| **Splitting Criterion** | **Purity:** Maximize Information Gain or minimize Gini Impurity. | **Error:** Minimize Mean Squared Error (MSE) |
| **Use Cases** | Spam detection, medical diagnosis, image classification. | Predicting revenue, temperature forecasting, risk assessment. |

## 3. How a Regression Tree "Learns": Minimizing Variance

Like a decision tree, a regression tree is built using **recursive partitioning**. However, its goal is different. Instead of creating "pure" nodes with a single class, a regression tree aims to create nodes where the target values are as **close to each other as possible**. In other words, it tries to **minimize the variance** within each node.

### Prediction at a Node
For any given node in the tree, the prediction is simply the **average** of the target values of all the data points that fall into that node.

$$
\hat{y}_{\text{node}} = \frac{1}{N_{\text{node}}} \sum_{i \in \text{node}} y_i 
$$

Where:
*   $\hat{y}_{\text{node}}$ is the prediction for that node.
*   $N_{\text{node}}$ is the number of data points in the node.
*   $y_i$ are the actual target values of those data points.

*(Note: While the mean is most common, the median could also be used, which is more robust to outliers but computationally more expensive.)*

## 4. The Splitting Criterion: Mean Squared Error (MSE)

To find the best split, a regression tree needs to measure how much a potential split reduces the overall error. The standard metric for this is the **Mean Squared Error (MSE)**.

For a single node, the MSE is the average of the squared differences between the actual values and the node's predicted value (the average). This is mathematically equivalent to the **variance** of the target values in that node.

$$
\text{MSE}_{\text{node}} = \frac{1}{N_{\text{node}}} \sum_{i \in \text{node}} (y_i - \hat{y}_{\text{node}})^2 = \text{Variance}(\mathbf{y}_{\text{node}})
$$

## Finding The Best Split
When considering a split, the algorithm calculates the **weighted average MSE** of the two resulting child nodes (left and right).

$$
\text{Weighted MSE} = \frac{N_{\text{left}}}{N_{\text{total}}} \text{MSE}_{\text{left}} + \frac{N_{\text{right}}}{N_{\text{total}}} \text{MSE}_{\text{right}} 
$$

The algorithm's goal is to find the feature and the split point that result in the **lowest possible weighted MSE**. This is the split that creates two groups with the smallest internal variance.

## 5. How to Split Different Feature Types

### Continuous Features
How does the tree find the best threshold (e.g., `Age < 35.5`) to split a continuous feature? It performs an exhaustive search:
1. Sort all the unique values of the feature.
2. Define candidate split points as the **midpoints** between each pair of consecutive unique values.
3. For each candidate split point, calculate the weighted MSE of the resulting split.
4. Choose the split point that results in the **minimum weighted MSE**.

*(Note: For very large datasets, this can be slow. In practice, algorithms might test only a subset of possible split points.)*

### Categorical Features
* **Binary Feature:** There is only one possible split (e.g., `Sex = Male` vs. `Sex = Female`). The algorithm simply calculates the weighted MSE for this single split.
* **Multi-Class Feature:** For a feature with more than two categories, the algorithm can test different ways to group them into two super-classes (e.g., using a One-vs-All approach) and finds the grouping that minimizes the weighted MSE.

## 6. Summary
*   A **Regression Tree** is a decision tree that predicts a **continuous** value.
*   The prediction at any leaf node is the **average** of the target values of the samples in that leaf.
*   It is built by recursively splitting the data to **minimize variance**.
*   The best split is found by choosing the feature and threshold that minimize the **Mean Squared Error (MSE)** of the resulting child nodes.
*   Like classification trees, they are highly interpretable but must be pruned to avoid overfitting.

---

**Next:** [Lab: Regression Trees](./06_lab--regression_trees.ipynb)