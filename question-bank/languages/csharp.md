# C#

C# language, runtime, object-oriented programming, and application-development questions.

[Back to the question-bank index](../README.md)

## What are the different types of inheritances in C#?

**Answer**

Single Inheritance: A class inherits from one base class. This is the most common form of inheritance in C#.
Multilevel Inheritance: A class inherits from a base class, and another class inherits from that derived class, forming a chain of inheritance.
Hierarchical Inheritance: Multiple classes inherit from a single base class.
Multiple Inheritance (via Interfaces): C# does not support multiple inheritance with classes, but it does support multiple inheritance through interfaces. A class can implement multiple interfaces.
Hybrid Inheritance: Hybrid inheritance is a combination of two or more types of inheritance. C# supports hybrid inheritance through a combination of single, multilevel, hierarchical inheritance, and interface implementation.

## Can virtual keywords only be used in abstract classes?

**Answer**

No, the virtual keyword in C# can be used in both abstract and non-abstract classes. The virtual keyword is used to indicate that a method or property can be overridden in a derived class.
In C# you cannot override methods in a derived class unless the method in the base class is marked with the virtual, abstract, or override keyword.
virtual: Allows a method to be overridden in a derived class.
abstract: Must be overridden in a derived class.
override: Used to override a virtual or abstract method in a base class.

## How will you compare 2 instances of the same class?

**Answer**

Reference Equality: Use ReferenceEquals to check if two references point to the same object.
Value Equality: Override Equals, GetHashCode, and the == and != operators to compare the values of properties.
Custom Comparison: Implement IComparable or IComparer for more complex comparisons.

## What are the different types of constructors in C#?

**Answer**

Default Constructor: A default constructor is a parameterless constructor that initializes an object with default values. If no constructor is explicitly defined in a class, the compiler provides a default constructor.
Parameterized Constructor: A parameterized constructor allows you to pass arguments to initialize an object with specific values.
Copy Constructor: A copy constructor initializes an object using another object of the same class. This is useful for creating a deep copy of an object.
Static Constructor: A static constructor is used to initialize static members of a class. It is called automatically before any static members are accessed or any instance of the class is created. It cannot have parameters and cannot be called explicitly.
Private Constructor: A private constructor is used to restrict the instantiation of a class. It is commonly used in singleton patterns or static classes.

## What is a static constructor in C#?

**Answer**

A static constructor in C# is a special constructor that is used to initialize static members of a class. It is called automatically before any static members are accessed or any static methods are invoked.

## Explain MVC architecture.

**Answer**

The Model-View-Controller (MVC) architecture is a design pattern that helps developers build applications in C# by separating the concerns of data, presentation, and user interaction. The MVC pattern can help developers create well-structured, maintainable, and testable applications.
Here's some more information about the MVC architecture:
Model: Stores data and its related logic, and responds to requests from the view and controller.
View: Displays the model data to the user, and allows them to modify it. Views can represent data in the form of tables, charts, and diagrams.
Controller: Handles user requests and interactions, and manages HTTP requests from the user and view. The controller works with the model to retrieve, save, or edit data from the database. The controller then selects a view to render and send the data to the user.

## Difference between Service vs Controller.

**Answer**

Controllers: Manage how users interact with an MVC application. They control the flow of logic, determine what response to send to a user, and ensure request data is valid. Controllers also choose which view or result to return for an API.
Services: Contain business logic and application-specific functionalities. They provide what the consumer of the API is requesting. For example, a service layer can mediate communication between a controller and repository layer, and contain validation logic

## What is Entity Framework?

**Answer**

The Entity Framework (EF) is an object-relational mapping (ORM) tool in C# that helps developers work with relational data in a variety of databases

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

public: The member is accessible from any other code in the same assembly or another assembly that references it.
private: The member is accessible only within the body of the class or the struct in which it is declared.
protected: The member is accessible within its own class and by derived class instances.
internal: The member is accessible only within files in the same assembly.
protected internal: The member is accessible within its own assembly and by derived class instances in another assembly
private protected: The member is accessible within its containing class or types derived from the containing class, but only within the same assembly.

## What is a protected internal access modifier in C#?

**Answer**

In C#, a protected internal access modifier allows a member to be accessed from the current assembly or from types that are derived from the containing class

## What is generic in C#?

**Answer**

Generics in C# are a programming construct that lets you create classes, methods, delegates, and interfaces that are not tied to a specific data type. Instead, you can use placeholders, or type parameters, to specify the type of data that will be used when the class or method is instantiated or called.

## What is the ref and out keyword in C# and How do you use it?

**Answer**

The ref and out keywords are used to pass arguments by reference and change how data is locally modified in method parameters.
The main difference between the two is that ref is two-way, while out is one-way:
ref Allows two-way communication, where the called method can both read and modify the parameter's value. The variable must be initialized before being passed.
out Allows the called method to modify the parameter's value, but the argument can be passed without initialization. It passes data from the caller to the callee but discards any data sent from the caller to the callee.

## What is the difference between readonly, static, and constant?

**Answer**

readonly fields can be assigned a value either at the time of declaration or in the constructor of the class. Once assigned, its value cannot be changed.
static member belongs to the type itself rather than to a specific object. It is shared among all instances of the class.
const field is a compile-time constant. Its value must be assigned at the time of declaration and cannot be changed thereafter

## What are tuples in C#?

**Answer**

In C#, a tuple is a lightweight data structure that can hold multiple data elements, each potentially of a different type. Tuples are used for various purposes, including Method return types, Anonymous types, and LINQ queries.

## How do you take input and output in C#?

**Answer**

```csharp
string? input = Console.ReadLine();
Console.WriteLine(input);
```

## Which LINQ method is used to join two sequences based on a key selector function in.NET?

**Answer**

In .NET, `Join` correlates two sequences by matching keys and projects a result from each matched
pair.

## How can LINQ count occurrences of a character in a string?

**Answer**

```csharp
char target = 'c';
int count = text.Count(character => character == target);
```

## Write a LINQ to filter even numbers and sum it

**Answer**

```csharp
int sum = numbers.Where(number => number % 2 == 0).Sum();
```

## Tell about any newly added features or concepts in C#.

**Answer**

C# 12, the most recent stable version of the language, introduced several new features, including:
Interceptors: An experimental feature that allows users to replace or intercept a method call with an alternative.
Alias any type: Allows users to alias any type using the using alias directive.
Inline arrays: Enables developers to create a fixed-size array in a struct type.
Primary constructors: Allows users to create primary constructors in any class or struct type.
Collection expressions: A new syntax for specifying collection expressions, including the spread element, ( ..e ), to expand any collection.
Ref readonly parameters: Enables more clarity for APIs that might be using ref parameters or in-parameters
