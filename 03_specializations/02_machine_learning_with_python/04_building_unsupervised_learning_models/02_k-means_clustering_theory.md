# K-Means Clustering 

## 1. The Intuitive Idea: Partitioning Around Centroids

**K-Means** is a popular, iterative, centroid-based clustering algorithm. It partitions a dataset into $k$ non-overlapping sub-groups (clusters) where each data point belongs to the cluster with the nearest mean (centroid).

The core goal of the algorithm is to create clusters that have:
* **Minimal Variance:** Points within a cluster should be as close to each other (and the center) as possible.
* **Maximum Dissimilarity:** Different clusters should be as distinct from each other as possible.

<img src="./images/0201.png" alt="K-Means Centroids" width="500"/>

* The **centroid** is the "center" of the cluster, marked by an X in visualizations. It represents the **average position** of all data points assigned to that cluster.
* The parameter **$k$** is the number of clusters you want to find. A higher $k$ creates smaller, more detailed clusters; a lower $k$ creates larger, broader groups.

## 2. How the Algorithm Works
K-Means is an iterative process that keeps moving the centroids until they find the optimal position.

1. **Initialize:** Choose the number of clusters $k$. Randomly select $k$ starting points as the initial centroids (these can be random data points or random locations in the feature space).
2. **Assign:** For every data point in the dataset, calculate the distance to each of the `k` centroids. Assign the data point to the cluster of the **nearest** centroid.
3. **Update:** Recalculate the position of the centroids. The new centroid becomes the **mean** (average) of all the data points currently assigned to that cluster.
4. **Repeat:** Repeat steps 2 and 3 until the centroids stop moving (convergence) or a maximum number of iterations is reached.

<img src="./images/0202.png" alt="K-Means Iterations" width="800"/>

## 3. The Mathematics: Minimizing Variance

The algorithm tries to minimize the **Within-Cluster Sum of Squares (WCSS)**, also known as **Inertia**. Mathematically, this is a double sum over each cluster $i$ and each point $x$ within that cluster:

$$
J = \sum_{i=1}^{k} \sum_{x \in C_i} ||x - \mu_i||^2
$$