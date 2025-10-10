# Supervised vs. Unsupervised Machine Learning

## What is Machine Learning?

- **Definition (Arthur Samuel, 1950s):** The field of study that gives computers the ability to learn without being explicitly programmed.
- **Example:** Samuel's checkers program learned to play by playing tens of thousands of games against itself. It identified which board positions led to wins or losses and eventually became a better player than Samuel himself.
- **Key Principle:** In general, the more opportunities (data/experience) you give a learning algorithm, the better it will perform.

### Main Types of Machine Learning

1.  **Supervised Learning:**
    - The most common type of ML used in real-world applications.
    - The focus of the first two courses in this specialization.
2.  **Unsupervised Learning:**
    - The focus of the third course in this specialization.
3.  **Other types:** Recommender systems and reinforcement learning will also be covered.

### The Importance of Practical Skills

- Knowing the algorithms (the "tools") is important, but knowing how to apply them effectively is even more critical.
- This course emphasizes the **best practices** for developing practical, valuable machine learning systems.
- The goal is to learn how to design and build serious ML systems, avoiding common pitfalls that can waste months of effort.

---

## Supervised Learning

- **Definition:** Supervised learning algorithms learn mappings from **input** ($x$) to **output** ($y$).
- **Key Characteristic:** The algorithm is trained on a dataset containing the correct output labels ($y$) for each input ($x$).
- After learning from these $(x, y)$ pairs, the model can predict the output $y$ for a new, unseen input $x$.

#### Examples of Supervised Learning

- **Spam Filtering:** $x$ = email, $y$ = "spam" or "not spam"
- **Speech Recognition:** $x$ = audio clip, $y$ = text transcript
- **Machine Translation:** $x$ = English text, $y$ = Spanish translation
- **Online Advertising:** $x$ = user/ad information, $y$ = "click" or "no click"
- **Self-Driving Cars:** $x$ = image, $y$ = position of other cars
- **Visual Inspection:** $x$ = product image, $y$ = "defect" or "no defect"

### Regression

- **Regression** is a type of supervised learning where the goal is to predict a **continuous number**.
- There are infinitely many possible output numbers.
- **Example: Housing Price Prediction**
    - **Input (x):** Size of a house (e.g., in square feet).
    - **Output (y):** Price of the house.
    - The learning algorithm fits a model (like a straight line or a curve) to the data.
    - This model can then be used to predict the price for a new house size.

### Classification

- **Classification** is a type of supervised learning where the goal is to predict a **discrete category or class**.
- The number of possible outputs is small and finite.
- The terms "class" and "category" are used interchangeably.

#### Examples of Classification:

- **Breast Cancer Detection:**
    - **Input (x):** Tumor size, patient age, etc.
    - **Output (y):** "Benign" (0) or "Malignant" (1).
- The algorithm learns a **boundary** that separates the different classes.
- Classification problems can have more than two categories (e.g., cancer type 1, type 2).
- Categories can be non-numeric ("cat", "dog") or numeric (0, 1, 2).

### Regression vs. Classification Recap

- **Regression:** Predicts a continuous number from an infinite set of possibilities.
- **Classification:** Predicts a discrete category from a small, finite set of possibilities.

---

## Unsupervised Learning

- **Definition:** Unsupervised learning algorithms are given data that **does not have any output labels ( $y$ )**.
- **Goal:** To find interesting structures or patterns in the data on its own, without being "supervised" with right answers.

### Clustering Algorithms

- A **clustering algorithm** is a type of unsupervised learning that automatically groups unlabeled data into different clusters.

#### Examples of Clustering:

- **Google News:**
    - Scans hundreds of thousands of news articles daily.
    - Groups related stories together into clusters based on similar words and topics.
    - The algorithm figures out the topics on its own without human supervision.
- **Genetics:**
    - Analyzes DNA microarray data from many individuals.
    - Groups individuals into different "types" based on their gene activity patterns, without being told in advance what those types are.
- **Market Segmentation:**
    - Groups customers into distinct segments based on their data.
    - Allows companies to understand their customer base and serve them more efficiently.

### Other Types of Unsupervised Learning

- **Anomaly Detection:**
    - Used to detect unusual events or outliers in data.
    - **Example:** Fraud detection in financial systems, where unusual transactions could be signs of fraud.
- **Dimensionality Reduction:**
    - Compresses a large dataset into a much smaller one while minimizing information loss.

### Unsupervised vs. Supervised Learning Examples

- **Spam filtering:** Supervised (requires labeled data: spam/not spam).
- **Grouping news stories:** Unsupervised (clustering algorithm finds groups automatically).
- **Market segmentation:** Unsupervised (clustering algorithm discovers segments automatically).
- **Diagnosing diabetes:** Supervised (requires labeled data: diabetes/not diabetes), similar to the breast cancer classification example.

---
**Next:** [Regression Model](./03_regression_model.md)