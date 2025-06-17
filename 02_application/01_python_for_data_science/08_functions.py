"""
Key Concepts:
- Function design principles
- Parameter patterns (*args, *kwargs)
- Type hints for data science
- Closures and decorators
- Generator functions for large datasets
"""


# ====================
# 1. FUNCTION BASICS
# ====================
def clean_data(value: float, threshold: float = 0.0) -> float:
    """Clean numerical data by applying threshold

    Args:
        value (float): Input data point
        threshold (float, optional): Minimum allowed value. Defaults to 0.0.

    Returns:
        float: Cleaned value or 0.0 if below threshold
    """
    return value if value >= threshold else 0.0


# Usage
print(clean_data(3.5))  # 3.5
print(clean_data(-2.1, 0.0))  # 0.0


# ====================
# 2. PARAMETER HANDLING
# ====================
# Flexible argument passing
def describe_dataset(*values: float, **metadata):
    """
    Process variable data with metadata.
    """
    stats = {
        "mean": sum(values) / len(values),
        "max": max(values),
        "min": min(values),
        **metadata,  # Merge metadata
    }
    return stats


# Usage
print(describe_dataset(1.2, 3.4, 5.6, source="sensor1", units="cm"))
# {'mean': 3.4, 'max': 5.6, 'min': 1.2, 'source': 'sensor1', 'units': 'cm'}


# ====================
# 3. TYPE HINTS
# ====================
from typing import List, Dict, Tuple, Optional, Union

DataPoint = Tuple[float, float]
Dataset = List[DataPoint]


def normalize_data(data: Dataset, factor: Optional[float] = None) -> List[float]:
    """Normalize coordinate data."""
    if factor is None:
        factor = max(max(x, y) for x, y in data)
    return [(x / factor, y / factor) for x, y in data]


data = [(1.0, 2.0), (3.0, 1.5), (0.5, 4.0)]
normalized = normalize_data(data)
# Result: [(0.25, 0.5), (0.75, 0.375), (0.125, 1.0)]
