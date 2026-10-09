# System Design

Scalability, distributed systems, data stores, caching, reliability, and architecture exercises.

[Back to the question-bank index](../README.md)

## Topic Map

- [Database storage, indexes, and transactions](#what-is-a-database)
- [Replication, partitioning, consensus, and distributed time](#what-is-database-replication)
- [Batch processing, stream processing, and joins](#what-is-hadoop)
- [Search, time-series, graph, and geospatial stores](#what-are-search-indexes-and-why-do-we-need-them)
- [Caching, CDNs, object storage, and load balancing](#what-is-distributed-caching)
- [Communication and service architecture](#explain-a-bit-about-tcp-vs-udp)
- [API performance and interview method](#how-can-you-optimize-the-performance-of-a-high-performing-api-to-ensure-a-great-user-experience-and-efficient-application-operation)
- [URL-shortener design exercise](#how-would-you-design-a-url-shortening-service)

## What is a system design?

**Answer**

System design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. The main points of system design are:
Scalability: Ensuring the system can handle increased load by adding resources.
Reliability: Ensuring the system operates correctly and consistently over time.
Maintainability: Making the system easy to maintain and update.
Performance: Ensuring the system meets performance requirements, such as response time and throughput.
Security: Protecting the system and its data from unauthorized access and breaches.
Cost-effectiveness: Balancing the cost of development and operation with the benefits provided.
Usability: Ensuring the system is user-friendly and meets user needs.

## What is a database?

**Answer**

A database is an organized collection of data that is stored and accessed electronically. Databases are designed to manage large amounts of information by storing, retrieving, and managing data efficiently.
Databases are managed by Database Management Systems (DBMS) which provide tools for data manipulation, querying, and administration.

## What are the Objectives of Database

**Answer**

Fast Reads: Ensure that data can be retrieved quickly and efficiently.
Fast Writes: Allow data to be inserted, updated, and deleted rapidly.
Persistent Data: Ensure that data is stored securely and reliably.
Data Integrity: Maintain accuracy and consistency of data.
Data Security: Protect data from unauthorized access and breaches.
Data Accessibility: Provide easy and efficient access to data for authorized users.
Data Sharing: Enable multiple users and applications to share data concurrently.
Data Independence: Allow changes to data structure without affecting applications.
Data Redundancy Reduction: Minimize duplicate data to save storage and maintain consistency.
Data Recovery: Provide mechanisms for data backup and recovery in case of failures.
Performance Optimization: Ensure fast query processing and efficient data retrieval.
Scalability: Allow the database to grow and handle increasing amounts of data and users.

## What are the different ways of Database Implementation?

**Answer**

Array: Read is O(n), Update is O(n); suitable for small datasets.
Append Only Log: Read is O(n), Update is O(1); Always search from bottom to top; but it will have more rows, useful for logging purposes.
Hashmap: Read is O(1), Update is O(1); efficient for lookups if the whole hashmap can fit in memory.
Indexing: Read is O(log n), Update is O(log n); keep extra data on each write to improve read performance, but write will take more time.

## Why Hashmaps are only good if they fit in memory?

**Answer**

Hashmaps are efficient for lookups because they use a hash function to map keys to specific memory locations. When the entire hashmap fits in memory, accessing an element is a quick, constant-time operation (O(1)) because the memory address can be directly computed and accessed.
However, if the hashmap exceeds the available memory and parts of it are stored on the hard disk, performance degrades significantly. This is due to the following reasons:
Disk Access Time: Accessing data on a hard disk is much slower than accessing data in memory. The hard disk's read/write head (rotator arm) needs to move to the correct location on the disk, which introduces latency.
Random Access Penalty: Hashmaps store data in a non-contiguous manner, which means that accessing elements can involve multiple random accesses. On a hard disk, this results in the read/write head moving frequently to different locations, further increasing access time.
Range Queries: Hashmaps are not optimized for range queries. Since data is stored based on hash values, elements that are close in terms of key values may be scattered across the disk. This scattering causes the read/write head to move around a lot, making range queries inefficient.

## What is WAL (Write Ahead Log)?

**Answer**

Write-Ahead Logging (WAL) is a technique used in databases to ensure data integrity and durability. Changes are first written to a log before being applied to the database. This log allows the system to recover and maintain consistency in case of a crash.

## What is Indexing?

**Answer**

Indexing is a technique used in databases to improve the speed of data retrieval. It involves creating a data structure, that allows for quick lookups, updates, and deletions. Indexes are created on one or more columns of a table to enable efficient access to rows based on key values. But this might increase data insertion time.

## How do indexes improve data retrieval efficiency in relational databases?

**Answer**

Data is read in terms of blocks. Traditionally, without indexing, reading data involves fetching each block one by one and checking if it contains the desired value, resulting in multiple disk I/O operations.
Indexes are smaller referential tables that hold row references against the index values. The column on which indexing is applied will have its values sorted and indexed. Each indexed value is mapped to the row ID or the corresponding row where it is located. These indexed values are stored on disk and occupy less space, requiring fewer I/O operations to read. This allows for quick identification of the row IDs of interest, enabling direct access to the blocks containing the desired rows, thus improving data retrieval efficiency.

## What are the pros and cons of Hash Indexes?

**Answer**

Pros:
O(1) Reads and Writes in Memory: Hash indexes provide constant-time complexity for read and write operations when the entire index fits in memory.
Cons:
Key Must Fit in Memory: The entire hash index must fit in memory for optimal performance.
No Durability: By default, hash indexes do not provide durability.
Using WAL with Hash Indexes:
Durability and Recoverability: Write-Ahead Logging (WAL) ensures that changes to hash indexes are durable and recoverable, maintaining data integrity and consistency.
No Range Queries: Hash indexes are not suitable for range queries, as they do not maintain any order of keys.
O(n) Time for Range Queries: Even if the hash index is in memory, performing range queries will take O(n) time, as it requires scanning all entries.

## What are B-Trees?

**Answer**

B-trees are balanced tree data structures used in databases and file systems to maintain sorted data and allow for efficient insertion, deletion, and search operations. Each node in a B-tree can have multiple children and keys, ensuring that the tree remains balanced and operations can be performed in logarithmic time, O(log n).
Constraints of B-trees:
Order (m): Each node can have at most m children and at least ceil(m/2) children, except for the root.
Keys per Node: Each node can contain at most m-1 keys and at least ceil(m/2) - 1 keys, except for the root.
Root Node: The root node must have at least 2 children if it is not a leaf node.
Balanced: All leaf nodes are at the same depth, ensuring the tree remains balanced.
Sorted Keys: Keys within each node are sorted in ascending order.
Node Splitting: When a node exceeds the maximum number of keys, it splits into two nodes, and the middle key is promoted to the parent node.
Advantages of B-trees
Range Queries: B-trees support efficient range queries. Since keys within each node are sorted, it is easy to traverse the tree and retrieve all keys within a specified range.
Efficient Disk Access: B-trees are designed to minimize disk I/O operations. By storing multiple keys in each node, B-trees reduce the number of disk accesses required to find a particular key, making them ideal for database and file system implementations.
Disadvantages of B-trees:
Rebalancing Overhead: Although B-trees are designed to minimize rebalancing, the process of splitting and merging nodes during insertions and deletions can still introduce overhead, especially in scenarios with frequent updates.

## What is B+ trees?

**Answer**

B+ Trees are a balanced tree data structure optimized for efficient insertion, deletion, and search operations. They extend B-trees by storing keys in internal nodes and actual data in leaf nodes, which are linked together for efficient sequential access and range queries. B+ Trees are widely used in databases and file systems to maintain sorted data and ensure efficient data retrieval

## Why size of B+ Tree node is kept same as disk block size?

**Answer**

**When performing any disk I/O, the most granular unit of data transfer is called the disk block size, which is often 4 KB.**

Efficient Disk I/O: Minimizes the number of disk reads/writes by aligning node size with disk block size.
Reduced Latency: Ensures nodes can be read or written in a single I/O operation, reducing latency.
Improved Cache Efficiency: Enhances disk block caching by matching node size to disk block size.
Simplified Management: Simplifies the management of nodes and disk blocks with consistent node size.

## What are LSM tree and SSTable?

**Answer**

Log-Structured Merge Trees (LSM Trees) are data structures optimized for high write throughput and efficient management of large volumes of data. They use an in-memory structure (often a balanced tree) to handle writes quickly. Changes are first recorded in a Write-Ahead Log (WAL) to ensure durability. When the in-memory structure becomes too large, it is flushed to disk as an immutable, sorted table known as an SSTable. LSM Trees periodically merge and compact these SSTables to maintain performance and reduce storage overhead.
Sorted String Tables (SSTables) are immutable, sorted files used to store key-value pairs on disk. They are created by flushing the in-memory structure of an LSM Tree to disk. SSTables are designed for efficient sequential reads and range queries. They are often used in conjunction with bloom filters and sparse indexes to optimize read performance. Periodic compaction merges SSTables to remove duplicates and maintain sorted order, ensuring efficient data retrieval.
Advantages:
Number of Keys Not Limited to Memory: Can handle large datasets by flushing data to disk.
Faster Writes Compared to B-trees: Write-optimized structure with sequential disk writes.
Support Range Queries: Range queries are supported, with optimizations like bloom filters and sparse indexes.
Disadvantages:
Slower Writes Compared to Hash Indexes: Generally slower than hash indexes for writes.
Range Queries Slower Compared to B-trees: May require checking multiple SSTables.
Extra CPU Usage for Table Compaction: Compaction is CPU-intensive and adds overhead.
Read and Write Amplification: Higher read and write amplification due to multiple SSTables and compaction.
Latency: Potentially higher read and write latencies.
Note:
Sparse Index: Also known as index for SSTable take “certain” keys of SSTable and create a sparse index with corresponding stored memory location.
LSM tree is the name industry gives to the entire structure
The in memory BST part is called the "memtable"
That is, memtable + SSTables  + Bloom filter == LSM Tree

## What are different type of indexes on table?

**Answer**

Clustered Index is a type of database index that determines the physical order of data in a table. In a table with a clustered index, the rows are stored on disk in the same order as the index. This means that the table data is sorted and stored according to the indexed column(s).
Non-clustered Index, the index contains a mapping of the value of the indexed column to the address (or pointer) of the corresponding row in the disk, rather than the entire row. This helps reduce data duplication and allows for efficient data retrieval.
Covering Index is an index that contains all the columns needed to satisfy a particular query, meaning the query can be answered entirely using the index without having to access the actual table data.
Multi-dimensional Index is a type of database index designed to handle queries involving multiple dimensions or attributes. It is commonly used in spatial databases, geographic information systems (GIS), and applications requiring multi-dimensional data retrieval, such as range queries and nearest neighbor searches.
Composite Index (also known as a multi-column index) is an index that includes multiple columns from a table. It allows for efficient querying based on combinations of the indexed columns.
Multi-Level Index is a hierarchical indexing technique used in databases to manage large indexes efficiently. It involves creating multiple levels of indexes to reduce the number of disk I/O operations required to locate a data record.

## What are ACID Database Transactions?

**Answer**

Atomicity: Ensures that all operations within a transaction are completed successfully. If any operation fails, the entire transaction is rolled back.
Consistency: Ensures that a transaction brings the database from one valid state to another, maintaining database invariants.
Isolation: Ensures that transactions are executed in isolation from one another, preventing concurrent transactions from interfering with each other. No Race Conditions
Durability: Ensures that once a transaction is committed, its changes are permanent, even in the event of a system failure.
Race Conditions occur when the behavior of software depends on the relative timing of events, such as the order in which threads or processes execute. This can lead to unpredictable and incorrect outcomes when multiple threads or processes access shared resources concurrently without proper synchronization.
Deadlock occurs when two or more processes or threads are unable to proceed because each is waiting for the other to release a resource. This results in a situation where none of the processes can continue execution.
Write-Ahead Log (WAL) can help achieve atomicity, consistency, and durability in database transactions.

## What are different database race condtions?

**Answer**

Dirty Write is when one transaction overwrites uncommitted changes made by another transaction, leading to potential data inconsistency.
Dirty Read is when a transaction reads uncommitted changes made by another transaction, which can lead to data inconsistency if the changes are later rolled back.
Read Skew/Non-Repeatable Read: Occurs when a transaction reads the same data multiple times and finds different values due to concurrent modifications by another transaction.
Lost Updates: A race condition where concurrent transactions read the same data and independently update it, resulting in one transaction's changes being overwritten by another.

**Can be prevented using Atomic write operations, Explicit locking, Automatically detecting lost updates, Compare-and-set**

Write Skew: An anomaly where two or more transactions read overlapping sets of data and make conflicting updates based on those reads, leading to an inconsistent state.
Phantoms/Phantom reads are a type of anomaly in database transactions where a write operation in one transaction changes the result of a search query in another transaction. This typically occurs when the initial query checks for the absence of rows (e.g., no existing bookings, no existing users with the same username). Since there are no rows to lock, subsequent writes can add new rows that affect the result of the initial query, leading to inconsistencies and write skew. This is particularly challenging in scenarios where the presence or absence of rows affects the transaction's logic.

**Can be prevented using Materializing conflicts**

## What are Locks in DB

**Answer**

Database locks are mechanisms that prevent multiple transactions from simultaneously modifying the same data or reading data that is being modified by another transaction. They are used to secure shared resources during transactions and help maintain the ACID properties

## What are different types of locks?

**Answer**

A predicate lock is a type of lock used in database systems to ensure serializability by locking a set of rows that satisfy a certain condition (predicate) rather than locking individual rows or tables. This type of lock is particularly useful for preventing phantom reads in transactions.
Shared locks allow concurrent read access to a data item, while exclusive locks ensure exclusive read and write access, preventing other transactions from accessing the data item concurrently.
Index range locking is a concurrency control mechanism used in database systems to lock a range of index entries, ensuring that no other transactions can insert, update, or delete rows within that range. This type of locking is particularly useful for preventing phantom reads and ensuring serializable isolation.

## What are Isolation levels in DB?

**Answer**

Isolation levels are rules that control how concurrent transactions access data, and are used to maintain the ACID properties of the database.
Weak isolation refers to a set of database transaction isolation levels that provide less stringent guarantees about the visibility and ordering of operations.
Read Uncommitted: The lowest level, which can retrieve data that has been modified but not yet committed by other transactions. This level has no read locking or versioning, so it minimizes overhead but can cause concurrency side effects.
Read Committed isolation is a transaction isolation level that ensures transactions only read data that has been committed by other transactions, preventing dirty reads. It also ensures that transactions only overwrite data that has been committed, preventing dirty writes. This level of isolation is commonly implemented using row-level locks for writes and a snapshot mechanism for reads, balancing data consistency with performance.
Snapshot Isolation and Repeatable Read: Snapshot Isolation, often referred to as Repeatable Read in databases like PostgreSQL and MySQL, is a transaction isolation level that ensures each transaction operates on a consistent snapshot of the database, reflecting the state at the start of the transaction. This prevents anomalies like nonrepeatable reads and read skew by using Multiversion Concurrency Control (MVCC), which maintains multiple versions of data. Readers never block writers, and writers never block readers, allowing for high concurrency and consistent snapshots for long-running read queries. This level of isolation provides strong consistency guarantees and is widely supported by modern databases.
Strong isolation refers to a level of isolation in database systems that ensures transactions are executed in such a way that they appear to be executed sequentially, even if they are executed concurrently. This guarantees that the outcome of executing transactions concurrently is the same as if the transactions were executed one after another in some order.
Serializability: The highest isolation level, ensuring that transactions are serializable, meaning they produce the same result as some serial execution of those transactions, preventing dirty reads, non-repeatable reads, and phantom reads.

## What is Actual Serial Execution

**Answer**

Actual Serial Execution refers to the process of executing database transactions one at a time, in a serial order, on a single thread. This approach avoids concurrency issues by ensuring that no two transactions are processed simultaneously, thus inherently providing serializable isolation.
For Perfomance Improvement:
Stored Procedures: Often used to encapsulate transactions to avoid the overhead of interactive multi-statement transactions and network communication delays.
In-Memory Data: Feasible due to the availability of cheap RAM, allowing the entire active dataset to be kept in memory for faster transaction execution.
Partitioning: To scale beyond a single CPU core, data can be partitioned so that each partition has its own transaction processing thread. However, cross-partition transactions require coordination and are significantly slower.

## What is Two Phase Locking?

**Answer**

Two-Phase Locking (2PL) [Pessimistic Concurrency Control] is a concurrency control method used in database systems to ensure serializability of transactions. It operates in two distinct phases:
Growing Phase: During this phase, a transaction can acquire locks (shared or exclusive) on data items but cannot release any locks.
The transaction continues to acquire all the locks it needs for its operations.
Shrinking Phase: Once the transaction releases its first lock, it enters the shrinking phase. During this phase, the transaction can release locks but cannot acquire any new locks.
2PL can lead to deadlocks, where two or more transactions are waiting indefinitely for each other to release locks. So, system has to detect them and abort some transactions then retry.

## What is Serializable Snapshot Isolation?

**Answer**

Serializable Snapshot Isolation (SSI) [Optimistic Concurrency Control] combines the performance benefits of snapshot isolation with the strong guarantees of serializable isolation. It ensures that transactions are executed in a way that they appear to be serial, preventing all types of read anomalies while maintaining high concurrency and performance
Snapshot Isolation: Each transaction operates on a consistent snapshot of the database taken at the start of the transaction.
Conflict Detection: Tracks dependencies between transactions to detect conflicts that could lead to anomalies.
Validation Phase: At the end of a transaction, checks for conflicts. If a conflict is detected, the transaction may be aborted and retried.
We should use serializable snapshot isolation instead of 2PL if most transactions don't overlap with each other otherwise use 2PL

## What is a Column Oriented Storage?

**Answer**

Column-oriented storage is a database storage technique where data is stored by columns rather than by rows. This approach is particularly beneficial for analytical queries that often need to read only a few columns from a large dataset.
Benefits:
Query Performance:
- Faster Aggregations: Aggregation queries (e.g., SUM, AVG) are faster because only the relevant columns are read.
- Reduced I/O: Only the columns needed for a query are read from disk, reducing I/O operations.
Data Compression:
- Higher Compression Ratios: Columns with similar data types and values can be compressed more effectively.
- Storage Efficiency: Reduced storage requirements due to better compression.
Analytical Workloads:
- Optimized for OLAP: Ideal for Online Analytical Processing (OLAP) workloads, which involve complex queries over large datasets.
Drawbacks:
Write Performance:
- Slower Writes: Writing data can be slower because each column must be written separately. [Can use LST Trees and SSTables]
- Complex Updates: Updates and deletes can be more complex and slower compared to row-oriented storage.
- Every column must have the same sort order.
Transactional Workloads:
- Not Ideal for OLTP: Less suited for Online Transaction Processing (OLTP) workloads, which involve frequent writes and updates.
Example Systems: Apache Cassandra, Google Bigtable, Amazon Redshift

## What is Predicate Pushdown?

**Answer**

Predicate pushdown is an optimization technique used in database systems and query engines to improve query performance by filtering data as early as possible in the query execution process. This means that predicates (conditions) are applied at the storage level, reducing the amount of data that needs to be read and processed.

## What are Data Serialization Frameworks?

**Answer**

Data serialization frameworks are tools and libraries designed to convert data structures or objects into a format that can be easily stored, transmitted, and reconstructed later. These frameworks are essential for data interchange between different systems, especially in distributed computing environments.
JSON, XML, Protocol Buffers, Apache Avro, Apache Thrift, MessagePack

## What is database replication?

**Answer**

Database replication is a technique used to copy and maintain database objects in multiple instances to ensure data redundancy, improve availability, and enhance performance. It can be implemented in various forms, such as master-slave, master-master, synchronous, and asynchronous replication, each suited to different use cases and requirements.
Synchronous Replication: Ensures real-time updates and strong consistency by applying changes simultaneously to all replicas. Suitable for critical applications requiring high availability and minimal data loss.
Asynchronous Replication: Allows for delayed updates and eventual consistency, optimizing write performance and suitable for applications where immediate consistency is not critical but users will get stale read.

## How to implement Replication?

**Answer**

Export SQL Statements: This method involves exporting the SQL statements from the primary database and then running these statements on the secondary database. But it is non deterministic and not suitable for real-time replication.
Write-Ahead Logging (WAL) is a method where changes to the database are first written to a log before being applied to the database. This log can be used to replicate changes to a secondary database. But if we change DB Software.
Replication logs are specialized logs that record changes to the database. These logs are used to replicate changes to secondary databases but also requires continuous connection and can be complex to manage.

## How to make eventual consistency better?

**Answer**

Reading from the Same Replica to Which You Write Ensure that read operations are directed to the same replica where the write operations were performed. This minimizes the chances of reading stale data.
Using Timestamps to Choose Which Replica to Read From: Use timestamps to determine the most recent replica to read from. This helps in selecting the replica with the latest data.
Monotonic Writes and Reads from the Same Replica: Ensure that writes are performed in a monotonic order and that reads are directed to the same replica to maintain consistency.
Monotonic Writes: Ensure that write operations are ordered and applied in a consistent sequence.
Consistent Prefix Reads: Ensure that read operations return data that reflects a consistent prefix of the write operations. This means that reads will see a consistent sequence of writes.
Causal Dependencies and Reading from the Same Replica: Ensure that read operations respect causal dependencies and are directed to the same replica to maintain consistency.
Causal dependency ensures that operations in a distributed system are executed in an order that respects their cause-and-effect relationships

## Explain Master-Slave Architecture in DB.

**Answer**

Master-slave architecture is a design pattern used in computing and data management systems where one device or process (the master) controls one or more other devices or processes (the slaves).
In database replication, also known as primary-secondary replication, the master database is the primary source of data, and the slave databases maintain an exact copy of the master's data.

## What is Sharding?

**Answer**

Sharding: A horizontal partitioning technique used to distribute data across multiple servers or nodes. It involves dividing data into smaller, more manageable pieces called shards, each operating as an independent database. Sharding improves scalability, performance, and fault tolerance by distributing the load across multiple servers. While sharding offers significant benefits, it also introduces challenges related to complexity, cross-shard operations, and shard rebalancing. By carefully planning and managing the sharding strategy, distributed systems can achieve high performance and scalability.
Range-Based Sharding: Data is divided into contiguous ranges based on the shard key.
Hash-Based Sharding: The shard key is hashed, and the hash value determines the shard.
List-Based Sharding: Specific values of the shard key are mapped to specific shards.
Geographic Sharding: Data is partitioned based on geographic regions.
Directory-Based Sharding: A central directory keeps track of which shard contains which data.
Dynamic Sharding: Shards are created and adjusted dynamically based on the current load and data distribution.
Local Secondary Index (LSI) is a type of secondary index that allows for efficient querying of data based on attributes other than the primary key within the same partition. It provides an alternative sort key, enabling more flexible querying options while ensuring consistency with the base table. LSIs improve query performance by reducing the need for full table scans but come with storage and write performance overhead.
Global Secondary Index (GSI) is a powerful indexing mechanism that allows for efficient querying of data based on attributes other than the primary key, across all partitions in a table. GSIs provide flexible querying options and can significantly improve query performance for specific access patterns. However, they come with storage and write performance overhead and are eventually consistent, which can lead to temporary inconsistencies in query results.

## What is Database Partitioning?

**Answer**

Partitioning A technique that divides a single database table into smaller partitions based on a specified key. This approach improves performance by allowing queries to target specific partitions, It improves query performance and manageability but requires careful planning.

## What is single leader replication?

**Answer**

Single leader replication is a replication strategy where one node (the leader) handles all write operations, and one or more follower nodes replicate the data from the leader and handle read operations. This approach improves read performance and simplifies write consistency but can suffer from replication lag and potential bottlenecks for write-heavy workloads. It is commonly used in distributed databases to achieve high availability and scalability.

## What can happen when a replication leader fails?

**Answer**

A failed or unreachable leader temporarily stops writes until a follower is promoted or the old
leader recovers. An unsafe failover can lose acknowledged writes that had not reached the promoted
replica. If two nodes accept writes as leader, split brain can produce conflicting histories.

Mitigations include quorum-based leader election, fencing tokens or epochs that reject an old
leader's writes, careful durability requirements before acknowledgment, and explicit conflict or
recovery procedures. A heartbeat detects suspicion of failure; it does not by itself prove which
side of a network partition is allowed to remain leader.

## What is Distributed consensus?

**Answer**

Distributed consensus is the process of achieving agreement among multiple nodes in a distributed system. It ensures consistency, fault tolerance, and coordination across the system. Common consensus algorithms include Paxos, Raft, and Zab, each with its own mechanisms for proposing, voting, and committing values. While consensus is crucial for maintaining data integrity and enabling coordinated actions, it also introduces challenges related to complexity, performance, and scalability.

## What is multi leader replication?

**Answer**

Multi-leader replication is a replication strategy where multiple nodes can accept write operations and replicate changes to each other. This approach provides high availability, fault tolerance, and load distribution but introduces challenges related to conflict resolution, consistency, and system complexity. Conflict resolution strategies such as last write wins, custom application logic, and version vectors are essential for maintaining data consistency in multi-leader replication systems.
Preventing Indefinite Message Passing: Update replication logs to track seen writes.
Conflict Avoidance: Route writes for the same key to the same replica.
Conflict Resolution:
Use Last Write Wins (LWW) with timestamps.
Employ distributed counters and version vectors.
Handling Concurrent Writes:
Store siblings and let users resolve conflicts.
Use CRDTs for automatic conflict resolution.

## What is CRDTs?

**Answer**

Conflict-Free Replicated Data Types (CRDTs) are data structures designed for distributed systems to achieve strong eventual consistency without complex conflict resolution. CRDTs automatically resolve conflicts and ensure that all replicas converge to the same state. While CRDTs offer significant benefits in terms of automatic conflict resolution and fault tolerance, they are suitable for specific use cases and can be complex to design and implement.
Operational CRDTs (Commutative Replicated Data Types) are a class of CRDTs that achieve strong eventual consistency by propagating operations between replicas. These operations are commutative, associative, and idempotent, ensuring that they can be applied in any order and still converge to the same state. It require a causally consistent message delivery system to ensure strong eventual consistency. This involves ensuring that operations are delivered in an order that respects their causal dependencies, with no drops or duplicates.
State-Based CRDTs (Convergent Replicated Data Types) achieve strong eventual consistency by periodically exchanging and merging the entire state of the data structure between replicas, the merge function must be commutative, associative, and idempotent. These CRDTs ensure automatic conflict resolution and strong eventual consistency but can introduce communication overhead and latency. By using predefined merge functions, state-based CRDTs ensure that all replicas converge to the same state, even in the presence of concurrent updates.
The gossip protocol can be effectively used with state-based CRDTs to propagate state information between replicas in a distributed system.
Sequence CRDTs are specialized CRDTs designed to handle sequences, such as lists or arrays, in distributed systems. They support concurrent operations, preserve the order of elements, and automatically resolve conflicts to ensure that all replicas converge to the same sequence. While sequence CRDTs offer significant benefits for collaborative applications, they can be complex to design and implement and may introduce overhead in terms of storage and computation.

## What is Leaderless Replication?

**Answer**

Leaderless replication is a replication strategy in distributed databases where there is no single designated leader node. Instead, all nodes are equal peers, and write operations can be sent to any node. This approach improves fault tolerance, availability, and scalability by eliminating the single point of failure associated with leader-based replication. Leaderless replication typically uses a quorum-based consensus approach for read and write operations, ensuring eventual consistency. While it offers significant benefits, it also introduces challenges related to conflict resolution, consistency guarantees, and quorum overhead.
Read Repair: During read operations, the client reads from a quorum of nodes, identifies the most up-to-date value, and writes it back to nodes with outdated values to ensure consistency.
Anti-Entropy: A background process that continuously synchronizes data between nodes, ensuring eventual consistency by propagating changes.
Efficient State Synchronization with Merkle Trees: Merkle trees are used to efficiently determine differences between data sets on different nodes, allowing nodes to synchronize only the differing parts, minimizing data transfer and improving efficiency.

## What are Merkle Trees?

**Answer**

Merkle trees are a data structure used to efficiently and securely verify the integrity of data. They work by hashing data blocks and organizing the hashes in a binary tree structure, with the root hash uniquely representing the entire data set. Merkle trees provide benefits such as data integrity, efficient comparison, and scalability, making them suitable for use cases in blockchain, distributed systems, and peer-to-peer networks. By comparing root hashes and traversing the tree, Merkle trees allow efficient detection and synchronization of differences between large data sets.

## What is quorums?

**Answer**

Quorums are a fundamental concept in distributed systems used to ensure consistency and coordination among multiple nodes. A quorum is a subset of nodes that must agree on an operation for it to be considered successful. Quorums are commonly used in leaderless replication, consensus algorithms, and distributed databases to achieve fault tolerance and consistency. By requiring a majority agreement on operations and ensuring an overlap between read and write quorums, quorums prevent stale reads and ensure that the most recent write is always read. While quorums provide significant benefits in terms of fault tolerance, consistency, and scalability, they can also introduce latency and complexity. ( W + R > N )
Problems:
Out-of-Order Writes: Writes can arrive at different nodes out of order, leading to inconsistencies. [Fix: Vector Clocks, Lamport Timestamps]
Write Failures: If a write operation fails to reach a quorum, it can leave the system in an inconsistent state. [Fix: Rollback Mechanism, Retries]
Sloppy Quorums: In some cases, nodes may temporarily accept writes even if they are not part of the quorum, leading to potential inconsistencies. [Fix: Hinted Handoff, Anti-Entropy]
Hinted Handoff: Temporarily store writes on a nearby node if the intended node is unavailable. Once the intended node becomes available, the write is handed off to it.

## What is Two Phase Commit?

**Answer**

Two-Phase Commit (2PC) is a distributed algorithm used to ensure atomicity and consistency in transactions that span multiple nodes or databases. It involves a two-phase process: the Prepare Phase, where participants prepare to commit the transaction, and the Commit Phase, where the coordinator instructs participants to commit or abort based on their votes. While 2PC ensures atomicity and consistency, it introduces latency, complexity, and potential blocking issues. Careful implementation and management are required to handle failure scenarios and maintain system performance.

## What is Cross-Partition Write?

**Answer**

Cross-Partition Write refers to a write operation that involves updating data across multiple partitions in a distributed database. These operations require coordination and consistency across partitions, making them more complex than single-partition writes. Challenges include ensuring atomicity, maintaining consistency, handling latency, and managing failures. Solutions such as Two-Phase Commit (2PC), distributed consensus algorithms, and eventual consistency models can help address these challenges and ensure data integrity in cross-partition writes.

## What is 3PC and Saga Pattern?

**Answer**

Three-Phase Commit (3PC) is an advanced distributed transaction protocol designed to improve fault tolerance and reduce the risk of blocking compared to the Two-Phase Commit (2PC). It introduces an additional "prepare to commit" phase between the initial prepare phase and the final commit phase. In the prepare phase, the coordinator asks participants to prepare for the transaction. Once all participants respond with "OK," the coordinator sends a "prepare to commit" signal. If the coordinator fails during the final commit phase, participants can query each other to determine if any node had reached the "prepare to commit" state. If at least one node had, they can proceed with committing the transaction; otherwise, they can collectively decide to abort. This mechanism allows recovery from coordinator failures, although participants must continue attempting to write to any downed nodes indefinitely.
Saga Pattern is a different approach to managing distributed transactions, particularly useful for long-running and complex workflows. Instead of attempting to write to multiple nodes simultaneously, the Saga Pattern executes writes sequentially, one node at a time. If a write operation fails, a compensating transaction is performed to revert the changes and restore the database to its previous state. This approach provides flexibility and fault tolerance by breaking down the transaction into smaller, independent steps. However, it introduces the risk that the compensating transaction might also fail, requiring robust error handling and recovery mechanisms to maintain data integrity.

## Different Hashing Schemes for Partitioning?

**Answer**

Hash Index with Modulo Operation: Simple but requires significant rebalancing when the number of partitions changes.
Consistent Hashing: Minimizes rebalancing and is highly scalable but more complex to implement.
Fixed Number of Partitions: Reduces rebalancing but requires careful planning to choose an appropriate number of partitions.
Dynamic Partitioning: Adapts to changing data and load patterns but is complex to implement and manage, especially for handling node failures and rebalancing.

## What is Consistent Hashing?

**Answer**

Consistent Hashing is a technique used to distribute data across multiple nodes in a distributed system while minimizing rebalancing when nodes are added or removed. It uses a hash ring to map data keys and nodes to positions on the ring, with each node represented by multiple virtual nodes to ensure a more even distribution of data. Virtual nodes help improve load balancing and prevent hotspots, making consistent hashing suitable for scalable and fault-tolerant distributed systems. However, it introduces complexity in implementation and requires careful management of the hash ring and choice of hash function.
Node Crash Detection: Detecting node crashes is a challenge for all distributed systems, including those using Consistent Hashing. Misinterpreting a node's state can lead to data inconsistencies and split-brain scenarios.
Hot Partitions: Hot partitions occur when a particular key receives a disproportionate amount of traffic. Addressing this requires deeper sharding within the hot key and dynamic load balancing techniques.

## What are vector clocks, version vector and lamport timestamps?

**Answer**

Vector Clocks are a mechanism used in distributed systems to capture the partial ordering of events and detect causality between them. Each node in the system maintains a vector of counters, one for each node. When an event occurs, the node increments its own counter and includes the updated vector in messages sent to other nodes. By comparing vector clocks, nodes can determine the causal relationship between events.
Lamport Timestamps are a simpler mechanism used to order events in a distributed system. Each node maintains a counter (timestamp) that is incremented with each event. When a node sends a message, it includes its current timestamp. Upon receiving a message, a node updates its timestamp to be greater than the maximum of its own timestamp and the received timestamp. Lamport timestamps provide a total ordering of events but do not capture causality.Lamport Timestamps are a simpler mechanism used to order events in a distributed system. Each node maintains a counter (timestamp) that is incremented with each event. When a node sends a message, it includes its current timestamp. Upon receiving a message, a node updates its timestamp to be greater than the maximum of its own timestamp and the received timestamp. Lamport timestamps provide a total ordering of events but do not capture causality.
Version Vectors are used in distributed systems to track the versions of replicated data and detect conflicts. Each replica maintains a vector of counters, incrementing its own counter with each update. By comparing version vectors, replicas can determine the most recent version of the data and detect conflicts, helping to maintain consistency across the system.

## What is Linearizable Databases?

**Answer**

Linearizable Databases provide the strongest form of consistency, ensuring that all operations appear to occur in a single, globally agreed-upon order. This guarantees that once a write operation is acknowledged, all subsequent read operations reflect that write, providing immediate visibility and strong data correctness. Linearizability is achieved through coordination protocols like Paxos or Raft, which handle consensus and maintain a consistent state across nodes. While linearizable databases offer strong consistency and simplicity for developers, they come with performance overhead and scalability challenges due to the need for coordination and consensus.
Single-Leader Replication Provides strong consistency within the leader but not linearizability due to replication lag and failover complexities.
Multi-Leader Replication: Provides eventual consistency but not linearizability due to conflicts and replication lag.
Version Vectors and Lamport Timestamps: Help detect causality and order events but do not ensure linearizability.

## What is Raft?

**Answer**

Raft is a consensus algorithm designed to manage a replicated log in a distributed system. It operates with a single leader that handles client requests and log replication, ensuring that all nodes agree on the same log entries and their order. Raft's clear separation of phases (leader election, log replication, and commitment) makes it easier to understand and implement compared to other consensus algorithms. While Raft provides strong consistency and fault tolerance, it can suffer from leader bottlenecks and election overhead.

## Explain Leader Election Raft?

**Answer**

Election Timeout: Nodes wait for heartbeats and start an election if no heartbeat is received within a timeout.
Transition to Candidate: Nodes increment their term number and request votes from other nodes.
RequestVote RPC: Candidates send their term number and log information to other nodes.
Majority Vote: Candidates need a majority of votes to become the leader.
Handling Split Votes: Staggered election timeouts help resolve split votes.
Quorum: Ensures only one leader is elected at a time.
Term Numbers: Prevent old leaders from regaining leadership.
Log Consistency: Ensures the leader has the most up-to-date log.

## Explain How write works in Raft?

**Answer**

Client Request: The client sends a write request to the leader.
Log Entry Creation: The leader creates a new log entry for the request.
Log Replication: The leader appends the entry to its log and sends AppendEntries RPCs to followers.
Follower Response: Followers append the entry to their logs and acknowledge the leader.
Commitment: The leader waits for a majority of acknowledgments, marks the entry as committed, applies it to its state machine, and responds to the client.
Follower Commitment: The leader informs followers of the commit index, and followers apply the committed entry to their state machines.

## What are Coordination Services?

**Answer**

Coordination Services are specialized systems that provide essential functionalities for managing and coordinating distributed processes and resources. They offer configuration management, synchronization, leader election, service discovery, and distributed locking, ensuring consistency, reliability, and fault tolerance in distributed applications. Examples of coordination services include Apache ZooKeeper, etcd, and Consul. These services are widely used in microservices architectures, distributed databases, and cluster management systems to maintain consistent state and efficient operation across distributed nodes.

## What is SYNC keyword in Zookeper?

**Answer**

The sync keyword in Apache ZooKeeper is used to synchronize a client's view of the ZooKeeper ensemble's state, ensuring that the client sees the most up-to-date data. It forces the server to process all pending updates before responding to the client, providing strong consistency. The sync operation is asynchronous, allowing the client to continue with other operations while the synchronization is being processed. While sync ensures data consistency and helps coordinate operations in distributed systems, it introduces performance overhead and requires careful consideration of the application's consistency requirements.

## How to decide which database to choose SQL or NoSQL?

**Answer**

SQL Databases
Structured Data: Ideal for highly structured data fitting into tables with predefined schemas.
Normalization: Ideal for normalized data structures where data integrity and relationships are crucial.
ACID Transactions: Required for strong consistency and ACID properties.
Complex Queries: Needed for performing complex queries, joins, and aggregations.
Data Integrity: Essential for enforcing data integrity and constraints.
Mature Ecosystem: Preferred for a mature ecosystem with well-established tools and community support.
Optimized Updates/Deletes: Suitable when updates and deletes are frequent and need to be efficient.
NoSQL Databases
Unstructured or Semi-Structured Data: Suitable for unstructured or semi-structured data.
Denormalization: Suitable for denormalized data structures where fast reads are prioritized over updates and deletes.
Scalability: Required for handling large volumes of data with horizontal scalability.
Flexible Schema: Needed for a flexible schema that can evolve over time.
High Throughput and Low Latency: Essential for high write/read throughput with low latency.
Specific Use Cases: Ideal for document stores, key-value stores, column-family stores, and graph databases.
Optimized Reads: Suitable when read operations are frequent and need to be highly efficient.

## What is the difference between MySQL vs PostgreSQL?

**Answer**

MySQL
General Overview: Developed by Oracle Corporation, known for ease of use, speed, and reliability.
SQL Compliance: Partially compliant with SQL standards.
Data Types: Supports a variety of data types with some limitations.
Performance: Generally faster for read-heavy operations and simple queries.
Extensibility: Limited extensibility with fewer options.
ACID Compliance: ACID-compliant with the InnoDB storage engine.
Replication: Supports master-slave and master-master replication.
Indexing: Supports basic indexing options like B-tree and full-text indexes.
Concurrency Control: Uses Two-Phase Locking (2PL) for concurrency control.
Community and Support: Large community with extensive documentation and commercial support from Oracle.
Licensing: Dual-licensed under GPL and a commercial license from Oracle.
Use Cases: Ideal for web applications, content management systems, and read-heavy workloads.
PostgreSQL
General Overview: Developed by the PostgreSQL Global Development Group, known for advanced features, extensibility, and standards compliance.
SQL Compliance: Highly compliant with SQL standards.
Data Types: Supports a wide range of advanced data types, including arrays and JSON.
Performance: Generally better for write-heavy operations and complex queries.
Extensibility: Highly extensible with support for custom functions and data types.
ACID Compliance: Fully ACID-compliant by default.
Replication: Supports streaming, logical, and cascading replication.
Indexing: Supports advanced indexing options like B-tree, hash, GiST, and GIN.
Concurrency Control: Uses Serializable Snapshot Isolation (SSI) for its highest isolation level.
Community and Support: Active community with extensive documentation and commercial support from various vendors.
Licensing: Licensed under the permissive PostgreSQL License.
Use Cases: Ideal for applications requiring complex queries, data integrity, and write-heavy workloads.

## What's VoltDb and why is it called new types of Relational DB?

**Answer**

VoltDB: A high-performance, in-memory relational database designed for real-time analytics and high-throughput transaction processing. It achieves actual serial execution of transactions by using a single-threaded execution model for each partition. This eliminates the need for complex locking mechanisms
In-Memory Storage: Provides extremely fast read and write operations by storing data entirely in memory.
High Throughput: Optimized for handling millions of transactions per second.
ACID Compliance: Ensures strong consistency and data integrity.
Horizontal Scalability: Supports automatic sharding and partitioning for distributed environments.
Stored Procedures: Uses stored procedures to reduce network overhead and improve efficiency.
SQL Support: Supports standard SQL for querying and managing data.
Modern Use Cases: Suitable for applications requiring real-time data processing and analytics.

## What is Google Spanner? What makes is special?

**Answer**

Google Spanner: A globally distributed, horizontally scalable, and strongly consistent database service developed by Google.
Global Distribution: Operates across multiple data centers and geographic regions, providing low-latency access to data from anywhere.
Horizontal Scalability: Scales horizontally by adding more nodes, with automatic sharding and load balancing.
Strong Consistency: Provides strong consistency and ACID transactions across distributed nodes using distributed consensus algorithms and TrueTime API.
Lock-Free Distributed Reads: Spanner can perform lock-free reads by leveraging precise time synchronization, reducing contention and improving performance.
SQL Support: Supports standard SQL for querying and managing data, with familiar relational database features.
High Availability: Designed for high availability and fault tolerance, with data replication across multiple nodes and regions.
TrueTime API: Uses Google's TrueTime API for globally synchronized timestamps, crucial for maintaining strong consistency.
Time Synchronization: Each data center is equipped with GPS receivers and atomic clocks to achieve highly accurate time synchronization.
Globally Distributed ACID Transactions: Supports ACID transactions that span multiple geographic regions.
Automatic Sharding and Load Balancing: Automatically shards data and balances the load across nodes.
High Performance and Low Latency: Optimized for high performance and low-latency access to data.
Integration with Google Cloud: Fully integrated with Google Cloud Platform, providing seamless integration with other Google Cloud services.

## Explain a bit about MongoDB and Apache Cassandra

**Answer**

MongoDB:
Document-Oriented: Stores data in flexible, JSON-like documents.
Scalability: Supports horizontal scalability through sharding.
Indexing: Uses B-trees for indexing, supporting various types of indexes.
Replication: Generally uses single-leader replication with replica sets.
ACID Transactions: Supports ACID transactions for strong consistency and data integrity.
Aggregation Framework: Offers powerful data processing and transformation capabilities.
Flexible Schema: Allows for dynamic schema design.
Apache Cassandra:
Distributed Architecture: Designed for distributed environments with no single point of failure.
Scalability: Supports horizontal scalability by adding more nodes.
Column-Family Data Model: Uses a flexible column-family data model.
Replication: Generally uses leaderless replication with configurable replication across data centers.
Consistency Levels: Offers tunable consistency levels.
Indexing: Uses LSM trees and SSTables for efficient data storage and retrieval.
Partitioning: Uses partition keys and clustering keys to distribute data, ensuring high throughput.
Transactions: Does not support full ACID transactions, but provides row-level locking for atomic operations within a single row.

## What is Hadoop?

**Answer**

Hadoop: An open-source framework for distributed storage and processing of large datasets using a cluster of commodity hardware.
HDFS: A distributed file system that provides high throughput access to data, with rack-aware storage for fault tolerance and performance.
MapReduce: A programming model for parallel processing of large datasets.
YARN: A resource management layer that schedules and manages resources across the cluster.
Hadoop Common: Provides common utilities and libraries for the other Hadoop modules.
Apache Spark: An alternative to MapReduce for distributed data processing with in-memory capabilities.
NameNode: Manages metadata and coordinates storage and retrieval of data.
DataNode: Stores actual data blocks and serves read/write requests.
Replication Pipeline: Ensures data is replicated across multiple DataNodes for fault tolerance.
Scalability: Designed to scale horizontally by adding more nodes.
Fault Tolerance: Automatically replicates data across multiple nodes for reliability.
Cost-Effective: Uses commodity hardware and is open-source.
Flexibility: Supports various data types and formats.
High Throughput: Optimized for batch processing and large-scale data analysis.

## What's HBase and how does it compare to Cassandra?

**Answer**

HBase:
Column-Oriented: Stores data in a column-family format.
Integration with Hadoop: Built on top of HDFS, integrates with Hadoop ecosystem components.
Scalability: Scales horizontally by adding more nodes.
Consistency: Provides strong consistency for read and write operations.
Data Model: Flexible data model with rows, column families, columns, and timestamps.
Indexing: Uses LSM trees for efficient data storage and retrieval.
Apache Cassandra:
Column-Family Data Model: Similar to HBase, uses a column-family data model.
Distributed Architecture: No single point of failure, data distributed across multiple nodes.
Scalability: Scales horizontally by adding more nodes.
Consistency Levels: Offers tunable consistency levels.
Replication: Uses leaderless replication with configurable replication across data centers.
Indexing: Uses LSM trees and SSTables for efficient data storage and retrieval.

## What is MapReduce?

**Answer**

MapReduce: A programming model and processing framework for distributed and parallel processing of large datasets.
Map Function: Processes input key-value pairs to generate intermediate key-value pairs.
Reduce Function: Merges intermediate key-value pairs to produce final output key-value pairs.
Input Splitting: Splits input data into smaller chunks for parallel processing.
Shuffling and Sorting: Groups intermediate key-value pairs by key for the Reduce function.
Scalability: Designed to scale horizontally across multiple nodes.
Fault Tolerance: Automatically handles node failures.
Simplicity: Provides a simple programming model for processing large datasets.
Parallel Processing: Enables parallel processing to reduce data processing time.

## How do we do Batch Job Data Joins?

**Answer**

Batch Job Data Joins: Combine data from two or more datasets based on a common key in batch processing pipelines.
Broadcast Hash Join: Broadcasts the smaller dataset to all nodes, allowing each node to perform the join locally.

**When to Use: Suitable when one dataset is significantly smaller than the other.**

Example: Joining a small user information dataset with a large user transactions dataset.
Partitioned Hash Join: Partitions both datasets based on the join key, allowing for parallel execution of the join operation.

**When to Use: Suitable when both datasets are large and can be partitioned based on the join key.**

Example: Joining large user information and user transactions datasets based on the user ID.

## What is Apache Spark and how is it better than MapReduce?

**Answer**

Apache Spark:
In-Memory Processing: Performs computations in memory, reducing disk I/O and speeding up data processing.
Unified Engine: Supports batch processing, interactive queries, real-time streaming, machine learning, and graph processing.
Ease of Use: Provides high-level APIs in multiple languages and rich built-in libraries.
Fault Tolerance: Ensures fault tolerance through lineage information and DAGs.
How Spark is Better Than MapReduce:
Performance: Spark's in-memory processing and lazy evaluation optimize performance.
Chained Jobs: Spark optimizes execution plans for chained jobs, reducing waiting times.
Intermediate State: Spark keeps intermediate data in memory, reducing disk usage.
Sorting: Spark avoids unnecessary sorting by optimizing execution plans.
Fault Tolerance: Spark uses lineage information for faster fault recovery.
Dependencies: Spark optimizes narrow and wide dependencies to minimize shuffling and improve efficiency.
Summary of Terms
DAGs: Directed Acyclic Graphs used by Spark to manage task dependencies and optimize execution plans.
Mapper: Function in MapReduce that processes input data and produces intermediate key-value pairs.
Reducer: Function in MapReduce that processes intermediate key-value pairs and generates the final output.
Sorting: Process of arranging data in a specific order, typically based on key values.
Shuffling: Redistributing data across the cluster to group data by key for processing.
Resilient Distributed Dataset (RDD): The fundamental data structure in Apache Spark, representing an immutable, distributed collection of objects.
Narrow Dependencies: Dependencies where each partition of the parent RDD is used by at most one partition of the child RDD, allowing for efficient processing.
Wide Dependencies: Dependencies where multiple child partitions depend on a single parent partition, requiring shuffling of data.
Chained Jobs: Sequence of jobs where the output of one job serves as the input to the next job, optimized by Spark using DAGs.

## What's Stream Processing and When Do We Use It?

**Answer**

Stream Processing: Real-time data processing paradigm that handles data as it arrives, enabling immediate insights and actions.
Real-Time Processing: Processes data in real-time, suitable for applications requiring immediate responses.
Continuous Data Flow: Handles a continuous flow of data from various sources.
Low Latency: Minimizes the time between data arrival and processing.
Metric Log Time Grouping and Bucketing: Aggregates and analyzes log data in real-time.
Change Data Capture (CDC): Captures and processes real-time changes in a database.
Event Sourcing: Stores and processes events as they occur, allowing for state reconstruction.
Time Window: Processes data within specific time intervals for time-based insights.
Tumbling Window: Non-overlapping windows starting at fixed intervals with a fixed time size.
Processing Semantics: Choose at-most-once, at-least-once, or a system-specific exactly-once model.
Exactly-once claims are scoped and usually require transactions, deduplication, or idempotent side
effects; a broker alone cannot guarantee every external business action happens once.

## How to perform joins in Stream Processing?

**Answer**

Stream processing systems often need to combine data from different sources in real-time.
Stream Enrichment: Enhancing a stream with additional information from another source.
Stream-Stream Join: Joining two continuous streams based on a common key and a time window.
Stream-Table Join: Joining a continuous stream with a static or slowly changing table.
Table-Table Join: Joining two static or slowly changing tables.

## What is Apache Flink?

**Answer**

Apache Flink: An open-source stream processing framework designed for high-throughput, low-latency, and stateful computations over unbounded and bounded data streams.
Stream Processing: Processes data in real-time, providing low-latency responses and enabling real-time analytics.
Batch Processing: Supports batch processing, allowing it to handle both real-time and historical data.
Stateful Computations: Maintains and queries state information across events in a fault-tolerant manner.
Event Time Processing: Handles out-of-order events and provides accurate time-based computations using watermarks.
Fault Tolerance: Uses distributed snapshots (checkpoints) to ensure state and computations can recover from failures.
Scalability: Scales horizontally to handle large volumes of data and high throughput.
Core Components: Includes DataStream API, DataSet API, state management, windowing, and connectors for integrating with various data sources and sinks.

## What are Search Indexes and Why do we need them?

**Answer**

Search Indexes: Specialized data structures designed to optimize full-text search operations.
Limitations of Traditional Indexes: Traditional database indexes are inefficient for full-text search due to their focus on exact match queries and inefficiency with large text data.
Tokenization: The process of breaking down text into smaller units (tokens) for indexing.
Inverted Index: A data structure that maps tokens to documents containing those tokens, enabling fast lookups.
Prefix and Suffix Searching: Efficiently handled by keeping tokens sorted and using binary search or specialized data structures.
Apache Lucene: A high-performance text search engine library that provides powerful indexing and search capabilities, supporting complex search queries and efficient full-text search operations.

## What's ElasticSearch and What's Used For?

**Answer**

Elasticsearch: An open-source, distributed search and analytics engine built on top of Apache Lucene.
Distributed Architecture: Runs on a cluster of nodes, distributing data and search operations across multiple nodes.
Real-Time Search and Analytics: Provides near real-time search and analytics capabilities.
Full-Text Search: Excels at full-text search using inverted indexing.
Scalability and Fault Tolerance: Scales horizontally and ensures data availability through replication.
RESTful API: Provides a RESTful API for easy integration with other applications.
Schema-Free: Automatically detects and indexes the structure of JSON documents.

## What are Time Series Databases?

**Answer**

Time Series Databases (TSDBs): Specialized databases optimized for storing, retrieving, and managing time-stamped data.
Optimized Write Performance: Handle high write throughput using batching and compression.
Optimized Read Performance: Efficient querying through indexing and partitioning.
Efficient Data Deletion: Use retention policies and compaction to manage storage.
Hypertable and Chunks: Logical tables partitioned into smaller segments based on time intervals.
LSM Tree (Log-Structured Merge Tree): Data structure designed for high write throughput, using in-memory structures and immutable disk files.
SSTable (Sorted String Table): Immutable, sorted files used to store data on disk in LSM tree-based databases.
Column-Oriented Storage: Storage format where data is stored by columns, enabling efficient compression and fast read performance.
Example TSDB: InfluxDB, TimescaleDB, Apache Druid

## What are Graph Databases? How are they so fast?

**Answer**

Graph Databases: Specialized databases designed to store, manage, and query data represented as a graph of nodes and edges.
Nodes and Edges: Nodes represent entities, and edges represent relationships between nodes.
Schema Flexibility: Allows for easy evolution of the data model without requiring changes to the existing schema.
Query Language: Uses specialized query languages like Cypher, Gremlin, and SPARQL for traversing and querying graph structures.
Index-Free Adjacency: Nodes store direct references to their adjacent nodes, enabling constant-time traversal of relationships.
Efficient Traversal: Optimized for traversing relationships, making them highly efficient for complex queries.
In-Memory Processing: Uses in-memory processing to speed up query execution.
Optimized Storage: Uses storage formats optimized for graph data, reducing the overhead of storing and retrieving nodes and relationships.
Example Graph Database: Neo4j:

## What are GeoSpatial Indexes? Why You Need Them?

**Answer**

Geospatial Indexes: Specialized data structures used to efficiently store, query, and manage spatial data.
Efficient Querying: Enable fast lookups, range queries, and nearest neighbor searches for spatial data.
Scalability: Maintain query performance even as the dataset grows.
Accuracy: Provide precise and accurate spatial queries for applications that rely on location data.
Types of Geospatial Indexes:
GeoHashes: Encode geographic coordinates into a compact string, representing rectangular areas.
QuadTrees: Partition a two-dimensional space into hierarchical regions, allowing for efficient spatial queries.
Example Use Cases: Location-based services, GIS, navigation and mapping, ride-sharing, and delivery services.

## What is Distributed Caching?

**Answer**

Distributed Caching: A technique used to store and manage frequently accessed data across multiple servers or nodes in a distributed system.
Improved Performance: Faster reads and writes, reduced network latency, and efficient resource utilization.
Reduced Load on Backend Systems: Offloading database queries and allowing backend systems to handle more critical tasks.
Scalability: Horizontal scaling and independent scaling of the cache layer.
Benefits: Faster reads and writes, reduced load on key components, and scalability.
Drawbacks: Cache misses and data consistency challenges.

**What to Cache: Database results, computations done by application servers, and popular static content.**

**Where to Store the Cache: Server local caching and global caching layer**

## What is Distributed Cache Writes?

**Answer**

Distributed Cache Writes: Strategies and mechanisms used to write data to a distributed cache, ensuring data consistency, performance, and reliability.
Write-Around Cache: Writes are made directly to the database, and the cache is updated on subsequent reads.
Write-Through Cache: Writes are made to both the cache and the database simultaneously, ensuring data consistency.
Write-Back Cache: Writes are initially made to the cache, and the data is asynchronously written to the database, providing faster write performance but potential data inconsistency.
Challenges: Data consistency, cache misses, and fault tolerance.
Solutions: Use techniques such as two-phase commit, distributed locking, efficient cache invalidation, and replication to address challenges

## What is Cache Evictions?

**Answer**

Cache Eviction: The process of removing items from a cache when it reaches its storage limit.
FIFO: Removes the oldest items first. Simple to implement but may not consider usage patterns.
LRU: Removes the least recently accessed items first. Takes into account usage patterns and provides better performance.
LFU: Removes the least frequently accessed items first. Considers access frequency but is more complex to implement.
TTL: Removes items that have exceeded a specified time-to-live period. Ensures stale data is removed.

## Explain Redis vs. Memcached

**Answer**

Data Structures:
Redis: Supports various data structures (strings, lists, sets, sorted sets, hashes, etc.).
Memcached: Supports only strings as values.
Persistence:
Redis: Supports data persistence with RDB (Redis Database Backup) and AOF (Append-Only File).
Memcached: No data persistence.
Replication and Clustering:
Redis: Supports replication and clustering.
Memcached: Supports sharding but no built-in replication or clustering.
Eviction Policies:
Redis: Multiple eviction policies (LRU, LFU, TTL, etc.).
Memcached: Simple LRU eviction policy.
Transactions:
Redis: Supports transactions.
Memcached: No transaction support.
Use Cases:
Redis: Versatile, suitable for caching, session storage, real-time analytics, message queuing, etc.
Memcached: Suitable for simple caching scenarios.

## What are Content Delivery Networks?

**Answer**

Content Delivery Networks (CDNs): A system of distributed servers that deliver web content and media to users based on their geographic location.
Static Content: Files that are written once and not modified frequently, such as images, videos, HTML, CSS, and JavaScript files.
Geographically Distributed Cache: CDNs consist of multiple servers distributed across various geographic locations to reduce latency and improve performance.
Caching: The process of storing copies of files in a cache to serve future requests faster.
Benefits of CDNs: Improved performance, reduced load on the origin server, scalability, and geographic flexibility.
Push vs. Pull CDNs:
Push CDNs: Content is preemptively uploaded to the CDN servers.
Pull CDNs: Content is fetched from the origin server and cached on the CDN servers only when requested by a user.

## What Are Object Stores Used For?

**Answer**

Object Stores: Manage and store data as objects, designed for scalability, durability, and cost-effectiveness.
Key Features: Scalability, metadata, durability, availability, and cost-effectiveness.
Use Cases: Backup and archiving, content storage and delivery, big data and analytics, media and entertainment, and log and event data.
Examples: Amazon S3, Google Cloud Storage, Azure Blob Storage.
Comparison: Object stores vs. traditional storage solutions, with object stores being more suitable for large-scale, unstructured data storage.

## What is Load Balancing?

**Answer**

Load Balancing: Distributes incoming network traffic across multiple servers to improve performance, reliability, and availability.
Horizontal vs. Vertical Scaling: Horizontal scaling adds more servers, while vertical scaling adds more resources to a single server.
Load Balancing Algorithms: Round robin, weighted round robin, least connections, least response time, IP hash, layer 4, and layer 7 load balancing.
Consistent Hashing: Distributes requests across servers in a way that minimizes reassignment when servers are added or removed.
Fault Tolerance: Active-active and active-passive load balancing provide redundancy and high availability.

## Explain a bit about TCP vs. UDP?

**Answer**

TCP:
Connection-oriented protocol with reliable data transmission.
Uses flow control, congestion control, sequence numbers, and acknowledgements.
Suitable for applications requiring reliable data transmission (e.g., web browsing, email, file transfers).
UDP:
Connectionless protocol with simple and fast data transmission.
No built-in flow control or congestion control.
Supports multicast and is suitable for applications prioritizing speed and low latency (e.g., video conferencing, online gaming).

## Explain a bit about Long Polling, Websockets, Server Sent Events?

**Answer**

Long Polling: Suitable for applications where real-time updates are needed, but WebSockets or SSE are not feasible due to compatibility or other constraints. Examples include legacy systems or environments with strict firewall rules.
WebSockets: Ideal for real-time, bidirectional communication. Examples include chat applications, online gaming, and collaborative editing tools.
Server-Sent Events (SSE): Best for scenarios where the server needs to push updates to the client. Examples include live news feeds, stock price updates, and notifications.

## Explain a bit about Monolith Vs. Microservices?

**Answer**

Monolithic Architecture: A monolithic architecture is a traditional model where all the functionality of an application is packaged into a single, self-contained unit.
Characteristics:
Single Codebase: All functionalities reside in a single codebase.
Single Deployment: The entire application is deployed as a single unit.
Tightly Coupled: Components are often tightly coupled.
Advantages:
Simplicity: Easier to develop, test, and deploy for small to medium-sized applications.
Consistency: Shared environment and dependencies.
Performance: Fewer network calls between components.
Disadvantages:
Scalability: Difficult to scale individual components independently.
Maintenance: Harder to manage and maintain as the application grows.
Deployment: Requires redeploying the entire application for changes, leading to longer deployment times and increased risk of downtime.
Microservices Architecture: A microservices architecture breaks down an application into smaller, independent services, each responsible for a specific functionality.
Characteristics:
Decoupled Services: Each service is developed, deployed, and scaled independently.
Independent Deployment: Services can be deployed independently.
Technology Diversity: Different services can use different technologies, languages, and databases.
Advantages:
Scalability: Individual services can be scaled independently.
Flexibility: Faster development cycles with independent teams.
Resilience: Failure in one service does not bring down the entire application.
Disadvantages:
Complexity: Increased complexity in managing multiple services.
Deployment Overhead: Requires sophisticated deployment and orchestration tools like Docker and Kubernetes.
Monitoring and Debugging: More challenging across multiple services.
Technologies for Microservices
Docker:
Containerization: Packages an application and its dependencies into a container.
Isolation: Each microservice runs in its own container with its own dependencies and configurations.
Kubernetes:
Orchestration: Automated deployment, scaling, and management of containerized applications.
Desired State Management: Ensures the desired state of the application is maintained, handling failures and scaling automatically.
Key Takeaways
Premature Optimization: Avoid over-engineering your architecture. If your application does not require the scalability and flexibility of microservices, a monolithic architecture might be more appropriate.
Scale Appropriately: Choose the architecture that best fits your application's current and future needs. For large-scale applications, microservices provide the necessary scalability and resilience.

## How can you optimize the performance of a high-performing API to ensure a great user experience and efficient application operation?

**Answer**

Optimizing the performance of a high-performing API involves several strategies to ensure a great user experience and efficient application operation. Here are some key techniques:
Caching:
Description: Store frequently accessed data in a cache (like Redis or Memcached) for rapid retrieval, bypassing the database for repeated requests.
Benefits:
Drastically reduces database load.
Significantly improves response times.
Challenges:
Deciding on the right caching strategy (time-based, event-based, etc.).
Managing cache invalidation to ensure data consistency.
Scale-out with Load Balancing:
Description: Distribute incoming requests across multiple server instances using a load balancer (like Nginx or HAProxy).
Benefits:
Handles increased traffic and prevents a single server from becoming a bottleneck.
Improves reliability as requests can be routed to healthy instances if one fails.
Considerations:
Stateless applications are easier to scale horizontally.
Requires infrastructure to manage load balancers.
Asynchronous Processing:
Description: Acknowledge client requests immediately and process them in the background, sending results later.
Benefits:
Unblocks the client and improves perceived responsiveness.
Allows the API server to handle long-running tasks without delaying other requests.
Considerations:
Requires careful design to manage background tasks and notifications.
Not suitable for all API operations (e.g., real-time data updates).
Pagination:
Description: Limit the number of records returned per request and provide a way to retrieve subsequent pages.
Benefits:
Reduces response sizes, especially for large datasets.
Prevents excessive memory consumption on both client and server.
Implementation:
Use query parameters for page number and size.
Include metadata in the response (e.g., total records, next/previous page links).
Connection Pooling:
Description: Maintain a pool of reusable database connections instead of creating a new one for each request.
Benefits:
Minimizes the overhead of establishing new connections.
Significantly improves performance under high concurrency.
Implementation:
Most database libraries/frameworks offer built-in connection pooling mechanisms.
Additional Tips:
Optimize Database Queries: Ensure that database queries are efficient and make use of indexes.
Gzip Compression: Reduce response sizes by compressing data before sending it to the client.
Content Delivery Network (CDN): Cache static assets globally for faster delivery to users.
Monitor and Profile: Use tools like New Relic or Datadog to identify bottlenecks and monitor performance.

Requirements Gathering (5 Minutes):
Once the question is explained, clarify what's expected by asking:
🔹 Functional Requirements: Focus on core user functionalities.

- Example: Can users see the freshness of their feed?
- Example: Are we designing for one hotel chain or a multi-tenant booking platform?
- Example: Can users submit recurring tasks?

🔹 Non-Functional Requirements: Identify key aspects like:
▪️ High availability
▪️ Latency expectations
▪️ Fault tolerance
▪️ Consistency needs
Capacity Estimation (3 Minutes):
Quick and to the point:
▪️Expected QPS (Queries Per Second) and read/write ratio
▪️Storage and memory requirements
API Design (5 Minutes):
Outline the key APIs your system will offer:
▪️Endpoints, request, and response structures
▪️Importance of endpoint structure, e.g., PUT /api/user/{user_id}
Database Schema Design (10 Minutes):
Design your database thoughtfully:
▪️ SQL or NoSQL? Justify your choice.
▪️ Design tables/collections with clear relationships and data flow.
System Design Deep Dive (25 Minutes):
▪️This is where the magic happens. Keep referring back to your requirements and iteratively refine your design. Spend more time on topics like Cache, Queues, Sharding, Web sockets, Object Storage etc.
▪️ Core Infrastructure: Proxy, DNS, CDN, load balancers, servers, and storage.
▪️ Caching: Consider client-side, CDN, app-level, and database caching.
▪️ Communication: Use messaging queues, Kafka, and relevant protocols (gRPC, WebSockets).
▪️ Scaling: Decide on vertical/horizontal scaling strategies.
▪️ Database Optimizations: Focus on sharding, indexing, and partitioning.
▪️ Redundancy & Replication: Discuss backup strategies and primary/secondary setups.
▪️ Remember to address the interviewer's questions and suggest ways to future-proof the system.
Miscellaneous (3 Minutes):
If time permits, discuss:
▪️ Rate limiting
▪️ Privacy concerns
▪️ Authentication and permissions
▪️ Explore scenarios like changing a particular data source

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
