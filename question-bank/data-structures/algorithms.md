# Data Structures and Algorithms

Core data-structure selection and complexity questions.

[Back to the question-bank index](../README.md)

## How many nodes are at level four of a perfect binary tree if the root is level one?

**Answer**

A perfect binary tree has `2^(level - 1)` nodes at a given level. Level four therefore has
`2^(4 - 1) = 8` nodes.

The word **perfect** matters. A tree described only as balanced is not guaranteed to have every
position at that level filled.

## What is the time complexity of finding the smallest element in a binary max-heap?

**Answer**

It is `O(n)` in the worst case. In a max-heap, only the maximum is ordered at the root. The minimum
must be among the leaves, and a binary heap has roughly `n / 2` leaves, so finding it requires a
linear scan of those candidates.

## What is the worst-case number of comparisons when searching a singly linked list of length `n`?

**Answer**

The worst case requires `n` comparisons: the value is either in the final node or is absent. The
time complexity is therefore `O(n)`.

## How many stacks are needed to implement a queue without another collection type?

**Answer**

Two stacks are sufficient:

- enqueue by pushing onto the input stack;
- dequeue from the output stack; and
- when the output stack is empty, move every item from the input stack to the output stack first.

Each element moves between stacks at most once before removal, so the amortized time per operation is
`O(1)`, although a single transfer can take `O(n)`.

## Which data structure should count web requests by IP address?

**Answer**

Use a hash map whose key is the normalized IP address and whose value is the request count. Each
request performs an expected `O(1)` lookup and increment.

For a bounded in-memory interview problem, this is sufficient. A production system must additionally
consider canonical IPv4/IPv6 representation, concurrency, memory limits, persistence, and whether
counts need to be distributed across multiple processes.
