# Testing Strategy Across Zones

Different parts of the system demand different testing approaches:

## Domain Tests (Unit Tests)

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

* **Tests assert on structured exception data, not just that an exception was raised:** `test_invalid_measurement_raises_domain_exception` checks `e.field_name`, `e.value`, and `e.reason`, the same fields that the API error handler will use to build its response. This verifies that the domain provides the information adapters need, not just that it fails in the right circumstances.

## Application Service Tests (Integration-within-Hexagon)

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

* **These tests verify the full error propagation chain:** `test_review_nonexistent_prediction_raises_not_found` confirms that when the repository raises `PredictionNotFoundError`, it propagates cleanly through the Application Service. `test_review_already_reviewed_raises_error` confirms the same for entity-level invariant violations. In production, these exceptions would propagate further to the inbound adapter's exception handler and become HTTP 404 and 409 responses respectively. The domain tests verify the first half of that chain; the API tests verify the second.

## Adapter Tests (Integration Tests)

Outbound adapters that interact with real infrastructure need **integration tests**: tests that verify the adapter correctly translates between domain objects and the external system.

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

* **These tests use real SQLite databases — but temporary ones:** The test creates a fresh database in a temp directory, exercises the adapter, and the directory is cleaned up automatically. This tests the actual SQL, the actual serialization, and the actual reconstruction; not mocked behavior.

* **`test_get_by_id_raises_domain_exception_for_missing_prediction` is a critical adapter test:** It verifies that the SQLite adapter correctly translates "no row found" into `PredictionNotFoundError`, the domain exception that the port contract requires. Without this test, a refactor of the adapter could accidentally break the error contract and surface SQLite-specific errors to the Application Service.

## API Tests (End-to-End within Process)

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

* **These tests verify the complete error translation chain:** `test_review_nonexistent_prediction_returns_404` exercises the full path: API call → Application Service → Repository (raises `PredictionNotFoundError`) → exception propagates → FastAPI exception handler catches it → returns 404 with structured body. The test asserts on the HTTP status code *and* the response body structure, verifying that the domain exception's structured data made it all the way to the API response.

* **`test_double_review_returns_409` exercises a multi-step error scenario:** First it creates a prediction (via `/classify`), reviews it, then attempts a second review. This tests the integration of the entity invariant (`PredictionAlreadyReviewedError`), the Application Service (which doesn't catch it), and the exception handler (which maps it to 409). Each component was tested individually earlier; this test verifies they work together correctly.

* **These tests use the same in-memory composition from `conftest.py`:** The API tests verify that HTTP semantics (status codes, JSON serialization, error responses) are handled correctly. The domain logic is already verified by domain tests. The API tests just confirm the adapter translates correctly in both directions, including the error direction.

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


* **`tests/` mirrors the `src/` structure:** Domain tests live in `tests/domain/`, adapter tests in `tests/adapters/`. This makes it clear which tests need external resources (adapter tests may need temp files, test databases) and which are pure logic (domain tests need nothing).

* **`in_memory_prediction_repository.py` lives in `adapters/outbound/`, not in `tests/`:**
It's a legitimate adapter, a full implementation of the port contract. It happens to be useful for testing, but it could also serve as the persistence mechanism during early development or in a demo environment. Its placement in `adapters/` reflects this: it's a real component, not a test-only artifact.

---

**Previous:** [Domain — The Inside of the Hexagon](./01_domain.md)