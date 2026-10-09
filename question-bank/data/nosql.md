# NoSQL Data Stores

[Back to the question-bank index](../README.md)

## What is MongoDB, and when is it a suitable choice?

**Answer**

MongoDB is a document database that stores BSON documents in collections. It supports flexible
document shapes, secondary indexes, aggregation pipelines, transactions, replica sets for high
availability, and sharding for horizontal scale. It is useful when an aggregate is naturally modeled
as a document and access patterns benefit from retrieving that aggregate together.

Schema flexibility does not mean schema design is unnecessary. Define validation, ownership of
embedded versus referenced data, document growth limits, indexes, consistency needs, and migration
strategy before choosing it over a relational database.

## How do indexing and replication work in MongoDB?

**Answer**

MongoDB supports single-field, compound, multikey, text, geospatial, hashed, wildcard, and other
index types. Index order should follow measured query filters, sorting, and selectivity; every index
also consumes storage and adds write cost. A multikey index indexes values from array fields, subject
to MongoDB's compound-multikey restrictions.

A replica set has a primary that accepts writes and secondaries that copy the operation log. If the
primary becomes unavailable, eligible voting members elect a replacement. Read preference chooses
where reads may go, while read concern and write concern define consistency and durability behavior.
Reading from a secondary can return stale data, so failover does not by itself guarantee the latest
write is visible everywhere.

## How does Redis work, and what is it used for?

**Answer**

Redis is an in-memory data store with structures including strings, hashes, lists, sets, sorted sets,
streams, bitmaps, HyperLogLogs, and geospatial indexes. Common uses include caches, rate limiters,
session stores, counters, leaderboards, lightweight queues, and coordination primitives. Optional
RDB snapshots and the append-only file provide different persistence trade-offs; replication and
Redis Cluster provide availability and partitioning options.

Redis is not a drop-in relational database. Model memory bounds, eviction, persistence, replication
lag, failover data loss, hot keys, and cache invalidation explicitly.

## Is Redis single-threaded?

**Answer**

The traditional Redis execution model serializes most commands on a main thread, which makes each
individual command atomic relative to other commands. Modern Redis versions can use additional
threads for network I/O and some background or data-structure work, so saying that “Redis has no
multithreading” is inaccurate. Long-running commands can still block command processing, and a
single instance does not automatically use every CPU core for command execution. Scale with better
commands and data models first, then consider sharding or multiple instances when needed.

## How should a Redis-based distributed lock be designed?

**Answer**

Acquire a unique lock value atomically with an expiration, release it only when the stored value
still matches the owner, and bound retry with jitter. Expiry prevents indefinite ownership but also
means a slow client may continue operating after its lease has expired. For operations that must
reject stale owners, include a monotonically increasing fencing token and have the protected resource
validate it.

Whether a single Redis instance, a consensus-backed lock service, or a multi-node algorithm is
appropriate depends on the failure model and correctness requirement. A lock algorithm cannot make
an external side effect atomic by itself.

## Which MongoDB index supports an array field?

**Answer**

A **multikey index** indexes values within an array field, allowing queries to match individual array
elements efficiently. MongoDB creates the multikey behavior automatically when an indexed field
contains an array. Check the current compound-index restrictions before combining multiple array
fields, and verify the resulting query plan with representative data.

## References

- [MongoDB indexes](https://www.mongodb.com/docs/manual/indexes/)
- [MongoDB replication](https://www.mongodb.com/docs/manual/replication/)
- [Redis documentation](https://redis.io/docs/latest/)
- [Redis distributed locks](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/)
