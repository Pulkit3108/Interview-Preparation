# Scalability and Content Delivery

Distributed caches, object storage, CDNs, load balancing, and real-time delivery transports.

[Back to the question-bank index](../README.md)

## What is a distributed cache?

**Answer**

A distributed cache is a network-accessible cache shared by multiple application instances. It can
provide more aggregate capacity and cross-instance visibility than process memory, but adds network
latency, serialization, partitioning, eviction, and availability concerns. It is derived state, so
define behavior for misses, stale values, outages, stampedes, and recovery rather than making it a
new ungoverned source of truth.

## How are writes handled with a distributed cache?

**Answer**

Common patterns are cache-aside with invalidate/update after the authoritative commit, write-through
through a cache abstraction, and write-behind for asynchronous persistence. None makes two separate
systems atomic by default. Prevent stale repopulation races with versions, compare-and-set, ordered
events, or short bounded TTLs, and define partial-failure and retry semantics.

## What cache eviction policies should you know?

**Answer**

LRU approximates recency, LFU approximates frequency, FIFO removes oldest insertions, and random
eviction is cheap and sometimes effective. TTL expiry is freshness policy rather than capacity
eviction, though both remove entries. Real caches often use approximations. Select from workload and
measure hit rate, memory, churn, latency, and the cost of a miss.

## How do Redis and Memcached differ?

**Answer**

Memcached is a simple distributed in-memory key/value cache with a small command model and no native
durable data-structure workflows. Redis provides richer data structures, scripting/transactions,
streams, replication, persistence options, and clustering. Those features can support more use cases
but add operational and semantic complexity. Choose from required operations, consistency,
durability, memory efficiency, topology, and team expertise, not popularity alone.

## What is a content delivery network?

**Answer**

A CDN serves cacheable responses from geographically distributed edge locations, reducing latency,
origin load, and network transit. Cache keys, TTLs, invalidation, request variation, private content,
origin shielding, TLS, and failure behavior determine correctness. Some CDNs also run edge compute or
security controls, but those features are product-specific.

## What is object storage used for?

**Answer**

Object stores hold immutable or replaceable blobs addressed by keys with metadata. They suit images,
video, backups, logs, data-lake files, and build artifacts. They are not mounted filesystems or
relational databases: rename, append, directory, transaction, consistency, and request-cost semantics
differ. Use lifecycle, versioning, encryption, checksums, access policy, and multipart upload as the
workload requires.

## What is load balancing?

**Answer**

Load balancing distributes traffic across healthy backends using algorithms such as round robin,
least connections, weighted choice, or consistent hashing. Layer 4 balances transport connections;
Layer 7 can route by HTTP attributes. Correct design includes health checks, connection draining,
timeouts, retries, session affinity only when necessary, zone/region failure, TLS, and overload
protection.

## How do TCP and UDP differ?

**Answer**

TCP provides an ordered reliable byte stream with connection state, congestion control, and
retransmission. UDP sends independent datagrams without delivery or ordering guarantees and has lower
protocol overhead. Applications can build reliability over UDP; QUIC does so while supporting secure
multiplexed streams. Choose from loss, ordering, latency, congestion, message-boundary, and network
requirements rather than "TCP slow, UDP fast."

## How do long polling, WebSockets, and server-sent events differ?

**Answer**

- **Long polling:** the client holds an HTTP request until data or timeout, then reconnects. It works
  widely but adds repeated request overhead.
- **Server-sent events:** one long-lived HTTP response carries ordered text events from server to
  browser with built-in reconnection; client-to-server traffic uses separate requests.
- **WebSockets:** one upgraded connection carries bidirectional messages and needs application-level
  framing, authentication refresh, backpressure, reconnect, and scale-out routing.

Select from directionality, frequency, proxies, mobile behavior, message format, and operational cost.

## What is Ehcache?

**Answer**

Ehcache is a Java caching library that can provide in-process caches and, depending on version and
configuration, tiered or clustered capabilities. In Spring it can back the cache abstraction through
a compatible provider. Configure maximum size, expiry, serialization, statistics, and shutdown;
defaulting to an unbounded process-local cache can create memory and consistency problems.

## What is Hazelcast?

**Answer**

Hazelcast is a distributed in-memory data grid and stream-processing platform with partitioned maps,
queues, topics, locks and other distributed structures. It can embed in applications or run as a
client/server cluster. Partition ownership, backups, split-brain policy, serialization, memory
capacity, persistence, and consistency semantics must match the workload; a distributed map is not a
substitute for an authoritative database by default.

## References

- [Redis documentation](https://redis.io/docs/latest/)
- [Memcached documentation](https://docs.memcached.org/)
- [RFC 9293: TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768: UDP](https://www.rfc-editor.org/rfc/rfc768)
- [WebSocket standard](https://websockets.spec.whatwg.org/)
- [Ehcache documentation](https://www.ehcache.org/documentation/)
- [Hazelcast documentation](https://docs.hazelcast.com/)
