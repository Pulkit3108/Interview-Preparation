# Maven and Gradle

Java build lifecycles, dependency management, multi-module builds, performance, and migration.

[Back to the question-bank index](../README.md)

## What is the Maven build lifecycle?

**Answer**

Maven has three built-in lifecycles: `default` builds and deploys a project, `clean` removes prior
build output, and `site` produces project documentation. The default lifecycle includes ordered
phases such as `validate`, `compile`, `test`, `package`, `verify`, `install`, and `deploy`. Invoking a
phase runs that phase and all earlier phases in the lifecycle. Plugins bind goals to phases; packaging
type and configuration determine the actual work.

## How do you manage a multi-module Maven project and its dependencies?

**Answer**

Use an aggregator POM with `<modules>` to define the reactor and a parent POM for shared properties,
plugin configuration, and dependency management. Put versions in `<dependencyManagement>` and let
modules declare only dependencies they use. Keep module direction acyclic and publish stable internal
contracts. Aggregation and inheritance are separate features even when one POM performs both.

## How can you optimize a large multi-module Maven build?

**Answer**

Measure first with build scans/profiling and distinguish dependency resolution, compilation, tests,
packaging, and plugins. Build only the affected reactor with `-pl` and `-am`, use parallel builds only
for thread-safe plugins and isolated tests, cache dependencies in CI, and remove duplicate or
unnecessary plugin executions. Split slow integration tests deliberately and keep generated sources
incremental. Skipping verification is not a build-speed optimization for release pipelines.

## What is the structure and purpose of `pom.xml`?

**Answer**

The Project Object Model identifies the project (`groupId`, `artifactId`, `version`, `packaging`) and
declares dependencies, build plugins, repositories when necessary, properties, profiles, modules,
reporting, and project metadata. Maven combines the POM with parent inheritance, dependency
management, profiles, and the Super POM to produce the effective model. Inspect `help:effective-pom`
when configuration origin is unclear.

## How do Maven and Gradle differ?

**Answer**

Maven uses a declarative XML model and standardized lifecycles, favoring convention and predictable
project structure. Gradle uses Kotlin or Groovy build scripts with a task graph, rich customization,
incremental execution, build cache, and configuration-cache features. Either can build large Java
projects well; performance depends on build design, plugins, caching, and CI environment rather than
syntax alone.

## How do you choose between Maven and Gradle?

**Answer**

Consider existing ecosystem and team expertise, plugin maturity, required customization, IDE/CI
support, reproducibility, dependency governance, and measured build performance. Maven is attractive
for conventional builds and standardized organizational patterns. Gradle is attractive for complex
multi-language/task graphs and advanced caching. Avoid migrating solely for an assumed speed gain.

## What challenges arise when migrating between Maven and Gradle?

**Answer**

You must preserve dependency versions/scopes, source sets, generated code, annotation processing,
test suites, resource filtering, packaging, publishing metadata, signing, repositories, profiles,
plugin behavior, and CI/release commands. Transitive conflict resolution and custom plugin semantics
can differ. Compare artifacts, dependency graphs, tests, and publication in parallel before cutover.

## What are Maven's advantages?

**Answer**

Maven offers a widely understood lifecycle, strong convention, mature Java plugins, transitive
dependency management, reactor builds, reproducible declarative configuration, and broad IDE/CI
support. Trade-offs include verbose XML and awkward expression of highly custom workflows. Its value
comes from consistent models, not from avoiding all configuration.

## What is the difference between a local and a central Maven repository?

**Answer**

The local repository is a per-user cache and install target, normally under `~/.m2/repository` unless
configured otherwise. Maven Central is a public remote repository. Organizations commonly use a
repository manager that proxies public repositories and hosts private releases/snapshots. A remote
artifact is downloaded to the local cache after checksum and policy handling.

## What is the `.m2` directory?

**Answer**

The default `~/.m2` directory contains the local artifact repository and may contain `settings.xml`
with mirrors, proxies, profiles, and server identifiers. Credentials in settings should use supported
encryption or an external secret mechanism and must not be committed. Deleting the whole repository
is a costly troubleshooting step; remove only a confirmed corrupt artifact when necessary.

## References

- [Maven lifecycle reference](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
- [Maven POM reference](https://maven.apache.org/pom.html)
- [Gradle build lifecycle](https://docs.gradle.org/current/userguide/build_lifecycle.html)
- [Gradle performance guide](https://docs.gradle.org/current/userguide/performance.html)
