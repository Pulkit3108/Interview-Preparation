# Angular

Angular and TypeScript fundamentals, components, templates, dependency injection, routing, forms, RxJS, and testing.

[Back to the question-bank index](../README.md)

## What is the difference between TypeScript and JavaScript?

**Answer**

Typing:
JavaScript: Dynamically typed.
TypeScript: Statically typed (optional).
Compilation:
JavaScript: Interpreted directly by the browser or Node.js.
TypeScript: Compiled to JavaScript before execution.
Inheritance:
JavaScript: Prototype-based inheritance.
TypeScript: Class-based inheritance.
Interfaces:
JavaScript: No built-in support for interfaces.
TypeScript: Supports interfaces for defining contracts.
Development Experience:
JavaScript: Provides basic development experience with dynamic typing.
TypeScript: Enhances development experience with static typing, better tooling, and advanced type features.

## What is Type Checking and Type Definitions?

**Answer**

Type Checking: TypeScript performs static type checking at compile time to ensure that variables, function parameters, return values, and other expressions have the correct types.
Type Definitions: TypeScript provides several ways to define types, including basic types, interfaces, and type aliases.
Type Checking and Type Definitions in Angular: Angular leverages TypeScript's type system to ensure the correctness and consistency of the code in components, services, and other constructs.

## What are the advantages and disadvantages of using Angular?

**Answer**

Advantages:
Two-Way Data Binding
Component-Based Architecture
Dependency Injection
Comprehensive Framework
TypeScript Support
Reactive Programming with RxJS
Strong Community and Ecosystem
Performance Optimization
Disadvantages:
Steep Learning Curve
Verbose and Complex Code
Performance Overhead
Frequent Updates and Breaking Changes
Opinionated Framework
Heavy Framework

## What is a Single Page Application?

**Answer**

A single-page application is a web application or website that interacts with the user by dynamically rewriting the current web page with new data from the web server, instead of the default method of loading entire new pages. The goal is faster transitions that make the website feel more like a native app

## What are modules, services, and components?

**Answer**

Modules are containers that group together related components, directives, pipes, and services. It organizes the application into cohesive blocks which helps to structure the data.
Services are singleton objects that encapsulate business logic, data access, or other reusable functionalities. It is used for loading data and communicating it.
Components are the building blocks of an Angular application. They control a part of the user interface. It defines the UI interaction and behavior of a part of the application.

## What are JIT and AOT compilation in Angular, and how are current Angular applications built?

**Answer**

- **JIT (Just-in-Time):** compiles templates while the application runs. It is mainly associated
  with development workflows.
- **AOT (Ahead-of-Time):** compiles templates during the build. Current Angular CLI production
  builds use AOT by default.
- `ng serve` runs the development server.
- `ng build` creates a production build by default in current Angular CLI projects.
- `ng build --configuration staging` selects a named configuration from `angular.json`.

Modern Angular applications use the application builder, based on esbuild, for client bundles and
optional prerendering or server-side rendering. Older commands such as `ng build --prod`,
`ng eject`, and `@nguniversal/express-engine` describe previous CLI generations and should not be
presented as current defaults. Current SSR support uses the `@angular/ssr` package and the
application builder.

**Further reading**

- [Angular application build system](https://angular.dev/tools/cli/build-system-migration)
- [Building Angular applications](https://angular.dev/tools/cli/build)
- [Angular CLI build command](https://angular.dev/cli/build)

## What is Angular CLI used for?

**Answer**

The Angular CLI (Command Line Interface) is a powerful tool that helps developers efficiently create, manage, and build Angular applications. It provides a set of commands for various tasks, streamlining the development workflow and ensuring best practices are followed

## What happens when you build your Angular code?

**Answer**

Compilation:
TypeScript Compilation: Transpiles TypeScript to JavaScript and performs type checking.
Angular Template Compilation: Compiles Angular templates into JavaScript (AOT compilation).
Bundling:
Module Bundling: Combines all JavaScript files into a few optimized bundles.
Optimization:
Minification: Reduces file size by removing whitespace and shortening variable names.
Tree Shaking: Removes unused code from the final bundle.
Ahead-of-Time (AOT) Compilation: Pre-compiles Angular templates and components.
Asset Optimization:
CSS and HTML Optimization: Minifies and concatenates CSS and HTML files.
Image Optimization: Compresses images to reduce file size.
Output Generation:
Distribution Directory: Places the final build artifacts in the dist/ directory.
Configuration and Environment Handling:
Environment Configuration: Applies environment-specific configurations.

## What are different data bindings in Angular?

**Answer**

Interpolation: {{ expression }} - Component to template.
Property Binding: [property]="expression" - Component to element property.
Attribute Binding: [attr.attributeName]="expression" - Component to element attribute.
Class Binding: [class.className]="expression" - Adds/removes class.
Style Binding: [style.styleProperty]="expression" - Sets style property.
Event Binding: (event)="handler" - Template to component method.
Two-way Binding: [(ngModel)]="property" - Two-way data binding.

## What is the Angular import for Component and Input?

**Answer**

```typescript
import { Component, Input } from '@angular/core';
```

## How will you pass data from parent to child component in Angular?

**Answer**

In Angular, you can pass data from a parent component to a child component using property binding and the @Input decorator.

## Can we Share data from parent to child like 2 way binding?

**Answer**

Sharing data from a parent component to a child component in Angular is typically done using one-way data binding, not two-way binding. This is achieved using @Input properties in the child component. Two-way binding, on the other hand, is used for synchronizing data between the view and the component.

## What are different ways to share data between 2 components?

**Answer**

Parent to Child using @Input: Pass data from parent to child.
Child to Parent using @Output and EventEmitter: Pass data from child to parent.
Using a Shared Service: Share data between components using a service.
Using Local Storage or Session Storage: Store and retrieve data in the browser's storage.
Using Angular Router with Route Parameters: Pass data through route parameters during navigation.

## What are different ways to share data between sibling components?

**Answer**

Using a Shared Service:
Create a service to hold shared data and provide methods to get and set the data.
Inject the service into sibling components to share data.
Using a Parent Component:
Use a parent component to hold shared data and pass it to sibling components via input properties and event emitters.
Using a State Management Library:
Use libraries like NgRx or Akita to manage and share state across the application, including between sibling components.

## Explain a bit about each Angular lifecycle hook.

**Answer**

Angular lifecycle hooks are methods that provide visibility into key moments in the lifecycle of a component or directive. Here are brief definitions:
ngOnChanges: Called when an input property value changes.
ngOnInit: Called once after the first ngOnChanges, when component is initialized.
ngDoCheck: Called during every change detection run.
ngAfterContentInit: Called once after content (ng-content) has been projected into the view.
ngAfterContentChecked: Called after every check of projected content.
ngAfterViewInit: Called once after the component's view and child views have been initialized.
ngAfterViewChecked: Called after every check of the component's view and child views.
ngOnDestroy: Called just before the component is destroyed.

## What are some common uses of ngOnInit?

**Answer**

Fetching Data: Retrieve data from services or APIs.
Initializing Component State: Set initial values for component properties.
Subscribing to Observables: Handle data streams.
Setting Up Event Listeners: Initialize event listeners.
Dependency Injection Initialization: Initialize services or other dependencies.

## Which Lifecycle Hook to use to fetch DOM Element?

**Answer**

Lifecycle Hook: Use ngAfterViewInit to fetch or interact with DOM elements after the component's view has been fully initialized.
Steps:
Import AfterViewInit, ViewChild, and ElementRef from @angular/core.
Use the @ViewChild decorator to get a reference to the DOM element.
Implement the ngAfterViewInit method to perform DOM manipulations.

## Which Lifecycle hook to use when sending value from parent to child?

**Answer**

Lifecycle Hook: Use ngOnChanges to capture changes to input properties and access both the previous and current values.
Steps:
Import OnChanges and SimpleChanges from @angular/core.
Implement the ngOnChanges method to capture the previous and current values of the input property.

## What is ViewChild?

**Answer**

@ViewChild: A decorator that allows you to access a child component, directive, or DOM element from a parent component.
Access Child Components: Use @ViewChild to access public properties and methods of a child component.
Access DOM Elements: Use @ViewChild to access native DOM elements directly.
Access Directives: Use @ViewChild to access directives applied to elements.
Lifecycle Hook: Use ngAfterViewInit to ensure the child component or DOM element is fully initialized before accessing it.

## What is a Dynamic Component?

**Answer**

Dynamic Component: A component that is created and inserted into the DOM at runtime.
Key Services:
ComponentFactoryResolver: Used to create a component factory for a given component type.
ViewContainerRef: Used to insert the dynamically created component into the DOM.
Steps:
Create the dynamic component.
Create a host component with a container for the dynamic component.
Use ComponentFactoryResolver and ViewContainerRef to create and insert the dynamic component.

## What is ViewContainerRef?

**Answer**

ViewContainerRef: A service that provides a way to interact with the view container of a component.
Key Methods:
createComponent: Creates and inserts a component into the view container.
createEmbeddedView: Creates and inserts an embedded view from a TemplateRef.
clear: Clears all views from the container.
remove: Removes a view from the container at a specified index.
insert: Inserts a view into the container at a specified index.
detach: Detaches a view from the container without destroying it.

## What is the concept of dependency injection?

**Answer**

Dependency Injection (DI) in Angular: A design pattern that allows you to inject dependencies into components, services, and other parts of the application.
Providers: Define how to create an instance of a dependency.
Injectors: Responsible for creating and managing instances of dependencies.
Tokens: Identifiers used to look up dependencies in the injector.
Hierarchical Injectors: Angular uses a hierarchical injector system, allowing services to be provided at different levels (root, component, etc.).

## How to implement Dependency Injection in Angular?

**Answer**

Create a Service: Define a service using the @Injectable decorator.
Inject the Service into a Component: Use Angular's DI system to inject the service into a component's constructor.
Register the Service with an Injector: Use the providedIn property in the @Injectable decorator or the providers array in a module.

## What is Angular Routing and How to use it?

**Answer**

Angular Routing enables navigation between different views in your single-page application (SPA). It allows users to move seamlessly between different parts of your app without full page reloads, providing a smooth user experience.
Steps to Use:
- Create an array of routes in your app's routing module:
- Add the RouterOutlet.
- Use the routerLink directive to create links in your templates

## What is Auth Guard in Angular?

**Answer**

In Angular, an Auth Guard is a feature that helps you protect certain routes in your application from unauthorized access. It acts as a gatekeeper, checking whether a user is authenticated before allowing them to navigate to a protected route.

## What are different types of guard in Angular?

**Answer**

CanActivate: Determines if a route can be activated. Used for authentication and authorization checks.
CanActivateChild: Determines if child routes can be activated. Used for protecting nested routes.
CanDeactivate: Determines if a route can be deactivated. Used to prevent users from leaving a route if certain conditions are not met.
CanLoad: Determines if a module can be loaded. Used for authentication and authorization checks for lazy-loaded modules.
Resolve: Pre-fetches data before activating a route. Used to ensure necessary data is available before the route is activated.

## What are custom pipes in Angular?

**Answer**

In Angular, custom pipes are a way to transform data directly in your templates. They are essentially functions that take an input value and return a transformed output

## How do you create custom pipes?

**Answer**

Generate the Pipe: Use Angular CLI to generate a new pipe.
ng generate pipe custom
Implement the Pipe: Define the transformation logic in the pipe class.
Register the Pipe: Ensure the pipe is declared in an Angular module.
Use the Pipe: Apply the custom pipe in your templates.
Import Required Modules: Import Pipe and PipeTransform from @angular/core.
Decorator: Use the @Pipe decorator to define the name of the pipe (titleCase).
Implement PipeTransform: Implement the PipeTransform interface by defining the transform method.

## What is the difference between ngIf and ngSwitch?

**Answer**

Use ngIf for simple true/false conditions and ngSwitch when you need to choose between multiple options.

## How do we implement form validation in Angular?

**Answer**

Validation in Template: You add validation rules directly within the HTML template using built-in directives like required, minlength, maxlength, pattern, etc.
Validation in Component: You define validation logic within your component class using the Validators class and its built-in validators or by creating custom validators.

## What are Angular directives?

**Answer**

Angular directives are special markers in the DOM that tell Angular to do something to a DOM element or even to the entire DOM structure. They are used to extend the HTML by adding new behavior to elements and components. There are three main types of directives in Angular:
Component Directives:
These are the most common directives and are used to create components. Components are directives with a template.
Example: <app-my-component></app-my-component>
Structural Directives:
These directives change the DOM layout by adding or removing elements. They typically use the asterisk (*) prefix.
Examples: *ngIf, *ngFor, *ngSwitch
Attribute Directives:
These directives change the appearance or behavior of an element, component, or another directive.
Examples: ngClass, ngStyle, ngModel

## Which Angular feature allows you to define custom HTML elements and attributes?

**Answer**

In Angular, Directives are the feature that allows you to define custom HTML elements and attributes. Directives are a core feature of Angular and are used to extend the capabilities of HTML by adding new behavior to elements and components.

## What are custom directives in Angular

**Answer**

Custom directives in Angular are a way to extend the HTML vocabulary and create reusable components or behaviors that can be applied to DOM elements.
Generate the Directive:
The ng generate directive Unless command creates a new directive called UnlessDirective.
Implement the Directive:
The @Directive decorator is used to define the directive.
The @Input decorator allows the directive to accept an input value (condition).
The TemplateRef and ViewContainerRef are used to manage the template and view container.
The appUnless setter method conditionally includes or removes the element from the DOM based on the condition.
Use the Directive in a Component:
The appUnless directive is applied to a <div> element, and the condition is toggled using a button.
Component Logic:
The AppComponent class defines the condition property and toggles it using a button click.

## How to Create Custom Directive

**Answer**

Generate the Directive: Use the Angular CLI to generate a new directive.
ng generate directive custom
Implement the Directive Logic: Define the behavior of the directive using the @Directive decorator and necessary methods.
Register the Directive in a Module: Add the custom directive to the declarations array in the module file.
Use the Custom Directive in a Template: Apply the custom directive in a component template.

## What is View encapsulation?

**Answer**

View encapsulation in Angular is a mechanism that determines how styles defined in a component affect the component's template and its children. It helps to scope styles to a specific component, preventing them from leaking out and affecting other parts of the application. Angular provides three types of view encapsulation:
Emulated (Default): Emulates Shadow DOM behavior by adding unique attribute selectors to elements and styles, scoping styles to the component.
None: No encapsulation; styles are global and can affect any element in the application.
Shadow DOM: Uses the native Shadow DOM to provide true encapsulation, ensuring styles are scoped to the component and do not leak out.

## What is content projection?

**Answer**

Content Projection: Allows you to insert content from a parent component into a child component.
ng-content Directive: Used in the child component's template to define where the projected content should be inserted.
Single Slot Content Projection: Projects content into a single slot.
Multi-Slot Content Projection: Projects content into multiple slots using selectors.

## What is Change detection in Angular?

**Answer**

Change detection in Angular is the mechanism by which the framework checks for changes in the application state and updates the DOM accordingly. Angular provides different strategies to optimize and control this process, ensuring that the application remains performant and responsive.
Default (CheckAlways): Angular checks the entire component tree for changes on every event. Suitable for most applications.
OnPush: Angular only checks the component and its children for changes when specific conditions are met. Suitable for performance optimization in large applications.
Manually Triggering Change Detection: Use ChangeDetectorRef to manually trigger change detection when using the OnPush strategy.

## What is an Observable in Angular? How do you subscribe to an Observable?

**Answer**

Observable is a lazy collection of future events. It is a data stream that can emit multiple values over time. Observers can subscribe to observables to receive emitted values. Observables are unicast by default, meaning each subscription has its own independent execution. It is a powerful tool for handling asynchronous data streams.  It's part of the RxJS library and provides a way to work with data that arrives over time, such as HTTP responses, user input events, and more
You can subscribe to an Observable by calling the subscribe() method.

## What is a Subject in Angular?

**Answer**

Subject is a special type of observable that allows values to be multicasted to multiple observers. Subjects are both an observable and an observer, meaning they can emit values and be subscribed to. It can be used to manually control the emission of values.
Types:
BehaviorSubject: A subject that requires an initial value and emits its current value (last emitted item) to new subscribers. Useful for representing "current state" that can change over time
ReplaySubject: A subject that stores a specified number of previous values and emits them to new subscribers. Useful for caching values and replaying them to new subscribers.
AsyncSubject: A subject that emits the last value to its subscribers when the subject completes. Useful for representing a single value that will be available in the future.

## What is the Difference between Subject and Behavior subject

**Answer**

Initial Value:
Subject: Does not have an initial value.
BehaviorSubject: Requires an initial value.
Replay Last Value:
Subject: Does not replay the last emitted value to new subscribers.
BehaviorSubject: Replays the last emitted value to new subscribers.
Use Case:
Subject: Use when you do not need to replay the last emitted value to new subscribers.
BehaviorSubject: Use when you need to ensure that new subscribers receive the most recent value immediately upon subscription.

## What is the difference between a promise and an observable?

**Answer**

Promises
Eager Execution: A Promise starts executing immediately when it is created.
Single Value: A Promise resolves or rejects with a single value or error.
Not Cancellable: Once a Promise is initiated, it cannot be cancelled.
Chaining: Promises use .then(), .catch(), and .finally() for chaining and handling results.
Built-in: Promises are a built-in feature of JavaScript (ES6).
Observables
Lazy Execution: An Observable does not start emitting values until it is subscribed to.
Multiple Values: An Observable can emit multiple values over time.
Cancellable: Subscriptions to Observables can be cancelled using the unsubscribe() method.
Operators: Observables use a wide range of operators for transforming, filtering, and combining streams.
Library Support: Observables are not built into JavaScript but are provided by libraries like RxJS.

## What are streams in observables?

**Answer**

In the context of Observables, streams represent a sequence of ongoing events ordered in time. Observables are a part of Reactive Programming and are used extensively in libraries like RxJS (Reactive Extensions for JavaScript).
Key Concepts of Streams in Observables:
Observable: Represents the stream itself, which can emit multiple values over time.
Observer: Consumes the values emitted by the Observable. It defines how to handle each value, errors, and completion.
Subscription: Represents the execution of an Observable. It allows you to start and stop listening to the stream.
Operators: Functions that enable complex asynchronous code by composing Observables together.

## How do you perform asynchronous operations in Angular?

**Answer**

Observables: Used extensively in Angular for handling asynchronous operations, especially with HTTPClient. They provide powerful operators for managing data streams.
Promises: Used for operations that return a single value or complete once. Can be converted from Observables using .toPromise().
async and await: Provide a more synchronous-looking way to handle Promises, making the code easier to read and write.
HttpClientModule: Import HttpClientModule in your app module to use HttpClient for making HTTP requests.
HttpClient: Use HttpClient in a service to perform HTTP operations such as GET, POST, PUT, DELETE.

## How will you integrate Backend APIs in Angular?

**Answer**

Set Up HttpClientModule:
Import HttpClientModule in your app module to use HttpClient for making HTTP requests.
Create a Service:
Generate a service and use HttpClient to perform HTTP operations like GET, POST, PUT, and DELETE.
Use the Service in a Component:
Inject the service into a component and use it to make HTTP requests to the backend API.

## What are different loading strategies in Angular?

**Answer**

Eager Loading: Loads all modules upfront when the application starts. Suitable for small applications or critical modules.
Lazy Loading: Delays loading of feature modules until they are needed. Ideal for large applications to improve initial load time.
Preloading: Loads lazy-loaded modules in the background after the initial load. Balances initial load time and subsequent navigation speed.
PreloadAllModules: Preloads all lazy-loaded modules.
Custom Preloading Strategy: Allows selective preloading based on custom logic.

## How to implement lazy loading in Angular?

**Answer**

To implement lazy loading in Angular, follow these steps:
Create a Feature Module: Generate a new module for the feature you want to lazy load.
Configure Routes: Set up the routes to load the feature module lazily.
Update App Routing Module: Use the loadChildren property to lazy load the module.

## How will you optimize and improve the performance of an Angular Application?

**Answer**

Lazy loading: It is a technique that allows you to load only the components that are needed at a given time. This can help to improve performance by reducing the size of the initial bundle that is downloaded by the browser.
To use lazy loading, you need to create a separate module for each lazy-loaded component. Then, you can use the router to load the module when the component is needed.
AOT compilation: It is a technique that allows Angular to compile the application code ahead of time. This can help to improve performance by reducing the amount of work that needs to be done by the browser when the application is loaded.
Avoid using ngIf with complex expressions: Instead of using a complex ngIf expression, use ngSwitch for better performance.
OnPush change detection strategy Angular uses change detection to track the changes to the application state. However, if change detection is used too often, this can lead to performance problems. To improve performance, you can use the OnPush change detection strategy. This strategy only checks for changes when the application state is explicitly changed.
Use trackBy in ngFor loops: The ngFor directive is used to iterate over a collection of data and render a template for each item. However, if the collection is large, this can lead to performance problems. To improve performance, you can use the trackBy property to track the changes to the collection. This will prevent Angular from re-rendering the entire template for each item in the collection.

## How will you load a large amount of data on a Web Application?

**Answer**

Pagination: Load data in smaller chunks with pagination controls.
Infinite Scrolling: Load data as the user scrolls down the page.
Virtual Scrolling: Render only the visible items in the viewport.
Lazy Loading: Load data or modules only when needed.
Server-Side Rendering (SSR): Render the initial view on the server for faster initial load times.

## Where would you call an API that needs to be called once and it will store data that will be used across different modules in Angular?

**Answer**

In Angular, if you need to call an API once and store the data for use across different modules, the best place to do this is in a service. Services in Angular are singleton by default when provided in the root injector, making them ideal for sharing data across the application.

## How will you implement Authorization in Angular?

**Answer**

Set Up Authentication: Create an authentication service to handle login, logout, and token management.
Protect Routes with Guards: Use route guards to protect routes and ensure only authenticated users can access certain parts of the application.
Manage User Roles and Permissions: Decode the JWT token to manage user roles and implement role-based authorization using custom guards.

## What are some of the new features in Angular 16?

**Answer**

Signal-Based Reactivity: Introduces a new reactivity model for more efficient change detection.
Standalone Components: Allows components, directives, and pipes to be created without NgModules.
Improved Server-Side Rendering (SSR): Enhances Angular Universal for better performance and easier setup.
Hydration: Supports reusing server-rendered HTML on the client side for improved SSR performance.
Enhanced Dependency Injection: Brings more flexibility and better error messages to the DI system.
Improved Error Handling: Provides more informative error messages and stack traces for easier debugging.
Performance Improvements: Includes optimizations for faster compilation, better change detection, and memory management.
Updated Angular CLI: Adds new features and improvements, including support for standalone components and better build performance.
TypeScript 4.9 Support: Integrates the latest TypeScript features and improvements into Angular applications.
Improved Forms: Enhances the forms module with better type safety, validation, and flexible form controls.

## What are some of the new features in Angular 18?

**Answer**

Zoneless Change Detection with Signals: Introduces a more efficient change detection mechanism using signals, eliminating the need for Zone.js.
Function-based Route Redirects: Allows dynamic and flexible route redirection using functions based on application conditions.
Improved Developer Tooling: Enhances Angular DevTools for better insights into performance, dependency management, and state changes.
Enhanced Angular Material and CDK: Updates Angular Material and CDK for full compatibility and optimization with Angular 18.
Server-Side Rendering (SSR) Enhancements: Improves SSR with event replay for a smoother user experience mimicking client-side behavior.
Improved Internationalization (i18n) Support: Introduces the @angular/localize package for easier management of translations and locale-specific formatting.
TypeScript 5.4 Support: Fully supports TypeScript 5.4, allowing the use of its latest features and improvements.
Additional Features:
Default Content in ng-content: Allows fallback content in ng-content projection when no projected content is available.
Improved Build Performance: Optimizes the build process for faster build times.
WebAssembly Support: Introduces developer preview support for WebAssembly, opening new performance optimization possibilities.

## How would you deploy an Angular Application

**Answer**

Build the Application for Production:
Use the Angular CLI to build the application for production.
Choose a Hosting Provider:
Select a hosting provider such as Firebase Hosting, Netlify, GitHub Pages, Amazon S3 and CloudFront, Heroku, or Azure Static Web Apps.
Deploy the Application:
Follow the specific steps for your chosen hosting provider to deploy the built files.

## What are signals in Angular?

**Answer**

Angular Signals in Angular 16 provide a powerful new way to manage state and optimize rendering updates in your application. By tracking state usage at a granular level, Signals help improve performance and make state management more intuitive.

## How would you do state management in Angular?

**Answer**

State management in Angular involves managing the state of your application in a way that makes it easy to maintain, test, and scale
Using Services: Simple and suitable for small to medium-sized applications.
Using NgRx: Powerful state management library that implements the Redux pattern.
Using Akita: Simple and scalable state management library.
Using NGXS: Inspired by the Redux pattern but aims to be simpler and more intuitive.

## Can we use angular signal in place of Input decorator?

**Answer**

@Input Decorator: Used for passing data from a parent component to a child component.
Signals: Used for managing local state within a component or service, providing a reactive way to trigger change detection.
Combination: While signals are not a direct replacement for @Input, they can be used together to manage state and pass data between components.

## What is Angular Gauge?

**Answer**

An Angular Gauge is a type of data visualization component that represents data in a circular or semi-circular format, similar to a speedometer or a dial. It is commonly used to display a single value within a range, providing a quick visual representation of performance metrics, progress, or other key indicators.

## How will you create a reactive form for login in Angular?

**Answer**

Set Up Angular Project: Ensure you have an Angular project set up. If not, create a new Angular project using the Angular CLI.
Import ReactiveFormsModule: Import ReactiveFormsModule in your Angular module (e.g., app.module.ts).
Create a Login Component: Generate a new component for the login form using the Angular CLI.
Define the Form Model: In the login component, define the form model using FormBuilder and FormGroup.
Create the Form Template: In the login component's template, create the form using Angular's reactive form directives (formGroup, formControlName).
Add Form Controls: Add form controls for the username and password fields in the form model.
Add Validation: Add validation rules to the form controls (e.g., required, minLength, maxLength).
Handle Form Submission: Implement a method to handle form submission and process the form data.
Display Validation Messages: Add logic in the template to display validation messages based on the form control's state.
Style the Form: Optionally, add CSS styles to make the form look presentable.

## What are some common testing frameworks in Angular?

**Answer**

Current Angular CLI projects use **Vitest** as the default unit-test runner, with `jsdom` providing a
browser-like DOM in Node.js. **Karma** remains supported for older projects, often together with
Jasmine. Angular's `TestBed` and `ComponentFixture` provide framework-specific utilities for testing
components, directives, pipes, and services.

For end-to-end tests, choose a browser automation tool such as Playwright, Cypress, WebdriverIO,
Nightwatch, or Puppeteer based on the team's browser coverage and debugging needs. Protractor is
discontinued and should be treated as legacy rather than selected for a new project.

Reference: [Angular testing overview](https://angular.dev/guide/testing) and
[Angular end-to-end testing](https://angular.dev/tools/cli/end-to-end).

## How will you mock the function in Jest framework

**Answer**

Using jest.fn(): Create a new, unused mock function.
Using jest.mock(): Automatically mock a module.
Using jest.spyOn(): Create a mock function that spies on a method of an object.
Using Manual Mocks: Create manual mocks in a __mocks__ directory.

## How can you add support for human languages in Angular?

**Answer**

Use Angular's localization support to mark translatable template text, extract source messages, and
build or serve a locale-specific version. Keep translations in files such as XLIFF, configure the
supported locales in `angular.json`, and use locale-aware pipes for dates, numbers, currencies, and
plurals. For an application that must change language without reloading, evaluate a runtime
translation library and define fallback, missing-key, and lazy-loading behavior explicitly.

Reference: [Angular internationalization](https://angular.dev/guide/i18n).

## How will you go about implementing a File Upload Functionality?

**Answer**

File Serialization and Deserialization:
Consideration: Ensure that the file data is correctly serialized when sending to the server and deserialized when received.
Implementation: Use FormData to serialize file data for transmission via HTTP requests.
Handling Disconnections:
Consideration: Implement mechanisms to handle user disconnections during file uploads.
Implementation: Use resumable uploads with libraries like tus-js-client or implement chunked uploads where the file is divided into smaller parts and uploaded sequentially. If a disconnection occurs, only the remaining chunks need to be uploaded.
Supported File Formats:
Consideration: Define and enforce the types of files that can be uploaded.
Implementation: Use input attributes like accept to restrict file types on the client side and validate file types on the server side.
File Size Limits:
Consideration: Set a maximum file size limit to prevent excessively large uploads that could impact server performance and storage.
Implementation: Check each browser `File.size` value before upload and enforce the limit again on
the server. The HTML file input has no `max` attribute for file size.
Multiple File Uploads:
Consideration: Allow users to upload multiple files simultaneously.
Implementation: Use the multiple attribute on the file input element and handle multiple files in the upload logic.
User Feedback:
Consideration: Provide feedback to users during the upload process, such as progress indicators and success/error messages.
Implementation: Use progress events to update the UI with the upload status.
User Authentication and Authorization:
Consideration: Ensure that only authenticated and authorized users can upload files.
Implementation: Use authentication mechanisms (e.g., JWT, OAuth) and enforce authorization rules on the server side.
Cross-Browser Compatibility:
Consideration: Ensure that the file upload functionality works across different browsers and devices.
Implementation: Test the file upload feature on various browsers and devices, and use polyfills or fallbacks if necessary.

## What will happen when this component is rendered?

**Answer**

```typescript
@Component({
  selector: 'app-observable',
  template: `
    <div *ngIf="data$ | async as data; else loading">
      {{ data }}
    </div>
    <ng-template #loading>Loading...</ng-template>
  `
})
export class ObservableComponent {
  data$: Observable<string>;
  constructor() {
    this.data$ = new Observable<string>((observer) => {
      setTimeout(() => {
        observer.next('Data loaded');
        observer.complete();
      }, 2000);
    });
  }
}
```

The `async` pipe subscribes during rendering. Until the observable emits, `data` is falsy and the
`loading` template displays. About two seconds later, the observable emits `Data loaded`; Angular
updates the view with that text. The observable then completes, and the `async` pipe handles
subscription cleanup automatically.

## How will you create a custom directive in which on hover you need to change the color of the button.?

**Answer**

```typescript
@Directive({
  selector: '[appHoverColor]'
})
export class HoverColorDirective {
  @Input('appHoverColor') hoverColor: string;
  constructor(private el: ElementRef, private renderer: Renderer2) {}
  @HostListener('mouseenter') onMouseEnter() {
    this.changeColor(this.hoverColor || 'blue');
  }
  @HostListener('mouseleave') onMouseLeave() {
    this.changeColor(null);
  }
  private changeColor(color: string) {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', color);
  }
}
```

Use the directive in a template:

```html
<button appHoverColor="green">
  Hover over this button to change its color.
</button>
```
