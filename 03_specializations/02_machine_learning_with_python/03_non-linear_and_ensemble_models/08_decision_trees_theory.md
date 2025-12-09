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
5. **Assign Predictions:** Once the tree is built, assign the majority class (for classificaiton) or the mean value (for regression) to each leaf node.

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