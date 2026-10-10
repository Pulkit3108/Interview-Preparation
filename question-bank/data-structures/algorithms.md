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

## How would you build an autocomplete index with a trie?

**Answer**

Insert normalized search terms into a trie, one character or token per edge. A lookup walks the
prefix and then returns candidate completions beneath that node. To avoid traversing a large subtree
for every request, each node can retain a bounded list of the highest-ranked completions for its
prefix.

Ranking might combine popularity, freshness, locale, personalization, and business rules. Updates
must keep those summaries consistent, and Unicode normalization and tokenization must be explicit.
A trie is not automatically the best production representation; compressed tries, finite-state
structures, search indexes, or database-specific prefix indexes can use less memory or support more
ranking features.

## How do you sort data that is larger than available memory?

**Answer**

Use an external merge sort:

1. read a memory-bounded chunk;
2. sort it in memory and write it as a sorted run;
3. repeat for the remaining input; and
4. perform a k-way merge of the runs using buffered reads and a min-heap keyed by the next item from
   each run.

Choose the run size and merge fan-in from the memory and file-descriptor budget. Stream output rather
than loading it all, use a stable tie-breaker when required, and plan temporary storage and cleanup.
For distributed data, partitioning and range boundaries add another correctness layer.
