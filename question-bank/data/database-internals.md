# Database Internals and Distributed Data

Storage engines, indexes, transactions, replication, partitioning, consensus, and database
selection.

[Back to the question-bank index](../README.md)

## Topic Map

- [Storage engines and indexes](#what-are-common-building-blocks-for-database-storage-engines)
- [Transactions and concurrency](#what-do-the-acid-properties-mean)
- [Replication and partitioning](#what-is-database-replication)
- [Consensus and distributed ordering](#what-is-distributed-consensus)
- [Database selection and products](#how-do-you-choose-between-a-relational-and-a-nosql-database)

## What is a database?

**Answer**

A database is an organized collection of data managed for durable storage, retrieval, update, and
concurrent access. A database management system provides data models, query or access APIs,
transactions or other consistency guarantees, security, backup/recovery, and operational tooling.
Different systems optimize different workloads and guarantees.

## What objectives should a database design balance?

**Answer**

The design balances correctness and integrity, durability and recovery, read/write latency and
throughput, concurrency, availability, security, operability, scalability, and cost. These objectives
conflict: an extra index can accelerate reads but increase write and storage cost; synchronous
replication can reduce data loss but increase latency or reduce write availability.

## What are common building blocks for database storage engines?

**Answer**

Simple designs illustrate the trade-offs:

- An unsorted file or array is easy to append but requires a scan for many reads.
- An append-only log makes writes sequential but needs indexing and compaction for efficient reads.
- A hash index provides efficient equality lookup but no natural ordered range scan.
- A B-tree-family index maintains order for point and range queries with page-update cost.
- An LSM-tree buffers writes and flushes immutable sorted runs, trading compaction and read
  amplification for high sequential write throughput.

Complexity notation alone is insufficient because page I/O, cache behavior, concurrency, durability,
and amplification dominate real storage engines.

## Why do hash indexes work best when their index fits in memory?

**Answer**

Hash lookup maps a key to a bucket without preserving order. If the bucket directory and hot chains
fit in memory, lookup needs few random accesses. When they do not, collisions and random page reads
can cause expensive storage I/O and poor cache locality. Disk-backed hash indexes still exist and can
be durable; fitting entirely in memory is an optimization, not a correctness requirement. Hash
indexes are also unsuitable for ordered range scans.

## What is write-ahead logging?

**Answer**

Write-ahead logging records the information needed to redo or undo a change in durable log order
before the corresponding data page is considered persisted. After a crash, recovery uses the log to
restore a transactionally valid state. WAL also supports replication and point-in-time recovery in
some systems, but exact record, flush, checkpoint, and recovery behavior is engine-specific.

## What is a database index?

**Answer**

An index is an auxiliary access structure that maps searchable keys to rows or storage locations. It
can avoid a full scan and may support joins, ordering, uniqueness, or covering a query. Indexes cost
storage, cache space, and work on inserts, deletes, and updates, so choose them from actual access
patterns and execution plans.

## How do indexes reduce data retrieval work?

**Answer**

An ordered or hashed structure narrows the set of candidate pages before the engine reads base rows.
A covering index may answer a query without visiting the table at all. Effectiveness depends on
selectivity, leading-column order, predicate form, clustering, statistics, and whether the optimizer
estimates that an index path is cheaper than a scan.

## What are the advantages and limitations of hash indexes?

**Answer**

Hash indexes are effective for equality predicates and can offer near-constant expected lookup cost
under a good distribution. They do not maintain key order, so range predicates, ordered scans, and
prefix searches normally need another structure. Collision handling, resizing, concurrency,
durability, and recovery are implementation concerns; a hash index is not inherently in-memory or
non-durable.

## What is a B-tree?

**Answer**

A B-tree is a balanced multiway search tree designed to keep its height small by storing many keys
per page. Search, insertion, and deletion traverse logarithmically many levels; splits, merges, or
redistribution preserve balance. Its high fan-out reduces random page reads and its ordered keys
support range scans.

## How does a B+ tree differ from a B-tree?

**Answer**

A B+ tree keeps navigation keys in internal pages and stores record references or values at the leaf
level. Leaves are commonly linked for efficient ordered scans. Database implementations vary in page
layout, prefix compression, duplicate handling, and concurrency, but the shallow ordered structure is
the important interview concept.

## Why are B+ tree nodes sized around storage pages?

**Answer**

Aligning a node with the database or storage page lets the engine fetch useful keys with one page I/O
and gives high fan-out, reducing tree height. The exact size is not universally the physical disk
block size; engines choose page sizes around I/O, cache, write-amplification, and record-layout
trade-offs, and one logical page can span physical sectors.

## What are an LSM-tree and an SSTable?

**Answer**

An LSM-tree records writes in a WAL and mutable in-memory table, then flushes sorted immutable files,
often called SSTables. Reads consult memory and relevant files using indexes and Bloom filters.
Background compaction merges runs and discards obsolete versions.

This design turns many writes into sequential I/O but introduces read, write, and space amplification,
compaction CPU/I/O, and tail-latency trade-offs. Range queries are supported because SSTables are
sorted, though reads may consult several levels or runs.

## What types of database indexes should you know?

**Answer**

Common categories include clustered or index-organized storage, secondary/nonclustered indexes,
unique indexes, composite indexes, covering/include-column indexes, filtered/partial indexes,
function/expression indexes, full-text/inverted indexes, bitmap indexes, and spatial or other
specialized multidimensional indexes. Names and capabilities differ by database. "Multi-level" is a
property of tree indexes, not usually a separate user-selected type.

## What do the ACID properties mean?

**Answer**

- **Atomicity:** a transaction's changes commit as one unit or do not commit.
- **Consistency:** committed transactions preserve declared application and database invariants.
- **Isolation:** concurrent execution provides a documented equivalence or visibility model.
- **Durability:** acknowledged commits survive the failures covered by the system's guarantee.

ACID does not mean there are no races, and WAL alone does not provide every property.

## What concurrency anomalies can database transactions encounter?

**Answer**

Examples include dirty writes, dirty reads, non-repeatable reads, read skew, lost updates, phantom
rows, and write skew. Which anomalies are possible depends on the database's isolation implementation,
not only the SQL level's name. Prevent them with atomic conditional writes, constraints, locks,
serializable execution, conflict detection, or redesigned invariants as appropriate.

## What are database locks?

**Answer**

Locks coordinate conflicting access to logical or physical resources such as rows, keys, pages,
tables, or predicates. Lock modes and compatibility determine which transactions may proceed. Locks
can protect invariants but introduce waiting, deadlocks, and contention; MVCC reduces some reader/
writer blocking but does not eliminate all locking.

## What lock types are commonly used?

**Answer**

Shared/read locks permit compatible readers; exclusive/write locks exclude conflicting access.
Intent locks coordinate granular row/page locks with table-level operations. Update locks in some
engines reduce conversion deadlocks. Range or predicate locks protect a set of possible rows and help
prevent phantoms. Exact modes, granularity, escalation, and MVCC interaction are database-specific.

## What are database isolation levels?

**Answer**

SQL names include Read Uncommitted, Read Committed, Repeatable Read, and Serializable, but engines
implement them differently. Snapshot Isolation gives a transaction a consistent snapshot and detects
some write conflicts, yet can permit write skew and is not synonymous with Repeatable Read or
Serializable. Evaluate the concrete anomalies and guarantees of the target database.

## What is actual serial transaction execution?

**Answer**

Executing transactions one at a time on one partition provides serial behavior without concurrency
control between them. In-memory, stored-procedure-style systems can make each transaction short and
avoid network pauses. Partitioning can add parallelism for disjoint data, while cross-partition
transactions need coordination and lose much of the simplicity.

## What is two-phase locking?

**Answer**

In two-phase locking, a transaction has a growing phase in which it acquires but does not release
locks, followed by a shrinking phase in which it releases but acquires no new locks. 2PL provides
conflict serializability; strict variants hold write or all locks until commit/abort for stronger
recovery behavior. Deadlocks remain possible and require prevention, detection, or timeout.

## What is serializable snapshot isolation?

**Answer**

Serializable Snapshot Isolation starts from snapshot/MVCC execution and tracks dependency patterns
that could form a non-serializable cycle. It aborts a transaction when necessary to preserve
serializability. PostgreSQL is a well-known implementation. SSI can reduce blocking but may require
application retries; it is not universally better than 2PL, and workload behavior determines the
trade-off.

## What is column-oriented storage?

**Answer**

Columnar storage keeps values from each column together, letting analytical queries read only needed
columns and compress similar values effectively. It is well suited to scans and aggregations; point
updates and reconstructing complete rows can be more expensive. Columnar analytical storage should
not be confused with wide-column data models such as Cassandra, whose on-disk implementation and API
serve different goals.

## What is predicate pushdown?

**Answer**

Predicate pushdown moves eligible filters closer to the storage scan or remote source so fewer rows
and bytes flow through later operators. Partition metadata, file statistics, indexes, or a remote
database may eliminate work. It is limited by expression support, semantics, and optimizer ability;
the execution plan should confirm it occurred.

## What are data serialization frameworks?

**Answer**

Serialization encodes data for storage or transport and later reconstruction. JSON and XML are
self-describing text formats; Protocol Buffers, Avro, Thrift, and MessagePack offer different schema,
compatibility, size, and tooling trade-offs. Choose with version evolution, unknown-field handling,
language support, human readability, security, and performance in mind. Never deserialize untrusted
native object formats without strict controls.

## What is database replication?

**Answer**

Replication maintains copies of data on multiple nodes for availability, read scale, locality, or
disaster recovery. Synchronous acknowledgement can reduce acknowledged data loss at latency and
availability cost; asynchronous replication improves write latency but permits lag and potential loss
during failover. Replication does not replace backups and does not automatically make stale reads
safe.

## How can database changes be replicated?

**Answer**

Engines commonly ship physical page/WAL records, logical row changes, or a deterministic command log.
Statement replication can diverge when statements depend on time, randomness, ordering, or local
state. Snapshot/bootstrap establishes a base copy, then a change stream catches it up. Choose with
engine compatibility, schema evolution, bandwidth, failover, and recovery goals in mind.

## How can a system improve the user experience under eventual consistency?

**Answer**

Provide read-your-writes by reading from the leader, carrying a session/version token, or waiting
until a replica reaches the write's position. Sticky routing can provide monotonic reads but fails
over imperfectly. Causal metadata can preserve dependencies, while conflict resolution handles
concurrent writes. Expose pending state when appropriate and bound or monitor replica lag instead of
claiming "eventual" without a time expectation.

## What is primary-replica replication?

**Answer**

One primary/leader accepts writes and emits an ordered replication stream to followers/replicas.
Followers may serve reads subject to lag. This simplifies write ordering but makes leader failover,
split-brain prevention, read consistency, and write capacity central design concerns. Prefer current
terms such as primary/replica or leader/follower.

## What is sharding?

**Answer**

Sharding horizontally distributes rows or keys across independently operated partitions or database
nodes. Range, hash, directory, geographic, or tenant-based placement can be used. The shard key
determines locality, balance, and query routing. Sharding expands capacity but complicates secondary
indexes, uniqueness, joins, transactions, resharding, hot keys, backup, and operations.

Local and global secondary indexes are product-specific ways to query by non-primary attributes;
their scope and consistency must be described for the named database rather than as universal
sharding concepts.

## What is database partitioning?

**Answer**

Partitioning divides one logical dataset into pieces by range, list, hash, or another rule. Partitions
may remain inside one database instance for pruning and lifecycle management, while sharding usually
places partitions across independently scaled nodes. Queries benefit only when predicates align with
the partition key; poor keys create skew or expensive cross-partition work.

## What is single-leader replication?

**Answer**

A single leader orders all writes for a replicated dataset and followers apply its log. It offers a
clear conflict/order model and can scale some reads, but leader throughput, replication lag, and
failover remain constraints. It is the general distributed-systems form of primary-replica
replication.

## What can happen when a replication leader fails?

**Answer**

Writes pause while failure detection and leader election occur. A stale follower may lack acknowledged
asynchronous writes; an old leader returning without fencing can create split brain. Safe failover
needs a quorum or other authority to choose one sufficiently current leader, increment a term/epoch,
fence the former leader, redirect clients, and reconcile or report any lost/uncommitted writes.

## What is distributed consensus?

**Answer**

Consensus lets non-faulty nodes agree on one value or ordered log despite failures and message delay,
under a defined fault model. Algorithms such as Raft and Paxos use quorums and terms/ballots to
maintain safety. They cannot guarantee progress through arbitrary network partitions without enough
reachable members, and they do not solve application-level conflicts automatically.

## What is multi-leader replication?

**Answer**

Multiple leaders accept writes, often in different regions or disconnected sites, and replicate
between them. It improves local write availability and latency but permits concurrent conflicts.
Designs need conflict detection/resolution, unique ID strategy, topology, loop prevention, and clear
semantics for operations that cannot be merged safely.

## What are CRDTs?

**Answer**

Conflict-free Replicated Data Types have merge rules that guarantee replicas converge when they have
received the same updates, despite reordering or duplication. State-based CRDTs merge monotonic
states; operation-based variants require delivery assumptions. CRDTs solve convergence for modeled
data types, not arbitrary business invariants, authorization, or causally correct user experiences.

## What is leaderless replication?

**Answer**

In a leaderless design, clients or coordinators write to and read from multiple replicas rather than
one elected write leader. Quorum reads/writes, read repair, hinted handoff, and anti-entropy can improve
availability and convergence. Concurrent versions and sloppy quorums mean conflict resolution and
consistency are more nuanced than the simple equation `R + W > N` suggests.

## What are Merkle trees used for in distributed storage?

**Answer**

A Merkle tree hashes blocks of data into a hierarchy whose root summarizes the dataset. Replicas can
compare hashes to locate differing subranges without transferring every record, making them useful
for anti-entropy and integrity verification. The tree's partitioning and rebuild/update strategy
determine its cost and granularity.

## What are quorums?

**Answer**

A quorum is a subset large enough to make a decision or overlap with another required subset. In
consensus, majority quorums ensure two committed majorities intersect. In Dynamo-style storage,
`N`, `W`, and `R` describe replication and response counts, but overlapping counts do not alone
guarantee linearizability because timing, failures, sloppy placement, and conflict handling matter.

## What is two-phase commit?

**Answer**

Two-phase commit coordinates an atomic outcome across participants. In prepare, each participant
durably promises it can commit; in commit/abort, the coordinator announces the decision. It provides
atomic commit, not consensus, and can block when the coordinator's decision is unavailable. Recovery,
timeouts, heuristic outcomes, and participant support are operational concerns.

## What is a cross-partition write?

**Answer**

A cross-partition write updates data owned by more than one partition. It requires coordination for
atomicity or a workflow for eventual consistency, adds latency and failure modes, and may limit
availability during partitions. Good keys colocate data that must change together; unavoidable
cross-partition operations need explicit idempotency, ordering, recovery, and consistency semantics.

## How do three-phase commit and sagas differ?

**Answer**

Three-phase commit adds a pre-commit phase and timing assumptions to reduce some 2PC blocking, but it
does not tolerate arbitrary partitions and is uncommon in modern application systems. A saga is not
an atomic commit protocol: it sequences local commits and uses compensating business actions on
failure, exposing intermediate and eventual states.

## What hashing schemes are used for partitioning?

**Answer**

Modulo hashing is simple but remaps most keys when shard count changes. Consistent hashing places
nodes and keys on a ring and limits movement; virtual nodes improve balance. Rendezvous/highest-random-
weight hashing selects the highest-scoring node and is easy to compute. Real systems also use fixed
hash slots, directories, or range maps to make rebalancing and heterogeneous capacity controllable.

## What is consistent hashing?

**Answer**

Consistent hashing maps keys and nodes into a hash space and assigns each key to the next eligible
node. Adding or removing a node moves only a portion of keys rather than nearly all of them. Virtual
nodes or weighted placement improve balance. Replication, hot keys, membership agreement, and data
movement still require separate design.

## What are Lamport timestamps, vector clocks, and version vectors?

**Answer**

A Lamport clock assigns scalar timestamps so causal order implies timestamp order, but a larger
timestamp does not prove causality. A vector clock tracks a counter per participant and can distinguish
causal order from concurrency, at metadata cost. A version vector adapts that idea to versions per
replica or actor for replicated data. None is a synchronized wall clock.

## What is linearizability?

**Answer**

Linearizability is a single-operation consistency model: each completed operation appears to take
effect atomically at some point between invocation and response, respecting real-time order. It makes
a distributed object behave like one current copy. It is stronger than sequential or eventual
consistency and may reduce availability or increase latency during faults. Transactions additionally
need isolation semantics across multiple operations.

## What is Raft?

**Answer**

Raft is a crash-fault-tolerant consensus algorithm for replicating a state-machine log. Nodes are
followers, candidates, or leaders and operate in monotonically increasing terms. A leader appends
commands, replicates them to a majority, and advances the commit index under Raft's term rules. Raft
requires a quorum for progress and does not tolerate Byzantine behavior.

## How does Raft elect a leader?

**Answer**

A follower that receives no valid leader communication before a randomized election timeout becomes
a candidate, increments its term, votes for itself, and requests votes. A node grants at most one vote
per term and only to a candidate whose log is at least as up to date. A majority elects the leader;
split votes retry in a later term with randomized timeouts.

## How does a write proceed in Raft?

**Answer**

The leader appends the command to its log and sends AppendEntries to followers. Once an entry from the
leader's current term is stored on a majority, the leader can mark it committed, apply it to the state
machine, and respond according to the system's durability policy. Followers learn the commit index
and apply entries in order. Conflicting uncommitted suffixes are repaired to match the leader.

## What are coordination services?

**Answer**

Systems such as ZooKeeper and etcd provide a small, strongly consistent namespace for coordination:
membership, configuration, leader election, locks, and watches. They are not general high-volume
application databases. Correct clients must understand sessions/leases, fencing, watch races,
ephemeral state, quorum availability, and size limits.

## What does `sync` do in ZooKeeper?

**Answer**

ZooKeeper's `sync(path, callback, context)` asks the connected server to synchronize with the leader
before completing the callback. A subsequent read through that server can observe state at least as
new as the synchronization point. It is not a filesystem flush and does not turn a multi-operation
client workflow into a transaction. Confirm semantics against the ZooKeeper version in use.

## How do you choose between a relational and a NoSQL database?

**Answer**

Start from access patterns, invariants, transaction scope, relationship/query needs, scale, latency,
availability, geographic placement, schema evolution, and operational skill. Relational databases
excel at declarative queries, constraints, joins, and transactions. NoSQL families offer specialized
key-value, document, wide-column, graph, or search models and scaling trade-offs. "NoSQL" is not one
consistency model, and a relational database often handles far more scale than assumed.

## How do MySQL and PostgreSQL differ?

**Answer**

Both are mature open-source relational systems with ACID transactions, replication, indexing, JSON,
and large ecosystems. PostgreSQL emphasizes extensibility, rich SQL/types, MVCC, and extensions;
MySQL, commonly with InnoDB, has broad hosting/tooling adoption and its own replication and operational
strengths. The right comparison is version- and workload-specific: test query plans, HA topology,
backup/recovery, migration tooling, compatibility, and team expertise rather than using a blanket
winner.

## What is VoltDB and why was it called a NewSQL database?

**Answer**

VoltDB is a distributed relational database descended from H-Store ideas. It partitions data and can
execute stored transactions serially within a partition, with coordination for multi-partition work.
"NewSQL" described systems seeking relational/SQL and ACID semantics with scale-out architecture.
Product capabilities and licensing evolve, so use current documentation for deployment decisions.

## What is Google Cloud Spanner and what makes it distinctive?

**Answer**

Spanner is Google's distributed relational database service. It combines synchronous replication,
SQL schemas/queries, horizontal partitioning, and externally consistent transactions. TrueTime
provides bounded clock uncertainty used by its commit protocol to respect real-time ordering. These
guarantees carry latency, schema/key-design, operational, and cost trade-offs; they are not simply
"SQL with unlimited scale."

## How do MongoDB and Apache Cassandra differ?

**Answer**

MongoDB is a document database organized around BSON documents, flexible schemas, indexes, and
document-oriented queries/aggregations; it also supports replica sets, sharding, and transactions.
Cassandra is a distributed wide-column database designed around partition-key access, tunable
consistency, peer replication, and high write availability/throughput. Choose from modeled queries,
transaction needs, partition sizes, consistency, topology, and operational behavior, not from the
generic label "NoSQL."

## References

- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [PostgreSQL Serializable Snapshot Isolation](https://www.postgresql.org/docs/current/applevel-consistency.html)
- [Raft paper](https://raft.github.io/raft.pdf)
- [ZooKeeper programmer's guide](https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html)
- [Cloud Spanner documentation](https://cloud.google.com/spanner/docs)
