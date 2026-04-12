# The Domain Layer: Inside of the Hexagon

In Ports & Adapters (P&A) - also known as **Hexagonal Architecture** - the domain is **the entire inside of the hexagon:** the core application logic that the architecture exists to protect. The domain defines its own **ports** (interfaces it needs or offers), and everything outside (databases, web frameworks, Machine Learning serving infrastructure) connects through **adapters** that plug into those ports.

The architecture has **two zones:** inside the hexagon (domain + ports) and outside the hexagon (adapters). The dependency rule is simple: **everything points inward.** Adapters depend on ports; port belong to the domain; the domain depends on nothing external.

For ML systems, this is a natural fit. The domain captures *what* the system *does* (clarifying an iris flower, recording a prediction, evaluating accuracy) while adapters handle *how* (serving predictions over HTTP, persisting logs to a database, loading a trained model from disk). The boundary between "what" and "how" is exactly where ports sit.

Based on business understanding and solution requirements, we identify the core concepts and behaviors that define the domain. Using a **ubiquitous language** (a shared vocabulary between developers and domain experts) we model:

* **Entities:** Objects defined by their identity, which persists even as their attributes change.
* **Value Objects:** Immutable objects defined entirely by their attributes. They require no unique identification, and two value objects with identical attributes are considered the same. They increase domain expressiveness while reducing complexity.
* **Domain Services:** Stateless operations that don't naturally belong to a single entity or value object. They handle domain logic that spans multiple objects. Not every domain needs them, but they become essential when business rules involve the coordination of several domain objects.
* **Application Services:** Orchestrators that coordinate domain objects and ports to fulfill user-facing tasks. They contain no business logic themselves, they sequence operations. In P&A, they live inside the hexagon alongside domain objects, rather than in a separate arhitectural layer.
* **Ports:** Abstract interfaces that define the hexagon's boundary: what the domain *needs* from the outside world (domain ports) and what it *offers* to the outside world (driving ports). Ports are owned by the domain; adapters implement them.

> 📌 **Bounded Context** is another key concept of the Domain layer. Bounded contexts are self-contained areas of the model with clear boundaries. Each bounded context has its own ubiquitous language and model, allowing for better modularity and separation of concerns.

## Domain Objects

### Entities

In DDD, an **Entity** is an object whose equality is determined by its **identity**, not its data. Two entities with identical attributes but different identities are considered distinct objects.

```python
# --- domain/objects/entity.py

from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Entity:
    id: UUID = field(default_factory=uuid4, init=False)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
```

**`id: UUID = field(default_factory=uuid4, init=False)`**

* The `id` is auto-generated using `uuid4` (random UUID) — callers never pass it in, because identity is an *internal* concern of the entity.
* `init=False` enforces this at the API level: the outside world cannot set or override it at construction time.
* Using `UUID` instead of plain `int` or `str` ensures identities are **globally unique without a database** — the domain remains infrastructure-free.

**`__eq__` based on `id`**

* `@dataclass` by default compares *all fields*. We override this because entity equality is about **identity, not state**.
* Two `Prediction` objects with identical measurements and classifications but different `id`s are not the same prediction — one may have been made in the morning, the other in the afternoon, under different conditions.
* `isinstance(other, type(self))` guards against cross-type equality: a `Prediction` can never equal a `FlowerMeasurement` even if their UUIDs matched.

**`__hash__` based on `id`**

* Python requires `__hash__` to be explicitly defined when `__eq__` is overridden (`@dataclass` sets `__hash__ = None` in that case).
* Basing it on `id` ensures entities can be safely stored in sets or used as dictionary keys, with correct identity semantics.

Now, the central entity in our Iris classification system. Each time an intern submits measurements and receives a classification, that event is a uniquely identifiable, trackable record - a **Prediction:**

```python
from dataclasses import dataclass, field
from datetime import datetime, timezone
from domain.objects.entity import Entity
from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification

@dataclass
class Prediction(Entity):
    measurement: FlowerMeasurement            # Value Object
    classification: SpeciesClassification     # Value Object
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc), init=False
    )
    reviewed: bool = field(default=False, init=False)
    expert_correction: SpeciesClassification | None = field(default=None, init=False)
```

* **`measurement` and `classification` are value objects, not primitives:** An intern doesn't submit four loose floats, they submit a coherent set of flower measurements. The system doesn't return a string, it returns a species classification. Giving these concepts explicit types prevents primitive obsession and makes the domain self-documenting. We'll define these Value Objects shortly.
* **`created_at` is `init=False` with a UTC factory:** Every prediction is timestampted at creation. The intern doesn't choose when the prediction happened, it's a fact recorded by the system. UTC avoids timezone ambiguity when logs are exported for the quality team.
* **`reviewed` and `expert_correction` are `init=False`:** A new prediction is always unreviewed. Its review state is managed by explicit domain methods (below), never set at construction time. This is a **domain invariant**, it is impossible to construct a prediction that claims to have already been reviewed.

#### Entities as Business Rule Enforcers

Entities should not be passive data containers. They are responsible for **enforcing the business rules that apply directly to them** — ensuring the entity always remains in a valid, meaningful state. These rules are called **invariants:** conditions that must hold true throughout the entity's lifetime.

```python
# --- domain/objects/prediction.py (continued)

@dataclass
class Prediction(Entity):
    # ... previous fields ...

    def mark_reviewed(self, correction: SpeciesClassification | None = None) -> None:
        if self.reviewed:
            raise ValueError("Prediction has already been reviewed.")
        self.reviewed = True
        self.expert_correction = correction

    @property
    was_correct(self) -> bool | None:
    if not self.reviewed:
        return None
    return self.expert_correction is None

    @property 
    def final_classification(self) -> SpeciesClassification:
        is self.expert_correction is not None:
            return self.expert_correction
        return self.classification
```

```python
# --- notebooks/demo.py

from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.objects.prediction import Prediction

# An intern submits measurements and receives a prediction
measurement = FlowerMeasurement(
    sepal_length=5.9, sepal_width=2.8, petal_length=4.1, petal_width=1.3
)
classification = SpeciesClassification(
    species=IrisSpecies.VERSICOLOR, confidence=0.92
)
prediction = Prediction(measurement=measurement, classification=classification)

print(prediction.classification.is_versicolor)    # True
print(prediction.was_correct)                     # None — not yet reviewed

# A senior botanist reviews and confirms
prediction.mark_reviewed(correction=None)
print(prediction.was_correct)                     # True

# Try to review again
try:
    prediction.mark_reviewed()
except ValueError as e:
    print(str(e))    # "Prediction has already been reviewed."
```

* **`mark_reviewed` enforces the review invariant:** A prediction can only be reviewed once. This protects the quality monitoring process: when a senior botanist spot-checks a prediction, that review is recorded immutably. The `correction` parameter is `None` if the prediction was correct, or a `SpeciesClassification` if the botanist disagrees.
* **`was_correct` returns `None` for unreviewed predictions:** This is an explicit three-stage design: correct, incorrect, or *unknown*. It prevents calling code from treating unreviewed predictions as either correct or incorrect by default - a subtle but important safety measure for accuracy monitoring.
* **`final_classification` gives the authoritative answer:** If a botanist corrected the prediction, that correction is the ground_truth. Otherwise, the model's classification stands. This property makes downstream code (e.g., export reports) simpler: they always use `final_classification` without checking review state themselves.

> #### ⚠️ Entity-level Rules vs. Domain-level rules
>
> * **Entity-level rules** govern the internal state and behavior of a single entity. For example, a `Prediction` cannot be reviewed twice, or a prediction's `created_at` cannot be modified after creation.
> * **Domain-level rules** involve interactions between multiple entities or the system as a whole. For example, *"the weekly versicolor precision across all reviewed predictions must stay above 95%"* - this rule cannot be enforced by any single entitiy alone. Domain-level rules are handled by **Domain Services**, which coordinate multiple entities to uphold these broader invariants. We will cover these shortly.

### Value Objects

In DDD, a **Value Object** is an immutable object defined entirely by its attributes. Two value objects with identical attributes are considered the same — there is no meaningful distinction between *this* sepal length of 5.9 cm and *that* sepal length of 5.9 cm. They carry no identity.

Value Objects provide several benefits:

* **Immutability:** A Value Object's state cannot change after creation, leading to safer and more predictable code. A `FlowerMeasurement` that was used in a prediction is a historical fact — it must never be silently mutated.
* **Equality by value:** Two `FlowerMeasurement` objects with identical dimensions are interchangeable. There is no meaningful distinction between them.
* **Encapsulation of domain concepts:** Value Objects give names and behavior to concepts that would otherwise be scattered across the code base. A `SpeciesClassification` knows whether it represents versicolor — that logic lives in one place.
* **Prevention of primitive obsession:** Relying on raw primitives leads to fragile, ambiguous code. Compare:

```python
# Using raw primitives (problematic)
prediction = predict(5.9, 2.8, 4.1, 1.3)           # What order? What units?
species = "versacolor"                             # Typo — silent bug
print(species == "versicolor")                     # False — no safety net

# Using proper Value Objects and Enums (robust)
measurement = FlowerMeasurement(
    sepal_length=5.9, sepal_width=2.8, petal_length=4.1, petal_width=1.3
)
classification = SpeciesClassification(
    species=IrisSpecies.VERSICOLOR, confidence=0.92
)
print(classification.is_versicolor)                # True — unambiguous
```

* **Simplified testing:** Value objects have no dependencies on other entities or external systems, making them straightforward to test in complete isolation.

```python
# --- domain/objects/flower_measurement.py

from dataclasses import dataclass

@dataclass(frozen=True)
class FlowerMeasurement:
    """Four physical measurements of an Iris flower, in centimeters."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __post_init__(self) -> None:
        for field_name in ("sepal_length", "sepal_width", "petal_length", "petal_width"):
            value = getattr(self, field_name)
            if value <= 0:
                raise ValueError(f"{field_name} must be positive, got {value}")
            if value > 15.0:
                raise ValueError(
                    f"{field_name} of {value} cm is outside the plausible range for Iris flowers."
                )
```

* **`frozen=True` enforces immutability:** Once a measurement is recorded, it cannot change. This is both a DDD principle (value objects are immutable) and a domain reality: the physical measurements of a flower are historical facts.
* **Validation in `__post_init__` catches nonsensical inputs early:** A negative petal width or a 50 cm sepal length is not a domain error to be handled gracefully — it's a data entry mistake that should be rejected immediately. The 15.0 cm upper bound is a domain-informed plausibility check: Iris flowers don't grow that large. This is an example of a value object encoding real-world knowledge.

```python
# --- domain/objects/species_classification.py

from dataclasses import dataclass
from enum import Enum, auto

class IrisSpecies(Enum):
    SETOSA = auto()
    VERSICOLOR = auto()
    VIRGINICA = auto()

@dataclass(frozen=True)
class SpeciesClassification:
    """The result of classifying an Iris flower."""
    species: IrisSpecies
    confidence: float

    def __post_init__(self) -> None:
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"Confidence must be between 0 and 1, got {self.confidence}")

    @property
    def is_versicolor(self) -> bool:
        return self.species == IrisSpecies.VERSICOLOR
```

* **`species` is an `Enum`, not a string:** This eliminates the class of bugs where someone writes `"versacolor"` or `"Versicolor"` and the comparison silently fails. The business is clear: the cost of misclassifying versicolor is high. Type safety on the classification itself is a low-cost safeguard against an expensive mistake.
* **`confidence` is part of the classification, not a separate return value:** A classification without a confidence score is incomplete in an ML context. Bundling them together means you can never accidentally have one without the other.
* **`is_versicolor` as a property:** This is a small convenience, but it directly maps to the business question: "Is this flower versicolor?" The code that uses a classification should read like the business requirement, not like `if classification.species == IrisSpecies.VERSICOLOR`.

## Domain Services

Many domain rules can be encapsulated within entities and value objects, but some rules span multiple entities or don't naturally fit within a single one. These are implemented as **Domain Services**, stateless operations that contain business logic involving multiple domain objects.

In our system, the quality monitoring requirement from the business is a natural Domain Service: *"NovaCure wants the ability to periodically review prediction accuracy"* and *"it is far worse to send non-versicolor flowers into the drug pipeline tha to lose some versicolor flowers."*

```python
# --- domain/services/quality_service.py

from domain.objects.prediction import Prediction

class QualityService:
    """Evaluates prediction quality against business criteria.

    The business states: "it is far worse to send non-versicolor flowers 
    into the drug pipeline than to lose some versicolor flowers." This 
    translates directly to precision on the versicolor class being the 
    critical metric.
    """

    @staticmethod
    def compute_versicolor_presicion(predictions: list[Prediction]) -> float | None:
        reviewed = [p for p in predictions if p.reviewed]
        predicted_versicolors = [
            p for p in reviewed if p.classification.is_versicolor
        ]
        if not predicted_versicolor:
            return None
        correct = sum(1 for p in predicted_versicolor if p.was_correct)
        return correct / len(predicted_versicolor)
    
    @staticmethod
    def has_acceptable_quality(
        predictions: list[Prediction],
        min_precision: float = 0.95,
    ) -> bool:
        precision = QualityService.compute_versicolor_precision(predictions)
        if precision is None:
            return False
        return precision >= min_precision
```

* **`compute_versicolor_precision` directly encodes the business priority:** Precision on the versicolor class - the proportion of flowers *predicted* as versicolor that *actually are* versicolor - is the metric that captures the stakeholders' concern. This method computes it from reviewed predictions.
* **`has_acceptable_quality` sets the quality gate:** The default threshold of 0.95 is a domain decision, not an infrastructure config. If the business later decides 0.90 is acceptable, this is the one place that changes.
* **Both methods only operate on reviewed predictions:** Unreviewed predictions have no ground truth, so including them would be meaningless. The methods silently handle this by filtering - no exceptions, no special error paths.
* **This logic doesn't belong in `Prediction` itself:** A single prediction has no concept of "quality across a batch." This is a cross-entity concern: it requires aggregating data from many predictions, applying a business rule, and returning a verdict. That is exactly the role of a Domain Service.

## Application Services (Introduction)

Application services coordinate domain objects and ports to fulfill user-facing tasks. They live inside the hexagon alongside domain objects. The crucial distinction: **Application Services contain no business logic.** They sequence operations - call a port, construct an entity, call another port - but the rules and decisions are made by domain objects and domain services.

Think of an Application Service as a director: it knows what needs to happen and in what order, but delegates the actual work to the actors (domain objects) and stage crew (ports/adapters). 

> ⚠️ Before we can write an Application Service, we need to introduce **ports**, the interfaces that define what the domain needs from the outside world.

## Ports: The Hexagon's Boundary

Ports are **abstract interfaces defined by the domain** that declare capabilities the domain needs but does not implement. They are the mechanisms that keeps the domain independent of all external concerns (databases, ML frameworks, APIs, file systems).

In P&A, there are two kings of ports:

* **Driven ports** (also called **outbound ports** or **secondary ports**): interfaces for capabilities the domain *needs from* the outside world. "I need to persist a prediction." "I need to classify a flower." The domain defines the contract; an adapter outside the hexagon fulfills it.
* **Driving ports** (also called **inbound ports** or **primary ports**): interfaces that the outside world uses *to interact with* the domain. "I want to submit a classification request." "I want to review a prediction." In practice, in Python, the Application Services themselves often serve as the driving port - they are the public API of the hexagon. An explicit driving port interface is optional but can be useful for documentation or when multiple adapters (REST API, CLI, message queue) need a shared contract.

> 📌 The naming can be confusing. A simple way to remember: **Driven ports** are things the domain *drives* (asks for). **Driving ports** are things that *drive* the domain (trigger it). The arrow point inward in both cases - adapters depend on ports, never the other way around.

### Driven Ports

These are the most common ports in practice. Each one represents an external capability the domain requires:

```python
# --- domain/ports/classifier.py

from abc import ABC, abstractmethod
from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification

class IrisClassifier(ABC):
    """Driven port: the domain's contract for species classification.

    The domain requires the ability to classify a flower from its measurements. 
    How that classification is performed (scikit-learn, a neural network, 
    a lookup table) is an adapter concern.
    """

    @abstractmethod
    def classify(self, measurement: FlowerMeasurement) -> SpeciesClassification:
        pass
    
```

```python 
# --- domain/ports/prediction_repository.py

from abc import ABC, abstractmethod
from uuid import UUID
from datetime import datetime
from domain.objects.prediction import Prediction

class PredictionRepository(ABC):
    """Driven port: the domain's contract for prediction persistence.

    The domain needs to save and retrieve predictions. How and where 
    they are stored is an adapter concern.
    """

    @abstractmethod
    def save(self, prediction: Prediction) -> None:
        pass

    @abstractmethod
    def get_by_id(self, prediction_id: UUID) -> Prediction:
        pass

    @abstractmethod
    def get_prediction_since(self, since: datetime) -> list[Prediction]:
        """Retrieve predictions created after the given timestamp.

        Used by the equality review process to pull recent predictions 
        for expert spot-checking.
        """
        pass
```

* **The domain _owns_ these interfaces:** This is the Dependency Inversion Principle in action. The domain doesn't import from any database library of ML framework. Instead, it declares exactly what it needs, and the outside world conforms to that contract. We can swap PostgreSQL for SQLite, or scikit-learn for a remote model server, without touching a single line of domain code.
* **`get_prediction_since` exists because the business needs it:** The quality team exports predictions weekly or bi-weekly for review. This isn't a generic CRUD method added "just in case", it directly supports a stated business requirement. Ports should be shaped by what the domain *actually needs*, not by what a generic repository pattern provides. This is the Interface Segregation Principle at work.
* **`IrisClassifier` takes and returns domain objects:** The port doesn't accept a numpy array or return a dictionary of probabilities. It accepts a `FlowerMeasurement` and returns a `SpeciesClassification`. The adapter is responsible for translating between the domain's language and whatever format the ML framework expects. This keeps the domain's vocabulary consistent throughout.

### Driving Ports (Optional in Python)

For our system, we'll let the Application Services serve as the driving port directly. But for clarity, here's what an explicit driving port would look like:

```python
# --- domain/ports/classification_port.py (optional — for illustration)

from abc import ABC, abstractmethod
from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.prediction import Prediction

class ClassificationPort(ABC):
    """Driving port: the contract for triggering a classification.
    
    Any inbound adapter (REST API, CLI, web UI) uses this interface 
    to request a classification. The Application Service implements it.
    """

    @abstractmethod
    def classify_flower(self, measurement: FlowerMeasurement) -> Prediction:
        pass
```

In practice, we'll skip this indirection and have the inbound adapters call `ClassificationService` directly. The explicit driving port becomes valuable when you need to enforce a strict contract across multiple very different inbound adapters, or when you want to generate API documentation from the port interface. For a system of this scale, it's unnecessary ceremony.

## Application Services (Wiring It Together)

With ports defined, the Application Service can orchestrate the classification workflow. It depends only on abstractions (ports), and coordinates domain objects to fulfill user tasks:

```python
# --- domain/services/classification_service.py

from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.prediction import Prediction
from domain.ports.classifier import IrisClassifier
from domain.ports.prediction_repository import PredictionRepository

class ClassificationService:
    """Orchestrates the classify-and-record workflow.
    
    This is an Application Service — it lives inside the hexagon and 
    coordinates domain objects through ports. It contains no business 
    logic itself; it sequences operations that domain objects and 
    ports perform.
    """

    def __init__(
        self,
        classifier: IrisClassifier,
        prediction_repository: PredictionRepository,
    ):
        self._classifier = classifier
        self._prediction_repository = prediction_repository

    def classify_flower(self, measurement: FlowerMeasurement) -> Prediction:
        classification = self._classifier.classify(measurement)
        prediction = Prediction(
            measurement=measurement,
            classification=classification,
        )
        self._prediction_repository.save(prediction)
        return prediction
```

* **Dependencies are ports, not implementations:** `IrisClassifier` and `PredictionRepository` are abstract interfaces. The service has no idea whether the classifier is scikit-learn or a random forest served via gRPC, or whether predictions are stored in PostgreSQL or a CSV file. This is the Dependency Inversion Principle at work, and it's the mechanism that makes the hexagon independent of everything outside it.
* **The method is pure orchestration:** Read it as a sentence: "Classify the measurement, create a prediction from the result, save it, return it." No business rules, no validation (that's done by the domain objects themselves), no infrastructure - just sequencing.

Now a second Application Service - the quality review workflow that supports the weekly spot-check process:

```python
# --- domain/services/review_service.py

from uuid import UUID
from datetime import datetime
from domain.objects.species_classification import SpeciesClassification
from domain.services.quality_service import QualityService
from domain.ports.prediction_repository import PredictionRepository

class ReviewService:
    """Orchestrates the prediction review workflow."""

    def __init__(self, prediction_repository: PredictionRepository):
        self._prediction_repository = prediction_repository

    def review_prediction(
        self,
        prediction_id: UUID,
        correction: SpeciesClassification | None = None,
    ) -> None:
        prediction = self._prediction_repository.get_by_id(prediction_id)
        prediction.mark_reviewed(correction=correction)
        self._prediction_repository.save(prediction)

    def get_quality_report(self, since: datetime) -> dict:
        predictions = self._prediction_repository.get_predictions_since(since)
        precision = QualityService.compute_versicolor_precision(predictions)
        acceptable = QualityService.has_acceptable_quality(predictions)
        reviewed_count = sum(1 for p in predictions if p.reviewed)
        return {
            "total_predictions": len(predictions),
            "reviewed_count": reviewed_count,
            "versicolor_precision": precision,
            "quality_acceptable": acceptable,
        }
```

* **`review_prediction` delegates all logic to the entity:** The service fetches, tells the entity to do its thing, and saves. The invariant enforcement (can't review twice) is `Predicion`'s responsibility, not the service's.
* **`get_quality_report` composes domain objects and domain services:** It uses `PredictionRepository` (a port) to fetch data, then delegates the business-rule evaluation to `QualityService` (a domain service). The Application Service itself just assembles the pieces - it doesn't contain the precision formula or the quality threshold.

> #### ⚠️ Application Services vs. Domain Services
> The distinction matters even though both live inside the hexagon.
> * **Domain Services** contain *business rules* that span multiple domain objects. `QualityService` encodes what "acceptable versicolor precision" means - that's a business rule.
> * **Application Services** contain *workflow orchestration*. They sequence calls to domain objects and ports to fulfill a user-facing task. `ClassificationService.classify_flower` doesn't devide *how* to classify or *what* a valid classification is - it just coordinates the objects that do.
>
> If you're unsure where a piece of logic belongs, ask: "Would this logic exist even if we had no users, no API, no interface at all?" If yes, it's domain logib. If no - if it only makes sense as a response to a user action - it's application orchestraion.

## Ensuring Domain Independence

Since the domain is the inside of the hexagon, it must not depend on anything outside. The domain model should be entirely self-contained — independent of any specific application framework, database, or infrastructure concern.

This is achieved through **ports** (as we've just seen) and by adhering to **encapsulation** and **separation of concerns**: domain logic expresses what the business requires, never how it is stored, served, or communicated.

### Avoiding External Dependencies

The key strategy is to define **abstractions** for external concerns inside the domain, and let adapters implement them. Every external capability the domain needs is expressed as a port that the domain *owns* and the outside world *implements*.

The concrete implementations live outside the hexagon:

```python
# --- adapters/outbound/sklearn_classifier.py (preview — covered in 02_adapters.md)

import numpy as np
from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.ports.classifier import IrisClassifier

class SklearnClassifier(IrisClassifier):
    def __init__(self, model, species_mapping: dict[int, IrisSpecies]):
        self._model = model
        self._species_mapping = species_mapping

    def classify(self, measurement: FlowerMeasurement) -> SpeciesClassification:
        features = np.array([[
            measurement.sepal_length, measurement.sepal_width,
            measurement.petal_length, measurement.petal_width,
        ]])
        prediction_idx = self._model.predict(features)[0]
        probabilities = self._model.predict_proba(features)[0]
        species = self._species_mapping[prediction_idx]
        confidence = float(probabilities[prediction_idx])
        return SpeciesClassification(species=species, confidence=confidence)
```

```python
# --- adapters/outbound/in_memory_prediction_repository.py (preview)

from uuid import UUID
from datetime import datetime
from domain.objects.prediction import Prediction
from domain.ports.prediction_repository import PredictionRepository

class InMemoryPredictionRepository(PredictionRepository):
    """Lightweight implementation for testing and development."""

    def __init__(self):
        self._store: dict[UUID, Prediction] = {}

    def save(self, prediction: Prediction) -> None:
        self._store[prediction.id] = prediction

    def get_by_id(self, prediction_id: UUID) -> Prediction:
        if prediction_id not in self._store:
            raise KeyError(f"Prediction {prediction_id} not found")
        return self._store[prediction_id]

    def get_predictions_since(self, since: datetime) -> list[Prediction]:
        return [
            p for p in self._store.values()
            if p.created_at >= since
        ]
```

* The domain (`IrisClassifier`, `ClassificationService`) defines and uses abstractions with no knowledge of concrete implementations.
* The adapters (`SklearnClassifier`, `InMemoryPredictionRepository`) implement the abstractions defined by the domain.
* The **dependency arrow points inward:** adapters depend on the domain, never the other way around.
* The domain remains independent of specific ML frameworks or storage technologies. We can swap scikit-learn for a deep learning model, or an in-memory store for PostgreSQL, without touching a single line of domain logic.

### Domain Independence and Testability

Because the domain has no dependency on external systems, domain logic can be tested in complete isolation — no database, no network, no ML framework required. We can provide the lightweight `InMemoryPredictionRepository` in tests and verify all business rules directly. This leads to fast, deterministic, and focused unit tests.

```python
# --- tests/test_classification_service.py (preview)

from domain.objects.flower_measurement import FlowerMeasurement
from domain.objects.species_classification import SpeciesClassification, IrisSpecies
from domain.services.classification_service import ClassificationService
from adapters.outbound.in_memory_prediction_repository import InMemoryPredictionRepository

class FakeClassifier(IrisClassifier):
    """Returns a fixed classification for testing."""
    def classify(self, measurement: FlowerMeasurement) -> SpeciesClassification:
        return SpeciesClassification(species=IrisSpecies.VERSICOLOR, confidence=0.95)

def test_classify_flower_saves_prediction():
    repo = InMemoryPredictionRepository()
    classifier = FakeClassifier()
    service = ClassificationService(classifier=classifier, prediction_repository=repo)

    measurement = FlowerMeasurement(
        sepal_length=5.9, sepal_width=2.8, petal_length=4.1, petal_width=1.3
    )
    prediction = service.classify_flower(measurement)

    assert prediction.classification.is_versicolor
    assert repo.get_by_id(prediction.id) == prediction
```

No database setup, no model loading, no HTTP server. The test runs in milliseconds and verifies the complete orchestration logic.

### Refactoring Towards a Purer Domain

As the system evolves, infrastructure concerns may leak into the domain. Some strategies for keeping it clean:

* **Regular code reviews:** Focus on identifying violations of the dependency rule — any domain class that imports from an adapter is a red flag.
* **Continuous refactoring:** As understanding of the domain deepens (e.g., distinguishing between a *batch prediction* and a *single prediction*, or introducing confidence thresholds for flagging uncertain results), the model should evolve to reflect that understanding accurately.
* **Avoiding frameworks in the domain:** The short-term convenience of pulling in a framework (e.g., importing numpy directly in a domain object for validation) leads to long-term coupling. The domain should be plain Python.
* **Explicitness over implicitness:** Avoid magic behaviors that implicitly trigger external side effects. Make all dependencies and behaviors explicit, even at the cost of slightly more code. This is especially important in ML systems where reproducibility and auditability matter.

A common violation is triggering side effects directly from within an entity:

```python
# --- domain/objects/prediction.py

# -- Before refactoring — violates domain purity

@dataclass
class Prediction(Entity):
    # ... existing fields ...

    def mark_reviewed(self, correction: SpeciesClassification | None = None) -> None:
        if self.reviewed:
            raise ValueError("Prediction has already been reviewed.")
        self.reviewed = True
        self.expert_correction = correction
        # Logging to an external monitoring system — violates domain independence
        self._send_to_monitoring()

    def _send_to_monitoring(self):
        import requests
        requests.post("https://monitoring.internal/api/reviews", json={...})
```

```python
# --- domain/objects/prediction.py

# -- After refactoring — domain stays pure

@dataclass
class Prediction(Entity):
    # ... existing fields ...

    def mark_reviewed(self, correction: SpeciesClassification | None = None) -> None:
        if self.reviewed:
            raise ValueError("Prediction has already been reviewed.")
        self.reviewed = True
        self.expert_correction = correction
        # No external calls here — that is the responsibility of an adapter,
        # triggered by the Application Service after this method returns.
```

The monitoring concern moves to a port defined by the domain and implemented by an adapter. The Application Service calls it after the entity method returns — keeping the entity pure and the side effect explicit.

## Reference Folder Structure

```
domain/
├── objects/
│   ├── entity.py                  # Base Entity class
│   ├── prediction.py              # Prediction (Entity)
│   ├── flower_measurement.py      # FlowerMeasurement (Value Object)
│   └── species_classification.py  # SpeciesClassification, IrisSpecies (Value Object, Enum)
│
├── services/
│   ├── classification_service.py  # ClassificationService (Application Service)
│   ├── review_service.py          # ReviewService (Application Service)
│   └── quality_service.py         # QualityService (Domain Service)
│
└── ports/
    ├── classifier.py              # Abstract: IrisClassifier (Driven Port)
    └── prediction_repository.py   # Abstract: PredictionRepository (Driven Port)
```

* **Ports live inside the domain.** This is the P&A convention: ports are part of the hexagon's boundary, defined by the domain, implemented by adapters. They sit in `domain/ports/` because the domain owns the contract.
* **Application Services and Domain Services share the `services/` directory.** Both live inside the hexagon. The distinction is logical (orchestration vs. business rules), not physical. If the services directory grows, they can be separated into `services/application/` and `services/domain/`.
* **No `factories/` directory.** For this system's complexity level, `@dataclass` constructors and `__post_init__` validation handle object creation cleanly. A `Prediction` is constructed from a `FlowerMeasurement` and a `SpeciesClassification` — no complex assembly, no polymorphic creation, no injected dependencies at construction time. If the domain grows (e.g., different prediction types for different classification strategies), a factory can be introduced then.
* **No `requests/` or `responses/` directory.** In P&A, there is no separate DTO translation layer inside the hexagon. The domain speaks in domain objects. Translating between HTTP requests, CLI inputs, and domain objects is the *adapter's* responsibility — that's exactly what adapters are for. This is one of the key structural simplifications over Clean Architecture.

---

**Next:** [The Adapters Layer - Outside of the Hexagon](./02_adapters.md)
