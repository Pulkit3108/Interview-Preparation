# Node.js

Node.js asynchronous programming, streams, Express, and data access.

[Back to the question-bank index](../README.md)

## How do you handle promises in Node.js?

**Answer**

Promises can be consumed with `.then()` and `.catch()`, but `async`/`await` usually makes multi-step asynchronous control flow easier to read. Use `try`/`catch` around awaited operations when the current layer can handle or enrich the error; otherwise, let the rejection propagate to a centralized error handler.

The main promise combinators have different completion rules:

- `Promise.all()` fulfills when every input fulfills and rejects when the first input rejects. It does not cancel the remaining operations.
- `Promise.allSettled()` waits for every input and returns each fulfillment or rejection outcome.
- `Promise.race()` settles with the first input to settle.
- `Promise.any()` fulfills with the first input to fulfill and rejects only if every input rejects.

```js
async function loadDashboard(userId) {
  try {
    const [profile, notifications] = await Promise.all([
      loadProfile(userId),
      loadNotifications(userId),
    ]);

    return { profile, notifications };
  } catch (error) {
    throw new Error(`Unable to load dashboard for ${userId}`, { cause: error });
  }
}
```

## What are streams in Node.js?

**Answer**

Streams process data incrementally instead of loading an entire payload into memory. They are useful for files, HTTP bodies, compression, and network traffic.

- **Readable:** produces data, such as `fs.createReadStream()`.
- **Writable:** consumes data, such as `fs.createWriteStream()`.
- **Duplex:** can be read from and written to, such as a TCP socket.
- **Transform:** a duplex stream that converts data, such as `zlib.createGzip()`.

Streams also support **backpressure**, which prevents a fast producer from overwhelming a slower consumer. Prefer `stream.pipeline()` or its promise-based form when connecting streams because it forwards errors and cleans up the pipeline.

```js
import { createReadStream, createWriteStream } from "node:fs";
import { pipeline } from "node:stream/promises";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream("input.log"),
  createGzip(),
  createWriteStream("input.log.gz"),
);
```

## What is Express, and what does it provide?

**Answer**

Express is a small web framework for Node.js. It builds on Node's HTTP primitives and provides:

- routing by HTTP method and path;
- an ordered middleware pipeline for concerns such as authentication, logging, validation, and body parsing;
- helpers for requests and responses;
- static-file and template-engine integration; and
- centralized error-handling middleware.

Middleware order matters because each function can handle the request, modify it, pass control with `next()`, or report an error. Route handlers should validate untrusted input, return deliberate status codes, and pass unexpected errors to the application's error boundary.

## How would you connect a Node.js service to a database?

**Answer**

The exact API depends on the database and driver, but a production service should follow the same basic approach:

1. Choose a maintained driver or ORM appropriate for the database.
2. Read the connection configuration from environment or secret management, never from committed source.
3. Create a bounded connection pool during application startup and reuse it across requests.
4. Use parameterized queries or the ORM's safe query API, and use transactions when multiple writes must succeed atomically.
5. Manage schema changes with migrations and expose a health check that distinguishes application health from database readiness.
6. Close the pool during graceful shutdown.

Database access should live in a dedicated repository or data-access layer rather than being mixed directly into HTTP route handlers. This keeps transport, business logic, and persistence concerns separate and easier to test.

## References

- [Node.js promises](https://nodejs.org/api/globals.html#class-promise)
- [Node.js streams](https://nodejs.org/api/stream.html)
- [Express routing](https://expressjs.com/en/guide/routing.html)
- [Express middleware](https://expressjs.com/en/guide/using-middleware.html)
