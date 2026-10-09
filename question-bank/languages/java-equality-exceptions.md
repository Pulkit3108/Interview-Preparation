# Java Equality, Types, and Exceptions

Object contracts, type conversion, null handling, annotations, exceptions, and resource handling.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## What is the difference between == and equals() method?

**Answer**

`==` compares primitive values, but for references it compares identity: whether both references
refer to the same object or are both `null`. It does not expose or compare memory addresses.
- **Example:** s1 == s2 checks if s1 and s2 reference the same object.
`equals()` compares logical equality as defined by the class and can be overridden with custom
equality logic. For example, `s1.equals(s2)` compares string content rather than reference identity.

## How will you compare 2 instances of the same class?

**Answer**

Reference Equality (==): Checks if two references point to the same object.
- **Logical Equality (equals()):** Checks if two objects are logically equivalent by comparing their contents. Override the equals() method for custom logic.
- **Custom Comparison (Comparable and Comparator):** Provides custom comparison logic for sorting and ordering.

## What are equals() and hashCode() methods?

**Answer**

`Object.equals` defaults to reference identity. A class overrides it when the domain needs logical
value equality.
- **Signature:** public boolean equals(Object obj)
`hashCode` returns an integer used by hash-based structures and must be overridden whenever
`equals` is overridden.
- **Signature:** public int hashCode()
- **General Contract:** Equal objects must have equal hash codes.
Non-equal objects can have the same or different hash codes.
Hash code should remain consistent as long as the object's state does not change.

## In which scenarios is it necessary to override hashcode() and equals() method?

**Answer**

Using Objects as Keys in Hash-Based Collections:
Override hashCode() and equals() to ensure correct behavior in HashMap, HashSet, etc.
- **Ensuring Logical Equality:** Override equals() to compare objects based on their logical state.
Maintaining Consistency Between hashCode() and equals():
Ensure that equal objects have equal hash codes by overriding both methods.

## Which method gets executed first equals() or hashCode()? Does both of these always get executed?

**Answer**

There is no universal execution order. A hash-based collection normally computes a key's hash first
and invokes `equals` only against candidate keys in the selected bucket. An ordinary direct call to
`a.equals(b)` does not call `hashCode`, and identity, empty buckets, or implementation shortcuts can
mean `equals` is not invoked during a map operation.

## What will happen if you override equals() method but not hashCode()?

**Answer**

- **Inconsistent Behavior:** Overriding equals() without overriding hashCode() can lead to inconsistent behavior in hash-based collections.
- **Difficulty in Retrieval:** Objects that are equal according to equals() may not be found in hash-based collections if they have different hash codes.
- **Violation of Contract:** The general contract of hashCode() is violated, leading to logical inconsistencies.

## Why is it important to override hashcode() method if we override equals()? What would be the consequences if we don't?

**Answer**

- **General Contract:** If two objects are equal according to equals(), they must have the same hash code.
If two objects are not equal according to equals(), they can have the same or different hash codes.
- **Consequences of Not Overriding hashCode():** Violation of Contract: Leads to inconsistent behavior in hash-based collections.
- **Incorrect Behavior in Hash-Based Collections:** HashMap: Inability to retrieve objects using the same key.
- **HashSet:** Duplicate elements may be added.
- **Correct Implementation:** Override both equals() and hashCode() to ensure consistent behavior.

## How will you make sure when 2 instances of the same class are compared, they must be equal?

**Answer**

Define equality from the class's stable value state and implement `equals` as reflexive, symmetric,
transitive, consistent, and false for `null`. Implement `hashCode` from the same fields. Do not make
all instances of a class equal merely because their runtime types match; that destroys meaningful
identity and breaks sets and maps.

## How would you handle the scenario where 2 objects in a hashmap have the same hashcode?

**Answer**

- **HashMap Collision Handling:** Uses chaining (linked lists or trees) to handle collisions.
Stores entries with the same hashcode in the same bucket.
- **Equality Check:** Uses the equals() method to find the exact match among entries with the same hashcode.

## What is Upcasting and Downcasting in Java?

**Answer**

- **Upcasting:** Casting a subclass object to a superclass reference. It is safe and does not require an explicit cast.
- **Downcasting:** Casting a superclass reference back to a subclass reference. It requires an explicit cast and can be unsafe if not checked properly.
instanceof Operator: Used to check if an object is an instance of a specific class before performing a downcast to avoid ClassCastException.

## What are covariant return types?

**Answer**

- **Covariant Return Types:** Allow an overridden method in a subclass to return a type that is a subclass of the return type declared in the superclass method.
- **Type Safety:** Maintains type safety by ensuring compatibility between the returned object and the expected type.
- **Flexibility and Specificity:** Provides more flexibility and allows methods to return more specific types, enhancing code expressiveness and reducing the need for type casting.
- **Introduced in Java 5:** This feature was introduced in Java 5.

## If a method that takes super class type as its parameter can it work with an object of it's subclass type?

**Answer**

Yes, a method that takes a superclass type as its parameter can work with objects of its subclass type. This is a fundamental concept in object-oriented programming known as polymorphism.

## What is a wrapper class?

**Answer**

- **Wrapper Classes:** Object representations of primitive data types.
- **Utility Methods:** Provide methods for type conversion, parsing, and more.
- **Autoboxing and Unboxing:** Automatic conversion between primitives and wrapper classes.
- **Immutability:** Wrapper class instances are immutable.

## Are there any performance issues with autoboxing?

**Answer**

- **Memory Overhead:** Autoboxing creates additional objects, leading to increased memory usage.
- **Garbage Collection:** Frequent autoboxing can put extra pressure on the garbage collector.
- **Boxing and Unboxing Overhead:** Method calls and object creation introduce performance overhead.
- **Equality Comparison:** Comparing boxed primitives using == can lead to subtle bugs.
- **Performance Impact in Collections:** Using collections with boxed primitives can impact performance.

## What is Optional Class and how do we use it?

**Answer**

`Optional<T>` represents a result that may be absent; it does not by itself prevent
`NullPointerException`. It is most useful as a return type. Avoid using it indiscriminately for
fields, parameters, collection elements, or serialization models.
- **Creating Optional Instances:** Optional.empty(): Creates an empty Optional.
Optional.of(value): Creates an Optional with a non-null value.
Optional.ofNullable(value): Creates an Optional with a value that may be null.
- **Using Optional:** isPresent(), ifPresent(): Check if a value is present and execute actions.
`orElse` evaluates its fallback eagerly; `orElseGet` invokes its supplier only when empty.
map(), flatMap(): Transform the value if present.
filter(): Conditionally return the value if it matches a predicate.

## What are ways to do null check in Java?

**Answer**

- **Simple Conditional Check:** Use if (str != null) to check for null values.
- **Ternary Operator:** Use (str != null) ? str.length() : 0 for concise null checks.
- **Objects Utility Class:** Use Objects.nonNull(str) for null checks.
- **Optional Class:** Use Optional.ofNullable(str) for more expressive null handling.
- **Apache Commons StringUtils:** Use StringUtils.length(str) for null-safe string operations.
Guava's Optional: Use Optional.fromNullable(str) for null handling with Guava.
Java `assert` statements may be disabled and must not enforce production input validation. Use
`Objects.requireNonNull` for a required value and an explicit conditional when absence is expected.

## What are the benefits of Optional class?

**Answer**

- **Avoid NullPointerException:** Provides a clear and explicit way to handle the absence of a value, reducing the risk of NullPointerException.
- **Expressive Code:** Makes the code more readable and expressive by clearly indicating that a value may be present or absent.
- **Functional Programming Support:** Supports functional programming constructs like map, flatMap, filter, and ifPresent, enabling more concise and declarative code.
- **Encourages Better API Design:** Encourages better API design by explicitly indicating that a method may return an absent value, improving documentation and usability.
- **Eliminates Boilerplate Code:** Reduces boilerplate code for null checks and handling default values with methods like orElse, orElseGet, and orElseThrow.

## What is Annotation in Java?

**Answer**

- **Annotations:** Provide metadata about the code without affecting its execution.
- **Built-in Annotations:** Include @Override, @Deprecated, and @SuppressWarnings.
- **Custom Annotations:** Can be defined using the @interface keyword and can include elements to store additional data.
- **Retention and Target:** Control how long annotations are retained and where they can be applied.

## What is Custom Annotation?

**Answer**

- **Custom Annotations:** Custom annotations allow you to add metadata to your code and can be defined using the @interface keyword.
- **Meta-Annotations:** Use meta-annotations like @Retention and @Target to specify the retention policy and target for the custom annotation.
- **Applying Annotations:** Apply custom annotations to program elements such as classes, methods, and fields.
- **Processing Annotations:** Use reflection or annotation processing tools to process custom annotations at runtime or compile-time.

## What are exceptions in Java?

**Answer**

- **Exception:** In Java, exceptions are represented by classes that are part of the java.lang.Throwable class hierarchy
- **Throwable:** The superclass of all errors and exceptions.
- **Error:** represents serious JVM or environment failures that ordinary application logic should
  generally not attempt to recover from. Narrow infrastructure code may still observe selected
  `Error` subtypes for logging or controlled shutdown.
- **Exception:** Represents conditions that applications might want to catch.
- **Checked Exception:** Exceptions checked at compile-time (e.g., IOException).
- **Unchecked Exception:** Exceptions not checked at compile-time (e.g., NullPointerException).
- **Types of Exceptions:** Built-in exceptions and user-defined exceptions.
throw Keyword: Used to explicitly throw an exception.
throws Keyword: Used in method signatures to declare that a method can throw exceptions.

## What is Exception Hierarchy?

**Answer**

- **Throwable:** The root class of the exception hierarchy.
- **Error:** Represents serious problems that applications should not catch.
- **Exception:** Represents conditions that applications might want to catch.
- **Checked Exceptions:** Must be caught or declared in the method signature.
- **Unchecked Exceptions (Runtime Exceptions):** Do not need to be caught or declared.

## What is the difference between exception and error.

**Answer**

- **Exception:** Definition: Represents conditions that a reasonable application might want to catch.
- **Types:** Includes checked exceptions (e.g., IOException, SQLException) and unchecked exceptions (e.g., NullPointerException, IllegalArgumentException).
- **Handling:** Can be caught and handled using try-catch blocks.
- **Usage:** Used for conditions that an application might anticipate and recover from.
- **Error:** Definition: Represents serious problems that a reasonable application should not try to catch.
- **Types:** Includes OutOfMemoryError, StackOverflowError, VirtualMachineError, etc.
- **Handling:** Generally not caught by applications because they indicate serious problems with the runtime environment.
- **Usage:** Used for conditions that are typically outside the control of the application and usually indicate a problem with the JVM or hardware.

## How does JVM handle exception?

**Answer**

Exception Occurrence The ArithmeticException occurs in method2() when attempting to divide by zero.
- **Exception Propagation:** The JVM creates an ArithmeticException object and searches for an appropriate handler in method2(). Since there is no handler, the exception is propagated to method1().
- **Exception Handling:** method1() also does not have a handler, so the exception is propagated to the main() method.
The main() method has a try-catch block that catches the ArithmeticException.
- **Handling the Exception:** The catch block in the main() method handles the exception by printing a message to the console.
- **Compile-Time:** The Java compiler checks for checked exceptions and ensures they are either caught or declared. This happens when the .class file is created.
- **Class Loading and Linking:** The JVM performs bytecode verification and linking checks when the class is loaded.
- **Runtime:** Exceptions are actually thrown and handled during the execution of the program. Unchecked exceptions are detected and handled at runtime.

## If a Java application encounters an out of memory error what does it mean?

**Answer**

- **OutOfMemoryError:** Indicates that the JVM has run out of memory and cannot allocate more memory for new objects or operations.
- **Common Causes:** Heap Space Exhaustion: Memory leaks, excessive object creation.
- **PermGen Space Exhaustion (Java 7 and earlier):** Excessive class loading.
- **Metaspace Exhaustion (Java 8 and later):** Excessive class loading.
- **Native Memory Exhaustion:** Excessive thread creation, large direct byte buffers.
- **GC Overhead Limit Exceeded:** Excessive time spent in garbage collection.
- **Diagnosing and Resolving:** Analyze Heap Dumps: Identify memory leaks and excessive memory usage.
- **Monitor Memory Usage:** Track memory usage trends.
- **Optimize Memory Usage:** Review and optimize memory usage patterns.
- **Increase Heap Size:** Use -Xms and -Xmx options.
- **Tune Garbage Collection:** Adjust GC settings.
- **Address Class Loading Issues:** Review class loading patterns, increase PermGen/Metaspace size if needed.

## When does an IO Exception occur?

**Answer**

- **Common Causes of IOException:** File Not Found: Attempting to open a non-existent file.
- **Access Denied:** Insufficient permissions to read/write a file or directory.
- **Disk Full:** No space left on the disk to write data.
- **Network Issues:** Connection timeouts, unreachable hosts, dropped connections.
- **Stream Closed:** Reading from or writing to a closed stream.
- **Handling IOException:** Use try-catch blocks to handle IOException and provide meaningful error messages.
Ensure resources like files and streams are properly closed, preferably using try-with-resources for automatic resource management.

## How does try catch finally affect the performance of the program?

**Answer**

- **Normal Execution Path:** The overhead of try, catch, and finally blocks is minimal when no exceptions are thrown.
- **Exception Handling Path:** The performance impact is more significant when exceptions are thrown due to the overhead of creating exception objects, unwinding the call stack, and executing the catch block.
- **`finally`:** runs when control leaves the associated `try`/`catch` normally or through an
  exception, but it is not guaranteed after abrupt JVM or process termination.
- **Best Practices:** Minimize exception usage, keep finally block code efficient, and use preconditions and validations to prevent exceptions.

## How will you handle it if the code can throw multiple types of exceptions?

**Answer**

- **Multiple Catch Blocks:** Handle different types of exceptions separately.
- **Multi-Catch Block:** Catch multiple exceptions in a single catch block (Java 7 and later).
- **Custom Exception Handling:** Create custom exception classes for specific scenarios.
- **Finally Block:** Execute code that must run regardless of whether an exception is thrown.
- **Rethrowing Exceptions:** Catch an exception, perform some processing, and then rethrow it.

## How will you handle Array Index Out Of Bound Exception?

**Answer**

- **Prevent the defect:** validate that `0 <= index && index < array.length`, or iterate without an
  index where appropriate. Do not routinely catch `ArrayIndexOutOfBoundsException`; it normally
  indicates a programming error that should be fixed.
- **Enhanced For Loop:** Use an enhanced for loop (for-each loop) to iterate over the array without worrying about indices.
- **Custom Method:** Create a custom method to safely access array elements, returning a default value if the index is out of bounds.
- **Using Streams:** Use Java Streams to process array elements safely without directly accessing indices.

## What is Exception Propagation?

**Answer**

- **Exception Propagation:** The process by which an exception is passed up the call stack until it is caught by an appropriate exception handler or reaches the top of the call stack.
- **Throwing an Exception:** An exception is thrown using the throw keyword, creating an exception object and transferring control to the nearest enclosing try-catch block.
- **Searching for a Catch Block:** The Java runtime searches for a matching catch block in the current method. If none is found, the exception is propagated to the caller.
- **Propagating the Exception:** The exception is propagated up the call stack until it is caught or reaches the top of the call stack.
- **Unhandled Exceptions:** If the exception reaches the top of the call stack without being caught, the program terminates, and the exception is printed to the console.

## How will you create a runtime custom exception?

**Answer**

- **Extend RuntimeException:** Create a new class that extends RuntimeException to define a custom runtime exception.
- **Define Constructors:** Provide constructors to allow for different ways of instantiating the exception, including with custom error messages and causes.
- **Use the Custom Exception:** Throw the custom exception in your code to handle specific error conditions and catch it where appropriate.

## What happens if an exception is thrown by the main thread?

**Answer**

- **Exception is Caught:** If the exception is caught within a try-catch block, the program can handle it gracefully and continue executing any remaining code.
- **Exception is Not Caught:** The exception propagates up the call stack, causing the main thread to terminate abruptly.
The JVM prints the stack trace of the uncaught exception to the standard error stream.
If no other non-daemon threads are running, the JVM terminates the entire application.
- **Handling Uncaught Exceptions:** You can set an UncaughtExceptionHandler to define custom behavior for uncaught exceptions in the main thread (or any thread).

## What is a try with resources?

**Answer**

The try-with-resources statement is a powerful feature that helps to manage resources efficiently and prevent resource leaks, making your code cleaner and more robust.
- **Automatic Resource Management:** Resources are automatically closed at the end of the try block.
- **Implements AutoCloseable:** Resources must implement the AutoCloseable interface.
- **Simplifies Code:** Reduces boilerplate code and makes the code more readable and maintainable.
- **Multiple Resources:** Can manage multiple resources in a single try-with-resources statement.
- **Custom Resources:** Can be used with custom classes that implement AutoCloseable.

## In which scenarios do you need to create an Custom Exception?

**Answer**

- **Domain-Specific Errors:** Represent specific error conditions unique to your application's domain.
- **Example:** ProductNotFoundException
- **More Descriptive Error Messages:** Provide more descriptive and meaningful error messages.
- **Example:** InvalidUserInputException
- **Wrapping Lower-Level Exceptions:** Wrap lower-level exceptions with higher-level exceptions that are more meaningful.
- **Example:** DatabaseException
- **Enforcing Business Rules:** Enforce specific business rules and constraints.
- **Example:** InsufficientFundsException
- **Improving Code Readability and Maintainability:** Use specific exception types to improve code readability and maintainability.
- **Example:** ConfigurationException
- **Providing Additional Context:** Provide additional context or information about the error condition.
- **Example:** ValidationException
- **Customizing Exception Handling:** Customize exception handling and provide specific responses or actions.
- **Example:** ResourceConflictException

## What is the difference between syntax and sematic errors?

**Answer**

- **Syntax Errors:** Definition: Violations of the grammatical rules of the programming language.
- **Detection:** Detected by the compiler or interpreter at compile time.
- **Impact:** Prevent the code from being executed.
- **Examples:** Missing semicolons, incorrect indentation, unmatched parentheses.
- **Semantic Errors:** Definition: Errors in the logic or meaning of the program.
- **Detection:** semantic errors include compile-time type errors and logic errors that compile but
  produce unintended results. “Using an uninitialized local variable” is a compile-time error in
  Java; an incorrect condition may be found only through tests or runtime behavior.

## In what cases will it finally not be called?

**Answer**

- **JVM Termination:** If the JVM is terminated using System.exit() or crashes, the finally block will not be executed.
- **Infinite Loop or Long-Running Operation:** If the try or catch block contains an infinite loop or a long-running operation that never completes, the finally block will not be executed.
- **Power Failure or Hardware Issues:** If there is a power failure or hardware issue that causes the JVM to terminate abruptly, the finally block will not be executed.

## What is System.exit and in what situations will you use it?

**Answer**

System.exit(int status): Terminates the JVM and exits the program with the specified status code.
- **Situations to Use:** Command-line applications to indicate normal or abnormal termination.
Error handling for critical errors that prevent the program from continuing.
Testing and debugging to observe program behavior.
Shutdown hooks to perform cleanup tasks before termination.
- **Caution:** Use System.exit with care, as it terminates the JVM abruptly and may prevent proper cleanup of resources and impact other running threads.

## What happens internally when system.exit is called?

**Answer**

System.exit(int status):
Terminates the JVM with the specified status code.
A non-zero status code indicates abnormal termination, while zero indicates normal termination.
- **Shutdown Hooks:** Runs all registered shutdown hooks.
Shutdown hooks are registered using Runtime.addShutdownHook(Thread hook).
- **Cleanup limits:** it does not wait for ordinary `finally` blocks in other threads and does not
  guarantee finalization. Shutdown hooks run concurrently and can themselves fail or hang. The
  legacy Security Manager check is not a portable current design assumption.
- **Termination:** Terminates the JVM and returns the status code to the operating system.
