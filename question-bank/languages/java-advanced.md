# Advanced Java Topics

Records, enums, memory diagnostics, serialization, JDBC, and CompletableFuture.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## What is a record class?

**Answer**

- **Record Class:** A special kind of class introduced in Java 14 (preview) and Java 16 (standard) for creating immutable data carriers.
- **Concise Syntax:** Provides a concise way to declare classes that primarily store data.
- **Shallowly immutable state:** component fields are final, but a component can reference a mutable
  object. Records do not make referenced collections or arrays immutable automatically.
- **Automatic Generation:** The compiler automatically generates the constructor, equals(), hashCode(), and toString() methods.
- **Components:** Fields of a record are called components.

## What is a canonical constructor?

**Answer**

- **Canonical Constructor:** A constructor automatically generated for record classes that initializes all the fields (components) of the record.
- **Automatic Generation:** The compiler generates the canonical constructor based on the components of the record.
- **Parameter Correspondence:** The parameters of the canonical constructor correspond to the components of the record.
- **Customization:** You can define your own canonical constructor to add validation or other logic.

## What are enums and what are their benefits?

**Answer**

Enums (short for enumerations) in Java are a special type of class that represents a fixed set of constants. Enums are used to define collections of constants that can be used to represent a specific set of values in a type-safe manner.
- **Type Safety:** Enums ensure that only valid values can be assigned to variables of the enum type, reducing the risk of errors.
- **Readability and Maintainability:** Enums provide meaningful names for a set of related constants, making the code easier to understand and maintain.
- **Namespace Management:** Enums provide a namespace for constants, preventing naming conflicts.
- **Built-in Methods:** Enums come with built-in methods like values(), valueOf(), name(), and ordinal().
- **Switch Statement Compatibility:** Enums can be used in switch statements for easier case handling.
- **Custom Methods and Fields:** Enums can have custom methods and fields, adding additional functionality and behavior.
- **Singleton Pattern:** Enums can be used to implement the Singleton pattern effectively.

## What is jagged array?

**Answer**

Java models multidimensional arrays as arrays of arrays. Each nested array is a separate object and
may have a different length or be `null`; “jagged array” simply emphasizes those unequal row lengths.

## Can you tell a bit about pass by value and pass by reference?

**Answer**

- **Pass by Value:** Definition: The function receives a copy of the argument's value.
- **Behavior in Java:** Java uses pass by value for both primitive types and object references. For objects, the reference itself is passed by value.
- **Example:** Modifying a primitive type within a method does not affect the original value. Modifying an object's state within a method affects the original object.
- **Pass by Reference:** Definition: The function receives a reference to the actual data, allowing it to modify the original argument.
- **Behavior in Other Languages:** Some languages support pass by reference, allowing functions to modify the original data directly.
- **Example:** In C++, passing a reference to a function allows the function to modify the original value.

## Can we use pointers in Java?

**Answer**

Java source has object references but no general pointer arithmetic or language-level access to raw
addresses. References are passed by value and managed by the runtime. Native interoperation is still
possible through supported APIs such as JNI or the Foreign Function and Memory API, where lifetime,
bounds, and native-safety concerns must be handled explicitly.

## What are Memory Leaks and Heap Dumps?

**Answer**

- **Memory Leaks:** Definition: Occurs when a program allocates memory but fails to release it, leading to increased memory usage and potential crashes.
- **Causes:** Unreleased resources, static references, listener and callback references, collections, inner classes.
- **Example:** Adding objects to a list and not removing them.
- **Heap Dumps:** Definition: A snapshot of the memory of a Java process at a specific point in time, containing information about all objects in the heap.
- **Uses:** Diagnosing memory leaks, analyzing memory usage, performance tuning.
- **Generating:** Using JVM options, JVisualVM, or jcmd.
- **Analyzing:** Using tools like Eclipse MAT, JVisualVM, or YourKit to identify memory issues and optimize memory usage

## What are some common things that cause Memory leaks in Java?

**Answer**

- **Unclosed resources:** these usually leak operating-system or pool resources rather than Java heap
  by themselves, though their owners may also remain reachable. Use try-with-resources.
- **Static Fields:** Holding references to objects in static fields.
- **Solution:** Avoid using static fields for large collections of objects.
- **Inner Classes and Anonymous Classes:** Non-static inner classes and anonymous classes holding references to their enclosing instance.
- **Solution:** Use static inner classes if possible.
- **Listeners and Callbacks:** Registering listeners or callbacks without unregistering them.
- **Solution:** Properly unregister listeners and callbacks.
- **Caching:** Caching objects without proper eviction policies.
- **Solution:** Use caching libraries with built-in eviction policies.
- **ThreadLocal Variables:** Not cleaning up ThreadLocal variables.
- **Solution:** Ensure ThreadLocal variables are removed when no longer needed.
- **Large Collections:** Holding references to large collections that grow indefinitely.
- **Solution:** Use weak references or implement proper cleanup mechanisms.

## Can Polymorphism lead to memory issues? If so then in what scenario?

**Answer**

- **Polymorphism:** Polymorphism itself does not inherently cause memory issues, but certain scenarios involving polymorphic behavior can lead to memory-related problems.
- **Memory Leaks:** Improper resource management in polymorphic objects can lead to memory leaks.
- **Object Retention:** Polymorphic references can cause unintended object retention, leading to high memory usage.
- **Excessive Object Creation:** Polymorphic behavior can lead to excessive object creation if not managed properly.
- **Best Practices:** Proper resource management, avoiding unnecessary object retention, using weak references, monitoring memory usage, and implementing resource cleanup can help prevent memory issues related to polymorphism.

## What are different ways to detect memory leaks in Java?

**Answer**

- **Profilers:** Tools like VisualVM, YourKit, and JProfiler provide real-time monitoring and heap dump analysis.
- **GC Logs:** Enable and analyze garbage collection logs using tools like GCViewer and GCEasy.
- **Heap Dumps:** Generate and analyze heap dumps using tools like Eclipse MAT.
- **Code Analysis Tools:** Use static code analysis tools like FindBugs/SpotBugs and SonarQube to detect potential memory leaks.
- **Custom Monitoring:** Implement custom monitoring using WeakReference and MemoryMXBean to track memory usage programmatically.

## Explain a bit on terms related to Memory Profiling?

**Answer**

Eden Space is part of the young generation in generational collectors, and most new objects are
allocated there. When allocation pressure triggers a young collection, live objects may be copied
to survivor regions or promoted depending on the collector and object age.

- **Survivor Space:** Also part of the Young Generation.
- **Consists of two areas:** S0 (Survivor 0) and S1 (Survivor 1).
Objects that survive a minor GC in the Eden Space are moved to one of the Survivor Spaces.
Objects are copied between S0 and S1 during subsequent GCs until they are promoted to the Old Generation.
- **Heap:** The runtime data area from which memory for all class instances and arrays is allocated.
Divided into Young Generation (Eden Space and Survivor Spaces) and Old Generation (Tenured Space).
Managed by the Java Virtual Machine (JVM) and subject to garbage collection.
- **Heap Dump:** A snapshot of the heap memory at a given point in time.
Contains information about all the objects in memory, including their classes, fields, and references.
Useful for diagnosing memory leaks and analyzing memory usage.
- **Memory Profiling:** JProfiler provides tools to analyze memory usage, track object allocations, and monitor garbage collection.
Helps identify memory leaks, excessive memory consumption, and inefficient object creation patterns.
- **Using JProfiler:** Heap Walker: Explore the heap dump to see objects, their sizes, and references.
- **Allocation Call Tree:** Identify where objects are being allocated in the code.
- **Garbage Collection Monitoring:** Monitor GC activity and its impact on application performance.

## Explain a bit about JProfiler?

**Answer**

JProfiler is a comprehensive Java profiling tool developed by ej-technologies. It is designed to help developers analyze and optimize the performance of their Java applications. Here are the key points:
- **Key Features:** CPU Profiling: Identifies methods consuming the most CPU time.
- **Memory Profiling:** Detects memory leaks and optimizes memory usage through heap dumps and object allocation tracking.
- **Thread Profiling:** Monitors thread activity, states, contention, and lifecycles.
- **Heap Walker:** Provides detailed views of objects in the heap, including references and sizes.
- **Call Graphs:** Visualizes the call hierarchy and time spent in each method.
- **SQL and NoSQL Profiling:** Profiles database interactions and optimizes database performance.
- **Remote Profiling:** Profiles applications running on remote servers.
- **IDE Integration:** Integrates with popular IDEs like IntelliJ IDEA, Eclipse, and NetBeans.
- **Usage:** Installation: Download and install from the official website.
- **Attaching to JVM:** Attach to a running JVM or start a new profiling session.
- **Analyzing Data:** Use various views and tools to analyze CPU, memory, and thread data.
- **Generating Reports:** Create detailed reports for further analysis and documentation.
- **Example Use Case:** CPU Profiling: Optimize methods with high CPU usage.
- **Memory Profiling:** Detects and fixes memory leaks.
- **Thread Profiling:** Resolve thread contention and deadlocks.

## What are the strategies you will use to fix Memory Leaks in your application

**Answer**

- **Use Profiling Tools:** VisualVM, YourKit, JProfiler, Eclipse MAT.
- **Analyze Heap Dumps:** Generate and analyze heap dumps to identify memory leaks.
- **Identify and Fix Common Memory Leak Patterns:** Unclosed resources: Use try-with-resources.
- **Static references:** Avoid holding references in static fields.
- **Listener and callback registrations:** Deregister listeners and callbacks.
- **Inner classes:** Use static inner classes.
- **Optimize Data Structures:** Use appropriate data structures.
Clear collections when no longer needed.
- **Monitor and Tune Garbage Collection:** Monitor GC logs and tune GC parameters.
- **Reference types:** use weak or phantom references only when their semantics match the ownership
  model. They are not a general repair for accidental retention, and soft references are a poor
  substitute for a bounded cache.
- **Review and Refactor Code:** Conduct code reviews and refactor code to improve memory management.

## What is Marshalling and unmarshalling?

**Answer**

- **Marshalling:** Definition: Converting an object or data structure into a format that can be easily stored or transmitted.
- **Purpose:** Prepare data for transmission over a network or for storage.
- **Example:** Converting a Java object into XML or JSON.
- **Unmarshalling:** Definition: Converting the marshalled data back into an object or data structure.
- **Purpose:** Reconstruct the original object or data structure from the transmitted or stored data.
- **Example:** Converting XML or JSON back into a Java object.

## What is the transient keyword in java?

**Answer**

transient Keyword:
Used to indicate that a field should not be serialized.
Prevents sensitive, temporary, or irrelevant data from being included in the serialized representation of an object.
- **Usage:** Place the transient keyword before the field declaration.
During deserialization, the transient field will be initialized to its default value.

## How do you do serialization in Java?

**Answer**

- **Serializable Interface:** Implement the Serializable interface to make a class serializable.
- **ObjectOutputStream:** Used to write serialized objects to an output stream.
- **ObjectInputStream:** Used to read serialized objects from an input stream.
serialVersionUID: A unique identifier for each class, used to ensure compatibility during deserialization.

## What is Serialization in Java and what are Serialization Attacks?

**Answer**

- **Serialization:** The process of converting an object's state into a byte stream.
Used for saving objects to files, sending over networks, or storing in databases.
- **Deserialization:** The reverse process of converting a byte stream back into an object.
- **Serialization Attacks:** Exploit vulnerabilities in the deserialization process.

**Can lead to remote code execution, denial of service, or data manipulation.**

- **Mitigation:** do not use native Java deserialization for untrusted input. Prefer a constrained
  data format with an explicit schema. Where legacy deserialization is unavoidable, authenticate and
  bound the input, apply a strict `ObjectInputFilter` allowlist and graph limits, minimize the
  classpath, and validate invariants. A custom `readObject` alone does not neutralize gadget chains.

## What challenges are faced when Serialization and Deserialization?

**Answer**

- **Versioning and Compatibility:** Manage changes to the class structure to ensure compatibility.
- **Security Risks:** Avoid deserializing untrusted data and use secure deserialization practices.
- **Performance Overhead:** Optimize the serialization format and use efficient libraries.
- **Handling Transient and Static Fields:** Ensure proper initialization and handling of transient and static fields.
- **Object Identity and Cyclic References:** Use frameworks that support object identity and cyclic references.
- **Serialization of Complex Object Graphs:** Use robust serialization libraries and implement custom logic if needed.
- **Platform and Language Independence:** Use platform-independent serialization formats and ensure consistent logic across platforms.

## What are different cloning types in Java?

**Answer**

- **Shallow Cloning:** Definition: Copies the object and its primitive fields, but not the objects referenced by the fields.
- **Implementation:** Implement Cloneable and override clone() method.
- **Use Case:** Suitable for objects with only primitive fields or immutable objects.
- **Example:** Changes to the cloned object's referenced objects affect the original object's referenced objects.
- **Deep Cloning:** Definition: Copies the object and recursively copies all objects referenced by the fields.
- **Implementation:** Implement Cloneable, override clone() method, and manually clone referenced objects.
- **Use Case:** Suitable for objects with references to mutable objects.
- **Example:** Changes to the cloned object's referenced objects do not affect the original object's referenced objects.

## What is the Difference Between Statement and PreparedStatement in Java?

**Answer**

Statement
- **Purpose:** Used to execute simple SQL queries without parameters.
- **Syntax:** SQL queries are passed directly as strings.
- **Performance:** Generally slower for repeated execution because the SQL query is parsed and compiled each time it is executed.
- **Security:** More vulnerable to SQL injection attacks because user input is directly concatenated into the SQL query.
- **Usage:** Suitable for executing static SQL queries that do not require parameters.
PreparedStatement
- **Purpose:** Used to execute precompiled SQL queries with or without parameters.
- **Syntax:** SQL queries are precompiled and parameters are set using setter methods.
- **Performance:** can reuse a prepared execution plan and batch parameters, but actual preparation
  and caching depend on the JDBC driver, connection, and database. Do not promise a compile-once
  speedup universally.
- **Security:** parameter binding prevents input from becoming SQL syntax for value placeholders.
  Identifiers and keywords generally cannot be bound, so dynamic table/order choices still need a
  strict allowlist.
- **Usage:** Suitable for executing dynamic SQL queries that require parameters.

## How would you combine multiple completable futures into a single completable future?

**Answer**

- **Combining with allOf:** Combines multiple CompletableFuture instances into a single CompletableFuture that completes when all of them complete.

**Does not return the results of the individual futures.**

- **Combining with anyOf:** Combines multiple CompletableFuture instances into a single CompletableFuture that completes when any one of them completes.
Returns the result of the first completed future.
- **Combining with thenCombine:** Combines two CompletableFuture instances and applies a function to their results.
Returns a new CompletableFuture that is completed with the result of the function.
