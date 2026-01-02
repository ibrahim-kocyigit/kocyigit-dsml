# Motivating Principal Component Analysis (PCA)

Now that we understand the concept of a projection, let's see how PCA uses it to reduce the dimensions of a dataset.

Imagine we have a 2D dataset where each point represents an observation. Reducing the dimensionality means moving these 2D points onto a 1D line. But which line should we choose?

The goal of PCA is to find the **best possible projection line**—the one that **preserves the most information** from the original dataset.

## The Core Idea: More Spread = More Information

How do we measure "information"? In the context of PCA, we measure it by the **variance** or "spread" of the data points after they have been projected.

* A projection that keeps the data points **spread out** has preserved a lot of the original structure and information.
* A projection that makes the data points **clump together** has lost a lot of information.

Let's visualize this. We'll start with a centered 2D dataset and project it onto several different lines to see which one is best.

![](./images/0201.png)

## Summary and Goal of PCA

As the visualizations show, different projection lines result in different amounts of spread in the final 1D data. The projection onto the "best" line (the one that follows the main trend of the data) keeps the points the most spread out.

**The goal of PCA** is to find the projection that preserves the maximum possible spread (variance) in your data, even as you reduce the dimensionality.

This process finds the "principal components" —the directions in the data that capture the most information. By projecting our data onto these components, we can reduce the number of columns in our dataset while minimizing the loss of valuable information.

---

**Next:** [Variance and Covariance](./03_variance_and_covariance.md)