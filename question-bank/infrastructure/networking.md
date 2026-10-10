# Networking and Web Security

Networking, HTTP, DNS, authentication, authorization, tokens, and troubleshooting.

[Back to the question-bank index](../README.md)

## What do common HTTP status codes mean?

**Answer**

HTTP status codes are grouped by class:

- `1xx` is informational, such as `100 Continue` and `101 Switching Protocols`.
- `2xx` indicates successful handling: `200 OK`, `201 Created`, `202 Accepted`, `204 No Content`,
  and `206 Partial Content`.
- `3xx` concerns redirection or cache validation: `301 Moved Permanently`, `304 Not Modified`, and
  `307 Temporary Redirect`. Unlike `302` in common historical client behavior, `307` preserves the
  request method and body.
- `4xx` reports a client-side request problem: `400 Bad Request`, `401 Unauthorized` (authentication
  is required or failed), `403 Forbidden` (the server refuses the authenticated or understood
  request), `404 Not Found`, `409 Conflict`, and `429 Too Many Requests`.
- `5xx` reports server-side failure: `500 Internal Server Error`, `502 Bad Gateway`, `503 Service
  Unavailable`, and `504 Gateway Timeout`.

Choose the code from the actual outcome and API contract; do not return `200` with an error only in
the response body.

## Explain WebSockets.

**Answer**

WebSocket provides a persistent, full-duplex message channel between a client and server. A web
client begins with an HTTP handshake and, when the server accepts the upgrade, both sides exchange
WebSocket frames over the connection without making a new HTTP request for every message.

It suits interactive applications such as chat and live collaboration. Production designs still
need authentication, origin validation, message limits, heartbeat and reconnect behavior,
backpressure, horizontal-scaling strategy, and protection from idle or abusive connections.

## What is socket programming?

**Answer**

Socket programming uses an operating-system socket API to communicate between processes, either on
one host or across a network.

A TCP server creates a socket, binds an address, listens, accepts connections, reads and writes byte
streams, and closes resources. A TCP client creates a socket and connects. UDP uses datagrams and
normally sends or receives without establishing a reliable stream. Real code must handle partial
reads and writes, timeouts, concurrent clients, framing, cleanup, and network failures.

## How can 2 processors communicate?

**Answer**

The answer depends on what "processors" means and how they are connected:

- cores or processes on one machine can communicate through shared memory, pipes, local sockets, or
  message queues, with synchronization where state is shared;
- processors in an embedded system may communicate over hardware interconnects such as SPI, I2C, or
  a system bus; and
- separate machines communicate through network protocols, direct messages, or a broker.

Choose based on latency, throughput, ordering, failure isolation, consistency, and whether the
participants share memory. Shared memory can be fast but requires careful synchronization; message
passing provides clearer isolation but adds serialization and transport costs.

## Explain CORS, HTTPS, Rate Limiting.

**Answer**

- **CORS** is an HTTP-header mechanism that lets a server relax a browser's same-origin read
  restrictions for selected origins, methods, and headers. The browser enforces it; CORS is not API
  authentication and does not stop non-browser clients.
- **HTTPS** is HTTP over TLS. It provides confidentiality and integrity in transit and authenticates
  the server when certificate validation succeeds.
- **Rate limiting** restricts accepted operations by an identity, client, resource, or other key over
  time. It protects capacity and reduces abuse, but it is only one layer of denial-of-service
  defense.

## What is HTTPS?

**Answer**

HTTPS is HTTP carried over TLS. During the TLS handshake, the client validates the server certificate
and both peers negotiate protocol parameters and derive session keys. HTTP data is then encrypted
and integrity-protected in transit.

HTTPS protects the connection, not the endpoints. It does not make application input trustworthy,
prevent an authorized server from mishandling data, or replace authentication and authorization.
Modern deployments should disable obsolete SSL/TLS versions, automate certificate renewal, redirect
HTTP deliberately, and use HSTS only after understanding its operational effect.

## What are TCP/IP and UDP?

**Answer**

- **IP** addresses and routes packets between networks. It is best-effort and does not guarantee
  delivery, ordering, or uniqueness. IPv4 uses 32-bit addresses and IPv6 uses 128-bit addresses.
- **TCP** provides an ordered, reliable byte stream between two endpoints. It uses connection setup,
  acknowledgments, retransmission, flow control, and congestion control. Applications must define
  their own message framing on top of the byte stream.
- **UDP** sends independent datagrams without built-in connection establishment, retransmission, or
  ordering. It has lower protocol overhead and lets an application choose any reliability behavior
  it needs.

"UDP is faster" is not a universal rule. Protocol choice depends on loss tolerance, latency goals,
message boundaries, congestion behavior, and whether a higher-level protocol such as QUIC supplies
reliability over UDP.

## What is Authentication and Authorization?

**Answer**

**Authentication** establishes which principal is making a request, using evidence such as a
password plus MFA, a certificate, a session, or a signed assertion.

**Authorization** decides whether that principal may perform a particular action on a particular
resource in the current context. RBAC, ABAC, ACLs, and policy engines are authorization mechanisms.

Authentication normally precedes user-specific authorization, but a system can also authorize
anonymous public access. A valid identity must never be treated as permission to do everything.

## What are the different types of Authentication Techniques?

**Answer**

Authentication factors are commonly grouped as something the user **knows** (password or PIN),
**has** (security key or device), or **is** (biometric). MFA combines independent factors; two
passwords are not MFA.

Systems may use passwords, passkeys/WebAuthn, one-time passwords, client certificates, federated
OpenID Connect or SAML assertions, Kerberos tickets, or device identities. SSO is an authentication
experience across services, not a factor. OAuth 2.0 is primarily an authorization framework;
OpenID Connect adds an authentication layer.

Security questions are weak because answers are often guessable or discoverable. Risk signals such
as device and location can inform step-up authentication but should not silently become the only
proof of identity.

## What is an Auth Token and what does it contain?

**Answer**

An authentication or authorization token is a credential issued after an identity or grant has been
validated. Its contents depend on its type. An opaque token may be only a random identifier whose
state lives on the server. A JWT may carry protected metadata and claims such as issuer (`iss`),
subject (`sub`), audience (`aud`), expiry (`exp`), and scopes.

Not every token has a JWT header, payload, and signature, and a token should not contain unnecessary
personal or secret data. The receiving service must validate the token according to the protocol and
authorize the requested operation; merely decoding it is not validation.

## What is the difference between access tokens and refresh tokens?

**Answer**

An **access token** is presented to a resource server and represents delegated authorization. It is
normally short-lived and restricted by audience and scope. Although bearer tokens are common, sender-
constrained access tokens also exist.

A **refresh token** is presented only to the authorization server to obtain a new access token. It is
usually longer-lived, more sensitive, and may be rotated after use. A client does not send it to
ordinary API endpoints.

Token format, lifetime, and scope are authorization-server policies rather than universal fixed
values. Browser applications should not default to `localStorage` for either credential; choose a
backend-for-frontend, protected cookie, memory, or platform secure storage based on the client and
threat model.

## What is JWT?

**Answer**

A JWT is a compact claims format. A signed JWT (JWS) commonly contains three Base64URL-encoded
parts separated by dots: protected header, claims payload, and signature or MAC. The signature
protects integrity and authenticity; it does **not** encrypt the claims. Anyone who obtains a signed,
unencrypted JWT can decode its header and payload.

JWT is a format, not an authentication protocol. OAuth 2.0 access tokens may be JWTs or opaque
tokens, and OpenID Connect ID tokens are JWTs.

## How does a server create a signed JWT?

**Answer**

After the relevant authentication or authorization flow succeeds, the issuer constructs a protected
header and a minimal claims set. It includes appropriate issuer, subject, audience, issue and expiry
times, and any required authorization claims. A maintained JOSE library Base64URL-encodes the parts
and signs them with an approved key and algorithm.

The issuer should manage key rotation, publish verification keys where appropriate, use short
lifetimes, and never place secrets in an unencrypted JWT payload. Application code should not
implement signing or JSON serialization by hand.

## How does a server verify a JWT?

**Answer**

Use a maintained JWT library and pin the allowed algorithm; never trust the token's `alg` value as
the policy. Verify the signature or MAC with the correct key, then validate at least expiration,
not-before time, issuer, and audience as required by the application. Validate token type and scopes
or roles separately before authorizing the operation. Reject malformed, unsigned, expired, wrong-
issuer, wrong-audience, or otherwise invalid tokens.

## What are the disadvantages of JWTs?

**Answer**

- Claims make JWTs larger than opaque identifiers and are sent on every request that carries them.
- Signed payloads are readable, so sensitive data can be exposed to anyone who obtains the token.
- Authorization data can become stale until expiry because a self-contained token does not require a
  server lookup.
- Immediate revocation needs short lifetimes, a deny list, key or session state, introspection, or
  another design that reduces the stateless advantage.
- A stolen bearer token can be replayed until it expires or is rejected.
- Algorithm selection, key rotation, issuer and audience validation, and claim interpretation add
  security complexity.

Use a JWT only when its distributed verification or claims portability solves a real requirement.
An opaque session identifier is often simpler for a first-party web application.

## Where do you store a JWT Token?

**Answer**

There is no universally correct location; it depends on the client and threat model.

- For browser applications, prefer a backend-for-frontend or an `HttpOnly`, `Secure`, appropriately
  scoped `SameSite` cookie so JavaScript cannot read the credential. Cookie-based authentication
  still needs CSRF defenses appropriate to the chosen `SameSite` policy and workflow.
- Avoid storing access tokens, refresh tokens, session identifiers, or other credentials in
  `localStorage` or `sessionStorage`; any JavaScript running after an XSS flaw can read them.
- In-memory storage limits persistence but does not make a token immune to malicious JavaScript.
- Native and mobile applications should use the platform's protected credential storage.

Keep access tokens short-lived, rotate refresh tokens where supported, minimize claims, use HTTPS,
and plan revocation or session termination.

**Further reading**

- [OWASP JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

## How do you use JWTs to protect API endpoints?

**Answer**

Use a maintained framework integration rather than a custom token parser. For each request, extract
the expected bearer credential, verify its signature with a trusted key and pinned algorithm, and
validate issuer, audience, expiry, not-before time, and token type. Map validated scopes or claims to
the endpoint's authorization policy.

Return `401` when authentication is absent or invalid and `403` when a valid principal lacks
permission. Keep authorization checks server-side, use TLS, avoid logging tokens, and test malformed,
expired, wrong-audience, insufficient-scope, and rotated-key cases. Token issuance belongs to a
trusted authorization service, not every resource endpoint.

## What is a DDoS attack?

**Answer**

A distributed denial-of-service attack uses many sources to exhaust network bandwidth, protocol
state, compute, dependencies, or application capacity so legitimate users cannot be served. Attacks
may be volumetric, target network or transport behavior, or resemble valid application requests.

Mitigation is layered: provider-level scrubbing and anycast capacity, CDN or edge filtering,
rate and concurrency limits, caching, bounded queues, timeouts, load shedding, autoscaling with cost
controls, and tested incident procedures. Application rate limiting alone cannot absorb an attack
that saturates the upstream network link.

## How will you secure Web APIs?

**Answer**

- authenticate callers with a protocol appropriate to the client, then authorize every operation and
  object using least privilege;
- require TLS and protect credentials and sensitive data in storage and logs;
- validate request shape, size, type, and allowed values; use parameterized data access and safe
  output encoding at the relevant sink;
- set body, concurrency, rate, and time limits and use bounded resource consumption;
- manage secrets and signing keys outside source code and rotate them safely;
- return deliberate errors without leaking internals;
- log security-relevant decisions with correlation identifiers while redacting sensitive content;
  and
- test dependency vulnerabilities, authorization boundaries, abuse cases, and failure behavior.

An API gateway can centralize some controls, but it cannot replace authorization and validation in
the service that understands the business resource.

## How can you implement SSO?

**Answer**

Use a trusted identity provider and a standard authentication protocol, normally OpenID Connect for
modern applications or SAML for an existing enterprise federation requirement. Register each relying
party with exact redirect URIs, establish trust and keys, and use a maintained protocol library.

The application must validate the issuer, audience, signature, nonce or request correlation, time
claims, and redirect state required by the protocol, then create its own appropriately protected
session. Plan logout, account linking, provisioning, MFA, key rotation, and emergency access.
OAuth 2.0 alone delegates access and is not an SSO authentication protocol.

## What are the different protocols you can use to implement SSO?

**Answer**

- **OpenID Connect:** authentication and identity federation built on OAuth 2.0; common for modern
  web, mobile, and API ecosystems.
- **SAML 2.0:** XML-based federation widely used for enterprise browser SSO.
- **Kerberos:** ticket-based network authentication common inside managed enterprise domains.
- **WS-Federation:** older web identity-federation protocol still present in some enterprise systems.

OAuth 2.0 supports delegated authorization and often participates in an OpenID Connect SSO flow, but
it is not authentication by itself. LDAP is a directory access protocol; it can support credential
validation or identity lookup but is not itself a browser SSO protocol.

## How can you implement OAuth2? What challenges might you face in its implementation?

**Answer**

Set Up Authorization Server: The authorization server is responsible for authenticating users and issuing access tokens.
Configure Resource Server: The resource server hosts the protected resources and validates access tokens to authorize requests.
Register Client Applications: Client applications need to be registered with the authorization server to obtain client credentials.
Choose a flow for the client type. Use authorization code with PKCE for browser, native, and other
public clients; use client credentials only for suitable machine-to-machine access. The OAuth 2.0
Security Best Current Practice says clients should not use the implicit grant and prohibits the
resource-owner password-credentials grant.
Challenges:
Security: Ensuring token security and preventing token leakage.
Token Management: Managing token expiration, revocation, and refresh tokens.
User Authentication: Integrating with existing authentication systems.
Scalability: Handling high traffic and concurrent requests.
Compliance: Ensuring compliance with OAuth2 specifications.
User Experience: Providing a seamless authorization flow.

**Further reading**

- [OAuth 2.0 Security Best Current Practice (RFC 9700)](https://www.rfc-editor.org/rfc/rfc9700.html)

## What is the difference between OAuth and SSO?

**Answer**

OAuth 2.0 is an authorization framework: a client obtains an access token representing delegated
permission to call a resource server. SSO is a user experience in which one identity-provider session
authenticates the user to multiple applications.

They are not alternatives at the same layer. OpenID Connect adds authentication to OAuth 2.0 and can
provide SSO. SAML can also provide SSO without OAuth. A button labeled "Sign in with ..." should use
an authentication protocol such as OpenID Connect, not infer identity from an OAuth access token
intended for another API.

## What is RBAC?

**Answer**

Role-based access control assigns permissions to roles and roles to principals. A permission should
describe an action on a resource, while a role groups permissions around a job function or service
responsibility.

RBAC reduces per-user permission management but can produce role explosion when decisions depend on
resource ownership, tenant, location, time, or other attributes. In those cases, combine coarse roles
with resource-level or attribute-based policy. Enforce authorization on the server and default to
deny when no policy grants access.

## How would you remotely troubleshoot a non-technical user's Internet connection?

**Answer**

Use simple questions to isolate the failing layer, changing one thing at a time:

1. Establish scope: does the problem affect one website, one application, one device, or every
   device on the home network?
2. Check physical state: power and provider-status lights, cables, airplane mode, and connection to
   the expected Wi-Fi network.
3. Compare another device on the same Wi-Fi and the same device on mobile data. This separates a
   device problem from a router or provider problem.
4. Check the provider's outage status. If there is no outage, restart the affected device and then
   power-cycle the modem or router using the vendor's normal procedure.
5. On a computer, inspect whether it received a plausible local address, gateway, and DNS server.
   Test the gateway, then a known IP address, then a hostname to distinguish local, upstream, and DNS
   failures. Remember that some hosts block ping.
6. Record exact error messages and escalate to the provider when the external link or modem remains
   unhealthy.

Avoid immediately factory-resetting the router; that erases provider and Wi-Fi configuration and can
make remote recovery harder.

## How would you troubleshoot when some websites open but others do not?

**Answer**

Record the affected URLs and exact browser errors, then compare:

- the same site in a private window or another current browser;
- the same site from another device on the same network; and
- the same device through a different network, such as mobile data.

Check system time, DNS resolution, TLS certificate errors, browser extensions, proxy or VPN state,
parental or security filtering, and whether IPv4 and IPv6 behave differently. Browser developer tools
or `curl -v` can show redirects, DNS, connection, TLS, and HTTP status details.

Do not broadly disable the firewall or antivirus, bypass certificate warnings, or permanently change
DNS before evidence points there. If every local device fails only through one provider path, collect
the failing domain and time and escalate a DNS or routing case to the provider or site operator.

## What if the issue is with the Wi-Fi itself?

**Answer**

Confirm the device is connected to the intended SSID, then test next to the access point. Compare
another device and, if possible, a wired connection. This distinguishes radio coverage from an
Internet-uplink failure.

For weak or intermittent Wi-Fi, inspect signal level, access-point placement, interference, band
selection, channel congestion, and roaming between mesh nodes. Reconnect or forget and rejoin the
network only after confirming the password is available. Apply vendor-supported firmware updates
through a trusted local connection.

A factory reset is a last resort only after recording ISP, router, SSID, security, and mesh settings
and confirming someone can restore them locally.

## What if the issue is due to a VPN?

**Answer**

Compare the same request with the VPN connected and disconnected, if organizational policy permits.
If only the VPN path fails, record the client error, selected gateway, time, and affected destination.

Check tunnel status, route and DNS configuration, split-tunnel policy, proxy settings, client version,
account or device compliance, and whether the target blocks the VPN's egress address. Changing to an
approved gateway can distinguish one unhealthy gateway from a policy problem. For a corporate VPN,
do not replace it with an unapproved service or weaken leak protection; provide the evidence to the
organization's support team.

## You opened a URL and it's not opening. What could be the cause?

**Answer**

Work through the request path instead of guessing:

1. Parse and verify the URL, scheme, host, port, and path.
2. Resolve the hostname and compare the returned addresses with the expected DNS records.
3. Test route and TCP connectivity to the destination port.
4. Inspect the TLS handshake, certificate name, trust chain, validity, and local clock.
5. Inspect the HTTP response, redirects, proxy behavior, and browser console or network errors.
6. Compare another client, network, and region to separate local policy, ISP routing, CDN, and origin
   failures.

Likely causes include DNS failure, routing or firewall policy, proxy or VPN configuration, a closed
port, TLS mismatch, server outage, redirect loop, authentication, rate limiting, geographic policy,
or a browser extension. Preserve the exact error and request time before changing caches or settings.

## What is DNS?

**Answer**

DNS is a hierarchical distributed database that maps names to typed records. A client normally asks a
recursive resolver, which uses its cache or follows referrals from root to top-level-domain and
authoritative name servers. Answers are cached according to their TTL, including some negative
answers.

Common records include `A` for IPv4, `AAAA` for IPv6, `CNAME` for an alias, `MX` for mail exchange,
`NS` for authoritative servers, `TXT` for text-based policies or verification, and `PTR` for reverse
lookup. DNS can return many record types and does more than translate a hostname to one address.

DNSSEC signs DNS data so a validating resolver can detect forged answers; it does not encrypt DNS
queries. DNS-over-HTTPS and DNS-over-TLS address transport privacy to a resolver but do not replace
DNSSEC authenticity.

## What is a network topology, and what trade-offs do common topologies make?

**Answer**

A network topology describes how nodes and links are arranged physically or logically.

- **Star:** each endpoint connects to a central switch or access point. One endpoint link can fail
  without disconnecting the others, but the central device is a shared dependency.
- **Bus:** endpoints share one communication medium. It uses little cabling but creates contention
  and a shared failure domain.
- **Ring:** each node connects to two neighbors in a closed path. A basic single ring is sensitive to
  a link or node failure; redundant rings and protection mechanisms can provide alternate paths.
- **Mesh:** nodes have multiple paths between them. It improves resilience and route choice at the
  cost of links, configuration, and control-plane complexity.
- **Tree or hierarchical star:** access networks connect through aggregation layers. It scales
  operationally but makes the upper layers important capacity and failure domains.

Real networks commonly combine these patterns. Evaluate redundancy, convergence, cost, cabling,
capacity, blast radius, and operational complexity instead of memorizing one topology as “best.”

## How do the OSI and Internet protocol models help explain networking?

**Answer**

The seven-layer OSI model is a conceptual vocabulary:

1. physical transmission;
2. data-link framing and local delivery;
3. network-layer addressing and routing;
4. end-to-end transport;
5. session management;
6. representation, encoding, and encryption; and
7. application protocols.

The Internet protocol suite is usually described more practically as link, internet, transport,
and application layers. Its boundaries do not map perfectly to OSI. For example, TLS is commonly
used between an application protocol and transport, while many applications manage their own
session and representation concerns.

The models are troubleshooting tools, not a claim that every implementation has seven independent
software components.

## What is encapsulation in a TCP/IP network?

**Answer**

As application data moves down a protocol stack, each layer adds the information it needs. A TCP
implementation adds a transport header to create a segment, IP adds an internet-layer header to
create a packet, and a link technology such as Ethernet places the packet in a frame.

At the receiver, each layer validates and removes or interprets its corresponding information before
passing the payload upward. Intermediate routers normally forward based on the network-layer packet;
they do not process the application payload as an endpoint would, though firewalls, proxies, and
other middleboxes may inspect additional layers.

## How do MAC addresses, IP addresses, and ports differ?

**Answer**

- A **MAC address** identifies an interface for delivery on a compatible local link. It is used in
  link-layer frames and normally changes at each routed hop.
- An **IP address** identifies an interface or logical endpoint at the internet layer and supports
  routing across networks. It may be assigned statically or dynamically and is not necessarily a
  permanent device identity.
- A **transport port** identifies a TCP or UDP endpoint within a host. The combination of protocol,
  source and destination addresses, and source and destination ports distinguishes a flow.

Neither an ISP nor a hardware manufacturer is the universal source of these values. Operating
systems, administrators, local address assignment, virtualization, privacy features, and cloud
platforms can all affect them.

## What does ARP do?

**Answer**

On an IPv4 local network, the Address Resolution Protocol maps an IPv4 address to the link-layer
address needed for local delivery. A host first decides whether the destination is on-link. For an
on-link destination it resolves that host; for an off-link destination it resolves the next-hop
router instead.

ARP requests are broadcast on the local link, while a reply normally identifies the requested
mapping. Hosts cache mappings for a limited period. ARP has no built-in authentication, so networks
may use controls such as segmentation and dynamic ARP inspection where spoofing is a concern. IPv6
uses Neighbor Discovery rather than ARP.

## What does DHCP provide?

**Answer**

DHCP lets a client obtain network configuration from a server. A typical IPv4 exchange is described
as Discover, Offer, Request, and Acknowledge. The lease can include an address, prefix or subnet
mask, default gateway, DNS resolvers, lease time, and other options.

DHCP uses UDP ports 67 and 68 for IPv4. Because a new client may not yet have an address or know its
server, the initial exchange can use broadcast and a relay can forward requests between subnets.
Address assignment does not itself prove that the client is trusted or authorized.

## What are CIDR notation and a subnet prefix?

**Answer**

Classless Inter-Domain Routing writes an address with a prefix length, such as `192.0.2.0/24` or
`2001:db8::/32`. The prefix length says how many leading bits identify the network prefix; the
remaining bits identify addresses within that prefix.

For IPv4, `/24` corresponds to the mask `255.255.255.0`. Modern allocation and routing use
prefixes rather than the historic Class A, B, and C boundaries. Subnet design must account for
route aggregation, required address count, reserved addresses, growth, broadcast domains for IPv4,
and security or failure boundaries.

## How do unicast, broadcast, multicast, and anycast differ?

**Answer**

- **Unicast:** one sender addresses one destination interface.
- **Broadcast:** one sender targets every receiver in an IPv4 broadcast domain. IPv6 does not use
  broadcast.
- **Multicast:** a sender targets a group whose interested receivers join; network support and scope
  determine how the traffic is delivered.
- **Anycast:** the same address is advertised from multiple locations, and routing delivers a packet
  to one selected instance, usually the instance with the preferred route rather than a guaranteed
  geographically nearest server.

These are delivery models, not reliability guarantees. The application and transport still define
ordering, retransmission, security, and session behavior.

## How does the TCP three-way handshake establish a connection?

**Answer**

The client sends a segment with `SYN` and an initial sequence number. The server replies with
`SYN-ACK`, acknowledging the client's sequence space and supplying its own initial sequence number.
The client acknowledges the server's sequence number, after which both sides have synchronized
sequence spaces and the connection is established.

The handshake establishes TCP state; it does not authenticate the application server or encrypt
traffic. HTTPS performs a TLS handshake over the transport connection, although newer protocols such
as QUIC combine transport and cryptographic setup differently over UDP.

## Which protocol facts are commonly misstated in interviews?

**Answer**

- ARP and ICMP do not use TCP or UDP ports. Port numbers belong to transport protocols.
- Standard FTP control uses TCP port 21, not port 27; active-mode data traditionally uses TCP port
  20, while passive mode negotiates another port.
- A DHCPv4 server listens on UDP 67 and a client uses UDP 68; saying only “DHCP uses port 67” is
  incomplete.
- SMTP commonly uses TCP 25 for server-to-server relay, TCP 587 for message submission, and TCP 465
  for implicit TLS submission. It is not universally an always-listening service on only port 25.
- TCP reliability does not mean an application request ran exactly once. A response can be lost
  after the server committed work, so APIs still need idempotency and retry design.
- UDP is not automatically faster for every workload. Congestion control, handshake behavior,
  packet loss, application recovery, and protocols such as QUIC affect the result.

## References

- [HTTP semantics and status codes](https://www.rfc-editor.org/rfc/rfc9110.html)
- [WebSocket protocol](https://www.rfc-editor.org/rfc/rfc6455.html)
- [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700.html)
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
- [IPv4 Address Resolution Protocol (RFC 826)](https://www.rfc-editor.org/rfc/rfc826.html)
- [Dynamic Host Configuration Protocol (RFC 2131)](https://www.rfc-editor.org/rfc/rfc2131.html)
- [Classless Inter-Domain Routing (RFC 4632)](https://www.rfc-editor.org/rfc/rfc4632.html)
- [IPv6 Addressing Architecture (RFC 4291)](https://www.rfc-editor.org/rfc/rfc4291.html)
- [Transmission Control Protocol (RFC 9293)](https://www.rfc-editor.org/rfc/rfc9293.html)
