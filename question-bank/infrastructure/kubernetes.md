# Kubernetes

Kubernetes orchestration, node components, and logging.

[Back to the question-bank index](../README.md)

## What is the difference between Docker and Kubernetes?

**Answer**

Docker provides tools for building images and running containers. Kubernetes orchestrates
containerized workloads across multiple nodes. It schedules Pods, reconciles desired state, manages
rollouts, and supplies abstractions for networking, configuration, and storage.

Kubernetes runs containers through a Container Runtime Interface compatible runtime such as
containerd or CRI-O; it does not require Docker Engine. Docker and Kubernetes therefore address
different concerns rather than being interchangeable products.

## How do the kubelet and container runtime write logs on a node?

**Answer**

The kubelet is the node agent that reconciles Pod specifications and communicates with the container
runtime through the Container Runtime Interface (CRI). Application containers should normally write
to standard output and standard error. The runtime writes those streams using the CRI log format,
and the kubelet exposes the current log through the Kubernetes API used by `kubectl logs`.

For node-level system components:

- on a Linux node using `systemd`, the kubelet and container runtime normally write to `journald`;
- without `systemd`, they normally write files under `/var/log`; and
- the kubelet manages container-log rotation settings, while a node logging agent commonly forwards
  logs to durable centralized storage.

Exact service and file names depend on the operating system, runtime, and cluster distribution, so
operators should verify the node's configured services instead of assuming Docker-specific paths.

## References

- [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
- [Kubernetes logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
