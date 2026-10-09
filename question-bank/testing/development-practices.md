# Test-Driven and Behavior-Driven Development

Development practices for guiding design and shared behavior through executable examples.

[Back to the question-bank index](../README.md)

## What is test-driven development?

**Answer**

Test-driven development (TDD) uses a short red-green-refactor cycle:

1. Write one small test that expresses missing behavior and confirm it fails for the expected reason.
2. Add the smallest implementation that makes the test pass.
3. Refactor production and test code while keeping the suite green.

TDD provides rapid feedback and often encourages testable interfaces, but passing tests prove only
the covered examples. Good test selection, integration testing, review, and operational validation
remain necessary. A test written after the implementation is useful testing but is not test-first
TDD for that behavior.

## What is behavior-driven development?

**Answer**

Behavior-driven development (BDD) is a collaborative practice for discovering and specifying
observable behavior through concrete examples. Product, engineering, and testing perspectives refine
rules and edge cases before or during implementation. Scenarios are often written as:

- **Given** an initial context,
- **When** an action occurs,
- **Then** an observable outcome follows.

Tools such as Cucumber, SpecFlow, and JBehave can automate selected scenarios, but BDD is not merely
writing every unit test in Gherkin. Keep examples business-readable, avoid coupling them to UI or
implementation detail, and maintain them as living specifications only when their value exceeds their
maintenance cost.

## How do TDD and BDD differ?

**Answer**

TDD is primarily a code-level feedback workflow that drives implementation through failing tests.
BDD emphasizes shared understanding of externally visible behavior through examples and conversation.
They can complement each other: BDD examples describe what the system should do, while TDD guides
the internal implementation in small steps.
