# Java

Core Java, object-oriented programming, collections, concurrency, JVM behavior, streams, testing, and coding exercises.

[Back to the question-bank index](../README.md)

## Topic Map

- [JVM, memory, garbage collection, and Java releases](#what-is-jvm-jdk-and-jre)
- [Core language and object-oriented programming](#how-is-java-platform-independent)
- [Functional interfaces and streams](#what-is-functional-interface)
- [Equality, object contracts, types, and annotations](#what-are-equals-and-hashcode-methods)
- [Exceptions and resource handling](#what-are-exceptions-in-java)
- [Concurrency and thread safety](#tell-a-bit-about-mutex-semaphores-threads-processes-and-program)
- [Generics and collections](#what-are-generics-in-java)
- [Records, memory analysis, serialization, JDBC, and testing](#what-is-a-record-class)
- [Coding and output exercises](#create-a-list-of-employees-object-from-a-hashmap-whose-key-is-string-id-and-value-is-an-basicinfo-object)

## What are the advantages and disadvantages of using Java for Enterprise Level Development

**Answer**

Advantages:
Platform Independence: Write once, run anywhere.
Scalability: Suitable for large-scale applications.
Robust Ecosystem: Rich libraries and frameworks.
Strong Community Support: Extensive documentation and resources.
Security: Built-in security features.
Performance: Optimized through JIT compilation and garbage collection.
Enterprise Integration: Extensive support for integrating with other systems.
Disadvantages:
Memory Consumption: Higher memory usage compared to some other languages.
Performance Overhead: JVM introduces some performance overhead.
Complexity: Verbose syntax and boilerplate code.
Startup Time: Slower startup times.
Learning Curve: Steep learning curve for new developers.
Licensing and Costs: Potential licensing fees for some distributions.

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

Class Loader Subsystem: Loads, links, and initializes classes.
Runtime Data Areas:
Method Area: Stores class-level data.
Heap: Stores objects and arrays.
Stack: Stores local variables and method call frames.
Program Counter (PC) Register: Stores the address of the current instruction.
Native Method Stack: Stores native method information.
Execution Engine:
Interpreter: Executes bytecode instructions one by one.
JIT Compiler: Compiles bytecode into native machine code at runtime.
Garbage Collector: Reclaims memory used by objects that are no longer needed.
Native Interface: Allows interaction with native libraries and applications.
Native Method Libraries: Provide native methods for the JVM.

## What are class loaders?

**Answer**

Class Loaders: Responsible for dynamically loading Java classes into memory during runtime.
Key Concepts:
Loading: Finding and loading the binary representation of a class.
Linking: Verifying and preparing the loaded class for use.
Initialization: Initializing the class, including executing static initializers.
Types of Class Loaders:
Bootstrap Class Loader: Loads core Java classes from the JRE.
Extension Class Loader: Loads classes from the Java extensions directory.
Application (System) Class Loader: Loads classes from the application's classpath.
Custom Class Loaders: Developers can create custom class loaders by extending the ClassLoader class to load classes from non-standard sources.
Class Loader Hierarchy: Class loaders follow a delegation model, where a class loader delegates the class loading request to its parent class loader before attempting to load the class itself.

## Is it possible to unload a class in Java?

**Answer**

Class Loading:
Classes are loaded by class loaders in Java.
The JVM uses a hierarchy of class loaders to load classes.
Class Unloading:
Classes cannot be explicitly unloaded.
Classes can be unloaded indirectly when the class loader that loaded them becomes unreachable and is garbage collected.
The JVM does not provide an API to explicitly unload classes.
Custom Class Loaders:
Custom class loaders can be used to load classes dynamically.

**When the custom class loader is no longer needed and becomes unreachable, it can be garbage collected, allowing the classes it loaded to be unloaded.**

## What is the difference between class loader and class forName?

**Answer**

ClassLoader:
An object responsible for loading classes into the JVM.
Provides methods like loadClass(String name) to load classes.
Allows for custom class loading by extending the ClassLoader class.

**Does not initialize the class when loading it.**

Class.forName():
A static method in the Class class that loads and initializes a class by its fully qualified name.
Convenient for loading and initializing classes at runtime.
Differences:
Initialization: ClassLoader does not initialize the class, while Class.forName() does.
Control: ClassLoader provides more control over the class loading process.
Usage Context: ClassLoader is used for custom class loading, while Class.forName() is used for immediate initialization when the class name is known at runtime.

## What is meta space in JVM?

**Answer**

Metaspace: A memory space in the JVM introduced in Java 8 to replace PermGen, used to store class metadata.
Dynamic Sizing: Metaspace can grow dynamically based on the application's needs, reducing the likelihood of OutOfMemoryError.
Native Memory: Metaspace is allocated in native memory (outside the Java heap).
Class Metadata Storage: Stores information about class structures, methods, fields, and other class-related data.
Garbage Collection: The JVM can perform garbage collection on Metaspace to reclaim memory used by classes that are no longer needed.
Configuration: Metaspace size can be configured using JVM options like -XX:MetaspaceSize and -XX:MaxMetaspaceSize.

## What are the different types of memory in Java?

**Answer**

Heap Memory: For dynamic object allocation, managed by the garbage collector.
- Young Generation: Eden Space, Survivor Spaces (S0, S1)
- Old Generation: Long-lived objects
Stack Memory: For method call frames, local variables, and method parameters.
Metaspace: For class metadata, replaced PermGen in Java 8.
Program Counter (PC) Register: Tracks the current instruction for each thread.
Native Method Stack: For native method calls.

## Which memory is faster Heap or Stack?

**Answer**

Stack Memory:
Speed: Faster access due to LIFO principle and CPU cache storage.
Memory Management: Automatic allocation and deallocation, no garbage collection.
Scope and Lifetime: Used for local variables, short-lived.
Size Limitations: Limited size, risk of stack overflow.
Heap Memory:
Speed: Slower access due to dynamic allocation and garbage collection.
Memory Management: Manual or automatic management, requires garbage collection.
Scope and Lifetime: Used for global variables and objects, long-lived.
Size Limitations: Larger size, can accommodate more data.
In a multithreaded application that frequently access shared data how does heap memory or stack memory affects performance
Heap Memory:
Shared Access: Shared among all threads, requiring synchronization for thread safety.
Garbage Collection: Can impact performance due to pauses.
Memory Contention: Can lead to increased latency and reduced throughput.
Example: Shared objects and instance variables.
Stack Memory:
Thread-Local Storage: Private to each thread, eliminating the need for synchronization.
Memory Allocation: Faster allocation and deallocation.
Stack Size: Limited size, risk of StackOverflowError.
Example: Local variables and method call frames.
Best Practices
Minimize Shared Data: Reduce the amount of shared data to minimize synchronization overhead and memory contention.
Use Thread-Local Storage: Use thread-local variables (ThreadLocal) for data that is specific to a thread and does not need to be shared.
Optimize Synchronization: Use fine-grained locking or lock-free algorithms to reduce contention and improve performance.
Monitor and Tune Garbage Collection: Monitor garbage collection performance and tune GC settings to minimize pauses in a multithreaded environment.

## What is the Java Memory Model?

**Answer**

Java Memory Model (JMM): A specification that defines how threads interact through memory, ensuring visibility, atomicity, and ordering of operations in a multi-threaded environment.
Main Memory and Working Memory: Variables are stored in main memory, and each thread has its own working memory (cache).
Visibility: Ensures that changes made by one thread to shared variables are visible to other threads.
Atomicity: Ensures that a series of operations are performed as a single, indivisible unit.
Ordering: Ensures that operations are executed in a specific sequence, defined by the happens-before relationship.
Volatile Variables: Provide visibility and ordering guarantees for reads and writes.
Synchronized Blocks: Ensure mutual exclusion and visibility for critical sections of code.
Happens-Before Relationship: Defines a partial ordering of operations, ensuring visibility and correct ordering.

## How does Java Memory Model affect the visibility of changes made from one thread to another?

**Answer**

The Java Memory Model (JMM) defines how threads interact through memory and ensures that changes made by one thread are visible to other threads. It provides rules and guarantees for visibility, ordering, and atomicity of operations in a multi-threaded environment.

## Describe a scenario in a multithreaded environment where improper handling of Java Memory Model could cause issues?

**Answer**

Scenario: Bank account transfer with multiple threads performing money transfers between accounts.
Issues:
Visibility Issues: Changes made by one thread may not be visible to other threads.
Race Conditions: Concurrent access and modification of shared data can lead to race conditions.
Inconsistent State: Lack of synchronization can result in an incorrect final state.
Solution: Use proper synchronization to ensure atomicity and visibility of operations, preventing race conditions and ensuring consistent state.

## How does garbage collection work in Java?

**Answer**

Garbage Collection (GC): The process of automatically identifying and reclaiming memory that is no longer in use by the application.
Heap Memory: Divided into the Young Generation and the Old Generation.
Young Generation: Where new objects are allocated, further divided into Eden Space and Survivor Spaces.
Old Generation: Where long-lived objects are stored.
Minor GC: Collects garbage in the Young Generation.
Major GC: Collects garbage in the Old Generation.
Garbage Collection Algorithms: Mark-and-Sweep, Mark-and-Compact, Copying.
Common Garbage Collectors: Serial GC, Parallel GC, CMS GC, G1 GC.
Configuration: JVM options can be used to configure the garbage collector and its parameters.

## Explain a bit about different Garbage Collection Algorithms?

**Answer**

Mark-and-Sweep Algorithm: Marks all reachable objects and sweeps unmarked objects. Can cause fragmentation.
Mark-and-Compact Algorithm: Marks all reachable objects and compacts them to eliminate fragmentation.
Copying Algorithm: Divides the heap into two regions and copies live objects between them. Eliminates fragmentation but requires more memory.
Generational Garbage Collection: Divides the heap into generations, optimizing garbage collection for young objects.
Incremental Garbage Collection: Breaks garbage collection into smaller steps to reduce pause times.
Concurrent Garbage Collection: Performs garbage collection concurrently with application threads to minimize pause times.

## How does Garbage Collector works in Java Memory Model

**Answer**

Java Memory Model:
Heap: Divided into Young Generation, Old Generation, and PermGen/Metaspace.
Stack: Stores local variables and method call frames.
Method Area: Stores class-level data.
Native Method Stacks: Store native method information.
Garbage Collection Process:
Generational GC: Divides the heap into generations to optimize GC.
Minor GC: Occurs in the Young Generation.
Major GC (Full GC): Occurs in the Old Generation.
Mark-and-Sweep Algorithm: Marks reachable objects and reclaims memory from unreachable objects.
Mark-and-Compact Algorithm: Marks reachable objects, reclaims memory, and compacts the heap.
Copying Algorithm: Copies live objects to Survivor Spaces and clears the Eden Space.
Types of Garbage Collectors:
Serial GC: Single-threaded GC.
Parallel GC: Multi-threaded GC for high throughput.
CMS GC: Concurrent GC to minimize pause times (deprecated).
G1 GC: Region-based GC for predictable pause times.
ZGC: Low-latency GC for large heaps.
Shenandoah GC: Low-pause-time GC with concurrent compaction.

## What is Generational GC?

**Answer**

Generational GC:
A garbage collection strategy that categorizes objects based on their age and manages them accordingly.
Divides the heap into generations: young generation, old generation, and permanent generation (Metaspace in Java 8+).
Generations:
Young Generation: Contains new objects, divided into Eden and survivor spaces.
Old Generation: Contains long-lived objects promoted from the young generation.
Permanent Generation (Metaspace): Stores metadata about classes and methods.
Garbage Collection Phases:
Minor GC: Collects garbage from the young generation.
Major GC (Full GC): Collects garbage from the old generation and may include the young generation.
Promotion:
Objects that survive multiple minor GCs are promoted to the old generation.
Advantages:
Efficiency in collecting short-lived objects.
Reduced pause times due to fast and frequent minor GCs.
Improved performance by reducing the frequency of major GCs.

## How does garbage collection handle circular references?

**Answer**

Reachability Analysis:
The garbage collector starts from root references and marks all reachable objects.
Objects not marked as reachable are considered unreachable and eligible for garbage collection.
Handling Circular References:
Circular references do not affect the reachability analysis.
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

As of October 2026, Java 25 is the latest long-term-support release designated by Oracle. Java 8,
11, 17, 21, and 25 are LTS releases; Java 27 is the latest feature release but is not LTS. “LTS” is
a vendor support designation, so confirm the support policy of the JDK distribution being used.

**Further reading**

- [Oracle Java SE Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [JEP 421: Deprecate Finalization for Removal](https://openjdk.org/jeps/421)
- [`jpackage` packaging overview](https://docs.oracle.com/en/java/javase/26/jpackage/packaging-overview.html)
**Answer**

LTS Versions: Java 8, Java 11, Java 17, and the upcoming Java 21 are designated as Long-Term Support (LTS) versions.
Extended Support: LTS versions receive extended support, including security patches and bug fixes, making them suitable for production environments.
Release Cadence: Oracle releases a new Java version every six months and an LTS version every three years.
Stability and Reliability: LTS versions are considered more stable and reliable, making them ideal for enterprises and developers who require a stable platform.

## What are some well-known Java 8 features?

**Answer**

Lambda Expressions: Provide a concise way to represent one method interface using an expression.
Stream API: Offers a functional approach to processing sequences of elements.
Default Methods: Allow adding new methods to interfaces without breaking existing implementations.
Functional Interfaces: Interfaces with a single abstract method, enabling lambda expressions and method references.
Optional Class: Represents optional values to avoid null checks.
Method References: Provide a way to refer to methods without invoking them.
New Date and Time API: A comprehensive and user-friendly date and time API.
Nashorn JavaScript Engine: Allows executing JavaScript code from within Java applications.

## Why was Java 8 introduced?

**Answer**

Shift from Imperative to Declarative Programming: Java 8 introduced features that support declarative programming, allowing developers to focus on what they want to achieve rather than how to achieve it. This results in more concise and readable code.
Improved Handling of Null Values: The introduction of the Optional class provides a more expressive way to handle null values, reducing the risk of NullPointerException and encouraging explicit handling of the presence or absence of values.
Enhanced Date and Time API: Java 8 introduced a new Date and Time API that is more intuitive, immutable, and thread-safe, simplifying date and time manipulation and reducing the likelihood of errors.
Embracing Functional Programming: To support modern programming paradigms and improve code readability and maintainability.
Enhancing Developer Productivity: To simplify common tasks, reduce boilerplate code, and improve productivity.
Improving Performance and Scalability: To leverage multi-core processors and improve parallel processing capabilities.
Addressing Long-Standing Issues: To modernize the language and address limitations in existing APIs.
Keeping Up with Industry Standards: To stay competitive and align with modern development practices.
Enhancing Interoperability: To improve integration with other languages and platforms.
Encouraging Best Practices: To promote clean, maintainable, and robust code.

## What are the changes in the Java Concurrency Model introduced in Java 8?

**Answer**

CompletableFuture:
Provides a more flexible and powerful way to handle asynchronous programming.
Supports chaining, combining futures, and exception handling.
Parallel Streams:
Enables parallel processing of data using the Stream API.
Leverages multiple CPU cores for better performance.
New Methods in ConcurrentHashMap:
Introduced methods like computeIfAbsent, computeIfPresent, forEach, merge, and search for more efficient concurrent operations.
StampedLock:
Provides an alternative to ReentrantReadWriteLock with better performance for certain use cases.
Supports optimistic reads, read and write locks, and stamped operations.

## What are some differences between Java 8 & Java 11?

**Answer**

Local-Variable Syntax for Lambda Parameters: Allows using var in lambda expressions.
HTTP Client: Standardized the HTTP Client API introduced in Java 9 for making HTTP requests.
String Methods: Added new methods to the String class, such as isBlank(), lines(), strip(), repeat(), etc.
File Methods: Added new methods to the Files class, such as readString(), writeString(), etc.
Running Java Files with java Command: Allows running a single-file source-code program directly using the java command.
Nest-Based Access Control: Introduced to improve access control for nested classes.
Deprecation and Removal of Features: Removed the Java EE and CORBA modules, deprecated the Nashorn JavaScript Engine.

## What are some recent updates in Java 17?

**Answer**

Sealed Classes (JEP 409): Restrict which classes or interfaces can extend or implement them.
Pattern Matching for Switch (Preview) (JEP 406): Extends pattern matching to switch statements and expressions.
Strongly Encapsulate JDK Internals (JEP 403): Enhances security by preventing access to non-public APIs.
Context-Specific Deserialization Filters (JEP 415): Allows fine-grained control over deserialization.
Foreign Function & Memory API (Incubator) (JEP 412): Interoperate with code and data outside of the Java runtime.
Deprecate the Applet API for Removal (JEP 398): Marks the Applet API for future removal.
New macOS Rendering Pipeline (JEP 382): Uses the Apple Metal framework for rendering on macOS.
Remove the Experimental AOT and JIT Compiler (JEP 410): Removes experimental AOT and JIT compiler features.
Enhanced Pseudo-Random Number Generators (JEP 356): Provides new interfaces and implementations for random number generators.

## How is Java platform independent?

**Answer**

Java Compiler: Compiles Java source code into platform-independent bytecode.
Java Bytecode: An intermediate representation that can be executed on any platform with a JVM.
Java Virtual Machine (JVM): Interprets and executes bytecode, providing a consistent runtime environment across different platforms.
Platform-Specific JVM Implementations: Each platform has its own JVM implementation, but all JVMs can execute the same bytecode.

## How does a Java code get executed?

**Answer**

Write Code: You write Java source code in a .java file.
Compile: The Java compiler (javac) compiles the source code into bytecode, which is stored in .class files.
Class Loader: The Java Class Loader loads the compiled bytecode into the Java Virtual Machine (JVM).
Bytecode Verification: The JVM verifies the bytecode to ensure it is valid and doesn't violate Java's security constraints.
Execution: The JVM's interpreter or Just-In-Time (JIT) compiler executes the bytecode. The JIT compiler may convert bytecode into native machine code for better performance.
Runtime Environment: The JVM provides a runtime environment with memory management, garbage collection, and other services.

## Why is Java partially Object Oriented? What are the benefits of it?

**Answer**

Primitive Data Types: Java includes primitive data types that are not objects, providing better performance in terms of memory and processing speed.
Static Methods and Variables: Java allows the use of static methods and variables, which belong to the class rather than to any specific instance, simplifying certain programming tasks.
Procedural Programming: Java supports procedural programming, allowing developers to write code using functions and procedures without strictly adhering to object-oriented principles.
Performance: The inclusion of primitive data types allows Java to achieve better performance.
Simplicity and Ease of Use: Static methods and variables simplify programming tasks.
Flexibility: Java's support for both object-oriented and procedural programming provides flexibility to developers.
Backward Compatibility: Java's design allows for backward compatibility with older code that may not strictly adhere to object-oriented principles.

## Why were OOPs introduced in Java?

**Answer**

Modularity and Reusability:
Encapsulation: Promotes modularity by encapsulating data and behavior within objects.
Inheritance: Enables code reuse and reduces redundancy.
Maintainability and Extensibility:
Separation of Concerns: Simplifies maintenance by dividing a program into distinct objects.
Polymorphism: Allows for easy extension and modification of existing code.
Abstraction and Encapsulation:
Simplified Interfaces: Defines abstract classes and interfaces to simplify interactions.
Data Hiding: Protects the integrity of data by hiding internal state.
Real-World Modeling:
Natural Mapping: Models real-world entities and interactions more naturally.
Improved Collaboration and Teamwork:
Clear Contracts: Provides clear contracts for collaboration.
Modular Development: Allows teams to divide work into manageable units.

## What exactly is public static void main(String[] args)?

**Answer**

public: Access modifier that makes the main method accessible from anywhere, allowing the JVM to call it.
static: Indicates that the main method belongs to the class and can be called without creating an instance of the class.
void: Specifies that the main method does not return any value.
main: The name of the method that serves as the entry point of the Java application.
String[] args: An array of String objects representing command-line arguments passed to the program.

## What would happen if the main method is not declared as static?

**Answer**

JVM Invocation: The main method must be static so that the JVM can invoke it without creating an instance of the class.
Entry Point: Declaring the main method as static provides a consistent and predictable way to start the program.
Runtime Error: If the main method is not declared as static, the JVM will not be able to find the method with the correct signature, resulting in a runtime error

## Can we have multiple public classes in Java?

**Answer**

No, in Java, a source file can contain only one public class, and the name of that public class must match the name of the file. This is a requirement of the Java language specification to ensure consistency and predictability in the organization of code.
Java had an interesting approach: where giving a programmer a choice can only degrade the programming experience, remove the choice.

## What are different data types in Java?

**Answer**

Java has two main categories of data types: primitive data types and reference data types.
Primitive Data Types
byte: 8-bit integer, range: -128 to 127
short: 16-bit integer, range: -32,768 to 32,767
int: 32-bit integer, range: -2^31 to 2^31-1
long: 64-bit integer, range: -2^63 to 2^63-1
float: 32-bit floating-point
double: 64-bit floating-point
char: 16-bit Unicode character
boolean: true or false
Reference Data Types
Classes: e.g., String, Scanner
Interfaces: e.g., Runnable, Serializable
Arrays: e.g., int[], String[]
Enums: e.g., enum Day { MONDAY, TUESDAY, ... }

## What are Strings in Java and what is String constant pool?

**Answer**

Strings: Immutable objects representing sequences of characters.
String Constant Pool (also known as the String Intern Pool) is a special memory region in the Java heap where String literals are stored. When a String literal is created, the JVM checks the pool to see if an identical String already exists. If it does, the reference to the existing String is returned. If not, the new String is added to the pool.

## What is the difference between string and string StringBuffer?

**Answer**

Immutability:
String: Immutable; values cannot be changed after creation.
StringBuffer: Mutable; values can be changed after creation.
Performance:
String: Less efficient for frequent modifications due to the creation of new objects.
StringBuffer: More efficient for frequent modifications; does not create new objects.
Thread Safety:
String: Inherently thread-safe due to immutability.
StringBuffer: Synchronized and thread-safe for use in multi-threaded environments.
Usage:
String: Suitable for storing and manipulating fixed strings.
StringBuffer: Suitable for building and modifying strings in a thread-safe manner.

## How String and StringBuffer handle memory differently

**Answer**

String:
Immutability: String objects are immutable, meaning their content cannot be changed after creation.
Memory Allocation: String literals are stored in the string pool, while String objects created with the new keyword are stored in the heap.
String Pool: Helps save memory by reusing existing string objects, but modifications result in new object creation.
Memory Efficiency: Less efficient for frequent modifications due to the creation of new objects.
StringBuffer:
Mutability: StringBuffer objects are mutable, meaning their content can be changed after creation.
Memory Allocation: Allocates a buffer with an initial capacity that can grow dynamically as needed.
Buffer Management: Modifies the existing buffer without creating new objects, but resizing the buffer can be costly.
Memory Efficiency: More efficient for frequent modifications, as it avoids creating multiple intermediate objects.

## What is StringBuffer and StringBuilder in Java?

**Answer**

Both of these are used to create mutable strings
StringBuffer: Synchronized, thread-safe, slightly slower.
StringBuilder: Not synchronized, not thread-safe, faster.

## What is the difference between String Literal and String Object?

**Answer**

String Literal:
Creation: Using double quotes (e.g., String str1 = "Hello";).
String Pool: Stored in the string pool, shared if identical.
Memory Management: Managed by the JVM, automatically interned.
Performance: Faster access due to interning.
Comparison: Can use == operator for comparison.
String Object:
Creation: Using the new keyword (e.g., String str3 = new String("Hello");).
Heap Memory: Stored in the heap, each new object creates a new object.
Memory Management: Managed by the garbage collector, not automatically interned.
Performance: Slower due to new object creation.
Comparison: Use equals() method for comparison.

## Why are strings immutable in Java?

**Answer**

Security: Immutable strings prevent unauthorized modification of sensitive data.
Thread Safety: Immutable strings are inherently thread-safe, eliminating the need for synchronization.
Caching and Performance: String pooling and hash code caching improve memory efficiency and performance.
Hash Code Caching: Efficient hashing for operations like hash-based lookups.
Design Simplicity: Predictable behavior and simplified design lead to more reliable code.

## Why would we prefer passwords in character array and not in strings?

**Answer**

Immutability of Strings:
Strings are immutable, meaning their contents cannot be changed once created.
Sensitive data stored in strings remains in memory until garbage collected, increasing the risk of exposure.
Explicit Clearing of Data:
Character arrays are mutable, allowing their contents to be modified.
You can explicitly overwrite the contents of a character array to clear sensitive data from memory.
Garbage Collection Behavior:
The garbage collector does not guarantee when or if it will remove a particular object from memory.
Using a character array allows you to control the lifecycle of sensitive data more precisely.

## What is String Constant Pool and how does it help in optimization?

**Answer**

String Constant Pool: A special memory region in the Java heap where string literals are stored and reused.
String Immutability: Strings in Java are immutable, allowing them to be safely shared and reused.
String Literals: When a string literal is created, the JVM checks the pool for an existing identical string and reuses it if found.
String Interning: The intern() method can be used to manually add strings to the pool or retrieve references to existing strings in the pool.
Benefits:
Memory Optimization: Reduces the number of string objects created, leading to more efficient memory usage.
Performance Improvement: Faster string comparison using the == operator for references from the pool.

## What is String interning and how does it influence comparison?

**Answer**

String Interning: A method of storing only one copy of each distinct string value in a pool.
String Pool: A special memory region where interned strings are stored.
Interning a String: Using the intern() method to add a string to the pool or retrieve the reference to an existing interned string.
Influence on Comparison:
Reference Comparison (==): Interned strings with the same value will have the same reference, so == will return true.
Content Comparison (equals()): Always compares the actual content of the strings, unaffected by interning.
Benefits:
Memory Efficiency: Reduces memory usage by storing only one copy of each distinct string value.
Performance Improvement: Allows for fast reference comparison using ==.

## What is the final keyword?

**Answer**

Final Variables: Constants that cannot be reassigned.
Final Methods: Methods that cannot be overridden.
Final Classes: Classes that cannot be subclassed.
Final Objects: The reference cannot be changed to point to a different object, but the state of the object can still be modified if the object's class is mutable.

## A class is not final but we are not able to extend it. What could be the different reasons?

**Answer**

Private Constructor: The class has a private constructor.
Package-Private Class: The class has package-private access and is in a different package.
Package-Private Constructor: The class has a package-private constructor and is in a different package.
Security Manager Restrictions: Restrictions imposed by a security manager.
Abstract Methods Not Implemented: The subclass does not implement all abstract methods of the abstract class.
Final Methods: Specific methods in the class are declared as final.
Static Methods: Static methods cannot be overridden but can be hidden.

## What would you do If you don't want a class to be inherited?

**Answer**

If you don't want a class to be inherited in Java, you can declare the class as final. A final class cannot be subclassed.

## How will you create an Immutable class and object?

**Answer**

Declare the Class as final: Prevents subclassing.
Make All Fields private and final: Ensures fields are immutable and cannot be accessed or modified directly.
Provide a Constructor to Initialize All Fields: Initializes all fields and ensures they cannot be modified later.

Do not provide setter methods. Make defensive copies of mutable constructor arguments and return
copies or immutable views from accessors so callers cannot mutate internal state.

## In which scenarios you will use immutable objects?

**Answer**

Thread Safety:
Immutable objects are inherently thread-safe and do not require synchronization.
Example: ImmutablePoint
Caching and Memoization:
Immutable objects can be safely cached and reused without worrying about state changes.
Example: FibonacciCache
Functional Programming:
Immutable objects align well with functional programming principles, avoiding side effects.
Example: FunctionalExample
Defensive Copying:
Immutable objects eliminate the need for defensive copying to protect internal state.
Example: ImmutablePerson
Simplifying Code and Reducing Bugs:
Immutable objects make it easier to reason about code and ensure consistent state.
Example: ImmutableRectangle
Value Objects:
Immutable value objects ensure consistent state and can be safely compared and used in collections.
Example: Money

## Can you tell the execution flow what happens when a class is loaded or when its object is created?

**Answer**

Class Loading:
Class is loaded by the class loader.
Static variables are initialized.
Static blocks are executed.
Object Creation:
Memory is allocated for the object.
Instance variables are initialized to default values.
Instance variables are initialized.
Instance initializer blocks are executed.
Constructor is executed.
Method Execution:
Static methods can be called without creating an object.
Non-static methods are called on the created object.

## In java why does static block execute before the main method?

**Answer**

Class Loading:
The JVM loads the class containing the main method into memory.
Class Initialization:
Static variables are initialized.
Static blocks are executed in the order they appear in the class.
Execution of the main Method:
Once the class is fully initialized, the main method is called to start the execution of the program

## What is a sealed class?

**Answer**

A sealed class allows you to restrict which classes can extend or implement a given class or interface. This provides more control over the class hierarchy and helps in maintaining a more predictable and secure codebase.

## What is the static keyword?

**Answer**

Static Variables: Shared among all instances of the class.
Static Methods: Can be called without creating an instance of the class.
Static Blocks: Used for static initialization of the class.
Static Nested Classes:[Inner class] Nested classes that do not have access to instance variables and methods of the outer class.

## What is a static initializer block?

**Answer**

A static initializer block is used to initialize static variables or perform static initialization tasks. It is executed when the class is first loaded into memory, before any instances of the class are created and before any static methods are called.

## Can a static block throw an exception

**Answer**

Checked Exceptions:
A static block cannot throw checked exceptions directly.
Checked exceptions must be caught and handled within the static block.
Unchecked Exceptions:
A static block can throw unchecked exceptions (runtime exceptions) directly.
If an unchecked exception is thrown, it will cause the class initialization to fail with an ExceptionInInitializerError.

## Can we override static methods?

**Answer**

Static Methods Cannot Be Overridden: Static methods belong to the class, not to instances of the class. Therefore, they cannot be overridden in the same way that instance methods can.
Method Hiding: When a subclass defines a static method with the same name and parameters as a static method in its superclass, the method in the subclass hides the method in the superclass.
Binding: Method hiding uses static (compile-time) binding, while method overriding uses dynamic (runtime) binding.
Instance vs. Class: Overriding applies to instance methods, while hiding applies to static methods.

## Can we overload static methods?

**Answer**

Method Overloading:
Allows a class to have more than one method with the same name but different parameter lists.
Applies to both instance methods and static methods.
Overloading Static Methods:
You can overload static methods by defining multiple static methods with the same name but different parameter lists.

## Can we call a non-static method from a static method?

**Answer**

Static Methods: Belong to the class itself and can be called without creating an instance of the class.
Non-Static Methods: Belong to an instance of the class and can only be called on an instance of the class.
Non-Static Instance Variables: Belong to an instance of the class and can only be accessed through an instance of the class.
Accessing Non-Static Instance Variables from Static Methods: You can access non-static instance variables from a static method by creating an instance of the class and then accessing the variables through that instance.
Calling Non-Static Method from Static Method: You can call a non-static method from a static method by creating an instance of the class and then calling the non-static method on that instance.

## What is the benefit of static methods and variables?

**Answer**

Static Methods:
Utility Functions: Provide common functionality that does not depend on instance-specific data.
Memory Efficiency: Loaded into memory only once, regardless of the number of instances.
Ease of Access: Can be called directly using the class name without creating an instance.
Encapsulation of Common Behavior: Ensure consistent behavior across all instances.
Static Variables:
Shared State: Shared among all instances of a class, useful for storing common data.
Memory Efficiency: Loaded into memory only once, leading to efficient memory usage.
Global Access: Can be accessed directly using the class name.
Constants: Used to define constants that are shared across the application.

## What is an abstract keyword?

**Answer**

Abstract Class: A class that cannot be instantiated and may contain abstract methods. It serves as a blueprint for other classes.
Abstract Method: A method without a body that must be implemented by subclasses and must be defined inside an Abstract Class.
Inheritance: Abstract classes are meant to be extended by other classes, which must provide implementations for the abstract methods.

## What is Interface in Java?

**Answer**

Interface: is a reference type, similar to a class, that can contain only constants, method signatures, default methods, static methods, and nested types. Interfaces cannot contain instance fields or constructors. They are used to specify a set of methods that a class must implement, providing a way to achieve abstraction and multiple inheritance.
Abstract Methods: Methods without a body that must be implemented by classes.
Default Methods: Methods with a body that provide a default implementation.
Static Methods: Methods with a body that belong to the interface itself.
Constants: Public static final fields.
Multiple Inheritance: A class can implement multiple interfaces, allowing for multiple inheritance of type.
No Constructors: Interfaces cannot be instantiated directly.
In Java, all methods in an interface are implicitly public and abstract by default, except for default methods and static methods introduced in Java 8. This means you do not need to explicitly specify the public and abstract modifiers for methods in an interface.

## What is the difference between abstract class and an interface?

**Answer**

Abstract Class:
Purpose: Provides a common base class with shared code and abstract methods.
Methods: Can have both abstract and concrete methods.
Fields: Can have instance variables and static fields.
Multiple Inheritance: A class can extend only one abstract class.
Constructors: Can have constructors.
Access Modifiers: Methods can have any access modifier.
Use Case: Used to share common code and define a common base class.
Interface:
Purpose: Defines a contract that implementing classes must follow.
Methods: Can have abstract methods, default methods, and static methods.
Fields: Can only have static final fields (constants).
Multiple Inheritance: A class can implement multiple interfaces.
Constructors: Cannot have constructors.
Access Modifiers: Methods are implicitly public and abstract (unless default or static).
Use Case: Used to define capabilities that can be shared across multiple classes.

## What are different Types of Interface in Java?

**Answer**

Marker Interface: An interface with no methods or constants, used to mark or tag a class (e.g., Serializable).
Functional Interface: An interface with exactly one abstract method, used for lambda expressions and method references (e.g., Runnable).
Normal Interface: A typical interface with multiple abstract methods, default methods, static methods, and constants (e.g., Vehicle).
Nested Interface: An interface declared within another class or interface (e.g., OuterClass.InnerInterface).
Tagging Interface: Similar to a marker interface, used to tag classes with specific capabilities or properties (e.g., Cloneable).

## What is a Marker interface?

**Answer**

Marker interfaces in Java are interfaces that do not contain any methods or fields. They are used to "mark" or "tag" a class with a specific property or behavior. The presence of a marker interface can be checked at runtime using reflection, and it can influence the behavior of certain operations or frameworks. It is a simple yet powerful way to convey metadata about a class, enabling certain behaviors or properties to be associated with the class without requiring additional methods or fields. They are often used in conjunction with frameworks or libraries that perform specific actions based on the presence of these markers.

## How does Java distinguish between classes that implement a Marker interface and those who don't?

**Answer**

Distinguishing Classes: Java distinguishes between classes that implement a marker interface and those that don't using the instanceof operator and reflection.
Serialization Example: The Serializable marker interface is used to indicate that a class can be serialized. The serialization mechanism checks if a class implements Serializable before attempting to serialize it.
Checking for Marker Interface:
Using instanceof: Checks if an object is an instance of a class that implements the marker interface.
Using Reflection: Checks if a class implements the marker interface using reflection.

## What is reflection?

**Answer**

Reflection: A powerful feature in Java that allows a program to inspect and manipulate the runtime behavior of applications.
Inspect Classes, Interfaces, Fields, and Methods: Reflection allows you to inspect the structure of classes, interfaces, fields, and methods at runtime.
Instantiate Objects: You can create instances of classes dynamically at runtime.
Invoke Methods: You can invoke methods on objects dynamically at runtime.
Access and Modify Fields: You can access and modify the fields of objects dynamically at runtime.
Common Use Cases: Used in frameworks, serialization, dynamic proxies, and development tools

## What is the Java Reflection API?

**Answer**

Java Reflection API is a powerful feature in the Java programming language that allows programs to inspect and manipulate the runtime behavior of applications. It provides the ability to examine or modify the runtime behavior of applications by accessing information about classes, methods, fields, and constructors at runtime.
Class Inspection:
Class Object: Obtain the Class object associated with a class using methods like Class.forName(), ClassName.class, or object.getClass().
Class Information: Retrieve information about the class, such as its name, superclass, interfaces, and modifiers.
Field Manipulation:
Access Fields: Use the Field class to access and manipulate the fields of a class. You can retrieve field information, get and set field values, and modify field accessibility.
Method Invocation:
Access Methods: Use the Method class to access and invoke methods of a class. You can retrieve method information, invoke methods, and modify method accessibility.
Constructor Invocation:
Access Constructors: Use the Constructor class to access and invoke constructors of a class. You can retrieve constructor information, create new instances, and modify constructor accessibility.
Annotations:
Access Annotations: Use reflection to access annotations on classes, methods, fields, and constructors. You can retrieve annotation information and process it at runtime.

## What is *able interfaces?

**Answer**

In Java, "*able" interfaces are a common naming convention for interfaces that define a specific capability or behavior that a class can implement. These interfaces typically end with the suffix "-able" and indicate that the implementing class is capable of performing a certain action or possessing a certain property. Here are some common examples of "*able" interfaces in Java:
Serializable: Indicates that a class can be serialized.
Cloneable: Indicates that a class allows a field-for-field copy of instances.
Comparable: Defines a natural ordering for objects of a class.
Iterable: Indicates that a class can be iterated over.
Closeable: Indicates that a class can be closed to release resources.
Runnable: Indicates that a class can be executed by a thread.

## What are runnable vs callable interfaces?

**Answer**

The Runnable interface is a functional interface that represents a task that can be executed by a thread.
The Callable interface is a functional interface that represents a task that can be executed by a thread and returns a result.
Return Value:
Runnable: The run() method does not return a result.
Callable: The call() method returns a result of type V.
Checked Exceptions:
Runnable: The run() method cannot throw checked exceptions.
Callable: The call() method can throw checked exceptions.
Functional Interface:
Runnable: Since Java 8, Runnable is a functional interface and can be used with lambda expressions and method references.
Callable: Since Java 8, Callable is a functional interface and can be used with lambda expressions and method references.
Usage:
Runnable: Suitable for tasks that do not need to return a result or throw checked exceptions. Commonly used with Thread and ExecutorService.
Callable: Suitable for tasks that need to return a result or throw checked exceptions. Commonly used with ExecutorService and Future.

## Why can’t we create objects for abstract class?

**Answer**

Incomplete Implementation: Abstract classes may contain abstract methods without implementations, making them incomplete and unsuitable for instantiation.
Design Purpose: Abstract classes are designed to be extended by other classes and provide a common interface and shared code.
Polymorphism: Abstract classes are used to achieve polymorphism, allowing different subclasses to provide their own implementations of abstract methods.

## What are different types of Inheritance in Java?

**Answer**

Single Inheritance: One class inherits from one superclass.
Multilevel Inheritance: A class inherits from a class which is also inherited from another class.
Hierarchical Inheritance: Multiple classes inherit from a single superclass.
Multiple Inheritance (via Interfaces): A class implements multiple interfaces.

## What is Hybrid Inheritance?

**Answer**

Hybrid Inheritance: A combination of two or more types of inheritance (single, multiple, multilevel, hierarchical) to create a complex inheritance structure.
Java Support: Java does not support multiple inheritance directly but allows it through interfaces.
Example: Combining single inheritance, multilevel inheritance, hierarchical inheritance, and multiple inheritance via interfaces to form a hybrid inheritance structure.

## What is the Diamond Problem in Java?

**Answer**

The Diamond Problem is a common issue in multiple inheritance scenarios where a class inherits from two classes that have a common ancestor. This can lead to ambiguity and conflicts, particularly when the inherited classes have methods with the same signature.
Example:
Class A is the common ancestor.
Classes B and C inherit from A.
Class D inherits from both B and C.
If both B and C override a method from A, and D does not override it, it becomes ambiguous which version of the method D should inherit.
Java avoids the Diamond Problem by not supporting multiple inheritance with classes. Instead, Java uses interfaces to achieve multiple inheritance, which does not lead to the Diamond Problem because interfaces do not contain implementation details.

## What are the different types of constructors in Java?

**Answer**

Default Constructor: Automatically provided by the Java compiler if no other constructors are defined.
No-Argument Constructor: Explicitly defined constructor with no parameters.
Parameterized Constructor: Constructor with parameters to initialize the object with specific values.
Copy Constructor: Constructor to create a new object as a copy of an existing object.

## How does Java resolve the call to an overloaded method?

**Answer**

Exact Match:
The compiler first looks for a method with an exact match of the parameter types.
Example: example.display(10); matches display(int a).
Type Promotion:
The compiler looks for methods where the arguments can be promoted to match the parameter types.
Example: example.display(10); could match display(long a) if no exact match is found.
Autoboxing and Unboxing:
The compiler considers methods where primitive types can be converted to their corresponding wrapper classes and vice versa.
Example: example.display(10); could match display(Integer a) due to autoboxing.
Varargs:
The compiler looks for methods that accept variable-length arguments.
Example: example.display(1, 2, 3); matches display(int... a).
Ambiguity:
If multiple methods match the call and none is more specific, the compiler throws a compile-time error.
Example: example.display(10, 20); is ambiguous if both display(int, long) and display(long, int) exist.

## What are some different types of access modifiers in Java?

**Answer**

Public: Accessible from any other class.
Private: Accessible only within the declaring class.
Protected: Accessible within the same package and by subclasses.
Default (Package-Private): Accessible only within the same package.

## What is a package in Java?

**Answer**

Package: A namespace that organizes a set of related classes and interfaces.
Namespace Management: Packages provide a unique namespace for each group of classes and interfaces, helping to avoid naming conflicts.
Access Control: Packages allow you to control access to classes and interfaces using access modifiers.
Code Organization: Packages help to organize code in a logical and hierarchical manner, making it easier to manage and maintain large codebases.
Reusability: Packages promote code reusability by grouping related classes and interfaces together.
Creating a Package: Use the package keyword followed by the package name at the top of the source file.
Using a Package: Use the import statement to import classes and interfaces from a package.

## Can 2 Java packages have the same class name?

**Answer**

Packages:
Packages group related classes and avoid naming conflicts.
Classes in different packages can have the same name.
Fully Qualified Class Names:
The fully qualified class name includes the package name, ensuring unique identification.
Example: com.example.package1.MyClass and com.example.package2.MyClass.
Import Statements:
Import classes using their fully qualified names.
Use aliases to differentiate between classes with the same name from different packages.

## In a complex project, How would you structure your packages for maximum efficiency and maintainability?

**Answer**

Layered Architecture:
Organize packages based on different layers (e.g., presentation, service, repository, domain).
Group by Feature or Module:
Group packages by feature or module for larger projects.
Descriptive Package Names:
Use clear and descriptive package names.
Separate Configuration Classes:
Place configuration classes in a dedicated package.
Organize Utility Classes:
Place utility classes in a dedicated package.
Use Sub-Packages for Related Classes:
Use sub-packages to further organize related classes.
Hybrid Approach:
Combine package-by-layer and package-by-feature for complex projects.

## What is the difference between new() vs newInstance()

**Answer**

new Keyword
Purpose: Used to create a new instance of a class.
Syntax: ClassName obj = new ClassName();
Compile-Time: The class type must be known at compile time.
Constructor: Calls the constructor of the class directly.
Checked Exceptions: Does not throw checked exceptions.
Usage: Commonly used for creating objects in a straightforward manner.
newInstance Method
Purpose: Used to create a new instance of a class dynamically at runtime.
Syntax: Class<?> clazz = Class.forName("ClassName"); Object obj = clazz.newInstance();
Runtime: The class type can be determined at runtime.
Constructor: Calls the no-argument constructor of the class.
Checked Exceptions: Throws InstantiationException and IllegalAccessException.
Usage: Useful for reflection, dynamic class loading, and frameworks that need to create instances of classes dynamically.

## What are different ways to create object in java?

**Answer**

In Java, there are several ways to create an object:
- 1. Using the new keyword:
MyClass obj = new MyClass();
- 2. Using reflection:
MyClass obj = (MyClass) Class.forName("MyClass").newInstance();
- 3. Using the clone method:
MyClass obj1 = new MyClass();
MyClass obj2 = (MyClass) obj1.clone();
- 4. Using deserialization:
ObjectInputStream in = new ObjectInputStream(new FileInputStream("file.ser"));
MyClass obj = (MyClass) in.readObject();
- 5. Using factory methods:
MyClass obj = MyClassFactory.createInstance();
- 6. Using builder pattern:
MyClass obj = new MyClass.Builder().setProperty(value).build();

## What is Dynamic Method Dispatch in Java?

**Answer**

Dynamic Method Dispatch, also known as runtime polymorphism or late binding, is a mechanism in Java that allows a method to be overridden in a subclass and the appropriate method to be called at runtime based on the object's actual type. This is a key feature of object-oriented programming that enables flexibility and extensibility in code.

## What is super() and this()?

**Answer**

In Java, super() is a special keyword used to call the constructor of the superclass (parent class). It is used within a subclass constructor to initialize the state of the superclass. This ensures that the superclass is properly initialized before the subclass adds its own initialization.
Every constructor has super()
this() is a special keyword used to call another constructor within the same class. It is used for constructor chaining, allowing one constructor to invoke another constructor in the same class to avoid code duplication and to initialize the object in a consistent manner.

## What is a POJO class?

**Answer**

POJO stands for Plain Old Java Object. It is a simple Java class that follows certain conventions and is used to represent data. POJOs are used to encapsulate data and provide getter and setter methods to access and modify that data.
No Special Requirements: A POJO does not require any special inheritance or implementation of interfaces.
It is not bound by any specific framework or library.
Private Fields: Fields (variables) are typically private to encapsulate the data.
Public Getter and Setter Methods: Provides public methods to access and modify the private fields.
No-Argument Constructor: Often includes a no-argument constructor for easy instantiation.
No Annotations: Generally, POJOs do not use annotations, although they can if needed.

## What is Object Class?

**Answer**

In Java, the Object class is the root class of the Java class hierarchy. Every class in Java implicitly extends the Object class, either directly or indirectly. This means that all Java classes inherit the methods of the Object class.

## What is the superclass of Java classes and why is it designed as the super class of all classes?

**Answer**

Superclass of All Classes: The Object class is the superclass of all classes in Java.
Common Behavior: Provides common methods such as equals(), hashCode(), toString(), getClass(), clone(), notify(), notifyAll(), and wait().
Polymorphism: Allows for polymorphism, enabling a single variable of type Object to refer to any object.
Collections Framework: Supports the Java Collections Framework by allowing collections to store any type of object.
Reflection: Provides the getClass() method, which is essential for reflection

## What are some of the well known methods of Object class?

**Answer**

equals(Object obj): Determines whether two objects are equal.
hashCode(): Returns a hash code value for the object.
toString(): Returns a string representation of the object.
clone(): Creates and returns a copy (clone) of the object.
finalize(): Legacy finalization hook, deprecated for removal; do not use it for resource cleanup.
getClass(): Returns the runtime class of the object.
notify(): Wakes up a single thread waiting on the object's monitor.
notifyAll(): Wakes up all threads waiting on the object's monitor.
wait(): Causes the current thread to wait until another thread invokes notify() or notifyAll() on the object.

## Why is the notify method part of the Object class when it is related to multithreading and should belong to that class?

**Answer**

Intrinsic Locks:
Every object in Java has an intrinsic lock (or monitor) associated with it. This lock is used to synchronize methods or blocks of code.
The synchronized keyword can be applied to any object, making it possible to use any object as a lock.
Wait-Notify Mechanism:
The wait, notify, and notifyAll methods are used for inter-thread communication. They allow threads to wait for certain conditions to be met and to notify other threads when those conditions change.
These methods must be called on the object that is being used as the lock. Since any object can be used as a lock, these methods are defined in the Object class.
Unified Synchronization Model:
By placing wait, notify, and notifyAll in the Object class, Java provides a unified and consistent synchronization model.
This design ensures that any object can be used for synchronization and inter-thread communication, making the language more flexible and powerful.

## What is an Anonymous Object?

**Answer**

An anonymous object in Java is an object that is instantiated but not assigned to any reference variable. These objects are typically used when you need to perform an operation only once and do not need to reuse the object.

## What is Inner class?

**Answer**

Member Inner Class: Defined within another class and has access to the outer class's members.
Static Nested Class: Defined with the static keyword and does not have access to the instance members of the outer class.
Local Inner Class: Defined within a method or a block and can only be instantiated within that method or block.
Anonymous Inner Class: A class without a name, defined and instantiated in a single expression, often used to provide quick implementations of interfaces or abstract classes.

## What is anonymous class and their advantages?

**Answer**

Anonymous class in Java is a class that is defined and instantiated in a single expression, without explicitly declaring a class name. It is typically used to create instances of classes with slight modifications or to implement interfaces on the fly
Inline Definition: Define and instantiate a class in a single expression.
One-Time Use: Ideal for event listeners, callbacks, and other one-time use cases.
No Separate Class File: Reduces the number of files in the project.
Encapsulation: Keeps the scope of the class limited to where it is used.
Flexibility: Can extend existing classes or implement interfaces.

## Difference between anonymous class and lambda expression?

**Answer**

Syntax:
Anonymous Classes: Defined using the new keyword followed by the interface or class to be extended/implemented, and a class body.
Lambda Expressions: Have a concise syntax using the -> operator.
Verbosity:
Anonymous Classes: More verbose and require more boilerplate code.
Lambda Expressions: More concise and require less boilerplate code.
Usage:
Anonymous Classes: Can be used to implement interfaces with multiple methods or extend classes.
Lambda Expressions: Can only be used with functional interfaces (interfaces with a single abstract method).
Scope:
Anonymous Classes: Can define fields and methods within the anonymous class body.
Lambda Expressions: Cannot define fields or additional methods within the lambda expression body.
Type:
Anonymous Classes: Can be used with any interface or class.
Lambda Expressions: Limited to functional interfaces.

## What is Functional Interface?

**Answer**

Functional Interface: An interface with exactly one abstract method.
Lambda Expressions: Can be used to implement functional interfaces.
@FunctionalInterface Annotation: Optional annotation to indicate a functional interface and prevent accidental addition of abstract methods.
Built-in Functional Interfaces: Java provides several built-in functional interfaces in the java.util.function package, such as Function, Consumer, Supplier, and Predicate

## Can we have a default method implementation in functional interface?

**Answer**

Yes, in Java, you can have default method implementations in functional interfaces.

## Can Functional interface extend or implement another interface?

**Answer**

Extending Another Interface:
A functional interface can extend another interface, including another functional interface.
The functional interface must have exactly one abstract method in total, even after extending another interface.
The extended interface can have default methods, static methods, and abstract methods.
Implementing Another Interface:
While a functional interface can technically implement another interface, this is less common and not typically how interfaces are used in Java.

## Can we have a static method in a functional interface?

**Answer**

Yes, you can have static methods in both functional interfaces and regular interfaces in Java

## What are the advantages of Functional Interface?

**Answer**

Concise and Readable Code:
Lambda Expressions: Enable more concise and readable code by eliminating boilerplate code.
Improved Code Maintainability:
Less Boilerplate: Easier to maintain and understand due to reduced boilerplate code.
Enhanced Expressiveness:
Method References: Further enhance the expressiveness and readability of the code.
Functional Programming Paradigm:
Functional Programming: Enable functional programming in Java, allowing declarative style and higher-order functions.
Interoperability with Streams API:
Streams API: Enable powerful and expressive data processing operations.
Custom Functional Interfaces:
Custom Interfaces: Define your own functional interfaces for modular and reusable code.
Compatibility with Existing Libraries:
Backward Compatibility: Provide backward compatibility with existing libraries and frameworks.

## What are the different functional interface in Java?

**Answer**

Predicate: Represents a boolean-valued function of one argument.
Function: Represents a function that takes one argument and produces a result.
Consumer: Represents an operation that takes a single input argument and returns no result.
Supplier: Represents a supplier of results.
UnaryOperator: A specialization of Function for the same input and output type.
BinaryOperator: A specialization of BiFunction for the same input and output type.
BiFunction: Represents a function that takes two arguments and produces a result.
BiConsumer: Represents an operation that takes two input arguments and returns no result.
BiPredicate: Represents a boolean-valued function of two arguments.

## How functional interface and lambda expression is related to each other?

**Answer**

Target Type: A lambda expression can be used wherever a functional interface is expected. The functional interface serves as the target type for the lambda expression.
Implementation of Abstract Method: The lambda expression provides the implementation for the single abstract method defined in the functional interface.
Type Inference: The compiler can infer the types of the parameters of the lambda expression based on the context provided by the functional interface.
Simplifying Code: Lambda expressions simplify the code by eliminating the need for anonymous inner classes to implement functional interfaces.

## What is Comparator vs Comparable in Java?

**Answer**

Comparable: [Interface used with class]
Purpose: Defines the natural ordering of objects.
Method: int compareTo(T o)
Single Sorting Sequence: Only one sorting sequence can be defined.
Package: java.lang
Example: Sorting by a single attribute like id.
Comparator:
Purpose: Defines multiple sorting sequences.
Method: int compare(T o1, T o2)
Multiple Sorting Sequences: Multiple sorting sequences can be defined.
Package: java.util
Example: Sorting by different attributes like id and name.

## Why Comparable Interface is not Functional Interface?

**Answer**

Comparable Interface:
Technically a functional interface because it has a single abstract method (compareTo).
Not annotated with @FunctionalInterface because it is intended to be a trait of an object, indicating that the object can be compared to another object of the same type.
Using a lambda expression to implement Comparable is not practical.
Comparator Interface:
Annotated with @FunctionalInterface and designed to represent a comparison function.
Commonly used with lambda expressions and method references to define custom orderings.

## What is Consumer, forEach and Stream API?

**Answer**

Stream API:
Functional Programming: Provides a functional approach to processing sequences of elements.
Intermediate Operations: Return a new stream (e.g., filter, map).
Terminal Operations: Produce a result or a side-effect (e.g., forEach, collect).
Intermediate operations are defined and chained together, but they are not executed until a terminal operation is invoked.
Usage: stream().filter(...).map(...).collect(...)
forEach Method:
Iterable Interface: Used to iterate over elements in a collection and perform an action on each element.
Stream Interface: Used to perform actions on each element of a stream.
Usage: collection.forEach(action) or stream.forEach(action)
Consumer Interface:
Functional Interface: Represents an operation that takes a single input argument and returns no result.
Method: void accept(T t)
Usage: Commonly used in lambda expressions and method references.
Example:
Consumer<String> printName = name -> System.out.println("Name: " + name);

Predicate Interface: A functional interface that represents a single argument function returning a boolean value.
Method: boolean test(T t) evaluates the predicate on the given argument.
Default Methods: Includes methods for combining predicates (and, or, negate).
Usage: Commonly used in lambda expressions, method references, and with the Stream API for filtering and matching operations.
Example:
Predicate<Integer> isEven = number -> number % 2 == 0;
Supplier Interface: Represents a supplier of results. It does not take any arguments and returns a result of a specified type.
Method: T get() - Gets a result.
Default Methods: The Supplier interface does not have any default methods.
Usage: Commonly used in lambda expressions, method references, and with the Stream API for generating or providing values.
Example:
Supplier<Double> randomSupplier = () -> Math.random();
Function Interface: A functional interface that represents a function taking one argument and producing a result.
Method: R apply(T t) applies the function to the given argument and returns the result.
Default Methods: Includes methods for composing functions (andThen, compose).
Usage: Commonly used in lambda expressions, method references, and with the Stream API for mapping and transforming data.
Example:
Function<String, Integer> stringLengthFunction = str -> str.length();
Runnable Interface: A functional interface that represents a task that can be executed by a thread. It does not take any arguments and does not return a result.
Method: void run() - Executes the task.
Default Methods: The Runnable interface does not have any default methods.
Usage: Commonly used to define tasks that can be executed by threads, often in lambda expressions and method references.
Example:
Runnable task = () -> System.out.println("Task is running");
Comparator Interface: A functional interface that represents a comparison function, which imposes a total ordering on some collection of objects.
Method: int compare(T o1, T o2) - Compares its two arguments for order. Returns a negative integer, zero, or a positive integer as the first argument is less than, equal to, or greater than the second.
Default Methods: Includes methods for composing comparators (thenComparing, reversed).
Usage: Commonly used to define custom sorting orders for collections, often in lambda expressions and method references.
Example:
Comparator<String> stringLengthComparator = (str1, str2) -> Integer.compare(str1.length(), str2.length());

## You need to check if an invoice is overdue, updates status, print the invoice details and supply new invoice instances?

**Answer**

Check if an invoice is overdue:
Functional Interface: Predicate<Invoice>
Predicate<Invoice> isOverdue = inv -> inv.getDueDate().isBefore(LocalDate.now());
Update the status of an invoice:
Functional Interface: Consumer<Invoice>
Consumer<Invoice> updateStatus = inv -> inv.setStatus("Overdue");
Print the invoice details:
Functional Interface: Consumer<Invoice>
Consumer<Invoice> printInvoice = inv -> System.out.println(inv);
Supply new invoice instances:
Functional Interface: Supplier<Invoice>
Supplier<Invoice> invoiceSupplier = () -> new Invoice("INV001", 1500.0, "Pending", LocalDate.now().plusDays(30));

## What is GroupBy & PartitioningBy?

**Answer**

groupingBy:
Purpose: Groups elements based on a classification function.
Result: Returns a Map where keys are the result of the classification function, and values are lists of items that match the classification.
Example: Grouping names by their length.
partitioningBy:
Purpose: Partitions elements into two groups based on a predicate.
Result: Returns a Map with Boolean keys (true and false), where values are lists of items that match or do not match the predicate.
Example: Partitioning names by whether their length is greater than 3.

## What is faster Stream API or traditional loops?

**Answer**

Stream API:
Declarative Style: More readable and maintainable code.
Parallel Processing: Can leverage multiple CPU cores for improved performance in certain scenarios.
Overhead: Introduces some overhead due to higher abstraction and intermediate objects.
Traditional Loops:
Imperative Style: More control over the iteration process.
Performance: Can be more performant for simple operations on small data sets due to lower overhead.
Optimization: Easier for the compiler and runtime to optimize.
For simple operations on small data sets, traditional loops may be faster due to their lower overhead.
For large data sets and computationally intensive operations, the Stream API, especially with parallel processing, can offer significant performance improvements.
The choice between Stream API and traditional loops should consider factors such as code readability, maintainability, and specific performance requirements.

## What are Terminal operations?

**Answer**

Terminal Operations: Operations that produce a result or a side-effect and mark the end of the stream pipeline.
Common Terminal Operations:
forEach: Performs an action for each element.
collect: Collect elements into a collection or another data structure.
reduce: Reduces elements to a single value.
toArray: Returns an array containing the elements.
count: Returns the count of elements.
findFirst: Returns the first element as an Optional.
findAny: Returns any element as an Optional.
allMatch, anyMatch, noneMatch: Return boolean values based on predicate matching.

## What is the difference between flatmap() and a map()?

**Answer**

Transformation:
map(): Transforms each element of the stream into another element.
flatMap(): Transforms each element of the stream into a stream of new elements and then flattens the resulting streams into a single stream.
Mapping:
map(): One-to-One Mapping (each input element is transformed into exactly one output element).
flatMap(): One-to-Many Mapping (each input element is transformed into zero or more output elements).
Resulting Stream:
map(): The result is a stream of the same structure but with transformed elements.
flatMap(): The result is a single flattened stream containing all the elements of the individual streams.

## What is parallelStream?

**Answer**

ParallelStream: A method to create a parallel stream from a collection, enabling parallel processing of elements.
Parallel Processing: Utilizes multiple threads to process elements concurrently, potentially improving performance for large datasets or computationally intensive tasks.
Fork/Join Framework: Internally uses the Fork/Join framework to split tasks into smaller subtasks and execute them concurrently.
Considerations: Ensure thread safety, be aware of order and side effects, and evaluate performance benefits.

## What is the difference between == and equals() method?

**Answer**

== Operator:
Compares primitive data types by value.
Compares object references by memory location.
Example: s1 == s2 checks if s1 and s2 reference the same object.
`equals()` compares logical equality as defined by the class and can be overridden with custom
equality logic. For example, `s1.equals(s2)` compares string content rather than reference identity.

## How will you compare 2 instances of the same class?

**Answer**

Reference Equality (==): Checks if two references point to the same object.
Logical Equality (equals()): Checks if two objects are logically equivalent by comparing their contents. Override the equals() method for custom logic.
Custom Comparison (Comparable and Comparator): Provides custom comparison logic for sorting and ordering.

## What are equals() and hashCode() methods?

**Answer**

equals() Method:
Used to compare two objects for equality based on their content.
Must be overridden to provide a meaningful comparison.
Signature: public boolean equals(Object obj)
hashCode() Method:
Returns an integer hash code value for the object.
Must be overridden when equals() is overridden to maintain the general contract.
Signature: public int hashCode()
General Contract:
Equal objects must have equal hash codes.
Non-equal objects can have the same or different hash codes.
Hash code should remain consistent as long as the object's state does not change.

## In which scenarios is it necessary to override hashcode() and equals() method?

**Answer**

Using Objects as Keys in Hash-Based Collections:
Override hashCode() and equals() to ensure correct behavior in HashMap, HashSet, etc.
Ensuring Logical Equality:
Override equals() to compare objects based on their logical state.
Maintaining Consistency Between hashCode() and equals():
Ensure that equal objects have equal hash codes by overriding both methods.

## Which method gets executed first equals() or hashCode()? Does both of these always get executed?

**Answer**

hashCode() Method:
Typically called first to compute the hash code of an object.
Used to determine the bucket in which the object should be placed or searched for.
equals() Method:
Called if two objects have the same hash code and are placed in the same bucket.
Used to compare the actual content of the objects to ensure they are logically equivalent.
Execution Context:
Both methods are used in hash-based collections like HashMap, HashSet, and Hashtable.
The hashCode() method is called first, followed by the equals() method if necessary.

## What will happen if you override equals() method but not hashCode()?

**Answer**

Inconsistent Behavior: Overriding equals() without overriding hashCode() can lead to inconsistent behavior in hash-based collections.
Difficulty in Retrieval: Objects that are equal according to equals() may not be found in hash-based collections if they have different hash codes.
Violation of Contract: The general contract of hashCode() is violated, leading to logical inconsistencies.

## Why is it important to override hashcode() method if we override equals()? What would be the consequences if we don't?

**Answer**

General Contract:
If two objects are equal according to equals(), they must have the same hash code.
If two objects are not equal according to equals(), they can have the same or different hash codes.
Consequences of Not Overriding hashCode():
Violation of Contract: Leads to inconsistent behavior in hash-based collections.
Incorrect Behavior in Hash-Based Collections:
HashMap: Inability to retrieve objects using the same key.
HashSet: Duplicate elements may be added.
Correct Implementation:
Override both equals() and hashCode() to ensure consistent behavior.

## How will you make sure when 2 instances of the same class are compared, they must be equal?

**Answer**

To ensure that two instances of the same class are considered equal when compared, you need to override the equals() and hashCode() methods in your class. This allows you to define what it means for two instances to be logically equivalent.

## How would you handle the scenario where 2 objects in a hashmap have the same hashcode?

**Answer**

HashMap Collision Handling:
Uses chaining (linked lists or trees) to handle collisions.
Stores entries with the same hashcode in the same bucket.
Equality Check:
Uses the equals() method to find the exact match among entries with the same hashcode.

## What is Upcasting and Downcasting in Java?

**Answer**

Upcasting: Casting a subclass object to a superclass reference. It is safe and does not require an explicit cast.
Downcasting: Casting a superclass reference back to a subclass reference. It requires an explicit cast and can be unsafe if not checked properly.
instanceof Operator: Used to check if an object is an instance of a specific class before performing a downcast to avoid ClassCastException.

## What are covariant return types?

**Answer**

Covariant Return Types: Allow an overridden method in a subclass to return a type that is a subclass of the return type declared in the superclass method.
Type Safety: Maintains type safety by ensuring compatibility between the returned object and the expected type.
Flexibility and Specificity: Provides more flexibility and allows methods to return more specific types, enhancing code expressiveness and reducing the need for type casting.
Introduced in Java 5: This feature was introduced in Java 5.

## If a method that takes super class type as its parameter can it work with an object of it's subclass type?

**Answer**

Yes, a method that takes a superclass type as its parameter can work with objects of its subclass type. This is a fundamental concept in object-oriented programming known as polymorphism.

## What is a wrapper class?

**Answer**

Wrapper Classes: Object representations of primitive data types.
Utility Methods: Provide methods for type conversion, parsing, and more.
Autoboxing and Unboxing: Automatic conversion between primitives and wrapper classes.
Immutability: Wrapper class instances are immutable.

## Are there any performance issues with autoboxing?

**Answer**

Memory Overhead: Autoboxing creates additional objects, leading to increased memory usage.
Garbage Collection: Frequent autoboxing can put extra pressure on the garbage collector.
Boxing and Unboxing Overhead: Method calls and object creation introduce performance overhead.
Equality Comparison: Comparing boxed primitives using == can lead to subtle bugs.
Performance Impact in Collections: Using collections with boxed primitives can impact performance.

## What is Optional Class and how do we use it?

**Answer**

Optional Class:
A container object that may or may not contain a non-null value.
Helps to avoid NullPointerException and makes the code more expressive.
Creating Optional Instances:
Optional.empty(): Creates an empty Optional.
Optional.of(value): Creates an Optional with a non-null value.
Optional.ofNullable(value): Creates an Optional with a value that may be null.
Using Optional:
isPresent(), ifPresent(): Check if a value is present and execute actions.
orElse(), orElseGet(): Provide default values if the value is absent.
map(), flatMap(): Transform the value if present.
filter(): Conditionally return the value if it matches a predicate.

## What are ways to do null check in Java?

**Answer**

Simple Conditional Check: Use if (str != null) to check for null values.
Ternary Operator: Use (str != null) ? str.length() : 0 for concise null checks.
Objects Utility Class: Use Objects.nonNull(str) for null checks.
Optional Class: Use Optional.ofNullable(str) for more expressive null handling.
Apache Commons StringUtils: Use StringUtils.length(str) for null-safe string operations.
Guava's Optional: Use Optional.fromNullable(str) for null handling with Guava.
Assertions: Use assert str != null for debugging null checks.

## What are the benefits of Optional class?

**Answer**

Avoid NullPointerException:
Provides a clear and explicit way to handle the absence of a value, reducing the risk of NullPointerException.
Expressive Code:
Makes the code more readable and expressive by clearly indicating that a value may be present or absent.
Functional Programming Support:
Supports functional programming constructs like map, flatMap, filter, and ifPresent, enabling more concise and declarative code.
Encourages Better API Design:
Encourages better API design by explicitly indicating that a method may return an absent value, improving documentation and usability.
Eliminates Boilerplate Code:
Reduces boilerplate code for null checks and handling default values with methods like orElse, orElseGet, and orElseThrow.

## What is Annotation in Java?

**Answer**

Annotations: Provide metadata about the code without affecting its execution.
Built-in Annotations: Include @Override, @Deprecated, and @SuppressWarnings.
Custom Annotations: Can be defined using the @interface keyword and can include elements to store additional data.
Retention and Target: Control how long annotations are retained and where they can be applied.

## What is Custom Annotation?

**Answer**

Custom Annotations: Custom annotations allow you to add metadata to your code and can be defined using the @interface keyword.
Meta-Annotations: Use meta-annotations like @Retention and @Target to specify the retention policy and target for the custom annotation.
Applying Annotations: Apply custom annotations to program elements such as classes, methods, and fields.
Processing Annotations: Use reflection or annotation processing tools to process custom annotations at runtime or compile-time.

## What are exceptions in Java?

**Answer**

Exception: In Java, exceptions are represented by classes that are part of the java.lang.Throwable class hierarchy
Throwable: The superclass of all errors and exceptions.
Error: Represents serious problems that should not be caught by applications.
Exception: Represents conditions that applications might want to catch.
Checked Exception: Exceptions checked at compile-time (e.g., IOException).
Unchecked Exception: Exceptions not checked at compile-time (e.g., NullPointerException).
Types of Exceptions: Built-in exceptions and user-defined exceptions.
throw Keyword: Used to explicitly throw an exception.
throws Keyword: Used in method signatures to declare that a method can throw exceptions.

## What is Exception Hierarchy?

**Answer**

Throwable: The root class of the exception hierarchy.
Error: Represents serious problems that applications should not catch.
Exception: Represents conditions that applications might want to catch.
Checked Exceptions: Must be caught or declared in the method signature.
Unchecked Exceptions (Runtime Exceptions): Do not need to be caught or declared.

## What is the difference between exception and error.

**Answer**

Exception:
Definition: Represents conditions that a reasonable application might want to catch.
Types: Includes checked exceptions (e.g., IOException, SQLException) and unchecked exceptions (e.g., NullPointerException, IllegalArgumentException).
Handling: Can be caught and handled using try-catch blocks.
Usage: Used for conditions that an application might anticipate and recover from.
Error:
Definition: Represents serious problems that a reasonable application should not try to catch.
Types: Includes OutOfMemoryError, StackOverflowError, VirtualMachineError, etc.
Handling: Generally not caught by applications because they indicate serious problems with the runtime environment.
Usage: Used for conditions that are typically outside the control of the application and usually indicate a problem with the JVM or hardware.

## How does JVM handle exception?

**Answer**

Exception Occurrence The ArithmeticException occurs in method2() when attempting to divide by zero.
Exception Propagation: The JVM creates an ArithmeticException object and searches for an appropriate handler in method2(). Since there is no handler, the exception is propagated to method1().
Exception Handling: method1() also does not have a handler, so the exception is propagated to the main() method.
The main() method has a try-catch block that catches the ArithmeticException.
Handling the Exception: The catch block in the main() method handles the exception by printing a message to the console.
Compile-Time: The Java compiler checks for checked exceptions and ensures they are either caught or declared. This happens when the .class file is created.
Class Loading and Linking: The JVM performs bytecode verification and linking checks when the class is loaded.
Runtime: Exceptions are actually thrown and handled during the execution of the program. Unchecked exceptions are detected and handled at runtime.

## If a Java application encounters an out of memory error what does it mean?

**Answer**

OutOfMemoryError:
Indicates that the JVM has run out of memory and cannot allocate more memory for new objects or operations.
Common Causes:
Heap Space Exhaustion: Memory leaks, excessive object creation.
PermGen Space Exhaustion (Java 7 and earlier): Excessive class loading.
Metaspace Exhaustion (Java 8 and later): Excessive class loading.
Native Memory Exhaustion: Excessive thread creation, large direct byte buffers.
GC Overhead Limit Exceeded: Excessive time spent in garbage collection.
Diagnosing and Resolving:
Analyze Heap Dumps: Identify memory leaks and excessive memory usage.
Monitor Memory Usage: Track memory usage trends.
Optimize Memory Usage: Review and optimize memory usage patterns.
Increase Heap Size: Use -Xms and -Xmx options.
Tune Garbage Collection: Adjust GC settings.
Address Class Loading Issues: Review class loading patterns, increase PermGen/Metaspace size if needed.

## When does an IO Exception occur?

**Answer**

Common Causes of IOException:
File Not Found: Attempting to open a non-existent file.
Access Denied: Insufficient permissions to read/write a file or directory.
Disk Full: No space left on the disk to write data.
Network Issues: Connection timeouts, unreachable hosts, dropped connections.
Stream Closed: Reading from or writing to a closed stream.
Handling IOException:
Use try-catch blocks to handle IOException and provide meaningful error messages.
Ensure resources like files and streams are properly closed, preferably using try-with-resources for automatic resource management.

## How does try catch finally affect the performance of the program?

**Answer**

Normal Execution Path: The overhead of try, catch, and finally blocks is minimal when no exceptions are thrown.
Exception Handling Path: The performance impact is more significant when exceptions are thrown due to the overhead of creating exception objects, unwinding the call stack, and executing the catch block.
Impact of finally Block: The finally block adds a small amount of overhead, but it ensures that cleanup code is always executed.
Best Practices: Minimize exception usage, keep finally block code efficient, and use preconditions and validations to prevent exceptions.

## How will you handle it if the code can throw multiple types of exceptions?

**Answer**

Multiple Catch Blocks: Handle different types of exceptions separately.
Multi-Catch Block: Catch multiple exceptions in a single catch block (Java 7 and later).
Custom Exception Handling: Create custom exception classes for specific scenarios.
Finally Block: Execute code that must run regardless of whether an exception is thrown.
Rethrowing Exceptions: Catch an exception, perform some processing, and then rethrow it.

## How will you handle Array Index Out Of Bound Exception?

**Answer**

Try-Catch Block: Use a try-catch block to catch and handle the exception.
Check Array Length: Manually check the array length before accessing an index to ensure it is within bounds.
Enhanced For Loop: Use an enhanced for loop (for-each loop) to iterate over the array without worrying about indices.
Custom Method: Create a custom method to safely access array elements, returning a default value if the index is out of bounds.
Using Streams: Use Java Streams to process array elements safely without directly accessing indices.

## What is Exception Propagation?

**Answer**

Exception Propagation: The process by which an exception is passed up the call stack until it is caught by an appropriate exception handler or reaches the top of the call stack.
Throwing an Exception: An exception is thrown using the throw keyword, creating an exception object and transferring control to the nearest enclosing try-catch block.
Searching for a Catch Block: The Java runtime searches for a matching catch block in the current method. If none is found, the exception is propagated to the caller.
Propagating the Exception: The exception is propagated up the call stack until it is caught or reaches the top of the call stack.
Unhandled Exceptions: If the exception reaches the top of the call stack without being caught, the program terminates, and the exception is printed to the console.

## How will you create a runtime custom exception?

**Answer**

Extend RuntimeException: Create a new class that extends RuntimeException to define a custom runtime exception.
Define Constructors: Provide constructors to allow for different ways of instantiating the exception, including with custom error messages and causes.
Use the Custom Exception: Throw the custom exception in your code to handle specific error conditions and catch it where appropriate.

## What happens if an exception is thrown by the main thread?

**Answer**

Exception is Caught:
If the exception is caught within a try-catch block, the program can handle it gracefully and continue executing any remaining code.
Exception is Not Caught:
The exception propagates up the call stack, causing the main thread to terminate abruptly.
The JVM prints the stack trace of the uncaught exception to the standard error stream.
If no other non-daemon threads are running, the JVM terminates the entire application.
Handling Uncaught Exceptions:
You can set an UncaughtExceptionHandler to define custom behavior for uncaught exceptions in the main thread (or any thread).

## What is a try with resources?

**Answer**

The try-with-resources statement is a powerful feature that helps to manage resources efficiently and prevent resource leaks, making your code cleaner and more robust.
Automatic Resource Management: Resources are automatically closed at the end of the try block.
Implements AutoCloseable: Resources must implement the AutoCloseable interface.
Simplifies Code: Reduces boilerplate code and makes the code more readable and maintainable.
Multiple Resources: Can manage multiple resources in a single try-with-resources statement.
Custom Resources: Can be used with custom classes that implement AutoCloseable.

## In which scenarios do you need to create an Custom Exception?

**Answer**

Domain-Specific Errors:
Represent specific error conditions unique to your application's domain.
Example: ProductNotFoundException
More Descriptive Error Messages:
Provide more descriptive and meaningful error messages.
Example: InvalidUserInputException
Wrapping Lower-Level Exceptions:
Wrap lower-level exceptions with higher-level exceptions that are more meaningful.
Example: DatabaseException
Enforcing Business Rules:
Enforce specific business rules and constraints.
Example: InsufficientFundsException
Improving Code Readability and Maintainability:
Use specific exception types to improve code readability and maintainability.
Example: ConfigurationException
Providing Additional Context:
Provide additional context or information about the error condition.
Example: ValidationException
Customizing Exception Handling:
Customize exception handling and provide specific responses or actions.
Example: ResourceConflictException

## What is the difference between syntax and sematic errors?

**Answer**

Syntax Errors:
Definition: Violations of the grammatical rules of the programming language.
Detection: Detected by the compiler or interpreter at compile time.
Impact: Prevent the code from being executed.
Examples: Missing semicolons, incorrect indentation, unmatched parentheses.
Semantic Errors:
Definition: Errors in the logic or meaning of the program.
Detection: Often detected at runtime.
Impact: Cause the program to produce incorrect or unintended results.
Examples: Incorrect use of operators, using uninitialized variables, logical errors in loops.

## In what cases will it finally not be called?

**Answer**

JVM Termination: If the JVM is terminated using System.exit() or crashes, the finally block will not be executed.
Thread Interruption: If the thread executing the try or catch block is forcibly stopped using deprecated methods like Thread.stop(), the finally block may not be executed.
Infinite Loop or Long-Running Operation: If the try or catch block contains an infinite loop or a long-running operation that never completes, the finally block will not be executed.
Power Failure or Hardware Issues: If there is a power failure or hardware issue that causes the JVM to terminate abruptly, the finally block will not be executed.

## What is System.exit and in what situations will you use it?

**Answer**

System.exit(int status): Terminates the JVM and exits the program with the specified status code.
Situations to Use:
Command-line applications to indicate normal or abnormal termination.
Error handling for critical errors that prevent the program from continuing.
Testing and debugging to observe program behavior.
Shutdown hooks to perform cleanup tasks before termination.
Caution: Use System.exit with care, as it terminates the JVM abruptly and may prevent proper cleanup of resources and impact other running threads.

## What happens internally when system.exit is called?

**Answer**

System.exit(int status):
Terminates the JVM with the specified status code.
A non-zero status code indicates abnormal termination, while zero indicates normal termination.
Internal Process:
Security Manager Check:
Calls the security manager's checkExit method.
Throws SecurityException if the exit is denied.
Shutdown Hooks:
Runs all registered shutdown hooks.
Shutdown hooks are registered using Runtime.addShutdownHook(Thread hook).
Finalization:
Runs all finalizers that have not yet been executed.
Termination:
Terminates the JVM and returns the status code to the operating system.

## Tell a bit about mutex, semaphores, threads, processes, and program

**Answer**

Mutex (Mutual Exclusion): Ensures that only one thread can access a resource at a time, preventing race conditions.
Semaphores: Controls access to a shared resource through a counter, allowing a specified number of threads to access the resource simultaneously.
Threads: The smallest unit of execution within a process, sharing the same memory space but executing independently.
Process is an instance of a program that is being executed. Each process has its own memory space. A program in execution.
Program is a sequence of instructions and data  that a CPU needs to accomplish a specific task. It is simply an executable file.

## What are different ways to create a Thread?

**Answer**

Extending the Thread Class: Create a new thread by extending the Thread class and overriding the run() method.
Implementing the Runnable Interface: Create a new thread by implementing the Runnable interface and passing an instance to a Thread object.
Using the Callable Interface and FutureTask: Create a new thread using the Callable interface, which can return a result and throw a checked exception, and manage it with FutureTask.
Using the ExecutorService Framework: Use the ExecutorService framework to manage a pool of threads and their lifecycle.

## In which scenarios you will see concurrent modification exception?

**Answer**

Single-Threaded Iteration with Modification: Occurs when a collection is modified during iteration without using the iterator's methods.
Solution: Use the iterator's remove method to modify the collection during iteration.
Multi-Threaded Access: Occurs when a collection is accessed and modified concurrently by multiple threads without proper synchronization.
Solution: Use synchronized collections or concurrent collections to ensure thread-safe access.

## Explain Multithreading and Asynchronous Programming.

**Answer**

Multithreading A form of concurrency that involves running multiple threads simultaneously on a multi-core processor. Multithreading is good for parallelizing CPU-bound tasks and managing user interfaces. However, managing multithreaded applications can be complex because of issues like deadlocks, race conditions, and the need for synchronization.
Asynchronous programming is a programming paradigm that allows a unit of work to run separately from the main application thread. When the work is complete, it notifies the main thread about its completion or failure. This approach is often used to handle I/O-bound operations, such as network requests, file I/O, or database queries, without blocking the main thread.
Multitasking is the ability of an operating system or a computing environment to execute multiple tasks or processes simultaneously. It allows a computer to perform several operations at the same time, improving efficiency and resource utilization. Multitasking can be achieved through various techniques, including time-sharing, parallel processing, and concurrency.
Preemptive Multitasking the operating system controls the allocation of CPU time to various tasks. The OS can interrupt a running task to allocate CPU time to another task, ensuring that all tasks get a fair share of the CPU.
Cooperative Multitasking: each task is responsible for yielding control to other tasks. If a task does not yield control, it can monopolize the CPU, leading to poor system responsiveness.
Multiprocessing: involves the use of two or more CPUs within a single computer system. Each CPU can execute its own process independently, allowing true parallel execution of tasks.

## What is the synchronized keyword?

**Answer**

synchronized keyword in Java is used to control access to a block of code or an object by multiple threads. It ensures that only one thread can execute a synchronized block or method at a time, which helps in achieving thread safety by preventing concurrent access to shared resources.
Synchronized Methods: Can be instance methods or static methods. Instance methods lock the object, while static methods lock the class object.
Synchronized Blocks: Allow more fine-grained control over synchronization by synchronizing only a portion of a method.

## What are some of the lock-less mechanisms?

**Answer**

Atomic Variables:
Lock-free, thread-safe operations on single variables.
Examples: AtomicInteger, AtomicLong, AtomicBoolean, AtomicReference.
Concurrent Collections:
Thread-safe collections without explicit synchronization.
Examples: ConcurrentHashMap, ConcurrentLinkedQueue, ConcurrentSkipListMap, CopyOnWriteArrayList.
Compare-And-Swap (CAS):
Atomic instruction for synchronization without locking.
Read-Write Locks:
Allow concurrent reads and exclusive writes.
Example: ReentrantReadWriteLock.
StampedLock:
Flexible and efficient alternative to ReentrantReadWriteLock.
Provides writing, reading, and optimistic reading modes.

## What is ReentrantLock?

**Answer**

ReentrantLock: A flexible and powerful alternative to the synchronized keyword for thread synchronization.
Reentrant: Allows a thread to re-acquire the lock it already holds.
Explicit Locking: Requires explicit calls to lock() and unlock().
Fairness: Can be configured to be fair, ensuring the longest-waiting thread acquires the lock first.
Condition Variables: Supports multiple condition variables for complex thread coordination.

## What are mutations?

**Answer**

Mutations: Changes or modifications made to the state of an object or data structure

When multiple threads mutate shared state without a correct happens-before relationship, a race can
make the outcome depend on execution timing. Avoid shared mutable state where possible; otherwise
use the appropriate lock, atomic type, concurrent collection, immutability, or message-passing model.

## What are different Thread states?

**Answer**

NEW: The thread is created but not yet started. When a thread is created using the new keyword.
RUNNABLE: The thread is ready to run and waiting for CPU time. When the start() method is called,
BLOCKED: The thread is blocked waiting for a monitor lock. When a thread tries to enter a synchronized block or method but another thread holds the lock
WAITING: The thread is waiting indefinitely for another thread to perform a particular action. When a thread calls Object.wait(), Thread.join(), or LockSupport.park()
TIMED_WAITING: The thread is waiting for another thread to perform a particular action for a specified waiting time. When a thread calls Thread.sleep(), Object.wait(long), Thread.join(long), or LockSupport.parkNanos()/parkUntil().
TERMINATED: The thread has completed its execution. When the run() method or call() method completes.

## What happens when thread.start() method is called on a method more than once?

**Answer**

First Call to start():
Transitions the thread from the "new" state to the "runnable" state.
The run() method is invoked in a new thread of execution.
Subsequent Calls to start():
Throws an IllegalThreadStateException.
A thread can only be started once. Once it has completed execution, it cannot be restarted.
Best Practices
Create a New Thread Object: If you need to run the same task again, create a new instance of the Thread class or implement the Runnable interface and create a new Thread object.
Use ExecutorService: For managing a pool of threads and reusing them, consider using the ExecutorService framework provided by the java.util.concurrent package.

## Suppose you are working on a high performance Financial Trading Application that frequently updates prices and sorts them. Which Java Collection is best suited for this scenario?

**Answer**

ConcurrentSkipListMap
Sorted Order: Maintains elements in a sorted order based on keys.
Concurrency: Thread-safe collection allowing concurrent access and updates.
Performance: Efficient O(log n) time complexity for insertion, deletion, and access operations.
NavigableMap Interface: Provides additional methods for navigation and range queries.

## What is the difference between fail safe and fail fast collection?

**Answer**

Fail-Fast Collections:
Behavior: Throw ConcurrentModificationException if modified during iteration.
Detection: Use a modification count (modCount) to detect concurrent modifications.
Examples: ArrayList, HashMap, HashSet, LinkedList.
Fail-Safe Collections:
Behavior: Do not throw ConcurrentModificationException if modified during iteration.
Detection: Operate on a snapshot of the collection's data.
Examples: CopyOnWriteArrayList, CopyOnWriteArraySet, ConcurrentHashMap.

## Suppose you are developing an application that allows multiple users to modify a shared list of tasks concurrently. In this scenario what causes Concurrent Modification Exception and what can you do to prevent this?

**Answer**

Causes of ConcurrentModificationException:
Modifying the list during iteration by another thread.
Preventing ConcurrentModificationException:
Synchronized Collections: Use Collections.synchronizedList() to synchronize access.
Concurrent Collections: Use CopyOnWriteArrayList for concurrent access and modifications.
Explicit Synchronization: Manually synchronize access using synchronized blocks or locks.

## What are some of the locking mechanisms?

**Answer**

Synchronized: Ensures that only one thread can execute a block or method at a time.
ReentrantLock: Provides explicit locking with more flexibility than synchronized.
Semaphore: Controls access to a resource by multiple threads through permits.
CountDownLatch: Allows threads to wait until a set of operations completes.
Phaser: Provides a flexible synchronization barrier for coordinating phases of tasks.

## Does Java support multithreading by default? If so, is it Synchronous or Asynchronous?

**Answer**

Java Supports Multithreading: Java has built-in support for multithreading through the Thread class, Runnable interface, and Executors framework.
Synchronous Execution: Tasks are executed one after another in a sequential manner.
Asynchronous Execution: Tasks can be executed concurrently, allowing multiple tasks to run in parallel.
Java's multithreading capabilities are inherently asynchronous, allowing threads to run concurrently and independently. Synchronization mechanisms are available to coordinate access to shared resources when needed.

## Why is implementing Runnable better than extending Thread for Multithreading?

**Answer**

Separation of Concerns:
Runnable: Separates the task from the thread execution mechanism.
Thread: Combines the task with the thread execution mechanism.
Reusability:
Runnable: The same Runnable instance can be reused by multiple threads.
Thread: Each instance is tightly coupled to a specific thread.
Flexibility:
Runnable: Allows the class to extend another class if needed.
Thread: Limits the class to extend only Thread.
Decoupling:
Runnable: Decouples the task from thread management.
Thread: Couples the task with thread management.
Thread Pool Compatibility:
Runnable: Easily used with thread pools and executor services.
Thread: Not compatible with thread pools.

## How Multithreading improves Application performance and what are some challenges in it?

**Answer**

Multithreading Improves Application Performance:
Parallelism: Multithreading allows multiple threads to run concurrently, making better use of multi-core processors and improving performance for CPU-bound tasks.
Responsiveness: By offloading long-running tasks to separate threads, the main thread can remain responsive to user interactions, enhancing the user experience.
Resource Utilization: Multithreading can improve resource utilization by allowing threads to perform I/O operations while other threads continue processing, reducing idle time.
Throughput: By processing multiple tasks simultaneously, multithreading can increase the overall throughput of the application.
Challenges in Multithreading:
Synchronization Issues: Ensuring that shared resources are accessed in a thread-safe manner can be complex and error-prone, leading to issues like race conditions, deadlocks, and data corruption.
Deadlocks: Deadlocks occur when two or more threads are waiting indefinitely for each other to release resources, causing the application to hang.
Race Conditions: Race conditions happen when the outcome of a program depends on the timing of thread execution, leading to unpredictable and incorrect results.
Complexity: Writing, debugging, and maintaining multithreaded code is more complex than single-threaded code, increasing the risk of bugs and errors.
Context Switching Overhead: Frequent context switching between threads can introduce overhead, reducing the performance gains from multithreading.
Resource Contention: Multiple threads competing for the same resources (e.g., CPU, memory, I/O) can lead to contention, reducing the efficiency of the application.
Memory Consistency Errors: Ensuring that changes made by one thread are visible to other threads can be challenging, leading to memory consistency errors.
Testing and Debugging: Multithreaded applications are harder to test and debug due to non-deterministic behavior and timing issues.

## What are Thread Leakages?

**Answer**

Thread Leakage:
Occurs when threads are created but not properly managed, leading to inactive or "leaked" threads that consume system resources.
Causes:
Unfinished threads due to unhandled exceptions, infinite loops, or blocking operations.
Improper thread pool management.
Resource leaks.
Blocking operations.
Consequences:
Resource exhaustion.
Increased latency.
Unpredictable behavior.
Prevention and Detection:
Proper thread management and termination.
Use thread pools and properly shut them down.
Use timeouts and handle interruptions.
Monitor and profile threads using tools like VisualVM, JConsole, and Java Mission Control.

## How would you make sure the update to a field of object is safe in a Multi Threaded Environment?

**Answer**

Synchronized Methods or Blocks:
Use synchronized keyword to ensure mutual exclusion.
Example: public synchronized void increment() { count++; }
Atomic Variables:
Use atomic variables from java.util.concurrent.atomic package.
Example: private AtomicInteger count = new AtomicInteger(0);
volatile Keyword:
Use volatile to ensure visibility of updates.
Example: private volatile int count = 0;
java.util.concurrent Locks:
Use explicit locks from java.util.concurrent.locks package.
Example: private final Lock lock = new ReentrantLock();
java.util.concurrent Collections:
Use thread-safe collections from java.util.concurrent package.
Example: private ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
java.util.concurrent Utilities:
Use higher-level concurrency utilities from java.util.concurrent package.
Example: ExecutorService, CountDownLatch, CyclicBarrier, Semaphore.

## What are different ways to make code Thread Safe?

**Answer**

Synchronized Methods/Blocks: Use the synchronized keyword to control access to critical sections of code.
Volatile Keyword: Use the volatile keyword to ensure visibility of changes to variables across threads.
Atomic Variables: Use classes from the java.util.concurrent.atomic package for atomic operations.
Locks: Use explicit locks provided by java.util.concurrent.locks.Lock.
Concurrent Collections: Use thread-safe collections from the java.util.concurrent package.
ThreadLocal Variables: Use ThreadLocal to ensure that each thread has its own instance of a variable.
Immutable Objects: Design objects to be immutable so that their state cannot be changed after creation.
Using Executors: Use the ExecutorService to manage and control thread execution.

## Can you explain synchronization for thread safety?

**Answer**

Synchronization:
Ensures that multiple threads can access shared resources in a controlled manner, preventing data inconsistency and ensuring thread safety.
Synchronized Methods:
Only one thread can execute a synchronized method at a time for a given object.
Synchronized Blocks:
Allows more fine-grained control over synchronization by locking only a specific section of code.
Intrinsic Locks (Monitors):
Every object in Java has an intrinsic lock. When a thread enters a synchronized method or block, it acquires the lock. When it exits, it releases the lock.
Reentrant Locks:
Java's intrinsic locks are reentrant, meaning that if a thread already holds the lock, it can re-enter the synchronized method or block without blocking itself.

## What is the difference between synchronized vs Reentrant Locks

**Answer**

Synchronized Block
Basic Concept: A synchronized block is a built-in mechanism in Java for achieving thread synchronization.
Syntax: Uses the synchronized keyword.
Locking: Implicitly acquires and releases the lock on the specified object.
Reentrancy: Supports reentrant locking, allowing a thread to re-enter a synchronized block it already holds the lock for.
Fairness: Does not provide fairness options; threads acquire locks in an unspecified order.
Condition Variables: Limited to using wait(), notify(), and notifyAll() for thread communication.
Performance: Simpler and generally faster for basic synchronization needs.
ReentrantLock
Basic Concept: A ReentrantLock is a class in java.util.concurrent.locks package that provides more advanced locking mechanisms.
Syntax: Uses the ReentrantLock class.
Locking: Explicitly acquires and releases the lock using lock() and unlock() methods.
Reentrancy: Supports reentrant locking, similar to synchronized blocks.
Fairness: Can be configured for fairness, ensuring threads acquire locks in the order they requested them.
Condition Variables: Provides multiple Condition objects for more flexible thread communication.
Performance: More flexible and powerful, but slightly more complex and may have a performance overhead for simple use cases.

## What are the different methods used in multithreading?

**Answer**

Locking and Unlocking
synchronized (object): Acquires the intrinsic lock on the specified object.
ReentrantLock.lock(): Acquires the lock, blocking if necessary until it is available.
ReentrantLock.unlock(): Releases the lock.
Waiting and Notification
Object.wait(): Causes the current thread to wait until another thread invokes notify() or notifyAll() on the same object.
Object.notify(): Wakes up a single thread that is waiting on the object's monitor.
Object.notifyAll(): Wakes up all threads that are waiting on the object's monitor.
Condition Variables (ReentrantLock)
Condition.await(): Causes the current thread to wait until it is signaled or interrupted.
Condition.signal(): Wakes up one waiting thread.
Condition.signalAll(): Wakes up all waiting threads.
Thread Management
Thread.start(): Begins execution of a new thread.
Thread.join(): Waits for the thread to die.
Thread.sleep(milliseconds): Causes the current thread to sleep for the specified number of milliseconds.
Thread.yield(): Hints to the scheduler that the current thread is willing to yield its current use of a processor.
Atomic Operations
AtomicInteger.incrementAndGet(): Atomically increments the current value by one and returns the updated value.
AtomicInteger.compareAndSet(expectedValue, newValue): Atomically sets the value to the given updated value if the current value equals the expected value.
Executors and Thread Pools
Executors.newFixedThreadPool(n): Creates a thread pool that reuses a fixed number of threads.
ExecutorService.submit(task): Submits a task for execution and returns a Future representing the task.
ExecutorService.shutdown(): Initiates an orderly shutdown in which previously submitted tasks are executed, but no new tasks will be accepted.
Summary

## Can a deadlock occur with a single thread?

**Answer**

Deadlock:
A situation where two or more threads are blocked forever, each waiting for the other to release a resource.
Requires multiple threads and the following conditions: mutual exclusion, hold and wait, no preemption, and circular wait.
Example of Deadlock with Multiple Threads:
Code:
Single Thread:
A single thread cannot create a deadlock because it does not have another thread to wait for.
Deadlock requires at least two threads to create a circular wait condition.

## What is the difference between volatile and Atomic variables?

**Answer**

Visibility:
Both volatile and atomic variables ensure visibility of changes across threads.
Atomicity:
volatile provides atomicity only for individual read/write operations.
Atomic variables provide atomicity for compound actions (e.g., incrementing, updating).
Usage:
Use volatile for simple flags and state variables where only individual read/write operations are needed.
Use atomic variables for counters, sequence numbers, and other variables where atomic operations are required.

## What are generics in Java?

**Answer**

Generics:
Allow you to define classes, interfaces, and methods with type parameters.
Provide compile-time type safety and eliminate the need for casting.
Generic Class: public class Box<T>
Generic Methods: public static <T> void printArray(T[] array)
Bounded Type Parameters: public static <T extends Number> void printNumber(T number)
Restrict the types that can be used as type parameters.
Wildcards: public static void printList(List<?> list)
Represent an unknown type.

## Tell a bit about collection API, Collection and Collections?

**Answer**

Collection API: A unified architecture for representing and manipulating collections in Java. It includes interfaces, implementations, and algorithms.
Collection Interface: The root interface of the Collection Framework, representing a group of objects. It is extended by other interfaces like List, Set, and Queue.
Collections Class: A utility class that provides static methods to operate on or return collections. It includes methods for sorting, searching, reversing,
and more.

## What is the difference between Arrays.sort() & Collection.sort()?

**Answer**

Data Structures:
Arrays.sort(): Used for sorting arrays.
Collections.sort(): Used for sorting lists.
Method Signatures:
Arrays.sort():
For primitive types: public static void sort(int[] a), public static void sort(char[] a), etc.
For objects: public static <T extends Comparable<? super T>> void sort(T[] a), public static <T> void sort(T[] a, Comparator<? super T> c).
Collections.sort():
For lists: public static <T extends Comparable<? super T>> void sort(List<T> list), public static <T> void sort(List<T> list, Comparator<? super T> c).
Performance:
Arrays.sort(): Uses dual-pivot Quicksort for primitive types and a modified mergesort for objects.
Collections.sort(): Internally uses Arrays.sort() on the backing array of the list, with similar performance characteristics.

## Can you tell me about the internal implementation of ArrayList & LinkedList?

**Answer**

ArrayList:
Underlying Data Structure: Dynamically resizable array.
Capacity and Size: Capacity is the size of the underlying array; size is the number of elements stored.
Growth Policy: Increases capacity by 1.5 times when needed.
Random Access: O(1) time complexity.
Insertion/Deletion: O(1) at the end, O(n) at arbitrary positions.
LinkedList:
Underlying Data Structure: Doubly linked list.
Nodes: Each node contains references to the previous and next nodes and the element itself.
Sequential Access: O(n) time complexity for random access.
Insertion/Deletion: O(1) at arbitrary positions if the position is known.

## What is the difference between Array and ArrayList?

**Answer**

Size:
Array: Fixed size. Once created, the size cannot be changed.
ArrayList: Dynamic size. Can grow and shrink as needed.
Type:
Array: Can hold both primitive types and objects.
ArrayList: Can only hold objects (no primitive types directly).
Performance:
Array: Generally faster for fixed-size collections due to less overhead.
ArrayList: Slightly slower due to dynamic resizing and additional methods.
Flexibility:
Array: Less flexible, requires manual resizing and copying.
ArrayList: More flexible, provides built-in methods for resizing, adding, and removing elements.
Syntax:
Array: int[] arr = new int[10];
ArrayList: ArrayList<Integer> list = new ArrayList<>();
Methods:
Array: Limited to basic operations (length, indexing).
ArrayList: Rich set of methods (add, remove, get, size, etc.).

## What are the performance differences when using Arrays.sort() on primitive types and objects?

**Answer**

Primitive Types:
Algorithm: Dual-Pivot Quicksort
Time Complexity: O(n log n) on average, O(n^2) in the worst case (rare)
Space Complexity: O(log n)
Performance: Highly efficient for large datasets, low memory overhead
Objects:
Algorithm: Timsort (hybrid of Merge Sort and Insertion Sort)
Time Complexity: O(n log n) in both average and worst cases
Space Complexity: O(n)
Performance: Stable sorting, optimized for real-world data, consistent performance

## Which collection will you use for no duplicates and insertion order is maintained?

**Answer**

Collection: LinkedHashSet
No Duplicates: Ensures that no duplicate elements are allowed.
Insertion Order: Maintains the order in which elements are inserted.
Performance: Provides constant-time performance for basic operations like add, remove, and contains.

## Which collection will you use if you want elements to be sorted?

**Answer**

TreeSet:
Description: Implements NavigableSet and stores elements in a sorted order.
Key Characteristics: No duplicates, O(log n) time complexity for basic operations.
TreeMap:
Description: Implements NavigableMap and stores key-value pairs in a sorted order based on the keys.
Key Characteristics: No duplicate keys, O(log n) time complexity for basic operations.
PriorityQueue:
Description: Implements Queue and orders elements based on their natural ordering or by a specified Comparator.
Key Characteristics: Allows duplicates, O(log n) time complexity for insertion, O(1) for access to the minimum or maximum element.

## How does TreeSet maintain sort order?

**Answer**

Underlying Data Structure:
TreeSet is backed by a TreeMap, which is implemented as a Red-Black tree.
Natural Ordering and Comparators:
Natural Ordering: Uses the natural ordering of elements (elements must implement Comparable).
Custom Comparator: Allows for a custom sort order by providing a Comparator.
Insertion:
Elements are added in the correct position to maintain the sorted order.
The Red-Black tree rebalances if necessary.
Balancing:
The Red-Black tree ensures balance by maintaining the longest path from the root to a leaf to be no more than twice as long as the shortest path.
Achieved through rotations and color changes during insertions and deletions.
Lookup:
Efficient lookup by traversing the tree from the root to the leaf, following the binary search property.

## Tell me any use cases of TreeMap?

**Answer**

Use Case: Implementing a Leaderboard
Consider a scenario where you need to implement a leaderboard for a game. The leaderboard should maintain the scores of players in sorted order, allowing you to quickly retrieve the top players and their scores.

## Does TreeSet allow null values? Why and Why not?

**Answer**

TreeSet Does Not Allow null Values:
Underlying Data Structure: TreeSet is implemented using a TreeMap, which is a Red-Black Tree.
Comparison Requirement: TreeSet relies on comparisons to maintain sorted order. null cannot be compared with other elements, leading to NullPointerException.
Consistency with TreeMap: Since TreeMap does not allow null keys, TreeSet also does not allow null values to maintain consistency.

## What are cursors in Java?

**Answer**

In Java, the term "cursor" generally refers to an object that allows traversal over the elements of a collection. Cursors are used to iterate through the elements of a collection, such as a list, set, or map. The most common types of cursors in Java are Iterator, ListIterator, and Enumeration.
Iterator:
Purpose: Forward traversal of a collection.
Methods: hasNext(), next(), remove().
Example: Iterating through a list.
ListIterator:
Purpose: Bidirectional traversal of a list.
Methods: Inherits from Iterator, plus hasPrevious(), previous(), add(E e), set(E e).
Example: Iterating forward and backward through a list.
Enumeration:
Purpose: Legacy interface for traversing collections like Vector and Hashtable.
Methods: hasMoreElements(), nextElement().
Example: Iterating through a Vector.

## What are the different types of iterators in Java?

**Answer**

Iterator:
Purpose: Forward traversal of a collection.
Methods: hasNext(), next(), remove().
Applicable Collections: All collections implementing Collection.
ListIterator:
Purpose: Bidirectional traversal of a list.
Methods: Inherits from Iterator, plus hasPrevious(), previous(), nextIndex(), previousIndex(), set(E e), add(E e).
Applicable Collections: Lists.
Enumeration:
Purpose: Legacy interface for traversing collections.
Methods: hasMoreElements(), nextElement().
Applicable Collections: Legacy collections like Vector and Hashtable.
Spliterator:
Purpose: Designed for parallel processing and partitioning elements.
Methods: tryAdvance(Consumer<? super T> action), trySplit(), estimateSize(), characteristics().
Applicable Collections: All collections implementing Collection.

## What is the difference between Iterator and ListIterator?

**Answer**

Supported Collections:
Iterator: Can be used with any collection that implements the Collection interface.
ListIterator: Can be used only with lists.
Traversal Direction:
Iterator: Supports only forward traversal.
ListIterator: Supports both forward and backward traversal.
Methods:
Iterator: hasNext(), next(), remove().
ListIterator: hasNext(), next(), hasPrevious(), previous(), nextIndex(), previousIndex(), remove(), set(E e), add(E e).
Capabilities:
Iterator: Does not support bidirectional traversal or adding elements during iteration. Can remove elements during iteration.
ListIterator: Supports bidirectional traversal, adding elements, removing elements, and replacing elements during iteration.

## In what situations will you prefer a ListIterator over Iterator?

**Answer**

Bidirectional Traversal: Use ListIterator when you need to traverse the list in both forward and backward directions.
Modifying the List During Iteration: Use ListIterator when you need to add, remove, or replace elements in the list while iterating.
Accessing Index Information: Use ListIterator when you need to know the index of the elements while iterating.
Navigating Subsections of a List: Use ListIterator when you need to navigate and manipulate specific subsections of a list.

## How does a Hashmap internally work?

**Answer**

Hashing: Converts a key into an integer value (hash code) to determine the index in the bucket array.
Buckets: Array elements that store linked lists (or trees) of entries with the same hash code.
Entries: Key-value pairs stored in the HashMap, each containing a reference to the next entry in the same bucket.
Collision Handling: Uses separate chaining (linked lists) and tree-based structures (in Java 8 and later) to handle collisions.
Initialization: Initializes an array of buckets with a default capacity and load factor.
Adding an Entry: Calculates the hash code, determines the bucket index, and adds the entry to the bucket.
Retrieving an Entry: Calculates the hash code, determines the bucket index, and retrieves the entry from the bucket.
Resizing: Doubles the capacity and rehashes all entries when the load factor threshold is exceeded.

## What is Load Factor in HashMap?

**Answer**

Load Factor: A measure that determines when to resize the HashMap. The default load factor is 0.75.
Default Initial Capacity: The initial number of buckets in the HashMap. The default initial capacity is 16.
Resizing: When the number of entries exceeds the product of the load factor and the current capacity, the HashMap is resized to maintain performance.

## What would happened if I reduce the value of load factor

**Answer**

Increased Space Usage:
A lower load factor means that the HashMap will have more empty slots, leading to increased memory usage.
For example, if you set the load factor to 0.5, the HashMap will resize when it is half full, resulting in more frequent resizing and more empty slots.
Reduced Collisions:
With a lower load factor, the HashMap will have fewer entries per bucket, reducing the likelihood of collisions.
This can improve the performance of get, put, and remove operations, as there will be fewer entries to search through in each bucket.
More Frequent Resizing:
A lower load factor will cause the HashMap to resize more frequently, as it will reach its threshold more quickly.
Resizing involves rehashing all the entries, which is a time-consuming operation. Frequent resizing can degrade performance, especially if the HashMap is large.
Improved Lookup Performance:
With fewer collisions, the average time complexity for get, put, and remove operations can approach O(1) more closely.
This can lead to improved performance for applications with high read/write operations.

## Explain the internal working of hashmap.

**Answer**

Hashing: Converts keys into hash codes to index into an array.
Buckets: Array of linked lists or trees to store key-value pairs.
Collision Handling: Uses separate chaining and treeification to handle collisions.
Insertion: Calculates hash, determines index, and inserts the node.
Retrieval: Calculates hash, determines index, and searches for the node.
Deletion: Calculates hash, determines index, and removes the node.
Resizing: Doubles the array size and rehashes entries when the load factor is exceeded.

## Write HashCode for Employee Class?

**Answer**

@Override
    public int hashCode() {
        return Objects.hash(id, name, department, salary);
    }

## What is the difference between treemap and hashmap?

**Answer**

Ordering:
TreeMap: Maintains sorted order of keys.
HashMap: No order of entries.
Performance:
TreeMap: O(log n) for get, put, remove operations.
HashMap: O(1) average for get, put, remove operations (O(n) in worst case).
Null Keys:
TreeMap: Does not allow null keys.
HashMap: Allows one null key.
Use Case:
TreeMap: Suitable for scenarios where sorted order of keys is required.
HashMap: Suitable for scenarios where fast access and insertion are required, and ordering is not important.

## What is the return Type of put method?

**Answer**

The put method is commonly used in Java's Map interface to insert a key-value pair into the map.
The return type of the put method is V, which represents the type of the values stored in the map.
Return Type:
V: The previous value associated with the key, or null if there was no mapping for the key.

## What was the enhancement done in Hashmap in Java 8

**Answer**

Improved Collision Handling with Balanced Trees:
Linked lists are converted to red-black trees when the number of entries in a bucket exceeds a threshold (default is 8).
This improves the worst-case time complexity for operations from O(n) to O(log n).
Threshold for Treeification:
Treeify Threshold: The threshold at which a bucket's linked list is converted to a red-black tree (default is 8).
Untreeify Threshold: The threshold at which a bucket's red-black tree is converted back to a linked list when the number of entries decreases (default is 6).
Improved Hash Function:
An improved hash function provides better distribution of keys across the hash table, reducing the likelihood of hash collisions.
Performance Improvements:
The combination of these enhancements results in significant performance improvements for HashMap operations, especially in scenarios with a high number of hash collisions.

## What is a synchronized Hashmap?

**Answer**

Synchronized HashMap: A thread-safe version of HashMap that ensures safe concurrent access by synchronizing method calls.
Creation: Use Collections.synchronizedMap() to create a synchronized map backed by a HashMap.
Synchronized Blocks for Iteration: Synchronize on the map when iterating to prevent concurrent modification exceptions.
Performance Overhead: Synchronization introduces performance overhead. For high-concurrency scenarios, consider using ConcurrentHashMap.
ConcurrentHashMap: An alternative to Synchronized HashMap that provides better performance through finer-grained locking and concurrency optimizations.

## What is the difference between Synchronized HashMap and ConcurrentHashMap?

**Answer**

ConcurrentHashMap
Concurrency: Allows concurrent read and write operations without locking the entire map.
Locking Mechanism: Uses a finer-grained locking mechanism (lock striping) to lock only portions of the map.
Performance: Higher performance in multi-threaded environments due to reduced contention.
Null Values: Does not allow null keys or values.
Use Case: Suitable for high-concurrency scenarios where multiple threads frequently read and write to the map.
Synchronized HashMap
Concurrency: Allows only one thread to access the map at a time by locking the entire map.
Locking Mechanism: Uses a single lock for the entire map, leading to higher contention.
Performance: Lower performance in multi-threaded environments due to the single lock.
Null Values: Allows null keys and values.
Use Case: Suitable for low-concurrency scenarios where thread safety is required but high performance is not critical.

## What is concurrentHashMap and HashTable?

**Answer**

Hashtable is a legacy class from the original Java 1.0 release that provides thread-safe operations by synchronizing all its methods. This means that only one thread can access the map at a time, ensuring thread safety but leading to significant contention and poor performance in highly concurrent environments. Due to its coarse-grained locking mechanism, Hashtable is generally suitable for single-threaded or lightly multi-threaded applications where the overhead of synchronization is minimal.
In contrast, ConcurrentHashMap, introduced in Java 5 as part of the java.util.concurrent package, is designed for high concurrency. It achieves thread safety through fine-grained locking, also known as lock striping, which allows multiple threads to read and write to different segments of the map concurrently. This reduces contention and improves performance in multi-threaded applications. ConcurrentHashMap is the preferred choice for modern applications that require efficient and scalable concurrent access to a map, making it ideal for environments where multiple threads frequently interact with the map.

## What is the difference between Hashmap vs ConcurrentHashMap?

**Answer**

HashMap
Thread Safety: HashMap is not thread-safe. Concurrent access by multiple threads without external synchronization can lead to unpredictable behavior.
Performance: Generally offers better performance in single-threaded scenarios because it does not have the overhead of synchronization.
Null Values: Allows one null key and multiple null values.
Internal Structure: Uses an array of linked lists (buckets) to store entries. In Java 8 and later, it uses a balanced tree (red-black tree) for buckets with a high collision rate to improve performance.
Use Case: Suitable for single-threaded scenarios or when external synchronization is used to manage concurrent access.
ConcurrentHashMap
Thread Safety: ConcurrentHashMap is thread-safe and designed for concurrent access. It allows multiple threads to read and write without external synchronization.
Performance: Optimized for concurrent access and provides better performance in multi-threaded scenarios compared to synchronizing a HashMap. Uses segment locking and non-blocking algorithms to minimize contention.
Null Values: Does not allow null keys or values. Attempting to insert a null key or value will result in a NullPointerException.
Internal Structure: Uses a more complex internal structure with segments and fine-grained locking to allow concurrent access. In Java 8 and later, it uses a combination of CAS (Compare-And-Swap) operations and synchronized blocks to achieve thread safety.
Use Case: Suitable for multi-threaded scenarios requiring concurrent access without the need for external synchronization

## What is the difference between identity hashmap and weak hashmap?

**Answer**

Comparison Method:
IdentityHashMap: Uses reference equality (==) to compare keys.
WeakHashMap: Uses object equality (equals()) to compare keys.
Garbage Collection:
IdentityHashMap: Keys and values are strongly referenced and not affected by garbage collection.
WeakHashMap: Keys are weakly referenced and can be garbage collected, leading to automatic removal of entries.
Use Cases:
IdentityHashMap: Suitable when you need to distinguish between different instances of the same object and use reference able equality for key comparison.
WeakHashMap: Suitable when you want to manage memory more efficiently by allowing keys to be garbage collected and automatically removing entries with keys that are no longer in use.

## What would happen if 2 threads tried to update the same key in a ConcurrentHashMap?

**Answer**

Thread-Safe Updates: ConcurrentHashMap ensures thread-safe updates using fine-grained locking and non-blocking algorithms.
Atomic Operations: Methods like compute, putIfAbsent, and merge provide atomic operations for safe updates.
Example Scenario: When two threads try to update the same key, ConcurrentHashMap ensures that the updates are performed safely and atomically.

## Why should we use immutable objects as keys in Hashmap?

**Answer**

Consistency of hashCode() and equals(): Immutable objects ensure that the hash code and equality comparisons remain consistent, preventing issues with key lookups in HashMap.
Thread Safety: Immutable objects are inherently thread-safe, eliminating the need for synchronization when accessing keys in a multi-threaded environment.
Reliable Behavior: Using immutable objects as keys ensures predictable and reliable behavior in hash-based collections.

## How does the performance of a Hashmap change when Hash Collision increases and what can be done to handle it?

**Answer**

Performance Impact: Increased hash collisions can degrade the performance of a HashMap by increasing the time complexity of search, insert, and delete operations.
Handling Collisions:
Separate Chaining: Uses linked lists or trees to handle collisions within buckets.
Treeify Bins: Converts linked lists to balanced trees when the number of entries in a bucket exceeds a threshold.
Resizing: Increases the number of buckets and rehashes entries when the load factor exceeds a threshold.
Best Practices:
Use a good hash function.
Choose an appropriate initial capacity.
Monitor and adjust the load factor.
Use immutable keys.
By following these best practic

## What is a record class?

**Answer**

Record Class: A special kind of class introduced in Java 14 (preview) and Java 16 (standard) for creating immutable data carriers.
Concise Syntax: Provides a concise way to declare classes that primarily store data.
Immutable: Fields are final and cannot be changed after object creation.
Automatic Generation: The compiler automatically generates the constructor, equals(), hashCode(), and toString() methods.
Components: Fields of a record are called components.

## What is a canonical constructor?

**Answer**

Canonical Constructor: A constructor automatically generated for record classes that initializes all the fields (components) of the record.
Automatic Generation: The compiler generates the canonical constructor based on the components of the record.
Parameter Correspondence: The parameters of the canonical constructor correspond to the components of the record.
Customization: You can define your own canonical constructor to add validation or other logic.

## What are enums and what are their benefits?

**Answer**

Enums (short for enumerations) in Java are a special type of class that represents a fixed set of constants. Enums are used to define collections of constants that can be used to represent a specific set of values in a type-safe manner.
Type Safety: Enums ensure that only valid values can be assigned to variables of the enum type, reducing the risk of errors.
Readability and Maintainability: Enums provide meaningful names for a set of related constants, making the code easier to understand and maintain.
Namespace Management: Enums provide a namespace for constants, preventing naming conflicts.
Built-in Methods: Enums come with built-in methods like values(), valueOf(), name(), and ordinal().
Switch Statement Compatibility: Enums can be used in switch statements for easier case handling.
Custom Methods and Fields: Enums can have custom methods and fields, adding additional functionality and behavior.
Singleton Pattern: Enums can be used to implement the Singleton pattern effectively.

## What is jagged array?

**Answer**

A jagged array, also known as an "array of arrays," is an array whose elements are themselves arrays, and these inner arrays can have different lengths. This is in contrast to a multidimensional array, where each dimension must have the same length.

## Can you tell a bit about pass by value and pass by reference?

**Answer**

Pass by Value:
Definition: The function receives a copy of the argument's value.
Behavior in Java: Java uses pass by value for both primitive types and object references. For objects, the reference itself is passed by value.
Example: Modifying a primitive type within a method does not affect the original value. Modifying an object's state within a method affects the original object.
Pass by Reference:
Definition: The function receives a reference to the actual data, allowing it to modify the original argument.
Behavior in Other Languages: Some languages support pass by reference, allowing functions to modify the original data directly.
Example: In C++, passing a reference to a function allows the function to modify the original value.

## Can we use pointers in Java?

**Answer**

No Pointers in Java: Java does not support pointers to enhance safety, security, and platform independence.
References: Java uses references to objects instead of pointers, providing a safer way to access and manipulate objects.
Memory Management: Java's automatic garbage collection abstracts away the need for manual memory management.
Alternatives: Java provides arrays, collections, and pass-by-value semantics to achieve similar functionality to pointers in a safer manner.

## What are Memory Leaks and Heap Dumps?

**Answer**

Memory Leaks:
Definition: Occurs when a program allocates memory but fails to release it, leading to increased memory usage and potential crashes.
Causes: Unreleased resources, static references, listener and callback references, collections, inner classes.
Example: Adding objects to a list and not removing them.
Heap Dumps:
Definition: A snapshot of the memory of a Java process at a specific point in time, containing information about all objects in the heap.
Uses: Diagnosing memory leaks, analyzing memory usage, performance tuning.
Generating: Using JVM options, JVisualVM, or jcmd.
Analyzing: Using tools like Eclipse MAT, JVisualVM, or YourKit to identify memory issues and optimize memory usage

## What are some common things that cause Memory leaks in Java?

**Answer**

Unclosed Resources:
Failing to close resources like file streams, database connections, and network sockets.
Solution: Use try-with-resources.
Static Fields:
Holding references to objects in static fields.
Solution: Avoid using static fields for large collections of objects.
Inner Classes and Anonymous Classes:
Non-static inner classes and anonymous classes holding references to their enclosing instance.
Solution: Use static inner classes if possible.
Listeners and Callbacks:
Registering listeners or callbacks without unregistering them.
Solution: Properly unregister listeners and callbacks.
Caching:
Caching objects without proper eviction policies.
Solution: Use caching libraries with built-in eviction policies.
ThreadLocal Variables:
Not cleaning up ThreadLocal variables.
Solution: Ensure ThreadLocal variables are removed when no longer needed.
Large Collections:
Holding references to large collections that grow indefinitely.
Solution: Use weak references or implement proper cleanup mechanisms.

## Can Polymorphism lead to memory issues? If so then in what scenario?

**Answer**

Polymorphism: Polymorphism itself does not inherently cause memory issues, but certain scenarios involving polymorphic behavior can lead to memory-related problems.
Memory Leaks: Improper resource management in polymorphic objects can lead to memory leaks.
Object Retention: Polymorphic references can cause unintended object retention, leading to high memory usage.
Excessive Object Creation: Polymorphic behavior can lead to excessive object creation if not managed properly.
Best Practices: Proper resource management, avoiding unnecessary object retention, using weak references, monitoring memory usage, and implementing resource cleanup can help prevent memory issues related to polymorphism.

## What are different ways to detect memory leaks in Java?

**Answer**

Profilers: Tools like VisualVM, YourKit, and JProfiler provide real-time monitoring and heap dump analysis.
GC Logs: Enable and analyze garbage collection logs using tools like GCViewer and GCEasy.
Heap Dumps: Generate and analyze heap dumps using tools like Eclipse MAT.
Code Analysis Tools: Use static code analysis tools like FindBugs/SpotBugs and SonarQube to detect potential memory leaks.
Custom Monitoring: Implement custom monitoring using WeakReference and MemoryMXBean to track memory usage programmatically.

## Explain a bit on terms related to Memory Profiling?

**Answer**

Eden Space is part of the young generation in generational collectors, and most new objects are
allocated there. When allocation pressure triggers a young collection, live objects may be copied
to survivor regions or promoted depending on the collector and object age.

Survivor Space:
Also part of the Young Generation.
Consists of two areas: S0 (Survivor 0) and S1 (Survivor 1).
Objects that survive a minor GC in the Eden Space are moved to one of the Survivor Spaces.
Objects are copied between S0 and S1 during subsequent GCs until they are promoted to the Old Generation.
Heap:
The runtime data area from which memory for all class instances and arrays is allocated.
Divided into Young Generation (Eden Space and Survivor Spaces) and Old Generation (Tenured Space).
Managed by the Java Virtual Machine (JVM) and subject to garbage collection.
Heap Dump:
A snapshot of the heap memory at a given point in time.
Contains information about all the objects in memory, including their classes, fields, and references.
Useful for diagnosing memory leaks and analyzing memory usage.
Memory Profiling:
JProfiler provides tools to analyze memory usage, track object allocations, and monitor garbage collection.
Helps identify memory leaks, excessive memory consumption, and inefficient object creation patterns.
Using JProfiler:
Heap Walker: Explore the heap dump to see objects, their sizes, and references.
Allocation Call Tree: Identify where objects are being allocated in the code.
Garbage Collection Monitoring: Monitor GC activity and its impact on application performance.

## Explain a bit about JProfiler?

**Answer**

JProfiler is a comprehensive Java profiling tool developed by ej-technologies. It is designed to help developers analyze and optimize the performance of their Java applications. Here are the key points:
Key Features:
CPU Profiling: Identifies methods consuming the most CPU time.
Memory Profiling: Detects memory leaks and optimizes memory usage through heap dumps and object allocation tracking.
Thread Profiling: Monitors thread activity, states, contention, and lifecycles.
Heap Walker: Provides detailed views of objects in the heap, including references and sizes.
Call Graphs: Visualizes the call hierarchy and time spent in each method.
SQL and NoSQL Profiling: Profiles database interactions and optimizes database performance.
Remote Profiling: Profiles applications running on remote servers.
IDE Integration: Integrates with popular IDEs like IntelliJ IDEA, Eclipse, and NetBeans.
Usage:
Installation: Download and install from the official website.
Attaching to JVM: Attach to a running JVM or start a new profiling session.
Analyzing Data: Use various views and tools to analyze CPU, memory, and thread data.
Generating Reports: Create detailed reports for further analysis and documentation.
Example Use Case:
CPU Profiling: Optimize methods with high CPU usage.
Memory Profiling: Detects and fixes memory leaks.
Thread Profiling: Resolve thread contention and deadlocks.

## What are the strategies you will use to fix Memory Leaks in your application

**Answer**

Use Profiling Tools:
VisualVM, YourKit, JProfiler, Eclipse MAT.
Analyze Heap Dumps:
Generate and analyze heap dumps to identify memory leaks.
Identify and Fix Common Memory Leak Patterns:
Unclosed resources: Use try-with-resources.
Static references: Avoid holding references in static fields.
Listener and callback registrations: Deregister listeners and callbacks.
Inner classes: Use static inner classes.
Optimize Data Structures:
Use appropriate data structures.
Clear collections when no longer needed.
Monitor and Tune Garbage Collection:
Monitor GC logs and tune GC parameters.
Use Weak References:
Use WeakReference, SoftReference, or PhantomReference.
Review and Refactor Code:
Conduct code reviews and refactor code to improve memory management.

## What is Marshalling and unmarshalling?

**Answer**

Marshalling:
Definition: Converting an object or data structure into a format that can be easily stored or transmitted.
Purpose: Prepare data for transmission over a network or for storage.
Example: Converting a Java object into XML or JSON.
Unmarshalling:
Definition: Converting the marshalled data back into an object or data structure.
Purpose: Reconstruct the original object or data structure from the transmitted or stored data.
Example: Converting XML or JSON back into a Java object.

## What is the transient keyword in java?

**Answer**

transient Keyword:
Used to indicate that a field should not be serialized.
Prevents sensitive, temporary, or irrelevant data from being included in the serialized representation of an object.
Usage:
Place the transient keyword before the field declaration.
During deserialization, the transient field will be initialized to its default value.

## How do you do serialization in Java?

**Answer**

Serializable Interface: Implement the Serializable interface to make a class serializable.
ObjectOutputStream: Used to write serialized objects to an output stream.
ObjectInputStream: Used to read serialized objects from an input stream.
serialVersionUID: A unique identifier for each class, used to ensure compatibility during deserialization.

## What is Serialization in Java and what are Serialization Attacks?

**Answer**

Serialization:
The process of converting an object's state into a byte stream.
Used for saving objects to files, sending over networks, or storing in databases.
Deserialization:
The reverse process of converting a byte stream back into an object.
Serialization Attacks:
Exploit vulnerabilities in the deserialization process.

**Can lead to remote code execution, denial of service, or data manipulation.**

Mitigation Strategies:
Avoid deserializing untrusted data.
Use secure deserialization libraries.
Implement custom readObject methods for validation.
Use ObjectInputFilter to filter deserialized objects.

## What challenges are faced when Serialization and Deserialization?

**Answer**

Versioning and Compatibility: Manage changes to the class structure to ensure compatibility.
Security Risks: Avoid deserializing untrusted data and use secure deserialization practices.
Performance Overhead: Optimize the serialization format and use efficient libraries.
Handling Transient and Static Fields: Ensure proper initialization and handling of transient and static fields.
Object Identity and Cyclic References: Use frameworks that support object identity and cyclic references.
Serialization of Complex Object Graphs: Use robust serialization libraries and implement custom logic if needed.
Platform and Language Independence: Use platform-independent serialization formats and ensure consistent logic across platforms.

## What are different cloning types in Java?

**Answer**

Shallow Cloning:
Definition: Copies the object and its primitive fields, but not the objects referenced by the fields.
Implementation: Implement Cloneable and override clone() method.
Use Case: Suitable for objects with only primitive fields or immutable objects.
Example: Changes to the cloned object's referenced objects affect the original object's referenced objects.
Deep Cloning:
Definition: Copies the object and recursively copies all objects referenced by the fields.
Implementation: Implement Cloneable, override clone() method, and manually clone referenced objects.
Use Case: Suitable for objects with references to mutable objects.
Example: Changes to the cloned object's referenced objects do not affect the original object's referenced objects.

## What is the Difference Between Statement and PreparedStatement in Java?

**Answer**

Statement
Purpose: Used to execute simple SQL queries without parameters.
Syntax: SQL queries are passed directly as strings.
Performance: Generally slower for repeated execution because the SQL query is parsed and compiled each time it is executed.
Security: More vulnerable to SQL injection attacks because user input is directly concatenated into the SQL query.
Usage: Suitable for executing static SQL queries that do not require parameters.
PreparedStatement
Purpose: Used to execute precompiled SQL queries with or without parameters.
Syntax: SQL queries are precompiled and parameters are set using setter methods.
Performance: Generally faster for repeated execution because the SQL query is parsed and compiled only once, and then executed multiple times with different parameters.
Security: More secure against SQL injection attacks because user input is passed as parameters, not concatenated into the SQL query.
Usage: Suitable for executing dynamic SQL queries that require parameters.

## How would you combine multiple completable futures into a single completable future?

**Answer**

Combining with allOf:
Combines multiple CompletableFuture instances into a single CompletableFuture that completes when all of them complete.

**Does not return the results of the individual futures.**

Combining with anyOf:
Combines multiple CompletableFuture instances into a single CompletableFuture that completes when any one of them completes.
Returns the result of the first completed future.
Combining with thenCombine:
Combines two CompletableFuture instances and applies a function to their results.
Returns a new CompletableFuture that is completed with the result of the function.

## How do you perform unit testing in Java?

**Answer**

Set Up Your Project: Add JUnit dependencies to your project using Maven or Gradle.
Create a Test Class: Create a test class in the src/test/java directory.
Write Test Methods: Write test methods annotated with @Test to test specific functionalities.
Run the Tests: Use your IDE, Maven, or Gradle to run the tests.
Analyze the Results: Ensure all tests pass and fix any issues if tests fail.
Versions: JUnit 4, JUnit 5 (JUnit Jupiter):

## What are some of the important annotation you use for JUnit testing

**Answer**

JUnit 5 Annotations:
@Test: Marks a method as a test method.
@BeforeEach: Executed before each test method.
@AfterEach: Executed after each test method.
@BeforeAll: Executed once before all test methods.
@AfterAll: Executed once after all test methods.
@DisplayName: Provides a custom display name.
@Disabled: Disables a test method or class.
@Tag: Assigns a tag for filtering tests.
@Nested: Denotes a nested test class.
@ParameterizedTest: Indicates a parameterized test.
@ValueSource: Provides values for a parameterized test.
@CsvSource: Provides CSV values for a parameterized test.
JUnit 4 Annotations:
@Test: Marks a method as a test method.
@Before: Executed before each test method.
@After: Executed after each test method.
@BeforeClass: Executed once before all test methods.
@AfterClass: Executed once after all test methods.
@Ignore: Disables a test method or class.
@Category: Assigns a category for filtering tests.

## How will you write test cases for an async method?

**Answer**

Use CompletableFuture or Future: If your async method returns a CompletableFuture or Future, use its methods to wait for the result.
Use CountDownLatch or Awaitility: If your async method does not return a CompletableFuture or Future, use CountDownLatch or Awaitility to wait for the async operation to complete.
Mock Dependencies: Use Mockito to mock dependencies and control their behavior during the test.
Verify Results: Verify the results of the async operation using assertion

## Create a list of Employees object from a hashmap whose key is string id and value is an basicinfo object

**Answer**

```java
Map<String, BasicInfo> basicInfoMap = new HashMap<>();
basicInfoMap.put("E001", new BasicInfo("Alice", 70000, "HR"));
basicInfoMap.put("E002", new BasicInfo("Bob", 85000, "Engineering"));
basicInfoMap.put("E003", new BasicInfo("Charlie", 60000, "Marketing"));
List<Employee> employees = new ArrayList<>();
for (Map.Entry<String, BasicInfo> entry : basicInfoMap.entrySet()) {
    String id = entry.getKey();
    BasicInfo basicInfo = entry.getValue();
    Employee employee = new Employee(id, basicInfo.getName(), basicInfo.getSalary(), basicInfo.getDepartment());
    employees.add(employee);
}
employees.forEach(System.out::println);
```

## How to find the highest salary employee?

**Answer**

```java
Optional<Employee> maxSalaryEmployee = employees.stream()
    .max((e1, e2) -> Double.compare(e1.getSalary(), e2.getSalary()));
maxSalaryEmployee.ifPresent(employee ->
    System.out.println("Employee with the highest salary: " + employee.getName())
);
```

## Create a map object from a list of salesperson object, the key of map is city and value is the count of employees in that city the map should be sorted by key in ascending order

**Answer**

```java
List<Salesperson> salespeople = Arrays.asList(
        new Salesperson("Alice", "New York"),
        new Salesperson("Bob", "Los Angeles"),
        new Salesperson("Charlie", "New York"),
        new Salesperson("David", "Chicago"),
        new Salesperson("Eve", "Los Angeles")
);
Map<String, Long> cityCountMap = salespeople.stream()
        .collect(Collectors.groupingBy(Salesperson::getCity, Collectors.counting()))
        .entrySet().stream()
        .sorted(Map.Entry.comparingByKey())
        .collect(Collectors.toMap(
                Map.Entry::getKey,
                Map.Entry::getValue,
                (oldValue, newValue) -> oldValue, LinkedHashMap::new));
cityCountMap.forEach((city, count) -> System.out.println(city + ": " + count));
```

## Create a map from the list of Integer where key is MAX and MIN String and value is max and min value of the list

**Answer**

Integer max = numbers.stream().max(Integer::compareTo).orElse(null);
Integer min = numbers.stream().min(Integer::compareTo).orElse(null);
Map<String, Integer> resultMap = new HashMap<>();
resultMap.put("MAX", max);
resultMap.put("MIN", min);
resultMap.forEach((key, value) -> System.out.println(key + ": " + value));

## How will I sort a list of employees by age?

**Answer**

```java
List<Employee> employees = Arrays.asList(
    new Employee("Alice", 30),
    new Employee("Bob", 25),
    new Employee("Charlie", 35),
    new Employee("David", 28)
);
List<Employee> sortedEmployees = employees.stream()
    .sorted((e1, e2) -> Integer.compare(e1.getAge(), e2.getAge()))
    .collect(Collectors.toList());
sortedEmployees.forEach(System.out::println);
```

## Write a stream api code to remove duplicates from list of strings

**Answer**

```java
List<String> strings = Arrays.asList("apple", "banana", "apple", "orange", "banana", "grape");
List<String> uniqueStrings = strings.stream()
                                            .distinct()
                                            .collect(Collectors.toList());
```

You are given an array String scores[][] where each element scores[i] represents a student's name and their scores in various subjects. Specifically:
1. scores[i][0] is the student's name.
2. scores[i][1] to scores[i][n] are the scores , where each student may have a different number of scores.
3. Scores may be positive or negative integers.
Additionally:
4. The same student may appear multiple times in the array with different scores.
5. You may assume names contain only alphabetic characters.
Write a function to find the student with the highest average score. If multiple students have the same average score, return the name that appears first in lexicographical (alphabetical) order.

```java
public static String findStudentWithHighestAverage(String[][] scores) {
    Map<String, int[]> studentScores = new HashMap<>();
    for (String[] scoreEntry : scores) {
        String name = scoreEntry[0];
        int[] scoreData = studentScores.getOrDefault(name, new int[2]);
        for (int i = 1; i < scoreEntry.length; i++) {
            scoreData[0] += Integer.parseInt(scoreEntry[i]);
            scoreData[1]++;
        }
        studentScores.put(name, scoreData);
    }
    String topStudent = null;
    double highestAverage = Double.NEGATIVE_INFINITY;
    for (Map.Entry<String, int[]> entry : studentScores.entrySet()) {
        String name = entry.getKey();
        int[] scoreData = entry.getValue();
        double average = (double) scoreData[0] / scoreData[1];
        if (average > highestAverage || (average == highestAverage && (topStudent == null || name.compareTo(topStudent) < 0))) {
            highestAverage = average;
            topStudent = name;
        }
    }
    return topStudent;
}
```

## Write code to encode the string?

**Answer**

```java
public static String encodeString(String input) {
    StringBuilder encoded = new StringBuilder();
    int[] count = {1};
    IntStream.range(1, input.length())
             .forEach(i -> {
                 if (input.charAt(i) == input.charAt(i - 1)) {
                     count[0]++;
                 } else {
                     encoded.append(input.charAt(i - 1)).append(count[0]);
                     count[0] = 1;
                 }
             });
    // Append the last character and its count
    encoded.append(input.charAt(input.length() - 1)).append(count[0]);
    return encoded.toString();
}
```

## Write a program to find the top 3 most occuring words in a list of strings?

**Answer**

```java
List<String> words = Arrays.asList(
    "apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "banana", "kiwi", "kiwi", "kiwi"
);
// Find the top 3 most occurring words
List<Map.Entry<String, Long>> topWords = findTopWords(words, 3);
// Print the results
topWords.forEach(entry -> System.out.println(entry.getKey() + ": " + entry.getValue()));
words.stream()
    .collect(Collectors.groupingBy(word -> word, Collectors.counting())) // Group by word and count occurrences
    .entrySet()
    .stream()
    .sorted(Map.Entry.<String, Long>comparingByValue().reversed()) // Sort by count in descending order
    .limit(topN) // Limit to top N
    .collect(Collectors.toList()); // Collect to list
```

## Find the sum of first n prime numbers?

**Answer**

```java
int n = 10; // Change this value to find the sum of the first n prime numbers
int sum = IntStream.iterate(2, i -> i + 1) // Start with 2 and generate an infinite stream of integers
                .filter(number -> IntStream.rangeClosed(2, (int) Math.sqrt(number))
                .allMatch(divisor -> number % divisor != 0)) // Filter to include only prime numbers
                .limit(n) // Limit to the first n prime numbers
                .sum(); // Sum the prime numbers
```

## Find the factorial of a number using Stream API?

**Answer**

IntStream.rangeClosed(1, number) // Create a stream of integers from 1 to the given number
         .reduce(1, (a, b) -> a * b); // Reduce the stream to calculate the product

## Merge 2 sorted arrays into 1 sorted array using Stream API?

**Answer**

IntStream.concat(Arrays.stream(array1), Arrays.stream(array2))
                        .sorted()
                        .toArray();

## Using Stream API find sum of squares of n numbers?

**Answer**

IntStream.rangeClosed(1, n) // Create a stream of numbers from 1 to n
               .map(x -> x * x)   // Map each number to its square
               .sum();

## Write a code in Stream API to find the name of the employee with the second highest salary?

**Answer**

```java
Optional<Employee> secondHighestSalaryEmployee = employees.stream()
    .sorted(Comparator.comparingDouble(Employee::getSalary).reversed())
    .skip(1)
    .findFirst();
secondHighestSalaryEmployee.ifPresent(employee ->
            System.out.println("Employee with the second highest salary: " + employee.getName())
        );
```

## Perform the following set of operations on an array.

**Answer**

1. Select even numbers
2. Multiply each of them by 2
3. Subtract 1 from each
4. Select all the numbers that are greater than 4

```java
List<Integer> result = Arrays.stream(array)
    .filter(n -> n % 2 == 0) // Select even numbers
    .map(n -> n * 2)         // Multiply each by 2
    .map(n -> n - 1)         // Subtract 1 from each
    .filter(n -> n > 4)      // Select numbers greater than 4
    .boxed()                 // Convert IntStream to Stream<Integer>
    .collect(Collectors.toList());
```

Generates a Fibonacci sequence, limits it to n elements, and then performs the following operations:
1. Collects the first element of each pair in the sequence.
2. Converts the collected elements to a list.
3. Streams the list and removes duplicates.
4. Filters out the even numbers.
5. Sums the remaining even numbers.

```java
int sum = Stream.iterate(new int[]{0, 1}, x -> new int[] {x[1], x[0] + x[1]})
    .limit(n)
    .map(x -> x[0])
    .collect(Collectors.toList())
    .stream()
    .distinct()
    .filter(x -> x % 2 == 0)
    .mapToInt(x -> x)
    .sum();
```

## Does the raw `ArrayList<Generic>` example compile, and why?

**Answer**

class Generic<T> {
    private T value;
    public Generic(T value) {
        this.value = value;
    }
    public T getValue() {
        return value;
    }
}
ArrayList<Generic> g = new ArrayList<>();
Generic<?> g1 = new Generic<>(10);
Generic<?> g2 = new Generic<>("Hello");
g.add(g1);
g.add(g2);
int i = g.get(0).getValue();
String s = g.get(1).getValue();
System.out.println(s);
System.err.println(i);

Creating Generic Objects:
Generic<?> g1 = new Generic<>(10); creates a generic object with an Integer value.
Generic<?> g2 = new Generic<>("Hello"); creates a generic object with a String value.
Adding to ArrayList:
Both g1 and g2 are added to the ArrayList<Generic>.
Retrieving Values:
int i = g.get(0).getValue(); will cause a compile-time error because getValue() returns an Object, and it cannot be directly assigned to an int.
String s = g.get(1).getValue(); will cause a compile-time error for the same reason.

## Which `drive()` implementation is invoked through the `Car` reference?

**Answer**

```java
class Automobile {
    private String drive() {
        return "Driving vehicle";
    }
}
class Car extends Automobile {
    protected String drive() {
        return "Driving car";
    }
}
public class ElectricCar extends Car {
    @Override
    public final String drive() {
        return "Driving an electric car";
    }
    public static void main(String[] wheels) {
        final Car car = new ElectricCar();
        System.out.print(car.drive());
    }
}
```

Driving an electric car.

## Which access modifiers can the overriding `display()` method use?

**Answer**

```java
public class Shape {
    protected void display() {
        System.out.println("Display-base");
    }
}
public class Circle extends Shape { <
    < access - modifier > void display() {
        System.out.println("Display-derived");
    }
}
```

public and protected both can be used.
In Java, when you override a method in a subclass, you can only use an access modifier that is less restrictive or the same as the access modifier of the method in the superclass.

## In what order do the constructors execute?

**Answer**

```java
class Base {
    public Base() {
        System.out.println("Base");
    }
}
class Derived extends Base {
    public Derived() {
        System.out.println("Derived");
    }
}
class DeriDerived extends Derived {
    public DeriDerived() {
        System.out.println("DeriDerived");
    }
}
public class Test {
    public static void main(String[] args) {
        Derived b = new DeriDerived();
    }
}
```

Base
Derived
DeriDerived
In Java, the constructor of the base class is called first, followed by the constructor of the derived class, and so on up the inheritance hierarchy.

## Why does the constructor with two `super` calls fail to compile?

**Answer**

```java
class Base {
    public Base() {
        System.out.print("Base ");
    }
    public Base(String s) {
        System.out.print("Base: " + s);
    }
}
class Derived extends Base {
    public Derived(String s) {
        super(); // Stmt-1
        super(s); // Stmt-2
        System.out.print("Derived ");
    }
}
class Test {
    public static void main(String[] args) {
        Base base = new Derived("Hello ");
    }
}
```

Removing Stmt-1 will make the program compilable and it will print the following: Base: Hello Derived.
Removing Stmt-2 will make the program compilable and it will print the following: Base Derived.
Removing both Stmt-1 and Stmt-2 will make the program compilable and it will print the following: Base Derived.
No, the program will not be compilable if you don't remove any statement. The reason is that a constructor in Java can only call one superclass constructor, and it must be the first statement in the constructor. Having both super(); and super(s); in the constructor of the Derived class violates this rule and will result in a compilation error.
Check if the string is palindrome or not.

public boolean isPalindrome(String s) {
    // Normalize the string: convert to lowercase and remove non-alphanumeric characters
    StringBuilder normalized = new StringBuilder();
    for (char c : s.toCharArray()) {
        if (Character.isLetterOrDigit(c)) {
            normalized.append(Character.toLowerCase(c));
        }
    }
    // Check if the normalized string is a palindrome
    String normalizedStr = normalized.toString();
    String reversedStr = normalized.reverse().toString();
    return normalizedStr.equals(reversedStr);
}

## Write a Java Program to reverse each individual word of a given String.

**Answer**

```java
public static String reverseWords(String str) {
    String[] words = str.split(" ");
    StringBuilder reversedString = new StringBuilder();
    for (String word : words) {
        StringBuilder reverseWord = new StringBuilder(word);
        reversedString.append(reverseWord.reverse().toString()).append(" ");
    }
    return reversedString.toString().trim();
}
```

## Write code to throw your own custom exception in Java.

**Answer**

```java
public class MyCustomException extends Exception {
    public MyCustomException(String message) {
        super(message);
    }
}
```

There are two threads: one has to print odd numbers, one has to print even numbers. It should be sequential from the common list.

```java
public class OddEvenPrinter {
    private static final List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
    private static final Object lock = new Object();
    private static int index = 0;
    public static void main(String[] args) {
        Thread oddThread = new Thread(new OddPrinter());
        Thread evenThread = new Thread(new EvenPrinter());
        oddThread.start();
        evenThread.start();
    }
    static class OddPrinter implements Runnable {
        @Override
        public void run() {
            while (true) {
                synchronized (lock) {
                    if (index >= numbers.size()) break;
                    if (numbers.get(index) % 2 != 0) {
                        System.out.println("Odd: " + numbers.get(index));
                        index++;
                        lock.notify();
                    } else {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                    }
                }
            }
        }
    }
    static class EvenPrinter implements Runnable {
        @Override
        public void run() {
            while (true) {
                synchronized (lock) {
                    if (index >= numbers.size()) break;
                    if (numbers.get(index) % 2 == 0) {
                        System.out.println("Even: " + numbers.get(index));
                        index++;
                        lock.notify();
                    } else {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                    }
                }
            }
        }
    }
}
```

## Write a short code for a deadlock situation?

**Answer**

```java
public class DeadlockExample {
    public static void main(String[] args) {
        final Object lock1 = new Object();
        final Object lock2 = new Object();
        Thread thread1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1: Holding lock 1...");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                System.out.println("Thread 1: Waiting for lock 2...");
                synchronized (lock2) {
                    System.out.println("Thread 1: Holding lock 1 & 2...");
                }
            }
        });
        Thread thread2 = new Thread(() -> {
            synchronized (lock2) {
                System.out.println("Thread 2: Holding lock 2...");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                System.out.println("Thread 2: Waiting for lock 1...");
                synchronized (lock1) {
                    System.out.println("Thread 2: Holding lock 1 & 2...");
                }
            }
        });
        thread1.start();
        thread2.start();
    }
}
```

## Find the top ten IP addresses from a web server log file.

**Answer**

A sample line from the log file:
14716104719,GET,/index.html,10.10.10.1
Sample output:
RANK, IP, COUNT
1, 127.10.24.1, 18975
2, 239.19.5.1, 17497
...
10, 94.104.1.100, 2945

```java
Map<String, Integer> ipCountMap = new HashMap<>();
for (String logLine : logFile) {
        String ip = logLine.split(",")[3];
        ipCountMap.put(ip, ipCountMap.getOrDefault(ip, 0) + 1);
}
// Step 2: Sort the IP addresses by count in descending order
List<Entry<String, Integer>> sortedIPList = new ArrayList<>(ipCountMap.entrySet());
sortedIPList.sort((entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue()));
// Step 3: Output the top ten IP addresses
System.out.println("RANK, IP, COUNT");
for (int i = 0; i < Math.min(10, sortedIPList.size()); i++) {
    Entry<String, Integer> entry = sortedIPList.get(i);
    System.out.println((i + 1) + ", " + entry.getKey() + ", " + entry.getValue());
}
```

## Write a short code for a counter that is increment and decremented by multiple threads?

**Answer**

```java
public class Counter {
    private int count = 0;
    private final ReentrantLock lock = new ReentrantLock();
    public void increment() {
        lock.lock();
        try {
            count++;
            System.out.println("Incremented to: " + count);
        } finally {
            lock.unlock();
        }
    }
    public void decrement() {
        lock.lock();
        try {
            count--;
            System.out.println("Decremented to: " + count);
        } finally {
            lock.unlock();
        }
    }
    public int getCount() {
        return count;
    }
    public static void main(String[] args) {
        Counter counter = new Counter();
        Runnable incrementTask = () -> {
            for (int i = 0; i < 10; i++) {
                counter.increment();
                try {
                    Thread.sleep(50); // Simulate some work
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        };
        Runnable decrementTask = () -> {
            for (int i = 0; i < 10; i++) {
                counter.decrement();
                try {
                    Thread.sleep(50); // Simulate some work
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        };
        Thread incrementThread1 = new Thread(incrementTask);
        Thread incrementThread2 = new Thread(incrementTask);
        Thread decrementThread1 = new Thread(decrementTask);
        Thread decrementThread2 = new Thread(decrementTask);
        incrementThread1.start();
        incrementThread2.start();
        decrementThread1.start();
        decrementThread2.start();
        try {
            incrementThread1.join();
            incrementThread2.join();
            decrementThread1.join();
            decrementThread2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Final count: " + counter.getCount());
    }
}
```

## Write a short code using stream API to update the list of employees in which if salary is less than 5000 give them 10% increment?

**Answer**

employees.stream()
            .filter(employee -> employee.getSalary() < 5000)
            .forEach(employee -> employee.setSalary(employee.getSalary() * 1.10));

Use flatMap to convert an ‘n’ nested list into a single list.

```java
List<Integer> flatList = nestedList.stream()
            .flatMap(List::stream)
            .collect(Collectors.toList());
public static List<Integer> flatten(List<?> nestedList) {
    return nestedList.stream()
        .flatMap(element -> {
            if (element instanceof List) {
                return flatten((List<?>) element).stream();
            } else {
                return Arrays.asList((Integer) element).stream();
            }
        })
        .collect(Collectors.toList());
}
```

## Find Output?

**Answer**

Class A {
    AB(String)
    AB(Integer)
}
Class B {
    BA(String)
    BA(Object)
}
AB(null)
BA(null)
Calling AB(null)
When you call AB(null), the compiler cannot determine whether to call AB(String) or AB(Integer) because both are equally specific in this context. This results in a compilation error due to ambiguity.
Calling BA(null)

**When you call BA(null), the compiler chooses BA(String) over BA(Object) because String is a subclass of Object, making BA(String) more specific.**

The term "more specific" refers to the method whose parameter type is a subclass of the other possible parameter types.
