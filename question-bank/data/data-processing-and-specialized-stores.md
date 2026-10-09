# Data Processing and Specialized Stores

Batch and stream processing, search indexes, time-series, graph, and geospatial data systems.

[Back to the question-bank index](../README.md)

## Topic Map

- [Batch processing](#what-is-hadoop)
- [Stream processing](#what-is-stream-processing-and-when-is-it-used)
- [Specialized indexes and databases](#what-is-a-search-index-and-why-is-it-used)

## What is Hadoop?

**Answer**

Apache Hadoop is an ecosystem for distributed storage and batch processing of large datasets. Its
core projects include HDFS for replicated block storage, YARN for cluster resource management, and
MapReduce for batch computation. It influenced modern data platforms, though many deployments now
combine object storage with engines such as Spark, Flink, or cloud-managed services.

## What is HBase and how does it compare with Cassandra?

**Answer**

HBase is a wide-column database modeled after Bigtable and commonly built on HDFS. Region servers
host ordered key ranges, while HBase integrates with Hadoop components and provides strong row-level
consistency. Cassandra uses a peer-to-peer architecture, partition-key placement, and tunable
consistency across replicas. Compare access patterns, consistency, geographic topology, ecosystem,
failure handling, and operational skill; neither is a general relational replacement.

## What is MapReduce?

**Answer**

MapReduce is a distributed batch model. Map functions transform input records into intermediate
key/value pairs; the framework groups values by key through shuffle/sort; reduce functions aggregate
each group. It provides fault recovery and data-parallel scale but materializes stages and is awkward
for iterative or interactive workloads.

## How can batch jobs join large datasets?

**Answer**

Choose from data size and partitioning:

- A broadcast/map-side join sends a small input to workers and avoids a large shuffle.
- A repartition/sort-merge join shuffles both inputs by join key and merges colocated groups.
- A bucketed or colocated join reuses compatible pre-partitioning.
- A reduce-side hash join groups matching keys after shuffle.

Handle skewed keys, null semantics, duplicate multiplication, memory bounds, and output partitioning.

## What is Apache Spark and how does it differ from classic MapReduce?

**Answer**

Spark is a distributed computation engine with higher-level APIs for SQL, batch, streaming, machine
learning, and graphs. Its execution DAG can pipeline stages and reuse cached data rather than forcing
every map/reduce step through disk. It is often faster and more expressive for iterative workflows,
but shuffles, skew, memory pressure, serialization, and cluster tuning still matter.

## What is stream processing and when is it used?

**Answer**

Stream processing continuously evaluates events as they arrive, producing low-latency aggregates,
alerts, enrichments, or state updates. Examples include fraud detection, telemetry, clickstreams, and
change-data capture. Designs must define event time versus processing time, windows, watermarks,
late/out-of-order events, state recovery, delivery guarantees, and sink idempotency.

## How are joins performed in stream processing?

**Answer**

A stream-table join enriches events from a changing reference table. A stream-stream join usually
buffers both inputs within a bounded time window and matches keys. A temporal join uses the table
version valid at an event's time. Joins require partitioning compatible keys and bounding state with
windows, watermarks, or retention; late data and retractions need explicit semantics.

## What is Apache Flink?

**Answer**

Apache Flink is a distributed stateful stream-processing engine with event-time processing,
watermarks, windows, checkpointed state, and batch support over bounded streams. Exactly-once state
consistency depends on checkpointing and source/sink integration; external side effects still need
transactional or idempotent handling. Flink is useful when low-latency stateful pipelines justify its
operational complexity.

## What is a search index and why is it used?

**Answer**

A search index, commonly an inverted index, maps normalized terms to documents and positions. It
supports full-text matching, ranking, phrase queries, facets, and relevance features that ordinary
row scans do poorly. Indexing requires tokenization/analyzers, refresh policy, storage, and a strategy
for keeping the index consistent with the source of truth.

## What is Elasticsearch used for?

**Answer**

Elasticsearch is a distributed search and analytics engine built on Lucene. It is used for full-text
search, log/event exploration, aggregations, and observability workloads. Documents are divided into
shards and replicas; mappings and analyzers control indexing. Treat it as a derived search store when
transactional relational constraints are authoritative, and plan shard count, lifecycle, security,
and reindexing carefully.

## What is a time-series database?

**Answer**

A time-series database optimizes timestamped measurements, labels/tags, range scans, aggregation,
retention, and downsampling. Common workloads include metrics, industrial signals, and market data.
High-cardinality labels, out-of-order writes, compression, retention tiers, and query windows drive
design. Product models vary from purpose-built engines to relational time-series extensions.

## What is a graph database and why can graph traversal be efficient?

**Answer**

A graph database models vertices and edges with properties and provides traversal or pattern-query
operations. Native adjacency can follow relationships without repeatedly joining large tables, which
helps variable-depth paths, recommendations, fraud networks, and dependency graphs. It is not
universally faster: simple aggregates or tabular access may favor relational or columnar systems, and
high-degree nodes or distributed traversals can be expensive.

## What are geospatial indexes and why are they needed?

**Answer**

Geospatial indexes organize points, lines, or polygons so the engine can prune candidates for
containment, intersection, nearest-neighbor, and distance queries. Implementations include R-trees,
quadtrees, geohash/grid schemes, and space-filling curves. Correctness also depends on coordinate
reference systems, spherical versus planar distance, dateline/pole behavior, and exact geometry
checks after index filtering.

## References

- [Apache Hadoop documentation](https://hadoop.apache.org/docs/current/)
- [Apache Spark documentation](https://spark.apache.org/docs/latest/)
- [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
- [Elasticsearch reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
