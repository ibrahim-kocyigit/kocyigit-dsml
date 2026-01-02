# Principal Component Analysis (PCA) - An Overview

Now, let's put all the pieces together to understand how Principal Component Analysis (PCA) works.

Recall our goal: to take a dataset and project it onto a line (or a lower-dimensional plane) that preserves the most information. We learned that the "best" line is the one that **maximizes the variance** (the spread) of the projected data.

The big question is: **How do we find this best line?**

This is where all the concepts we've been studying—projections, eigenvectors, and the covariance matrix—come together in a clever way.


## The PCA Algorithm

Here are the high-level steps for performing PCA on a 2D dataset.

#### Step 1: Center the Data
First, we calculate the mean of our dataset and shift the data so that its center is at the origin (0, 0).

#### Step 2: Calculate the Covariance Matrix
Next, we calculate the **covariance matrix** for our centered data. This 2x2 matrix, $C$, compactly represents the spread (variance) and relationship (covariance) between our two features. Suppose for our data, we calculate the following covariance matrix:  

$$
C = \begin{bmatrix}
9 & 4 \\
4 & 3
\end{bmatrix}
$$

#### Step 3: Find the Eigenvectors and Eigenvalues of the Covariance Matrix
This is the most important leap in the process. The eigenvectors of the covariance matrix point in the directions of maximum variance in the data. The corresponding eigenvalues tell us how *much* variance is in each of those directions.

For our covariance matrix `C`, we would find:

* **Eigenvector 1:** $v_1 = (2, 1)$ with **Eigenvalue 1:** $\lambda_1 = 11$
* **Eigenvector 2:** $v_2 = (-1, 2)$ with **Eigenvalue 2:** $\lambda_2 = 1$

#### Step 4: Select the Principal Component
The eigenvector with the **largest eigenvalue** is the direction that captures the most variance. This is our **first principal component**.

In our case, $\lambda_1 = 11$ is much larger than $\lambda_2 = 1$, so our principal component is the direction defined by the eigenvector $v_1 = (2, 1)$. This is the "best line" we've been looking for. We can discard the second eigenvector.

#### Step 5: Project the Data
The final step is to project our original data onto the line spanned by our chosen principal component. The result is a new, 1-dimensional dataset that has preserved the maximum possible variance.

![](./images/0501.png)

## PCA for a High-Dimensional Dataset

This process works for datasets of any size. Imagine you have a dataset with 9 features (a 9-dimensional dataset).

1.  **Calculate the 9x9 Covariance Matrix.**
2.  **Find the 9 Eigenvalues and their corresponding Eigenvectors.**
3.  **Sort the eigenvectors** by their eigenvalues, from largest to smallest.
4.  **Choose the top *k* eigenvectors.** If you want to reduce your dataset to 2 dimensions, you keep the two eigenvectors with the two largest eigenvalues and discard the rest.
5.  **Project the data.** Create a new matrix `V` where the columns are your chosen eigenvectors (normalized to have a length of 1). The final, reduced dataset is calculated as $ A_{projected} = A_{original} \cdot V$

The result is a new dataset with the same number of rows but only *k* columns, having lost as little information as possible.

---

**Next:** [PCA - Why It Works (The Intuition)](./06_pca--why_it_works.md)