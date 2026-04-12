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

### Domain Services

