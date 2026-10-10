# Java Functional Interfaces and Streams

Functional interfaces, lambdas, method references, and stream processing.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## What is Functional Interface?

**Answer**

- **Functional interface:** an interface with exactly one abstract method after ignoring methods that
  merely match public methods of `Object`.
- **Lambda Expressions:** Can be used to implement functional interfaces.
- **`@FunctionalInterface`:** optional but useful because the compiler rejects changes that break the
  single-abstract-method contract.
- **Built-in Functional Interfaces:** Java provides several built-in functional interfaces in the java.util.function package, such as Function, Consumer, Supplier, and Predicate

## Can we have a default method implementation in functional interface?

**Answer**

Yes, in Java, you can have default method implementations in functional interfaces.

## Can Functional interface extend or implement another interface?

**Answer**

An interface can **extend** one or more interfaces; interfaces do not implement interfaces. The
result remains functional only if all inherited abstract declarations represent one logical method
signature after override-equivalence is considered. Default, static, and private methods do not add
abstract methods.

## Can we have a static method in a functional interface?

**Answer**

Yes, you can have static methods in both functional interfaces and regular interfaces in Java

## What are the advantages of Functional Interface?

**Answer**

- **Concise and Readable Code:** Lambda Expressions: Enable more concise and readable code by eliminating boilerplate code.
- **Improved Code Maintainability:** Less Boilerplate: Easier to maintain and understand due to reduced boilerplate code.
- **Enhanced Expressiveness:** Method References: Further enhance the expressiveness and readability of the code.
- **Functional Programming Paradigm:** Functional Programming: Enable functional programming in Java, allowing declarative style and higher-order functions.
- **Interoperability with Streams API:** Streams API: Enable powerful and expressive data processing operations.
- **Custom Functional Interfaces:** Custom Interfaces: Define your own functional interfaces for modular and reusable code.
- **Compatibility with Existing Libraries:** Backward Compatibility: Provide backward compatibility with existing libraries and frameworks.

## What are the common functional interfaces in Java?

**Answer**

The `java.util.function` package provides reusable target types for lambdas and method references.

| Interface | Abstract method | Typical use |
|---|---|---|
| `Predicate<T>` | `boolean test(T value)` | Test or filter a value |
| `Function<T, R>` | `R apply(T value)` | Transform one value into another |
| `Consumer<T>` | `void accept(T value)` | Perform an operation with no returned result |
| `Supplier<T>` | `T get()` | Create or provide a value without an input |
| `UnaryOperator<T>` | `T apply(T value)` | Transform a value without changing its type |
| `BinaryOperator<T>` | `T apply(T left, T right)` | Combine two same-typed values into one |
| `BiFunction<T, U, R>` | `R apply(T left, U right)` | Transform two inputs into a result |
| `BiConsumer<T, U>` | `void accept(T left, U right)` | Consume two inputs without returning a result |
| `BiPredicate<T, U>` | `boolean test(T left, U right)` | Test a condition involving two inputs |

Primitive specializations such as `IntPredicate` and `LongSupplier` avoid boxing when operating on
primitive values.

## How functional interface and lambda expression is related to each other?

**Answer**

- **Target Type:** A lambda expression can be used wherever a functional interface is expected. The functional interface serves as the target type for the lambda expression.
- **Implementation of Abstract Method:** The lambda expression provides the implementation for the single abstract method defined in the functional interface.
- **Type Inference:** The compiler can infer the types of the parameters of the lambda expression based on the context provided by the functional interface.
- **Simplifying Code:** Lambda expressions simplify the code by eliminating the need for anonymous inner classes to implement functional interfaces.

## What is Comparator vs Comparable in Java?

**Answer**

Both define an ordering, but they place that responsibility in different locations.

| Concern | `Comparable<T>` | `Comparator<T>` |
|---|---|---|
| Meaning | The type's natural ordering | An external or alternate ordering |
| Method | `int compareTo(T other)` | `int compare(T left, T right)` |
| Package | `java.lang` | `java.util` |
| Implementation | Implemented by the class being ordered | Implemented separately or supplied as a lambda |
| Number of orderings | Normally one natural order per type | Any number of named or composed orders |

For example, an `Employee` might implement `Comparable<Employee>` to order by employee ID while
separate comparators order employees by name or joining date. In both cases, the comparison contract
must be transitive and consistent enough for the target sorted collection or algorithm.

## Why Comparable Interface is not Functional Interface?

**Answer**

`Comparable<T>` is structurally a functional interface because `compareTo` is its one abstract
method, even though the JDK does not annotate it with `@FunctionalInterface`. A lambda can target it,
but `Comparable` normally expresses an object's intrinsic natural ordering, so implementing it on the
type is more meaningful than creating ad hoc lambda instances.
- **Comparator Interface:** Annotated with @FunctionalInterface and designed to represent a comparison function.
Commonly used with lambda expressions and method references to define custom orderings.

## How do `Consumer`, `forEach`, and the Stream API relate?

**Answer**

These three APIs work together, but they are not the same thing.

### `Consumer<T>`

`Consumer<T>` is a functional interface for an operation that accepts one value and returns no
result. Its single abstract method is `void accept(T value)`. It is appropriate for an intentional
side effect such as printing, logging, or sending a value to another API.

```java
Consumer<String> printName = name -> System.out.println("Name: " + name);
printName.accept("Asha");
```

### `forEach`

`forEach` accepts a `Consumer` and invokes it for each element:

- `Iterable.forEach` traverses an iterable such as a `List`.
- `Stream.forEach` is a terminal stream operation. On a parallel stream it does not guarantee
  encounter order; use `forEachOrdered` when that order is required.

```java
List<String> names = List.of("Asha", "Ravi", "Mina");
names.forEach(System.out::println);
```

### Stream API

The Stream API processes a sequence of elements as a pipeline. A stream does not store data. It
reads from a source, applies zero or more lazy intermediate operations such as `filter` and `map`,
and finishes with a terminal operation such as `collect`, `reduce`, or `forEach`.

```java
List.of("Asha", "Ravi", "Mina").stream()
    .filter(name -> name.length() == 4) // intermediate; builds the pipeline
    .map(String::toUpperCase)           // intermediate; transforms each match
    .forEach(System.out::println);       // terminal; executes the pipeline
```

Here, the lambda passed to `forEach` is represented by a `Consumer<String>`. Prefer transformations
and collectors when producing a result; use `forEach` when the required outcome is genuinely a side
effect.

## Which functional interfaces fit common invoice operations?

**Answer**

Use `Predicate` for a test, `Consumer` for a side effect, and `Supplier` for deferred creation:

```java
Predicate<Invoice> isOverdue =
    invoice -> invoice.getDueDate().isBefore(LocalDate.now());
Consumer<Invoice> updateStatus = invoice -> invoice.setStatus("Overdue");
Consumer<Invoice> printInvoice = System.out::println;
Supplier<Invoice> invoiceSupplier =
    () -> new Invoice("INV001", 1500.0, "Pending", LocalDate.now().plusDays(30));
```

Mutable consumers are easy to misuse in parallel streams. Keep state changes deliberate and avoid
using side effects merely to work around a missing transformation.

## What is the difference between `groupingBy` and `partitioningBy`?

**Answer**

Both are collectors, but they produce different key spaces.

| Collector | Classifier | Result |
|---|---|---|
| `groupingBy` | A function that produces any key type | A `Map<K, List<T>>` with one group per observed key |
| `partitioningBy` | A predicate | A `Map<Boolean, List<T>>` with `true` and `false` partitions |

```java
List<String> names = List.of("Ana", "Ravi", "Mina", "Raj");

Map<Integer, List<String>> byLength =
    names.stream().collect(Collectors.groupingBy(String::length));

Map<Boolean, List<String>> longerThanThree =
    names.stream().collect(Collectors.partitioningBy(name -> name.length() > 3));
```

Use `groupingBy` for multiple categories and `partitioningBy` for a binary decision.

## What is faster Stream API or traditional loops?

**Answer**

Neither is universally faster. Loops often have lower pipeline and lambda overhead for small, simple
hot paths, while streams can express bulk transformations clearly and may optimize well after JIT
compilation. A parallel stream helps only when work is sufficiently large, splittable, CPU-bound,
side-effect free, and not constrained by ordering or the common pool. Data size alone does not make
parallel execution faster. Benchmark the real operation with JMH after choosing the clearest correct
implementation.

## What are terminal stream operations?

**Answer**

A terminal operation starts traversal of the stream pipeline and produces a non-stream result or a
side effect. After it completes, that stream cannot be reused.

| Purpose | Common operations | Result |
|---|---|---|
| Aggregate | `collect`, `reduce`, `count` | A collection, summary, count, or combined value |
| Search | `findFirst`, `findAny` | An `Optional` containing a matching element, if present |
| Match | `allMatch`, `anyMatch`, `noneMatch` | A boolean; these operations may short-circuit |
| Materialize | `toArray` | An array containing the traversed elements |
| Perform an action | `forEach`, `forEachOrdered` | No value; invokes a `Consumer` for elements |

Whether an operation processes every element depends on its semantics. For example, `anyMatch` can
stop after the first match, while `collect` normally consumes the entire finite stream.

## What is the difference between `map` and `flatMap`?

**Answer**

`map` transforms each input element into one output value. `flatMap` transforms each input element
into a stream and then flattens those nested streams into one stream.

```java
List<String> lines = List.of("red blue", "green");

List<String[]> arrays = lines.stream()
    .map(line -> line.split(" "))
    .toList(); // one array per input line

List<String> words = lines.stream()
    .flatMap(line -> Arrays.stream(line.split(" ")))
    .toList(); // one stream containing red, blue, and green
```

Use `map` for a one-to-one transformation and `flatMap` when each input can yield zero or more
outputs or when a nested stream-like result needs to be flattened.

## What is parallelStream?

**Answer**

`Collection.parallelStream()` creates a parallel stream whose pipeline may split work across tasks,
normally using the common `ForkJoinPool`. Parallel does not guarantee faster execution or arbitrary
thread-per-element behavior. Avoid shared mutable side effects, understand encounter-order costs, and
do not use it casually for blocking I/O or in server code where common-pool contention is difficult to
control. Measure before keeping it.

## References

- [Java Stream package documentation](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/package-summary.html)
- [`Stream` API](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html)
- [`Consumer` API](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html)
