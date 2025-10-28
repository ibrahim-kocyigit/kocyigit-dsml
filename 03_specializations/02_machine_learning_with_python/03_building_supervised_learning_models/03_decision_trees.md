# Decision Trees

## 1. The Intuitive Idea: A Flowchart of Decisions

A **Decision Tree** is a supervised learning algorithm that works like a flowchart. It asks a series of simple questions about the data to arrive at a final classification decision. It's one of the most interpretable machine learning models because you can literally see the decision-making process.

The tree is composed of three main parts:
* **Internal Nodes:** Represent a "test" on a specific feature (e.g., "Is `age` < 30?")
* **Branches:** Represent the outcome of the test (e.g., "Yes" or "No").
* **Leaf Nodes (or Terminal Nodes):** Represent the final class label or decision (e.g., "Prescribe Drug A")

<img src="./images/0301.png" alt="Decision Tree Example" width="600"/>

## 2. How a Decision Tree "Learns": Recursive Partioning

A Decision Tree is built through a process called **recursive partitioning**. The algorithm tries to split the data into smaller and smaller groups that are as "pure" as possible (i.e., contain only a single class).

