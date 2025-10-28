import numpy as np


def mean_squared_error(y_test: np.ndarray, predictions: np.ndarray) -> float:
    return float(np.mean((predictions - y_test) ** 2))
