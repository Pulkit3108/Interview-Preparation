# Spring and Spring Boot

Spring Core, Spring Boot foundations, auto-configuration, dependency injection, profiles, and beans.

[Back to the question-bank index](../README.md)

## Topic Map

- [Spring Boot foundations and versions](#which-spring-boot-version-should-a-new-project-use)
- [Annotations, the application context, and dependency injection](#what-is-spring-application-context)
- [Auto-configuration, profiles, and beans](#what-is-the-difference-between-the-spring-boot-application-annotation-and-enable-auto-configuration-annotation)

## Which Spring Boot version should a new project use?

**Answer**

Use a currently supported stable release that is compatible with the organization's Java baseline and
dependency ecosystem, not an arbitrary version from an old tutorial. Spring Boot 3.x moved the
baseline to Java 17 and Jakarta EE namespaces; later major releases must be evaluated against their
published system requirements and the project's dependencies.

In an interview, name the version used by the project and explain why: support window, Java version,
Spring Framework generation, Jakarta namespace compatibility, security updates, and third-party
library support. Verify exact requirements in the
[official system requirements](https://docs.spring.io/spring-boot/system-requirements.html) and
[supported versions](https://github.com/spring-projects/spring-boot/wiki/Supported-Versions).

## What is the difference between spring vs spring boot?

**Answer**

Spring Framework supplies the IoC container, AOP, transactions, data integration, MVC/WebFlux, and
other application infrastructure. Spring Boot builds on it with opinionated auto-configuration,
dependency management, starters, executable packaging, externalized configuration, Actuator, and
tooling. Boot reduces setup; it does not replace or hide the need to understand Spring Framework.

## What are the advantages of Spring Boot Applications over traditional Spring Applications?

**Answer**

Spring Boot reduces manual assembly through conditional auto-configuration and curated dependency
management, packages servlet applications with embedded servers, externalizes configuration, and
provides Actuator and test support. Spring Initializr generates a compatible starting project. These
conventions improve delivery consistency, while explicit beans and properties can override defaults.

## How does Spring Boot simplify the deployment of a Web Application?

**Answer**

It can package the application and embedded server as an executable JAR with a consistent startup
entry point. Dependency management, auto-configuration, external properties, health/readiness,
metrics, graceful shutdown, and build-image support reduce platform glue. Deployment still needs an
explicit runtime, resources, secrets, network, observability, rollout, and rollback design.

## What are some of the updates and changes in Spring Boot 3?

**Answer**

Spring Boot 3 raised the Java baseline to 17, moved from Java EE `javax.*` APIs to Jakarta EE
`jakarta.*`, adopted Spring Framework 6, introduced first-class AOT/GraalVM native-image support,
and revised observability around Micrometer Observation/Tracing. It also upgraded its managed
ecosystem. These are migration boundaries, not a claim that every application becomes native,
containerized, or faster automatically.

## What challenges are faced when migrating from Spring Boot 2.7 to 3.x?

**Answer**

The major migration concerns are:

- Upgrade to Java 17 or later and move to compatible build tools and libraries.
- Replace Java EE `javax.*` APIs with Jakarta EE `jakarta.*` APIs where applicable.
- Upgrade to Spring Framework 6 and compatible Spring Security, Spring Data, and Spring Cloud lines.
- Review removed and deprecated configuration properties, auto-configurations, and APIs.
- Rework custom security configuration for the current component-based Spring Security model.
- Update observability code from older tracing integrations to Micrometer Observation and Tracing.
- Rebuild tests, generated code, serialization boundaries, and deployment images against the new
  runtime, then validate behavior and performance rather than relying on compilation alone.

Use the project's exact 2.7 patch version and follow the official migration guide incrementally.

## What is convention over configuration in Spring Boot?

**Answer**

Convention over configuration means Boot applies documented defaults and conditional beans from the
classpath, environment, and existing application beans. The application configures only deviations.
Back-off conditions let user-defined beans replace many defaults, while condition reports and metadata
make the resulting configuration inspectable.

## What are the ways to create Spring Boot Application?

**Answer**

Generate a Maven or Gradle project with Spring Initializr, use supported IDE integration, or configure
a build manually with the Boot parent/BOM and plugin. An organization may provide a vetted template.
Copying an old starter repository or relying on the historical Boot CLI can preserve stale versions,
so verify dependencies and support status.

## What are Starter Dependencies

**Answer**

Starters are dependency descriptors for a capability, such as `spring-boot-starter-web`,
`data-jpa`, `security`, `actuator`, or `test`. They combine commonly used libraries while Boot's BOM
manages compatible versions. Starters do not themselves enable every feature; auto-configuration
conditions and application settings determine runtime behavior.

## What are Spring Devtools? Can it cause any issue in the production environment?

**Answer**

DevTools improves local development with restart, LiveReload integration, and development-oriented
property defaults. It is automatically disabled for normal fully packaged application launch in
common setups, but dependency configuration should still keep it out of production artifacts and
remote DevTools must not be exposed. Maven commonly marks it optional; Gradle uses
`developmentOnly`.

## What is run method in Spring Boot Application

**Answer**

`SpringApplication.run` prepares the environment, determines the application type, creates and
refreshes the application context, registers sources/listeners, runs initializers and runners, and
starts an embedded server when applicable. It returns the context. For customization, configure a
`SpringApplication` or `SpringApplicationBuilder` before calling `run`.

## What is Spring Application Context?

**Answer**

`ApplicationContext` is Spring's feature-rich IoC container. It creates and wires bean definitions,
manages lifecycle, resolves resources/messages, publishes application events, exposes the
`Environment`, and integrates post-processors and AOP. It extends `BeanFactory`; common implementations
include annotation-based and web application contexts. Boot creates the appropriate context for the
application type.

## What are Annotations in Spring?

**Answer**

Spring uses annotations as metadata consumed by container, AOP, web, data, and Boot infrastructure.
Examples include stereotypes (`@Component`, `@Service`, `@Repository`, `@Controller`), bean
configuration (`@Configuration`, `@Bean`), injection (`@Autowired`, `@Qualifier`, `@Value`), web
mapping, transactions, and `@SpringBootApplication`. An annotation has behavior only when the
relevant processor or infrastructure is active.

## What are Stereotype Annotations in Java?

**Answer**

Stereotypes are component annotations discovered by scanning: `@Component` is generic;
`@Service`, `@Repository`, and `@Controller` express architectural roles. `@Repository` participates
in persistence-exception translation when the required post-processor is configured, and controllers
are detected by web infrastructure. Custom stereotypes can meta-annotate `@Component`.

## What is the difference between `@Repository`, `@Component`, and `@Service`?

**Answer**

All three register component-scan candidates. `@Component` is generic; `@Service` communicates
business/service-layer intent; `@Repository` communicates persistence intent and can enable
translation of supported persistence exceptions into Spring's `DataAccessException` hierarchy.
Choose the annotation that documents the role.

## What is the difference between @Service and @Repository?

**Answer**

`@Service` is a semantic specialization for service/business logic. `@Repository` marks a
persistence component and can trigger exception translation. Both are meta-annotated with
`@Component`, so both are injectable beans, but their roles and infrastructure semantics differ.

## Can `@Repository` and `@Service` be interchanged?

**Answer**

Both are detected as components, so basic injection may still work if swapped. Do not interchange
them: the stereotypes communicate architectural intent and `@Repository` has persistence-exception
translation semantics. Correct labeling also supports architecture tests and tooling.


## What are Qualifier markers in spring boot?

**Answer**

`@Qualifier` narrows autowiring candidates when multiple beans share a type. Put a qualifier at the
injection point and on the bean definition, or create a custom qualifier annotation for domain
meaning. `@Primary` supplies a default candidate, while a qualifier expresses explicit selection.

## What are Actuators in spring boot?

**Answer**

Spring Boot Actuator exposes production-oriented endpoints and integrations for health, information,
metrics, loggers, mappings, conditions, and more depending on configuration. Expose only required
endpoints, secure the management path or port, and define health groups for platform probes. Actuator
adds signals; it does not replace an observability backend.

## How does @Autowired annotation works?

**Answer**

`@Autowired` asks Spring to resolve constructor, method, or field dependencies primarily by type,
then by qualifier and candidate rules. A class with one constructor needs no annotation. Prefer
constructor injection for required dependencies; field injection hides requirements and makes plain
unit tests harder.

## Which method-level annotations define a custom Actuator endpoint?

**Answer**

Inside a class annotated with `@Endpoint`, use `@ReadOperation`, `@WriteOperation`, or
`@DeleteOperation` to expose technology-neutral operations. Web/JMX-specific variants exist when
needed. Endpoint IDs, inputs, output types, caching, exposure, and authorization must be configured
carefully.

## What is Dependency Injection in Spring?

**Answer**

Dependency injection supplies collaborators from outside an object rather than having it construct
concrete dependencies. Spring resolves bean definitions and wires them through constructors, methods,
or fields. DI makes requirements explicit, improves substitution and testing, and supports inversion
of control; it does not require every value to be a Spring bean.

## What are the different types of dependency injection in Spring Boot?

**Answer**

Constructor injection suits required dependencies and immutable fields. Setter or method injection
suits optional or reconfigurable dependencies. Field injection exists but hides requirements and
couples tests to the container. Spring also supports lookup/method injection for narrow lifecycle
cases.

## What is the difference between constructor injection and setter injection?

**Answer**

Constructor injection makes required dependencies impossible to omit and supports final fields and
plain construction in tests. Setter injection communicates optional or reconfigurable collaboration
but allows a temporarily incomplete object. Prefer constructors by default. Do not use setter
injection merely to hide a circular design; break the cycle or use a deliberate lazy boundary.

## How do @Autowired, @Resource and @Inject differ from each other?

**Answer**

`@Autowired` is Spring-specific, resolves primarily by type, and supports Spring qualifiers and
optional forms. `jakarta.inject.Inject` is a standard DI annotation with type-based resolution and
standard qualifiers. `jakarta.annotation.Resource` is name-oriented and commonly used on fields or
setters. Prefer constructor injection; a single constructor needs none of these in Spring.


## What is the difference between the Spring Boot Application Annotation and enable auto configuration annotation?

**Answer**

`@SpringBootApplication` combines Boot configuration, component scanning, and
`@EnableAutoConfiguration`, and is normally placed on the root application class. Using
`@EnableAutoConfiguration` alone enables only Boot's conditional auto-configuration; the application
must provide configuration/component scanning separately. Both support excluding auto-configuration,
but the composed annotation is the usual entry point.

## What is AutoConfiguration in spring boot?

**Answer**

Auto-configuration contributes beans when classpath, existing-bean, property, application-type, and
other conditions match. It backs off when the application supplies many of those beans. It is
opinionated conditional configuration, not runtime guessing, and can be inspected through the
conditions report or Actuator.

## What is the mechanism behind Spring Boot AutoConfiguration?

**Answer**

`@EnableAutoConfiguration` imports candidate auto-configuration classes. Current Boot libraries list
them in `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`; older
generations used `spring.factories`. `@AutoConfiguration` classes use conditions such as class,
bean, property, resource, and web-application checks, bind typed `@ConfigurationProperties`, and
usually back off for user beans. Ordering controls relative evaluation, not bean startup completion.

## How do you externalize configuration in your Spring Boot Application

**Answer**

Use `application.properties` or YAML, profile documents, environment variables, system properties,
command-line arguments, config trees, and imported remote/local sources as appropriate. Bind related
settings to validated `@ConfigurationProperties` records/classes instead of scattering `@Value`.
Keep secrets in a secret mechanism, not committed configuration, and understand property-source
precedence before overriding values.

## How will you exclude Auto Configuration and in how many ways can you do it?

**Answer**

Exclude a class with `@SpringBootApplication(exclude = ...)`,
`@EnableAutoConfiguration(exclude = ...)`, or the `spring.autoconfigure.exclude` property. Use the
`excludeName` form when the class cannot be referenced directly. `@SpringBootTest` does not itself
have a general auto-configuration `exclude` attribute; tests can supply the property, use an explicit
test application configuration, or apply test-slice-specific exclusion tools.

## What is @SpringBootTest Annotation

**Answer**

`@SpringBootTest` finds a Boot configuration and creates an application context for an integration
test. Its web environment can be `MOCK`, `RANDOM_PORT`, `DEFINED_PORT`, or `NONE`. It does not always
mean a real server or production-equivalent environment. Prefer narrower slice tests when a full
context is unnecessary, and use `RANDOM_PORT` when testing the actual network stack.

## What is the order of precedence in Spring Boot Configurations?

**Answer**

Spring Boot uses an ordered `Environment`; when two property sources define the same key, the
higher-precedence source wins. In practical terms, test overrides and command-line arguments can
override packaged configuration, external configuration can override configuration inside the jar,
and profile-specific files override their non-profile counterparts in the same location. Default
properties supplied through `SpringApplication` have low precedence.

The complete order includes additional sources and has changed across Boot generations, so use the
reference documentation for the version being interviewed. In a running application, the Actuator
`env` and `configprops` endpoints can help diagnose the effective value when exposed securely.

## How can you disable auto configuration in Spring Boot and override it?

**Answer**

Exclude an unwanted auto-configuration with `exclude` or `excludeName` on
`@SpringBootApplication`/`@EnableAutoConfiguration`, or with `spring.autoconfigure.exclude`.

To customize behavior, first prefer documented properties. If the relevant auto-configuration uses
`@ConditionalOnMissingBean`, supplying an application bean of the expected type makes that default
back off. An arbitrary bean with the same type or name does not universally override
auto-configuration, and bean-definition overriding is disabled by default. Use the condition report
to verify what matched.

## In which scenarios do we need to disable auto configuration?

**Answer**

Disable a specific auto-configuration only when the application deliberately replaces that entire
facility, a dependency activates configuration inappropriate for this application, or a narrow test
intentionally excludes it. Prefer removing an unused starter or configuring the feature first.
Exclusion can hide a dependency mistake and may remove more infrastructure than intended, so name
the exact class and verify startup and the conditions report.

## In which scenarios do we need to override auto configuration?

**Answer**

Customize it when the defaults remain useful but one collaborator, policy, or property set must
differ, such as a qualified `DataSource`, security chain, serializer, or client builder. Prefer
supported properties and customizer callbacks. Supply a bean only where the auto-configuration
documents a back-off condition. Excluding the whole auto-configuration is a different decision.

## What is the use of conditional annotation in auto configuration?

**Answer**

Conditional annotations activate configuration only when its assumptions are true. Common examples
are `@ConditionalOnClass`, `@ConditionalOnMissingClass`, `@ConditionalOnBean`,
`@ConditionalOnMissingBean`, `@ConditionalOnProperty`, and web-application or resource conditions.
They let libraries provide defaults without unconditionally taking control. Ordering and the phase
in which a condition is evaluated can affect what definitions are visible.

## How can you read properties from application.properties or application.yml

**Answer**

Use `@ConfigurationProperties` for a related, typed, and optionally validated group of settings.
Use `@Value` for a small isolated value or expression, and inject `Environment` when code genuinely
needs dynamic lookup. Constructor-bound configuration objects are easier to validate and test than
scattered field injection. Never log secrets read from configuration.

## Which has more priority application.properties or application.yml?

**Answer**

For files in the same location, Spring Boot gives `.properties` precedence over YAML. Using both can
therefore produce surprising partial merges; choose one format per location. Location, profile, and
the broader property-source order still determine precedence before the file-format tie is relevant.

## How can you change the application port in Spring Boot Application

**Answer**

Set `server.port` in properties, YAML, an environment variable, or a command-line argument:

```properties
server.port=9090
```

```bash
java -jar app.jar --server.port=9090
```

`SERVER_PORT=9090` is the relaxed-binding environment-variable form. A
`WebServerFactoryCustomizer` can set the port programmatically when configuration is insufficient.
A JVM option must precede `-jar`, for example `java -Dserver.port=9090 -jar app.jar`.

## What is the circular dependency issue?

**Answer**

A circular dependency exists when a bean eventually requires itself, such as `A -> B -> A`.
Constructor cycles cannot be constructed and fail context startup. Modern Boot applications also
disallow circular references by default. The preferred fix is to redesign responsibilities, extract
the shared collaboration, or communicate through an event or narrower boundary. `@Lazy` or a provider
can deliberately defer a dependency in rare cases, but switching to setter injection merely conceals
the design cycle and should not be the default remedy.

## How does Spring Boot supports internationalization in Microservices

**Answer**

Spring resolves messages through `MessageSource` bundles such as `messages.properties` and
`messages_fr.properties`. In an MVC application, locale resolution can use the request's
`Accept-Language` header, a cookie, or a session, depending on the configured `LocaleResolver`.
Resolve localized presentation text at the system boundary; internal services should normally
exchange stable codes and structured data. If locale must cross services, propagate an explicit,
validated locale rather than assuming every downstream service shares message bundles.

## What are Spring Profiles?

**Answer**

Profiles conditionally activate beans and configuration documents. Use `@Profile` for bean
definitions and `application-{profile}.properties` or YAML profile documents for values. Activate
them externally with `spring.profiles.active`; use profile groups where several profiles represent
one deployment mode. Profiles are useful for coherent environment variants, but ordinary tunable
values should remain properties rather than multiplying profiles.

## What would happen if 2 profiles are active simultaneously with conflicting configurations?

**Answer**

Both profiles are active, so beans guarded by either profile may be registered. For properties from
otherwise equivalent profile documents, later active profiles can override earlier ones, but the
overall property-source order still applies. Duplicate bean names normally cause startup failure
because bean-definition overriding is disabled by default; do not depend on profile order to choose
one. Make profile conditions mutually exclusive or use distinct bean names plus `@Primary` or
`@Qualifier` intentionally.

## How will you configure your Spring Boot Application to support different environments like dev, testing and prod? How would you manage the application properties of each of the environments?

**Answer**

Keep safe shared defaults in `application.properties` and environment-specific, non-secret values in
files such as `application-dev.properties` and `application-test.properties`. Activate the profile
outside the artifact. Supply deployment-specific values through environment/configuration services
and secrets through the platform's secret store. Build one immutable artifact for all environments,
validate required properties with `@ConfigurationProperties`, and avoid committing production
credentials or baking them into profile files.

## What is the default web server in Java? How to change it?

**Answer**

Java itself has no default web server. With Spring Boot's servlet web starter, the usual embedded
default is Tomcat. To use another server supported by the chosen Boot version, exclude the Tomcat
starter and add that server's starter. Reactive WebFlux commonly defaults to Reactor Netty. Available
alternatives and supported versions depend on the Boot release, so confirm them in its dependency
documentation.

## What is the Spring Bean Life Cycle?

**Answer**

At a high level, the container creates the bean, injects dependencies, invokes relevant `Aware`
callbacks, runs `BeanPostProcessor` callbacks before initialization, invokes initialization callbacks
such as `@PostConstruct`, and then runs post-processors after initialization. The exposed object may
be a proxy returned by a post-processor. On orderly context shutdown, destruction callbacks such as
`@PreDestroy` run for managed singleton beans. Spring does not manage the complete lifecycle of a
prototype after returning it to the caller.

## What is the difference between configuration component scan and bean annotation?

**Answer**

`@Configuration` marks a class that declares bean definitions and enables full configuration-class
semantics by default. `@ComponentScan` discovers annotated component classes in selected packages.
`@Bean` registers the object returned by a factory method and is useful for explicit construction or
third-party types. They solve different concerns and can be combined; `@SpringBootApplication`
already includes configuration and component scanning from its package downward.

## How can we handle multiple Beans of the same type?

**Answer**

Use `@Qualifier` at the injection point to select a semantic variant, or mark one candidate
`@Primary` as the default. `@Resource(name = ...)` can select by name. Injecting `List<T>` or
`Map<String,T>` intentionally receives all matching beans, with `@Order`/`Ordered` controlling list
order. Prefer meaningful qualifiers over relying on parameter or field names.

## How would you implement custom scope in Spring Beans?

**Answer**

Implement `org.springframework.beans.factory.config.Scope`, including object retrieval/removal,
destruction callbacks, contextual resolution, and a conversation identifier. Register it before
scoped beans are created, commonly with a `CustomScopeConfigurer`, then use `@Scope("name")`.
Define ownership, concurrency, cleanup, and context propagation explicitly. When a shorter-lived bean
is injected into a singleton, use a scoped proxy or provider so resolution occurs in the active
scope.

## What annotations we use for adding scope to Beans

**Answer**

Use `@Scope(ConfigurableBeanFactory.SCOPE_SINGLETON)` or
`@Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE)` for core scopes. Web applications can use the
composed `@RequestScope`, `@SessionScope`, and `@ApplicationScope` annotations. `@Scope("custom")`
selects a registered custom scope. The composed web annotations also configure an appropriate proxy
mode.

## How can I modify the Bean Life Cycle using Hooks?

**Answer**

For one bean, prefer `@PostConstruct`/`@PreDestroy` or `@Bean(initMethod=..., destroyMethod=...)`;
`InitializingBean` and `DisposableBean` couple the class to Spring. A `BeanPostProcessor` can wrap or
change bean instances around initialization, while a `BeanFactoryPostProcessor` changes bean
definitions before ordinary beans are created. Use global processors sparingly because ordering and
early initialization can affect the entire context.

## What is the difference between BeanFactory and Application Context?

**Answer**

`BeanFactory` is the core bean registry and dependency-resolution contract. `ApplicationContext`
extends it with application events, message resolution, resource loading, environment support, and
automatic discovery of important processors. Contexts normally pre-instantiate non-lazy singleton
beans, while a bare factory generally creates them on demand. Modern applications almost always use
an `ApplicationContext`; AOP is not accurately summarized as simply unavailable to every
`BeanFactory`.

## Describe a scenario where you will use Bean Factory over Application Context?

**Answer**

Direct `BeanFactory` use is uncommon. It can be appropriate in framework or container internals that
need only programmatic bean registration and lookup and deliberately do not want context services.
For an application, use `ApplicationContext` and configure lazy initialization where justified;
choosing a bare factory merely because a system is resource-constrained usually loses useful
infrastructure without addressing the real footprint.

## How will you make sure that a certain bean is loaded last in the application context?

**Answer**

There is no reliable global "last bean" contract. `@DependsOn` enforces that named dependencies are
initialized first and destroyed later, but only within that relationship. `SmartInitializingSingleton`
runs a callback after regular singleton pre-instantiation, not necessarily after every lazy bean or
application phase. For startup work, choose the semantic hook you need, such as an application event,
`ApplicationRunner`, `CommandLineRunner`, or `SmartLifecycle`.

## What are the different Spring Bean scopes we have?

**Answer**

Core scopes are singleton, one instance per bean definition per container, and prototype, a new
instance for each container lookup or injection request. Web-aware contexts add request, session,
application, and WebSocket scopes. The historical global-session scope belonged to portlet
environments and should not be presented as a normal modern servlet scope. Custom scopes may also be
registered.

## Can you explain the difference between Single and Prototype scope in Spring Bean?

**Answer**

A singleton is one object per bean definition per container and is the default. It must be safe for
concurrent callers if used that way. A prototype is created whenever the container resolves it, but
Spring does not manage its destruction afterward. Injecting a prototype directly into a singleton
does not create one per method call; use `ObjectProvider`, a lookup method, or a scoped proxy for
dynamic retrieval. User-session state belongs in session scope, not prototype scope.

## How can you instantiate a bean in Java Programming Spring?

**Answer**

Register a component discovered by scanning, return an object from an `@Bean` method, import
configuration, or define it through functional or XML registration when appropriate. The container
instantiates registered definitions and injects them into consumers. Prefer constructor injection;
programmatic `ApplicationContext.getBean(...)` is useful at integration boundaries but is usually a
service-locator smell in domain code.

## References

- [Spring Boot reference documentation](https://docs.spring.io/spring-boot/reference/)
- [Spring Boot externalized configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html)
- [Spring Framework bean scopes](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html)
- [Spring Framework container extension points](https://docs.spring.io/spring-framework/reference/core/beans/factory-extension.html)
