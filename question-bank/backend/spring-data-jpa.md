# Spring Data, JPA, and Transactions

Database integration, repositories, ORM behavior, transactions, migrations, identifiers, and
connection pools in Spring applications.

[Back to the question-bank index](../README.md)

## Topic Map

- [Database setup and repository choices](#how-do-you-integrate-a-database-into-a-spring-boot-application)
- [Queries, pagination, and performance](#how-do-you-implement-pagination-and-sorting)
- [Transactions](#what-does-transactional-do)
- [ORM behavior and identifiers](#what-is-an-orm-and-how-does-hibernate-relate-to-jpa)
- [Migrations and connection pools](#how-should-a-spring-boot-application-manage-database-migrations)

## How do you integrate a database into a Spring Boot application?

**Answer**

Choose the database and access model from transactions and queries, add the matching starter and
driver, configure a `DataSource` through externalized properties, and manage schema changes with
Flyway or Liquibase. Define entities/repositories for JPA or SQL mappings for JDBC, put transaction
boundaries in the service layer, and test against the real database engine with disposable instances.
Keep credentials outside source control and expose pool/query health and metrics.

## How does a Spring Boot application connect to a database?

**Answer**

Spring Boot binds `spring.datasource.*` properties and auto-configures a `DataSource` when the JDBC
driver and relevant starter are present. It commonly selects HikariCP. JPA adds an
`EntityManagerFactory` and transaction manager; JDBC provides `JdbcTemplate`. Production settings
should come from environment/configuration and a secret store, not hard-coded values.

## How do you configure multiple databases in Spring Boot?

**Answer**

Bind separate property groups and define a `DataSource` for each. For JPA, configure a distinct
`EntityManagerFactory`, transaction manager, entity package, and repository package for each database,
using qualifiers and explicit transaction-manager selection. Cross-database atomicity is not created
by having two managers; use XA only when supported and justified, or design an eventual workflow.

## How do `JdbcTemplate` and Spring Data JPA repositories differ?

**Answer**

`JdbcTemplate` executes SQL directly and handles resource/error boilerplate while the application
maps rows. It gives precise SQL and predictable loading. Spring Data JPA repositories operate over
entities through JPA/Hibernate, providing derived queries, unit-of-work/change tracking, and object
relationships. JPA reduces routine CRUD code but requires understanding generated SQL, fetch plans,
and persistence context. They can coexist.

## How do `CrudRepository` and `JpaRepository` differ?

**Answer**

`CrudRepository` exposes basic save, find, existence, count, and delete operations. `JpaRepository`
extends the Spring Data repository hierarchy with JPA-specific operations such as flush and batch
delete variants and includes list-oriented and paging/sorting capabilities through its supertypes.
Choose the narrowest interface needed; repository inheritance does not make a query efficient.

## What common methods does `JpaRepository` provide?

**Answer**

Typical operations include `save`, `saveAll`, `findById`, `findAll`, `existsById`, `count`, delete
methods, paging/sorting overloads, `flush`, and `saveAndFlush`. Exact signatures change across Spring
Data generations. Bulk delete/update operations can bypass persistence-context synchronization and
entity callbacks, so clear or refresh state as required.

## How do you model a composite primary key with JPA?

**Answer**

Use either an `@Embeddable` key referenced by `@EmbeddedId`, or an `@IdClass` with matching `@Id`
fields. The key type must be serializable for portable JPA use and implement stable `equals` and
`hashCode`. Keep key fields immutable after persistence and map relationships inside a key only with
care.

```java
// EnrollmentId.java
@Embeddable
public class EnrollmentId implements Serializable {
    private Long studentId;
    private Long courseId;

    protected EnrollmentId() {}

    public EnrollmentId(Long studentId, Long courseId) {
        this.studentId = studentId;
        this.courseId = courseId;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (!(other instanceof EnrollmentId that)) return false;
        return Objects.equals(studentId, that.studentId)
            && Objects.equals(courseId, that.courseId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(studentId, courseId);
    }
}
```

```java
// Enrollment.java
@Entity
public class Enrollment {
    @EmbeddedId
    private EnrollmentId id;
}
```

## How does Spring Data JPA optimize repository performance?

**Answer**

It does not automatically optimize arbitrary repositories. It reduces boilerplate and supports
projections, pagination, entity graphs, query derivation, batch settings, and custom queries, but the
developer must inspect generated SQL and plans. Select only needed data, avoid N+1 loading, index
actual predicates, bound result sets, batch deliberately, and measure under realistic transactions.

## How do you implement pagination and sorting?

**Answer**

Pass a `Pageable`, commonly created with `PageRequest.of(page, size, Sort.by(...))`, to a repository
method. `Page<T>` includes a count query and total metadata; `Slice<T>` only reports whether another
slice exists and can avoid the count. Offset pagination becomes expensive and unstable deep into a
changing dataset; use keyset/cursor pagination with a unique deterministic order when needed.

## How do you create and optimize a custom JPA query?

**Answer**

Use a derived method for simple predicates, `@Query` for explicit JPQL/native SQL, Specifications or
Querydsl for dynamic composition, and a custom repository implementation for specialized logic.
Bind parameters, project only required columns, make joins/fetching explicit, paginate with a stable
order, and inspect generated SQL plus the database's actual plan. A native query trades portability
and entity semantics for SQL-specific control; it is not inherently faster.

## How do you implement repository behavior not provided by Spring Data?

**Answer**

Create a fragment interface and implementation, then extend that fragment from the repository. The
implementation can inject `EntityManager`, `JdbcTemplate`, or another appropriate client. Keep domain
query intent in the repository contract, parameterize all input, and test SQL/ORM behavior against the
target database.

## How does Spring Data JPA participate in transactions and rollback?

**Answer**

Repository methods use Spring transaction infrastructure, but business operations should define their
transaction boundary in a service. Within a transaction, JPA tracks managed entity changes and flushes
before commit or when required by a query. By default, Spring rolls back for unchecked exceptions and
`Error`, not every checked exception; configure rollback rules only when the business contract
requires them. A caught exception cannot trigger rollback unless it is rethrown or the transaction is
marked rollback-only.

## How do you diagnose slow Spring Data JPA queries?

**Answer**

Correlate request traces, pool metrics, database statement statistics, and generated SQL. Check for
N+1 selects, unbounded results, unnecessary entity hydration, missing indexes, bad cardinality
estimates, locks, connection-pool waits, flushes, and excessive transaction scope. Use the actual
execution plan and representative data. Fix the measured bottleneck with projections, fetch plans,
query/schema/index changes, batching, pagination, or transaction redesign.

## How do `@EmbeddedId` and `@IdClass` differ?

**Answer**

`@EmbeddedId` stores the key fields in one embeddable value used as the entity's ID property.
`@IdClass` keeps the ID fields directly on the entity and names a separate class with matching names
and types. `@EmbeddedId` often models the key more cohesively; `@IdClass` can make JPQL property paths
flatter. Both require correct equality and stable key values.

## What is Spring Batch?

**Answer**

Spring Batch is a framework for restartable bulk and scheduled processing. A job contains steps;
chunk-oriented steps read, optionally process, and write items within repeated transaction chunks.
The job repository records executions and checkpoints. Design item identity, restartability, skip/
retry policy, partitioning, idempotency, and operational metadata rather than treating a batch job as
one enormous transaction.

## What identifier-generation strategies can JPA use?

**Answer**

JPA provides `AUTO`, `IDENTITY`, `SEQUENCE`, and `TABLE`, while providers also support UUIDs and
custom generators. Database sequences allow allocation blocks and batching; identity columns may
restrict insert batching; table generators can contend. Application-generated UUID/ULID-style keys
avoid central allocation but affect index locality and storage. Choose from database capability,
write concurrency, key exposure, sharding, batching, and ordering requirements.

## Which identifier strategy suits a high-traffic application?

**Answer**

There is no universal choice. On databases with sequences, a pooled sequence often provides compact,
ordered numeric keys and efficient batching. Distributed writers may prefer application-generated
UUIDs or time-ordered identifiers to avoid coordination. Benchmark insertion, index size/locality,
replication, and operational needs; do not select UUID solely because traffic is high.

## How do sequence-generated IDs and UUIDs differ?

**Answer**

Sequence IDs are compact and usually index-friendly but require a database/allocation authority and
can reveal approximate creation order. UUIDs can be generated independently and are globally unique
with negligible collision risk, but use more storage and random variants reduce index locality. Newer
time-ordered UUID variants improve locality but still require a consistent representation and privacy
review.

## Can UUIDs cause index fragmentation?

**Answer**

Random UUIDs inserted into an ordered B-tree land throughout the key space, causing page splits,
lower locality, larger indexes, and more cache pressure than a compact increasing key. The impact
depends on engine, fill factor, write rate, and representation. Store UUIDs in a native/binary type
instead of text where supported, consider time-ordered variants, and measure before changing key
design.

## What caching does Spring Boot provide by default?

**Answer**

Spring Boot auto-configures Spring's cache abstraction when caching is enabled and a supported cache
provider is present. If none is configured, it can fall back to a simple in-memory concurrent-map
provider, which is process-local, unbounded by default, and not suitable as a production distributed
cache. `@Cacheable` does not define freshness; key, TTL, eviction, serialization, and multi-instance
consistency belong to the chosen provider and application design.

## How can Spring call database functions or stored procedures?

**Answer**

Options include `JdbcTemplate`/`SimpleJdbcCall`, JPA `StoredProcedureQuery`, Spring Data
`@Procedure`, or a native query for a scalar function when supported. Map IN/OUT parameters and
result sets explicitly, keep the call inside the intended transaction, and integration-test against
the real database because syntax and metadata behavior are vendor-specific.

## What does `@Transactional` do?

**Answer**

Spring usually applies `@Transactional` through an AOP proxy. At method entry an interceptor obtains
or joins a transaction according to propagation, configures isolation/read-only/timeout where
supported, then commits or rolls back at exit. Self-invocation and calls to non-proxied objects bypass
proxy interception. The annotation does not make remote calls atomic.

## What happens when `@Transactional` appears at class and method level?

**Answer**

The method's transaction metadata overrides the class default for that method. This is valid, but
mixed propagation, isolation, read-only, timeout, or rollback rules can surprise maintainers. Keep
class defaults simple and use method overrides only when the changed semantics are intentional and
tested.

## What is transaction propagation in Spring?

**Answer**

Propagation defines how a method relates to an existing transaction. `REQUIRED` joins or creates one;
`REQUIRES_NEW` suspends the current transaction and creates another; `SUPPORTS`, `MANDATORY`,
`NOT_SUPPORTED`, `NEVER`, and `NESTED` express other policies. `NESTED` relies on savepoint support
and is not equivalent to an independent transaction. Use non-default propagation sparingly because
it changes failure and visibility semantics.

## How should transaction management be structured in Spring?

**Answer**

Place short transaction boundaries around cohesive business operations in the service layer, use one
appropriate transaction manager, and keep slow network calls outside database transactions when
possible. Enforce invariants with database constraints and locking/version checks, allow exceptions
to trigger correct rollback, and test concurrency and failure. Programmatic `TransactionTemplate` is
useful when the boundary cannot be expressed cleanly through proxies.

## How do you handle a database transaction when a remote call fails?

**Answer**

A database rollback cannot undo an already completed remote side effect. Avoid holding a database
transaction open across an unreliable call when possible. Commit local state plus an outbox record,
perform the remote operation idempotently, and record progress in a retryable workflow or saga with
compensation/reconciliation. If the call must occur first, use an idempotency key and persist the
observed outcome carefully.

## Is native SQL always faster than JPQL?

**Answer**

No. JPQL is translated to SQL, and both can produce the same database plan. Performance depends on
the generated statement, parameters, indexes, cardinality, data returned, fetch strategy, and ORM
hydration. Native SQL is valuable for database-specific features or precise shaping, but it reduces
portability and can still be slow. Compare actual plans and end-to-end measurements.

## What is an ORM and how does Hibernate relate to JPA?

**Answer**

Object-relational mapping maps object state and relationships to relational tables and SQL. Jakarta
Persistence (JPA) is the standard API/specification; Hibernate ORM is a common implementation with
additional features. An ORM provides identity mapping, dirty checking, relationship loading, and
query translation, but developers still need SQL, transaction, schema, and database knowledge.

## What is the N+1 query problem?

**Answer**

One query loads a collection of parent rows, then accessing a relationship triggers one additional
query per parent. It causes latency and database load that grows with result size. Detect it from SQL
counts/traces and fix the specific use case with a fetch join, entity graph, projection, batch fetch,
or explicit second query. Making every relationship eager can create huge joins and is not a general
solution.

## What is the difference between eager and lazy loading?

**Answer**

Eager loading retrieves an association as part of loading the owning entity, though the provider may
use joins or additional queries. Lazy loading defers retrieval until the association is accessed and
usually relies on a proxy or persistent collection while a persistence context is available. Choose
fetching per use case with projections/entity graphs rather than changing every mapping to eager.
Lazy access after the session closes can fail, while uncontrolled eager graphs can over-fetch.

## What fields would you model for users, bookings, and payments?

**Answer**

Separate persistence entities from API DTOs and include only data needed by each operation. Typical
domain fields include:

- User: immutable ID, display/contact data, status, and timestamps; never return password hashes or
  internal credentials.
- Booking: ID, user/resource IDs, time range, status, price/currency snapshot, version, and timestamps.
- Payment: ID, booking ID, provider reference, amount/currency, status, idempotency key, and timestamps.

Store payment tokens through a compliant provider rather than raw card data. Define state transitions,
uniqueness, audit, timezone, privacy, and concurrency rules before choosing annotations.

## What is database connection pooling?

**Answer**

A connection pool keeps a bounded set of reusable database connections, avoiding handshake/session
setup on every request and limiting database concurrency. Borrowers must close connections promptly
to return them. Pool size should reflect database capacity and request behavior; a larger pool can
worsen contention. Monitor active, idle, pending, timeout, creation, lifetime, and leak signals.

## How do you add database indexes in a Spring Boot application?

**Answer**

Create indexes through versioned Flyway/Liquibase migrations so production schema changes are
reviewable and repeatable. JPA annotations can describe indexes for schema generation in tests or
simple environments, but `ddl-auto` is not a production migration strategy. Derive each index from
queries and constraints, use database-specific online/concurrent options where needed, and verify the
plan and write impact.

## What is a repository in Spring Data JPA?

**Answer**

A repository is a domain-facing abstraction for loading and persisting aggregate data. Spring Data
generates implementations for supported interfaces and query methods. Keep boundaries aligned with
aggregate ownership, avoid exposing an unbounded generic query surface, and do not place orchestration
or transaction-spanning business workflows in a repository.

## How should a Spring Boot application manage database migrations?

**Answer**

Use one migration tool, normally Flyway or Liquibase, with immutable, ordered scripts in source
control. Test migrations from a production-like baseline and on a clean database, make deployments
backward compatible for rolling releases, separate expand and contract changes, back up and monitor,
and define rollback or forward-repair strategy. Prevent multiple uncontrolled schema owners such as
Hibernate DDL and a migration tool in production.

## Which connection-pool parameters matter most?

**Answer**

Important settings include maximum pool size, minimum idle, connection-acquisition timeout, idle
timeout, maximum lifetime, validation/keepalive behavior, and leak detection for diagnosis. Set
maximum lifetime below infrastructure-enforced connection lifetime and leave capacity for other
clients and administration. Tune from database limits, concurrency, transaction duration, and pool
metrics rather than CPU count alone.

## References

- [Spring Data JPA reference](https://docs.spring.io/spring-data/jpa/reference/)
- [Spring transaction management](https://docs.spring.io/spring-framework/reference/data-access/transaction.html)
- [Hibernate ORM documentation](https://hibernate.org/orm/documentation/)
- [Spring Batch reference](https://docs.spring.io/spring-batch/reference/)
- [HikariCP configuration](https://github.com/brettwooldridge/HikariCP#configuration-knobs-baby)
