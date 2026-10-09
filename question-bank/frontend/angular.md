# Angular

Angular and TypeScript fundamentals, components, templates, dependency injection, routing, forms, RxJS, and testing.

[Back to the question-bank index](../README.md)

## What is the difference between TypeScript and JavaScript?

**Answer**

JavaScript is a dynamically typed runtime language. TypeScript is a superset of JavaScript that adds
an erasable, structural static type system and must be transpiled to JavaScript before it runs.

TypeScript adds interfaces, type aliases, generics, unions, and compile-time checking, which improves
editor tooling and catches many mistakes before execution. Its types do not validate untrusted data
at runtime, and both languages ultimately use JavaScript's prototype-based object model.

## What is Type Checking and Type Definitions?

**Answer**

Type checking verifies at compile time that expressions are compatible with their declared or
inferred types. A type definition describes a value's shape using primitives, interfaces, type
aliases, classes, generics, unions, and related constructs. Declaration files (`.d.ts`) describe the
types exposed by JavaScript libraries without adding runtime code.

Angular's compiler extends this checking to templates when strict template checking is enabled.
Runtime validation is still required for API responses, storage, and other untrusted input.

## What are the advantages and disadvantages of using Angular?

**Answer**

Advantages include an integrated router, forms, HTTP client, dependency injection, testing support,
CLI, component model, TypeScript tooling, signals, and RxJS interoperability. The consistent,
opinionated structure can help large teams maintain applications.

Trade-offs include a broad API surface, framework-specific concepts, migration work between major
versions, and more initial structure than a small application may need. Performance depends on
bundle design, rendering behavior, and application code; calling Angular simply "heavy" is not a
useful diagnosis.

## What is a Single Page Application?

**Answer**

A single-page application loads an application shell and handles later navigation by updating the
current document rather than requesting a full HTML page for every route. It can provide smooth
transitions, but it still needs deliberate routing, history, accessibility, loading, error, caching,
SEO, and deep-link behavior. SSR or prerendering can complement an SPA for initial delivery.

## What are modules, services, and components?

**Answer**

- A **component** combines a template, behavior, and styles for part of the user interface.
- A **service** is an ordinary class used for reusable state or logic and is commonly obtained through
  dependency injection. It is a singleton only within the injector that provides it.
- An **NgModule** groups declarations and providers in module-based applications. Modern Angular
  components are standalone by default, so new applications can compose components and providers
  without application NgModules. NgModules remain supported for existing code and libraries.

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

The Angular CLI creates and updates workspaces, generates code, serves development builds, runs tests,
builds deployable artifacts, and applies supported migrations. Common commands include `ng new`,
`ng generate`, `ng serve`, `ng test`, `ng build`, and `ng update`.

## What happens when you build your Angular code?

**Answer**

The CLI selects a build configuration, compiles TypeScript and Angular templates, resolves imports,
processes styles and configured assets, and emits browser bundles. Production builds normally apply
AOT compilation, tree shaking, minification, hashing, and configured size budgets. SSR or prerendered
outputs are produced when those features are configured.

The output location and file replacements come from workspace configuration. A build does not
automatically optimize arbitrary images or guarantee that unused code with side effects disappears;
inspect the emitted bundles and budgets rather than assuming every optimization occurred.

## What are different data bindings in Angular?

**Answer**

- Interpolation: `{{ expression }}` renders a value as text.
- Property binding: `[property]="expression"` assigns a DOM, directive, or component property.
- Attribute binding: `[attr.name]="expression"` writes an HTML attribute.
- Class and style bindings: `[class.active]` and `[style.width.px]` update presentation.
- Event binding: `(event)="handler($event)"` invokes template logic.
- Two-way binding: `[(ngModel)]="value"` combines an input and matching change event. Component
  two-way binding can also be exposed with a model input.

## What is the Angular import for Component and Input?

**Answer**

Both symbols are exported by Angular's core package:

```typescript
import { Component, Input } from '@angular/core';
```

## How will you pass data from parent to child component in Angular?

**Answer**

Declare an input in the child, then bind it from the parent. Current Angular supports signal-based
`input()` declarations as well as the `@Input` decorator.

```typescript
// child
name = input.required<string>();
```

```html
<app-child [name]="selectedName" />
```

## Can we Share data from parent to child like 2 way binding?

**Answer**

Yes. Prefer one-way input binding plus an explicit output when that makes ownership clearer. For a
true component two-way binding, expose an input/output pair such as `value` and `valueChange`, or use
a model input and bind it with `[(value)]`. Two-way binding should not obscure which component owns
the state.

## What are different ways to share data between 2 components?

**Answer**

- Parent to child: an input property or signal input.
- Child to parent: an output event.
- Closely related components: lift state to their common parent.
- Unrelated components: an injected service using signals or RxJS; use a store when state complexity
  justifies one.
- Navigation state: route parameters, query parameters, resolver data, or history state.
- Persistent client state: storage only when persistence is required; do not treat browser storage as
  an event bus or store sensitive credentials there.

## What are different ways to share data between sibling components?

**Answer**

The simplest approach is to keep the state in the closest common parent, pass values down through
inputs, and receive changes through outputs. If the siblings do not share a practical parent, inject
a service scoped to the feature and expose controlled signal or observable state. Adopt a store such
as NgRx only when application-wide state, effects, traceability, or team conventions justify it.

## Explain a bit about each Angular lifecycle hook.

**Answer**

- `ngOnChanges`: runs when bound inputs change; the first call precedes `ngOnInit`.
- `ngOnInit`: runs once after Angular initializes the component's inputs.
- `ngDoCheck`: runs during checks and supports custom change detection; keep it lightweight.
- `ngAfterContentInit` / `ngAfterContentChecked`: run after projected content is initialized or
  checked.
- `ngAfterViewInit` / `ngAfterViewChecked`: run after the component view and view children are
  initialized or checked.
- `ngOnDestroy`: runs immediately before destruction and is used for cleanup.

`afterNextRender` and `afterEveryRender` schedule callbacks after Angular has rendered application
changes to the DOM. Avoid changing bound state inside the checked hooks because that can cause
expression-changed errors or repeated work.

## What are some common uses of ngOnInit?

**Answer**

Use `ngOnInit` for initialization that depends on resolved inputs or injected collaborators, such as
starting a data request or deriving initial component state. Prefer template `async`, signals, or
`takeUntilDestroyed` for subscriptions. Constructor injection already makes dependencies available;
`ngOnInit` does not perform dependency injection.

## Which Lifecycle Hook to use to fetch DOM Element?

**Answer**

Use a view query such as `viewChild()` or `@ViewChild`. For imperative work that requires the view to
exist, read it in `ngAfterViewInit`; for DOM work that must happen after rendering, use a render
callback such as `afterNextRender`. Prefer bindings and `Renderer2` over direct DOM mutation, and
guard browser-only DOM access in SSR applications.

## Which Lifecycle hook to use when sending value from parent to child?

**Answer**

No lifecycle hook is needed merely to receive a value: Angular assigns a bound input automatically.
Use `ngOnChanges` when code must react to decorated-input changes and needs previous/current values.
For signal inputs, derive state with `computed` or react with `effect` only when a side effect is
actually required.

## What is ViewChild?

**Answer**

`@ViewChild` is a view query that retrieves the first matching component, directive, provider, or
template/element reference from a component's own view. Dynamic queries update when the view changes;
static queries resolve before initialization and do not update. Current Angular also provides the
signal-based `viewChild()` API. A view query does not cross component boundaries.

## What is a Dynamic Component?

**Answer**

A dynamic component is selected and instantiated at runtime rather than appearing statically in a
template. Use `ViewContainerRef.createComponent(ComponentType)` to insert one at a known container,
or the standalone `createComponent` function for more controlled host-element creation. Configure
inputs, outputs, environment injector, and destruction explicitly. `ComponentFactoryResolver` is a
legacy approach and is unnecessary in current Angular.

## What is ViewContainerRef?

**Answer**

`ViewContainerRef` represents a location that can contain host views and embedded views. It can
create components, instantiate a `TemplateRef`, insert or move views, detach a view without
destroying it, remove a view, or clear the container. Angular includes attached views in rendering
and change detection.

## What is the concept of dependency injection?

**Answer**

Dependency injection separates a consumer from construction of its collaborators. A token identifies
a dependency, a provider explains how to create or obtain its value, and an injector resolves and
caches it according to provider scope. Angular's hierarchical injectors allow application-, route-,
and component-scoped instances. Resolution can use constructor parameters or `inject()` in an
injection context.

## How to implement Dependency Injection in Angular?

**Answer**

Define an injectable class or another provider, register it at the intended scope, and request its
token from the consumer. `providedIn: 'root'` provides one lazily created instance in the root
environment injector; component `providers` create scoped instances for that component subtree.

```typescript
@Injectable({ providedIn: 'root' })
export class UserService {}

@Component({ /* ... */ })
export class ProfileComponent {
  private readonly users = inject(UserService);
}
```

## What is Angular Routing and How to use it?

**Answer**

Angular Router maps URLs to component trees. Define a `Routes` array, register it with
`provideRouter(routes)` in a standalone application, place a `RouterOutlet` where activated content
should render, and navigate with `routerLink` or `Router`. Routes can lazy-load components, declare
children, resolve data, and run guards.

## What is Auth Guard in Angular?

**Answer**

A route guard can allow, reject, redirect, or conditionally match client-side navigation based on
authentication state or another condition. It improves navigation UX, but browser code is
modifiable and therefore cannot enforce authorization. Every protected API and resource must also
authorize the request on the server.

## What are different types of guard in Angular?

**Answer**

- `CanActivate`: controls activation of a route.
- `CanActivateChild`: controls activation of descendant routes.
- `CanDeactivate`: controls leaving the current route, often for unsaved changes.
- `CanMatch`: controls whether a route definition can match, including lazy routes.

A resolver loads data before activation but is not a guard. `CanLoad` appears in older Angular code;
current routing guidance uses `CanMatch` for route matching and lazy-loading decisions.

## What are custom pipes in Angular?

**Answer**

A custom pipe encapsulates a reusable template transformation. Pure pipes run again when a primitive
argument changes or an input object reference changes. Impure pipes run during every check and can be
expensive, so use them only when necessary. Pipes should not hide side effects or subscriptions.

## How do you create custom pipes?

**Answer**

Generate one with `ng generate pipe short-name`, implement `PipeTransform`, and import the standalone
pipe into each component that uses it. Module-based applications can declare and export it from an
NgModule.

```typescript
@Pipe({ name: 'initials' })
export class InitialsPipe implements PipeTransform {
  transform(value: string): string {
    return value.split(/\s+/).filter(Boolean).map(part => part[0]).join('');
  }
}
```

## What is the difference between ngIf and ngSwitch?

**Answer**

`NgIf` conditionally includes one branch; `NgSwitch` selects among multiple cases. In current Angular,
the built-in `@if` and `@switch` template blocks are preferred for new code and do not require
importing structural directives. Use an `if` for a binary or chained condition and a switch when one
expression is compared against several cases.

## How do we implement form validation in Angular?

**Answer**

Angular supports template-driven and reactive forms. Add synchronous or asynchronous validators to
controls, display messages after an appropriate interaction state such as `touched`, prevent invalid
submission, and test both valid and invalid paths. Browser validation improves UX; the server must
repeat all trust and business-rule validation.

## What are Angular directives?

**Answer**

Directives attach Angular behavior to host elements. A component is a directive with a template.
Attribute directives change an element's behavior or appearance, while structural directives create
or remove embedded views. Older structural-directive shorthand uses `*ngIf` and `*ngFor`; current
Angular also provides built-in control-flow blocks such as `@if` and `@for`.

## Which Angular feature allows you to define custom HTML elements and attributes?

**Answer**

Components define custom elements with templates. Attribute directives define custom attributes or
selectors that add behavior to an existing host. Angular Elements can package a component as a
standards-based custom element when interoperability outside Angular is required.

## What are custom directives in Angular

**Answer**

A custom directive packages reusable host behavior under a selector. An attribute directive can use
host bindings and listeners; a structural directive receives a `TemplateRef` and controls its
embedded views through `ViewContainerRef`. Define a clear input API and prefer renderer or host
bindings over direct DOM manipulation.

## How to Create Custom Directive

**Answer**

Run `ng generate directive custom`, define its selector and behavior with `@Directive`, then import the
standalone directive into the consuming component. In a module-based application, declare and export
it from an NgModule. The hover-color example at the end of this file shows a complete attribute
directive.

## What is View encapsulation?

**Answer**

View encapsulation controls how component styles are scoped:

- `Emulated`, the default, rewrites selectors with generated attributes. It scopes component rules
  but is not a real shadow root.
- `ShadowDom` uses the browser's native shadow DOM and its style boundary.
- `None` emits the styles globally.

Inherited CSS properties and custom properties can still cross relevant boundaries, so
encapsulation is not complete isolation of all visual state.

## What is content projection?

**Answer**

Content projection lets a component render content supplied by its consumer. The child places
`<ng-content>` slots in its template; slots with `select` support multi-slot projection. Projected
content retains the binding context of the component that declared it. It is different from creating
an embedded view from `TemplateRef`.

## What is Change detection in Angular?

**Answer**

Change detection evaluates bindings and updates the DOM when application state changes. The default
strategy checks a component whenever its view participates in a traversal. `OnPush` lets Angular skip
eligible subtrees until a trigger occurs, such as a new input value, an event in the subtree, an
observable notification consumed by `async`, a signal read by the template changing, or an explicit
mark. Mutating an object without changing its reference is a common `OnPush` bug.

## What is an Observable in Angular? How do you subscribe to an Observable?

**Answer**

An RxJS `Observable` describes a sequence of zero or more values followed by completion or an error.
Many observables are lazy and cold, but hot/multicast observables also exist, so neither property is
universal. Subscribe with the template `async` pipe when possible; otherwise call `subscribe` and
bind cleanup to component destruction, for example with `takeUntilDestroyed`.

## What is a Subject in Angular?

**Answer**

A `Subject` is both an observer and an observable, so code can push values with `next` and multicast
them to current subscribers. A plain `Subject` has no current value or replay. `BehaviorSubject`
requires an initial value and replays the latest value, `ReplaySubject` replays a configured buffer,
and `AsyncSubject` emits its final value only when it completes. Hide writable subjects behind a
read-only observable when exposing service state.

## What is the Difference between Subject and Behavior subject

**Answer**

A plain `Subject` emits only events that occur after subscription. A `BehaviorSubject` requires an
initial value, exposes the current value, and immediately emits that latest value to a new subscriber.
Use a plain subject for transient events and a behavior subject only when the stream genuinely models
current state.

## What is the difference between a promise and an observable?

**Answer**

A promise is a built-in JavaScript object that settles once with a value or error. Its executor starts
when the promise is created, and the promise itself has no standard cancellation operation.

An RxJS observable can emit multiple values and provides composition operators. Unsubscribing stops
that subscription and runs teardown logic, but it cancels underlying work only if the observable's
producer implements cancellation. Observables are often lazy, not universally so.

## What are streams in observables?

**Answer**

"Stream" informally means values or events delivered over time. The observable defines how values
are produced; an observer handles `next`, `error`, and `complete`; a subscription represents one
execution and its teardown; and operators create new observables by transforming or combining
sources. An observable need not be infinite or ongoing.

## How do you perform asynchronous operations in Angular?

**Answer**

Use RxJS observables for router events, forms, HTTP composition, and other streams; use promises and
`async`/`await` for single-result APIs when that model is clearer. Convert an observable with
`firstValueFrom` or `lastValueFrom` only when completion semantics are understood. `toPromise` was
removed from current RxJS.

Configure HTTP with `provideHttpClient`, inject `HttpClient`, and compose its returned observables.
Use template `async`, signals, or lifecycle-bound subscriptions so work and cleanup are explicit.

## How will you integrate Backend APIs in Angular?

**Answer**

Register `provideHttpClient`, usually in `app.config.ts`, and isolate endpoint details in a service
that injects `HttpClient`. Define response types, but remember a TypeScript generic does not validate
the server payload. Handle loading, empty, error, cancellation, retry, and caching behavior according
to the operation. Use interceptors for cross-cutting concerns, not hidden business logic, and enforce
authentication and authorization on the server.

## What are different loading strategies in Angular?

**Answer**

- **Eager loading** includes code in the initial route's dependency graph.
- **Lazy loading** downloads a route's component or children when navigation needs them.
- **Preloading** fetches selected lazy routes after initial navigation to reduce later latency;
  `PreloadAllModules` and custom strategies are available.
- **Deferred template loading** with `@defer` splits eligible template dependencies and loads them on
  triggers such as viewport or interaction.

## How to implement lazy loading in Angular?

**Answer**

Use `loadComponent` for a standalone component or `loadChildren` for child routes:

```typescript
export const routes: Routes = [
  {
    path: 'admin',
    loadComponent: () => import('./admin/admin.component')
      .then(module => module.AdminComponent),
  },
];
```

Confirm the feature becomes a separate chunk and avoid importing it eagerly elsewhere.

## How will you optimize and improve the performance of an Angular Application?

**Answer**

Measure first with browser performance tools, Angular DevTools, bundle budgets, and real-user
metrics. Common improvements include route lazy loading and `@defer`, stable tracking keys in
`@for`/`trackBy`, list virtualization, `OnPush` plus immutable state, avoiding repeated template work,
canceling obsolete requests, caching deliberately, and reducing third-party JavaScript. Use SSR or
prerendering when it improves initial delivery. Re-measure after each change; replacing a complex
`ngIf` with `ngSwitch` is not a general performance rule.

## How will you load a large amount of data on a Web Application?

**Answer**

Fetch bounded pages or cursor-based chunks from the server, cancel obsolete requests, and render long
lists with virtualization. Infinite scrolling still needs stable ordering, deduplication, loading and
error states, accessibility, and a way to recover position. Filtering, sorting, and aggregation
should usually happen server-side. SSR can improve initial HTML delivery but does not replace data
pagination.

## Where would you call an API that needs to be called once and it will store data that will be used across different modules in Angular?

**Answer**

Use a root- or feature-scoped service and expose cached signal or observable state. Ensure concurrent
callers share one in-flight request, define refresh and invalidation rules, and handle errors without
permanently caching a failed stream. A service is not inherently singleton; its provider scope
determines the instance lifetime.

## How will you implement Authorization in Angular?

**Answer**

Use an authentication service for session state, route guards for navigation UX, and an interceptor
only when it is appropriate to attach credentials or handle common responses. Render controls based
on capabilities, but never trust a decoded client token or hidden UI as authorization. The backend
must validate the credential and authorize every protected operation. Prefer secure, framework-
appropriate token storage and protect cookie sessions against CSRF.

## What are some of the new features in Angular 16?

**Answer**

Angular 16, released in 2023, introduced signals in developer preview, developer-preview hydration,
required inputs, `DestroyRef`, and `takeUntilDestroyed`. It also expanded the functional APIs for
dependency injection and guards and previewed an esbuild/Vite-based build path. Standalone
components were introduced earlier, in Angular 14, although Angular 16 continued their adoption.
Treat this as a historical release question rather than a description of current feature stability.

## What are some of the new features in Angular 18?

**Answer**

Angular 18, released in 2024, made built-in control flow and deferrable views stable. It introduced
experimental zoneless change detection, function-based route redirects, and developer-preview event
replay for hydration. It also supported fallback content in `ng-content` and TypeScript 5.4. It did
not simply eliminate Zone.js for every application, and `@angular/localize` predates Angular 18.

## How would you deploy an Angular Application

**Answer**

Choose the deployment model first: static client rendering, prerendering, or an SSR server. Run and
test the production build, enforce bundle budgets, publish the correct output directory, configure
TLS, caching and compression, and make the host fall back to `index.html` for client-side routes.
SSR needs a compatible runtime and health/observability setup. Keep runtime configuration and secrets
out of browser bundles, then smoke-test deep links and rollback behavior after deployment.

## What are signals in Angular?

**Answer**

A signal is a reactive value read by calling it. Writable signals update with `set` or `update`;
`computed` derives memoized state; and `effect` runs side effects when its dependencies change.
Angular tracks signal reads in templates so affected views can be scheduled for update. Signals are
useful for synchronous state, while RxJS remains useful for asynchronous event composition.

## How would you do state management in Angular?

**Answer**

Start by classifying state as local UI, shared feature, server cache, URL, or persisted state. Keep
local state in the component, lift shared state to the nearest owner, and use a scoped service with
signals or RxJS for a feature. Adopt a store such as NgRx when the application needs coordinated
effects, normalized shared state, replayable events, or strict conventions. Avoid duplicating server
state across unrelated stores without clear refresh and invalidation rules.

## Can we use angular signal in place of Input decorator?

**Answer**

Yes, current Angular supports signal inputs with `input()` and `input.required()`. They replace an
`@Input` declaration for that property while preserving parent-to-child binding semantics. A plain
`signal()` is only local state and does not receive a parent binding. Use a model input when the child
must expose two-way binding.

## What is Angular Gauge?

**Answer**

"Angular gauge" is not an Angular framework feature. It usually means a gauge chart implemented by a
third-party Angular component library. Evaluate accessibility, bundle size, SSR support, theming,
license, maintenance, and whether a simpler progress visualization communicates the value better.

## How will you create a reactive form for login in Angular?

**Answer**

Import `ReactiveFormsModule`, create typed controls with validation, bind the `FormGroup`, show
accessible validation errors, and submit only valid values. Disable duplicate submission while the
request is pending and map server errors back to the form without revealing whether a sensitive
account exists.

```typescript
readonly loginForm = this.formBuilder.nonNullable.group({
  email: ['', [Validators.required, Validators.email]],
  password: ['', Validators.required],
});
```

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

- `jest.fn()` creates a controllable mock function.
- `jest.spyOn(object, 'method')` observes or replaces one existing method; restore it after the test.
- `jest.mock('module')` replaces a module, subject to Jest's module-hoisting and ESM rules.
- A `__mocks__` directory can provide a manual module mock.

Prefer injecting a small fake or spy through Angular's test provider configuration when that keeps
the test explicit. Mock behavior at the boundary being tested, not every implementation detail.

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
  @Input('appHoverColor') hoverColor = 'blue';
  constructor(private el: ElementRef, private renderer: Renderer2) {}
  @HostListener('mouseenter') onMouseEnter() {
    this.changeColor(this.hoverColor);
  }
  @HostListener('mouseleave') onMouseLeave() {
    this.renderer.removeStyle(this.el.nativeElement, 'backgroundColor');
  }
  private changeColor(color: string): void {
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

## References

- [Angular documentation](https://angular.dev/overview)
- [Component lifecycle](https://angular.dev/guide/components/lifecycle)
- [Accepting data with input properties](https://angular.dev/guide/components/inputs)
- [Route guards](https://angular.dev/guide/routing/route-guards)
- [HTTP client setup](https://angular.dev/guide/http/setup)
- [Angular version compatibility](https://angular.dev/reference/versions)
