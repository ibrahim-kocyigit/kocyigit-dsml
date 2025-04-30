import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def perform_pca(data, n_components=None):
    """
    Performs PCA on the given data and returns the transformed data, explained variance ratio,
    and cumulative explained variance.

    Args:
        data (np.ndarray): The input data matrix where rows are samples and columns are features.
        n_components (int or None): The number of principal components to retain. If None, all components are kept.

    Returns:
        np.ndarray: Transformed data in the principal component space.
        np.ndarray: Explained variance ratio of the principal components.
        np.ndarray: Cumulative explained variance.
    """
    # Standardize the data (mean=0, variance=1)
    scaler = StandardScaler()
    data_standardized = scaler.fit_transform(data)

    # Perform PCA
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data_standardized)

    # Explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_

    # Cumulative explained variance
    cumulative_explained_variance = np.cumsum(explained_variance_ratio)

    return transformed_data, explained_variance_ratio, cumulative_explained_variance


def plot_cumulative_variance(cumulative_explained_variance):
    """
    Plots the cumulative explained variance to help decide how many principal components to keep.

    Args:
        cumulative_explained_variance (np.ndarray): Cumulative explained variance for each principal component.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(
        range(1, len(cumulative_explained_variance) + 1),
        cumulative_explained_variance,
        marker="o",
        linestyle="--",
    )
    plt.title("Cumulative Explained Variance")
    plt.xlabel("Number of Principal Components")
    plt.ylabel("Cumulative Explained Variance")
    plt.grid(True)
    plt.axhline(
        y=0.95, color="r", linestyle="-", label="95% Variance"
    )  # Threshold line
    plt.legend()
    plt.show()


def main():
    # Load the Iris dataset
    iris = load_iris()
    data = iris.data  # 150 samples with 4 features # type: ignore
    target = iris.target  # Target labels (species) # type: ignore

    # Perform PCA with all components to analyze explained variance
    transformed_data, explained_variance_ratio, cumulative_explained_variance = (
        perform_pca(data)
    )

    # Print the explained variance ratio
    print("Explained Variance Ratio for Each Component:", explained_variance_ratio)
    print("Cumulative Explained Variance:", cumulative_explained_variance)

    # Plot the cumulative explained variance
    plot_cumulative_variance(cumulative_explained_variance)

    # Decide how many components to keep (e.g., retain components that explain 95% of the variance)
    n_components = np.argmax(cumulative_explained_variance >= 0.95) + 1
    print(f"Number of components to retain for 95% variance: {n_components}")

    # Perform PCA again with the selected number of components
    transformed_data, _, _ = perform_pca(data, n_components=n_components)

    # Plot the transformed data (if 2 components are retained)
    if n_components >= 2:
        plt.figure(figsize=(8, 6))
        plt.scatter(
            transformed_data[:, 0], transformed_data[:, 1], c=target, cmap="viridis"
        )
        plt.title("PCA Transformed Data (Iris Dataset)")
        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.colorbar(label="Species")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    main()
