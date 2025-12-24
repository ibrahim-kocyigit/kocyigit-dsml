# K-Nearest Neighbors (KNN)

## 1. The Intuitive Idea: "Tell Me Who Your Friends Are..."

**K-Nearest Neighbors** is a supervised learning algorithm that operates on a very simple, intuitive principle: similar things exist in close proximity to each other.

If you want to know if a new, unclassified movie a "Romance" or an "Action" movie, you look at the movies it is most similar to (in terms of keywords, duration, intensity). If the 5 most similar movies are all "Action" movies, you classify the new one as "Action".

- **Instance-Based Learning:** Unlike other models that learn a mathematical formula (like a line or curve), KNN simply memorizes the training instances.
- **Lazy Learning:** It does not have a training phase. All the computation happens at the moment you ask for a prediction.

<img src="./images/1701.png" alt="KNN Example" width="600"/>

## 2. The Mathematics: Measuring Similarity

To define "neighbors", we need a mathematical way to measure distance. The most common metric is **Euclidean Distance**.

### Euclidean Distance Formula
This is essentially the straight-line distance between two points in space (derived from the Pythagorean theorem).

For two points $p$ and $q$ in an n-dimensional feature space:

$$
d(p, q) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}
$$

#### In Plain English:
1. **Subtract:** For every feature (dimension), calculate the difference between the two points ( $q_i - p_i$ ).
2. **Square:** Square that difference to make it positive and emphasize larger differences.
3. **Sum:** Add up all the squared differences.
4. **Square Root:** Take the square root of the sum to bring the scale back to the original units.

*In your Python implementation, this will be a vectorized operation using Numpy.*

## 3. How the Algorithm Works (Lazy Learning)

Since there is no "training" phase to find coefficients, the algorithm's logic is entirely in the **prediction** step.

### Step-by-Step Prediction Logic
For a new query point $x_{new}$:

1. **Calculate Distances:** Compute the Euclidean distance between $x_{new}$ and **every single example** in the training set ( $X_{train}$ ).
2. **Sort:** Sort these distances from smallest to largest.
3. **Select Neighbors:** Pick the top $k$ examples with the smallest distances. These are the "K-Nearest Neighbors".
4. **Vote (for Classification):** 
    * Look at the target values ( $y$ ) of the $k$ neighbors.
    * The predicted class is the **mode** (the most frequent class).
5. **Average (for Regression):**
    * Look at the target values ( $y$ ) of the $k$ neighbors.
    * The predicted value is the **mean** (average) of these values.

## 4. Key Assumptions

1. **Proximity equals Similarity:** The core assumption is that points that are close in distance share the same label.
2. **Relevant Features:** The distance metric assumes all features contribute meaningfully to the similarity. If you have many irrelevant noise features, the distance becomes meaningless.

## 5. Model-Specific Considerations

### 5.1. Choosing the Hyperparameter `k`
The variable `k` controls the balance between overfitting and underfitting.

* **Low `k` (e.g., k=1):** The model is **overly flexible**. It decides based on a single neighbor. If that neigbor is an outlier or noise, the prediction is wrong. This leads to **High Variance (Overfitting)**.
* **High `k` (e.g., k=50):** The model is **overly rigid**. It averages over a large region, potentially washing out local patterns. This leads to **High Bias (Underfitting)**.

**Selection Strategy:** Typically, we test odd numbers (1, 3, 5...) to avoid ties in voting, and pick the `k` that minimizes error on a validation set.

<img src="./images/1702.png" alt="KNN k value trade-off" width="500"/>

### 5.2. Weighting Neighbors
In standard KNN, all $k$ neighbors get 1 vote. However, it often makes sense to give more influence to closer neighbors.
* **Uniform Weights:** 1 neighbor = 1 vote
* **Distance Weights:** Vote weight is $1/distance$. A neighbor 1 unit away has more influence than a neighbor 10 units away.

## 6. Common Pitfalls

### 6.1. The Critical Need for Feature Scaling
**This is the most important implementation detail.** Because KNN calculates distances based on feature magnitudes, features with large ranges will dominate the calculation.

- **Example:** If Feature A is "Salary" (range 20,000 - 100,000) and Feature B is "Age" (range 20-60). A difference of 1 year in Age is tiny compared to a difference of $1 in Salary.
- **Solution:** You **must** apply `StandardScaler` or `MinMaxScaler` to all features before using KNN.

### 6.2. The Curse of Dimensionality
As the number of features (dimensions) increases, the volume of the space increases exponentially. In high dimensions, data becomes sparse, and "distance" loses its meaning because all points tend to be roughly equidistant from each other.
* **Solution:** Perform **Feature Selection** or dimensionality reduction (like PCA) before running KNN on high-dimensional data.

### 6.3. Computational Cost
KNN is computationally expensive at **prediction time**. To predict one point, it must calculate the distance to *all* training points ( $O(N)$ ). This makes it slow for very large datasets.

## 7. Summary

*   **KNN** classifies new data based on the majority vote of the **k** closest training examples.
*   It uses **Euclidean Distance** as the standard measure of similarity.
*   It is a **Lazy Learner**, meaning it memorizes data rather than learning a model.
*   **Feature Scaling** is mandatory to prevent large-magnitude features from dominating the distance metric.
*   **k** is a hyperparameter that trades off between overfitting (low k) and underfitting (high k).

---

**Next:** [KNN Implementation](./18_knn_implementation.py)