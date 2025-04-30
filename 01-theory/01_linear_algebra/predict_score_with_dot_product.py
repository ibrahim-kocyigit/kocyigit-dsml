import numpy as np


# The industry standard
def predict_score(features: np.ndarray, weights: np.ndarray) -> float:
    """Predicts a score using dot product

    Args:
        features (np.ndarray): Input feature vector (shape: [n_features])
        weights (np.ndarray): Model weights (shape: [n_features])

    Raises:
        TypeError: If inputs are not NumPy arrays.
        Exception: If shapes mismatch.

    Returns:
        float: Prediction score
    """

    if not isinstance(features, np.ndarray) or not (isinstance(weights, np.ndarray)):
        raise TypeError("Inputs must be NumPy arrays")
    if features.shape != weights.shape:
        raise ValueError(f"Shape mismatch: {features.shape} vs {weights.shape}")

    return np.dot(features, weights)


# Only educational
def predict_score_manual(features, weights):
    return sum(f * w for f, w in zip(features, weights))


X = np.array([5, 0.1], dtype="float")
w = np.array([0.8, -0.2], dtype="float")

y_hat = predict_score(X, w)
print(y_hat)

# To verify:
y_hat_manual = predict_score_manual(X, w)
print(y_hat_manual)
