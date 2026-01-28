# Evaluating Unsupervised Learning Models: Heuristics and Techniques

## 1. The Challenge of Unsupervised Evaluation
Evaluating unsupervised learning models (like clustering and dimension reduction) is fundamentally harder than supervised learning.

- **No Labels:** In supervised learning, we have "ground truth" labels to check against (e.g., "Was this image actually a cat?"). In unsupervised learning, we are discovering hidden structures, so there is no pre-defined "right-answer."
- **Subjectivity:** Results can be subjective. Is a cluster of "High Spenders" meaningful? That often depends on the business context. 
- **Stability:** A key indicator of quality is **stability**. If we slightly change the data or the random seed, does the model produce the same results? If the clusters change drastically, the model is unreliable.

Therefore, we rely on a combination of **heuristics**, **internal metrics**, **external metrics** (if labels exist), and **visualization**.

## 2. Internal Evaluation Metrics (No Labels)
Internal metrics evaluate the quality of clustering based solely on the data itself. They generally measure two things:

1. **Cohesion:** How close are points to other points in the *same* cluster? (Higher is better).
2. **Separation:** How far are points from points in *other* clusters? (Higher is better).

### 2.1. Silhouette Score
The Silhouette Score measures how similar a point is to its own cluster compared to other clusters.

-   **Range:** -1 to +1.
    *   **+1:** Perfect. The point is far from neighboring clusters and close to its own.
    *   **0:** The point is on the decision boundary between two clusters.
    *   **-1:** The point is assigned to the wrong cluster.
-   **Usage:** A high average Silhouette Score indicates well-defined, distinct clusters.

### 2.2. Davies-Bouldin Index
This index measures the average ratio of cluster compactness to cluster separation. A low score means clusters are tight (compact) and far apart (separated). Therefore, **lower is better**.

### 2.3. Inertia (for K-Means)
Inertia measures the sum of squared distances of samples to their closest cluster center.

*   **Interpretation:** Lower is generally better (more compact clusters).
*   **Trade-off:** Inertia *always* decreases as you increase the number of clusters ($k$). You must use the "Elbow Method" to find the balance between low inertia and a reasonable number of clusters.

## 3. External Evaluation Metrics (With Labels)
Sometimes, we have labels but we still use clustering (e.g., to see if the natural groupings match our known classes). In this case, we can use external metrics.

### 3.1. Adjusted Rand Index (ARI)
Measures the similarity between the true labels and the predicted clusters, ignoring permutations (e.g., it doesn't matter if we call the cluster "0" and the label "A", or vice versa).

- **Range:** -1 to 1.
    - **1**: Perfect match.
    - **0**: Random guessing.
    - **Negative:** Worse than random.

### 3.2. Normalized Mutual Information (NMI)
Quantifies the "shared information" between the predicted clusters and the true labels.

*   **Range:** 0 to 1.
    *   **1:** Perfect correlation.
    *   **0:** No correlation.

## 4. Evaluating Dimensionality Reduction
When reducing dimensions (e.g., PCA), we need to ensure we haven't lost critical information.

### 4.1. Explained Variance Ratio (for PCA)
This tells us what percentage of the dataset's total variance (information) is captured by each principal component.

- **Cumulative Variance:** We often look at the *cumulative* sum. For example, "The first 2 components explain 95% of the variance."
- **Elbow Plot:** We plot variance against the number of components to decide where to cut off.

### 4.2. Reconstruction Error
This measures how accurately we can reconstruct the original data from the reduced representation. **Lower is better**. High error means the dimension reduction discarded important details.

### 4.3. Neighborhood Preservation
For non-linear methods like t-SNE and UMAP, we care less about global variance and more about **local structure**. We check: *Are points that were neighbors in high-dimensional space still neighbors in the low-dimensional projection?*

## 5. Summary

| Type | Metric | Goal | Interpretation |
| :--- | :--- | :--- | :--- |
| **Internal (Clustering)** | Silhouette Score | Cohesion & Separation | Higher (+1) is better. |
| **Internal (Clustering)** | Davies-Bouldin | Compactness vs. Separation | Lower is better. |
| **External (Clustering)** | Adjusted Rand Index | Match usually known labels | Higher (+1) is better. |
| **Dim. Reduction** | Explained Variance | Retain Information | Higher is better. |
| **Dim. Reduction** | Reconstruction Error | Accuracy of reconstruction | Lower is better. |

---

**Next:** [Evaluating K-means Clustering Lab](./06_evaluating_k-means_clustering_lab.ipynb)
