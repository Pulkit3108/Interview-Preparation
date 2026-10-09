# Java Mocking Tools

Mockito, static mocking, and the legacy role of PowerMock.

[Back to the question-bank index](../README.md)

## What is PowerMock?

**Answer**

PowerMock is a legacy extension framework that used custom class loading and bytecode manipulation to
mock static methods, constructors, final/private behavior, and other code that older Mockito versions
could not handle. Its invasive runtime model can conflict with modern JDK modules, coverage tools,
test engines, and framework instrumentation. Treat existing use as technical debt rather than a
default for new tests.

## When would you use PowerMock instead of Mockito?

**Answer**

Prefer current Mockito, which supports final types and scoped static/construction mocking through its
modern mock maker. Use PowerMock only for otherwise unchangeable legacy code on a verified compatible
toolchain, and isolate the tests. A better long-term fix is to move static/global behavior behind an
injectable boundary and test observable behavior without mocking private implementation details.

## References

- [Mockito documentation](https://javadoc.io/doc/org.mockito/mockito-core/latest/org.mockito/org/mockito/Mockito.html)
- [PowerMock project](https://github.com/powermock/powermock)
