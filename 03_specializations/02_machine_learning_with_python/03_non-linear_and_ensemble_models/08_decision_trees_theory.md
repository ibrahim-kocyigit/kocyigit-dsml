# Decision Trees

## 1. The Intuitive Idea: A Flowchart of Simple Decisions
A **Decision Tree** is a supervised learning algorithm that models data as a flowchart of questions and answers. Each internal node poses a simple question about a single feature (e.g., "Is sepal_length < 5.5?"), branches split on the possible outcomes, and each leaf node assigns a final prediction (class label for classification, value for regression).

Visually and conceptually, a decision tree recursively partitions the feature space into regions that are increasingly "pure" with respect to the target. This makes decision trees highly interpretable: you can follow the decision path from the root to a leaf to understand *exactly* why a prediction was made.

<img src="./images/0801.png" alt="Decision Tree Example" width="600"/>

## How a Decision Tree Learns: Recursive Partitioning

Decision trees are constructed using a greedy, top-down procedure called **recursive partitioning**:

1. **Start at the Root:** Begin with the entire training set at the root node.
2. **Find the Best Split:** Evaluate candidate splits for every feature (and every possible threshold) and select the single split that maximizes a "purity gain" (or equivalently minimizes impurity).
3. **Partition the Data:** Divide the data into child nodes according to the selected split.
4. **Repeat:** Repeat step 2 recursively for each child node until a stopping condition is met (e.g., no further impurity reduction, minimum samples per node, or maximum tree depth).
5. **Assign Predictions:** Once the tree is built, assign the majority class (for classificaiton) or the mean value (for regression) to each leaf node.

Because the algorithm selects the best local split at each step, it is computationally efficient but can produce sub-optimal global structures (greedy approach).

## 3. Splitting Criteria: Measuring Purity