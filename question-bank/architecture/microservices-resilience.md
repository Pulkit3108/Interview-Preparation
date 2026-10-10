# Microservices and Resilience

Service boundaries, communication, distributed workflows, resilience, security, observability,
caching, and scaling.

[Back to the question-bank index](../README.md)

## Topic Map

- [Architecture and migration](#what-are-microservices)
- [Communication and gateways](#what-is-an-api-gateway)
- [Distributed transactions and workflows](#can-a-transaction-be-reverted-across-microservices)
- [Resilience patterns](#what-is-the-circuit-breaker-pattern)
- [Observability and security](#how-can-you-monitor-and-detect-performance-issues-in-a-microservice-environment)
- [Locking, caching, and scaling](#what-is-the-difference-between-optimistic-and-pessimistic-locking)

## What are microservices?

**Answer**

Microservices are an architectural style in which independently deployable services own bounded
business capabilities and communicate through explicit contracts. Useful boundaries align with
domain ownership, data, and change cadence, not merely small code size.

They can enable team autonomy, independent releases, fault isolation, and targeted scaling. They
also introduce network failure, distributed data consistency, versioned contracts, deployment,
security, and observability costs. A modular monolith is often the simpler starting point.

## What is an API gateway?

**Answer**

An API gateway is an entry point that routes client requests to backend services and may centralize
cross-cutting concerns such as authentication, rate limiting, TLS termination, request shaping, and
observability. Keep business logic out of the gateway, avoid making it a single point of failure, and
apply timeouts and payload limits.

## How would you diagnose and recover from an API gateway outage?

**Answer**

Confirm impact from external probes and route-specific metrics, then distinguish gateway failure from
DNS, certificate, load balancer, network, identity-provider, or upstream-service failure. Correlate
recent changes, health, saturation, errors, latency, logs, traces, and dependency status.

Mitigate with healthy replicas, traffic shifting, rollback, or a tested failover path. Preserve
authentication and rate limits during bypass or degradation. After recovery, document the failure
mode, improve alerting/runbooks, and test redundancy rather than merely restarting the process.

## What are the benefits of microservices over a monolith?

**Answer**

Potential benefits are independent deployment, ownership by bounded domain, targeted scaling,
smaller failure domains, and freedom to evolve implementation behind stable contracts. These appear
only when service boundaries and delivery practices are sound. A distributed monolith can retain
monolithic coupling while adding network and operational complexity.

## What challenges arise when migrating a monolith to microservices?

**Answer**

The hard parts are finding stable domain boundaries, separating data ownership, replacing in-process
transactions and calls, versioning contracts, migrating data safely, and building deployment,
observability, security, and incident-response capabilities. Use incremental extraction, such as a
strangler approach, with measurable outcomes. Do not decompose solely by technical layer or rewrite
everything at once.

## What is the difference between fault tolerance and resilience?

**Answer**

Fault tolerance keeps a required function operating despite specified faults, commonly through
redundancy and failover. Resilience is broader: a system anticipates disruption, limits blast radius,
degrades safely, recovers, and adapts. A replicated service may tolerate one instance failure but
still be non-resilient to overload, bad data, or a shared dependency outage.

## How do you connect one microservice to another?

**Answer**

Use a versioned contract over a suitable transport: HTTP/REST or gRPC for request/response, or a
broker/event stream for asynchronous communication. Resolve endpoints through platform service
discovery or configuration and apply connection pooling, deadlines, bounded retries, circuit
breaking, authentication, and trace-context propagation. Avoid hard-coded instance addresses.

## How should a REST API call an external API?

**Answer**

Use the platform's maintained HTTP client with connection pooling and explicit connect/read/overall
deadlines. Validate destination and response, bound payloads, propagate only approved headers, and
map failures deliberately. Retry only transient idempotent operations with backoff and jitter; add a
circuit breaker or bulkhead when the dependency can exhaust shared resources. Never log credentials
or blindly proxy untrusted URLs.

## What communication styles can microservices use?

**Answer**

- Synchronous request/response over HTTP or gRPC when the caller needs an immediate result.
- Asynchronous commands through a queue when work can be decoupled in time.
- Events or streams for publishing facts to multiple consumers.
- Batch/file exchange for high-volume or externally governed integration.

A service mesh manages transport policy; it is not a business communication style. A shared database
is technically communication but couples schemas and ownership, so treat it as a migration constraint
rather than the default design.

## Can a transaction be reverted across microservices?

**Answer**

There is usually no universal rollback after independently committed service transactions. A saga
uses compensating business actions, which may not restore the exact prior state and must handle
failures and retries. Two-phase commit provides atomic commit only when all resources support it and
accept its coordination and availability costs. Prefer local ACID transactions, idempotency, an
outbox/inbox, and explicit consistency expectations.

## What is Temporal?

**Answer**

Temporal is a durable workflow platform. Workflow state is reconstructed from persisted event
history, so execution can continue after worker failure. Workflow code must remain deterministic
during replay; activities perform external side effects and may run more than once when retried, so
they should be idempotent. Workers poll task queues, while the Temporal service owns scheduling,
history, timers, and coordination.

Temporal provides durable execution, not automatic atomicity across services and not an
unconditional exactly-once guarantee for side effects.

## What strategy would you use for transactions across multiple microservices?

**Answer**

First ask whether the invariant can be contained within one service and database. Otherwise define
the required consistency and failure semantics. A common design commits local state and an outbox
record atomically, publishes idempotent messages, and coordinates a saga with durable state and
compensations. Use 2PC only when every participant and the availability requirement support it.
Design reconciliation, audit, timeout, retry, and manual-repair paths before production.

## How should a service behave when its database is unavailable?

**Answer**

Fail fast with bounded connection and query timeouts, stop unbounded retries, trip a circuit breaker,
and protect thread/connection pools with bulkheads. Return an explicit unavailable or degraded
response unless a bounded, sufficiently fresh cache can safely serve the operation. Buffer writes
only when durable queuing, ordering, idempotency, and capacity are defined. Use database failover only
after validating replication state and consistency. Alert and expose dependency health without
claiming the service is healthy.

## What is the saga pattern?

**Answer**

A saga coordinates a business operation as a sequence of local transactions. Each committed step
has a compensating action or another recovery decision for later failure. The overall state is often
eventually consistent, so intermediate states must be modeled explicitly. Messages and steps need
idempotency, durable progress, correlation, timeouts, retries, and reconciliation.

## How does a saga maintain data consistency?

**Answer**

It preserves agreed business invariants through ordered local commits and compensations rather than
one global rollback. A durable state machine records progress, retries ambiguous outcomes, and invokes
compensation when forward progress cannot continue. Compensation is a business action, not a byte-for-
byte undo, so irreversible steps and concurrent changes require explicit policy.

## How do choreography and orchestration sagas differ?

**Answer**

In choreography, services react to events without one central coordinator. It reduces central
control but can make flow, ownership, and debugging hard as the process grows. In orchestration, a
coordinator sends commands and records the workflow state, improving visibility and control but
making that coordinator important infrastructure. Choose based on workflow complexity and ownership,
not the number of services alone.

## What is the circuit-breaker pattern?

**Answer**

A circuit breaker observes calls to a dependency. It is closed while calls are allowed, opens when a
configured failure or slow-call threshold is exceeded, and later permits limited probes in a half-
open state. It prevents repeated work against an unhealthy dependency and protects caller resources.
It complements, rather than replaces, deadlines, bulkheads, retries, and capacity controls.

## How would you configure a circuit breaker for periodic failure spikes?

**Answer**

Use measured rolling failure and slow-call rates with a meaningful minimum call count instead of one
consecutive-failure number. Set dependency deadlines first, choose a window long enough to ignore
noise but short enough to react, limit half-open probes, and use an open duration compatible with
recovery. Classify only relevant failures. Load-test the settings and alert on open state, rejected
calls, fallback use, and recovery oscillation.

## What is the strangler pattern?

**Answer**

The strangler pattern incrementally replaces a legacy system. A routing seam sends selected
capabilities or traffic to a new implementation while the remaining requests continue to use the
legacy system. Migrate one bounded capability at a time, compare behavior, move data ownership
carefully, provide rollback, and retire the old path after evidence shows it is unused.

## What is the main purpose of the strangler pattern?

**Answer**

Its purpose is to reduce migration risk by delivering and validating replacement capabilities
incrementally instead of performing a single high-risk rewrite or cutover.

## What is the primary benefit of CQRS?

**Answer**

Command Query Responsibility Segregation uses different models for writes and reads. Its primary
benefit is independent optimization of those models when their workloads and representations differ
substantially. Independent scaling can follow, but CQRS adds projection, synchronization, and
eventual-consistency complexity and is unnecessary for ordinary CRUD systems.

## What is an example use case for CQRS?

**Answer**

An order platform might validate commands against an authoritative transactional model while
maintaining denormalized customer, operations, and analytics projections for high-volume queries.
Each projection records checkpoints and tolerates replay. A stock-trading label alone does not
justify CQRS; the differing command invariants and query needs do.

## How can you monitor and detect performance issues in a microservice environment?

**Answer**

Define service-level indicators for traffic, errors, latency, and saturation, then correlate metrics
with structured logs and distributed traces. Instrument boundaries with OpenTelemetry or equivalent,
propagate correlation context, and include dependency, queue, database, runtime, and infrastructure
signals. Use percentiles and exemplars rather than averages alone. Alerts should map to user impact or
capacity risk, while profiles and query plans support deeper diagnosis.

## How would you implement distributed tracing?

**Answer**

Adopt a common context format such as W3C Trace Context. Instrument inbound requests, outbound calls,
messaging, and important internal operations, preferably through OpenTelemetry. Propagate context in
approved headers or message metadata, record errors and useful low-cardinality attributes, and export
through a collector to a trace backend. Configure sampling deliberately and never attach secrets or
unbounded personal data.

## What security controls are important for microservices?

**Answer**

Use authenticated workload identity, least-privilege authorization, encrypted transport, managed
secrets with rotation, input and schema validation, egress controls, dependency and image scanning,
audit logs, and network segmentation as defense in depth. Centralize policy where useful but enforce
authorization at the resource-owning service. Threat-model service-to-service calls, queues,
administrative endpoints, supply chain, and tenant boundaries.

## What is token-based authentication in a microservice architecture?

**Answer**

After authenticating, an identity provider issues a bounded credential such as an opaque access token
or signed JWT. An edge or service validates issuer, audience, signature or introspection result,
expiry, and required claims before authorization. Tokens should be short-lived, narrowly scoped, and
protected in transit and storage. A JWT is a token format, not proof that validation or authorization
is correct.

## How can tokens be passed securely between microservices?

**Answer**

Forward an end-user token only when downstream delegation is intended and its audience permits that
service. Otherwise exchange it for a narrower downstream token or use the calling workload's own
identity. Use TLS or mTLS, keep tokens out of URLs and logs, validate at every trust boundary, and
limit lifetime and scope. A gateway can validate ingress but does not remove downstream authorization.

## What is the difference between optimistic and pessimistic locking?

**Answer**

Optimistic locking reads without holding a long-lived conflicting lock and checks a version or
predicate during update; conflicts cause retry or a user-visible resolution. It works well when
contention is low and operations can retry. Pessimistic locking acquires a database lock before the
critical change, reducing conflicts at the cost of blocking, deadlocks, and lower concurrency. Exact
behavior depends on the database and isolation level.

## When can optimistic locking perform poorly?

**Answer**

It performs poorly when many clients repeatedly update the same record, such as the final seats for a
popular event. Conflicts waste completed work and can create retry storms or starvation. Use atomic
conditional updates, queues, reservation/lease models, finer-grained ownership, or pessimistic
locking when measured contention and business semantics justify them.

## How would you invalidate cached data?

**Answer**

Start with the allowed staleness and source-of-truth write path. Common choices are a bounded TTL,
explicit delete/update after commit, versioned keys, or an outbox/change-data event consumed by cache
owners. Protect against races where an old read repopulates after invalidation, cache stampedes,
missing events, and partial failures. Multi-instance local caches need a coherence plan; if correct
invalidation cannot be designed, do not cache that value.

## What caching strategies are available?

**Answer**

- **Cache-aside:** the application reads the cache, loads on miss, and populates it.
- **Read-through:** the cache abstraction loads missing values.
- **Write-through:** writes pass through the cache abstraction to the store.
- **Write-behind:** writes reach the store asynchronously, improving latency at durability and
  consistency cost.
- **Refresh-ahead:** hot entries refresh before expiry.
- **Local, distributed, hierarchical, HTTP, and CDN caches:** placement choices with different
  latency, capacity, and consistency boundaries.

Every strategy needs key design, bounded size, TTL or invalidation, negative caching policy, failure
semantics, stampede protection, metrics, and a decision about whether stale data is safe.

## How would you serve frequently accessed static reference data without repeated database reads?

**Answer**

If the data is small and truly immutable for a release, load a validated snapshot into process memory
at startup and version it with the application. If it changes independently, use cache-aside or a
distributed snapshot with explicit refresh/version rules. Bound memory, define startup behavior when
the source is unavailable, and expose freshness. Do not introduce Redis merely because data is read
often; choose placement from size, consistency, and multi-instance requirements.

## How can you identify slow database queries?

**Answer**

Start with database statement statistics, slow-query facilities, and application traces to rank
queries by total time, latency percentile, call count, rows, waits, and resource use. Capture a
representative statement and parameters, then inspect the actual execution plan and cardinalities.
Look for scans, spills, bad joins, repeated lookups, lock waits, or excessive round trips. Tools vary:
PostgreSQL has `pg_stat_statements`, SQL Server has Query Store/Extended Events, MySQL has Performance
Schema and the slow log, and Oracle has AWR/ASH subject to licensing and access.

## What should you do when an e-commerce site receives a large traffic spike?

**Answer**

Protect correctness first, especially inventory, orders, and payments. Measure the bottleneck and
apply layered controls: CDN/HTTP caching for public assets, admission control and fair rate limits,
autoscaling within tested capacity, connection-pool limits, queues for deferrable work, and graceful
degradation. Optimize hot queries and indexes, isolate critical dependencies, and use idempotency for
retries. Load-test expected and failure scenarios, monitor saturation, and keep a rollback/runbook.

## What is vertical scaling?

**Answer**

Vertical scaling increases CPU, memory, storage, I/O, or network capacity of one node. It is often
simpler than distributing a workload and can be appropriate for databases or legacy applications,
but it has hardware limits, may require downtime, can be costly, and does not by itself remove a
single failure domain. Horizontal scaling adds nodes and requires partitioning, coordination, or
statelessness appropriate to the workload.

## What is Zuul API Gateway?

**Answer**

Zuul is Netflix's JVM-based edge-service project for routing and filters. Older Spring interview
material often refers to Spring Cloud Netflix Zuul 1, which is a legacy choice and should not be the
default for a new Spring application. Current alternatives include Spring Cloud Gateway, managed API
gateways, ingress proxies, and service-mesh gateways. When maintaining Zuul, state the version and
verify support, threading, timeout, filter, and security behavior.

## What is service discovery?

**Answer**

Service discovery maps a logical service identity to currently usable endpoints. In client-side
discovery, the caller queries a registry or local cache and selects an endpoint. In server-side
discovery, a load balancer, proxy, gateway, or service mesh resolves and selects the endpoint.

Registration and health must reflect readiness rather than mere process existence. Clients also need
timeouts, load-balancing policy, stale-entry handling, connection refresh, retries bounded by an
overall deadline, and behavior for an unavailable registry. In Kubernetes, Services and cluster DNS
provide common discovery abstractions over changing Pod endpoints.

## References

- [Temporal documentation](https://docs.temporal.io/)
- [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [OWASP Microservices Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html)
- [Kubernetes service discovery](https://kubernetes.io/docs/concepts/services-networking/service/)
