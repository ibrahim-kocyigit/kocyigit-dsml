# Decision Trees

## 1. The Intuitive Idea: A Flowchart of Simple Decisions
A **Decision Tree** is a supervised learning algorithm that models data as a flowchart of questions and answers. Each internal node poses a simple question about a single feature (e.g., "Is sepal_length < 5.5?"), branches split on the possible outcomes, and each leaf node assigns a final prediction (class label for classification, value for regression).

Visually and conceptually, a decision tree recursively partitions the feature space into regions that are increasingly "pure" with respect to the target. This makes decision trees highly interpretable: you can follow the decision path from the root to a leaf to understand *exactly* why a prediction was made.

<img src="./images/0801.png" alt="Decision Tree Example" width="600"/>

## 2. How a Decision Tree Learns: Recursive Partitioning

Decision trees are constructed using a greedy, top-down procedure called **recursive partitioning**:

1. **Start at the Root:** Begin with the entire training set at the root node.
2. **Find the Best Split:** Evaluate candidate splits for every feature (and every possible threshold) and select the single split that maximizes a "purity gain" (or equivalently minimizes impurity).
3. **Partition the Data:** Divide the data into child nodes according to the selected split.
4. **Repeat:** Repeat step 2 recursively for each child node until a stopping condition is met (e.g., no further impurity reduction, minimum samples per node, or maximum tree depth).
5. **Assign Predictions:** Once the tree is built, assign the majority class (for classification) or the mean value (for regression) to each leaf node.

Because the algorithm selects the best local split at each step, it is computationally efficient but can produce sub-optimal global structures (greedy approach).

## 3. Splitting Criteria: Measuring Purity

To choose the "best" split, the algorithm relies on mathematical functions to measure the purity of the resulting nodes.

### 3.1. Gini Impurity
**Gini impurity** is a measure of how often a randomly chosen element from the set would be incorrectly labeled if it were randomly labeled according to the distribution of labels in the subset. It is the default metric for scikit-learn.

For a node with $K$ classes and class probabilities $p_k$:

$$
\text{Gini} = 1 - \sum_{k=1}^{K} p_k^2
$$

* **Low Gini (near 0):** The node is pure (mostly one class).
* **High Gini (near 0.5 for binary):** The node is impure (classes are mixed evenly).

### 3.2. Entropy (Information Gain)
**Entropy** quantifies the disorder or uncertainty in the data.

$$
\text{Entropy} = -\sum_{k=1}^{K} p_k \log_2 p_k
$$

The algorithm chooses the split that maximizes **Information Gain**, which is simply the reduction in entropy:


$$
\text{Information Gain} = \text{Entropy}(\text{parent}) - \sum_{c \in \{\text{children}\}} \frac{N_c}{N_{\text{parent}}} \text{Entropy}(c)
$$

### 3.3. Regression Criteria

For regression trees (predicting continuous values), impurity is typically measured using **Mean Squared Error (MSE)** or Mean Absolute Error (MAE). The goal is to find splits that minimize the variance of the target values within each node. We'll learn more about this in [Regression Trees Theory](./11_regression_trees_theory.md).

## 4. Preventing Overfitting: Controlling Tree Complexity

A fully grown decision tree can perfectly memorize the training data (zero training error) but will likely fail to generalize to new data. This is **overfitting**. To prevent this, we control the tree's complexity.

### 4.1. Pre-pruning (Early Stopping)
We stop the tree from growing before it becomes too complex by setting hyperparameter constraints: 

* `max_depth`: Limits how deep the tree can grow.
* `min_samples_split`: The minimum number of samples required to split an internal node.
* `min_samples_leaf`: The minimum number of samples allowed in a leaf node.
* `max_features`: The number of features to consider when looking for the best split.

### 4.2. Post-pruning (Cost-Complexity Pruning)
We allow the tree to grow to its full depth and then prune back branches that provide little predictive power. A common method is **Cost-Complexity Pruning**, which penalizes the number of terminal nodes (leaves).

$$
R_\alpha(T) = R(T) + \alpha |T_{\text{leaves}}|
$$

By tuning the complexity parameter $\alpha$, we can find the optimal subtree that balances training error $R(T)$ and model complexity.

## 5. Model-Specific Considerations

### 5.1. Advantages
* **Interpretability:** They are easy to understand and visualize (white-box models).
* **Minimal Preprocessing:** Trees handle mixed data types well and are invariant to feature scaling (no need for `StandardScaler`).
* **Non-Parametric:** They do not assume a linear relationship or normal distribution of data.
* **Implicit Feature Selection:** The most important features tend to appear near the root of the tree.

### 5.2. Disadvantages and Pitfalls
* **High Variance:** Small changes in the training data can result in a completely different tree structure. This makes single trees unstable.
* **Overfitting:** Without pruning, trees tend to overfit complex data.
* **Bias:** Splits can be biased toward features with a large number of levels/categories.
* **Solution:** Most of these limitations are solved by **[Ensemble Methods](./23_bias_variance_and_ensemble_models_theory.md)** (like Random Forests or Gradient Boosting), which combine many trees to create a robust model. 

## 6. Summary
* **Decision Trees** learn a hierarchy of if/else questions to partition data into pure regions. 
* Splits are chosen to minimize impurity, measured by **Gini Impurity** or **Entropy**.
* The algorithm is **greedy** and recursive.
* **Overfitting** is a major challenge; it is managed via **pruning** (limiting depth, setting minimum samples).
* While highly **interpretable** and easy to use, single trees are often used as building blocks for more powerful **Ensemble** models.

---

**Next:** [Decision Trees Implementation](./09_decision_trees_implementation.py)