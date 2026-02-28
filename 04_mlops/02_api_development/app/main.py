"""
Iris Prediction API

A FastAPI application that serves predictions from the Iris classification Pipeline
trained in the Model Persistence section.

Run from the 02_api_development directory with:
> uvicorn main:app --reload
"""

from contextlib import asynccontextmanager
import numpy as np
from fastapi import FastAPI

from app.model_loader import load_pipeline, TARGET_NAMES
from app.schemas import IrisFeatures, IrisPrediction


# ---------------------------------------------------------------------------
# Model Storage: Loaded once at startup, shared across all requests
# ---------------------------------------------------------------------------
ml_model: dict = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the model at startup and clear it on shutdown."""
    ml_model["pipeline"] = load_pipeline()
    print("✅ Model loaded successfully.")
    yield
    ml_model.clear()
    print("🧹 Model cleared from memory.")


# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Iris Prediction API",
    description="A simple API that predicts Iris flower species from sepal and petal measurements.",
    version="1.0.0",
    lifespan=lifespan,
)


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    """Health check endpoint for monitoring and deployment verification."""
    return {
        "status": "healthy",
        "model_loaded": "pipeline" in ml_model,
    }


@app.post("/predict", response_model=IrisPrediction)
def predict(features: IrisFeatures):
    """Predict the Iris species for a single sample."""
    X = np.array(
        [
            [
                features.sepal_length,
                features.sepal_width,
                features.petal_length,
                features.petal_width,
            ]
        ]
    )

    pipeline = ml_model["pipeline"]
    prediction_id = int(pipeline.predict(X)[0])
    probabilities = pipeline.predict_proba(X)[0]

    return IrisPrediction(
        prediction=TARGET_NAMES[prediction_id],
        prediction_id=prediction_id,
        probabilities={
            name: round(float(prob), 4)
            for name, prob in zip(TARGET_NAMES, probabilities)
        },
    )


@app.post("/predict/batch", response_model=list[IrisPrediction])
def predict_batch(samples: list[IrisFeatures]):
    """Predict the Iris species for multiple samples in one request."""
    X = np.array(
        [
            [s.sepal_length, s.sepal_width, s.petal_length, s.petal_width]
            for s in samples
        ]
    )

    pipeline = ml_model["pipeline"]
    predictions = pipeline.predict(X)
    probabilities = pipeline.predict_proba(X)

    return [
        IrisPrediction(
            prediction=TARGET_NAMES[int(pred)],
            prediction_id=int(pred),
            probabilities={
                name: round(float(prob), 4) for name, prob in zip(TARGET_NAMES, probs)
            },
        )
        for pred, probs in zip(predictions, probabilities)
    ]
