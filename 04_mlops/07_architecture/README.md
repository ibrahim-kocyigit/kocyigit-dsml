# Architecture

## Ports & Adapters with Domain-Driven Design for ML Systems

After learning the individual building blocks of MLOps, the next step is learning how to **assemble them into a well-designed system**. Knowing *what* the blocks are is not enough; you need to know *how* they fit together so that the result is maintainable, testable, and adaptable to change. That's what software architecture is about.

This module covers **Ports & Adapters** (also known as **Hexagonal Architecture**) combined with **Domain-Driven Design (DDD)**, a pragmatic architecture that provides the bare minimum structure needed to design ML systems that still follow the **SOLID principles**:

1. **Single Responsibility Principle (SRP):** Each module should have exactly one reason to change.
    * If you can identify more than one reason a class might change, consider splitting it.
    * That said, if the split makes the system harder to understand, it may not be the right trade-off.
2. **Open-Closed Principle (OCP):** Software should be open for extension but closed for modification.
3. **Liskov Substitution Principle (LSP):** Subclasses must behave predictably as substitutes for their base classes.
    * A base class defines a behavioral contract that its users rely on.
    * Subclasses may extend or specialize that contract, but must never weaken or violate it.
4. **Interface Segregation Principle (ISP):** Interfaces should be lean and purpose-specific.
    * Classes should only depend on the methods they actually use.
    * Changes to one area of behavior should not ripple into unrelated classes.
5. **Dependency Inversion Principle (DIP):** High-level modules should not depend on low-level modules. Both should depend on abstractions.
    * The domain defines abstract interfaces (ports); infrastructure provides concrete implementations (adapters).
    * Dependencies always point inward, toward the domain, never away from it.

## Sample Project

The code examples throughout the notes follow a **sample mini project** based on a hypothetical business scenario:

A pharmaceutical company has partnered with a botanical research institute to identify and sort thousands of *Iris versicolor* specimens for drug production within a 3-month deadline. The current manual identification process (performed by only two expert botanists at roughly 5 minutes per flower) cannot scale to the required volume of 2,000–3,000 flowers per week. The solution is a classification system that predicts whether a given Iris flower is *versicolor* or *not versicolor* based on four physical measurements (sepal length, sepal width, petal length, petal width), delivered as a REST API and a simple web interface for use by quickly-trained interns. Precision on the versicolor class is the critical metric: it is far worse to send a non-versicolor flower into the drug pipeline than to lose a true versicolor specimen.

The code snippets in these notes are **educational, not a working codebase**. They are designed to illustrate architectural concepts, not to be copy-pasted into a project. For a fully functional, end-to-end implementation that applies these principles to the same Iris classification problem, see the [**iris_fmds**](https://github.com/ibrahim-kocyigit/iris-fmds) repository. That project is also covered as a [series on YouTube](https://www.youtube.com/playlist?list=PLtDMlt2aHBIHNMBpyzws3i65YE5IWhTtT).

## Contents

1. [**Domain: The Inside of the Hexagon**](./01_domain.md) -
    Entities, Value Objects, Domain Services, Domain Exceptions, Application Services, and Ports... Everything that lives inside the hexagon and depends on nothing external.

2. [**Adapters: The Outside of the Hexagon**](./02_adapters.md) - 
    Inbound adapters (REST API), outbound adapters (ML model, database, CSV exporter), error translation at boundaries, and the in-memory adapter pattern for testing.

3. [**main.py: The Composition Root**](./03_composition_root.md) - The single entry point where concrete adapters are instantiated and wired into the domain's ports. The one place that knows about all implementations.

4. [**Testing Strategies Across Zones**](./04_testing_strategies.md) - How to test each zone of the architecture: unit tests for domain logic, integration tests for adapters, and end-to-end API tests... All leveraging the architecture's natural seams.

## A Starting Point, Not a Ceiling

The folder structures and patterns presented here are designed as a **healthy starting point** for freelance and small-to-medium ML projects. For larger and/or more complex systems (e.g., multiple bounded contexts, event-driven communication between services, complex multi-step orchestration) the structures can be expanded, and a more layered architecture (such as **Clean Architecture**) may be more appropriate. Start simple, and let the complexity of the architecture grow with the complexity of the problem.

---

**Next:** [Domain: The Inside of the Hexagon](./01_domain.md)