"""
Pydantic schemas for the Iris prediction API.

These schemas define the contract between the client and the server:
- What data the API expects (IrisFeatures)
- What data the API returns (IrisPrediction)
"""

from pydantic import BaseModel, Field


class IrisFeatures(BaseModel):
    """Input schema: The 4 features the Iris Pipeline expects."""

    sepal_length: float = Field(..., gt=0, le=10, description="Sepal length in cm")
    sepal_width: float = Field(..., gt=0, le=6, description="Sepal width in cm")
    petal_length: float = Field(..., gt=0, le=8, description="Petal length in cm")
    petal_width: float = Field(..., gt=0, le=4, description="Petal width in cm")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sepal_length": 5.1,
                    "sepal_width": 3.5,
                    "petal_length": 1.4,
                    "petal_width": 0.2,
                }
            ]
        }
    }


class IrisPrediction(BaseModel):
    """Output schema: The prediction the API returns."""

    prediction: str
    prediction_id: int
    probabilities: dict[str, float]
