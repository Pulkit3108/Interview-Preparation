# System Design

Requirements, architectural trade-offs, API performance, and end-to-end design exercises.

[Back to the question-bank index](../README.md)

## Topic Map

- [System-design goals](#what-is-a-system-design)
- [Monolith and microservices](#explain-a-bit-about-monolith-vs-microservices)
- [API performance](#how-can-you-optimize-the-performance-of-a-high-performing-api-to-ensure-a-great-user-experience-and-efficient-application-operation)
- [Interview method](#how-should-you-structure-a-system-design-interview)
- [URL-shortener design exercise](#how-would-you-design-a-url-shortening-service)
- [Leaderboard design exercise](#how-would-you-design-a-game-leaderboard)

## What is a system design?

**Answer**

System design turns functional and quality requirements into components, data ownership, interfaces,
deployment topology, and operational behavior. A strong design makes trade-offs explicit across
correctness, latency, throughput, scalability, availability, durability, security, privacy,
maintainability, operability, and cost. It also describes failure modes, evolution, validation, and
what is intentionally deferred.


## Explain a bit about Monolith Vs. Microservices?

**Answer**

A monolith deploys the application as one unit. It can still be modular, scale horizontally, and use
strong internal boundaries. It offers simple local calls, transactions, testing, and operations, but
independent deployment and targeted scaling become harder when modules are tightly coupled.

Microservices deploy bounded capabilities separately. They can improve autonomy, fault isolation,
and targeted scaling, but introduce network failure, distributed data, contract, security,
observability, and platform costs. Containers and Kubernetes are optional deployment tools, not the
definition. Choose from organizational and domain boundaries plus measured needs; application size
alone does not make microservices resilient.

See [Microservices and Resilience](microservices-resilience.md) for the detailed question set.

## How can you optimize the performance of a high-performing API to ensure a great user experience and efficient application operation?

**Answer**

Measure first: define the user-facing latency/availability objective, inspect percentiles and traces,
and locate CPU, I/O, database, dependency, network, serialization, or queue bottlenecks. Then optimize
the limiting path: correct queries/indexes and N+1 calls, bound and paginate results, reuse connections,
reduce payloads, cache only safe hot data, and move genuinely asynchronous work behind a durable job
contract. Scale stateless compute behind a load balancer only after protecting downstream capacity.

Add deadlines, cancellation, overload control, idempotency, and bounded retries. Load-test realistic
traffic and failure modes, compare before/after metrics, and watch tail latency and saturation rather
than only average response time.

## How should you structure a system design interview?

**Answer**

1. Clarify users, core flows, scope, and explicit exclusions.
2. Prioritize quality attributes such as latency, availability, durability, consistency, security,
   privacy, regional needs, and cost.
3. Estimate order-of-magnitude traffic, read/write ratio, object size, storage growth, bandwidth, and
   concurrency only where they influence decisions.
4. Define APIs/events and the data model with ownership and invariants.
5. Draw the simplest end-to-end design and walk through read/write and failure paths.
6. Deep-dive on the actual bottlenecks: partitioning, caching, queues, replication, hot keys,
   backpressure, or real-time delivery.
7. Cover observability, security, rollout, recovery, and trade-offs, then summarize limits and the next
   evolution point.

Use time flexibly rather than forcing a memorized minute-by-minute script. Keep tying each component
to a stated requirement.

## How would you design a URL-shortening service?

**Answer**

Start by clarifying whether links are permanent or expiring, whether users can choose aliases, the
expected read/write ratio, redirect latency, analytics needs, and abuse controls.

The write path validates and normalizes a destination URL, allocates a unique key, and stores a
mapping such as `short_key -> destination, owner, created_at, expires_at`. A Base62-encoded sequence
ID is compact and collision-free but predictable. A random key is harder to enumerate but requires
collision detection and retry. Truncating a URL hash does not remove collision handling and makes
identical URLs share a key unless the design deliberately adds a salt or owner boundary.

The read path looks up the key, checks policy and expiration, records analytics asynchronously, and
returns an HTTP redirect. Use `301` or `308` only when the mapping is intentionally permanent and
cacheable; `302` or `307` is safer when the destination can change. Cache popular mappings, but keep
expiration and invalidation behavior consistent with the source of truth.

At scale, partition by a stable hash of the short key, replicate the mapping store, and protect both
creation and redirect endpoints with rate limits and malicious-URL detection. Define behavior for
deleted links, custom-alias conflicts, hot keys, regional failover, analytics loss, and cache/store
outages. Observability should cover redirect latency, lookup failures, cache hit rate, key collisions,
abuse decisions, and asynchronous analytics lag.

## How would you design a game leaderboard?

**Answer**

Clarify whether the board is global or scoped by game mode, region, season, or friend group; whether
scores replace, increment, or accumulate; how ties are broken; how quickly ranks must update; and
whether users need top-N, their exact rank, or neighbors around their rank. Define reset, late-event,
moderation, privacy, and cheating rules before choosing storage.

Keep an authoritative score event or transaction with an idempotency key so retries cannot award a
result twice. Maintain a ranked projection keyed by board and player. A Redis sorted set is one
option for a bounded real-time board: the member is the player ID, the score is the ranking value,
and sorted-set operations update scores and return ranges or ranks. Store profile data separately,
define a deterministic tie-breaker, and rebuild the projection from authoritative data when needed.

One ordered structure can become a hot key for a very large global board. Partitioning by region or
league helps local boards but makes an exact global rank expensive because shard results must be
merged or summarized. Alternatives include a database table with a suitable composite index,
precomputed rank snapshots, or approximate distributions when exact rank is unnecessary. Separate
exact leaderboards from heavy-hitter sketches, which answer a different question.

Protect score submission with authentication, authorization, server-side validation, replay and
rate controls, and an audit trail. Plan season rollover, retention, deletion, failover consistency,
cache invalidation, and recovery. Observe update latency, read latency, rejected or duplicate events,
projection lag, hot partitions, and rebuild progress.

## References

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [Redis sorted sets](https://redis.io/docs/latest/develop/data-types/sorted-sets/)
