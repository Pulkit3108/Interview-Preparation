# Computer Architecture Fundamentals

Memory hierarchies, cache organization, locality, and processor-memory performance.

[Back to the question-bank index](../README.md)

## Why do computers use a memory hierarchy?

**Answer**

No single storage technology simultaneously provides the lowest latency, highest capacity, lowest
cost, and non-volatility. A hierarchy combines small, fast storage close to execution units with
progressively larger and slower storage farther away.

A typical path includes registers, one or more processor-cache levels, main memory, and persistent
storage. Performance depends on how often requested data is found at each level and the penalty for
continuing to the next one. Exact levels, sharing, inclusion policies, and latencies vary by
processor and system.

## What are temporal and spatial locality?

**Answer**

**Temporal locality** means recently accessed data or instructions are likely to be accessed again.
**Spatial locality** means addresses near a recent access are likely to be accessed soon.

Caches exploit temporal locality by retaining recently used lines and spatial locality by moving a
block of adjacent bytes rather than one byte at a time. Sequential traversal often benefits from
both, while large irregular pointer-heavy access patterns can produce more misses.

## What are cache lines, hits, misses, and miss penalties?

**Answer**

A cache stores memory in fixed-size blocks called cache lines. A **hit** occurs when the requested
line is present at the checked cache level. A **miss** requires looking in another cache level or
memory, incurring a **miss penalty**.

Misses are often described as compulsory, capacity, or conflict misses. Real processors add
prefetching, non-blocking requests, coherence, translation, write buffers, and out-of-order
execution, so observed latency is not simply one fixed number per level.

## How do direct-mapped, fully associative, and set-associative caches differ?

**Answer**

- In a **direct-mapped** cache, each memory block has one possible cache location. Lookup hardware
  is simple, but frequently used blocks that map to the same location can evict one another.
- In a **fully associative** cache, a block can occupy any line. This minimizes placement conflicts
  but requires comparing more tags and choosing a victim from the entire cache.
- In an **N-way set-associative** cache, an address selects one set and the block can occupy any of
  the set's `N` ways. This balances lookup cost and conflict reduction.

Associativity is only one design dimension. Line size, capacity, replacement approximation, write
policy, coherence, latency, energy, and workload access patterns also matter.

## What do write-through, write-back, write-allocate, and no-write-allocate mean?

**Answer**

With **write-through**, a cache write also propagates to the next level, often through a write
buffer. With **write-back**, the cache marks the line dirty and writes it to the next level when the
line is evicted or explicitly cleaned.

On a write miss, **write-allocate** first brings the line into the cache and then updates it.
**No-write-allocate** sends the write onward without filling that cache. Write-back commonly pairs
with write-allocate, while write-through often pairs with no-write-allocate, but these are separate
policy choices.

## Why can cache-friendly code be faster even when its algorithmic complexity is unchanged?

**Answer**

Two implementations can perform the same asymptotic number of operations but generate very
different memory traffic. Traversing contiguous data, reusing a bounded working set, and processing
data in blocks can improve line reuse and reduce cache and translation misses.

This is not permission to optimize from folklore. Measure with representative inputs and profiling
or hardware-counter tools. A transformation that improves locality can increase code complexity,
copying, branch cost, or memory use and may behave differently across processors.

## References

- [Intel 64 and IA-32 Architectures Optimization Reference Manual](https://www.intel.com/content/dam/doc/manual/64-ia-32-architectures-optimization-manual.pdf)
- [Intel architecture manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
