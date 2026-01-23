# DBSCAN and HDBSCAN Clustering

## 1. The Intuitive Idea: Density-Based Clustering

Standard clustering algorithms like K-Means are "centroid-based." They assume clusters are spherical blobs and try to assign every point to a group, often forcing outliers into clusters where they don't belong.

**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) takes a different approach. It defines clusters based on **density**, regions where data points are packed closely together. 

* **Arbitrary Shapes:** It can find clusters of any shape (crescents, spirals, irregular blobs), not just spheres.
* **Noise Handling:** It explicitly identifies and excludes "noise" points (outliers) that do not belong to any dense cluster.
* **Unknown Number of Clusters:** Unlike K-Means, you do *not* need to tell it how many clusters ($k$) to find. 