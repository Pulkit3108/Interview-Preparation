# C++

C++ language fundamentals, ownership, memory safety, and error handling.

[Back to the question-bank index](../README.md)

## What are smart pointers in C++?

**Answer**

Smart pointers are standard-library types in `<memory>` that express ownership of dynamically
allocated objects and release those objects automatically:

- `std::unique_ptr<T>` represents exclusive ownership. It cannot be copied, but it can be moved.
- `std::shared_ptr<T>` represents shared ownership through a reference count. The object is destroyed
  when the last owning `shared_ptr` is released.
- `std::weak_ptr<T>` observes an object managed by `shared_ptr` without extending its lifetime. It is
  commonly used to avoid reference cycles.

Prefer automatic storage and ordinary value types when possible. Use `std::make_unique` or
`std::make_shared` instead of pairing raw `new` and `delete` calls manually.

## What is a dangling pointer?

**Answer**

A dangling pointer refers to an object whose lifetime has ended. Dereferencing it is undefined
behavior. Common causes include deleting dynamically allocated memory while another pointer still
refers to it, returning the address of a local variable, or retaining a pointer into a container that
has reallocated its storage.

Prefer value semantics, references with clear lifetimes, and smart pointers with explicit ownership.
Assigning one raw pointer to `nullptr` after deletion prevents reuse through that variable, but it
does not repair other aliases that still point to the destroyed object.

## What is the difference between an `int*` and a `char*`?

**Answer**

Both are pointer types, but their pointed-to types affect dereferencing and pointer arithmetic:

- Dereferencing an `int*` produces an `int`; incrementing it advances by `sizeof(int)` bytes.
- Dereferencing a `char*` produces a `char`; incrementing it advances by `sizeof(char)`, which is
  defined as one byte.

The size of an `int` is implementation-defined, so it should not be assumed to be four bytes.
Character pointer types also have special rules that allow them to inspect an object's byte
representation.

## What is the difference between `nullptr` and `NULL`?

**Answer**

`nullptr`, introduced in C++11, is a dedicated null-pointer literal of type `std::nullptr_t`. It
converts to pointer types but not to an ordinary integer, so overload resolution can distinguish a
null pointer from the integer `0`.

`NULL` is an implementation-defined macro traditionally expanding to an integer null-pointer
constant such as `0`. In C++, it can therefore select an integer overload unexpectedly. Modern C++
code should use `nullptr`.

## What does the `mutable` keyword do in C++?

**Answer**

For a non-static data member, `mutable` permits modification even through a `const` object or inside
a `const` member function. It supports **logical constness**: the externally observable value stays
the same while internal implementation state changes.

Typical uses include a cached calculation or a synchronization primitive. It should not be used to
hide changes to the object's logical value, and mutable shared state still requires correct
synchronization.

## What does `inline` mean in C++?

**Answer**

The `inline` specifier permits identical definitions of a function or variable in multiple
translation units, which is why functions defined in headers are often inline. It does not require
the compiler to replace a call with the function body.

Actual call-site inlining is an optimization decision made by the compiler regardless of whether
the keyword is present. Defining a function inside a class definition makes it implicitly inline.

## How should errors and logs be handled in C++?

**Answer**

Choose an error mechanism based on the contract:

- use exceptions for failures that prevent an operation from returning its normal result;
- use a result type, such as `std::optional`, `std::expected` where available, or a project-specific
  result type when failure is expected and should be handled explicitly;
- use error codes at interoperability boundaries or where the surrounding API requires them; and
- use assertions only for violated programmer invariants, not recoverable runtime input errors.

Acquire resources through RAII so stack unwinding performs cleanup automatically. Catch exceptions
only where code can recover, add useful context, or translate the error at a boundary.

Production logging should use a consistent logging abstraction with severity, timestamp, and
request or correlation context. Do not log credentials or sensitive payloads, and do not treat
logging as a substitute for returning or handling an error.

## How can a C++ function check whether a supported input has duplicate characters?

**Answer**

First define the contract. Silently converting arbitrary values such as floating-point numbers to
text creates surprising semantics, and a null pointer is not a valid string. Prefer a function that
accepts a string-like value and let callers perform deliberate conversions.

```cpp
#include <array>
#include <string_view>

bool hasUniqueBytes(std::string_view input) {
    std::array<bool, 256> seen{};

    for (unsigned char value : input) {
        if (seen[value]) {
            return false;
        }
        seen[value] = true;
    }

    return true;
}
```

This checks unique bytes, which is appropriate for ASCII or raw-byte input. It does not check
Unicode characters or grapheme clusters; those require an explicit encoding-aware design.

## What constructor forms should a C++ class designer know?

**Answer**

Important forms include default, converting or other parameterized, copy, and move constructors.
The compiler may implicitly declare some special member functions, but declaring a destructor, copy
operation, or move operation can affect which others are generated or deleted.

Prefer the **rule of zero**: let value-type members and RAII ownership types manage resources so the
class needs no custom destructor, copy constructor, copy assignment, move constructor, or move
assignment. When a class directly manages a resource and must define one of these operations,
consider the complete rule-of-five contract.

## Why should a polymorphic base class usually have a virtual destructor?

**Answer**

Deleting a derived object through a base pointer requires the base destructor to be virtual. Without
it, the behavior is undefined and the derived portion may not be destroyed correctly.

```cpp
class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};
```

A base class that is not intended for polymorphic deletion can instead make destruction protected or
otherwise prevent deletion through a base pointer. Do not add virtual dispatch to every class
automatically; make the ownership and substitution contract explicit.

## What is a pure virtual function and an abstract class?

**Answer**

A pure virtual function is declared with `= 0`. A class with at least one unimplemented pure virtual
function is abstract and cannot be instantiated. Derived concrete classes must provide the required
overrides unless they remain abstract.

```cpp
class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};
```

A pure virtual function can still have a definition in some advanced designs, but the class remains
abstract. Use `override` on derived implementations so the compiler diagnoses signature mistakes.

## How does runtime polymorphism work in C++?

**Answer**

Calling a virtual function through a base-class pointer or reference selects the final overrider for
the object's dynamic type.

```cpp
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
    virtual void show() const { std::cout << "base\n"; }
};

class Derived final : public Base {
public:
    void show() const override { std::cout << "derived\n"; }
};
```

Non-virtual member calls are selected from the static type. Object slicing can also discard the
derived portion when an object is copied into a base value, so polymorphic code normally uses
references or ownership-aware pointers.

## Can functions be overloaded by return type alone?

**Answer**

No. An overload set is distinguished by its parameter-type list and, for member functions, relevant
qualifiers and constraints. The return type alone does not provide enough information at many call
sites and is not part of ordinary overload selection.

```cpp
int convert(int value);
// double convert(int value); // error: differs only by return type
```

Use a different function name, an output parameter, a result wrapper, or a template whose requested
type is supplied explicitly when callers need different result types.

## What are friend functions and classes?

**Answer**

A `friend` declaration grants a named non-member function or another class access to private and
protected members. Friendship is explicitly granted, is not inherited, and is not automatically
reciprocal or transitive.

Friendship can be appropriate for tightly coupled operators or helper types whose implementation is
part of the class's abstraction. It also increases coupling, so prefer a small public interface when
that interface can express the operation without exposing representation details.

## What problem do C++ namespaces solve?

**Answer**

Namespaces group declarations and prevent unrelated libraries from colliding on the same names.
Qualified names such as `project::parser::parse` make ownership explicit, while namespace aliases
can shorten a frequently used qualified name locally.

Avoid `using namespace ...` in headers because it affects every including translation unit and can
create ambiguous or silently changed lookup. A using-declaration for one name in a narrow scope is
usually safer.

## How do `public`, `protected`, and `private` inheritance differ?

**Answer**

The inheritance access specifier controls how accessible base members appear through the derived
type:

- `public` inheritance preserves public and protected access and normally models an is-a
  substitution relationship;
- `protected` inheritance makes inherited public members protected; and
- `private` inheritance makes inherited public and protected members private.

Private inheritance is an implementation technique, not ordinary subtype modeling. Prefer
composition when the derived class only needs to use another type's behavior and does not need to
override protected virtual hooks or exploit another inheritance-specific requirement.

## References

- [C++ smart pointers](https://en.cppreference.com/w/cpp/memory)
- [C++ `nullptr`](https://en.cppreference.com/w/cpp/language/nullptr)
- [C++ `inline`](https://en.cppreference.com/w/cpp/language/inline)
