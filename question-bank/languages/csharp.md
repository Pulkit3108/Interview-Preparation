# C#

C# language, runtime, object-oriented programming, and application-development questions.

[Back to the question-bank index](../README.md)

## What forms of inheritance does C# support?

**Answer**

C# supports single class inheritance: a class can have one direct base class. This permits common
shapes described as multilevel inheritance (a chain of derived classes) and hierarchical inheritance
(several classes sharing one base class).

C# does not support inheriting implementation from multiple classes. A class can implement multiple
interfaces, but interface implementation is not the same as inheriting state and implementation from
multiple base classes. Prefer composition when the relationship is not genuinely an "is-a"
relationship.

## Can the `virtual` keyword be used only in abstract classes?

**Answer**

No. A non-abstract class can declare a method, property, indexer, or event as `virtual`, provide a
default implementation, and allow a derived class to replace it with `override`.

- `virtual` supplies an overridable implementation.
- `abstract` declares a member without an implementation and requires a concrete derived class to
  implement it.
- `override` replaces an inherited `virtual` or `abstract` member and remains virtual unless marked
  `sealed`.

The `new` keyword hides an inherited member instead of participating in virtual dispatch.

## How do you compare two instances of the same class?

**Answer**

- Use `ReferenceEquals(a, b)` when the question is whether both references point to the same object.
- Define value equality with `Equals` and `GetHashCode`, typically by implementing
  `IEquatable<T>`. If `==` and `!=` are overloaded, keep them consistent with `Equals`.
- Use `IComparable<T>` for a type's natural ordering or `IComparer<T>` for an external or alternate
  ordering.

Records provide compiler-generated value equality by default. Classes use reference equality unless
they override the equality members.

## What are the different types of constructors in C#?

**Answer**

- **Parameterless constructor:** takes no arguments. For a class, the compiler supplies a public
  parameterless constructor only when no instance constructor is declared.
- **Parameterized constructor:** accepts values needed to establish a valid instance.
- **Copy constructor:** a user-defined constructor that accepts another instance of the same type.
  C# does not generate copy constructors for classes, and copying is not automatically deep.
- **Static constructor:** initializes type-level state once before the type is first used. It has no
  parameters or access modifier and cannot be called directly.
- **Private constructor:** restricts construction by outside callers; it can support factories or
  types that should not be instantiated directly.

C# also supports primary-constructor syntax. It changes how constructor parameters are declared but
does not remove the need to enforce type invariants.

## What is a static constructor in C#?

**Answer**

A static constructor initializes type-level state. The runtime invokes it automatically at most once
for an application domain, before the first instance is created or a static member is referenced.
It cannot take parameters, declare an access modifier, or be called directly. If it throws, the type
usually remains unusable for that application domain and subsequent access throws
`TypeInitializationException`.

## Explain MVC architecture.

**Answer**

Model-View-Controller separates an application's presentation concerns:

- **Model:** the data and domain or application behavior used to fulfill a request. It is not simply
  the database entity.
- **View:** renders a representation of the model, commonly HTML in a server-rendered web
  application.
- **Controller:** accepts input, coordinates application services, and selects the response or view.

In ASP.NET Core MVC, controllers should remain thin. Business rules belong in domain or application
services so they can be reused and tested without the HTTP layer.

## What is the difference between a service and a controller?

**Answer**

A controller is an HTTP boundary. It binds and validates request data, invokes an application use
case, and maps the outcome to an HTTP response or view.

A service implements reusable application or domain behavior and should not depend on controller or
HTTP details unless it is specifically an infrastructure adapter. Keeping controllers thin avoids
duplicated business logic and makes that logic easier to test.

## What is Entity Framework?

**Answer**

Entity Framework Core is a .NET object-relational mapper. It maps .NET entities and relationships to
a database model, translates LINQ queries, tracks changes, persists updates through `DbContext`, and
supports schema migrations through provider-specific tooling.

An ORM does not remove the need to understand SQL, indexes, transactions, query plans, or data-model
boundaries. Inspect generated SQL and avoid accidentally loading large graphs or producing N+1
queries.

## Explain the difference between dispose(), finalize() and finally in C#

**Answer**

- **`Dispose()` / `IDisposable`:** deterministic cleanup invoked explicitly, commonly through a
  `using` statement or declaration. It releases unmanaged resources and managed disposable objects
  owned by the instance; it does not directly free ordinary managed memory.
- **Finalizer (`~TypeName()`):** nondeterministic fallback run by the GC before reclaiming an object
  that has a finalizer. Use it only when directly owning unmanaged resources and follow the dispose
  pattern, preferably wrapping the resource in `SafeHandle`.
- **`finally`:** a control-flow block that normally runs when execution leaves a `try`, whether the
  `try` succeeds or throws. It is not a cleanup API by itself, and process termination or other
  exceptional runtime conditions can prevent it from running.

## What are some different types of access modifiers in C#?

**Answer**

- `public`: accessible from any code that can access the containing type.
- `private`: accessible only within the containing type.
- `protected`: accessible within the containing type and derived types.
- `internal`: accessible within the same assembly.
- `protected internal`: accessible from the same assembly **or** from a derived type in another
  assembly.
- `private protected`: accessible from the containing type or a derived type, but only within the
  same assembly.
- `file`: a top-level type is accessible only within the current source file.

## What is a protected internal access modifier in C#?

**Answer**

`protected internal` is the union of `protected` and `internal`: a member is accessible from any code
in the same assembly **or** from a derived type in another assembly. This differs from
`private protected`, which requires both derivation and access from the same assembly.

## What are generics in C#?

**Answer**

Generics let classes, structs, interfaces, delegates, and methods operate on type parameters while
preserving compile-time type safety. For example, `List<T>` works for many element types without
casting values to and from `object`.

Constraints such as `where T : class`, `where T : struct`, `where T : BaseType`, or
`where T : new()` state which operations the generic implementation may perform. Generics reduce
duplication and, for value types, can avoid boxing.

## What is the ref and out keyword in C# and How do you use it?

**Answer**

Both keywords pass an argument by reference:

- `ref` requires the caller to initialize the variable. The method may read it and must not
  necessarily assign a new value.
- `out` does not require caller initialization, but the method must assign the parameter before it
  returns normally. It is intended to return an additional value.

The caller must also write the corresponding modifier at the call site. Prefer an ordinary return
value or a tuple when that makes the API clearer; `TryParse`-style APIs are a common appropriate use
of `out`.

## What is the difference between readonly, static, and constant?

**Answer**

- `const` is an implicitly static compile-time constant and must be assigned at declaration. Its
  value is embedded into consuming assemblies, so public constants require versioning care.
- `readonly` is a field modifier. An instance readonly field can be assigned at declaration or in an
  instance constructor; a static readonly field can be assigned at declaration or in a static
  constructor.
- `static` controls ownership, not mutability. A static member belongs to the type rather than an
  instance and can still be mutable unless combined with another constraint.

For a readonly reference-type field, the reference cannot be replaced after initialization, but the
referenced object's own state may still be mutable.

## What are tuples in C#?

**Answer**

C# tuple syntax such as `(string Name, int Age)` uses `System.ValueTuple` to group a fixed number of
possibly different values. Tuples are useful for local composition and returning a small set of
related values without defining a dedicated type.

Element names improve readability but are not part of runtime type identity. Use a record or class
when the value has domain meaning, invariants, behavior, or a public contract that should evolve
independently.

## How do you take input and output in C#?

**Answer**

`Console.ReadLine` may return `null` when no more input is available, so the variable is nullable.

```csharp
string? input = Console.ReadLine();
Console.WriteLine(input);
```

## Which LINQ method joins two sequences using key selectors?

**Answer**

`Enumerable.Join` performs an inner equijoin: it matches elements from two sequences by key and
projects a result for every match. `GroupJoin` produces each outer element with its group of matching
inner elements and can be used when modeling grouped or left-join behavior.

## How can LINQ count occurrences of a character in a string?

**Answer**

`Count` evaluates the predicate for each UTF-16 `char`. Counting user-perceived Unicode characters
requires text-element handling instead.

```csharp
char target = 'c';
int count = text.Count(character => character == target);
```

## How do you filter even numbers and sum them with LINQ?

**Answer**

Filter the sequence with `Where`, then aggregate the remaining values with `Sum`.

```csharp
int sum = numbers.Where(number => number % 2 == 0).Sum();
```

## Which features were added in recent C# releases?

**Answer**

As of the stable C# 14 release, notable additions include:

- extension-member syntax that supports extension properties and static extension members;
- null-conditional assignment, such as `customer?.Order = currentOrder`;
- the `field` contextual keyword for accessing a compiler-generated property backing field;
- more implicit conversions involving `Span<T>` and `ReadOnlySpan<T>`;
- `nameof` support for unbound generic types; and
- additional partial members and user-defined compound-assignment operators.

In an interview, state the version you are discussing and connect a feature to a practical use case.
Avoid presenting preview features as stable language behavior.

## References

- [C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)
- [What's new in C# 14](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14)
- [What's new in C# 14](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14/)
- [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/)
