# Low-Level Design

Object modeling, relationships, SOLID principles, and reusable design patterns.

[Back to the question-bank index](../README.md)

## Topic Map

- [Object-oriented fundamentals](#what-is-oops-and-explain-its-concepts)
- [Relationships and composition](#what-is-association-aggregation-and-composition)
- [SOLID and dependency design](#explain-solid-principles)
- [Creational patterns](#what-is-a-singleton-class)
- [Structural and behavioral patterns](#what-are-some-different-design-patterns-out-there)

## What is OOPS and explain its concepts?

**Answer**

Object-oriented programming models state and behavior through collaborating objects. A class defines
construction and shared behavior, while an object is a runtime instance. Its core ideas are:

- **Encapsulation:** protect invariants behind an intentional API.
- **Abstraction:** expose essential behavior while hiding changeable details.
- **Inheritance:** define a subtype relationship and share base behavior.
- **Polymorphism:** use different implementations through one contract.

OOP is one tool; good designs also use functions, modules, composition, and immutable values where
those are clearer.

## What are the different types of Polymorphism?

**Answer**

Common forms include ad-hoc polymorphism through overloads, subtype polymorphism through overriding
and dynamic dispatch, and parametric polymorphism through generics. Some languages also support
coercion polymorphism. The exact forms and dispatch rules depend on the language.

## What is Method Overloading?

**Answer**

Method overloading declares methods with the same name but different parameter lists. The compiler
selects an applicable signature from the static argument types. It is distinct from overriding, where
a subtype supplies a new implementation for an inherited signature. Support and ambiguity rules are
language-specific.

## What is the difference between abstraction and encapsulation?

**Answer**

Abstraction defines the essential contract while omitting irrelevant implementation detail.
Encapsulation groups state and behavior and controls how state may be observed or changed. An
interface is an abstraction; a class that keeps fields private and preserves invariants uses
encapsulation. Getters and setters alone do not guarantee either quality.

## How can we achieve abstraction?

**Answer**

Use small interfaces, abstract base classes where shared implementation is justified, functions,
modules, facades, or service contracts. Choose the narrowest abstraction that captures what clients
need and avoid leaking storage, framework, or transport details.

## Can you overload a method by changing just it's return type

**Answer**

Not in Java, C#, and many similar overload-resolution systems. The arguments would not identify which
method to call, so overloads need distinct parameter signatures. Other languages may differ; state
the target language.

## Explain SOLID Principles.

**Answer**

- **Single Responsibility:** a module should have one cohesive reason to change.
- **Open/Closed:** behavior should be extensible at deliberate variation points without repeatedly
  editing stable code.
- **Liskov Substitution:** subtypes must honor the behavioral contract of their base type.
- **Interface Segregation:** clients should not depend on operations they do not need.
- **Dependency Inversion:** high-level policy and low-level detail should depend on appropriate
  abstractions rather than policy depending directly on volatile details.

These are design heuristics, not instructions to create an interface for every class.

## What changes will you make to make sure the class follows an open-closed principle?

**Answer**

Identify behavior that genuinely varies, define a stable contract for it, and move each policy into a
separate implementation selected through composition, configuration, or a factory. Keep stable
orchestration dependent on the contract. Inheritance is not required, and speculative extension
points add complexity.

## Explain the Liskov Substitution Principle with an example.

**Answer**

A subtype must accept everything its base contract accepts, preserve promised outcomes and
invariants, and not introduce stronger preconditions. If `Bird.fly()` is part of a base contract,
making `Penguin` throw violates substitutability. Model `Bird` separately from a `FlyingAnimal`
capability so flight algorithms accept only valid implementations.

## Explain the Dependency Injection

**Answer**

Dependency injection supplies an object's collaborators from outside instead of letting it construct
concrete dependencies internally. Constructor injection makes required dependencies explicit and
supports testing and replacement. A DI container can automate assembly, but the design technique does
not require a framework.

## What is cohesion and coupling?

**Answer**

Cohesion measures how strongly a module's responsibilities belong together; high cohesion gives it a
clear purpose. Coupling measures how much one module depends on another's details. Aim for cohesive
modules connected through small, stable contracts, but make real domain coupling explicit rather than
hiding it behind unnecessary layers.

## What is Composition over Inheritance principle?

**Answer**

Composition assembles behavior from collaborators and can vary it independently. Inheritance tightly
couples a subtype to base-class behavior and should represent a genuine substitutable "is-a"
relationship. Prefer composition for reuse and orthogonal capabilities; use inheritance when the
behavioral subtype contract is stable and meaningful.

## What is Association, Aggregation and Composition?

**Answer**

Association is a general relationship in which objects know about or collaborate with each other; it
may be uni- or bidirectional. Aggregation is a weak whole-part relationship where the part can exist
independently. Composition is strong ownership: the whole controls the part's lifecycle and the part
normally belongs to one whole. UML uses a hollow diamond for aggregation and a filled diamond for
composition, but code should express actual ownership rather than diagram labels alone.

## Tell a bit about different types of entity relationships with examples?

**Answer**

Cardinality describes how many instances can participate: one-to-one, one-to-many/many-to-one, and
many-to-many. In a relational model, a foreign key commonly implements one-to-many, a unique foreign
key constrains one-to-one, and a junction table implements many-to-many. Also specify optionality,
ownership, uniqueness, and deletion behavior; labels alone do not capture those rules.

## If you are given a task to design University, how will you form the relationships?

**Answer**

Model `Student`, `Instructor`, `Department`, `Course`, `CourseOffering`, and `Enrollment`. A department
offers courses; a course has many term-specific offerings; instructors teach offerings; students join
offerings through enrollment, which owns status and grade. This resolves the many-to-many relationship
and distinguishes a catalog course from a scheduled section. Treat addresses as value objects when
their lifecycle follows the owner. Confirm whether departments/courses survive university deletion
before calling the relationship composition.

## What is the difference between is-a and has-a relationship?

**Answer**

An "is-a" relationship is behavioral subtyping: every subtype must be usable where the base contract
is expected. A "has-a" relationship uses composition or aggregation: one object collaborates with or
owns another. Use inheritance only for substitutability, not merely to reuse code.

## Suppose you are refactoring an existing application to improve Object Oriented Design. You find a Vehicle which has methods called fly and sale. How would you refactor the class using is-a and has-a relationship. So, that it follows the Single Responsibility Principle?

**Answer**

Assuming `sale` means `sail`, remove both capabilities from a universal `Vehicle` base. Keep only
shared vehicle invariants, define `Flyable` and `Sailable` capabilities, and implement them only for
valid types such as `Airplane` and `Boat`. Prefer injected `FlightBehavior` or `SailingBehavior` when
behavior must vary independently. This improves responsibility and avoids subtypes whose inherited
methods must throw.

## What is a Singleton Class?

**Answer**

A singleton restricts a class to one instance within a defined runtime or class-loader boundary and
provides access to it. It is not one instance across processes or a cluster. The global lifetime can
hide dependencies, complicate tests, and create contention, so prefer explicit dependency scopes when
possible.

## What is the Singleton design pattern and in which scenario we will use it?

**Answer**

Use it only when one process-wide instance is an actual invariant or when integrating with an API that
requires it. In Java, an enum singleton gives simple serialization and initialization safety; a
static-holder idiom supports lazy initialization. Logging, caches, pools, and configuration often need
lifecycle management or multiple test instances, so a DI-container singleton scope is usually more
flexible than a hard-coded global.

## How would you implement Singleton Design Pattern with double check locking?

**Answer**

In Java, the field must be `volatile` so publication is safe, and the second check must occur inside
the synchronized block:

```java
public final class Registry {
    private static volatile Registry instance;

    private Registry() {}

    public static Registry getInstance() {
        Registry result = instance;
        if (result == null) {
            synchronized (Registry.class) {
                result = instance;
                if (result == null) {
                    result = new Registry();
                    instance = result;
                }
            }
        }
        return result;
    }
}
```

Prefer an enum or initialization-on-demand holder unless double-checked locking is specifically being
tested.

## What are some different design patterns out there?

**Answer**

The GoF catalog groups patterns by intent:

- **Creational:** Abstract Factory, Builder, Factory Method, Prototype, Singleton.
- **Structural:** Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy.
- **Behavioral:** Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento,
  Observer, State, Strategy, Template Method, and Visitor.

Patterns are vocabulary for recurring trade-offs, not mandatory layers. Explain the problem, forces,
and consequences rather than only naming a pattern.

## What is an Observable design pattern?

**Answer**

The usual name is the **Observer** pattern. A subject maintains subscriptions and notifies observers
when an event or state change occurs. It decouples the publisher from concrete consumers, but still
needs unsubscribe/lifecycle handling, ordering and error policy, and protection from slow or
reentrant observers. Reactive streams add completion, errors, operators, and often backpressure
semantics beyond the basic GoF pattern.

## What is the Command Design Pattern?

**Answer**

Command represents a request as an object with an operation such as `execute`. A concrete command
captures the receiver and arguments; an invoker triggers it without knowing the business operation.
Commands can support queues, audit, retries, macros, or undo when the command explicitly captures
enough state. Persisted commands also need versioning and idempotency.

## What is the factory design pattern?

**Answer**

Factory Method defines a creation operation in a base creator and lets subclasses choose the concrete
product. A simple factory function is a related idiom but not the same GoF structure. Both hide
construction details and let clients depend on a product contract; use them when selection or setup is
complex enough to justify indirection.

## What is the Abstract Factory design pattern?

**Answer**

Abstract Factory creates a compatible family of related products without exposing concrete classes.
For example, a UI factory can create matching button, menu, and dialog implementations for one
platform theme. It preserves family consistency and makes family replacement easy, but adding a new
product kind requires changing every factory implementation.

## Suppose you're using a Factory Pattern to create objects in a multithreaded environment. How would you ensure that the factory itself is thread-safe without significantly impacting the performance of object creation?

**Answer**

First make the factory stateless; allocating a new object from immutable configuration needs no lock.
For shared registries or cached constructors, use immutable snapshots, `ConcurrentHashMap` with an
appropriate atomic operation, or safely published initialization. Synchronize only the mutation that
must be atomic, and verify whether a mapping function may execute more than once. Double-checked
locking is relevant to lazy publication of one shared value, not general object creation.

## What is Builder Design Pattern?

**Answer**

Builder constructs a complex object step by step and performs final validation before producing it.
It makes many optional parameters readable and can create immutable products. A director is optional
and captures a reusable construction sequence. Avoid a builder when a small constructor or factory is
already clear.

## What is the Decorator Design Pattern?

**Answer**

Decorator wraps an object behind the same component interface and adds behavior before or after
delegation. Decorators can be stacked to combine responsibilities without subclass explosion. Order
can matter, identity/debugging becomes less obvious, and a decorator must preserve the component
contract.

## Which of the following design patterns are creational patterns?

**Answer**

Singleton, Factory Method, Abstract Factory, Builder, and Prototype are the five GoF creational
patterns.


## What is Proxy Design Pattern?

**Answer**

Proxy provides a surrogate implementing the same subject interface and controls access to the real
subject. Examples include virtual proxies for lazy creation, protection proxies for access control,
remote proxies for another address space, and caching proxies. Unlike Decorator, Proxy primarily
manages access or location, though their structures can look similar.

## References

- [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.pearson.com/en-us/subject-catalog/p/design-patterns-elements-of-reusable-object-oriented-software/P200000000477)
- [Java Language Specification: method signatures](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2)
