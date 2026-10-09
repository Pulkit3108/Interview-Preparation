# JavaScript

JavaScript language fundamentals, asynchronous programming, browser behavior, and coding exercises.

[Back to the question-bank index](../README.md)

## Topic Map

- [Language fundamentals, functions, and scope](#what-is-hoisting-are-let-variables-hoisted-and-what-is-the-temporal-dead-zone)
- [Objects, prototypes, classes, and modules](#what-are-object-prototypes)
- [Arrays, iteration, and collections](#explain-map-filter-and-reduce-methods-with-an-example)
- [Asynchronous JavaScript and promises](#difference-between-callback-promises-and-async-await)
- [Browser storage, rendering, networking, and performance](#what-different-types-of-storage-in-browsers-are-there)
- [Implementation exercises](#write-an-implementation-of-the-bind-function)
- [Output and behavior exercises](#is-i-visible-outside-the-settimeout-callback)

## What is hoisting, are `let` variables hoisted, and what is the temporal dead zone?

**Answer**

"Hoisting" describes how bindings are created during scope setup; source code is not physically
moved. Function declarations are initialized early, so they can usually be called before their
declaration. A `var` binding is initialized to `undefined` before execution reaches its declaration.

`let`, `const`, and `class` bindings also exist from the start of their block, but remain
uninitialized until evaluation reaches the declaration. Access during that interval, the temporal
dead zone, throws a `ReferenceError`.

## Difference between `var`, `let`, and `const` keywords

**Answer**

- `var` is function- or global-scoped, is initialized to `undefined`, permits redeclaration, and can
  be reassigned.
- `let` is block-scoped, has a temporal dead zone, cannot be redeclared in the same scope, and can be
  reassigned.
- `const` has the same scope and temporal-dead-zone behavior as `let`, but its binding cannot be
  reassigned. It does not make a referenced object or array immutable.

## What is Shadowing?

**Answer**

Shadowing occurs when an inner scope declares a binding with the same name as one in an outer scope.
Name lookup resolves to the nearest binding, so the outer one is inaccessible by that name within the
inner scope. Some combinations, such as declaring `var` where it conflicts with an enclosing block's
`let`, are syntax errors rather than valid shadowing.

## Difference between Normal and Arrow Functions

**Answer**

Function declarations are initialized during scope setup; function expressions and arrow functions
follow the initialization rules of the variable that stores them. Regular functions have dynamic
`this` and their own `arguments`, can be constructors when constructible, and can be generators.
Arrow functions capture `this`, `arguments`, and `super` lexically, cannot be called with `new`, and
cannot be generators. Choose based on invocation semantics, not just shorter syntax.

## What are first-class, higher-order, callback, IIFE, function-expression, anonymous, and declared functions?

**Answer**

- **First-class function:** a function can be stored in a variable, passed as an argument, or returned
  like another value.
- **Higher-order function:** accepts a function, returns a function, or both.
- **Callback:** a function supplied for another operation to invoke; callbacks are not necessarily
  asynchronous.
- **IIFE:** a function expression invoked immediately after it is created.
- **Function expression:** a function created as part of an expression and optionally named.
- **Anonymous function:** a function written without an explicit name.
- **Function declaration:** a `function name(...) {}` declaration whose binding is initialized
  during declaration instantiation, allowing it to be called earlier in that scope.

## What is the Lexical Environment and Execution Context?

**Answer**

A lexical environment is the specification model for bindings in one scope plus a reference to the
outer environment. A closure retains access to the environment where it was created.

An execution context represents the state needed to evaluate global, module, function, or `eval`
code, including its lexical/variable environments, current function, and `this` binding where
applicable. Calling a function pushes a new execution context; reducing it to "memory and code" is a
teaching shorthand, not the language model.

## Explain JavaScript Execution and Microtask Queue.

**Answer**

Before evaluating a scope, the engine creates its bindings and initializes them according to the
declaration type. It then executes statements synchronously on the call stack.

When a task finishes and the stack is empty, the host performs a microtask checkpoint. Promise
reaction jobs and `queueMicrotask` callbacks run from the microtask queue; browsers also deliver
`MutationObserver` callbacks as microtasks. The queue drains before the browser proceeds to another
task, so recursively scheduling microtasks can delay rendering and timers.

## What is the Event Loop?

**Answer**

The event loop is the host's scheduling model. It selects a runnable task, executes its JavaScript to
completion, drains microtasks, and may then render before selecting another task. Timers, user input,
network events, and message channels enqueue work through host-defined task sources. JavaScript on
one agent is run-to-completion, but a long task still blocks input and rendering.

## What is Callback?

**Answer**

A callback is a function supplied to another operation for later invocation by that operation. It may
run synchronously, as with `Array.prototype.map`, or asynchronously, as with a timer. It does not
necessarily run after the receiving function has returned.

## Explain Promises & Closure in JavaScript.

**Answer**

A promise represents the eventual fulfillment or rejection of an operation and allows reactions to
be composed with `then`, `catch`, and `finally`. A closure is a function together with access to the
lexical environment where it was created. They are separate concepts, though callbacks attached to a
promise may themselves be closures.

## What are Disadvantages of closure?

**Answer**

Closures are a core language feature, not inherently a disadvantage. Problems arise when a
long-lived closure unintentionally retains a large object graph, when mutable captured state creates
hidden coupling, or when many callbacks share a binding in an unexpected way. Limit captured state,
release long-lived listeners, and prefer explicit state ownership when it improves clarity.

## Difference between Callback, Promises, and Async Await

**Answer**

Callbacks are the general mechanism for passing behavior, but nested error-first asynchronous
callbacks can be difficult to compose. Promises provide one eventual result and centralized chaining.
An `async` function always returns a promise, and `await` makes its fulfillment or rejection readable
with normal control flow. Top-level `await` is also available in modules in supporting environments.

Promise combinators differ in failure behavior:

- `Promise.all` preserves input order and rejects on the first observed rejection.
- `Promise.allSettled` waits for every input and returns fulfillment/rejection records.
- `Promise.race` settles with the first input to settle.
- `Promise.any` fulfills with the first fulfillment and rejects with `AggregateError` only when all
  inputs reject.

None of these combinators automatically cancels work that is still running.

## How will you make multiple API calls simultaneously in JavaScript?

**Answer**

Start independent requests before awaiting them, then choose a combinator based on failure semantics:

```javascript
const [user, orders] = await Promise.all([
  fetchUser(userId),
  fetchOrders(userId),
]);
```

Use `allSettled` for partial results, add `AbortSignal` support when cancellation matters, and limit
concurrency instead of launching an unbounded number of requests.

## What is a static keyword in JavaScript?

**Answer**

The `static` keyword defines a public or private field, method, accessor, or initialization block on a
class constructor rather than on its instances. In a static method called as `ClassName.method()`,
`this` is the class; subclasses can inherit static methods. Common uses include factories,
class-level registries, and utilities closely associated with the class.

## What is `use strict` in Javascript?

**Answer**

`"use strict"` at the start of a script or function body enables strict mode. It turns some silent
errors into exceptions, forbids accidental global assignment and duplicate simple parameters, makes
plain-function `this` be `undefined`, and changes some legacy syntax and `eval` behavior. ECMAScript
modules and class bodies are strict automatically.

## Explain the behavior of the 'this' keyword

**Answer**

`this` is determined by how a function is invoked, not simply by where it is written. A method call
such as `object.method()` normally binds `this` to `object`; `call`, `apply`, or `bind` can provide it
explicitly; constructor calls bind it to the new instance. Arrow functions do not create their own
`this` and instead capture it lexically from the surrounding scope. In strict-mode plain function
calls, `this` is `undefined`.

## What is a Template Literal?

**Answer**

A template literal uses backticks and supports multiline text and `${expression}` interpolation.
Interpolation converts values to strings; it does not automatically escape HTML, SQL, shell, or URL
contexts.

## What is Tagged Template Literal?

**Answer**

A tagged template calls a tag function with an immutable array of literal segments followed by the
interpolated values. The tag can return any value, not only a string. Tags are useful for
context-aware escaping or domain-specific construction, but safety depends on the tag's
implementation.

## Difference between `==` and `===` operators

**Answer**

`===` compares without coercing operand types, with special cases such as `NaN !== NaN` and
`0 === -0`. `==` follows the abstract equality coercion rules, which can be surprising. Prefer
strict equality unless a deliberate coercive comparison is clearer, such as `value == null` to test
for either `null` or `undefined`.

## How does || and && operator works in JS?

**Answer**

Both operators short-circuit and return an operand rather than a forced Boolean. `a || b` returns
`a` when it is truthy, otherwise `b`; `a && b` returns `a` when it is falsy, otherwise `b`. Use `??`
instead of `||` for defaults when valid values such as `0`, `false`, or an empty string must remain.

## Difference between `null`, `undefined`, and `not defined`

**Answer**

- `null` is an explicit primitive value commonly used to represent intentional absence.
- `undefined` is the default result for many missing values, including an uninitialized `let` or
  `var`, a missing object property, or a function with no return value.
- "Not defined" is not a JavaScript value. Resolving an undeclared identifier normally throws a
  `ReferenceError`; `typeof undeclaredName` is the notable safe check and returns `"undefined"`.

## What is isNaN?

**Answer**

The global `isNaN(value)` converts its argument to a number before checking, so values such as
`"hello"` return `true`. `Number.isNaN(value)` returns `true` only when the value is the numeric
`NaN` value and is usually the clearer test. `NaN` is the only JavaScript value not equal to itself;
`Infinity` and `-Infinity` are numbers, not `NaN`.

## Explain Implicit Type Coercion in JS

**Answer**

Implicit coercion converts values according to an operator's rules. For example, `"5" + 1` produces
`"51"`, while `"5" - 1` produces `4`; an object may be converted through `Symbol.toPrimitive`,
`valueOf`, or `toString`. Use explicit conversion at boundaries when coercion would obscure intent.

## What is eval()?

**Answer**

`eval` parses and executes a string as JavaScript. Direct `eval` can access the current lexical scope,
which complicates optimization and auditing; indirect `eval` executes in the global scope. It also
turns data into code and can create injection vulnerabilities. Prefer parsers, lookup tables,
`JSON.parse`, or explicit functions instead.

## What will be the value of 0.1 + 0.2 === 0.3 and why?

**Answer**

It is `false`. JavaScript `Number` uses IEEE 754 binary floating-point, and values such as `0.1` and
`0.2` cannot be represented exactly. Compare approximate values with a tolerance appropriate to the
scale and domain, not a universal magic constant. Represent money using integer minor units or a
decimal type/library rather than binary floating-point.

## What is Truthy and Falsy Value

**Answer**

In a Boolean context, JavaScript coerces values. The falsy values are `false`, `0`, `-0`, `0n`,
`NaN`, `""`, `null`, `undefined`, and the legacy browser value `document.all`. Every other value,
including empty arrays and empty objects, is truthy.

## What is the Spread and Rest Operator?

**Answer**

The same `...` syntax has context-dependent meanings. A rest parameter or rest property collects
remaining values, while spread expands an iterable into call arguments or array elements, or copies
an object's own enumerable properties.

```javascript
const { name, ...remainingProperties } = person;
const combined = [...first, ...second];
```

Array and object spread are shallow; they do not clone nested objects.

## Explain Map, Filter, and Reduce methods with an example

**Answer**

`map` produces one transformed element per input element, `filter` retains elements whose predicate
is truthy, and `reduce` accumulates the array into one result.

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(number => number * 2);
const even = numbers.filter(number => number % 2 === 0);
const sum = numbers.reduce((total, number) => total + number, 0);
```

These methods do not mutate the source array, though a callback can still mutate referenced objects.

## Which methods you can use on array to modify it’s original state?

**Answer**

Common mutating methods are `push`, `pop`, `shift`, `unshift`, `splice`, `sort`, `reverse`, `fill`,
and `copyWithin`. Assignment to an index or `length` also mutates an array. Current JavaScript offers
non-mutating counterparts for several operations: `toSorted`, `toReversed`, `toSpliced`, and `with`.

## What is the difference between splice and slice?

**Answer**

`splice(start, deleteCount, ...items)` mutates an array by removing and/or inserting elements and
returns the removed elements. `slice(start, end)` returns a shallow copy from `start` through, but
not including, `end` and does not mutate the source. `toSpliced` is the non-mutating counterpart to
`splice` in current JavaScript.

## What is the difference between JSON.parse() and JSON.stringify()

**Answer**

`JSON.parse(text, reviver?)` parses valid JSON and optionally transforms parsed values.
`JSON.stringify(value, replacer?, space?)` serializes supported JavaScript data to JSON. JSON cannot
represent cycles, `BigInt`, functions, symbols, or `undefined` as ordinary values; dates serialize as
strings through `toJSON`, and a reviver is needed to reconstruct richer types. Parsing data does not
make it trusted, so validate the resulting shape.

## What is a deep copy and shallow copy in JavaScript?

**Answer**

A shallow copy creates a new outer array or object while preserving references to nested objects.
Spread and `Object.assign` are common shallow-copy tools. A deep copy recursively duplicates the
supported object graph so nested mutable values are independent.

Use `structuredClone` for supported structured-clone values, including cycles, maps, sets, and many
platform objects. JSON serialization is not a general deep-clone technique because it loses types,
rejects cycles and `BigInt`, and omits or changes unsupported values. Domain objects may need an
explicit copy operation.

## What is the difference between `call`, `apply`, and `bind`?

**Answer**

`call` invokes a function immediately with an explicit `this` followed by individual arguments.
`apply` also invokes it immediately but accepts the arguments as an array-like object. `bind` returns
a new function with `this` and optional leading arguments fixed for later invocation. Arrow
functions ignore attempts to rebind `this` because they capture it lexically.

```javascript
function greet(greeting, punctuation) {
  return `${greeting}, ${this.name}${punctuation}`;
}

greet.call({ name: 'Ava' }, 'Hello', '!');
greet.apply({ name: 'Ava' }, ['Hello', '!']);
const greetAva = greet.bind({ name: 'Ava' }, 'Hello');
greetAva('!');
```

## What is Currying?

**Answer**

Currying transforms `f(a, b, c)` into `f(a)(b)(c)`, a chain of unary functions. Closures retain the
previous arguments. It differs from partial application, which fixes any subset of arguments and may
leave a function that still accepts more than one argument.

## What is Method Chaining?

**Answer**

Method chaining calls methods consecutively on each preceding return value. A mutable fluent API may
return `this`; immutable APIs often return a new value; promise chains return a new promise. A method
need not return the same object for chaining to work.

## What is a Partial application?

**Answer**

Partial application creates a function with some arguments fixed in advance. It can be implemented
with a closure or `bind`; unlike currying, the returned function may still accept several arguments.

## What are the phases of Event Propagation?

**Answer**

DOM event dispatch has a capture phase from the window/document side toward the target, a target
phase, and then, for events whose `bubbles` flag is true, a bubble phase back through ancestors.
Listeners registered with `{ capture: true }` participate on the capture path; ordinary listeners
normally run at the target and during bubbling. `stopPropagation` stops later nodes on the path, while
`stopImmediatePropagation` also stops remaining listeners on the current node.

## What is Event Propagation - Bubbling & Capturing?

**Answer**

Capturing travels from ancestors toward the target; bubbling travels from the target back through
ancestors. The event object is the same dispatch, while `event.target` remains the origin and
`event.currentTarget` identifies the listener currently running. Not every event bubbles, so check
the event's specification rather than assuming delegation will work.

## What is Event Delegation?

**Answer**

Event delegation attaches one listener to a stable ancestor and uses the bubbling event's target,
often with `closest`, to identify the relevant descendant. It reduces listeners and naturally handles
later-added children. Validate that the matched element belongs to the intended container and account
for events that do not bubble.

## What is a constructor function?

**Answer**

A constructible function can be called with `new`. JavaScript creates an object linked to the
function's `prototype`, calls the function with that object as `this`, and returns the object unless
the function explicitly returns another object. Arrow functions are not constructible. Class syntax
provides stricter, clearer constructor semantics over the same prototype model.

## What is Debouncing and Throttling?

**Answer**

Debouncing waits for a quiet interval before invoking a function, which suits search input or resize
recalculation. Throttling permits at most one invocation per interval, which suits continuous scroll
or pointer updates. Production helpers should define leading/trailing behavior, preserve `this` and
arguments, expose cancellation where useful, and not be confused with server-side rate limiting.

## What is the difference between setInterval() and setTimeout()?

**Answer**

`setTimeout` queues one callback after at least the requested delay. `setInterval` attempts to queue
callbacks repeatedly at the interval. Neither provides exact timing; busy tasks, throttling, and
clamping can delay execution. Recursive `setTimeout` is often safer for polling because it can wait
for one operation to finish before scheduling the next. Use `requestAnimationFrame` for visual
animation.

## What are Object Prototypes?

**Answer**

Every ordinary object has an internal `[[Prototype]]` that is either another object or `null`.
Property lookup checks own properties first and then follows this link. Arrays normally inherit from
`Array.prototype`, which in turn inherits from `Object.prototype`. Inspect the link with
`Object.getPrototypeOf`; avoid the legacy `__proto__` accessor.

## What is Prototypal Inheritance?

**Answer**

Prototypal inheritance is delegation through an object's prototype chain. Constructor functions and
class syntax create and organize these links, but classes do not replace the prototype model.
Methods placed on a prototype are shared rather than copied into each instance.

## What is the difference between `prototype` and `__proto__`?

**Answer**

For a constructible function `F`, `F.prototype` is the object used as the `[[Prototype]]` of objects
created by `new F()`. It is an ordinary property of the function and is not the function's own
prototype link. `__proto__` is a legacy accessor on `Object.prototype` for reading or changing an
object's internal prototype. Prefer `Object.getPrototypeOf`, `Object.create`, and, rarely,
`Object.setPrototypeOf`.

## What is a Prototype Chain?

**Answer**

A prototype chain is the sequence followed during inherited property lookup until a property is found
or a `null` prototype is reached. Not all objects inherit from `Object.prototype`; for example,
`Object.create(null)` deliberately creates a null-prototype object.

## Can we implement Polymorphism in JavaScript?

**Answer**

Yes. JavaScript commonly uses subtype polymorphism through overridden prototype/class methods and
duck typing, where any object with the required behavior can be used. The language has no runtime
interface construct; TypeScript interfaces are erased before execution.

## What OOPs concept we can follow in JavaScript?

**Answer**

JavaScript supports encapsulation with closures, modules, and private class fields; abstraction with
functions and public APIs; inheritance through prototype chains; and polymorphism through overriding
or duck typing. Favor composition when it expresses behavior more directly than a deep inheritance
hierarchy.

## What are some of the ES6 features of JavaScript?

**Answer**

Arrow Functions: Shorter syntax for functions with lexical this.
let and const: Block-scoped variable declarations.
Template Literals: String literals with embedded expressions.
Default Parameters: Default values for function parameters.
Destructuring Assignment: Unpack values from arrays or objects.
Spread and Rest Operators: Spread elements and collect multiple elements.
Classes: Concise syntax for constructor functions and inheritance.
Modules: Export and import functions, objects, or primitives.
Promises: Handle asynchronous operations gracefully.
Enhanced Object Literals: Shorthand syntax for object properties and methods.
Iterators and Generators: Custom iteration behavior for objects.

## Which sorting algorithm is used in JavaScript?

**Answer**

ECMAScript specifies observable behavior, not one sorting algorithm. Since ES2019,
`Array.prototype.sort` must be stable, but engines may choose or change their implementation. Without
a comparator, elements are compared as strings by UTF-16 code-unit order; numeric sorting therefore
needs a comparator such as `(a, b) => a - b`. `sort` mutates the array; `toSorted` returns a sorted
copy.

## What is yield in JavaScript?

**Answer**

`yield` pauses a generator and produces a value to its iterator consumer. Calling `next(value)`
resumes execution and makes `value` the result of the suspended `yield` expression. `yield*` delegates
to another iterable. It is valid in generator functions, not ordinary functions.

## What is a symbol in JavaScript?

**Answer**

A symbol is a unique primitive commonly used as an object property key. `Symbol()` creates a new
symbol; `Symbol.for` uses a global registry. Well-known symbols such as `Symbol.iterator` customize
language protocols. Symbols reduce accidental name collisions but are not private or secret.

## What is a proxy in JavaScript?

**Answer**

A `Proxy` wraps a target and traps operations such as property access, assignment, enumeration,
function calls, or construction. Proxy handlers must obey language invariants, and behavior can be
harder to optimize and debug. `Reflect` methods are useful for forwarding default behavior. A
revocable proxy can be disabled later.

## What is a weakSet and weakMap?

**Answer**

`WeakMap` holds key/value associations without keeping eligible keys alive; `WeakSet` similarly tracks
eligible values weakly. Current JavaScript permits objects and non-registered symbols as weak keys.
Because garbage collection is nondeterministic, weak collections are not enumerable and expose no
size. They suit object-associated metadata, memoization, or membership without controlling lifetime.

## What is a Mutation Observer?

**Answer**

`MutationObserver` asynchronously reports configured DOM changes such as child-list, attribute, or
text mutations. Observe the narrowest subtree and mutation types needed, process batches efficiently,
and call `disconnect` when finished. Its callbacks run as microtasks and replace legacy synchronous
mutation events.

## What is DOM and BOM?

**Answer**

The DOM is the standardized object model for documents and nodes. "BOM" is an informal term for
browser APIs outside the document model, such as `window`, `location`, `history`, `navigator`, and
`screen`. These APIs come from multiple web standards rather than one BOM specification.

## What is a Critical Rendering Path?

**Answer**

The critical rendering path covers the work needed for initial pixels: parse HTML into the DOM, parse
CSS into the CSSOM, execute render-blocking scripts, construct the render tree, perform layout, then
paint and composite. Reduce blocking resources and main-thread work, prioritize critical assets, and
measure user-centric metrics rather than assuming fewer files alone is faster.

## What is the difference between a Website and a Web Application?

**Answer**

The terms overlap rather than form a strict technical boundary. "Website" often emphasizes
information and navigation, while "web application" emphasizes task-oriented interaction and state.
The distinction does not determine architecture: either may use static generation, server rendering,
client rendering, APIs, authentication, or offline capabilities.

## What different types of storage in browsers are there?

**Answer**

- `localStorage`: synchronous string key/value storage scoped by origin and retained until cleared.
- `sessionStorage`: synchronous string key/value storage scoped by origin and browser tab/session.
- Cookies: small values associated with HTTP requests according to domain, path, SameSite, expiry,
  and security attributes.
- IndexedDB: asynchronous transactional storage for larger structured data, indexes, and blobs.
- Cache Storage: request/response storage commonly used by service workers.

Quotas, eviction, and partitioning vary by browser. Web SQL is obsolete. Do not store secrets merely
because an API is client-side; XSS can read any storage accessible to JavaScript.

## How do cookies work?

**Answer**

A server sets a cookie with `Set-Cookie`; browser JavaScript can set non-`HttpOnly` cookies through
`document.cookie`. The browser stores its name/value and attributes and later attaches applicable
cookies in a `Cookie` request header. Matching depends on host/domain, path, expiry, `Secure`,
`SameSite`, partitioning, and browser policy.

Session cookies should normally use `Secure`, `HttpOnly`, and an appropriate `SameSite` value, with a
narrow host and path. Cookies are credentials when used for sessions, so state-changing requests also
need a CSRF strategy.

## How are cookies passed in an HTTPS request?

**Answer**

The server can set a cookie in an HTTPS response:

```http
HTTP/1.1 200 OK
Set-Cookie: __Host-session=opaque-value; Path=/; Secure; HttpOnly; SameSite=Lax
```

For a later matching request, the browser adds:

```http
GET /dashboard HTTP/1.1
Host: example.com
Cookie: __Host-session=opaque-value
```

TLS protects the request in transit. `Secure` prevents normal transmission over plain HTTP;
`HttpOnly` prevents JavaScript from reading the value but does not stop an injected script from
making authenticated requests. Certificate validation and XSS/CSRF defenses remain necessary.

## How is the expiration time of cookies set and managed?

**Answer**

`Max-Age` sets lifetime in seconds; `Expires` sets an HTTP-date. When both are present, `Max-Age`
takes precedence. With neither attribute, the cookie is a session cookie, although session restoration
can preserve it across a browser restart. Servers should enforce session expiry independently rather
than trusting client deletion.

```http
Set-Cookie: sessionId=abc123; Max-Age=3600; Path=/; Secure; HttpOnly; SameSite=Lax
```

Set `Max-Age=0` or an expiry in the past with the same name, domain, and path to delete a cookie.

## What is Browser Caching and what are its benefits?

**Answer**

HTTP caches reuse responses to reduce latency, bandwidth, and origin load. `Cache-Control` defines
freshness and reuse policy; validators such as `ETag` and `Last-Modified` enable conditional requests.
Use immutable, content-hashed URLs for long-lived static assets and conservative/private policies for
personalized responses. Browser HTTP caching is distinct from application-managed Cache Storage.

## What is Server-Side Rendering (SSR) and how to optimize it.

**Answer**

SSR renders route HTML on the server before sending it to the browser, which can improve initial
content delivery and crawler access. The client may then hydrate the markup for interactivity.
Optimize server latency, streaming, caching, data-fetch deduplication, payload size, critical assets,
and hydration cost. SSR adds server capacity, cache-isolation, and browser/server consistency
concerns, so verify its benefit with field metrics.

## What is SEO?

**Answer**

Search engine optimization improves a page's discoverability and usefulness in organic search. It
includes crawlable links, correct status codes and canonicals, useful titles and content, semantic
HTML, structured data where applicable, mobile usability, performance, and trustworthy external
signals. SSR alone does not guarantee ranking, and SEO should not compromise accessibility or users.

## What is the Largest Contentful Paint (LCP)?

**Answer**

Largest Contentful Paint is a Core Web Vital measuring when the largest eligible image, text block,
or video poster in the viewport finishes rendering. A good field target is at most 2.5 seconds at the
75th percentile, segmented by mobile and desktop. Improve it by reducing time to first byte, making
the LCP resource discoverable and high priority, avoiding unnecessary render blocking, and optimizing
the resource's size and delivery.

## What is webpack and polyfills?

**Answer**

Webpack builds a dependency graph from application modules and produces configured bundles and
assets through loaders and plugins. Code splitting, tree shaking, and caching depend on configuration
and module behavior. A polyfill implements a missing runtime API in an older environment. Syntax
transformation and API polyfilling are different tasks, and target-browser policy should determine
both.

## What is Babel?

**Answer**

Babel parses JavaScript and applies configured syntax transformations through plugins and presets.
`@babel/preset-env` selects transformations from declared runtime targets. Babel does not make every
new runtime API available by syntax transformation alone; polyfills such as `core-js` require a
separate, target-aware strategy.

## What is an HTTP redirect? What other methods are available for redirecting users to a different page?

**Answer**

An HTTP redirect is a 3xx response with a `Location` header. `301` and `308` are permanent; `302` and
`307` are temporary. `307` and `308` preserve the request method and body, while historical user-agent
behavior can change a POST to GET for `301`/`302`. `303` explicitly directs the client to retrieve the
new location with GET, which is useful after a form submission.

Server redirects are generally preferable because they work without JavaScript and communicate clear
HTTP semantics. `location.assign`/`replace` and meta refresh can navigate client-side when necessary.
An ordinary anchor is navigation, not a redirect. Validate redirect targets to prevent open-redirect
vulnerabilities.

## How might a web app determine whether an end user is accessing the site via a mobile phone or a desktop browser?

**Answer**

Prefer responsive layout and capability queries such as CSS media/container queries, pointer/hover
media features, and feature detection. Device categories are ambiguous, user-agent strings can be
reduced or spoofed, and tablets or desktop touchscreens blur the boundary. Use user-agent client hints
only when a server genuinely needs an approximate device signal and send correct variation headers.

## What Happens When You Type a URL into Your Browser?

**Answer**

The browser parses and normalizes the URL, applies security and cache policy, and resolves the host
through available DNS caches/resolvers. It establishes a suitable transport: commonly TCP plus TLS
for HTTP/1.1 or HTTP/2, or QUIC with TLS for HTTP/3. During TLS it validates the server identity and
negotiates keys and an application protocol.

The browser sends an HTTP request, potentially through a proxy or CDN. The origin or intermediary
returns a status, headers, and optional body. For HTML, the browser incrementally parses the DOM,
discovers subresources, builds style/layout information, executes scripts according to their loading
semantics, and paints/composites pixels. Redirects, service workers, caching, connection reuse, CSP,
and prioritization can alter this path.

## Can you explain DNS caching and its layers?

**Answer**

DNS answers may be cached by the browser, operating system/stub resolver, local network, recursive
resolver, and intermediate authoritative infrastructure according to TTL and negative-caching rules.
Application and network caches are implementation-dependent, and encrypted DNS may change which
resolver is used. Caching reduces latency and upstream load but delays propagation until cached
records expire.

## What is the TLS handshake and why is it important for HTTPS connections?

**Answer**

During a TLS handshake, peers negotiate a protocol version and algorithms, perform a key exchange,
and derive symmetric session keys. The server presents a certificate chain for the requested host;
the client validates identity, trust, validity, and policy. TLS then protects confidentiality and
integrity in transit. Session resumption can reduce later handshakes, and client certificates are
optional rather than part of ordinary public HTTPS.

## How do CDNs improve web performance?

**Answer**

A CDN serves cacheable content from edge locations nearer to users, reducing network latency and
origin traffic. It can also reuse connections, negotiate modern protocols, compress/transform assets,
and absorb traffic spikes. Performance depends on cache keys, TTLs, invalidation, origin shielding,
and hit ratio; dynamic or personalized content needs deliberate caching and privacy rules.

## What causes SSL errors in browsers and how do you fix them?

**Answer**

Common causes include an expired or not-yet-valid certificate, hostname mismatch, untrusted issuer,
missing intermediate certificate, revoked certificate, unsupported TLS policy, incorrect client clock,
or an intercepting proxy. Mixed content is a separate page-security error after the main TLS
connection succeeds.

Inspect the browser error and certificate chain for the exact host, confirm DNS and virtual-host/SNI
routing, install the full chain from a trusted issuer, renew or replace the certificate, and verify
the system clock and TLS configuration. Do not teach users to bypass a production warning. An HTTPS
redirect cannot repair a certificate failure because TLS validation happens before HTTP.

## What is asynchronous resource loading and how does it benefit web performance?

**Answer**

Classic scripts without attributes block parsing. A classic `defer` script downloads in parallel and
executes after parsing, in document order, before `DOMContentLoaded`. A classic `async` script
downloads in parallel and executes as soon as it is ready, without order guarantees. Module scripts
are deferred by default; `async` changes their scheduling. Use these semantics according to
dependency order and measure whether execution still creates long main-thread tasks.

## Can you explain the significance of different HTTP response codes?

**Answer**

Status classes communicate the outcome: `1xx` informational, `2xx` successful, `3xx` redirection or
cache control, `4xx` a condition associated with the request, and `5xx` server failure.

Common examples are `200 OK`, `201 Created` (usually with `Location`), `202 Accepted` for unfinished
asynchronous processing, and `204 No Content`; `301`/`308` permanent redirects, `302`/`307`
temporary redirects, and `304 Not Modified`; `400 Bad Request`, `401 Unauthorized` (authentication
is required or failed), `403 Forbidden`, `404 Not Found`, `409 Conflict`, `422 Unprocessable
Content`, and `429 Too Many Requests`; and `500 Internal Server Error`, `502 Bad Gateway`, `503
Service Unavailable`, and `504 Gateway Timeout`. Clients must interpret the status together with the
method, headers, and application contract.

## What are the ways to reduce the load time of a webpage?

**Answer**

Measure field and lab performance first, then separate network, server, and main-thread bottlenecks.
Typical improvements include lower origin latency, CDN and HTTP caching, Brotli/Gzip, responsive
modern images, font subsetting, code splitting, tree shaking, reduced third-party JavaScript, and
lazy loading below-the-fold content. Prioritize the LCP resource and critical CSS/JavaScript without
inlining so much that caching suffers. HTTP/2 and HTTP/3 reduce the value of blindly combining every
file, so optimize dependency and execution cost rather than request count alone.

## How can you optimize images on an e-commerce website that loads a lot of products?

**Answer**

Generate appropriately sized variants at ingestion, compress them, and negotiate formats such as
AVIF/WebP with a safe fallback. Use `srcset` and `sizes` or `<picture>` so the browser chooses the
right dimensions. Include intrinsic `width` and `height` to reserve space, lazy-load offscreen images,
but load and prioritize the likely LCP image eagerly. Serve content-hashed assets through a CDN with
long cache lifetimes, validate uploads, and retain a suitable source asset for future transformations.
Measure visual quality, bytes, LCP, and layout shift on realistic product grids.

## Write an implementation of the bind function.

**Answer**

```javascript
Function.prototype.myBind = function myBind(thisArg, ...boundArgs) {
  const target = this;

  function boundFunction(...callArgs) {
    const receiver = new.target ? this : thisArg;
    return Reflect.apply(target, receiver, [...boundArgs, ...callArgs]);
  }

  if (target.prototype) {
    boundFunction.prototype = Object.create(target.prototype);
  }

  return boundFunction;
};
```

This demonstrates argument binding, return-value preservation, and constructor calls. A complete
native-equivalent polyfill must also reproduce details such as `length`, `name`, and exotic function
behavior, so production code should use the built-in `bind`.

## Write an implementation to Reverse an array.

**Answer**

```javascript
function reverseArray(array) {
  const reversed = [];
  for (let index = array.length - 1; index >= 0; index--) {
    reversed.push(array[index]);
  }
  return reversed;
}
```

## Write an implementation of debounce function.

**Answer**

```javascript
function debounce(fn, delay) {
  let timerId;
  return function debounced(...args) {
    const receiver = this;
    clearTimeout(timerId);
    timerId = setTimeout(() => {
      fn.apply(receiver, args);
    }, delay);
  };
}
```

## Write an implementation of throttle function.

**Answer**

```javascript
function throttle(fn, interval) {
  let lastRun = -Infinity;
  return function throttled(...args) {
    const now = performance.now();
    if (now - lastRun >= interval) {
      lastRun = now;
      return fn.apply(this, args);
    }
    return undefined;
  }
}
```

This is a leading-only throttle. State explicitly if trailing execution or cancellation is required.

## Write an implementation to Flatten an array.

**Answer**

```javascript
function flattenArray(array) {
  const flattened = [];
  for (const value of array) {
    if (Array.isArray(value)) {
      flattened.push(...flattenArray(value));
    } else {
      flattened.push(value);
    }
  }
  return flattened;
}
```

## Write the implementation of a map function.

**Answer**

```javascript
Array.prototype.myMap = function myMap(callback, thisArg) {
  if (this == null) throw new TypeError('myMap called on null or undefined');
  if (typeof callback !== 'function') throw new TypeError('callback must be a function');

  const source = Object(this);
  const length = source.length >>> 0;
  const result = new Array(length);
  for (let index = 0; index < length; index++) {
    if (index in source) {
      result[index] = callback.call(thisArg, source[index], index, source);
    }
  }
  return result;
};
```

This handles sparse arrays and a callback receiver, but extending native prototypes is generally
avoided in application code because names can collide.

## Write an implementation to flatten an object.

**Answer**

```javascript
function flattenObject(object, prefix = '', result = {}) {
  for (const [key, value] of Object.entries(object)) {
    const path = prefix ? `${prefix}.${key}` : key;
    if (value !== null && typeof value === 'object' && !Array.isArray(value)) {
      flattenObject(value, path, result);
    } else {
      result[path] = value;
    }
  }
  return result;
}
```

This contract treats arrays as leaf values. Production code must define escaping for keys containing
dots and behavior for cycles, dates, maps, and other non-plain objects.

## Write a function for sum(1)(2)(3)....(n)() which return sum of n numbers

**Answer**

```javascript
const sum = (total = 0) => (value) =>
  value === undefined ? total : sum(total + value);

sum(1)(2)(3)(); // 6
```

## Write a program to count occurrence of character in a string

**Answer**

```javascript
function countCharacterOccurrences(str) {
  const charCount = {};
  for (let char of str) {
      if (charCount[char]) {
          charCount[char]++;
      } else {
          charCount[char] = 1;
      }
  }
  return charCount;
}
```

## How can a two-dimensional array of key/value entries be transformed into objects?

**Answer**

```javascript
function entriesToObjects(groups) {
  return groups.map(group => Object.fromEntries(
    group.map(({ key, value }) => [key, value]),
  ));
}
```

For example, `[[{ key: 'id', value: 1 }, { key: 'name', value: 'A' }]]` becomes
`[{ id: 1, name: 'A' }]`. If each pair is already `[key, value]`, use
`groups.map(Object.fromEntries)`.

## Write a code for calculator where you perform chaining?

**Answer**

```javascript
class Calculator {
  constructor() {
      this.value = 0;
  }
  add(number) {
      this.value += number;
      return this;
  }
  subtract(number) {
      this.value -= number;
      return this;
  }
  multiply(number) {
      this.value *= number;
      return this;
  }
  divide(number) {
    if (number === 0) {
      throw new RangeError('Division by zero is not allowed');
    }
    this.value /= number;
    return this;
  }
  getResult() {
      return this.value;
  }
}
```

## How would you run promise-returning tasks together with retries?

**Answer**

```javascript
async function retry(task, maxRetries) {
  let retries = 0;
  while (true) {
    try {
      return await task();
    } catch (error) {
      if (retries >= maxRetries) throw error;
      retries++;
    }
  }
}

function allWithRetry(taskFunctions, maxRetries) {
  return Promise.all(taskFunctions.map(task => retry(task, maxRetries)));
}
```

Retries require functions that create a fresh attempt, not already-started promises. In production,
retry only transient, idempotent operations and add bounded exponential backoff, jitter, cancellation,
and observability. This composes the native `Promise.all`; it is not a `Promise.all` polyfill.

## Implement Browser history feature

**Answer**

```javascript
class BrowserHistory {
  constructor() {
    this.history = [];
    this.currentIndex = -1;
  }
  visit(url) {
    this.history = this.history.slice(0, this.currentIndex + 1);
    this.history.push(url);
    this.currentIndex++;
  }
  back(steps) {
    const newIndex = Math.max(this.currentIndex - steps, 0);
    this.currentIndex = newIndex;
    return this.history[this.currentIndex];
  }
  forward(steps) {
    const newIndex = Math.min(this.currentIndex + steps, this.history.length - 1);
    this.currentIndex = newIndex;
    return this.history[this.currentIndex];
  }
  current() {
    return this.history[this.currentIndex];
  }
}
```

## Explain How to create Custom events in JavaScript and how to dispatch it?

**Answer**

```javascript
const myEvent = new CustomEvent('myCustomEvent', {
  detail: { message: 'Hello, World!' },
  bubbles: true,
});
const targetElement = document.getElementById('myElement');
targetElement.addEventListener('myCustomEvent', (event) => {
  console.log('Custom event received:', event.detail.message);
});
targetElement.dispatchEvent(myEvent);
```

Register listeners before dispatch. `dispatchEvent` is synchronous; `bubbles`, `cancelable`, and
`composed` must be enabled explicitly when the event contract requires them.

## Implement auto-retry promises

**Answer**

```javascript
async function autoRetry(task, maxRetries = 3, delayMs = 0) {
  for (let attempt = 0; ; attempt++) {
    try {
      return await task();
    } catch (error) {
      if (attempt >= maxRetries) throw error;
      if (delayMs > 0) {
        await new Promise(resolve => setTimeout(resolve, delayMs));
      }
    }
  }
}
function simulateAPICall() {
  return new Promise((resolve, reject) => {
    const isSuccessful = Math.random() > 0.5;
    setTimeout(() => (isSuccessful ? resolve("Success!") : reject("Failed!")), 500);
  });
}
// Using autoRetry with 5 retries and a 1-second delay between attempts.
autoRetry(simulateAPICall, 5, 1000)
  .then(result => console.log("Result:", result))
  .catch(error => console.error("Error:", error));
```

## How can promise-returning tasks be processed in bounded batches?

**Answer**

```javascript
async function throttlePromises(taskFunctions, batchSize) {
  const results = [];
  for (let startIndex = 0; startIndex < taskFunctions.length; startIndex += batchSize) {
    const currentBatch = taskFunctions.slice(startIndex, startIndex + batchSize).map(task => task());
    results.push(...await Promise.all(currentBatch));
  }
  return results;
}
// Example: Create an array of promise-returning functions
const taskFunctions = Array.from({ length: 10 }, (_, index) => () =>
  new Promise(resolve => setTimeout(() => resolve(`Task ${index + 1} completed`), 1000))
);
// Process the tasks in batches of 3 concurrently
throttlePromises(taskFunctions, 3)
  .then(results => console.log(results))
  .catch(error => console.error(error));
```

Batching limits active work to the batch size but waits for the slowest task in each batch before
starting more. A worker-pool approach provides a strict concurrency limit with better utilization.

## How would you implement array difference using SameValueZero equality?

**Answer**

`includes` uses SameValueZero, so it treats `NaN` as equal to `NaN` and treats `0` and `-0` as equal:

```javascript
function difference(array, values) {
  return array.filter(value => !values.includes(value));
}
```

## Is `i` visible outside the `setTimeout` callback?

**Answer**

```javascript
setTimeout(function callback() {
  for (var i = 0; i < 10; i++) {
    // `i` is scoped to callback because `var` is function-scoped.
  }
});

console.log(i);
```

The final line throws `ReferenceError: i is not defined`. The `var` binding belongs to the callback's
function scope, not to the surrounding scope. Its asynchronous timing does not change that boundary.

## What does the IIFE print when `var a` is hoisted?

**Answer**

```javascript
(function() {
  console.log(a);
  var a = 10;
  console.log(a);
})();
```

It prints `undefined` and then `10`: the `var` binding exists from function setup and is initialized
to `undefined`, while the assignment runs at its original position.

## What values do `x` and `y` have after post-increment?

**Answer**

```javascript
let x = 10;
let y = x++;
console.log(x, y);
```

The post-increment expression returns the old value (`10`) and then increments `x`, so the output is
`11 10`.

## How do loose and strict equality compare `null` and `undefined`?

**Answer**

```javascript
console.log(null == undefined);  // true
console.log(null === undefined); // false
```

Loose equality has a special rule that treats `null` and `undefined` as equal to each other. Strict
equality does not coerce or apply that special equivalence, so different types are unequal.

## What does a `Set` contain after duplicate values are supplied?

**Answer**

```javascript
const set = new Set([1, 2, 3, 3]);
console.log(set); // Set(3) { 1, 2, 3 }
```

## Write a code to find the first non repeat character in a string

**Answer**

```javascript
function firstNonRepeatingCharacter(str) {
  const charCount = new Map();
  for (let char of str) {
    if (charCount.has(char)) {
      charCount.set(char, charCount.get(char) + 1);
    } else {
      charCount.set(char, 1);
    }
  }
  for (let char of str) {
    if (charCount.get(char) === 1) {
      return char;
    }
  }
  return null;
}
```

## How would you memoize calls with primitive, array, and plain-object arguments?

**Answer**

```javascript
// Helper to stringify values in a stable manner (handles objects, arrays, primitives, and null).
function stableStringify(value) {
  if (value === null || typeof value !== 'object') return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(stableStringify).join(',')}]`;
  const sortedEntries = Object.entries(value).sort(([keyA], [keyB]) => keyA.localeCompare(keyB));
  return `{${sortedEntries.map(([key, val]) => `${JSON.stringify(key)}:${stableStringify(val)}`).join(',')}}`;
}
// Memoization utility using stable stringify for consistent key generation.
function memoize(func) {
  const cache = new Map();
  return function (...args) {
    const cacheKey = args.map(stableStringify).join('|');
    if (!cache.has(cacheKey)) cache.set(cacheKey, func.apply(this, args));
    return cache.get(cacheKey);
  };
}
// Example usage:
const heavyComputation = (input) => input; // Simulate heavy computation
const memoizedComputation = memoize(heavyComputation);
const obj1 = { a: 1, b: 2 };
const obj2 = { b: 2, a: 1 };
console.log(memoizedComputation(obj1)); // Caches result
console.log(memoizedComputation(obj2)); // Returns cached result
```

This exercise assumes JSON-like, acyclic inputs. It does not support `BigInt`, symbols, functions,
cycles, maps, sets, or distinct object identities with the same structure, and delimiter-based keys
can collide. Production memoization should define argument semantics and eviction; nested `Map` and
`WeakMap` caches are often safer for identity-based object arguments.

## Write a function that ensures a maximum of maxLimit concurrent asynchronous operations while processing an array of inputs and calling a final callback with all outputs.

**Answer**

```javascript
function mapLimit(inputs, maxLimit, asyncFn, finalCallback) {
  if (!Number.isInteger(maxLimit) || maxLimit < 1) {
    throw new RangeError('maxLimit must be a positive integer');
  }

  const results = new Array(inputs.length);
  let inFlight = 0;
  let nextIndex = 0;
  let completed = 0;

  function processNext() {
    if (completed === inputs.length) {
      finalCallback(results);
      return;
    }

    while (inFlight < maxLimit && nextIndex < inputs.length) {
      const currentIndex = nextIndex++;
      inFlight++;
      asyncFn(inputs[currentIndex], (err, result) => {
        results[currentIndex] = err ? { error: err } : result;
        inFlight--;
        completed++;
        processNext();
      });
    }
  }

  if (inputs.length === 0) finalCallback([]);
  else processNext();
}
// Example async function simulating an asynchronous operation.
function asyncOperation(input, callback) {
  const delay = Math.random() * 1000;
  setTimeout(() => callback(null, input * 2), delay);
}
// Example usage:
const inputs = [1, 2, 3, 4, 5];
const maxConcurrent = 2;
mapLimit(inputs, maxConcurrent, asyncOperation, (results) => {
  console.log('All operations completed:', results);
});
```

This contract records each failure at its input position and continues processing. A fail-fast API
would instead stop launching work and call a Node-style final callback with the first error.

## References

- [ECMAScript language specification](https://tc39.es/ecma262/)
- [HTML event loops](https://html.spec.whatwg.org/multipage/webappapis.html#event-loops)
- [Fetch standard](https://fetch.spec.whatwg.org/)
- [HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [Cookie specification](https://www.rfc-editor.org/rfc/rfc6265)
- [Web performance metrics](https://web.dev/articles/vitals)
