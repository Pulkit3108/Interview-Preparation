# Apache Kafka

Kafka architecture, producers, consumers, partitions, delivery semantics, operations, and design.

[Back to the question-bank index](../README.md)

## What is a Message Queue?

**Answer**

A message queue or event broker lets producers publish work without waiting for consumers to process
it immediately. This decouples availability and scaling between components and can provide buffering,
retry, and retention.

Delivery, durability, and ordering are product- and configuration-specific. Do not assume that every
queue is durable or globally ordered. Kafka, for example, orders records within a partition.

## What is Apache Kafka, and what are its core components?

**Answer**

Apache Kafka is a distributed event-streaming platform built around append-only partition logs.

- **Producer:** publishes records to topics.
- **Consumer:** fetches records and tracks progress with offsets.
- **Broker:** stores partitions and serves producer and consumer requests.
- **Topic:** a named stream divided into partitions.
- **Partition:** the unit of ordering, storage distribution, and consumer parallelism.
- **Replica:** a copy of a partition on another broker.
- **Leader and followers:** the leader handles partition reads and writes; followers replicate it.
- **KRaft controller quorum:** stores cluster metadata and performs controller elections in current
  Kafka releases. Kafka 4.0 removed ZooKeeper mode; ZooKeeper belongs only in legacy-version or
  migration discussions.

## Explain the difference between a topic, partition, and segment.

**Answer**

- A **topic** is the logical named stream to which producers send records and from which consumers
  read.
- A **partition** is an ordered append-only log within a topic. It is Kafka's unit of storage
  distribution, replication, ordering, and consumer-group parallelism. Each record has an offset
  meaningful only within that partition.
- A **segment** is a bounded group of files used to store part of one partition on disk. Kafka rolls
  segments so retention, compaction, indexing, and deletion can operate on manageable files.

Adding partitions can increase parallelism but changes key-to-partition mapping and does not create a
global order across the topic. A consumer group can actively process at most one consumer per
assigned partition.

## How does Kafka internally work?

**Answer**

Producers serialize records and choose a topic partition. The partition leader appends each record to
an ordered log split into segment files, and followers replicate that log. Consumers fetch records
and store offsets per consumer group; Kafka does not remove a record merely because it was consumed.
Retention or compaction determines when stored records are removed.

The KRaft controller quorum owns cluster metadata and controller elections. Replication, batching,
sequential disk I/O, page-cache use, and zero-copy transfer where applicable support Kafka's
throughput. Log compaction is an optional topic policy, not Kafka's general write-ahead mechanism.

## How does Kafka ensure message ordering?

**Answer**

Kafka orders records by offset **within one partition**, not across an entire topic. Use a stable key
when all events for one entity must reach the same partition. The partition leader establishes the
log order and followers replicate it.

Producer retries and multiple in-flight requests can affect ordering unless idempotence and related
producer settings are configured correctly. Consumers should process a partition sequentially when
the business operation depends on order; dispatching records to an unordered worker pool can lose
the guarantee after consumption. Adding partitions can also change future key placement.

## What is a consumer group in Kafka?

**Answer**

A consumer group is a set of consumers that share work for one group identifier. For a subscribed
topic, each partition is assigned to at most one member of that group at a time. A separate group has
its own assignments and offsets and can read the same records independently.

Membership or partition changes can trigger reassignment. If a consumer stops heartbeating or fails
to poll within the configured interval, its partitions are reassigned. Processing may pause during
the transition and records may be seen again depending on when offsets were committed. Adding more
consumers than partitions creates idle consumers rather than additional parallelism.

## How does Kafka achieve fault tolerance?

**Answer**

- Partitions are replicated across brokers; one replica is leader and the others follow.
- The in-sync replica set (ISR) tracks replicas sufficiently caught up with the leader.
- The KRaft controller quorum manages metadata and leader elections in current Kafka versions.
- With `acks=all`, a producer waits for acknowledgements required by the broker from the current ISR.
  `min.insync.replicas` defines how many in-sync replicas must be available for the write to succeed.
- Unclean leader election should remain disabled when consistency is more important than
  availability because electing an out-of-sync replica can lose acknowledged records.
- Replication provides fault tolerance. Retention and log compaction are separate storage policies.

## Explain Kafka's partitioning strategy and how it impacts performance.

**Answer**

A producer's partitioner chooses the partition, commonly from an explicit partition, a hash of a
non-null key, or a batching strategy for unkeyed records. A custom partitioner can encode domain
routing but becomes a compatibility contract.

More partitions increase potential producer, broker, and consumer-group parallelism, but also add
metadata, files, replication traffic, and rebalance work. Hot or low-cardinality keys can overload one
partition while others are idle. Choose keys from the ordering and co-location requirement, measure
skew and throughput, and size partitions for both current load and expected consumer parallelism.

## Describe Kafka's consumer offset management.

**Answer**

An offset identifies a record's position within one partition. A consumer's current position is local
state; a **committed offset** is the recovery checkpoint stored for the consumer group, normally in
Kafka's `__consumer_offsets` topic.

Automatic commit is convenient but can commit work before the application has completed it. With
manual commits, commit the next offset only after the relevant processing succeeds. Committing before
the side effect risks loss; committing after it permits replay after a crash, so external operations
should be idempotent. Rebalances require pending work and offset commits to be coordinated with
partition revocation.

## Explain the concept of exactly-once semantics (EOS) in Kafka.

**Answer**

Kafka's exactly-once support is scoped, not a universal end-to-end guarantee:

- idempotent producers prevent duplicate records caused by producer retries within their supported
  session and configuration;
- transactions atomically write records to Kafka partitions and can include consumed offsets;
- consumers must use `read_committed` to hide aborted transactional records;
- a Kafka read-process-write pipeline can therefore make its Kafka output and input-offset commit
  atomic.

External databases, APIs, email, and other side effects still require their own idempotency,
transaction, or deduplication design. Kafka cannot make an arbitrary external side effect exactly
once by itself.

## How would you monitor and optimize Kafka performance in a production environment?

**Answer**

Metrics Collection: Use JMX, Prometheus, and Grafana to collect and visualize Kafka metrics.
Key Metrics to Monitor: Track broker metrics (request latency, request rate, under-replicated partitions, disk usage), producer metrics (record send rate, record error rate, batch size), consumer metrics (lag, fetch rate, commit latency), and topic/partition metrics (message rate, partition size).
Alerting: Configure alerts using Prometheus Alertmanager and custom alerts for critical metrics.
Broker Configuration: Optimize replication factor, log retention, and compression settings.
Producer Configuration: Optimize batch size, linger time, retries, and enable idempotence.
Consumer Configuration: Optimize fetch size, max poll records, and session timeout.
Topic and Partition Management: Ensure an appropriate number of partitions and address data skew.
Hardware and Infrastructure: Use high-performance disks, ensure sufficient network bandwidth, and allocate adequate memory and CPU resources.

Establish a baseline before tuning, change one control at a time, and validate producer durability and
consumer-processing semantics after every performance change. Consumer-group failure and rebalancing
are covered in the dedicated consumer-group questions below.

## How would you design a Kafka-based system to guarantee data consistency in the event of node failures?

**Answer**

Start from the required failure tolerance rather than copying one fixed configuration:

- place replicas across independent failure domains and choose an appropriate replication factor;
- use `acks=all` and set `min.insync.replicas` so a write fails instead of silently reducing the
  required durability during replica loss;
- enable producer idempotence and use transactions for Kafka-to-Kafka atomic processing when needed;
- commit offsets only after processing succeeds, or include offsets in the Kafka transaction;
- make external side effects idempotent, commonly with a stable event identifier, inbox/outbox
  pattern, or database constraint;
- monitor ISR shrinkage, offline partitions, controller quorum health, produce failures, and consumer
  lag; test broker and network failures rather than relying on configuration alone.

This increases consistency and durability but cannot guarantee availability during every failure.

**Further reading**

- [Kafka 4.1 upgrade guide: ZooKeeper removal](https://kafka.apache.org/41/getting-started/upgrade/)
- [Kafka KRaft operations](https://kafka.apache.org/41/operations/kraft/)

## What are the advantages of Kafka?

**Answer**

Kafka combines durable retained logs with scalable producers and independent consumers. Its main
advantages are:

- partitions distribute storage and processing across brokers and consumer-group members;
- replication and leader election tolerate configured broker failures;
- retention lets slow or new consumers replay data independently rather than deleting a record after
  the first read;
- batching and sequential log I/O support high throughput;
- keyed partitions preserve per-key ordering; and
- Kafka Connect and Kafka Streams support integration and stream-processing use cases.

These benefits carry trade-offs: partition planning, consumer rebalances, eventual replication,
operational capacity, and at-least-once side effects must be designed explicitly. Kafka is not the
best default for a simple low-volume task queue or request-response workflow.

## How do you create a topic in Kafka using the Confluent CLI?

**Answer**

After selecting the intended authenticated Kafka cluster, create a topic with an explicit design:

```bash
confluent kafka topic create orders \
  --partitions 6 \
  --config retention.ms=604800000
```

The exact supported flags depend on the installed Confluent CLI version and whether the target is
Confluent Cloud or Platform, so confirm with `confluent kafka topic create --help`. Choose partition
count, replication behavior, retention or compaction, and authorization deliberately; creating a
topic with arbitrary defaults is not production design.

## Explain the role of the Schema Registry in Kafka.

**Answer**

A schema registry stores versioned schemas under subjects and can enforce configured compatibility
rules before accepting a new version. Confluent Schema Registry supports Avro, JSON Schema, and
Protobuf and integrates with serializers that place a schema identifier in the wire payload.

It enables producers and consumers in different languages to share an explicit contract and evolve
it deliberately. It does not validate arbitrary bytes already in Kafka unless clients or broker-side
controls use the schema-aware format. Subject naming, compatibility mode, schema references,
authorization, and deletion policy are part of the contract and governance design.

## How do you register a new schema in the Schema Registry?

**Answer**

First choose the subject naming convention and compatibility mode. Check compatibility before
registration, then register through the schema-aware serializer, an approved client, the CLI, or the
registry REST API. The registry returns an identifier for the schema version.

In delivery pipelines, treat schemas as reviewed versioned artifacts and run compatibility checks
before deployment. Do not embed production credentials or unescaped schema JSON directly in an
ad-hoc shell command; use the platform's authenticated tooling and a file or client library.

## What is the importance of key-value messages in Kafka?

**Answer**

A record key commonly determines partition placement, so records with the same key reach the same
partition and can retain per-key order. Keys also drive grouping, joins, aggregations, table semantics,
and log compaction in stream-processing applications.

A key does not automatically deduplicate records or make processing idempotent. It also does not
directly assign consumers; Kafka assigns whole partitions to group members. Choose a stable,
well-distributed business key and plan for hot keys and for the partition-mapping changes that can
occur when the partition count increases.

## Describe a scenario where using a random key for messages is beneficial.

**Answer**

For independent telemetry records with no per-entity ordering or grouping requirement, distributing
records across partitions improves parallelism and avoids a hot business key. A random key can
approximate that distribution.

However, a random key becomes part of the record and defeats key-based compaction or later grouping.
When no semantic key exists, sending a null key and allowing the producer's batching-aware default
partitioner is often better than generating random data solely for routing. Measure the resulting
partition skew rather than assuming perfect balance.
## When should related messages use the same key?

**Answer**

Use the same **business key**, not one constant for the entire topic, when related events need the
same partition. For an order stream, use `orderId` for creation, payment, shipment, and status events.
Events for one order then retain partition order while different orders can be processed in parallel.

A single literal key for every record would send the whole topic to one partition and create a
bottleneck. Per-key ordering also requires the consumer to preserve order during processing and does
not by itself make external side effects consistent.
## Write a simple Kafka producer that sends JSON to a topic.

**Answer**

The example intentionally serializes JSON before calling Kafka so serialization failure is separated
from broker delivery failure:

```java
public class JsonKafkaProducer {
    public static void main(String[] args) {
        // Kafka producer configuration settings
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        // Create a Kafka producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(props);
        // Create a JSON object
        Map<String, Object> jsonMessage = new HashMap<>();
        jsonMessage.put("id", 1);
        jsonMessage.put("name", "John Doe");
        jsonMessage.put("email", "john.doe@example.com");
        try {
            // Convert the JSON object to a string
            ObjectMapper objectMapper = new ObjectMapper();
            String jsonString = objectMapper.writeValueAsString(jsonMessage);
            // Create a producer record
            ProducerRecord<String, String> record = new ProducerRecord<>("json-topic", jsonString);
            // Send the JSON message to the Kafka topic
            producer.send(record);
            System.out.println("Sent message: " + jsonString);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Close the producer
            producer.close();
        }
    }
}
```

## How do you serialize a custom object before sending it to a Kafka topic?

**Answer**

Use a standard schema format and maintained serializer where possible. A custom serializer must have
a stable binary contract, deterministic error behavior, and tests for compatibility. A minimal
producer configuration looks like this:

```java
public class CustomObjectProducer {
    public static void main(String[] args) {
        // Kafka producer configuration settings
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, UserSerializer.class.getName());
        // Create a Kafka producer
        KafkaProducer<String, User> producer = new KafkaProducer<>(props);
        // Create a custom object
        User user = new User(1, "John Doe", "john.doe@example.com");
        // Create a producer record
        ProducerRecord<String, User> record = new ProducerRecord<>("users-topic", user);
        // Send the custom object to the Kafka topic
        producer.send(record);
        System.out.println("Sent message: " + user);
        // Close the producer
        producer.close();
    }
}
```

## Describe how you can handle serialization errors in Kafka producers.

**Answer**

Exception Handling in Custom Serializer:
Try-Catch Block: Implement proper exception handling within the custom serializer to catch and handle serialization errors.
Logging: Log the error details for debugging and monitoring purposes.
Fallback Mechanism: Implement a fallback mechanism to handle the error, such as sending a default value or skipping the problematic message.
Producer Callback:
Asynchronous Send with Callback: Use the send method with a callback to handle errors that occur during the send operation. The callback provides information about the success or failure of the send operation.
Error Handling in Callback: Implement error handling logic within the callback to handle serialization errors and take appropriate actions.
Error Handling in Producer Configuration:
Retries: Configure the producer to retry sending messages in case of transient errors. This can be done using the retries configuration property.
Error Handling Policies: Define error handling policies such as dead-letter topics to handle records that cannot be serialized or sent successfully after deliberate retry handling.

Serialization normally occurs before the broker send, so retrying the same invalid object will not
help. Do not silently replace invalid data with a default value. Record a safe error summary and
route the original business input through an explicit remediation path when policy permits it.

## Write a Kafka consumer that reads JSON into a custom object.

**Answer**

```java
public class JsonKafkaConsumer {
    public static void main(String[] args) {
        // Kafka consumer configuration settings
        Properties props = new Properties();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "json-consumer-group");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, UserDeserializer.class.getName());
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        // Create a Kafka consumer
        KafkaConsumer<String, User> consumer = new KafkaConsumer<>(props);
        // Subscribe to the topic
        consumer.subscribe(Collections.singletonList("users-topic"));
        // Poll for new messages
        try {
            while (true) {
                ConsumerRecords<String, User> records = consumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String, User> record : records) {
                    User user = record.value();
                    System.out.println("Received message: " + user);
                }
            }
        } finally {
            // Close the consumer
            consumer.close();
        }
    }
}
```

## How do you handle deserialization errors in Kafka consumers?

**Answer**

Exception Handling in Custom Deserializer:
Try-Catch Block: Implement proper exception handling within the custom deserializer to catch and handle deserialization errors.
Logging: Log the error details for debugging and monitoring purposes.
Fallback Mechanism: Implement a fallback mechanism to handle the error, such as returning a default value or skipping the problematic message.
Error Handling in Consumer Poll Loop:
Try-Catch Block: Wrap the consumer poll loop in a try-catch block to catch and handle any exceptions that occur during message consumption and deserialization.
Error Handling Logic: Implement error handling logic within the catch block to take appropriate actions, such as logging the error, sending the message to a dead-letter queue (DLQ), or retrying the operation.
Dead-Letter Queue (DLQ):
DLQ: Use a dead-letter queue to handle messages that cannot be deserialized. When a deserialization error occurs, send the problematic message to a separate Kafka topic designated as the DLQ for further analysis and processing.
Error Handling Configuration:
Kafka Consumer Configuration: Configure the Kafka consumer with appropriate error handling settings, such as enable.auto.commit set to false to manually control offset commits and avoid committing offsets for problematic messages.

## Explain the process of deserializing messages into custom objects.

**Answer**

Define the Custom Object:
Create a class representing the custom object you want to deserialize the messages into.
Implement the Custom Deserializer:
Create a class that implements the org.apache.kafka.common.serialization.Deserializer interface. This class will define how to convert the byte array back into the custom object.
Configure the Kafka Consumer:
Configure the Kafka consumer to use the custom deserializer for the value (or key) of the messages.
Consume and Deserialize Messages:
Use the Kafka consumer to read messages from the topic and deserialize them into the custom object using the custom deserializer.

## Describe a scenario where multiple consumer groups are used for a single topic.

**Answer**

Suppose an `orders` topic feeds inventory projection, customer notification, fraud analysis, and
analytics. Give each independent application its own group identifier. Every group can then read the
full topic at its own pace, while instances inside one group divide that group's partitions.

Do not place unrelated applications in one group merely to share a topic: they would divide records
instead of each receiving every order. Each application still needs its own retry, idempotency,
offset, and failure policy.

## How does Kafka ensure load balancing among consumers in a group?

**Answer**

The group coordinator and assignment protocol distribute subscribed partitions so each partition has
one active consumer within the group. Assignment strategies include range, round-robin, sticky, and
cooperative-sticky behavior, each with different balance and movement trade-offs.

Joining or leaving consumers, subscription changes, and partition changes can cause reassignment.
Heartbeats and poll progress help detect failed or stalled members. Cooperative rebalancing can
reduce stop-the-world movement, but consumers still need correct revocation and offset handling.
Assignment balances partition counts, not necessarily work: skewed keys or partitions can leave one
consumer much busier than another.

## Explain how you can work with CSV data in Kafka, including serialization and deserialization.

**Answer**

Define the CSV dialect and schema first: column order, quoting, escaping, character encoding, null
representation, header behavior, and schema version. Use a mature CSV library rather than splitting
on commas because quoted fields may contain commas, quotes, or line breaks.

A producer can serialize a validated record to UTF-8 bytes or a string and publish it with a stable
key. The consumer parses the same contract and treats malformed rows according to an explicit policy,
such as a dead-letter topic with safe diagnostic metadata.

CSV is fragile for evolving event contracts because it carries little type information. Avro,
Protobuf, or JSON Schema with a schema registry is often safer for service-to-service events. If CSV
is required for an external integration, version the contract and test compatibility with real
fixtures.

## How do Kafka and RabbitMQ differ?

**Answer**

Kafka is a partitioned retained log. Consumer groups track offsets and can replay retained events
independently. It suits durable event streams, high-throughput integration, and stream processing
where partition-based ordering and replay are valuable.

RabbitMQ is a message broker centered on exchanges, bindings, and queues. It supports flexible
routing and acknowledgement-based work distribution and is often a natural fit for task queues and
brokered messaging patterns.

Neither product has one universal throughput, latency, ordering, or delivery guarantee. Kafka orders
within a partition; RabbitMQ ordering can be affected by multiple consumers, priority, and redelivery.
Both can redeliver, so consumers should be idempotent. Choose using routing needs, replay and
retention, ordering scope, operational expertise, failure behavior, and measured workload rather than
the simplistic label "stream" versus "queue."

## References

- [Apache Kafka documentation](https://kafka.apache.org/documentation/)
- [Kafka design](https://kafka.apache.org/documentation/#design)
- [Confluent Schema Registry fundamentals](https://docs.confluent.io/platform/current/schema-registry/fundamentals/)
- [RabbitMQ reliability guide](https://www.rabbitmq.com/docs/reliability)
