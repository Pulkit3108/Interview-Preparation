# Docker

Docker containers, images, registries, isolation, and runtime behavior. For orchestration, see the
[Kubernetes questions](kubernetes.md).

[Back to the question-bank index](../README.md)

## What is Docker, and what principle is it based on?

**Answer**

Docker is a platform and toolchain for building, distributing, and running applications as
containers. A container is an isolated process with a packaged filesystem and runtime configuration.

On Linux, containers share the host kernel and use mechanisms such as namespaces for isolation and
control groups for resource governance. An image packages the application files and dependencies;
a container is a running instance of that image. Containers improve environment consistency, but
they do not provide the same isolation boundary as a separate virtual-machine kernel.

## How do images, registries, and containers support the build-ship-run workflow?

**Answer**

- **Build:** a Dockerfile describes how to create an image. Image layers are content-addressed and
  unchanged layers can be reused across builds and pulls.
- **Ship:** a registry stores image manifests and layers. Tags are convenient mutable names; a digest
  identifies immutable image content and is safer when exact reproducibility matters.
- **Run:** the container runtime starts an isolated process from the image plus runtime configuration
  such as environment variables, mounts, networks, and resource limits.

Images should contain application artifacts, not secrets. Runtime state that must survive container
replacement belongs in a volume or external service.

## Why are containers generally faster to start than virtual machines?

**Answer**

A container starts one or more processes while sharing the host kernel. A traditional virtual
machine must start a guest operating-system kernel and its supporting services, so it usually has a
larger memory footprint and slower startup.

Layer reuse can also reduce build and distribution time. This does not make every containerized
workload faster at runtime, and startup still depends on image size, initialization work, storage,
networking, and resource constraints.

## References

- [Docker overview](https://docs.docker.com/get-started/docker-overview/)
- [Docker image concepts](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/)
- [Kubernetes container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
