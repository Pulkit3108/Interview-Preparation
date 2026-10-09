# Java JVM and Runtime

JVM architecture, class loading, memory, garbage collection, releases, and execution.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## What are the advantages and disadvantages of using Java for Enterprise Level Development

**Answer**

Java offers a mature ecosystem, strong static typing, portable bytecode, managed memory, capable JIT
compilation, production diagnostics, and extensive libraries for networking, persistence, security,
and observability. Its compatibility culture and tooling make it a practical choice for large,
long-lived systems.

Trade-offs include runtime and memory overhead, warm-up and startup costs for some workloads,
garbage-collection tuning at scale, and more ceremony than some languages. Native integration and
very small deployment footprints may require extra work. Java itself is not inherently subject to a
fee: licensing and support costs depend on the selected JDK distribution, version, and use terms.

## What is JVM, JDK, and JRE?

**Answer**

- **JVM (Java Virtual Machine):** executes Java bytecode and provides runtime services such as
  class loading, memory management, garbage collection, and JIT compilation. A JVM implementation
  is platform-specific even though Java bytecode is portable.
- **Java runtime:** the JVM plus the Java modules and native libraries needed by an application.
  Historically this was commonly installed as a separate JRE distribution.
- **JDK (Java Development Kit):** a Java runtime plus development and diagnostic tools such as
  `javac`, `java`, `jar`, `javadoc`, `jlink`, and debuggers.

Since the Java module system, applications can also be shipped with a purpose-built runtime image
created with `jlink` or bundled by `jpackage`; a separately installed, general-purpose JRE is not the
only deployment model.

## Can a Java application run without JRE?

**Answer**

A Java application needs a compatible Java runtime: a JVM plus the required Java modules and native
libraries. It does **not** require a separately installed product named “JRE.” The runtime may come
from a JDK installation or may be a custom image bundled with the application using `jlink` or
`jpackage`.

Compilation normally uses `javac` from a JDK. Execution uses the `java` launcher and JVM from the
selected runtime image.

## What are different JVM components?

**Answer**

The JVM includes a class-loading subsystem; runtime data areas such as the heap, per-thread JVM
stacks and program counters, the method area, and native stacks; and an execution engine that may
interpret and JIT-compile bytecode. Garbage collectors reclaim unreachable heap objects. JNI and
other native interfaces connect managed code to platform libraries. Exact implementation details,
such as code caches and compiler tiers, vary by JVM and are not all prescribed by the JVM
specification.

## What are class loaders?

**Answer**

Class loaders locate class bytes and define `Class` objects. The lifecycle is loading, linking
(verification, preparation, and optional resolution), then initialization when required. Modern Java
uses bootstrap, platform, and application class loaders; the old extension-class-loader and
`lib/ext` mechanism was removed with the module-system transition. Custom loaders support plugin,
container, and isolation use cases. Parent-first delegation is common but not an absolute rule for
every custom loader.

## Is it possible to unload a class in Java?

**Answer**

There is no API to unload one class explicitly. A class can become unloadable when its defining
class loader, all classes it defined, and their reachable instances are no longer reachable. The JVM
decides when unloading occurs, usually during an appropriate garbage-collection cycle. Long-lived
threads, static registries, thread locals, JNI references, and caches commonly prevent plugin class
loaders from becoming unreachable.

## What is the difference between class loader and class forName?

**Answer**

`ClassLoader.loadClass(name)` loads through that loader and normally does not initialize the class.
`Class.forName(name)` uses the caller's loader and initializes the class by default. The overload
`Class.forName(name, initialize, loader)` makes both choices explicit. Loading obtains a `Class`
object; initialization runs static field initializers and static blocks when the JVM's initialization
rules require it.

## What is meta space in JVM?

**Answer**

HotSpot introduced metaspace in Java 8 to replace PermGen for class metadata. It uses native memory
and grows as classes are loaded, subject to native-memory availability and limits such as
`-XX:MaxMetaspaceSize`. `-XX:MetaspaceSize` is an initial threshold that influences collection, not a
simple fixed initial allocation. Space can be reclaimed when class loaders and their classes are
unloaded.

## What are the different types of memory in Java?

**Answer**

The JVM specification defines a shared heap, a method area, and per-thread JVM stacks, program
counters, and native-method stacks. Objects and arrays normally live on the heap; frames contain
local-variable slots, operand stacks, and call state. HotSpot implements class metadata in native
metaspace and also has implementation-specific areas such as code caches. Young/old generations are
collector implementation choices, not a universal JVM memory layout.

## Which memory is faster Heap or Stack?

**Answer**

The premise is too broad. JVM stack frames are allocated and discarded with method calls, while
objects normally live on the heap, but access speed depends on generated machine code, cache
locality, escape analysis, allocation behavior, and contention. A local variable can hold a reference
to a shared heap object, so “stack” does not make the referenced state thread-safe. HotSpot can also
eliminate allocations or replace an object with scalar values. Measure the real workload rather than
choosing a structure because one region is assumed to be faster.

## What is the Java Memory Model?

**Answer**

The Java Memory Model defines which writes a read may observe and the ordering guarantees between
threads. A *happens-before* relationship makes earlier effects visible to the later action. It is
established by rules including program order, monitor unlock/lock, volatile write/read, thread
start/join, and transitivity. `volatile` provides visibility and ordering for that variable but does
not make a compound action such as `count++` atomic. Locks provide mutual exclusion plus memory
visibility. “Main memory” and “working memory” are specification concepts, not literal CPU caches.

## How does Java Memory Model affect the visibility of changes made from one thread to another?

**Answer**

A write in one thread is guaranteed visible to a read in another only when the actions are ordered by
a happens-before edge or another specified synchronization guarantee. Without one, the reader may
observe a stale value and the compiler or processor may legally reorder independent actions. Safe
publication can use locks, volatile fields, final-field construction guarantees, concurrent
collections, thread start/join, or higher-level concurrency utilities.

## Describe a scenario in a multithreaded environment where improper handling of Java Memory Model could cause issues?

**Answer**

Suppose one thread writes ordinary fields `data = result; ready = true;` and another spins until
`ready` and then reads `data`. With no synchronization, the reader is not guaranteed to see either
write in the intended order. Making `ready` volatile establishes a volatile write/read happens-before
edge, so writes before publishing `ready` become visible after the reader observes it. For a compound
bank transfer, a volatile flag is insufficient; the debit and credit need one atomic protocol,
usually coordinated locks or a transactional boundary.

## How does garbage collection work in Java?

**Answer**

Collectors trace from GC roots such as live thread stacks, static references, and JNI handles.
Objects not reachable through that graph are eligible for reclamation, including unreachable cycles.
Collectors differ in how they mark, copy, compact, partition, and process memory concurrently with
application threads. Do not assume every collector uses identical young/old regions or that “major”
and “full” GC are interchangeable terms. Select and tune a collector from measured latency,
throughput, allocation rate, heap occupancy, and pause evidence.

## Explain a bit about different Garbage Collection Algorithms?

**Answer**

- **Mark-sweep:** mark reachable objects, then reclaim unmarked space; fragmentation may remain.
- **Mark-compact:** mark live objects and move them together, trading relocation work for contiguous
  free space.
- **Copying:** copy live objects to another region and reclaim the source region at once.
- **Generational:** collect regions based on the empirical tendency of many objects to die young.
- **Concurrent or incremental:** perform parts of collection alongside application work or in smaller
  phases, generally with barriers and some remaining stop-the-world work.

Real collectors combine these techniques rather than implementing one textbook algorithm.

## How does Garbage Collector works in Java Memory Model

**Answer**

Garbage collection and the Java Memory Model are different concepts. GC determines object
reachability and reclaims storage; the JMM defines legal inter-thread observations and ordering.
Collectors preserve JMM guarantees while relocating objects and coordinating with application
threads, using safepoints and barriers as needed. Current HotSpot choices include Serial, Parallel,
G1, and ZGC; availability depends on the JDK build. CMS was removed, and Shenandoah is available in
some OpenJDK distributions rather than every JDK.

## What is Generational GC?

**Answer**

Generational collection groups objects by age because many workloads create numerous short-lived
objects. New allocations enter young regions; survivors may age and be promoted to old regions, so
young collections can examine a smaller area frequently. Remembered sets or card tables track
old-to-young references. Metaspace is class-metadata storage, not a heap generation. The exact region
layout and terminology depend on the collector, and generational operation is an implementation
strategy rather than a Java semantic guarantee.

## How does garbage collection handle circular references?

**Answer**

- **Reachability Analysis:** The garbage collector starts from root references and marks all reachable objects.
Objects not marked as reachable are considered unreachable and eligible for garbage collection.
- **Handling Circular References:** Circular references do not affect the reachability analysis.
If a group of objects reference each other but are not reachable from any root reference, they are considered unreachable.
The garbage collector will collect these objects, breaking the cycle.

## What is finalize method in Java?

**Answer**

`Object.finalize()` was a finalization callback that the JVM could invoke after an object became
unreachable. There was never a guarantee that it would run promptly or at all. Finalization is
unreliable, can resurrect objects, delays reclamation, and creates security and performance risks.

Finalization is deprecated for removal. Use deterministic cleanup with `AutoCloseable` and
try-with-resources. Use `Cleaner` only as a carefully designed safety net for state that does not
retain the cleaned object.

## Why is finalize deprecated?

**Answer**

It was deprecated in Java 9 and deprecated for removal by JEP 421 in Java 18. Its execution is
unpredictable, it can keep objects alive unexpectedly, and it complicates garbage collection and
security reasoning. Prefer explicit lifecycle management and try-with-resources.

## What is the Java LTS version?

**Answer**

Java 25 is Oracle's current long-term-support release. Oracle designates Java 8, 11, 17, 21, and 25
as LTS releases. “LTS” is a vendor support designation, so duration, licensing, and available updates
depend on the chosen JDK distribution. Check the current vendor roadmap instead of memorizing the
latest six-month feature release.

**Further reading**

- [Oracle Java SE Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [JEP 421: Deprecate Finalization for Removal](https://openjdk.org/jeps/421)
- [`jpackage` packaging overview](https://docs.oracle.com/en/java/javase/26/jpackage/packaging-overview.html)

## What are some well-known Java 8 features?

**Answer**

- **Lambda Expressions:** Provide a concise way to represent one method interface using an expression.
- **Stream API:** Offers a functional approach to processing sequences of elements.
- **Default Methods:** Allow adding new methods to interfaces without breaking existing implementations.
- **Functional Interfaces:** Interfaces with a single abstract method, enabling lambda expressions and method references.
- **Optional:** models a possibly absent return value and supports declarative composition.
- **Method References:** Provide a way to refer to methods without invoking them.
- **New Date and Time API:** A comprehensive and user-friendly date and time API.
- **Nashorn:** Java 8 included this JavaScript engine; it was deprecated later and removed in Java 15,
  so it is historical rather than a current platform feature.

## Why was Java 8 introduced?

**Answer**

Shift from Imperative to Declarative Programming: Java 8 introduced features that support declarative programming, allowing developers to focus on what they want to achieve rather than how to achieve it. This results in more concise and readable code.
- **Improved Handling of Null Values:** The introduction of the Optional class provides a more expressive way to handle null values, reducing the risk of NullPointerException and encouraging explicit handling of the presence or absence of values.
- **Enhanced Date and Time API:** Java 8 introduced a new Date and Time API that is more intuitive, immutable, and thread-safe, simplifying date and time manipulation and reducing the likelihood of errors.
- **Embracing Functional Programming:** To support modern programming paradigms and improve code readability and maintainability.
- **Enhancing Developer Productivity:** To simplify common tasks, reduce boilerplate code, and improve productivity.
- **Improving Performance and Scalability:** To leverage multi-core processors and improve parallel processing capabilities.
- **Addressing Long-Standing Issues:** To modernize the language and address limitations in existing APIs.
- **Keeping Up with Industry Standards:** To stay competitive and align with modern development practices.
- **Enhancing Interoperability:** To improve integration with other languages and platforms.
- **Encouraging Best Practices:** To promote clean, maintainable, and robust code.

## What concurrency APIs and capabilities were added in Java 8?

**Answer**

- **CompletableFuture:** Provides a more flexible and powerful way to handle asynchronous programming.
Supports chaining, combining futures, and exception handling.
- **Parallel Streams:** Enables parallel processing of data using the Stream API.
Leverages multiple CPU cores for better performance.
- **New Methods in ConcurrentHashMap:** Introduced methods like computeIfAbsent, computeIfPresent, forEach, merge, and search for more efficient concurrent operations.
- **StampedLock:** added write, read, and optimistic-read modes for specialized coordination. It is
  not reentrant and optimistic reads must be validated.

These are library and stream additions, not a replacement Java Memory Model.

## What are some differences between Java 8 & Java 11?

**Answer**

- **Local-Variable Syntax for Lambda Parameters:** Allows using var in lambda expressions.
- **HTTP Client:** Standardized the HTTP Client API introduced in Java 9 for making HTTP requests.
- **String Methods:** Added new methods to the String class, such as isBlank(), lines(), strip(), repeat(), etc.
- **File Methods:** Added new methods to the Files class, such as readString(), writeString(), etc.
- **Running Java Files with java Command:** Allows running a single-file source-code program directly using the java command.
- **Nest-Based Access Control:** Introduced to improve access control for nested classes.
- **Deprecation and Removal of Features:** Removed the Java EE and CORBA modules, deprecated the Nashorn JavaScript Engine.

## What notable features were delivered in Java 17?

**Answer**

- **Sealed Classes (JEP 409):** Restrict which classes or interfaces can extend or implement them.
Pattern Matching for Switch (Preview) (JEP 406): Extends pattern matching to switch statements and expressions.
- **Strongly Encapsulate JDK Internals (JEP 403):** Enhances security by preventing access to non-public APIs.
Context-Specific Deserialization Filters (JEP 415): Allows fine-grained control over deserialization.
Foreign Function & Memory API (Incubator) (JEP 412): Interoperate with code and data outside of the Java runtime.
- **Deprecate the Applet API for Removal (JEP 398):** Marks the Applet API for future removal.
- **New macOS Rendering Pipeline (JEP 382):** Uses the Apple Metal framework for rendering on macOS.
Remove the Experimental AOT and JIT Compiler (JEP 410): Removes experimental AOT and JIT compiler features.
Enhanced Pseudo-Random Number Generators (JEP 356): Provides new interfaces and implementations for random number generators.
