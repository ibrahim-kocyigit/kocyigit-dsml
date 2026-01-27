# Dimension Reduction Algorithms

## 1. Principal Component Analysis (PCA)

**PCA** is the most common *linear* dimensionality reduction technique. It assumes that the features in the dataset are linearly correlated.

*   **Strengths:** Fast, deterministic, and preserves global structure.
*   **Weaknesses:** Only captures linear relationships.

### How it Works
PCA works by identifying the "principal components", new axes that maximize the variance (information) in the data. These components are orthogonal (uncorrelated) to each other.

1. **First Component:** Captures the direction of maximum variance.
2. **Second Component:** Captures the remaining variance orthogonal to the first, and so on.


> ⚠️ **Note on Mathematics:** The mathematical foundation of PCA has been already explained in great detail in the [Principal Component Analysis](../../../01_math/02_linear_algebra_for_ml_and_ds/07_principal_component_analysis/) section of our Linear Algebra notes.

## 2. t-Distributed Stochastic Neighbor Embedding (t-SNE)

**t-SNE** is a *non-linear* probabilistic tehnique. Unlike PCA, which focuses on preserving large global distances (variances), t-SNE focuses on preserving **local structure**, keeping similar points close together.

*   **Strengths:** Excellent for visualizing clusters in complex data (images, text).
*   **Weaknesses:** Computationally expensive ($O(N^2)$), stochastic (results change every run), and **sensitive to hyperparameters** (perplexity). It often struggles to preserve global structure (distances between clusters may be meaningless).

### The Mathematics of t-SNE
t-SNE converts Euclidean distances between points into conditional probabilities that represent similarities.

#### Step 1: High-Dimensional Similarity ($P_{ij}$)
In the high-dimensional space, we compute the similarity between point $x_i$ and $x_j$ using a Gaussian distribution. The probability that $x_i$ would pick $x_j$ as its neighbor is:

$$
p_{j|i} = \frac{\exp(-||x_i - x_j||^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-||x_i - x_k||^2 / 2\sigma_i^2)}
$$

- If points are close, $p_{j|i}$ is high.
- If points are far, $p_{j|i}$ is almost zero.
- $\sigma_i$ is determined by a "perplexity" hyperparameter (loosely, the number of effective neighbors).

#### Step 2: Low-Dimensional Similarity ($Q_{ij}$)
In the low
