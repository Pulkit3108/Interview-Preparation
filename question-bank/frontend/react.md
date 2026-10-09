# React

React components, hooks, routing, composition, context, and performance.

[Back to the question-bank index](../README.md)

## What are React Hooks, and how does routing work in a React application?

**Answer**

**Hooks** are functions that let function components use React features such as state, effects, context, and reducers. Common examples include `useState`, `useEffect`, `useContext`, and `useReducer`. Hooks must be called at the top level of a component or custom Hook, not inside loops or conditions.

**Routing** is not built into React itself. A routing library such as React Router maps URL paths to UI elements and supports navigation without a full page reload. In React Router's declarative mode, an application commonly uses `BrowserRouter`, `Routes`, `Route`, `Link`, and `NavLink`. `Switch` belongs to older React Router versions; current declarative routing uses `Routes`.

```jsx
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/users/:userId" element={<UserProfile />} />
  </Routes>
</BrowserRouter>
```

## In React, how would you implement a higher-order component (HOC)?

**Answer**

A higher-order component is a function that accepts a component and returns a new component with additional behavior or props. It is a composition technique, not a special React API.

```jsx
function withLoading(WrappedComponent) {
  return function WithLoading({ isLoading, ...props }) {
    if (isLoading) {
      return <p>Loading...</p>;
    }

    return <WrappedComponent {...props} />;
  };
}

const UserListWithLoading = withLoading(UserList);
```

The wrapper should forward the props the wrapped component needs. HOCs remain useful in existing code and libraries, although custom Hooks are often clearer for sharing stateful logic in new function components.

## In React, what is the main advantage of using the Context API over passing props?

**Answer**

Context lets a distant descendant read a value without forwarding that value through every intermediate component. This reduces prop drilling for values such as the current user, theme, or locale.

Context is not automatically more efficient and is not a replacement for every form of state management. When a provider receives a different value, React re-renders consumers of that context. Keep providers focused, avoid recreating object values unnecessarily, and use ordinary props when the data is needed by only a few nearby components.

## In React, what is the difference between useCallback and useMemo hooks?

**Answer**

- `useCallback(fn, dependencies)` caches the **function definition** between renders. It is mainly useful when passing a callback to a memoized child or when another Hook depends on a stable function reference.
- `useMemo(calculate, dependencies)` calls a pure calculation and caches its **result** until a dependency changes. It is useful for an expensive calculation or a value whose stable identity enables another optimization.

```jsx
const handleSave = useCallback(() => saveDocument(documentId), [documentId]);
const visibleRows = useMemo(() => filterRows(rows, query), [rows, query]);
```

Both are performance optimizations, not correctness tools. Their dependency lists must include every reactive value used by the callback or calculation, and they should be added only when there is a concrete reason to preserve identity or avoid work.

## References

- [Built-in React Hooks](https://react.dev/reference/react/hooks)
- [React `useContext`](https://react.dev/reference/react/useContext)
- [React `useCallback`](https://react.dev/reference/react/useCallback)
- [React `useMemo`](https://react.dev/reference/react/useMemo)
- [React Router declarative routing](https://reactrouter.com/start/declarative/routing)
