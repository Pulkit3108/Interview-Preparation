# Observability

Telemetry, dashboards, latency, caches, flow control, and managed analytics tools.

[Back to the question-bank index](../README.md)

## What is Grafana?

**Answer**

Grafana is an observability and visualization platform that queries data from configured sources and
presents it through dashboards, exploratory views, and alerts. It can work with metrics, logs,
traces, SQL databases, and cloud monitoring services through built-in support and plugins.

Grafana is usually not the system that originally collects or stores all telemetry. For example, it
may query Prometheus metrics, Loki logs, or a cloud provider's monitoring service. A useful dashboard
starts from operational questions and service-level indicators rather than displaying every
available metric.

## Why should observability include ephemeral data stores such as caches?

**Answer**

A cache or in-memory grid can change both latency and correctness even though its data is temporary.
Observe hit and miss rates, request latency, errors, evictions, memory use, entry count, refresh age,
connection saturation, replication state, and fallback load on the source of truth.

The signals must be interpreted together. A high hit rate can still serve stale data, while a sudden
drop in hit rate can overload a database and cause a cascading failure. Include cache invalidation
and refresh events in traces or logs so an incident can be correlated with application behavior.

## What is the difference between average and percentile latency?

**Answer**

Average latency is total observed latency divided by request count. It is useful for aggregate cost
but can hide a slow tail.

The `p99` is the latency at or below which 99 percent of observations fall; roughly one percent are
slower. Percentiles show the distribution experienced by slower requests, but they require enough
samples and a correctly aggregated histogram. Track request rate and errors alongside several
percentiles, and do not average percentile values from separate instances or time windows.

## What are throttling, load shedding, buffering, and backpressure?

**Answer**

- **Throttling** limits admitted work to a configured rate or quota.
- **Load shedding** rejects or drops work when capacity is exhausted so the system can preserve core
  service.
- **Buffering** temporarily queues data to absorb short producer-consumer rate differences; an
  unbounded buffer only postpones failure.
- **Backpressure** signals or enforces that upstream producers slow down when downstream consumers
  cannot keep pace.

They are complementary controls. A resilient design uses bounded queues, explicit overload behavior,
timeouts, and metrics for saturation and rejected work.

## What is Zipkin?

**Answer**

Zipkin is a distributed-tracing system that receives spans, stores trace data, and provides a UI for
examining request paths and latency across services. Applications can instrument through
OpenTelemetry or compatible libraries and propagate trace context between calls. Sampling, storage
retention, attribute cardinality, and sensitive-data filtering must be configured deliberately.

## What is Splunk?

**Answer**

Splunk is a commercial platform for ingesting, indexing, searching, alerting on, and visualizing
machine data such as logs and events, with observability and security products around that platform.
It does not replace good telemetry design: emit structured events, control sensitive data and
cardinality, define retention, and build alerts from actionable service signals.

## References

- [Grafana overview](https://grafana.com/docs/grafana/latest/introduction/)
- [Grafana alert rules](https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/)
- [Zipkin documentation](https://zipkin.io/pages/quickstart.html)
- [Splunk documentation](https://docs.splunk.com/)
