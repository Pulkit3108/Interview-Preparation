# JavaScript

JavaScript language fundamentals, asynchronous programming, browser behavior, and coding exercises.

[Back to the question-bank index](../README.md)

## Topic Map

- [Language fundamentals, functions, and scope](#what-is-hoisting-and-are-letvariables-hoisted-and-what-is-temporal-dead-zone)
- [Objects, prototypes, classes, and modules](#what-are-object-prototypes)
- [Arrays, iteration, and collections](#explain-map-filter-and-reduce-methods-with-an-example)
- [Asynchronous JavaScript and promises](#difference-between-callback-promises-and-async-await)
- [Browser storage, rendering, networking, and performance](#what-different-types-of-storage-in-browsers-are-there)
- [Implementation exercises](#write-an-implementation-of-the-bind-function)
- [Output and behavior exercises](#is-i-visible-outside-the-settimeout-callback)

## What is Hoisting and are `let`variables hoisted and what is Temporal Dead Zone?

**Answer**

Hoisting is a JavaScript mechanism where variable and function declarations are moved to the top of their scope before code execution. This means you can use a variable or function before it is declared in your code.
Yes, let variables are hoisted in JavaScript, but they are not initialized. This means that the block of code is aware of the variable, but it cannot be used until it has been declared
Attempting to access the variable before its declaration will result in a ReferenceError. This period is known as the Temporal Dead Zone

## Difference between `var`, `let`, and `const` keywords

**Answer**

var is function-scoped and hoisted, allowing reassignment, and can be redeclared
let is block-scoped, hoisted, and allows reassignment, can't be redeclared
const is block-scoped, hoisted, and does not allow reassignment (except for object and array content).

## What is Shadowing?

**Answer**

In JavaScript, shadowing occurs when a variable declared within a certain scope (like a function or a block) has the same name as a variable in an outer scope. The inner variable "shadows" the outer one, meaning that within the inner scope, any reference to that variable name will access the inner variable instead of the outer one

## Difference between Normal and Arrow Functions

**Answer**

Regular functions are hoisted to the top of their containing scope, but arrow functions can't be accessed before they are initialized.

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

Lexical environment in JavaScript is a data structure that stores the variables and functions that are defined in the current scope and all of the outer scopes using a reference to an outer environment
Execution context in JavaScript is the environment in which JavaScript code is executed. It contains information about the current scope, variables, and functions. Each time a function is called, a new execution context is created.
Everything in JS happens inside this execution context. It is divided into two components. One is memory and the other is code.

## Explain JavaScript Execution and Microtask Queue.

**Answer**

JavaScript Execution: The JavaScript engine scans a script file, and it makes an environment called the Execution Context that handles the entire transformation and execution of the code.
There are two phases of JavaScript execution context:
Creation phase: In this phase, the JavaScript engine creates the execution context and sets up the script's environment. It determines the values of variables and functions and sets up the scope chain for the execution context.
Execution phase: In this phase, the JavaScript engine executes the code in the execution context. It processes statements or expressions in the script and evaluates function calls.
The Microtask Queue is like the Callback Queue, but the Microtask Queue has higher priority. All the callback functions coming through Promises and Mutation Observer will go inside the Microtask Queue.

## What is the Event Loop?

**Answer**

Event loop is a loop that runs indefinitely and continuously monitors both the call stack and the task queue. If the call stack is empty, it takes the first callback from the task queue and pushes it onto the call stack for execution. This process ensures that callbacks are only executed when the stack is clear, allowing the program to handle asynchronous operations efficiently without blocking the execution.

## What is Callback?

**Answer**

A JavaScript callback is a function that is to be executed after another function has finished execution.
Any function that is passed as an argument to another function so that it can be executed in that other function is called as a callback function

## Explain Promises & Closure in JavaScript.

**Answer**

Promise: It is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value.
Closure: It is the combination of a function and the lexical environment within which that function was declared. This environment consists of any local variables that were in scope at the time the closure was created.

## What are Disadvantages of closure?

**Answer**

Memory Consumption: Closures retain references to their outer scope, which can lead to increased memory usage and potential memory leaks.
Performance Overhead: The additional memory management and scope retention can introduce performance overhead.
Complexity and Readability: Closures can make code more complex and harder to understand, especially for developers unfamiliar with the concept.
Debugging Challenges: Debugging closures can be difficult due to the retained state of the outer scope.
Potential for Unintended Behavior: Closures can lead to unintended behavior, particularly in loops and asynchronous code.

## Difference between Callback, Promises, and Async Await

**Answer**

Callbacks, Promises, and Async/Await provide us with different approaches to handling asynchronous operations in JavaScript.
While callbacks are simple but prone to callback hell,
Promises and Async/Await provide cleaner and more readable code structures
Note: await keyword is always used inside the async function scope.

Promise Combinators - `all`, `race`, `allSettled`, `any`
.all() lets you know when either all input promises have been fulfilled or when one of them is rejected. If any of the promises fail the overall promise fails.
.race() As the name suggests all the promises will race against each other and whichever promise is resolved/rejected first wins.
.allSettled() returns an Array of all Promises whether it is resolved or rejected. It will settle when all the supplied promises are settled.  It won’t stop executing if any of the Promises is rejected.
.any() works similar to that of .race() but will only return the first resolved promises. - if all items of promise input are unsuccessful then will return an array of rejected promises.

## How will you make multiple API calls simultaneously in JavaScript?

**Answer**

In JavaScript, you can make multiple API calls simultaneously using Promise.all(). This method takes an array of promises and returns a single promise that resolves when all of the promises in the array have been resolved or rejects if any of the promises in the array are rejected.

## What is a static keyword in JavaScript?

**Answer**

the static keyword defines a static method or property for a class. Static members are associated with the class itself, not with class instances.
Inside a static method, the this keyword refers to the class itself, not to an instance.
Use Cases: Utility functions, Constants, Factory methods:

## What is `use strict` in Javascript?

**Answer**

"use strict" is a directive in JavaScript that enables strict mode. Strict mode is a way to opt into a restricted variant of JavaScript, which helps catch common coding errors and "unsafe" actions.
Actions:
Disallows Undeclared Variables
Disallows Duplicates in Function Parameters
Prevents this from Defaulting to the Global Object:
Disallows Deleting Plain Names

## Explain the behavior of the 'this' keyword

**Answer**

`this` is determined by how a function is invoked, not simply by where it is written. A method call
such as `object.method()` normally binds `this` to `object`; `call`, `apply`, or `bind` can provide it
explicitly; constructor calls bind it to the new instance. Arrow functions do not create their own
`this` and instead capture it lexically from the surrounding scope. In strict-mode plain function
calls, `this` is `undefined`.

## What is a Template Literal?

**Answer**

A template literal, also known as a template string, is a feature in JavaScript that allows you to create strings in a more flexible and readable way. They are denoted by backticks ( ` ) instead of single or double quotes

## What is Tagged Template Literal?

**Answer**

A tagged template literal is a template literal that uses a function, called a tag function, to parse the template literal. This allows you to perform custom operations on the template literal, rather than just creating a string

## Difference between `==` and `===` operators

**Answer**

The "==" operator compares values after performing type conversion, while the "===" operator compares values without type conversion.

## How does || and && operator works in JS?

**Answer**

Logical OR (||) The logical OR operator (||) evaluates operands from left to right and returns the first truthy value it encounters. If all operands are falsy, it returns the last operand.
Logical AND (&&) The logical AND operator (&&) evaluates operands from left to right and returns the first falsy value it encounters. If all operands are truthy, it returns the last operand.

## Difference between `null`, `undefined`, and `not defined`

**Answer**

null: Represents the intentional absence of any object value.
It is an assignment value that can be assigned to a variable as a representation of no value.
undefined: A variable that has been declared but not assigned a value. It is the default value for uninitialized variables
not defined: A variable that has not been declared at all. Trying to access such a variable will result in a ReferenceError.

## What is isNaN?

**Answer**

isNaN Function:
Determines whether a value is NaN.
Performs type coercion before checking.
Number.isNaN Function:
Determines whether a value is NaN without type coercion.
More reliable for checking NaN.
Infinity is Not NaN:
Infinity and -Infinity are special numeric values representing positive and negative infinity.
They are considered numbers, not NaN.

## Explain Implicit Type Coercion in JS

**Answer**

Implicit type coercion in JavaScript refers to the automatic conversion of values from one data type to another during operations, without explicit instructions from the developer

## What is eval()?

**Answer**

The eval() function in JavaScript is a global function that evaluates a string of JavaScript code and executes it. It can be used to dynamically execute code that is constructed as a string at runtime.

## What will be the value of 0.1 + 0.2 === 0.3 and why?

**Answer**

In JavaScript, the expression 0.1 + 0.2 === 0.3 evaluates to false. This is due to the way floating-point arithmetic works in JavaScript.
JavaScript uses the IEEE 754 standard for representing floating-point numbers. This standard cannot precisely represent some decimal fractions, leading to small rounding errors. When you add 0.1 and 0.2, the result is a number very close to 0.3, but not exactly 0.3.
To compare floating-point numbers for equality, a common approach is to check if they are close enough within a small tolerance
const tolerance = 1e-10;

## What is Truthy and Falsy Value

**Answer**

**When non-boolean values are used in a boolean context, such as the condition of an if statement, they will be coerced into either true or false.**

Values that are coerced into truth are called truthy and values that are coerced into false are called falsy

## What is the Spread and Rest Operator?

**Answer**

JavaScript uses three dots (...) for both the rest and spread operators. But these two operators are not the same.
The main difference between rest and spread is that the rest operator puts the rest of some specific user-supplied values into a JavaScript array.
const { name, age, ...rest } = person;
But the spread syntax expands iterable into individual elements.
const spread = [...arr1, ...arr2];

## Explain Map, Filter, and Reduce methods with an example

**Answer**

.map() transforms every element in an array individually and creates a new array.
const arr = arr.map((x) => x * 2);
.filter() removes elements that are not required and creates a new array containing the ones needed.
const arr = arr.filter((el) => el > 3);
.reduce() reduces all array elements into a single value.
const sum = arr.reduce((acc, val) => acc + val, 0);

## Which methods you can use on array to modify it’s original state?

**Answer**

push(): Adds elements to the end.
pop(): Removes the last element.
shift(): Removes the first element.
unshift(): Adds elements to the beginning.
splice(): Adds, removes, or replaces elements.
sort(): Sorts the elements.
reverse(): Reverses the order of elements.
fill(): Fills elements with a static value.
copyWithin(): Copies elements within the array.

## What is the difference between splice and slice?

**Answer**

splice():
Used to add, remove, or replace elements in an array.
Modifies the original array.
Returns an array of deleted elements.
Example: arr.splice(1, 2, 'a', 'b') removes 2 elements starting from index 1 and adds 'a' and 'b'.
slice():
Used to create a shallow copy of a portion of an array.

**Does not modify the original array.**

Returns a new array with the extracted elements.
Example: arr.slice(1, 3) extracts elements from index 1 to 3 (exclusive).

## What is the difference between JSON.parse() and JSON.stringify()

**Answer**

JSON.parse():
Converts a JSON string into a JavaScript object.
Used when you need to work with JSON data received as a string.
Example: JSON.parse('{"name": "John"}') results in { name: "John" }.
JSON.stringify():
Converts a JavaScript object into a JSON string.
Used when you need to send or store JavaScript objects as JSON data.
Example: JSON.stringify({ name: "John" }) results in '{"name":"John"}'.

## What is a deep copy and shallow copy in JavaScript?

**Answer**

Shallow Copy: A shallow copy of an object is a copy where only the first level of the object is duplicated. Nested objects are not copied and still reference the same memory locations as the original.
const copy = { ...obj };
Deep Copy: A deep copy of an object is a copy where all levels of the object are duplicated. Nested objects are also copied, ensuring that the new object is completely independent of the original.
deepCopy = JSON.parse(JSON.stringify(original));

Explicit Object Binding - `call`, `apply`, `bind`
call attaches this into a function and executes the function immediately:
apply is similar to call except that it takes an array-like object instead of listing the arguments out one at a time:
bind attaches this into function and it needs to be invoked separately.

## What is Currying?

**Answer**

Currying in JavaScript is a technique of transforming a function that takes multiple arguments into a sequence of functions, each taking a single argument
We can achieve it using bind and closures.

## What is Method Chaining?

**Answer**

Method Chaining: A technique where multiple methods are called on the same object consecutively, with each method returning the object itself for further chaining.

## What is a Partial application?

**Answer**

Partial application in JavaScript is a technique where you create a new function by pre-filling some of the arguments of an existing function. This new function can then be called with the remaining arguments.

## What are the phases of Event Propagation?

**Answer**

Event propagation in JavaScript consists of three phases:
Capturing Phase: The event starts from the root of the DOM tree and propagates down to the target element. Event listeners registered for this phase will be triggered in this top-down manner.
Target Phase: The event reaches the target element. Event listeners registered directly on the target element will be triggered.
Bubbling Phase: The event propagates back up from the target element to the root of the DOM tree. Event listeners registered for this phase will be triggered in this bottom-up manner.

## What is Event Propagation - Bubbling & Capturing?

**Answer**

Event propagation is a mechanism that defines how events travel through the DOM tree in a web page. It determines the order in which event handlers are executed when an event occurs on an element.
With bubbling, the event is first captured and handled by the innermost element and then propagated to the outer elements.
With capturing, the event is first captured by the outermost element and propagated to the inner elements.

## What is Event Delegation?

**Answer**

Event delegation is a JavaScript design pattern that lets developers handle events for multiple child elements by attaching a single event listener to a common ancestor element

## What is a constructor function?

**Answer**

Constructor Function in JavaScript is a special type of function used to create and initialize objects. When called with the new keyword, a constructor function sets up a new object and assigns properties and methods to it.

## What is Debouncing and Throttling?

**Answer**

Debouncing Prevents a function from being called until a specific period has passed since it was last called. Debouncing monitors the time delay between user actions and only executes the callback function if the delay exceeds the time delay defined by the developer. This is ideal for tasks that don't need to be executed repeatedly in quick succession, such as API calls based on user input, form validation, search box suggestions, and window resize events.
Throttling Limits the number of times a function can be called in a certain amount of time. Throttling uses the time delay to execute the callback function at regular intervals until the event trigger is active. This is suited for controlling the execution rate of functions called in response to events like scrolling or resizing, button click events, and rate-limiting API calls.

## What is the difference between setInterval() and setTimeout()?

**Answer**

setTimeout(): Useful for delaying the execution of a function, such as showing a message after a delay or executing a function after a certain period.
setInterval(): Useful for repeated actions, such as updating a clock, polling a server at regular intervals, or creating animations.

## What are Object Prototypes?

**Answer**

In JavaScript, object prototypes are the mechanisms by which objects inherit properties and methods from one another.

**When you create an object in JavaScript, it automatically inherits properties and methods from another object, known as its prototype.**

For Ex: arr.__proto__ === Array.prototype

## What is Prototypal Inheritance?

**Answer**

Prototypal inheritance is a mechanism in JavaScript where objects can inherit properties and methods from other objects. Unlike classical inheritance, which relies on classes and constructors, JavaScript uses prototypes to achieve inheritance.

## What is the difference between.prototype vs.__proto__?

**Answer**

.prototype is a property of constructor functions. It is used to define properties and methods that should be inherited by instances created by that constructor.
.__proto__ is used to access or modify the prototype of an existing object, effectively linking the object to its prototype.

## What is a Prototype Chain?

**Answer**

Prototype chain: The prototype itself is an object, which can also have its own prototype, and so on. This forms a chain of prototypes, known as the prototype chain.
All objects in JavaScript ultimately inherit from Object.prototype, which provides a set of basic properties and methods like toString(), hasOwnProperty(), etc.

## Can we implement Polymorphism in JavaScript?

**Answer**

Yes, polymorphism can be implemented in JavaScript. Polymorphism allows objects to be treated as instances of their parent class rather than their actual class. This can be achieved through method overriding and interface implementation.

## What OOPs concept we can follow in JavaScript?

**Answer**

JavaScript is a versatile language that supports Object-Oriented Programming (OOP) concepts
Encapsulation: Bundling data and methods into a single unit and restricting access to some components.
Inheritance: Creating hierarchical relationships between classes, allowing child classes to inherit properties and methods from parent classes.
Polymorphism: Treating different classes as instances of the same class through inheritance, allowing methods to be used interchangeably.
Abstraction: Hiding complex implementation details and showing only the essential features of an object.

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

V8 (Google Chrome, Node.js): Uses Timsort.
SpiderMonkey (Mozilla Firefox): Uses Merge Sort.
JavaScriptCore (Safari): Uses Quicksort (with optimizations).
Default Behavior: The Array.prototype.sort() method sorts elements as strings in ascending order by default.
Custom Sort Function: You can provide a custom compare function to sort numbers or objects based on specific criteria.
Quick Sort is often preferred for its speed and efficiency in average cases.
Merge Sort is preferred for its stability and consistent performance.
Heap Sort is chosen for its in-place sorting and good worst-case performance.
Timsort is used in practical applications for its efficiency with real-world data.

## What is yield in JavaScript?

**Answer**

yield is a keyword used in JavaScript within generator functions to pause and resume the execution of the function. It allows the function to produce a sequence of values over time, rather than computing them all at once and sending them back in a single return statement.

## What is a symbol in JavaScript?

**Answer**

Symbol is a unique and immutable primitive value that can be used as an identifier for object properties. Symbols are often used to avoid property name collisions in objects, especially when working with code that involves multiple libraries or frameworks.

## What is a proxy in JavaScript?

**Answer**

Proxy in JavaScript is an object that allows you to intercept and customize operations performed on another object, known as the target object. Proxies provide a way to define custom behavior for fundamental operations (e.g., property lookup, assignment, enumeration, function invocation, etc.).

## What is a weakSet and weakMap?

**Answer**

WeakSet:
A collection of objects with weak references.
Only objects can be added to a WeakSet.
Objects in a WeakSet can be garbage-collected if there are no other references to them.

**Does not support iteration methods.**

Methods: add, delete, has.
WeakMap:
A collection of key-value pairs with weak references to the keys.
Only objects can be used as keys in a WeakMap.
Key-value pairs in a WeakMap can be garbage-collected if there are no other references to the keys.

**Does not support iteration methods.**

Methods: set, get, delete, has.

## What is a Mutation Observer?

**Answer**

Mutation Observer: It is an interface that provides the ability to watch for changes being made to the DOM tree. It is designed to replace the older Mutation Events feature, which was part of the DOM3 Events specification.
It provides a way to react to changes in the DOM, such as when elements are added, removed, or modified

## What is DOM and BOM?

**Answer**

The Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content.
The Browser Object Model (BOM) is a collection of objects exposed by the browser that allow JavaScript to interact with the browser window, document, and other browser-specific functionalities. The BOM includes objects such as Window, Navigator, Location, History, and Screen.

## What is a Critical Rendering Path?

**Answer**

The Critical Rendering Path is the sequence of steps the browser goes through to convert the HTML, CSS, and JavaScript into pixels on the screen.
Optimizing the critical render path improves render performance

## What is the difference between a Website and a Web Application?

**Answer**

Websites are a collection of webpages that provide information through text, visuals, or video. For Ex: a Blog Website
Web applications are software programs that run on a web server and provide interactivity and functionality.
While all web applications are technically websites, not all websites are web applications. For Ex: YouTube

## What different types of storage in browsers are there?

**Answer**

Local Storage: Key-value storage with no expiration time.
Session Storage: Key-value storage scoped to the browser session.
Cookies: Small pieces of data for session management and tracking.
IndexedDB: Low-level API for storing large amounts of structured data.
Web SQL (Deprecated): Relational database storage (not recommended for new projects).

## How do cookies work?

**Answer**

Cookies are small pieces of data stored on a user's device by a web browser while browsing a website. They are used to remember information about the user, such as login status, preferences, and tracking information. Here's how cookies work:
Creation and Storage:
Set by Server: When a user visits a website, the server can send a Set-Cookie header in the HTTP response. This instructs the browser to store the cookie.
Stored by Browser: The browser stores the cookie on the user's device, typically in a text file or a database.
Structure of a Cookie:
Name-Value Pair: A cookie consists of a name and a value, which store the actual data.
Attributes: Cookies can have various attributes, such as Domain, Path, Expires, Max-Age, Secure, and HttpOnly.
Sending Cookies:
Included in Requests: For subsequent requests to the same domain, the browser automatically includes the relevant cookies in the Cookie header of the HTTP request.
Server Reads Cookies: The server reads the cookies from the request header and uses the information to provide a personalized experience or maintain session state

## How are cookies passed in an HTTPS request?

**Answer**

Cookies are passed in an HTTPS request in a similar manner to how they are passed in an HTTP request. The primary difference is that HTTPS provides an encrypted communication channel, ensuring that the cookies and other data are securely transmitted between the client and server. Here’s how cookies are passed in an HTTPS request:
Setting a Cookie:

## When a user visits a website, the server can send a Set-Cookie header in the HTTP response to instruct the browser to store a cookie.

**Answer**

Example response with a Set-Cookie header:
HTTP/1.1 200 OK
Set-Cookie: sessionId=abc123; Path=/; Secure; HttpOnly
The browser stores the cookie with the specified attributes.
Storing the Cookie:
The browser stores the cookie on the user's device, typically in a text file or a database, along with its attributes (e.g., domain, path, expiration date, secure flag).
Sending the Cookie:
For subsequent requests to the same domain and path, the browser automatically includes the relevant cookies in the Cookie header of the HTTPS request.
Example HTTPS request with a Cookie header:
GET /dashboard HTTP/1.1
Host: example.com
Cookie: sessionId=abc123
The server reads the Cookie header from the request and uses the information to identify the user's session or provide a personalized experience.
Secure Flag: When the Secure attribute is set on a cookie, the browser ensures that the cookie is only sent over secure HTTPS connections. This prevents the cookie from being transmitted over unencrypted HTTP connections, protecting it from eavesdropping and man-in-the-middle attacks.
HttpOnly Flag: When the HttpOnly attribute is set on a cookie, the cookie is not accessible via client-side scripts (e.g., JavaScript). This helps mitigate cross-site scripting (XSS) attacks by preventing malicious scripts from accessing the cookie.

## How is the expiration time of cookies set and managed?

**Answer**

The expiration time of cookies determines how long a cookie will be stored on the user's device before it is automatically deleted. There are two main ways to set the expiration time of cookies: using the Expires attribute and the Max-Age attribute.
Expires Attribute: The Expires attribute specifies the exact date and time when the cookie should expire.
Format: The date and time must be in a specific format (e.g., Wdy, DD-Mon-YYYY HH:MM:SS GMT).
Set-Cookie: sessionId=abc123; Expires=Wed, 01 Jan 2023 00:00:00 GMT; Path=/
Max-Age Attribute: The Max-Age attribute specifies the maximum age of the cookie in seconds. After this time, the cookie will expire.
Example: Setting a cookie to expire after 3600 seconds (1 hour):
Set-Cookie: sessionId=abc123; Max-Age=3600; Path=/
Session Cookies: If neither Expires nor Max-Age is set, the cookie is considered a session cookie. Session cookies are temporary and are deleted when the user closes the browser.
Example: Setting a session cookie:
Set-Cookie: sessionId=abc123; Path=/

## What is Browser Caching and what are its benefits?

**Answer**

Browser Caching: A mechanism that allows web browsers to store copies of web resources locally on the user's device, improving performance and user experience.
Benefits:
Improved Performance: Faster load times and reduced latency.
Reduced Server Load: Fewer requests to the server and reduced bandwidth usage.
Better User Experience: Smooth navigation and limited offline access.
Cost Savings: Bandwidth savings and improved scalability.
Caching Headers:
Cache-Control: Specifies caching directives.
Expires: Specifies an absolute expiration time.
ETag: Provides a unique identifier for resource versions.
Last-Modified: Indicates the last modification time of the resource.

## What is Server-Side Rendering (SSR) and how to optimize it.

**Answer**

Server-Side Rendering (SSR): Generates HTML on the server and sends it to the client.
Benefits: Improved performance, SEO, and user experience.
Optimization Techniques: Caching, code splitting, minimizing server processing time, reducing payload size, using a CDN, lazy loading, optimizing images, and prefetching/preloading resources.

## What is SEO?

**Answer**

SEO (Search Engine Optimization): The practice of optimizing a website to improve its visibility and ranking on search engine results pages.
Key Components: On-page SEO, off-page SEO, technical SEO, and local SEO.
Benefits: Increased visibility, organic traffic, credibility, better user experience, and competitive advantage.

## What is the Largest Contentful Paint (LCP)?

**Answer**

Largest Contentful Paint (LCP): A performance metric that measures the time it takes for the largest content element in the viewport to become visible.
Importance: LCP is crucial for user experience as it affects the perceived load time of the main content.
Ideal Time: LCP should occur within 2.5 seconds for a good user experience.
Optimization Techniques: Optimize images, improve server response times, minimize render-blocking resources, preload key resources, and optimize web fonts.

## What is webpack and polyfills?

**Answer**

Webpack is a powerful and flexible module bundler for JavaScript applications. It takes your application's modules and dependencies, processes them, and bundles them into one or more output files. This helps in optimizing the loading time and performance of your web application..
Polyfills are pieces of code (usually JavaScript) used to provide modern functionality on older browsers that do not natively support it. They essentially "fill in" the gaps in browser support for newer web standards.

## What is Babel?

**Answer**

Babel: A JavaScript compiler that transforms modern JavaScript into a version compatible with older environments.
Transpilation: Converts ES6+ code into ES5 or other specified versions.
Plugins and Presets: Uses configurable plugins and presets to apply specific transformations.
Polyfills: Adds support for new JavaScript features in older environments.
Integration: Works seamlessly with build tools like Webpack, Gulp, and Grunt.

## What is an HTTP redirect? What other methods are available for redirecting users to a different page?

**Answer**

HTTP redirect is a response from a web server that instructs the client's browser to navigate to a different URL. This is typically done using HTTP status codes in the 3xx range, such as 301 (Moved Permanently) or 302 (Found).
HTTP Redirect (Server-Side Redirect):
301 Moved Permanently: Indicates that the resource has been permanently moved to a new URL.
302 Found: Indicates that the resource is temporarily located at a different URL.
303 See Other: Indicates that the response to the request can be found at another URL using a GET method.
307 Temporary Redirect: Indicates that the resource is temporarily located at a different URL, and the request method should not change.
308 Permanent Redirect: Similar to 301, but the request method should not change.
Example in PHP:
<?php
// 301 Moved Permanently
header("Location: http://www.new-url.com", true, 301);
exit();
Meta Refresh (Client-Side Redirect):
Uses the <meta> tag in the HTML <head> section to instruct the browser to redirect after a specified number of seconds.
Example:
<meta http-equiv="refresh" content="5;url=http://www.new-url.com">
JavaScript Redirect (Client-Side Redirect):
Uses JavaScript to change the location of the browser.
Example:
<script type="text/javascript">
    window.location.href = "http://www.new-url.com";
</script>
HTML Anchor Tag:
Uses an anchor (<a>) tag to provide a clickable link that redirects the user to a different page.
Example:
<a href="http://www.new-url.com">Click here to go to the new page</a>

## How might a web app determine whether an end user is accessing the site via a mobile phone or a desktop browser?

**Answer**

A web app can determine whether an end user is accessing the site via a mobile phone or a desktop browser by examining the User-Agent string sent by the browser in the HTTP request headers. The User-Agent string contains information about the browser, operating system, and device type.

## What Happens When You Type a URL into Your Browser?

**Answer**

Browser Parses the URL The browser identifies the components: scheme (https), domain (example.com), and path (/hello-world).
DNS Lookup The browser checks its cache or queries a DNS resolver (ISP or public DNS like Google’s 8.8.8.8) to translate the domain name into an IP address.
If not cached, the resolver performs a recursive DNS lookup, contacting root, TLD, and authoritative name servers.
Establishing a Connection A TCP connection is initiated between the browser and the server at the resolved IP address.
If the URL uses HTTPS, a TLS handshake is performed to encrypt the connection.
Sending the HTTP Request The browser sends an HTTP request with details like method (GET/POST), headers (e.g., User-Agent), and optional body data.
Example: GET /hello-world HTTP/1.1.
Server Processes the Request The server identifies the resource from the request path and processes it.
For dynamic content, the server might query a database, run application logic, and generate the response on the fly.
Returning the Response The server responds with:
Status Line: Indicates success or failure (e.g., 200 OK, 404 Not Found).
Headers: Metadata like Content-Type (e.g., text/html) and caching instructions.
Body: The requested content (e.g., HTML, JSON, or image data).
Browser Renders the Content The browser parses the HTML and makes additional requests for linked resources (e.g., CSS, JS, images).
Resources are rendered progressively, and JavaScript is executed to enhance interactivity.
Caching and Optimization Browsers cache resources based on headers like Cache-Control.
CDNs (Content Delivery Networks) and edge servers may serve static content to reduce latency.

## Can you explain DNS caching and its layers?

**Answer**

DNS caching occurs at multiple layers to improve lookup efficiency:
Browser Cache: Stores DNS records for previously visited sites.
Operating System Cache: Maintains a cache of DNS queries to reduce repeated lookups.
ISP Cache: Internet Service Providers cache DNS records to speed up resolution for their users.

## What is the TLS handshake and why is it important for HTTPS connections?

**Answer**

TLS handshake is a process that establishes a secure connection between the browser and the server. It involves:
Exchange of Protocol Versions: Ensures both parties support the same version of TLS.
Cipher Suite Negotiation: Determines the encryption algorithms to be used.
Authentication: The server presents a digital certificate to verify its identity.
Session Keys Generation: Secure keys are generated for encrypting the data transfer. This process ensures data integrity, confidentiality, and authentication, making HTTPS connections secure.

## How do CDNs improve web performance?

**Answer**

Content Delivery Networks (CDNs) enhance performance by:
Geographical Distribution: Serving content from servers closer to the user, reducing latency.
Load Balancing: Distributing traffic across multiple servers to prevent overload.
Caching Static Content: Storing copies of static resources (e.g., images, CSS) to reduce server load and speed up delivery.

## What causes SSL errors in browsers and how do you fix them?

**Answer**

SSL errors occur when a browser can't establish a secure HTTPS connection with a server—essentially, the browser doesn't trust the connection. This typically appears as a broken or red 🔒 icon. The most common causes include:
- An expired SSL certificate.
- A self-signed certificate or one not issued by a trusted Certificate Authority.
- A mismatch between the certificate and the domain name.
- An incomplete or misconfigured certificate chain.
To fix these errors, you should:
- 1. Verify Certificate Validity:
- ○ Use tools like SSL Labs or browser developer tools to ensure the certificate isn’t expired, is issued by a trusted CA, and matches your domain name.
- 2. Install Intermediate Certificates:
- ○ Ensure that the server is configured to provide the full certificate chain; missing intermediate certificates can lead to browser distrust.
- 3. Force HTTPS Redirects:
- ○ Configure your server (using .htaccess, Nginx, etc.) to redirect all traffic to HTTPS, eliminating potential mixed content issues.
- 4. Eliminate Mixed Content:
- ○ Make sure every resource on your site (images, scripts, fonts, etc.) is served over HTTPS.
While you can bypass SSL warnings temporarily in a development environment (using tools like mkcert), it’s critical not to ignore these issues in production. Being able to explain these points clearly shows an understanding of web security fundamentals and full-stack deployment troubleshooting, which is vital in technical interviews.

## What is asynchronous resource loading and how does it benefit web performance?

**Answer**

Asynchronous resource loading allows scripts to be fetched and executed without blocking the rendering of the page. This can be achieved using:
defer Attribute: Scripts are executed after the HTML is fully parsed.
async Attribute: Scripts are executed as soon as they are downloaded. This improves page load times and enhances user experience by allowing the main content to be displayed faster.

## Can you explain the significance of different HTTP response codes?

**Answer**

HTTP response codes indicate the status of the request:
1xx: Informational Responses
100 Continue: The server has received the request headers, and the client should proceed to send the request body.
101 Switching Protocols: The requester has asked the server to switch protocols, and the server has agreed to do so.
2xx: Success
200 OK: The request has succeeded. The meaning of success depends on the HTTP method (GET, POST, PUT, DELETE).
201 Created: The request has been fulfilled, resulting in the creation of a new resource.
202 Accepted: The request has been accepted for processing, but the processing has not been completed.
204 No Content: The server successfully processed the request, but is not returning any content.
3xx: Redirection
301 Moved Permanently: The requested resource has been permanently moved to a new URL.
302 Found: The requested resource resides temporarily under a different URL.
303 See Other: The response to the request can be found under another URL using a GET method.
304 Not Modified: The resource has not been modified since the last request.
307 Temporary Redirect: The requested resource resides temporarily under a different URL, and the client should use the original URL for future requests.
308 Permanent Redirect: The requested resource has been permanently moved to a new URL, and the client should use the new URL for future requests.
4xx: Client Errors
400 Bad Request: The server cannot or will not process the request due to a client error (e.g., malformed request syntax).
401 Unauthorized: The request requires user authentication.
403 Forbidden: The server understood the request, but refuses to authorize it.
404 Not Found: The server cannot find the requested resource.
405 Method Not Allowed: The request method is known by the server but is not supported by the target resource.
409 Conflict: The request could not be completed due to a conflict with the current state of the resource.
410 Gone: The requested resource is no longer available and will not be available again.
429 Too Many Requests: The user has sent too many requests in a given amount of time ("rate limiting").
5xx: Server Errors
500 Internal Server Error: The server encountered an unexpected condition that prevented it from fulfilling the request.
501 Not Implemented: The server does not support the functionality required to fulfill the request.
502 Bad Gateway: The server, while acting as a gateway or proxy, received an invalid response from the upstream server.
503 Service Unavailable: The server is currently unable to handle the request due to temporary overloading or maintenance.
504 Gateway Timeout: The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server.
505 HTTP Version Not Supported: The server does not support the HTTP protocol version used in the request.

## What are the ways to reduce the load time of a webpage?

**Answer**

Optimize Images:
Compression: Use image compression tools to reduce file sizes without compromising quality.
Formats: Use modern image formats like WebP for better compression.
Responsive Images: Serve appropriately sized images for different devices using the srcset attribute.
Minimize HTTP Requests:
Combine Files: Combine CSS and JavaScript files to reduce the number of HTTP requests.
Inline Small CSS and JavaScript: Inline small CSS and JavaScript directly into the HTML to reduce requests.
Use Content Delivery Networks (CDNs):
CDNs: Distribute content across multiple servers worldwide to reduce latency and improve load times for users globally.
Enable Browser Caching:
Caching: Set appropriate cache headers to allow browsers to cache static resources, reducing the need to re-download them on subsequent visits.
Minify CSS, JavaScript, and HTML:
Minification: Remove unnecessary characters (whitespace, comments) from CSS, JavaScript, and HTML files to reduce their size.
Reduce Server Response Time:
Optimize Server: Ensure your server is optimized and has sufficient resources to handle requests efficiently.
Use a Fast Hosting Provider: Choose a reliable and fast hosting provider.
Enable Compression:
Gzip/Brotli Compression: Enable Gzip or Brotli compression on your server to reduce the size of HTML, CSS, and JavaScript files sent to the browser.
Optimize CSS and JavaScript Delivery:
Asynchronous Loading: Load JavaScript files asynchronously using the async or defer attributes.
Critical CSS: Inline critical CSS required for above-the-fold content and load the rest asynchronously.
Reduce Redirects:
Minimize Redirects: Avoid unnecessary redirects as they add additional HTTP requests and increase load time.
Use Lazy Loading:
Lazy Loading: Implement lazy loading for images and other media to load them only when they are about to enter the viewport.
Optimize Web Fonts:
Font Loading: Use modern font loading techniques to reduce the impact of web fonts on load time.
Subset Fonts: Include only the characters needed for your webpage to reduce font file sizes.
Monitor and Analyze Performance:
Performance Tools: Use tools like Google PageSpeed Insights, Lighthouse, and WebPageTest to analyze and monitor webpage performance and identify areas for improvement.

## How can you optimize images on an e-commerce website that loads a lot of products?

**Answer**

Image Compression:
Lossless Compression: Use tools like ImageOptim, TinyPNG, or JPEGmini to compress images without losing quality.
Lossy Compression: Apply lossy compression to further reduce file sizes while maintaining acceptable quality.
Use Modern Image Formats:
WebP: Use WebP format, which provides better compression than JPEG and PNG while maintaining quality.
AVIF: Consider using AVIF, a newer format that offers even better compression and quality than WebP.
Responsive Images:
Srcset Attribute: Use the srcset attribute to serve different image sizes based on the user's device resolution and screen size.
Picture Element: Use the <picture> element to provide different image formats and sizes for different devices and conditions.
Lazy Loading:
Deferred Loading: Implement lazy loading to defer the loading of images until they are about to enter the viewport. This reduces initial load time and bandwidth usage.
Native Lazy Loading: Use the loading="lazy" attribute on <img> tags for native lazy loading support in modern browsers.
Image Dimensions:
Specify Dimensions: Always specify the width and height attributes for images to prevent layout shifts and improve rendering performance.
Resize Images: Resize images to the appropriate dimensions for their display context to avoid serving unnecessarily large images.
Content Delivery Network (CDN):
Global Distribution: Use a CDN to cache and serve images from edge locations closer to users, reducing latency and improving load times.
Image Optimization Services: Leverage CDN features that automatically optimize and compress images on-the-fly.
Image Sprites:
Combine Images: Combine multiple small images (e.g., icons) into a single sprite sheet to reduce the number of HTTP requests.
Optimize Image Delivery:
Progressive JPEGs: Use progressive JPEGs that load a low-resolution version of the image first, followed by higher resolutions, improving perceived load times.
Adaptive Images: Serve different image resolutions based on the user's device and network conditions.
Caching:
Browser Caching: Set appropriate cache headers to allow browsers to cache images, reducing the need to re-download them on subsequent visits.

## Write an implementation of the bind function.

**Answer**

Function.prototype.myBind = function (...context) {
  return (...args) => {
      this.apply(context[0], context.slice(1).concat(args));
  }
};

## Write an implementation to Reverse an array.

**Answer**

```javascript
const reverseArray = (arr) => {
  let reversedArray = [];
  for (let i = arr.length - 1; i >= 0; i--) {
      reversedArray.push(arr[i]);
  }
  return reversedArray;
}
```

## Write an implementation of debounce function.

**Answer**

```javascript
const debounce = (fn, delay) => {
  let timer;
  return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
          fn.apply(this, args);
      }, delay);
  };
};
```

## Write an implementation of throttle function.

**Answer**

```javascript
const throttle = (fn, delay) => {
  let lastCall = 0;
  return (...args) => {
      const now = new Date().getTime();
      if (now - lastCall < delay) {
          return;
      }
      lastCall = now;
      return fn.apply(this, args);
  }
}
```

## Write an implementation to Flatten an array.

**Answer**

```javascript
const flattenArray = (arr) => {
  let flattenedArray = [];
  for (let i = 0; i < arr.length; i++) {
      if (Array.isArray(arr[i])) {
          flattenedArray = flattenedArray.concat(flattenArray(arr[i]));
      } else {
          flattenedArray.push(arr[i]);
      }
  }
  return flattenedArray;
}
```

## Write the implementation of a map function.

**Answer**

Function.prototype.myMap = function(callback) {
  let result = [];
  for (let i = 0; i < this.length; i++) {
    result.push(callback(this[i], i, this));
  }
  return result;
};

## Write an implementation to flatten an object.

**Answer**

```javascript
const flatten = (obj, parentKey = '', result = {}) => {
  for (let key in obj) {
      if (typeof obj[key] === 'object' && obj[key] !== null) {
          flatten(obj[key], parentKey + key + '.', result);
      } else {
          result[parentKey + key] = obj[key];
      }
  }
  return result;
};
```

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
function transformArray(inputArray) {
  const result = [];
  inputArray.forEach(innerArray => {
      innerArray.forEach(obj => {
          const newObj = {};
          newObj[obj.key] = obj.value;
          result.push(newObj);
      });
  });
  return result;
}
```

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
      if (number !== 0) {
          this.value /= number;
      } else {
          console.error('Division by zero is not allowed.');
      }
      return this;
  }
  getResult() {
      return this.value;
  }
}
```

## Design a Polyfill for Promise.all with Retry Callback

**Answer**

```javascript
function promiseAllWithRetry(promises, retryCount) {
  // Helper function to retry a promise
  function retryPromise(promise, retries) {
    return new Promise((resolve, reject) => {
      function attempt() {
        promise()
          .then(resolve)
          .catch((error) => {
            if (retries === 0) {
              reject(error);
            } else {
              retries--;
              attempt();
            }
          });
      }
      attempt();
    });
  }
  // Map each promise to a retryable promise
  const retryablePromises = promises.map(promise => retryPromise(promise, retryCount));
  // Use Promise.all to wait for all retryable promises
  return Promise.all(retryablePromises);
}
```

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
  detail: { message: 'Hello, World!' }
});
const targetElement = document.getElementById('myElement');
targetElement.dispatchEvent(myEvent);
targetElement.addEventListener('myCustomEvent', (event) => {
  console.log('Custom event received:', event.detail.message);
});
```

## Implement auto-retry promises

**Answer**

```javascript
function autoRetry(executeFunction, maxRetries = 3, retryDelay = 0) {
  return new Promise((resolve, reject) => {
    const tryExecution = () => {
      executeFunction()
        .then(resolve)
        .catch((error) => {
          if (maxRetries > 0) {
            maxRetries--;
            retryDelay ? setTimeout(tryExecution, retryDelay) : tryExecution();
          } else {
            reject(error);
          }
        });
    };
    tryExecution();
  });
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

Throttle promises by batching

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

Implement a function difference(array, values) that creates an array of array values not included in the other given arrays using SameValueZero for equality comparisons. The order and references of result values are determined by the first array.
The SameValueZero equality comparison is a method of comparing two values for equality. It is similar to the strict equality comparison (===), but with a few key differences. Specifically, SameValueZero considers NaN to be equal to NaN, whereas strict equality does not.

```javascript
function difference(array, values) {
  const result = [];
  for (let i = 0; i < array.length; i++) {
    const element = array[i];
    if (!values.includes(element)) {
      result.push(element);
    }
  }
  return result;
}
```

## Is `i` visible outside the `setTimeout` callback?

**Answer**

setTimeout(function() {
    for(var i=0; i<10;i++) {
    }
 });
 console.log("i======", i)

ReferenceError: i is not defined

## What does the IIFE print when `var a` is hoisted?

**Answer**

```javascript
(function() {
  console.log(a);
  var a = 10;
  console.log(a);
})();
```

undefined
10

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

Set(3) {1, 2, 3}

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

 Implement Memorization to handle data types like strings, numbers, arrays, and objects.

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

## Write a function that ensures a maximum of maxLimit concurrent asynchronous operations while processing an array of inputs and calling a final callback with all outputs.

**Answer**

```javascript
function mapLimit(inputs, maxLimit, asyncFn, finalCallback) {
  const results = [];
  let inFlight = 0;
  let index = 0;
  function processNext() {
    if (index >= inputs.length && inFlight === 0) {
      return finalCallback(results); // All tasks are completed.
    }
    if (inFlight < maxLimit && index < inputs.length) {
      const currentIndex = index++;
      inFlight++;
      asyncFn(inputs[currentIndex], (err, result) => {
        results[currentIndex] = err ? { error: err } : result;
        inFlight--;
        processNext(); // Launch the next task.
      });
      processNext(); // Continue launching tasks until the limit is reached.
    }
  }
  processNext(); // Start processing.
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
