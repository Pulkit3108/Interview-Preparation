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

## What are the different functional interface in Java?

**Answer**

- **Predicate:** Represents a boolean-valued function of one argument.
- **Function:** Represents a function that takes one argument and produces a result.
- **Consumer:** Represents an operation that takes a single input argument and returns no result.
- **Supplier:** Represents a supplier of results.
- **UnaryOperator:** A specialization of Function for the same input and output type.
- **BinaryOperator:** A specialization of BiFunction for the same input and output type.
- **BiFunction:** Represents a function that takes two arguments and produces a result.
- **BiConsumer:** Represents an operation that takes two input arguments and returns no result.
- **BiPredicate:** Represents a boolean-valued function of two arguments.

## How functional interface and lambda expression is related to each other?

**Answer**

- **Target Type:** A lambda expression can be used wherever a functional interface is expected. The functional interface serves as the target type for the lambda expression.
- **Implementation of Abstract Method:** The lambda expression provides the implementation for the single abstract method defined in the functional interface.
- **Type Inference:** The compiler can infer the types of the parameters of the lambda expression based on the context provided by the functional interface.
- **Simplifying Code:** Lambda expressions simplify the code by eliminating the need for anonymous inner classes to implement functional interfaces.

## What is Comparator vs Comparable in Java?

**Answer**

- **Comparable:** [Interface used with class]
- **Purpose:** Defines the natural ordering of objects.
- **Method:** int compareTo(T o)
- **Single Sorting Sequence:** Only one sorting sequence can be defined.
- **Package:** java.lang
- **Example:** Sorting by a single attribute like id.
- **Comparator:** Purpose: Defines multiple sorting sequences.
- **Method:** int compare(T o1, T o2)
- **Multiple Sorting Sequences:** Multiple sorting sequences can be defined.
- **Package:** java.util
- **Example:** Sorting by different attributes like id and name.

## Why Comparable Interface is not Functional Interface?

**Answer**

`Comparable<T>` is structurally a functional interface because `compareTo` is its one abstract
method, even though the JDK does not annotate it with `@FunctionalInterface`. A lambda can target it,
but `Comparable` normally expresses an object's intrinsic natural ordering, so implementing it on the
type is more meaningful than creating ad hoc lambda instances.
- **Comparator Interface:** Annotated with @FunctionalInterface and designed to represent a comparison function.
Commonly used with lambda expressions and method references to define custom orderings.

## What is Consumer, forEach and Stream API?

**Answer**

- **Stream API:** Functional Programming: Provides a functional approach to processing sequences of elements.
- **Intermediate Operations:** Return a new stream (e.g., filter, map).
- **Terminal Operations:** Produce a result or a side-effect (e.g., forEach, collect).
Intermediate operations are defined and chained together, but they are not executed until a terminal operation is invoked.
- **Usage:** stream().filter(...).map(...).collect(...)
forEach Method:
- **Iterable Interface:** Used to iterate over elements in a collection and perform an action on each element.
- **Stream Interface:** Used to perform actions on each element of a stream.
- **Usage:** collection.forEach(action) or stream.forEach(action)
- **Consumer Interface:** Functional Interface: Represents an operation that takes a single input argument and returns no result.
- **Method:** void accept(T t)
- **Usage:** Commonly used in lambda expressions and method references.
- **Example:** `Consumer<String> printName = name -> System.out.println("Name: " + name)`

- **Predicate Interface:** A functional interface that represents a single argument function returning a boolean value.
- **Method:** boolean test(T t) evaluates the predicate on the given argument.
- **Default Methods:** Includes methods for combining predicates (and, or, negate).
- **Usage:** Commonly used in lambda expressions, method references, and with the Stream API for filtering and matching operations.
- **Example:** `Predicate<Integer> isEven = number -> number % 2 == 0`
- **Supplier Interface:** Represents a supplier of results. It does not take any arguments and returns a result of a specified type.
- **Method:** T get() - Gets a result.
- **Default Methods:** The Supplier interface does not have any default methods.
- **Usage:** Commonly used in lambda expressions, method references, and with the Stream API for generating or providing values.
- **Example:** `Supplier<Double> randomSupplier = Math::random`
- **Function Interface:** A functional interface that represents a function taking one argument and producing a result.
- **Method:** R apply(T t) applies the function to the given argument and returns the result.
- **Default Methods:** Includes methods for composing functions (andThen, compose).
- **Usage:** Commonly used in lambda expressions, method references, and with the Stream API for mapping and transforming data.
- **Example:** `Function<String, Integer> stringLengthFunction = String::length`
- **Runnable Interface:** A functional interface that represents a task that can be executed by a thread. It does not take any arguments and does not return a result.
- **Method:** void run() - Executes the task.
- **Default Methods:** The Runnable interface does not have any default methods.
- **Usage:** Commonly used to define tasks that can be executed by threads, often in lambda expressions and method references.
- **Example:** `Runnable task = () -> System.out.println("Task is running")`
- **Comparator Interface:** A functional interface that represents a comparison function, which imposes a total ordering on some collection of objects.
- **Method:** int compare(T o1, T o2) - Compares its two arguments for order. Returns a negative integer, zero, or a positive integer as the first argument is less than, equal to, or greater than the second.
- **Default Methods:** Includes methods for composing comparators (thenComparing, reversed).
- **Usage:** Commonly used to define custom sorting orders for collections, often in lambda expressions and method references.
- **Example:** `Comparator<String> byLength = Comparator.comparingInt(String::length)`

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

## What is GroupBy & PartitioningBy?

**Answer**

groupingBy:
- **Purpose:** Groups elements based on a classification function.
- **Result:** Returns a Map where keys are the result of the classification function, and values are lists of items that match the classification.
- **Example:** Grouping names by their length.
partitioningBy:
- **Purpose:** Partitions elements into two groups based on a predicate.
- **Result:** Returns a Map with Boolean keys (true and false), where values are lists of items that match or do not match the predicate.
- **Example:** Partitioning names by whether their length is greater than 3.

## What is faster Stream API or traditional loops?

**Answer**

Neither is universally faster. Loops often have lower pipeline and lambda overhead for small, simple
hot paths, while streams can express bulk transformations clearly and may optimize well after JIT
compilation. A parallel stream helps only when work is sufficiently large, splittable, CPU-bound,
side-effect free, and not constrained by ordering or the common pool. Data size alone does not make
parallel execution faster. Benchmark the real operation with JMH after choosing the clearest correct
implementation.

## What are Terminal operations?

**Answer**

- **Terminal Operations:** Operations that produce a result or a side-effect and mark the end of the stream pipeline.
- **Common Terminal Operations:** forEach: Performs an action for each element.
collect: Collect elements into a collection or another data structure.
reduce: Reduces elements to a single value.
toArray: Returns an array containing the elements.
count: Returns the count of elements.
findFirst: Returns the first element as an Optional.
findAny: Returns any element as an Optional.
allMatch, anyMatch, noneMatch: Return boolean values based on predicate matching.

## What is the difference between flatmap() and a map()?

**Answer**

- **Transformation:** map(): Transforms each element of the stream into another element.
flatMap(): Transforms each element of the stream into a stream of new elements and then flattens the resulting streams into a single stream.
- **Mapping:** map(): One-to-One Mapping (each input element is transformed into exactly one output element).
flatMap(): One-to-Many Mapping (each input element is transformed into zero or more output elements).
- **Resulting Stream:** map(): The result is a stream of the same structure but with transformed elements.
flatMap(): The result is a single flattened stream containing all the elements of the individual streams.

## What is parallelStream?

**Answer**

`Collection.parallelStream()` creates a parallel stream whose pipeline may split work across tasks,
normally using the common `ForkJoinPool`. Parallel does not guarantee faster execution or arbitrary
thread-per-element behavior. Avoid shared mutable side effects, understand encounter-order costs, and
do not use it casually for blocking I/O or in server code where common-pool contention is difficult to
control. Measure before keeping it.
