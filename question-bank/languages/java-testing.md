# Java Testing

Unit testing and asynchronous-test fundamentals.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## How do you perform unit testing in Java?

**Answer**

- **Set Up Your Project:** Add JUnit dependencies to your project using Maven or Gradle.
- **Create a Test Class:** Create a test class in the src/test/java directory.
- **Write Test Methods:** Write test methods annotated with @Test to test specific functionalities.
- **Run the Tests:** Use your IDE, Maven, or Gradle to run the tests.
- **Design the test:** arrange one behavior, act through the public API, and assert observable output
  or state. Keep unit tests isolated, deterministic, and fast; use integration tests when framework,
  database, filesystem, or network behavior is part of the contract.
- **Current API:** prefer JUnit Jupiter for new code unless the project is constrained to JUnit 4.

## What are some of the important annotation you use for JUnit testing

**Answer**

- **JUnit 5 Annotations:** @Test: Marks a method as a test method.
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
- **JUnit 4 Annotations:** @Test: Marks a method as a test method.
@Before: Executed before each test method.
@After: Executed after each test method.
@BeforeClass: Executed once before all test methods.
@AfterClass: Executed once after all test methods.
@Ignore: Disables a test method or class.
@Category: Assigns a category for filtering tests.

## How will you write test cases for an async method?

**Answer**

Prefer an API that returns a completion handle such as `CompletionStage`, then await it with a strict
timeout and assert both success and exceptional completion. For callback/event APIs, use a latch,
test probe, or Awaitility condition with a timeout. Inject controllable executors or clocks where
possible instead of sleeping. Verify cancellation, interruption, timeout, and thread-safety behavior
when they are part of the contract; always shut down executors created by the test.
