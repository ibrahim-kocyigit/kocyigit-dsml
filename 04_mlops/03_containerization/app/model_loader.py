"""
Model leader utility.

Loads the trained Iris Pipeline from dist at application startup.

The model artifact was created in 04_mlops/01_model_persistence/01_pickle_and_joblib.ipynb
"""

from pathlib import Path
import joblib
import os

# Path to the model artifact (can be set via the MODEL_PATH environment variable, otherwise defaults to the path that works when running locally from 02_api_development/)
MODEL_PATH = Path(
    os.environ.get(
        "MODEL_PATH",  # Default: the path that works when running locally from 02_api_development/
        str(
            Path(__file__).resolve().parent.parent.parent
            / "01_model_persistence"
            / "models"
            / "iris_pipeline.joblib"
        ),
    )
)

# Target class names (must match the order used during model training.
# Best practice would have been to save this as part of the model artifact, but for simplicity we hardcode it here)
TARGET_NAMES = ["setosa", "versicolor", "virginica"]


def load_pipeline():
    """
    Load the saved Pipeline from disk and return it.

    Returns:
        sklearn.pipeline.Pipeline: The trained Iris classification pipeline.

    Raises:
        FileNotFoundError: If the model file does not exist at the specified path.
    """

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}"
            f"Please run the 01_model_persistence/01_pickle_and_joblib.ipynb notebook first "
            f"to generate the model artifact."
        )

    return joblib.load(MODEL_PATH)
