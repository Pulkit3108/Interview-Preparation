# REST and HTTP API Design

HTTP semantics, resource modeling, security, performance, and REST/SOAP trade-offs.

[Back to the question-bank index](../README.md)

## Which HTTP status code represents a missing resource?

**Answer**

`404 Not Found` means the server did not find a current representation of the target resource or is
not willing to disclose that it exists. `410 Gone` is more explicit when the resource is known to be
permanently removed.

## Which HTTP status-code range indicates a client-associated error?

**Answer**

`400` through `499` are 4xx responses. They indicate that fulfilling the request requires a client
change or condition, such as malformed syntax (`400`), missing/invalid authentication (`401`), denied
authorization (`403`), missing resource (`404`), conflict (`409`), or rate limit (`429`). They do not
necessarily mean the end user personally made a mistake.

## What is idempotence for an HTTP method?

**Answer**

A method is idempotent when multiple identical requests have the same intended effect on server state
as one request. GET, HEAD, PUT, DELETE, OPTIONS, and TRACE are defined as idempotent; POST and PATCH
are not guaranteed to be. Responses may differ across repetitions, and implementations must still
handle concurrent requests and side effects such as logging.

## How do GET and POST differ?

**Answer**

GET retrieves a representation and is safe, idempotent, cacheable by default semantics, and normally
places selection data in the URI. POST submits data for resource-specific processing and is neither
safe nor inherently idempotent; it commonly creates a subordinate resource or invokes an operation.
Payload presence is not the fundamental distinction, though GET request content has no generally
defined semantics and poor interoperability.

## What are limitations of GET requests?

**Answer**

GET must not be used for state-changing actions, query data appears in URLs and related logs/history,
and practical URI-size limits vary across clients and intermediaries. Complex or sensitive searches
may use a POST-based query resource when a URI cannot represent the request safely. GET responses can
be cached, so personalized data needs correct cache controls and variation.

## How do you make GET endpoints secure?

**Answer**

Use HTTPS, authenticate when required, authorize access to the exact resource, validate and bound all
parameters, use parameterized database queries, prevent object-level authorization failures, and set
appropriate cache and content-security headers. Do not put secrets or bearer tokens in URLs. Apply
rate limits and audit sensitive reads. GET being read-only does not make it harmless.

## What is PATCH and when should it be used?

**Answer**

PATCH applies a partial modification described by a media type such as JSON Patch or JSON Merge
Patch. Define supported operations, validation, null/removal semantics, and concurrency protection
with ETags/`If-Match`. PATCH is not inherently idempotent, although a particular patch document can
be. Use PUT when replacing the complete resource representation is the clearer contract.

## Which response formats can an HTTP API return?

**Answer**

Any registered or documented media type can be returned: JSON, XML, HTML, plain text, CSV, images,
PDF, Protocol Buffers, and others. Use `Content-Type` to describe the representation and HTTP content
negotiation (`Accept`) when multiple formats are supported. Do not infer format solely from a filename
extension.

## How do safe and idempotent HTTP methods differ?

**Answer**

A safe method is intended only for retrieval and has no requested state-changing semantics: GET,
HEAD, OPTIONS, and TRACE. An idempotent method may change state, but repeating it has the same intended
effect as one call. All safe methods are idempotent; PUT and DELETE are idempotent but not safe.

## What is REST and what are good API practices?

**Answer**

REST is an architectural style built around resources, representations, uniform interfaces,
stateless requests, cacheable responses, layered components, and optional code-on-demand. For HTTP
APIs, model stable resources and identifiers, honor method/status/cache semantics, version or evolve
contracts compatibly, validate input, provide consistent errors and pagination, and document with
examples. Not every HTTP JSON API fully implements REST, and that label is less important than a
coherent contract.

## How do you secure REST APIs?

**Answer**

Use TLS, strong authentication, resource-level authorization with deny-by-default policy, short-lived
scoped credentials, input/schema validation, output encoding, payload limits, rate limiting, safe
CORS/CSRF policy, secret rotation, dependency hygiene, and audit/monitoring. Prevent mass assignment
and object-level authorization flaws. Gateways add defense in depth but the owning service must enforce
authorization.

## How do you optimize REST APIs?

**Answer**

Set a latency objective, trace the request, and optimize the measured bottleneck. Bound and paginate
collections, reduce representation size, use compression and conditional caching, fix N+1 queries and
indexes, pool connections, batch safe work, and move long-running operations behind asynchronous job
resources. Protect dependencies with deadlines, cancellation, load shedding, and bounded retries.
Verify improvement with load tests and tail latency.

## What is HATEOAS?

**Answer**

Hypermedia as the Engine of Application State means responses include links or action controls that
tell clients which transitions are currently available. It can reduce hard-coded workflow knowledge
and improve discoverability, but requires stable relation semantics, media types, and client support.
Adding arbitrary URLs to JSON without transition meaning is not the full constraint.

## How do REST and SOAP differ?

**Answer**

REST is an architectural style often implemented directly with HTTP resources and multiple media
types. SOAP is an XML messaging protocol with envelopes, faults, WSDL contracts, and optional WS-*
standards for security, reliable messaging, and transactions. REST/JSON is often simpler for web APIs;
SOAP remains useful where formal enterprise contracts and WS-* interoperability are required.

## What are SOAP's advantages and disadvantages?

**Answer**

Advantages include formal WSDL/XSD contracts, standardized faults, mature enterprise tooling, and
optional WS-Security/reliable-messaging specifications. Costs include verbose XML, complex standards
and tooling, heavier processing, and less natural use of HTTP resource/cache semantics. Security and
reliability still depend on correct configuration.

## What role do HTTP methods play in a REST API?

**Answer**

Methods express standardized intent: GET retrieves, POST submits/creates according to the target,
PUT replaces, PATCH partially modifies, DELETE removes, HEAD retrieves metadata, and OPTIONS reports
communication options. Correct safe/idempotent/cache semantics let clients, retries, gateways, and
caches behave predictably.

## What does statelessness mean in REST?

**Answer**

Each request contains the information needed to understand and authorize it; the server does not rely
on hidden conversational state from previous requests. The server can still persist resource state,
and authentication can use a server-side session identified by a cookie. Statelessness concerns the
request protocol, not whether the backend stores data.

## What is an authorization token and how is it created?

**Answer**

An access token is a credential issued by a trusted authorization server after an authenticated and
authorized flow. It may be opaque or a signed JWT and represents a bounded audience, scope, subject,
and lifetime. Applications should use established OAuth/OIDC libraries and key management rather than
inventing tokens. Resource servers must validate issuer, audience, expiry, signature/introspection,
and permissions.

## What are REST API advantages and disadvantages?

**Answer**

HTTP-based resource APIs have broad tooling, simple interoperability, cache support, and independent
client/server evolution when contracts are stable. Limitations include over/under-fetching, manual
workflow discovery, inconsistent conventions between APIs, and weak guarantees if schemas and errors
are undocumented. REST does not inherently provide messaging reliability, transactions, or security.

## How would you model endpoints for products, orders, and users?

**Answer**

Use nouns and ownership boundaries, for example `GET /products/{productId}`, `POST /orders`,
`GET /orders/{orderId}`, and `GET /users/{userId}/orders?cursor=...`. Creating an order accepts product
IDs, quantities, shipping/payment references, and an idempotency key; the server calculates trusted
price and status. Use subresources only for true containment, expose state transitions explicitly,
authorize every object, and avoid leaking internal table structure.

## What can cause a connection timeout?

**Answer**

Causes include wrong DNS/address/port, routing or firewall drops, exhausted ephemeral ports or
connection pools, an overloaded/unavailable listener, proxy/load-balancer issues, TLS setup counted in
an overall timeout, or network packet loss. Distinguish DNS, connect, TLS, write, response/read, pool-
acquisition, and total deadlines using timestamped client/server/edge evidence.

## How should an API return a very large resource?

**Answer**

Avoid materializing it fully in memory. Paginate records, stream bytes with backpressure, support
range requests or resumable downloads when appropriate, compress compatible content, and generate
expensive exports asynchronously into object storage with a short-lived authorized download URL.
Declare size limits, cancellation, checksums, timeout behavior, and failure recovery.

## When should data be a path parameter versus a query parameter?

**Answer**

Path segments identify a resource within the hierarchy, such as `/orders/{orderId}`. Query parameters
modify the view or selection, such as filters, sort, fields, locale, or pagination. Keep identifiers
stable and required in the path; use optional/combinable controls in the query. Neither location is
appropriate for secrets, and authorization must not depend on obscurity.

## How should a Spring API implement file upload and storage?

**Answer**

Accept `multipart/form-data` with explicit count and byte limits, stream rather than buffering large
files, generate server-side object IDs, and validate authorization, media type from content, filename,
and malware policy. Store large bytes in object/blob storage and keep metadata, ownership, checksum,
status, and object key in the database; database BLOBs are reasonable only when transactional and size
requirements justify them. Upload to a temporary/quarantine location, scan, then publish atomically.
Use short-lived signed URLs or an authorized streaming endpoint for download.

## References

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 5789: PATCH](https://www.rfc-editor.org/rfc/rfc5789)
- [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700)
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
