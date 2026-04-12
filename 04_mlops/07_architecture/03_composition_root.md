# `main.py`: The Composition Root

Every Ports & Adapters system needs a place where the two zones meet: where concrete adapters are instantiated and plugged into the ports that Application Services expect. This is the **composition root**: the single location in the codebase that knows about *all* concrete implementations.

The composition root is **not** part of the domain. It's not part of any adapter either. It's the application's entry point: the `main.py` that assembles the system.


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

* **This is the only file in the entire codebase that imports concrete adapter classes:** The domain imports nothing from adapters. The adapters import from the domain (ports and objects). But `main.py` imports from *both*: it's the one place where the system is assembled. This is a deliberate architectural violation confined to a single file, because *someone* has to plug the pieces together.

* **The wiring order reflects the dependency structure:** Outbound adapters are created first (they have no dependencies on the domain beyond the port interfaces). Application Services are created next, receiving the outbound adapters as constructor arguments. Inbound adapters are created last, receiving the Application Services. The dependency flow is always inward: inbound → services → outbound.

* **Configuration is explicit, not magical:** Model paths, database paths, host, port are all visible and changeable in one place. For a system of this scale, this is sufficient. For larger systems, you'd extract configuration into environment variables or a config file, but the composition root remains the place that reads and applies them.

## Testing with a Different Composition

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

* **Same Application Services, different adapters:** `ClassificationService` doesn't know or care that it's backed by a stub classifier and an in-memory repository. The tests exercise the real orchestration logic (the same code that runs in production) with fast, deterministic, infrastructure-free adapters.

This is the payoff of the entire architecture: **the domain is tested in isolation, at full speed, with complete confidence that the logic being tested is the same logic that runs in production.** The only thing that changes between test and production is which adapters are plugged in, and that's a one-line change in the composition root.

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

```

* **`main.py` sits at the root, outside both zones:** It's the one file that imports from both `domain/` and `adapters/`. Every other file imports in only one direction: adapters import from domain, domain imports from nothing external.


---

**Next:** [Testing Strategies Across Zones](./04_testing_strategies.md)