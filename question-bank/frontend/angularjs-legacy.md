# AngularJS (Legacy)

[Back to the question-bank index](../README.md)

AngularJS is the end-of-life 1.x framework and is different from modern Angular. These questions are
retained because they can still appear when interviewing for maintenance or migration work.

## What are `$rootScope`, `$scope`, and `$broadcast` in AngularJS?

**Answer**

- `$scope` is the binding context traditionally used between an AngularJS controller and its view.
- `$rootScope` is the top-level scope from which other scopes inherit. Storing broad mutable state
  there creates hidden coupling, so services are generally a better owner for shared state.
- `$broadcast(name, data)` sends an event downward from a scope to its descendants. `$emit` sends an
  event upward toward the root.

Listeners registered with `$scope.$on(...)` should be cleaned up when their lifecycle requires it.
For new applications, use modern Angular components, dependency injection, signals or observables
instead of introducing AngularJS scope-based architecture.

## What does this AngularJS `ng-switch` example render?

**Answer**

```html
<div ng-app="myApp" ng-controller="ColorController">
  <div ng-switch="color">
    <div ng-switch-when="red">You selected Red!</div>
    <div ng-switch-when="blue">You selected Blue!</div>
    <div ng-switch-default>Please select a color.</div>
  </div>
</div>

<script>
  angular.module('myApp', []).controller('ColorController', function ($scope) {
    $scope.color = 'red';
  });
</script>
```

AngularJS bootstraps the `myApp` module, creates the controller scope, and assigns `red` to
`color`. `ng-switch` evaluates that value, so the page renders **You selected Red!**. This is an
AngularJS 1.x example; its modules, controllers, scopes, and directives should not be confused with
modern Angular's component model.

## References

- [AngularJS long-term support ended](https://goo.gle/angularjs-eol)
- [Modern Angular documentation](https://angular.dev/)
