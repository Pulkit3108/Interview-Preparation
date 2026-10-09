# .NET

.NET and ASP.NET Core runtime, dependency injection, HTTP, hosting, and application lifecycle.

[Back to the question-bank index](../README.md)

## What is the difference between ASP.NET and ASP.NET Core?

**Answer**

**ASP.NET** commonly refers to the original web framework built on .NET Framework and `System.Web`. It is primarily tied to Windows and includes technologies such as Web Forms, ASP.NET MVC 5, and ASP.NET Web API 2.

**ASP.NET Core** is the newer, open-source, cross-platform framework for building web applications and HTTP APIs on modern .NET. It has a modular middleware pipeline, built-in dependency injection, flexible hosting, and configuration and logging abstractions. It supports multiple application styles, including Minimal APIs, controller-based APIs, Razor Pages, MVC, and Blazor; it is not built only on MVC.

## In .NET, what is the purpose of `Task.Run`?

**Answer**

`Task.Run` queues work to the thread pool and returns a `Task` representing that work. It is mainly useful for moving CPU-bound work away from a UI thread so the interface remains responsive.

It should not be used merely to wrap naturally asynchronous I/O. Database, file, and network APIs that already expose asynchronous methods should normally be awaited directly. In ASP.NET Core request handling, adding `Task.Run` usually consumes another thread without improving scalability.

## Describe the lifetime of dependencies in a Dependency Injection (DI) container.

**Answer**

The built-in .NET dependency injection container supports three primary lifetimes:

- **Transient:** creates a new instance each time the service is resolved. It suits lightweight, stateless services.
- **Scoped:** creates one instance per dependency-injection scope. In an ASP.NET Core application, the framework normally creates one scope per HTTP request.
- **Singleton:** creates one instance for the application container and reuses it for all resolutions.

A singleton must be thread-safe and must not directly capture a scoped service. Disposable services should be created and released by the container rather than manually retained beyond their intended lifetime.

## What is the purpose of `IHttpClientFactory`?

**Answer**

`IHttpClientFactory` centralizes the creation and configuration of `HttpClient` instances. It supports named and typed clients, integrates with dependency injection and logging, and pools underlying `HttpMessageHandler` instances. Handler pooling avoids unnecessary connection creation while periodically replacing handlers so clients can react to DNS changes.

The factory returns a new `HttpClient` object on each creation, but it manages and reuses the expensive handlers underneath. Applications can also attach delegating handlers for cross-cutting behavior such as authentication, tracing, or resilience policies.

## Does Entity Framework `DbContext` require a separate Unit of Work or Repository abstraction?

**Answer**

Not necessarily. Entity Framework's `DbContext` already behaves like a Unit of Work: it tracks changes across entity sets and persists them together through `SaveChanges`. `DbSet<TEntity>` provides repository-like access to an entity type.

A domain-specific repository can still be useful when it expresses meaningful aggregate operations, hides persistence details, or enforces domain boundaries. A generic repository that merely mirrors every `DbSet` operation often adds indirection without adding behavior or improving testability.

## Explain Event Sourcing, CQRS, a message bus, and MediatR.

**Answer**

- **Event Sourcing:** stores state changes as an append-only sequence of domain events. Current state is reconstructed by replaying events, often with snapshots for efficiency.
- **CQRS:** separates commands that change state from queries that read state. The read and write sides may share a database or use different models and stores.
- **Message bus:** transports messages between components or services, often asynchronously. Delivery guarantees, ordering, retries, and dead-letter handling depend on the chosen broker and configuration.
- **MediatR:** a .NET library that implements in-process mediator-style dispatch. It decouples a sender from request or notification handlers inside one process; it is not a network message broker.

These concepts can be combined, but none of them requires the others. Event sourcing and distributed messaging add substantial operational and consistency complexity, so they should be chosen for a concrete requirement rather than applied by default.

## What is IIS and what is it used for?

**Answer**

Internet Information Services (IIS) is Microsoft's web server for Windows. It can serve static content and host web applications such as classic ASP.NET applications.

For ASP.NET Core, IIS can host the application in process or act as a reverse proxy to the ASP.NET Core server. It can also provide process management, TLS termination, authentication integration, request filtering, logging, and application-pool isolation.

## What are physical, logical, and virtual cores?

**Answer**

- **Physical core:** an actual execution core on a processor package. A CPU socket can contain multiple physical cores.
- **Logical processor:** a hardware execution context visible to the operating system. With simultaneous multithreading, one physical core may expose multiple logical processors that share some core resources.
- **Virtual CPU (vCPU):** the processor resource exposed to a virtual machine. A hypervisor schedules vCPUs onto host logical processors. The exact relationship between a vCPU, a hardware thread, and available compute capacity depends on the cloud provider and instance type.

## What is the ASP.NET Core application lifecycle?

**Answer**

At a high level, an ASP.NET Core application has two related lifecycles:

1. **Host lifecycle:** the process builds the host, loads configuration, registers services, constructs the middleware pipeline, starts listeners and hosted services, and reports that the application has started. During graceful shutdown it stops accepting work, signals hosted services, disposes managed resources, and exits.
2. **Request lifecycle:** the server receives an HTTP request and passes it through the configured middleware in order. Routing selects an endpoint, middleware and the endpoint can short-circuit or produce a response, and control then unwinds back through earlier middleware before the response is completed.

Startup and shutdown work belongs in the host lifecycle. Per-request state belongs in scoped services or the request context, not in singleton application state.

## How do you configure CORS in an ASP.NET Core REST API?

**Answer**

Register a named policy and apply it through middleware or endpoint routing. Allow only the origins, methods, and headers the client needs.

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddCors(options =>
{
    options.AddPolicy("Frontend", policy =>
        policy.WithOrigins("https://app.example.com")
              .AllowAnyHeader()
              .AllowAnyMethod());
});

var app = builder.Build();

app.UseRouting();
app.UseCors("Frontend");
app.UseAuthorization();
app.MapControllers();
app.Run();
```

CORS is enforced by browsers and is not authentication or authorization. Avoid `AllowAnyOrigin` unless the API is intentionally public, and never combine a wildcard origin with credentialed requests.

## What is the ASP.NET Web Forms page lifecycle?

**Answer**

This is a **legacy ASP.NET Web Forms** concept, not the ASP.NET Core request lifecycle. A page moves through these broad stages:

1. **Page request and start:** ASP.NET determines whether it must compile or reuse the page and establishes request properties such as `IsPostBack`.
2. **Initialization:** controls are created and assigned IDs and themes.
3. **State restoration:** view state, control state, and postback data are loaded.
4. **Load:** the page and its controls load; application code commonly reads restored values here.
5. **Postback event handling:** control events and validation run for a postback.
6. **Pre-render and state saving:** final control changes are made, then view state and control state are saved.
7. **Render:** the page and controls write their markup to the response.
8. **Unload:** cleanup runs after the response is rendered; writing to the response is no longer appropriate.

Understanding the order matters because a control's state may not be available during early initialization and changes made after state saving will not be preserved for the next postback.

## References

- [ASP.NET Core fundamentals](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/)
- [.NET dependency-injection service lifetimes](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection/service-lifetimes)
- [Use `IHttpClientFactory` in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-requests)
- [Enable CORS in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/cors)
- [ASP.NET Web Forms page lifecycle](https://learn.microsoft.com/en-us/previous-versions/aspnet/ms178472(v=vs.100))
