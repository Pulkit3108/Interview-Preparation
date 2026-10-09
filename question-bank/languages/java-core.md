# Core Java Language

Language fundamentals, object-oriented programming, classes, interfaces, and object creation.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## How is Java platform independent?

**Answer**

- **Java Compiler:** Compiles Java source code into platform-independent bytecode.
- **Java Bytecode:** An intermediate representation that can be executed on any platform with a JVM.
- **Java Virtual Machine (JVM):** Interprets and executes bytecode, providing a consistent runtime environment across different platforms.
- **Platform-Specific JVM Implementations:** Each platform has its own JVM implementation, but all JVMs can execute the same bytecode.

## How does a Java code get executed?

**Answer**

- **Write Code:** You write Java source code in a .java file.
- **Compile:** The Java compiler (javac) compiles the source code into bytecode, which is stored in .class files.
- **Class Loader:** The Java Class Loader loads the compiled bytecode into the Java Virtual Machine (JVM).
- **Bytecode Verification:** The JVM verifies the bytecode to ensure it is valid and doesn't violate Java's security constraints.
- **Execution:** The JVM's interpreter or Just-In-Time (JIT) compiler executes the bytecode. The JIT compiler may convert bytecode into native machine code for better performance.
- **Runtime Environment:** The JVM provides a runtime environment with memory management, garbage collection, and other services.

## Why is Java partially Object Oriented? What are the benefits of it?

**Answer**

- **Primitive Data Types:** Java includes primitive data types that are not objects, providing better performance in terms of memory and processing speed.
- **Static Methods and Variables:** Java allows the use of static methods and variables, which belong to the class rather than to any specific instance, simplifying certain programming tasks.
- **Procedural Programming:** Java supports procedural programming, allowing developers to write code using functions and procedures without strictly adhering to object-oriented principles.
- **Performance:** The inclusion of primitive data types allows Java to achieve better performance.
- **Simplicity and Ease of Use:** Static methods and variables simplify programming tasks.
- **Flexibility:** Java's support for both object-oriented and procedural programming provides flexibility to developers.
- **Backward Compatibility:** Java's design allows for backward compatibility with older code that may not strictly adhere to object-oriented principles.

## Why were OOPs introduced in Java?

**Answer**

- **Modularity and Reusability:** Encapsulation: Promotes modularity by encapsulating data and behavior within objects.
- **Inheritance:** Enables code reuse and reduces redundancy.
- **Maintainability and Extensibility:** Separation of Concerns: Simplifies maintenance by dividing a program into distinct objects.
- **Polymorphism:** Allows for easy extension and modification of existing code.
- **Abstraction and Encapsulation:** Simplified Interfaces: Defines abstract classes and interfaces to simplify interactions.
- **Data Hiding:** Protects the integrity of data by hiding internal state.
- **Real-World Modeling:** Natural Mapping: Models real-world entities and interactions more naturally.
- **Improved Collaboration and Teamwork:** Clear Contracts: Provides clear contracts for collaboration.
- **Modular Development:** Allows teams to divide work into manageable units.

## What exactly is public static void main(String[] args)?

**Answer**

public: Access modifier that makes the main method accessible from anywhere, allowing the JVM to call it.
static: Indicates that the main method belongs to the class and can be called without creating an instance of the class.
void: Specifies that the main method does not return any value.
main: The name of the method that serves as the entry point of the Java application.
String[] args: An array of String objects representing command-line arguments passed to the program.

## What would happen if the main method is not declared as static?

**Answer**

- **JVM Invocation:** The main method must be static so that the JVM can invoke it without creating an instance of the class.
- **Entry Point:** Declaring the main method as static provides a consistent and predictable way to start the program.
- **Runtime Error:** If the main method is not declared as static, the JVM will not be able to find the method with the correct signature, resulting in a runtime error

## Can we have multiple public classes in Java?

**Answer**

A compilation unit can contain multiple top-level classes, but at most one may be `public`. If a
public top-level class is present, its simple name must match the source filename under the standard
file-based compiler convention. A class may also contain multiple public nested classes.

## What are different data types in Java?

**Answer**

- **Java has two main categories of data types:** primitive data types and reference data types.
Primitive Data Types
byte: 8-bit integer, range: -128 to 127
short: 16-bit integer, range: -32,768 to 32,767
int: 32-bit integer, range: -2^31 to 2^31-1
long: 64-bit integer, range: -2^63 to 2^63-1
float: 32-bit floating-point
double: 64-bit floating-point
char: unsigned 16-bit UTF-16 code unit; one Unicode code point may require two `char` values
boolean: true or false
Reference Data Types
- **Classes:** e.g., String, Scanner
- **Interfaces:** e.g., Runnable, Serializable
- **Arrays:** e.g., int[], String[]
- **Enums:** e.g., enum Day { MONDAY, TUESDAY, ... }

## What are Strings in Java and what is String constant pool?

**Answer**

- **Strings:** Immutable objects representing sequences of characters.
String Constant Pool (also known as the String Intern Pool) is a special memory region in the Java heap where String literals are stored. When a String literal is created, the JVM checks the pool to see if an identical String already exists. If it does, the reference to the existing String is returned. If not, the new String is added to the pool.

## What is the difference between string and string StringBuffer?

**Answer**

- **Immutability:** String: Immutable; values cannot be changed after creation.
- **StringBuffer:** Mutable; values can be changed after creation.
- **Performance:** String: Less efficient for frequent modifications due to the creation of new objects.
- **StringBuffer:** More efficient for frequent modifications; does not create new objects.
- **Thread Safety:** String: Inherently thread-safe due to immutability.
- **StringBuffer:** Synchronized and thread-safe for use in multi-threaded environments.
- **Usage:** String: Suitable for storing and manipulating fixed strings.
- **StringBuffer:** Suitable for building and modifying strings in a thread-safe manner.

## How String and StringBuffer handle memory differently

**Answer**

- **String:** Immutability: String objects are immutable, meaning their content cannot be changed after creation.
- **Memory Allocation:** String literals are stored in the string pool, while String objects created with the new keyword are stored in the heap.
- **String Pool:** Helps save memory by reusing existing string objects, but modifications result in new object creation.
- **Memory Efficiency:** Less efficient for frequent modifications due to the creation of new objects.
- **StringBuffer:** Mutability: StringBuffer objects are mutable, meaning their content can be changed after creation.
- **Memory Allocation:** Allocates a buffer with an initial capacity that can grow dynamically as needed.
- **Buffer Management:** Modifies the existing buffer without creating new objects, but resizing the buffer can be costly.
- **Memory Efficiency:** More efficient for frequent modifications, as it avoids creating multiple intermediate objects.

## What is StringBuffer and StringBuilder in Java?

**Answer**

Both of these are used to create mutable strings
- **StringBuffer:** Synchronized, thread-safe, slightly slower.
- **StringBuilder:** Not synchronized, not thread-safe, faster.

## What is the difference between String Literal and String Object?

**Answer**

- **String Literal:** Creation: Using double quotes (e.g., String str1 = "Hello";).
- **String Pool:** Stored in the string pool, shared if identical.
- **Memory Management:** Managed by the JVM, automatically interned.
- **Performance:** Faster access due to interning.
- **Comparison:** use `equals` for content. `==` may be true for references to the same pooled
  literal, but it is not a correct general string-comparison strategy.
- **String Object:** Creation: Using the new keyword (e.g., String str3 = new String("Hello");).
- **Heap Memory:** Stored in the heap, each new object creates a new object.
- **Memory Management:** Managed by the garbage collector, not automatically interned.
- **Performance:** Slower due to new object creation.
- **Comparison:** Use equals() method for comparison.

## Why are strings immutable in Java?

**Answer**

- **Security:** Immutable strings prevent unauthorized modification of sensitive data.
- **Thread Safety:** Immutable strings are inherently thread-safe, eliminating the need for synchronization.
- **Caching and Performance:** String pooling and hash code caching improve memory efficiency and performance.
- **Hash Code Caching:** Efficient hashing for operations like hash-based lookups.
- **Design Simplicity:** Predictable behavior and simplified design lead to more reliable code.

## Why would we prefer passwords in character array and not in strings?

**Answer**

- **Immutability of Strings:** Strings are immutable, meaning their contents cannot be changed once created.
Sensitive data stored in strings remains in memory until garbage collected, increasing the risk of exposure.
- **Explicit Clearing of Data:** Character arrays are mutable, allowing their contents to be modified.
You can explicitly overwrite the contents of a character array to clear sensitive data from memory.
- **Garbage Collection Behavior:** The garbage collector does not guarantee when or if it will remove a particular object from memory.
Using a character array allows you to control the lifecycle of sensitive data more precisely.

## What is String Constant Pool and how does it help in optimization?

**Answer**

- **String Constant Pool:** A special memory region in the Java heap where string literals are stored and reused.
- **String Immutability:** Strings in Java are immutable, allowing them to be safely shared and reused.
- **String Literals:** When a string literal is created, the JVM checks the pool for an existing identical string and reuses it if found.
- **String Interning:** The intern() method can be used to manually add strings to the pool or retrieve references to existing strings in the pool.
- **Benefits:** Memory Optimization: Reduces the number of string objects created, leading to more efficient memory usage.
- **Lookup trade-off:** canonical references can support identity checks in a deliberately designed
  interned-symbol system, but ordinary code should use `equals` for string content.

## What is String interning and how does it influence comparison?

**Answer**

- **String Interning:** A method of storing only one copy of each distinct string value in a pool.
- **String Pool:** A special memory region where interned strings are stored.
- **Interning a String:** Using the intern() method to add a string to the pool or retrieve the reference to an existing interned string.
- **Influence on Comparison:** Reference Comparison (==): Interned strings with the same value will have the same reference, so == will return true.
- **Content Comparison (equals()):** Always compares the actual content of the strings, unaffected by interning.
- **Benefits:** Memory Efficiency: Reduces memory usage by storing only one copy of each distinct string value.
- **Comparison:** equal interned strings share a canonical reference, but ordinary content
  comparisons should remain value-based with `equals`.

## What is the final keyword?

**Answer**

- **Final Variables:** Constants that cannot be reassigned.
- **Final Methods:** Methods that cannot be overridden.
- **Final Classes:** Classes that cannot be subclassed.
- **Final Objects:** The reference cannot be changed to point to a different object, but the state of the object can still be modified if the object's class is mutable.

## A class is not final but we are not able to extend it. What could be the different reasons?

**Answer**

The superclass may be inaccessible from the caller's package or module, sealed without permitting the
new subtype, or have no accessible constructor. A private constructor prevents external subclassing
unless another accessible constructor exists. Abstract methods do not prevent extension: the subtype
must implement them or remain abstract. Final or static individual methods restrict overriding, not
subclassing of an otherwise extensible class.

## What would you do If you don't want a class to be inherited?

**Answer**

If you don't want a class to be inherited in Java, you can declare the class as final. A final class cannot be subclassed.

## How will you create an Immutable class and object?

**Answer**

- **Declare the Class as final:** Prevents subclassing.
- **Make All Fields private and final:** Ensures fields are immutable and cannot be accessed or modified directly.
- **Provide a Constructor to Initialize All Fields:** Initializes all fields and ensures they cannot be modified later.

Do not provide setter methods. Make defensive copies of mutable constructor arguments and return
copies or immutable views from accessors so callers cannot mutate internal state.

## In which scenarios you will use immutable objects?

**Answer**

- **Thread safety:** immutable state can be shared after safe publication without locking that state;
  surrounding compound operations may still need coordination.
- **Example:** ImmutablePoint
- **Caching and Memoization:** Immutable objects can be safely cached and reused without worrying about state changes.
- **Example:** FibonacciCache
- **Functional Programming:** Immutable objects align well with functional programming principles, avoiding side effects.
- **Example:** FunctionalExample
- **Defensive Copying:** Immutable objects eliminate the need for defensive copying to protect internal state.
- **Example:** ImmutablePerson
- **Simplifying Code and Reducing Bugs:** Immutable objects make it easier to reason about code and ensure consistent state.
- **Example:** ImmutableRectangle
- **Value Objects:** Immutable value objects ensure consistent state and can be safely compared and used in collections.
- **Example:** Money

## Can you tell the execution flow what happens when a class is loaded or when its object is created?

**Answer**

Loading finds and defines the class. Linking verifies it, prepares static storage with default
values, and may resolve symbolic references. Initialization evaluates static field initializers and
static blocks in source order after the superclass is initialized.

For object creation, memory is allocated and fields receive default values. The selected constructor
invokes another constructor with `this(...)` or a superclass constructor with `super(...)`. After the
superclass constructor returns, this class's instance field initializers and initializer blocks run
in source order, followed by the remainder of the constructor body.

## In java why does static block execute before the main method?

**Answer**

Before invoking a class's `main` method, the JVM initializes that class. Initialization executes its
static field initializers and static blocks in textual order after superclass initialization. Merely
loading a class does not always initialize it; an active use, such as invoking a static method,
triggers initialization.

## What is a sealed class?

**Answer**

A sealed class or interface restricts its direct permitted subtypes. Each permitted subtype must be
`final`, `sealed`, or `non-sealed`. In an unnamed module, permitted subtypes must be in the same
package; in a named module, they must be in the same module. Sealing supports exhaustive domain
modeling but is not a security boundary.

## What is the static keyword?

**Answer**

- **Static Variables:** Shared among all instances of the class.
- **Static Methods:** Can be called without creating an instance of the class.
- **Static Blocks:** Used for static initialization of the class.
- **Static nested classes:** have no implicit outer-instance reference. They can access static members
  directly and instance members through an explicit outer object.

## What is a static initializer block?

**Answer**

A static initializer block performs class-initialization work. It runs when the JVM initializes the
class, not necessarily when the class is merely loaded. Static field initializers and static blocks
run in textual order after superclass initialization.

## Can a static block throw an exception

**Answer**

- **Checked Exceptions:** A static block cannot throw checked exceptions directly.
Checked exceptions must be caught and handled within the static block.
- **Unchecked Exceptions:** A static block can throw unchecked exceptions (runtime exceptions) directly.
If an unchecked exception is thrown, it will cause the class initialization to fail with an ExceptionInInitializerError.

## Can we override static methods?

**Answer**

- **Static Methods Cannot Be Overridden:** Static methods belong to the class, not to instances of the class. Therefore, they cannot be overridden in the same way that instance methods can.
- **Method Hiding:** When a subclass defines a static method with the same name and parameters as a static method in its superclass, the method in the subclass hides the method in the superclass.
- **Binding:** Method hiding uses static (compile-time) binding, while method overriding uses dynamic (runtime) binding.
Instance vs. Class: Overriding applies to instance methods, while hiding applies to static methods.

## Can we overload static methods?

**Answer**

- **Method Overloading:** Allows a class to have more than one method with the same name but different parameter lists.
Applies to both instance methods and static methods.
- **Overloading Static Methods:** You can overload static methods by defining multiple static methods with the same name but different parameter lists.

## Can we call a non-static method from a static method?

**Answer**

- **Static Methods:** Belong to the class itself and can be called without creating an instance of the class.
- **Non-Static Methods:** Belong to an instance of the class and can only be called on an instance of the class.
- **Non-Static Instance Variables:** Belong to an instance of the class and can only be accessed through an instance of the class.
Accessing Non-Static Instance Variables from Static Methods: You can access non-static instance variables from a static method by creating an instance of the class and then accessing the variables through that instance.
- **Calling Non-Static Method from Static Method:** You can call a non-static method from a static method by creating an instance of the class and then calling the non-static method on that instance.

## What is the benefit of static methods and variables?

**Answer**

- **Static Methods:** Utility Functions: Provide common functionality that does not depend on instance-specific data.
- **Memory Efficiency:** Loaded into memory only once, regardless of the number of instances.
- **Ease of Access:** Can be called directly using the class name without creating an instance.
- **Encapsulation of Common Behavior:** Ensure consistent behavior across all instances.
- **Static Variables:** Shared State: Shared among all instances of a class, useful for storing common data.
- **Memory Efficiency:** Loaded into memory only once, leading to efficient memory usage.
- **Global Access:** Can be accessed directly using the class name.
- **Constants:** Used to define constants that are shared across the application.

## What is an abstract keyword?

**Answer**

- **Abstract Class:** A class that cannot be instantiated and may contain abstract methods. It serves as a blueprint for other classes.
- **Abstract method:** a method without an implementation, declared in an abstract class or interface.
  A concrete subtype must implement inherited abstract methods.
- **Inheritance:** Abstract classes are meant to be extended by other classes, which must provide implementations for the abstract methods.

## What is Interface in Java?

**Answer**

An interface is a reference type that declares a contract. It can declare abstract, default, static,
and private methods, constants (`public static final` fields), and nested types, but no instance state
or constructors. A class can implement multiple interfaces, enabling multiple inheritance of type
and limited behavior through default methods.
- **Abstract Methods:** Methods without a body that must be implemented by classes.
- **Default Methods:** Methods with a body that provide a default implementation.
- **Static Methods:** Methods with a body that belong to the interface itself.
- **Constants:** Public static final fields.
- **Multiple Inheritance:** A class can implement multiple interfaces, allowing for multiple inheritance of type.
- **No Constructors:** Interfaces cannot be instantiated directly.
An interface method with no body is implicitly `public abstract`. Default and static methods have
bodies, and modern Java also permits private helper methods inside interfaces.

## What is the difference between abstract class and an interface?

**Answer**

- **Abstract Class:** Purpose: Provides a common base class with shared code and abstract methods.
- **Methods:** Can have both abstract and concrete methods.
- **Fields:** Can have instance variables and static fields.
- **Multiple Inheritance:** A class can extend only one abstract class.
- **Constructors:** Can have constructors.
- **Access Modifiers:** Methods can have any access modifier.
- **Use Case:** Used to share common code and define a common base class.
- **Interface:** Purpose: Defines a contract that implementing classes must follow.
- **Methods:** can have abstract, default, static, and private methods.
- **Fields:** Can only have static final fields (constants).
- **Multiple Inheritance:** A class can implement multiple interfaces.
- **Constructors:** Cannot have constructors.
- **Access modifiers:** abstract and default methods are public; static methods may be public or
  private, and private helper methods are allowed.
- **Use Case:** Used to define capabilities that can be shared across multiple classes.

## What are different Types of Interface in Java?

**Answer**

- **Marker Interface:** An interface with no methods or constants, used to mark or tag a class (e.g., Serializable).
- **Functional Interface:** An interface with exactly one abstract method, used for lambda expressions and method references (e.g., Runnable).
- **Normal Interface:** A typical interface with multiple abstract methods, default methods, static methods, and constants (e.g., Vehicle).
- **Nested Interface:** An interface declared within another class or interface (e.g., OuterClass.InnerInterface).
- **Tagging Interface:** Similar to a marker interface, used to tag classes with specific capabilities or properties (e.g., Cloneable).

## What is a Marker interface?

**Answer**

Marker interfaces in Java are interfaces that do not contain any methods or fields. They are used to "mark" or "tag" a class with a specific property or behavior. The presence of a marker interface can be checked at runtime using reflection, and it can influence the behavior of certain operations or frameworks. It is a simple yet powerful way to convey metadata about a class, enabling certain behaviors or properties to be associated with the class without requiring additional methods or fields. They are often used in conjunction with frameworks or libraries that perform specific actions based on the presence of these markers.

## How does Java distinguish between classes that implement a Marker interface and those who don't?

**Answer**

- **Distinguishing Classes:** Java distinguishes between classes that implement a marker interface and those that don't using the instanceof operator and reflection.
- **Serialization Example:** The Serializable marker interface is used to indicate that a class can be serialized. The serialization mechanism checks if a class implements Serializable before attempting to serialize it.
- **Checking for Marker Interface:** Using instanceof: Checks if an object is an instance of a class that implements the marker interface.
- **Using Reflection:** Checks if a class implements the marker interface using reflection.

## What is reflection?

**Answer**

- **Reflection:** A powerful feature in Java that allows a program to inspect and manipulate the runtime behavior of applications.
Inspect Classes, Interfaces, Fields, and Methods: Reflection allows you to inspect the structure of classes, interfaces, fields, and methods at runtime.
- **Instantiate Objects:** You can create instances of classes dynamically at runtime.
- **Invoke Methods:** You can invoke methods on objects dynamically at runtime.
- **Access and Modify Fields:** You can access and modify the fields of objects dynamically at runtime.
- **Common Use Cases:** Used in frameworks, serialization, dynamic proxies, and development tools

## What is the Java Reflection API?

**Answer**

Java Reflection API is a powerful feature in the Java programming language that allows programs to inspect and manipulate the runtime behavior of applications. It provides the ability to examine or modify the runtime behavior of applications by accessing information about classes, methods, fields, and constructors at runtime.
- **Class Inspection:** Class Object: Obtain the Class object associated with a class using methods like Class.forName(), ClassName.class, or object.getClass().
- **Class Information:** Retrieve information about the class, such as its name, superclass, interfaces, and modifiers.
- **Field Manipulation:** Access Fields: Use the Field class to access and manipulate the fields of a class. You can retrieve field information, get and set field values, and modify field accessibility.
- **Method Invocation:** Access Methods: Use the Method class to access and invoke methods of a class. You can retrieve method information, invoke methods, and modify method accessibility.
- **Constructor Invocation:** Access Constructors: Use the Constructor class to access and invoke constructors of a class. You can retrieve constructor information, create new instances, and modify constructor accessibility.
- **Annotations:** Access Annotations: Use reflection to access annotations on classes, methods, fields, and constructors. You can retrieve annotation information and process it at runtime.

## What is *able interfaces?

**Answer**

In Java, "*able" interfaces are a common naming convention for interfaces that define a specific capability or behavior that a class can implement. These interfaces typically end with the suffix "-able" and indicate that the implementing class is capable of performing a certain action or possessing a certain property. Here are some common examples of "*able" interfaces in Java:
- **Serializable:** Indicates that a class can be serialized.
- **Cloneable:** Indicates that a class allows a field-for-field copy of instances.
- **Comparable:** Defines a natural ordering for objects of a class.
- **Iterable:** Indicates that a class can be iterated over.
- **Closeable:** Indicates that a class can be closed to release resources.
- **Runnable:** Indicates that a class can be executed by a thread.

## What are runnable vs callable interfaces?

**Answer**

The Runnable interface is a functional interface that represents a task that can be executed by a thread.
The Callable interface is a functional interface that represents a task that can be executed by a thread and returns a result.
- **Return Value:** Runnable: The run() method does not return a result.
- **Callable:** The call() method returns a result of type V.
- **Checked Exceptions:** Runnable: The run() method cannot throw checked exceptions.
- **Callable:** The call() method can throw checked exceptions.
- **Functional-interface use:** both are single-abstract-method interfaces and can be lambda targets.
  Java 8 introduced lambda syntax; the interfaces themselves predate it.
- **Usage:** Runnable: Suitable for tasks that do not need to return a result or throw checked exceptions. Commonly used with Thread and ExecutorService.
- **Callable:** Suitable for tasks that need to return a result or throw checked exceptions. Commonly used with ExecutorService and Future.

## Why can’t we create objects for abstract class?

**Answer**

- **Incomplete Implementation:** Abstract classes may contain abstract methods without implementations, making them incomplete and unsuitable for instantiation.
- **Design Purpose:** Abstract classes are designed to be extended by other classes and provide a common interface and shared code.
- **Polymorphism:** Abstract classes are used to achieve polymorphism, allowing different subclasses to provide their own implementations of abstract methods.

## What are different types of Inheritance in Java?

**Answer**

- **Single Inheritance:** One class inherits from one superclass.
- **Multilevel Inheritance:** A class inherits from a class which is also inherited from another class.
- **Hierarchical Inheritance:** Multiple classes inherit from a single superclass.
- **Multiple Inheritance (via Interfaces):** A class implements multiple interfaces.

## What is Hybrid Inheritance?

**Answer**

- **Hybrid Inheritance:** A combination of two or more types of inheritance (single, multiple, multilevel, hierarchical) to create a complex inheritance structure.
- **Java Support:** Java does not support multiple inheritance directly but allows it through interfaces.
- **Example:** Combining single inheritance, multilevel inheritance, hierarchical inheritance, and multiple inheritance via interfaces to form a hybrid inheritance structure.

## What is the Diamond Problem in Java?

**Answer**

The Diamond Problem is a common issue in multiple inheritance scenarios where a class inherits from two classes that have a common ancestor. This can lead to ambiguity and conflicts, particularly when the inherited classes have methods with the same signature.
- **Example:** Class A is the common ancestor.
Classes B and C inherit from A.
Class D inherits from both B and C.
If both B and C override a method from A, and D does not override it, it becomes ambiguous which version of the method D should inherit.
Java avoids multiple inheritance of class state by allowing a class to extend only one class.
Interfaces can contain default implementations, so conflicting defaults are possible. A class
implementation wins over an interface default; a more specific interface wins over a parent
interface; otherwise the implementing class must override the method explicitly.

## What are the different types of constructors in Java?

**Answer**

- **Default Constructor:** Automatically provided by the Java compiler if no other constructors are defined.
- **No-Argument Constructor:** Explicitly defined constructor with no parameters.
- **Parameterized Constructor:** Constructor with parameters to initialize the object with specific values.
- **Copy Constructor:** Constructor to create a new object as a copy of an existing object.

## How does Java resolve the call to an overloaded method?

**Answer**

- **Exact Match:** The compiler first looks for a method with an exact match of the parameter types.
- **Example:** example.display(10); matches display(int a).
- **Type Promotion:** The compiler looks for methods where the arguments can be promoted to match the parameter types.
- **Example:** example.display(10); could match display(long a) if no exact match is found.
- **Autoboxing and Unboxing:** The compiler considers methods where primitive types can be converted to their corresponding wrapper classes and vice versa.
- **Example:** example.display(10); could match display(Integer a) due to autoboxing.
- **Varargs:** The compiler looks for methods that accept variable-length arguments.
- **Example:** example.display(1, 2, 3); matches display(int... a).
- **Ambiguity:** If multiple methods match the call and none is more specific, the compiler throws a compile-time error.
- **Example:** example.display(10, 20); is ambiguous if both display(int, long) and display(long, int) exist.

## What are some different types of access modifiers in Java?

**Answer**

- **Public:** Accessible from any other class.
- **Private:** Accessible only within the declaring class.
- **Protected:** Accessible within the same package and by subclasses.
- **Default (Package-Private):** Accessible only within the same package.

## What is a package in Java?

**Answer**

- **Package:** A namespace that organizes a set of related classes and interfaces.
- **Namespace Management:** Packages provide a unique namespace for each group of classes and interfaces, helping to avoid naming conflicts.
- **Access Control:** Packages allow you to control access to classes and interfaces using access modifiers.
- **Code Organization:** Packages help to organize code in a logical and hierarchical manner, making it easier to manage and maintain large codebases.
- **Reusability:** Packages promote code reusability by grouping related classes and interfaces together.
- **Creating a Package:** Use the package keyword followed by the package name at the top of the source file.
- **Using a Package:** Use the import statement to import classes and interfaces from a package.

## Can 2 Java packages have the same class name?

**Answer**

- **Packages:** Packages group related classes and avoid naming conflicts.
Classes in different packages can have the same name.
- **Fully Qualified Class Names:** The fully qualified class name includes the package name, ensuring unique identification.
- **Example:** com.example.package1.MyClass and com.example.package2.MyClass.
- **Import Statements:** Import classes using their fully qualified names.
Java imports do not support aliases. Import one type and refer to the other by its fully qualified
name, or use fully qualified names for both.

## In a complex project, How would you structure your packages for maximum efficiency and maintainability?

**Answer**

- **Layered Architecture:** Organize packages based on different layers (e.g., presentation, service, repository, domain).
- **Group by Feature or Module:** Group packages by feature or module for larger projects.
- **Descriptive Package Names:** Use clear and descriptive package names.
- **Separate Configuration Classes:** Place configuration classes in a dedicated package.
- **Organize Utility Classes:** Place utility classes in a dedicated package.
- **Use Sub-Packages for Related Classes:** Use sub-packages to further organize related classes.
- **Hybrid Approach:** Combine package-by-layer and package-by-feature for complex projects.

## What is the difference between `new` and reflective construction?

**Answer**

`new MyClass(args)` is compile-time checked and invokes the selected constructor directly.
Reflection chooses the type and constructor at runtime and wraps several failures in reflective
exceptions. `Class.newInstance()` is deprecated because it requires an accessible no-argument
constructor and handles constructor exceptions poorly. Prefer:

```java
Class<?> type = Class.forName("com.example.MyClass");
Object value = type.getDeclaredConstructor().newInstance();
```

## What are different ways to create object in java?

**Answer**

Common construction paths are a constructor call with `new`, a static factory, a builder that
eventually invokes a constructor, or reflection through `Constructor.newInstance`. Deserialization
and cloning can also produce objects without an ordinary constructor call, but both carry strong
design and security caveats and should not be treated as default construction techniques.

## What is Dynamic Method Dispatch in Java?

**Answer**

Dynamic Method Dispatch, also known as runtime polymorphism or late binding, is a mechanism in Java that allows a method to be overridden in a subclass and the appropriate method to be called at runtime based on the object's actual type. This is a key feature of object-oriented programming that enables flexibility and extensibility in code.

## What is super() and this()?

**Answer**

`super(...)` invokes a superclass constructor; `this(...)` invokes another constructor in the same
class. Either call, when present, must be the constructor's first statement, and they cannot both
appear in one constructor. If neither is written and the constructor is not in `Object`, the compiler
inserts `super()`. Compilation fails if the superclass has no accessible no-argument constructor.

## What is a POJO class?

**Answer**

POJO stands for Plain Old Java Object. It is a simple Java class that follows certain conventions and is used to represent data. POJOs are used to encapsulate data and provide getter and setter methods to access and modify that data.
- **No Special Requirements:** A POJO does not require any special inheritance or implementation of interfaces.
It is not bound by any specific framework or library.
- **Private Fields:** Fields (variables) are typically private to encapsulate the data.
- **Public Getter and Setter Methods:** Provides public methods to access and modify the private fields.
- **No-Argument Constructor:** Often includes a no-argument constructor for easy instantiation.
- **No Annotations:** Generally, POJOs do not use annotations, although they can if needed.

## What is Object Class?

**Answer**

In Java, the Object class is the root class of the Java class hierarchy. Every class in Java implicitly extends the Object class, either directly or indirectly. This means that all Java classes inherit the methods of the Object class.

## What is the superclass of Java classes and why is it designed as the super class of all classes?

**Answer**

- **Superclass of All Classes:** The Object class is the superclass of all classes in Java.
- **Common Behavior:** Provides common methods such as equals(), hashCode(), toString(), getClass(), clone(), notify(), notifyAll(), and wait().
- **Polymorphism:** Allows for polymorphism, enabling a single variable of type Object to refer to any object.
- **Collections Framework:** Supports the Java Collections Framework by allowing collections to store any type of object.
- **Reflection:** Provides the getClass() method, which is essential for reflection

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

- **Intrinsic Locks:** Every object in Java has an intrinsic lock (or monitor) associated with it. This lock is used to synchronize methods or blocks of code.
The synchronized keyword can be applied to any object, making it possible to use any object as a lock.
- **Wait-Notify Mechanism:** The wait, notify, and notifyAll methods are used for inter-thread communication. They allow threads to wait for certain conditions to be met and to notify other threads when those conditions change.
These methods must be called on the object that is being used as the lock. Since any object can be used as a lock, these methods are defined in the Object class.
- **Unified Synchronization Model:** By placing wait, notify, and notifyAll in the Object class, Java provides a unified and consistent synchronization model.
This design ensures that any object can be used for synchronization and inter-thread communication, making the language more flexible and powerful.

## What is an Anonymous Object?

**Answer**

An anonymous object in Java is an object that is instantiated but not assigned to any reference variable. These objects are typically used when you need to perform an operation only once and do not need to reuse the object.

## What is Inner class?

**Answer**

- **Member Inner Class:** Defined within another class and has access to the outer class's members.
- **Static Nested Class:** Defined with the static keyword and does not have access to the instance members of the outer class.
- **Local Inner Class:** Defined within a method or a block and can only be instantiated within that method or block.
- **Anonymous Inner Class:** A class without a name, defined and instantiated in a single expression, often used to provide quick implementations of interfaces or abstract classes.

## What is anonymous class and their advantages?

**Answer**

Anonymous class in Java is a class that is defined and instantiated in a single expression, without explicitly declaring a class name. It is typically used to create instances of classes with slight modifications or to implement interfaces on the fly
- **Inline Definition:** Define and instantiate a class in a single expression.
- **One-Time Use:** Ideal for event listeners, callbacks, and other one-time use cases.
- **No Separate Class File:** Reduces the number of files in the project.
- **Encapsulation:** Keeps the scope of the class limited to where it is used.
- **Flexibility:** Can extend existing classes or implement interfaces.

## Difference between anonymous class and lambda expression?

**Answer**

- **Syntax:** Anonymous Classes: Defined using the new keyword followed by the interface or class to be extended/implemented, and a class body.
- **Lambda Expressions:** Have a concise syntax using the -> operator.
- **Verbosity:** Anonymous Classes: More verbose and require more boilerplate code.
- **Lambda Expressions:** More concise and require less boilerplate code.
- **Usage:** Anonymous Classes: Can be used to implement interfaces with multiple methods or extend classes.
- **Lambda Expressions:** Can only be used with functional interfaces (interfaces with a single abstract method).
- **Scope:** Anonymous Classes: Can define fields and methods within the anonymous class body.
- **Lambda Expressions:** Cannot define fields or additional methods within the lambda expression body.
- **Type:** Anonymous Classes: Can be used with any interface or class.
- **Lambda Expressions:** Limited to functional interfaces.
