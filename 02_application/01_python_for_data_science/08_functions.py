# 08_functions.py
# Building professional-grade functions for data processing

"""
Key Concepts:
- Function design principles for clean data pipelines
- Advanced parameter handling (*args, **kwargs)
- Type hints for maintainable data science code
- Stateful closures for custom data processors
- Decorators for cross-cutting concerns
- Generator functions for memory-efficient data streaming
"""

# ====================
# 1. FUNCTION BASICS
# ====================
# Core principles for data processing functions:
# - Single responsibility
# - Clear naming (verb + noun)
# - Documented inputs/outputs
# - Sensible defaults


def clean_data(value: float, threshold: float = 0.0) -> float:
    """Clean numerical data by applying threshold.

    Args:
        value: Input data point to be cleaned
        threshold: Minimum allowed value (default 0.0)
                  Values below this will be clipped to 0.0

    Returns:
        Cleaned value or 0.0 if below threshold

    Example:
        >>> clean_data(3.5, 1.0)
        3.5
        >>> clean_data(-2.1)
        0.0
    """
    return value if value >= threshold else 0.0


# ====================
# 2. PARAMETER HANDLING
# ====================
# Advanced parameter techniques:
# - *args: Variable positional arguments (tuples)
# - **kwargs: Variable keyword arguments (dicts)
# - Combined for maximum flexibility


def describe_dataset(*values: float, **metadata):
    """Process variable numerical data with attached metadata.

    Uses Python's flexible argument passing to handle:
    - Any number of data points (*values)
    - Any additional metadata as key-value pairs (**metadata)
    """
    stats = {
        "mean": sum(values) / len(values),
        "max": max(values),
        "min": min(values),
        "samples": len(values),
        **metadata,  # Merge metadata into results
    }
    return stats


# ====================
# 3. TYPE HINTS
# ====================
# Type hints provide:
# - Better code documentation
# - IDE autocompletion
# - Early error detection
# - Required for modern Python data pipelines

from typing import List, Dict, Tuple, Optional, Union

# Custom type aliases for domain clarity
DataPoint = Tuple[float, float]  # (x,y) coordinate
Dataset = List[DataPoint]  # List of coordinates


def normalize_data(
    data: Dataset, factor: Optional[float] = None
) -> List[Tuple[float, float]]:
    """Normalize coordinate data to unit scale.

    Args:
        data: List of (x,y) coordinate tuples
        factor: Scaling factor (defaults to max coordinate if None)

    Returns:
        List of normalized (x,y) tuples
    """
    if factor is None:
        factor = max(max(x, y) for x, y in data) or 1.0  # Avoid division by zero
    return [(x / factor, y / factor) for x, y in data]


# ====================
# 4. CLOSURES
# ====================
# Closures create functions with:
# - Encapsulated state
# - Custom behavior
# - Configuration at creation time


def make_outlier_detector(multiplier: float = 1.5):
    """Factory function creating outlier detectors using IQR method.

    The created detector remembers its configuration (multiplier)
    and can be reused across different datasets.
    """

    def detector(values: List[float]) -> List[bool]:
        """Identify outliers using interquartile range (IQR)."""
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        q1 = sorted_vals[n // 4]
        q3 = sorted_vals[3 * n // 4]
        iqr = q3 - q1
        lower_bound = q1 - multiplier * iqr
        upper_bound = q3 + multiplier * iqr
        return [v < lower_bound or v > upper_bound for v in values]

    return detector


test_data = [8.0, 16.0, 13.0, 14.0, 15.0, 16.0, 17.0, 30.0]

detect = make_outlier_detector(3.5)
flags = detect(test_data)
# [False, False, False, False, False, False, False, True]

strict_detect = make_outlier_detector(1.0)
flags_strict = strict_detect(test_data)
# [True, False, False, False, False, False, False, True]


# ====================
# 5. DECORATORS
# ====================
# Decorators allow adding behavior to functions:
# - Logging
# - Timing
# - Caching
# - Validation


def log_execution(func):
    """Decorator that logs function entry/exit with parameters."""

    def wrapper(*args, **kwargs):
        print(f"🚀 Executing {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ Completed {func.__name__} with result={result}")
        return result

    return wrapper


@log_execution
def process_batch(data: List[float], scale: float = 1.0) -> List[float]:
    """Example processing function that scales input data."""
    return [x * scale for x in data]


process_batch(test_data)

# ====================
# 6. GENERATOR FUNCTIONS
# ====================
# Generators enable:
# - Memory-efficient data streaming
# - Lazy evaluation
# - Pipeline processing


def stream_csv(filepath: str, chunk_size: int = 1000):
    """Yield CSV data in manageable chunks.

    Instead of loading entire file into memory:
    - Reads file line by line
    - Yields chunks of specified size
    - Allows processing of files larger than RAM
    """
    with open(filepath) as f:
        chunk = []
        for i, line in enumerate(f):
            chunk.append(line.strip().split(","))
            if (i + 1) % chunk_size == 0:
                yield chunk
                chunk = []
        if chunk:  # Yield any remaining lines
            yield chunk


# ====================
# 7. DATA SCIENCE PATTERNS
# ====================
# 1) Validation Function
def validate_input(value: Union[int, float], valid_range: Tuple[float, float]) -> bool:
    """Check if value falls within specified range.

    Args:
        value: Input value to validate
        valid_range: (minimum, maximum) inclusive bounds

    Returns:
        True if value is within bounds, False otherwise
    """
    low, high = valid_range
    return low <= value <= high


# 2) Pipeline Factory
def make_feature_pipeline(*steps):
    """Create a composed transformation pipeline.

    Args:
        *steps: Sequence of transformation functions

    Returns:
        A function that applies all transformations in sequence
    """

    def pipeline(data):
        for step in steps:
            data = step(data)
        return data

    return pipeline


# 3) Memoization (Caching)
from functools import lru_cache


@lru_cache(maxsize=128)
def expensive_computation(params: Tuple[float, ...]) -> float:
    """Cache results of computation-heavy functions.

    Automatically caches up to 128 most recent calls
    based on input parameters.
    """
    # Simulate expensive calculation
    result = sum(p**2 for p in params) ** 0.5
    return result


print("\nProfessional function patterns ready for production data pipelines!")
