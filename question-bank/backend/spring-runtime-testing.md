# Spring Runtime, Events, and Testing

Logging, application events, reactive processing, scaling, security, diagnostics, and test strategy.

[Back to the question-bank index](../README.md)

## What logging setup does Spring Boot use by default?

**Answer**

Spring Boot uses Commons Logging internally and, with the standard starters, routes through SLF4J to
Logback. Defaults provide console output and sensible levels. The exact backend can be replaced by
excluding the default logging starter and adding another supported implementation. Application code
should log through SLF4J rather than directly depending on Logback APIs.

## How should logging be implemented in a Spring Boot service?

**Answer**

Use parameterized structured logs with stable event names and correlation/trace IDs. Choose levels
consistently, log an exception once at the responsible boundary, and never emit credentials, tokens,
or sensitive payloads. Externalize level/format configuration, ship logs asynchronously through the
platform where appropriate, and combine them with metrics and traces. Avoid expensive argument work
when a level is disabled.

## What is Logback?

**Answer**

Logback is a Java logging implementation and the common default backend in Spring Boot. It supports
appenders, encoders/layouts, rolling policies, filters, asynchronous appenders, and environment-aware
configuration. Configure bounded retention and failure behavior; asynchronous logging can still drop
or block when its queue is exhausted.

## How do Spring application events work?

**Answer**

Publish an event through `ApplicationEventPublisher` and handle it with `@EventListener` or a listener
interface. Delivery is synchronous in the publisher thread by default, so listener failure and
latency affect the publisher. `@Async` changes thread execution but not durability. For transaction-
aware in-process handling use `@TransactionalEventListener`; for durable cross-service events use an
outbox and broker.

## How would you build real-time user notifications?

**Answer**

Persist the notification and recipient state first, publish a durable event, and have workers fan out
through WebSocket, SSE, push, or email channels. Use IDs for deduplication, authorize subscriptions,
bound per-user queues, handle reconnect/resume, and store delivery/read state when required. Spring
application events alone are in-process and are lost on crash.

## Which Spring Boot features help a service scale?

**Answer**

Spring Boot provides production packaging, externalized configuration, Actuator, metrics, health
groups, graceful shutdown, servlet or reactive stacks, caching abstractions, async execution, and
messaging integrations. None automatically creates scalability. Keep instances stateless where
appropriate, bound thread/connection pools, optimize measured bottlenecks, and scale through the
deployment platform while protecting downstream capacity.

## How would you design high availability for a Spring e-commerce service?

**Answer**

Run multiple instances across failure domains behind health-aware load balancing, use safe readiness
and graceful shutdown, and keep critical state in replicated durable stores. Protect inventory,
orders, and payments with idempotency and concurrency controls. Use queues for deferrable work,
circuit breakers and load shedding for dependencies, tested database failover/backups, observability,
capacity planning, and rollback. Availability is an end-to-end property, not a Spring annotation.

## How do WebFlux and Kafka relate?

**Answer**

Spring WebFlux is a non-blocking web framework based on Reactor; Kafka is a distributed event-streaming
platform. They can coexist through reactive Kafka libraries or adapters, but a Kafka consumer is not
an HTTP event loop. Preserve backpressure where supported, avoid blocking WebFlux threads, configure
consumer concurrency and offset/transaction semantics, and remember that end-to-end delivery depends
on the sink and side effects.

## How should a Spring Boot application protect sensitive customer data?

**Answer**

Classify and minimize collected data, enforce least-privilege authorization and tenant boundaries,
encrypt in transit and at rest with managed keys, tokenize fields when possible, and keep secrets in a
secret manager. Mask logs and telemetry, validate input, use parameterized queries, rotate credentials,
audit access, define retention/deletion, patch dependencies, and test backup and incident response.
Application-level encryption requires a key-rotation and query strategy.

## What testing strategy should a Spring Boot application use?

**Answer**

Use fast unit tests for pure logic; focused slices such as `@WebMvcTest`, `@DataJpaTest`, and client
tests for framework boundaries; and a smaller number of `@SpringBootTest` integration tests. Test
repositories against the real database engine with containers, verify security and serialization,
use contract tests for service boundaries, and keep a few end-to-end critical flows. Do not replace
every collaborator with mocks and call that integration testing.

## When should asynchronous messaging be used?

**Answer**

Use it when producers and consumers should be decoupled in time, work can be retried, multiple
consumers need events, or spikes need buffering. Examples include notifications, fulfillment,
analytics, and integration events. Define message ownership/schema, ordering key, idempotency,
delivery guarantee, retry/backoff, dead-letter handling, retention, backpressure, and observability.
Do not use it when an immediate strongly consistent result is required without modeling the workflow.

## How do you diagnose a Spring Boot service that is slower only in production?

**Answer**

Compare like-for-like traffic, configuration, versions, JVM/container limits, GC, CPU throttling,
thread/connection pools, network, dependencies, database plans/data volume, cache hit rate, and logging.
Use traces and profiles to locate time, correlate latency percentiles with saturation and errors, and
check recent deploy/config changes. Reproduce with production-like load and data, change one measured
bottleneck at a time, and verify the result. Do not start by increasing every pool.

## How do Jersey and Spring integrate for a CRUD API?

**Answer**

Add the Jersey starter, register JAX-RS resource classes in a `ResourceConfig`, and let Spring create
or inject services/repositories used by those resources. Use JAX-RS annotations for paths and media
types, Bean Validation for input, and Spring transactions in the service layer. Choose either Jersey
or Spring MVC as the primary HTTP stack unless coexistence is an explicit requirement; overlapping
mappings and error/security configuration add complexity.

## How should a proxied Spring bean be invoked from `main`?

**Answer**

Start the application context and obtain the bean from it rather than constructing the target class:

```java
ConfigurableApplicationContext context = SpringApplication.run(Application.class, args);
Employee employee = context.getBean(Employee.class);
employee.performWork();
```

Calling the managed bean lets Spring apply AOP advice such as transactions or security. Self-invoking
another advised method on the same target still bypasses proxy interception; move the method to
another bean or use AspectJ when that behavior is truly needed.

## References

- [Spring Boot logging](https://docs.spring.io/spring-boot/reference/features/logging.html)
- [Spring application events](https://docs.spring.io/spring-framework/reference/core/beans/context-introduction.html#context-functionality-events)
- [Spring Boot testing](https://docs.spring.io/spring-boot/reference/testing/index.html)
- [Spring WebFlux](https://docs.spring.io/spring-framework/reference/web/webflux.html)
