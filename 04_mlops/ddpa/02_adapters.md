# Adapters: The Outside of the Hexagon

Adapters are **everything outside the hexagon**. They are the concrete implementations that connect the domain to the real world — HTTP frameworks, databases, ML model files, file systems, external APIs. Each adapter plugs into a **port** defined by the domain, conforming to the domain's contract rather than imposing its own.

The hexagon never reaches outward. It declares what it needs (ports), and adapters reach inward to fulfill those declarations. This means:

* The domain has **zero knowledge** of which adapters are connected. It doesn't know whether predictions are stored in PostgreSQL or a CSV file, whether classifications come from scikit-learn or a remote model server, whether requests arrive over HTTP or from a CLI.
* Adapters can be **swapped, added, or removed** without touching domain code. Migrating from SQLite to PostgreSQL, or adding a CLI alongside the REST API, is an adapter-level change only.
* Each adapter has **exactly one job**: translate between the outside world's language and the domain's language. A REST adapter translates JSON into domain objects and domain objects back into JSON. A database adapter translates domain entities into rows and rows back into entities. An ML adapter translates domain value objects into numpy arrays and model outputs back into domain value objects.

## Inbound vs. Outbound Adapters

Adapters come in two flavors, mirroring the two kinds of ports:

* **Inbound adapters** (also called **driving adapters** or **primary adapters**) are the entry points to the system. They receive external input — an HTTP request, a CLI command, a message from a queue — and translate it into a call on an Application Service inside the hexagon. They *drive* the application.

* **Outbound adapters** (also called **driven adapters** or **secondary adapters**) are the exit points. They implement the driven ports that the domain defines — persisting data, calling external services, loading ML models. The application *drives* them through the port interfaces.

```
                    ┌─────────────────────────────────────┐
                    │          THE HEXAGON (Domain)       │
  ┌───────────┐     │                                     │     ┌───────────────┐
  │  REST API │────▶│  Application    Domain    Ports     │────▶│  SQLite       │
  │ (inbound) │     │  Services       Objects  (driven)   │     │  (outbound)   │
  └───────────┘     │                                     │     └───────────────┘
  ┌───────────┐     │                                     │     ┌───────────────┐
  │    CLI    │────▶│                                     │────▶│  scikit-learn │
  │ (inbound) │     │                                     │     │  (outbound)   │
  └───────────┘     └─────────────────────────────────────┘     └───────────────┘
```

The arrows always point **inward**: inbound adapters depend on Application Services, outbound adapters implement domain ports. The hexagon depends on nothing outside itself.

## Outbound Adapters

We start with outbound adapters because they fulfill the contracts the domain has already defined. An inbound adapter can't do anything useful until the outbound adapters are in place — you can't classify a flower through the API if there's no classifier implementation to call.

### The ML Model Adapter

The `IrisClassifier` port declared: "Given a `FlowerMeasurement`, return a `SpeciesClassification`." The domain doesn't care how. Here's the scikit-learn implementation:

```python
# --- adapters/outbound/sklearn_classifier.py

import numpy as np
import joblib
from pathlib import Path

from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.ports.classifier import IrisClassifier

# Mapping from model output indices to domain enum values
_SPECIES_MAPPING: dict[int, IrisSpecies] = {
    0: IrisSpecies.SETOSA,
    1: IrisSpecies.VERSICOLOR,
    2: IrisSpecies.VIRGINICA,
}

class SklearnClassifier(IrisClassifier):
    """Outbound adapter: bridges scikit-learn to the IrisClassifier port."""

    def __init__(self, model_path: Path):
        self._model = joblib.load(model_path)

    def classify(self, measurement: FlowerMeasurement) -> SpeciesClassification:
        features = np.array([[
            measurement.sepal_length,
            measurement.sepal_width,
            measurement.petal_length,
            measurement.petal_width,
        ]])
        prediction_idx = int(self._model.predict(features)[0])
        probabilities = self._model.predict_proba(features)[0]
        species = _SPECIES_MAPPING[prediction_idx]
        confidence = float(probabilities[prediction_idx])
        return SpeciesClassification(species=species, confidence=confidence)
```

Several design decisions deserve attention:

**The adapter translates in both directions.**
Inward: it converts a `FlowerMeasurement` (domain language) into a numpy array (scikit-learn language). Outward: it converts the model's integer prediction and probability array back into a `SpeciesClassification` (domain language). The domain never sees numpy, and scikit-learn never sees domain objects. The adapter is the translator between two languages.

**`_SPECIES_MAPPING` is adapter-level knowledge.**
The fact that scikit-learn encodes setosa as `0`, versicolor as `1`, and virginica as `2` is an artifact of how the model was trained — it's infrastructure knowledge, not domain knowledge. The mapping lives in the adapter, not in the domain's `IrisSpecies` enum.

**Model loading happens at construction time.**
The `__init__` method loads the serialized model once. The `classify` method is then a fast, stateless prediction call. This keeps the per-request path efficient — there's no file I/O during classification.

**`model_path` is a constructor parameter, not a hardcoded constant.**
Where the model file lives on disk is a deployment concern. Different environments (development, staging, production) will have different paths. The adapter receives this information at construction time from the composition root (covered later), keeping the adapter itself environment-agnostic.

> 📌 If you later need to swap in a different ML framework — say a PyTorch model or a remote model served via HTTP — you write a new adapter class that implements `IrisClassifier`. The domain, the Application Services, the inbound adapters, and all tests that use the `IrisClassifier` port remain untouched. This is the core promise of Ports & Adapters.

### The Persistence Adapter

The `PredictionRepository` port declared three capabilities: save, get by ID, and get predictions since a timestamp. Here's a SQLite implementation suitable for the production system described in the Business Understanding:

```python
# --- adapters/outbound/sqlite_prediction_repository.py

import sqlite3
from uuid import UUID
from datetime import datetime
from pathlib import Path

from domain.objects.prediction import Prediction
from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.ports.prediction_repository import PredictionRepository
from domain.exceptions import PredictionNotFoundError


class SqlitePredictionRepository(PredictionRepository):
    """Outbound adapter: persists predictions to a SQLite database."""

    def __init__(self, db_path: Path):
        self._db_path = db_path
        self._ensure_table()

    def _ensure_table(self) -> None:
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS predictions (
                    id TEXT PRIMARY KEY,
                    sepal_length REAL NOT NULL,
                    sepal_width REAL NOT NULL,
                    petal_length REAL NOT NULL,
                    petal_width REAL NOT NULL,
                    species TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    created_at TEXT NOT NULL,
                    reviewed INTEGER NOT NULL DEFAULT 0,
                    expert_correction_species TEXT,
                    expert_correction_confidence REAL
                )
            """)

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self._db_path)

    def save(self, prediction: Prediction) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO predictions
                (id, sepal_length, sepal_width, petal_length, petal_width,
                 species, confidence, created_at, reviewed,
                 expert_correction_species, expert_correction_confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    str(prediction.id),
                    prediction.measurement.sepal_length,
                    prediction.measurement.sepal_width,
                    prediction.measurement.petal_length,
                    prediction.measurement.petal_width,
                    prediction.classification.species.name,
                    prediction.classification.confidence,
                    prediction.created_at.isoformat(),
                    int(prediction.reviewed),
                    (prediction.expert_correction.species.name
                     if prediction.expert_correction else None),
                    (prediction.expert_correction.confidence
                     if prediction.expert_correction else None),
                ),
            )

    def get_by_id(self, prediction_id: UUID) -> Prediction:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM predictions WHERE id = ?",
                (str(prediction_id),),
            ).fetchone()
        if row is None:
            raise PredictionNotFoundError(prediction_id)
        return self._row_to_prediction(row)

    def get_predictions_since(self, since: datetime) -> list[Prediction]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM predictions WHERE created_at >= ? ORDER BY created_at",
                (since.isoformat(),),
            ).fetchall()
        return [self._row_to_prediction(row) for row in rows]

    def _row_to_prediction(self, row) -> Prediction:
        """Reconstruct a Prediction entity from a database row."""
        measurement = FlowerMeasurement(
            sepal_length=row[1],
            sepal_width=row[2],
            petal_length=row[3],
            petal_width=row[4],
        )
        classification = SpeciesClassification(
            species=IrisSpecies[row[5]],
            confidence=row[6],
        )
        prediction = Prediction(
            measurement=measurement,
            classification=classification,
        )
        # Restore internal state that is normally init=False
        object.__setattr__(prediction, "id", UUID(row[0]))
        object.__setattr__(prediction, "created_at", datetime.fromisoformat(row[7]))
        object.__setattr__(prediction, "reviewed", bool(row[8]))
        if row[9] is not None:
            correction = SpeciesClassification(
                species=IrisSpecies[row[9]],
                confidence=row[10],
            )
            object.__setattr__(prediction, "expert_correction", correction)
        return prediction
```

**The adapter flattens domain objects into columns and reconstructs them on the way out.**
A `Prediction` in the domain is a rich object graph: an entity containing value objects. In the database, it's a flat row. The adapter is solely responsible for this mapping. The domain never knows its objects were flattened, and the database schema never leaks into the domain.

**`_row_to_prediction` handles the reconstruction of `init=False` fields.**
Fields like `id`, `created_at`, and `reviewed` are set automatically at construction time and cannot be passed to `__init__`. When reconstructing from a database, we need to restore the *actual* stored values. `object.__setattr__` bypasses `@dataclass` restrictions to set these fields directly. This is an infrastructure concern — it exists only in the adapter. The domain's invariants (auto-generated ID, auto-set timestamp) still hold for *newly created* predictions.

**`INSERT OR REPLACE` serves as a simple upsert.**
When a prediction is first saved, it's an insert. When it's saved again after a review (with `reviewed=True` and possibly `expert_correction` set), it replaces the existing row. For a system of this scale — a few hundred predictions per day — this is pragmatic and sufficient.

**`get_by_id` raises `PredictionNotFoundError`, not a SQLite-specific error.**
This is the critical error-handling pattern for outbound adapters: the adapter **translates infrastructure errors into domain exceptions**. The port contract specifies that `get_by_id` raises `PredictionNotFoundError` when a prediction doesn't exist. The SQLite adapter fulfils this by checking for a `None` row. A PostgreSQL adapter might catch `psycopg2.ProgrammingError`. A DynamoDB adapter might catch `ClientError`. Each adapter absorbs its own infrastructure errors and raises the domain exception that callers expect. The Application Service and inbound adapters never need to know which database is behind the port — the error language is always the domain's language.

> ⚠️ **Why SQLite?** The Business Understanding doc describes a system processing a few hundred requests per day, used by a small team of interns, within a 3-month campaign. SQLite is file-based, requires no server setup, is trivially portable, and handles this workload effortlessly. If NovaCure later decides to scale the system across multiple workers or data centers, swapping to PostgreSQL means writing a new adapter — the domain and all other adapters stay unchanged. Choose the simplest technology that meets the actual requirements.

### The CSV Exporter Adapter

The quality team needs to periodically export predictions for review. This is an outbound adapter that serves its own port. Let's define the port first:

```python
# --- domain/ports/prediction_exporter.py

from abc import ABC, abstractmethod
from domain.objects.prediction import Prediction

class PredictionExporter(ABC):
    """Driven port: exports predictions for external review.
    
    The quality team needs periodic exports of predictions to compare 
    against expert spot-checks. How and where the export is written 
    is an adapter concern.
    """

    @abstractmethod
    def export(self, predictions: list[Prediction], destination: str) -> None:
        pass
```

And the CSV adapter:

```python
# --- adapters/outbound/csv_prediction_exporter.py

import csv
from pathlib import Path
from domain.objects.prediction import Prediction
from domain.ports.prediction_exporter import PredictionExporter


class CsvPredictionExporter(PredictionExporter):
    """Outbound adapter: exports predictions to a CSV file."""

    def export(self, predictions: list[Prediction], destination: str) -> None:
        path = Path(destination)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "id", "created_at",
                "sepal_length", "sepal_width", "petal_length", "petal_width",
                "predicted_species", "confidence",
                "reviewed", "expert_correction", "was_correct",
            ])
            for p in predictions:
                writer.writerow([
                    str(p.id),
                    p.created_at.isoformat(),
                    p.measurement.sepal_length,
                    p.measurement.sepal_width,
                    p.measurement.petal_length,
                    p.measurement.petal_width,
                    p.classification.species.name,
                    f"{p.classification.confidence:.4f}",
                    p.reviewed,
                    (p.expert_correction.species.name
                     if p.expert_correction else ""),
                    p.was_correct if p.reviewed else "",
                ])
```

**The adapter decides the format; the domain decides the content.**
Which fields to expose — `was_correct`, `final_classification`, `confidence` — are properties of the domain objects. How to serialize them (CSV columns, header names, float formatting) is the adapter's call.

**`destination` is a string, not a `Path`.**
The port defines `destination: str` because the *concept* of "where to export" is domain-relevant, but the *type* (`Path`, S3 URI, etc.) is adapter-specific. The CSV adapter interprets it as a file path. A future S3 adapter would interpret it as a bucket key. The port stays generic.

### The In-Memory Adapter (for Testing)

A lightweight in-memory implementation of `PredictionRepository` is essential for testing. It satisfies the same port contract as `SqlitePredictionRepository` but requires no database, no file system, and no setup:

```python
# --- adapters/outbound/in_memory_prediction_repository.py

from uuid import UUID
from datetime import datetime
from domain.objects.prediction import Prediction
from domain.ports.prediction_repository import PredictionRepository
from domain.exceptions import PredictionNotFoundError


class InMemoryPredictionRepository(PredictionRepository):
    """Outbound adapter: in-memory repository for testing and development."""

    def __init__(self):
        self._store: dict[UUID, Prediction] = {}

    def save(self, prediction: Prediction) -> None:
        self._store[prediction.id] = prediction

    def get_by_id(self, prediction_id: UUID) -> Prediction:
        if prediction_id not in self._store:
            raise PredictionNotFoundError(prediction_id)
        return self._store[prediction_id]

    def get_predictions_since(self, since: datetime) -> list[Prediction]:
        return [
            p for p in self._store.values()
            if p.created_at >= since
        ]
```

**`get_by_id` raises `PredictionNotFoundError` — the same domain exception as the SQLite adapter.**
This is the port contract in action. Every adapter implementing `PredictionRepository` must raise the same domain exception for the same failure condition. The in-memory adapter doesn't raise `KeyError`; the SQLite adapter doesn't return `None`; a PostgreSQL adapter wouldn't raise `psycopg2.Error`. They all speak the domain's error language. This consistency is what allows Application Services and inbound adapters to handle errors without knowing which adapter is behind the port.

This is a full, legitimate adapter — not a mock, not a test double, not a hack. It implements the same contract as the SQLite adapter. The domain and Application Services don't know or care which one they're talking to. This is the Liskov Substitution Principle in action: any adapter implementing a port can substitute for any other without changing the system's behavior.

> #### When to Use In-Memory Adapters vs. Mocks
>
> In-memory adapters are **preferred over mocks** for testing domain and Application Service logic because:
>
> * They exercise real behavior: `save` actually stores, `get_by_id` actually retrieves. A mock that returns a canned response doesn't verify that save-then-retrieve works.
> * They don't couple tests to implementation details: you're testing *what* happens, not *how many times* a method was called or in what order.
> * They're reusable: the same `InMemoryPredictionRepository` works in every test that needs a repository, without per-test mock configuration.
>
> Reserve mocks for verifying that *side effects* occurred — e.g., confirming that a notification was sent. For data flow (save/load/query), in-memory adapters are more faithful and less brittle.

## Inbound Adapters

Inbound adapters are the entry points to the system. They receive external requests, translate them into domain language, call an Application Service, and translate the response back into the external format.

Crucially, inbound adapters are also the **error boundary** — the place where domain exceptions are caught and translated into external-format responses. The domain raises exceptions in its own vocabulary (`PredictionNotFoundError`, `InvalidMeasurementError`). The inbound adapter catches them and produces the appropriate external response (an HTTP 404, a CLI error message, a gRPC status code).

### The REST API Adapter

The Business Understanding doc specifies two delivery mechanisms: a web interface for interns and an API endpoint for NovaCure's systems. FastAPI can serve both — it handles REST endpoints natively and can serve a simple HTML form.

```python
# --- adapters/inbound/api.py

from uuid import UUID
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.services.classification_service import ClassificationService
from domain.services.review_service import ReviewService
from domain.exceptions import (
    DomainError,
    PredictionNotFoundError,
    PredictionAlreadyReviewedError,
    InvalidMeasurementError,
)


# --- Request and Response schemas (Pydantic models) ---

class ClassifyRequest(BaseModel):
    """Inbound DTO: what the API expects from the client."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    @field_validator("sepal_length", "sepal_width", "petal_length", "petal_width")
    @classmethod
    def must_be_positive(cls, v: float, info) -> float:
        if v <= 0:
            raise ValueError(f"{info.field_name} must be positive")
        return v


class ClassifyResponse(BaseModel):
    """Outbound DTO: what the API returns to the client."""
    prediction_id: str
    species: str
    is_versicolor: bool
    confidence: float


class ReviewRequest(BaseModel):
    """Inbound DTO for expert review submissions."""
    correction_species: str | None = None
    correction_confidence: float | None = None

    @field_validator("correction_species")
    @classmethod
    def must_be_valid_species(cls, v: str | None) -> str | None:
        if v is not None and v not in IrisSpecies.__members__:
            raise ValueError(
                f"Unknown species: {v}. Must be one of {list(IrisSpecies.__members__)}"
            )
        return v


class QualityReportResponse(BaseModel):
    """Outbound DTO for quality report data."""
    total_predictions: int
    reviewed_count: int
    versicolor_precision: float | None
    quality_acceptable: bool


class ErrorResponse(BaseModel):
    """Standardized error response body."""
    error_type: str
    message: str
    details: dict | None = None


# --- API factory ---

def create_api(
    classification_service: ClassificationService,
    review_service: ReviewService,
) -> FastAPI:
    """Factory function that creates the FastAPI app with injected dependencies."""

    app = FastAPI(title="Iris Classification API")

    @app.post("/classify", response_model=ClassifyResponse)
    def classify_flower(request: ClassifyRequest) -> ClassifyResponse:
        measurement = FlowerMeasurement(
            sepal_length=request.sepal_length,
            sepal_width=request.sepal_width,
            petal_length=request.petal_length,
            petal_width=request.petal_width,
        )
        prediction = classification_service.classify_flower(measurement)
        return ClassifyResponse(
            prediction_id=str(prediction.id),
            species=prediction.classification.species.name,
            is_versicolor=prediction.classification.is_versicolor,
            confidence=prediction.classification.confidence,
        )

    @app.post("/predictions/{prediction_id}/review")
    def review_prediction(prediction_id: str, request: ReviewRequest) -> dict:
        correction = None
        if request.correction_species is not None:
            correction = SpeciesClassification(
                species=IrisSpecies[request.correction_species],
                confidence=request.correction_confidence or 1.0,
            )
        review_service.review_prediction(
            prediction_id=UUID(prediction_id),
            correction=correction,
        )
        return {"status": "reviewed", "prediction_id": prediction_id}

    @app.get("/quality-report", response_model=QualityReportResponse)
    def quality_report(since_days: int = 7) -> QualityReportResponse:
        since = datetime.now(timezone.utc) - timedelta(days=since_days)
        report = review_service.get_quality_report(since=since)
        return QualityReportResponse(**report)

    # --- Error handlers ---

    @app.exception_handler(InvalidMeasurementError)
    async def handle_invalid_measurement(request, exc: InvalidMeasurementError):
        return _error_response(
            status_code=422,
            error_type="invalid_measurement",
            message=str(exc),
            details={
                "field": exc.field_name,
                "value": exc.value,
                "reason": exc.reason,
            },
        )

    @app.exception_handler(PredictionNotFoundError)
    async def handle_prediction_not_found(request, exc: PredictionNotFoundError):
        return _error_response(
            status_code=404,
            error_type="not_found",
            message=str(exc),
            details={"prediction_id": str(exc.prediction_id)},
        )

    @app.exception_handler(PredictionAlreadyReviewedError)
    async def handle_already_reviewed(request, exc: PredictionAlreadyReviewedError):
        return _error_response(
            status_code=409,
            error_type="already_reviewed",
            message=str(exc),
            details={"prediction_id": str(exc.prediction_id)},
        )

    @app.exception_handler(DomainError)
    async def handle_domain_error(request, exc: DomainError):
        return _error_response(
            status_code=400,
            error_type="domain_error",
            message=str(exc),
        )

    return app


def _error_response(
    status_code: int,
    error_type: str,
    message: str,
    details: dict | None = None,
):
    from fastapi.responses import JSONResponse
    body = ErrorResponse(
        error_type=error_type,
        message=message,
        details=details,
    )
    return JSONResponse(status_code=status_code, content=body.model_dump())
```

This adapter is dense, so let's unpack the key architectural patterns:

**Request/response translation is the adapter's sole responsibility.**
`ClassifyRequest` (Pydantic) is the external-facing contract — what the API client sends. `FlowerMeasurement` (domain) is the internal representation. The adapter converts between them. The domain never sees Pydantic models, and the API client never sees domain objects. This is the adapter doing its job: translating between two languages.

**Validation happens at two levels, for different reasons.**
Pydantic's `field_validator` catches HTTP-level input problems (negative numbers, missing fields) and returns clean 422 responses before the request ever reaches the domain. The domain's `FlowerMeasurement.__post_init__` catches domain-level problems (implausible measurements like a 20 cm sepal). Both are needed: the API adapter handles transport-level validation, the domain handles business-level validation. The Pydantic layer is a convenience for the API client — it gives fast, format-appropriate feedback. The domain layer is the safety net — it protects invariants regardless of which adapter is calling.

**`create_api` is a factory function, not a global `app` object.**
The Application Services (`classification_service`, `review_service`) are injected as parameters. This means:
* The adapter has no idea how the services were constructed or what adapters back them.
* In tests, you can inject services backed by in-memory adapters.
* In production, you inject services backed by SQLite and scikit-learn.
* The wiring happens in the composition root (covered next), not in the adapter itself.

**The endpoint handlers contain no `try/except` blocks.**
This is a deliberate design choice. Rather than scattering error handling across every endpoint, domain exceptions propagate naturally and are caught by **centralized exception handlers** registered on the FastAPI app. This keeps the endpoint handlers focused on their primary job — translation and orchestration — and centralizes error-to-HTTP mapping in one place.

**Exception handlers are layered from specific to general.**
FastAPI matches exception handlers by type specificity. The handler chain works as:

1. `InvalidMeasurementError` → 422 with field-level detail
2. `PredictionNotFoundError` → 404 with the missing prediction ID
3. `PredictionAlreadyReviewedError` → 409 (conflict) with the prediction ID
4. `DomainError` (the base class) → 400 as a catch-all for any domain error we haven't explicitly mapped

This structure is maintainable: when a new domain exception is added, you either register a specific handler for it (if it needs a particular status code or response shape) or let the `DomainError` fallback handle it with a generic 400. No endpoint code changes either way.

**Each handler uses the exception's structured data, not its message string.**
`InvalidMeasurementError` carries `field_name`, `value`, and `reason` as typed attributes. The handler builds a structured JSON response from these fields. The human-readable `str(exc)` goes into the `message` field as a convenience, but the `details` dict is what API clients should parse programmatically. This is why domain exceptions carry structured data — so that every adapter can extract what it needs without string parsing.

**`ErrorResponse` is a Pydantic model, like all other API responses.**
Error responses deserve the same structure and consistency as success responses. A client consuming this API can always expect `{"error_type": "...", "message": "...", "details": ...}` on failure, regardless of which endpoint failed or why. This is the adapter's contract with the outside world.

> #### Why not put DTOs (Request/Response models) inside the domain?
>
> In Clean Architecture, request and response models live in a dedicated Application layer between the domain and the interface. In Ports & Adapters, they live *in the adapter* — because they are an infrastructure concern. `ClassifyRequest` exists because we chose FastAPI. If we added a CLI adapter, it would have its own input parsing, not reuse Pydantic models. If we added a gRPC adapter, it would use protobuf. Each adapter speaks its own external language and translates to/from the one shared internal language: domain objects.

> #### The Error Handling Flow, End to End
>
> Let's trace a concrete error through the system to see how each layer plays its role:
>
> 1. An intern submits a measurement with `petal_width: -0.5` through the API.
> 2. **Pydantic validation** catches the negative value and returns a 422 immediately. The domain is never called. This is a transport-level guard.
> 3. Now suppose an intern submits `petal_width: 18.0` — positive, so Pydantic passes it through.
> 4. The endpoint handler constructs `FlowerMeasurement(petal_width=18.0)`.
> 5. **`FlowerMeasurement.__post_init__`** raises `InvalidMeasurementError(field_name="petal_width", value=18.0, reason="outside the plausible range for Iris flowers")`.
> 6. The exception propagates up — through the Application Service (which doesn't catch it), through the endpoint handler (which doesn't catch it either), to FastAPI's exception handling machinery.
> 7. **The `handle_invalid_measurement` exception handler** catches it and returns a 422 with `{"error_type": "invalid_measurement", "details": {"field": "petal_width", "value": 18.0, "reason": "outside the plausible range..."}}`.
>
> At no point did any layer parse a string, guess at an error type, or use a broad `except Exception`. Each layer raised or translated errors using typed, structured domain vocabulary.

## The Composition Root

Every Ports & Adapters system needs a place where the two zones meet — where concrete adapters are instantiated and plugged into the ports that Application Services expect. This is the **composition root**: the single location in the codebase that knows about *all* concrete implementations.

The composition root is **not** part of the domain. It's not part of any adapter either. It's the application's entry point — the `main.py` that assembles the system:

```python
# --- main.py

from pathlib import Path
from domain.services.classification_service import ClassificationService
from domain.services.review_service import ReviewService
from adapters.outbound.sklearn_classifier import SklearnClassifier
from adapters.outbound.sqlite_prediction_repository import SqlitePredictionRepository
from adapters.inbound.api import create_api


def bootstrap() -> None:
    """Assemble the application: instantiate adapters, wire into services, start."""

    # --- Outbound adapters ---
    classifier = SklearnClassifier(
        model_path=Path("models/iris_classifier.joblib"),
    )
    prediction_repository = SqlitePredictionRepository(
        db_path=Path("data/predictions.db"),
    )

    # --- Application services (inside the hexagon) ---
    classification_service = ClassificationService(
        classifier=classifier,
        prediction_repository=prediction_repository,
    )
    review_service = ReviewService(
        prediction_repository=prediction_repository,
    )

    # --- Inbound adapter ---
    app = create_api(
        classification_service=classification_service,
        review_service=review_service,
    )

    # --- Start ---
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    bootstrap()
```

**This is the only file in the entire codebase that imports concrete adapter classes.**
The domain imports nothing from adapters. The adapters import from the domain (ports and objects). But `main.py` imports from *both* — it's the one place where the system is assembled. This is a deliberate architectural violation confined to a single file, because *someone* has to plug the pieces together.

**The wiring order reflects the dependency structure.**
Outbound adapters are created first (they have no dependencies on the domain beyond the port interfaces). Application Services are created next, receiving the outbound adapters as constructor arguments. Inbound adapters are created last, receiving the Application Services. The dependency flow is always inward: inbound → services → outbound.

**Configuration is explicit, not magical.**
Model paths, database paths, host, port — all are visible and changeable in one place. For a system of this scale, this is sufficient. For larger systems, you'd extract configuration into environment variables or a config file, but the composition root remains the place that reads and applies them.

### Testing with a Different Composition

The composition root pattern makes it trivial to wire the system differently for tests:

```python
# --- tests/conftest.py

import pytest
from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.ports.classifier import IrisClassifier
from domain.services.classification_service import ClassificationService
from domain.services.review_service import ReviewService
from adapters.outbound.in_memory_prediction_repository import InMemoryPredictionRepository


class StubClassifier(IrisClassifier):
    """Always returns versicolor with high confidence."""

    def classify(self, measurement: FlowerMeasurement) -> SpeciesClassification:
        return SpeciesClassification(
            species=IrisSpecies.VERSICOLOR, confidence=0.95,
        )


@pytest.fixture
def prediction_repository():
    return InMemoryPredictionRepository()


@pytest.fixture
def classification_service(prediction_repository):
    return ClassificationService(
        classifier=StubClassifier(),
        prediction_repository=prediction_repository,
    )


@pytest.fixture
def review_service(prediction_repository):
    return ReviewService(prediction_repository=prediction_repository)
```

**Same Application Services, different adapters.**
`ClassificationService` doesn't know or care that it's backed by a stub classifier and an in-memory repository. The tests exercise the real orchestration logic — the same code that runs in production — with fast, deterministic, infrastructure-free adapters.

This is the payoff of the entire architecture: **the domain is tested in isolation, at full speed, with complete confidence that the logic being tested is the same logic that runs in production.** The only thing that changes between test and production is which adapters are plugged in — and that's a one-line change in the composition root.

## Testing Strategy Across Zones

Different parts of the system demand different testing approaches:

### Domain Tests (Unit Tests)

Domain objects, domain services, and application services are tested with **unit tests** using in-memory adapters. No external dependencies, no setup, millisecond execution.

```python
# --- tests/domain/test_prediction.py

from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.objects.prediction import Prediction
from domain.exceptions import PredictionAlreadyReviewedError, InvalidMeasurementError


def test_new_prediction_is_unreviewed():
    prediction = Prediction(
        measurement=FlowerMeasurement(5.9, 2.8, 4.1, 1.3),
        classification=SpeciesClassification(IrisSpecies.VERSICOLOR, 0.92),
    )
    assert not prediction.reviewed
    assert prediction.was_correct is None


def test_reviewed_prediction_with_no_correction_is_correct():
    prediction = Prediction(
        measurement=FlowerMeasurement(5.9, 2.8, 4.1, 1.3),
        classification=SpeciesClassification(IrisSpecies.VERSICOLOR, 0.92),
    )
    prediction.mark_reviewed(correction=None)
    assert prediction.was_correct is True
    assert prediction.final_classification.is_versicolor


def test_cannot_review_prediction_twice():
    prediction = Prediction(
        measurement=FlowerMeasurement(5.9, 2.8, 4.1, 1.3),
        classification=SpeciesClassification(IrisSpecies.VERSICOLOR, 0.92),
    )
    prediction.mark_reviewed()
    try:
        prediction.mark_reviewed()
        assert False, "Should have raised PredictionAlreadyReviewedError"
    except PredictionAlreadyReviewedError:
        pass


def test_invalid_measurement_raises_domain_exception():
    try:
        FlowerMeasurement(sepal_length=-1.0, sepal_width=2.8,
                          petal_length=4.1, petal_width=1.3)
        assert False, "Should have raised InvalidMeasurementError"
    except InvalidMeasurementError as e:
        assert e.field_name == "sepal_length"
        assert e.value == -1.0
        assert "positive" in e.reason
```

**Tests assert on structured exception data, not just that an exception was raised.**
`test_invalid_measurement_raises_domain_exception` checks `e.field_name`, `e.value`, and `e.reason` — the same fields that the API error handler will use to build its response. This verifies that the domain provides the information adapters need, not just that it fails in the right circumstances.

### Application Service Tests (Integration-within-Hexagon)

These test the orchestration logic with in-memory adapters. They verify that the Application Service sequences operations correctly and that the domain objects interact as expected.

```python
# --- tests/domain/test_classification_service.py

from domain.objects.flower_measurement import FlowerMeasurement
from domain.services.classification_service import ClassificationService


def test_classify_flower_saves_and_returns_prediction(
    classification_service, prediction_repository
):
    measurement = FlowerMeasurement(5.9, 2.8, 4.1, 1.3)
    prediction = classification_service.classify_flower(measurement)

    assert prediction.classification.is_versicolor
    assert prediction.measurement == measurement

    # Verify it was persisted
    saved = prediction_repository.get_by_id(prediction.id)
    assert saved == prediction
```

```python
# --- tests/domain/test_review_service.py

from uuid import uuid4
from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.objects.prediction import Prediction
from domain.exceptions import PredictionNotFoundError, PredictionAlreadyReviewedError


def test_review_prediction_marks_as_reviewed(
    review_service, prediction_repository
):
    prediction = Prediction(
        measurement=FlowerMeasurement(5.9, 2.8, 4.1, 1.3),
        classification=SpeciesClassification(IrisSpecies.VERSICOLOR, 0.92),
    )
    prediction_repository.save(prediction)

    review_service.review_prediction(prediction_id=prediction.id, correction=None)

    updated = prediction_repository.get_by_id(prediction.id)
    assert updated.reviewed is True
    assert updated.was_correct is True


def test_review_nonexistent_prediction_raises_not_found(review_service):
    try:
        review_service.review_prediction(prediction_id=uuid4(), correction=None)
        assert False, "Should have raised PredictionNotFoundError"
    except PredictionNotFoundError:
        pass


def test_review_already_reviewed_raises_error(
    review_service, prediction_repository
):
    prediction = Prediction(
        measurement=FlowerMeasurement(5.9, 2.8, 4.1, 1.3),
        classification=SpeciesClassification(IrisSpecies.VERSICOLOR, 0.92),
    )
    prediction_repository.save(prediction)
    review_service.review_prediction(prediction_id=prediction.id, correction=None)

    try:
        review_service.review_prediction(prediction_id=prediction.id, correction=None)
        assert False, "Should have raised PredictionAlreadyReviewedError"
    except PredictionAlreadyReviewedError:
        pass
```

**These tests verify the full error propagation chain.**
`test_review_nonexistent_prediction_raises_not_found` confirms that when the repository raises `PredictionNotFoundError`, it propagates cleanly through the Application Service. `test_review_already_reviewed_raises_error` confirms the same for entity-level invariant violations. In production, these exceptions would propagate further to the inbound adapter's exception handler and become HTTP 404 and 409 responses respectively. The domain tests verify the first half of that chain; the API tests verify the second.

### Adapter Tests (Integration Tests)

Outbound adapters that interact with real infrastructure need **integration tests** — tests that verify the adapter correctly translates between domain objects and the external system.

```python
# --- tests/adapters/test_sqlite_prediction_repository.py

import tempfile
from pathlib import Path
from datetime import datetime, timezone, timedelta
from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.objects.prediction import Prediction
from domain.exceptions import PredictionNotFoundError
from adapters.outbound.sqlite_prediction_repository import SqlitePredictionRepository


def test_save_and_retrieve_prediction():
    with tempfile.TemporaryDirectory() as tmp:
        repo = SqlitePredictionRepository(db_path=Path(tmp) / "test.db")
        prediction = Prediction(
            measurement=FlowerMeasurement(5.9, 2.8, 4.1, 1.3),
            classification=SpeciesClassification(IrisSpecies.VERSICOLOR, 0.92),
        )
        repo.save(prediction)
        loaded = repo.get_by_id(prediction.id)

        assert loaded.id == prediction.id
        assert loaded.measurement == prediction.measurement
        assert loaded.classification == prediction.classification
        assert loaded.reviewed == prediction.reviewed


def test_get_by_id_raises_domain_exception_for_missing_prediction():
    with tempfile.TemporaryDirectory() as tmp:
        repo = SqlitePredictionRepository(db_path=Path(tmp) / "test.db")
        from uuid import uuid4
        try:
            repo.get_by_id(uuid4())
            assert False, "Should have raised PredictionNotFoundError"
        except PredictionNotFoundError:
            pass


def test_get_predictions_since_filters_by_date():
    with tempfile.TemporaryDirectory() as tmp:
        repo = SqlitePredictionRepository(db_path=Path(tmp) / "test.db")
        prediction = Prediction(
            measurement=FlowerMeasurement(5.9, 2.8, 4.1, 1.3),
            classification=SpeciesClassification(IrisSpecies.VERSICOLOR, 0.92),
        )
        repo.save(prediction)

        # Predictions since an hour ago should include it
        results = repo.get_predictions_since(
            datetime.now(timezone.utc) - timedelta(hours=1)
        )
        assert len(results) == 1

        # Predictions since an hour from now should not
        results = repo.get_predictions_since(
            datetime.now(timezone.utc) + timedelta(hours=1)
        )
        assert len(results) == 0
```

**These tests use real SQLite databases — but temporary ones.**
The test creates a fresh database in a temp directory, exercises the adapter, and the directory is cleaned up automatically. This tests the actual SQL, the actual serialization, and the actual reconstruction — not mocked behavior.

**`test_get_by_id_raises_domain_exception_for_missing_prediction` is a critical adapter test.**
It verifies that the SQLite adapter correctly translates "no row found" into `PredictionNotFoundError` — the domain exception that the port contract requires. Without this test, a refactor of the adapter could accidentally break the error contract and surface SQLite-specific errors to the Application Service.

### API Tests (End-to-End within Process)

FastAPI's `TestClient` lets you test the full request-response cycle without starting a server:

```python
# --- tests/adapters/test_api.py

from fastapi.testclient import TestClient
from adapters.inbound.api import create_api


def test_classify_endpoint_returns_prediction(
    classification_service, review_service
):
    app = create_api(classification_service, review_service)
    client = TestClient(app)

    response = client.post("/classify", json={
        "sepal_length": 5.9,
        "sepal_width": 2.8,
        "petal_length": 4.1,
        "petal_width": 1.3,
    })

    assert response.status_code == 200
    data = response.json()
    assert data["is_versicolor"] is True
    assert "prediction_id" in data


def test_classify_endpoint_rejects_negative_values(
    classification_service, review_service
):
    app = create_api(classification_service, review_service)
    client = TestClient(app)

    response = client.post("/classify", json={
        "sepal_length": -1.0,
        "sepal_width": 2.8,
        "petal_length": 4.1,
        "petal_width": 1.3,
    })

    assert response.status_code == 422


def test_review_nonexistent_prediction_returns_404(
    classification_service, review_service
):
    app = create_api(classification_service, review_service)
    client = TestClient(app)

    response = client.post(
        "/predictions/00000000-0000-0000-0000-000000000000/review",
        json={},
    )

    assert response.status_code == 404
    data = response.json()
    assert data["error_type"] == "not_found"
    assert "prediction_id" in data["details"]


def test_double_review_returns_409(
    classification_service, review_service
):
    app = create_api(classification_service, review_service)
    client = TestClient(app)

    # Create a prediction first
    classify_response = client.post("/classify", json={
        "sepal_length": 5.9,
        "sepal_width": 2.8,
        "petal_length": 4.1,
        "petal_width": 1.3,
    })
    prediction_id = classify_response.json()["prediction_id"]

    # First review succeeds
    response = client.post(f"/predictions/{prediction_id}/review", json={})
    assert response.status_code == 200

    # Second review returns 409 Conflict
    response = client.post(f"/predictions/{prediction_id}/review", json={})
    assert response.status_code == 409
    data = response.json()
    assert data["error_type"] == "already_reviewed"
```

**These tests verify the complete error translation chain.**
`test_review_nonexistent_prediction_returns_404` exercises the full path: API call → Application Service → Repository (raises `PredictionNotFoundError`) → exception propagates → FastAPI exception handler catches it → returns 404 with structured body. The test asserts on the HTTP status code *and* the response body structure, verifying that the domain exception's structured data made it all the way to the API response.

**`test_double_review_returns_409` exercises a multi-step error scenario.**
First it creates a prediction (via `/classify`), reviews it, then attempts a second review. This tests the integration of the entity invariant (`PredictionAlreadyReviewedError`), the Application Service (which doesn't catch it), and the exception handler (which maps it to 409). Each component was tested individually earlier; this test verifies they work together correctly.

**These tests use the same in-memory composition from `conftest.py`.**
The API tests verify that HTTP semantics (status codes, JSON serialization, error responses) are handled correctly. The domain logic is already verified by domain tests. The API tests just confirm the adapter translates correctly in both directions — including the error direction.

## Reference Folder Structure

```
src/
├── domain/                                    # THE HEXAGON
│   ├── exceptions.py
│   ├── objects/
│   │   ├── entity.py
│   │   ├── prediction.py
│   │   ├── flower_measurement.py
│   │   └── species_classification.py
│   ├── services/
│   │   ├── classification_service.py
│   │   ├── review_service.py
│   │   └── quality_service.py
│   └── ports/
│       ├── classifier.py
│       ├── prediction_repository.py
│       └── prediction_exporter.py
│
├── adapters/                                  # OUTSIDE THE HEXAGON
│   ├── inbound/
│   │   └── api.py
│   └── outbound/
│       ├── sklearn_classifier.py
│       ├── sqlite_prediction_repository.py
│       ├── csv_prediction_exporter.py
│       └── in_memory_prediction_repository.py
│
├── main.py                                    # COMPOSITION ROOT
│
└── tests/
    ├── conftest.py
    ├── domain/
    │   ├── test_prediction.py
    │   ├── test_flower_measurement.py
    │   ├── test_classification_service.py
    │   ├── test_review_service.py
    │   └── test_quality_service.py
    └── adapters/
        ├── test_sqlite_prediction_repository.py
        └── test_api.py
```

**`adapters/inbound/` and `adapters/outbound/` mirror the two kinds of ports.**
The folder structure makes the direction of each adapter explicit. When you need to add a new way to *enter* the system (CLI, message queue), you add to `inbound/`. When you need a new external capability (different database, different model server), you add to `outbound/`.

**`main.py` sits at the root, outside both zones.**
It's the one file that imports from both `domain/` and `adapters/`. Every other file imports in only one direction: adapters import from domain, domain imports from nothing external.

**`tests/` mirrors the `src/` structure.**
Domain tests live in `tests/domain/`, adapter tests in `tests/adapters/`. This makes it clear which tests need external resources (adapter tests may need temp files, test databases) and which are pure logic (domain tests need nothing).

**`in_memory_prediction_repository.py` lives in `adapters/outbound/`, not in `tests/`.**
It's a legitimate adapter — a full implementation of the port contract. It happens to be useful for testing, but it could also serve as the persistence mechanism during early development or in a demo environment. Its placement in `adapters/` reflects this: it's a real component, not a test-only artifact.

---

**Previous:** [Domain — The Inside of the Hexagon](./01_domain.md)