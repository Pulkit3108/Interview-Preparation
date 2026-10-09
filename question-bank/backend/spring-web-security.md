# Spring Web, Security, and Error Handling

Spring MVC request mapping, content negotiation, clients, security, exceptions, and asynchronous
execution.

[Back to the question-bank index](../README.md)

## What do `@RestController` and `@RequestMapping` do?

**Answer**

`@RestController` combines `@Controller` with `@ResponseBody`, so handler return values are written
through configured `HttpMessageConverter`s rather than resolved as view names. `@RequestMapping`
constrains a controller or method by path, HTTP method, parameters, headers, consumed media types, and
produced media types. Prefer the composed method annotations when one method is intended.

## How do `@Controller` and `@RestController` differ?

**Answer**

`@Controller` participates in Spring MVC and commonly returns logical view names; individual methods
can add `@ResponseBody`. `@RestController` applies response-body semantics to every handler. Either can
return `ResponseEntity`; choose from HTML view rendering versus representation APIs.

## Which annotations are common in Spring MVC REST endpoints?

**Answer**

Common annotations include `@RestController`, `@RequestMapping`, `@GetMapping`, `@PostMapping`,
`@PutMapping`, `@PatchMapping`, `@DeleteMapping`, `@PathVariable`, `@RequestParam`, `@RequestHeader`,
`@RequestBody`, `@Valid`, and `@ControllerAdvice`/`@ExceptionHandler`. Annotations express the
contract, but validation, authorization, and HTTP semantics still require deliberate design.

## How do `@RequestParam` and `@PathVariable` differ?

**Answer**

`@PathVariable` binds a URI-template segment that identifies the routed resource, such as
`/orders/{id}`. `@RequestParam` binds a query/form parameter commonly used for optional filters,
sorting, or pagination. Both can be converted and validated. Do not place secrets in either location,
and authorize the resolved object rather than trusting the identifier.

## Why prefer `@GetMapping` to `@RequestMapping(method = GET)`?

**Answer**

`@GetMapping` is a composed annotation with the same GET mapping semantics and less noise. Use
`@RequestMapping` when defining shared class-level constraints or when a handler intentionally maps
multiple methods, though separate method-specific handlers are usually clearer.

## How does Spring MVC select a controller method?

**Answer**

`DispatcherServlet` asks `RequestMappingHandlerMapping` for mappings whose path, HTTP method,
parameters, headers, `consumes`, and `produces` conditions match. Spring selects the most specific
valid mapping or reports no match/ambiguity. HTTP method is part of the mapping, so identical paths
can have separate GET and POST handlers.

## What is the Spring MVC request flow?

**Answer**

Servlet filters run first, including the Spring Security chain. `DispatcherServlet` finds a handler,
interceptors run, an adapter resolves method arguments through converters/resolvers and validation,
then invokes the controller. The return value is handled as a view or serialized representation.
Exceptions pass through registered resolvers and advice. Interceptor completion and filters run as
the response unwinds.

## Which upload representation should a Spring API use?

**Answer**

Use `multipart/form-data` for a file plus structured fields, or a raw request body for one known media
type. Avoid base64 inside JSON for large files because it adds size and buffering. Configure strict
count/size limits, stream content, validate authorization and actual type, sanitize names, scan when
required, and prefer object storage for large blobs.

## How would you structure a Spring API that retrieves users from a database?

**Answer**

Use a controller for HTTP mapping/validation, a service for authorization and business orchestration,
and a repository for persistence. Return a response DTO rather than the entity, map absence to 404,
and paginate collections. Put the read transaction at the service boundary and test web, service, and
repository behavior at appropriate layers.

## How can a Spring endpoint support JSON and XML?

**Answer**

Add compatible Jackson JSON and XML message converters, declare supported `produces`/`consumes`
media types, and let `Content-Type` describe request content while `Accept` negotiates the response.
Use one DTO contract only when both serializers represent it consistently, and test validation,
polymorphism, dates, nulls, and error responses in both formats.

## How should a Spring Boot application call a third-party REST API?

**Answer**

Use `RestClient` for imperative applications or `WebClient` for reactive/streaming use cases; use
Spring's HTTP service interfaces when a declarative client fits. Configure pooled transport,
deadlines, TLS, authentication, payload limits, validation, observability, and cancellation. Retry
only transient idempotent operations with backoff/jitter and protect resources with a circuit breaker
or bulkhead when justified.

## How do you configure HTTP Basic authentication in Spring Security?

**Answer**

Define a `SecurityFilterChain`, authorize request patterns, configure an `AuthenticationProvider` or
user source with a strong `PasswordEncoder`, and enable `httpBasic`. Basic sends credentials on each
request, so TLS is mandatory. It is suitable for controlled service/tool scenarios, not usually the
best browser-user login experience. Disable CSRF only when the authentication/client model makes that
safe, not simply because the API returns JSON.

## How would you secure an inventory REST API?

**Answer**

Authenticate through a trusted identity provider, validate access tokens or sessions, and enforce
resource/action-level authorization in the service. Separate read, adjustment, reservation, and admin
permissions; validate quantities and state transitions; use optimistic/atomic concurrency controls
and idempotency for retries. Add TLS, payload limits, rate limits, audit trails, safe errors, secret
management, dependency hygiene, and security tests.

## What does Spring Security provide?

**Answer**

Spring Security supplies servlet/reactive filter chains, authentication, authorization, password
encoding, session and OAuth2/OIDC resource/client support, method security, CSRF protection, security
headers, and test utilities. It provides mechanisms, not a complete policy: the application must
model identities, permissions, tenant/resource boundaries, credential lifecycle, and failure behavior.

## What is method-level security?

**Answer**

After enabling method security, annotations such as `@PreAuthorize`, `@PostAuthorize`,
`@PreFilter`, and `@PostFilter` can enforce authorization at service methods. Prefer pre-authorization
with explicit domain checks; post-filtering loaded collections can be inefficient and may expose data
before filtering. Like transactions, proxy-based interception can be bypassed by self-invocation.

## How should communication between Spring microservices be secured?

**Answer**

Use TLS or mTLS for transport and workload identity, OAuth2 access tokens or signed service
credentials with narrow audience/scope, and authorization at every receiving service. Keep secrets in
a managed store, rotate them, restrict network/egress paths, and propagate user identity only when
delegation is intended. Spring Boot does not secure service calls automatically.

## How are exceptions handled in a Spring Boot API?

**Answer**

Let domain/application exceptions propagate to centralized `@ControllerAdvice` handlers. Map them to
stable HTTP semantics and a consistent `ProblemDetail` or error DTO, log unexpected failures once
with correlation context, and avoid exposing stack traces or internal details. Validation,
authentication, and framework exceptions can be customized through the same resolver chain.

## How do you create and use a custom exception?

**Answer**

Create a meaningful exception representing a domain or application failure, include safe structured
context, throw it at the boundary that detects the failure, and map it centrally. Do not create one
class per message or make exceptions carry HTTP concerns deep into the domain unless that coupling is
intentional.

## How does `@ControllerAdvice` map exceptions to responses?

**Answer**

`@ControllerAdvice` applies cross-controller concerns. Methods annotated with `@ExceptionHandler`
select exception types and return `ProblemDetail`, a DTO, or `ResponseEntity` with an appropriate
status and headers. Ordering matters when multiple advice beans can handle the same exception. Keep
the mapping deterministic and integration-test content negotiation and status.

## How would you design an exception hierarchy for a large application?

**Answer**

Use a small hierarchy around stable failure semantics, such as not found, conflict, invalid state,
dependency unavailable, and authorization denied. Preserve the original cause, include a non-secret
error code/correlation ID, and map categories centrally. Avoid catching everything into one business
exception or mirroring every infrastructure exception; unexpected failures should remain visible as
server errors.

## How do `ExecutorService` and `ThreadPoolExecutor` differ?

**Answer**

`ExecutorService` is the interface for submitting tasks, lifecycle, futures, and bulk execution.
`ThreadPoolExecutor` is a configurable implementation exposing core/max threads, queue, keep-alive,
thread factory, rejection policy, and hooks. Program to the interface where possible, but configure
the concrete pool from workload and capacity. An unbounded queue can make maximum threads irrelevant
and turn overload into memory/latency growth.

## What is the Java executor framework?

**Answer**

The executor framework separates task submission from thread management through `Executor`,
`ExecutorService`, scheduled executors, futures, and implementations such as thread pools and
fork/join pools. Choose pools by blocking versus CPU-bound work, bound queues, propagate required
context deliberately, handle rejection, and shut down owned executors. Virtual-thread executors are
another option for high-concurrency blocking tasks on supported Java versions.

## What does Spring's `@Async` do?

**Answer**

With async execution enabled, a proxy intercepts an eligible method and submits it to a configured
`TaskExecutor`. The caller returns immediately; supported return types include `void`, `Future`, and
`CompletableFuture`. Self-invocation bypasses the proxy. Configure a named bounded executor, rejection
policy, shutdown behavior, and context propagation rather than relying on an accidental default.

## How are exceptions handled from `@Async` methods?

**Answer**

For `Future`/`CompletableFuture` methods, the exception completes the future exceptionally and the
caller must observe it. Exceptions from `void` async methods go to an `AsyncUncaughtExceptionHandler`
and cannot be returned to the original caller. Log and meter failures, preserve correlation context,
and prefer a returned future or durable job mechanism when the result matters.

## How do you map exceptions to HTTP status codes?

**Answer**

Use `@ExceptionHandler` in `@ControllerAdvice`, or `ResponseStatusException` for narrowly scoped
cases. Map by semantics: invalid syntax/input to 400, unauthenticated to 401, unauthorized to 403,
missing resource to 404, state/version conflict to 409, and unexpected failures to 500. A dependency
timeout may be 502/503/504 depending on the gateway and contract. Do not return 200 with an error
body.

## Should controllers catch exceptions directly?

**Answer**

Only when a controller can add endpoint-specific recovery. Otherwise central advice produces more
consistent responses and avoids duplicated catch blocks. Controllers should validate and delegate;
services express failures, and centralized handlers translate them to HTTP without leaking internal
exceptions.

## References

- [Spring Web MVC](https://docs.spring.io/spring-framework/reference/web/webmvc.html)
- [Spring Security reference](https://docs.spring.io/spring-security/reference/)
- [Spring REST clients](https://docs.spring.io/spring-framework/reference/integration/rest-clients.html)
- [Spring asynchronous execution](https://docs.spring.io/spring-framework/reference/integration/scheduling.html#scheduling-annotation-support-async)
