# Operating Systems

Processes, threads, scheduling, synchronization, deadlocks, memory management, and storage I/O.

[Back to the question-bank index](../README.md)

## What does an operating system do?

**Answer**

An operating system manages hardware resources and provides abstractions and services that
applications use. Its responsibilities commonly include:

- scheduling threads on processors;
- isolating processes and managing virtual memory;
- coordinating access to devices and persistent storage;
- exposing file, networking, timing, and interprocess-communication interfaces; and
- enforcing permissions and other protection boundaries.

The kernel is the privileged core of the operating system. User-facing tools, libraries, and
services are part of the broader operating-system environment but do not all run in kernel mode.

## How do batch, multiprogramming, time-sharing, and real-time systems differ?

**Answer**

- **Batch processing** executes submitted jobs with little or no interactive input.
- **Multiprogramming** keeps several jobs available so the processor can run another when one is
  waiting, such as for I/O.
- **Time-sharing** rapidly schedules runnable work from multiple users or applications to provide
  interactive responsiveness.
- **Real-time systems** must satisfy defined timing constraints. A hard real-time system treats a
  missed deadline as a system failure; a soft real-time system can tolerate occasional misses with
  degraded quality.

These descriptions are workload and scheduling models, not mutually exclusive product categories.
A modern operating system can support several of them.

## What is the difference between a program, process, and thread?

**Answer**

A **program** is executable code and associated data at rest. A **process** is a running instance
with resources such as a virtual address space, open handles, credentials, and at least one thread.
A **thread** is an execution stream that the scheduler can run.

Threads in one process normally share the process's code, heap, and open resources, while each
thread has its own execution context, including a program counter, registers, and stack. This makes
communication between threads inexpensive, but it also means an unsynchronized write by one thread
can corrupt state observed by the others.

## What information does a process control block contain?

**Answer**

A process control block, or equivalent kernel structure, records the state needed to manage a
process. Typical fields include its identifier, execution state, scheduling information, saved CPU
context, address-space metadata, credentials, accounting data, and references to open resources.

Exact names and boundaries are implementation-specific. Thread execution state may live in a
separate thread-control structure rather than directly in the process record.

## What happens during a context switch?

**Answer**

The operating system stops one runnable thread and resumes another. It preserves the outgoing
thread's execution context and restores the incoming thread's context. Depending on the switch, it
may also change address-space mappings and other processor state.

Context switching enables multitasking but is not free. It consumes CPU time and can disturb
caches and translation lookaside buffers, so excessive switching can reduce throughput.

## How does `fork()` differ from creating a thread?

**Answer**

On POSIX systems, `fork()` creates a child process. The child begins with a copy-on-write view of
the parent's address space and inherits selected process resources under defined rules. A thread
creation API adds another execution stream inside the same process and therefore shares that
process's address space and resources.

Calling `fork()` does not create a new thread in the parent. If a multithreaded process calls
`fork()`, only the calling thread is replicated in the child, which is why the child must be careful
with inherited synchronization state before an `exec` operation.

## What do arrival, burst, completion, turnaround, response, and waiting time mean?

**Answer**

- **Arrival time:** when work becomes ready for scheduling.
- **CPU burst time:** processor time the work requires during a burst.
- **Completion time:** when the work finishes.
- **Turnaround time:** completion time minus arrival time.
- **Response time:** time from arrival until the work first receives service.
- **Waiting time:** total time spent ready but not running.

For a simple single-burst exercise, waiting time is often calculated as turnaround time minus burst
time. Real workloads can alternate between CPU and I/O bursts, so schedulers measure these concepts
over a more complex lifecycle.

## How do common CPU scheduling algorithms differ?

**Answer**

- **First come, first served (FCFS):** runs work in arrival order. It is simple but can suffer from
  the convoy effect.
- **Shortest job first (SJF):** chooses the smallest predicted CPU burst. It minimizes average
  waiting time when predictions are accurate, but long jobs can starve.
- **Shortest remaining time first (SRTF):** the preemptive form of SJF.
- **Round robin:** gives each runnable task a time quantum. A very small quantum increases switching
  overhead; a very large one approaches FCFS.
- **Priority scheduling:** selects by priority and needs an anti-starvation policy such as aging.
- **Multilevel feedback queue (MLFQ):** moves work between queues based on observed behavior to
  balance responsiveness and throughput.

There is no universally best scheduler. The choice depends on goals such as latency, fairness,
deadline compliance, throughput, and implementation cost.

## What is a race condition?

**Answer**

A race condition exists when correctness depends on the relative timing or interleaving of
concurrent operations. For example, two threads that perform a read-modify-write update without
synchronization can lose one update.

A **data race** has a narrower language-level meaning: concurrent conflicting memory accesses, at
least one of which is a write, without the required synchronization. A program can be free of data
races and still have a higher-level race condition.

## What is a critical section, and what properties should its protocol provide?

**Answer**

A critical section accesses shared state that must not be manipulated concurrently in conflicting
ways. A classic solution aims to provide:

1. **Mutual exclusion:** at most one participant executes the protected section at a time.
2. **Progress:** if the section is free, eligible participants can eventually decide who enters.
3. **Bounded waiting:** a participant is not postponed indefinitely after requesting entry.

Real synchronization primitives also require a defined memory-ordering contract. Mutual exclusion
without the necessary visibility guarantees would not make shared-memory communication correct.

## How do mutexes and semaphores differ?

**Answer**

A **mutex** represents ownership of a mutually exclusive region. The thread that locks it is
normally responsible for unlocking it. Mutexes are appropriate for protecting an invariant over
shared state.

A **semaphore** maintains a count. Waiting decrements or consumes an available permit; signaling
increments or returns one. Counting semaphores can limit access to a pool of resources or coordinate
producers and consumers. A binary semaphore has at most one available permit, but it does not
necessarily have the ownership rules of a mutex.

## What is a deadlock?

**Answer**

A deadlock is a state in which a set of participants cannot make progress because each is waiting
for an event or resource that another participant in the set must provide.

For reusable, non-shareable resources, the classic Coffman conditions are:

1. mutual exclusion;
2. hold and wait;
3. no forced preemption; and
4. circular wait.

All four are necessary for this resource-deadlock model. Removing at least one prevents that class
of deadlock, though other liveness failures can still occur.

## How can a system handle deadlocks?

**Answer**

- **Prevention:** design resource rules so at least one necessary condition cannot hold, such as
  acquiring locks in a global order.
- **Avoidance:** grant requests only when the resulting state remains safe. Banker's algorithm is
  the textbook example and requires knowing maximum resource claims.
- **Detection and recovery:** allow deadlocks, detect cycles or unrecoverable waits, then terminate,
  roll back, or preempt work where the resource model permits it.
- **Operational handling:** when deadlock is rare or recovery is cheaper than continuous avoidance,
  use timeouts, watchdogs, cancellation, or restart procedures.

The right strategy depends on whether resources are preemptible, whether work can be rolled back,
and how costly false recovery is.

## How do deadlock, starvation, and livelock differ?

**Answer**

- **Deadlock:** participants are blocked waiting on one another and cannot proceed.
- **Starvation:** one participant waits indefinitely because others repeatedly receive service.
- **Livelock:** participants continue changing state or retrying but make no useful progress.

Fair scheduling, aging, bounded retries, randomized backoff, and consistent resource ordering
address different parts of these problems; none is a universal cure.

## What are logical and physical addresses?

**Answer**

A program normally issues virtual, or logical, addresses. The processor's memory-management unit
translates them through page tables and related structures into physical memory locations. This
translation lets each process use a private address space while the operating system controls
mapping, protection, sharing, and residency.

## What is virtual memory?

**Answer**

Virtual memory gives a process an address space independent of the exact physical-memory layout.
Only a working subset of mapped pages must be resident in RAM at a given moment; other mappings can
refer to executable files, memory-mapped files, zero-filled pages, or backing storage.

Virtual memory provides isolation and flexible mapping. It does not mean every virtual page must
have a copy in a swap file, and it does not make memory capacity unlimited.

## How do paging and segmentation differ?

**Answer**

**Paging** divides virtual and physical memory into fixed-size pages and frames. Page-table entries
map virtual pages to physical frames and store protection and status information.

**Segmentation** divides an address space into variable-size logical regions such as code, data, or
stacks. Classic pure segmentation can suffer from external fragmentation. Some architectures and
operating systems combine segmentation concepts with paging, while many modern general-purpose
systems rely primarily on paging.

## What is internal versus external fragmentation?

**Answer**

**Internal fragmentation** is unused space inside an allocated unit, such as the unused remainder
of a fixed-size page or block. **External fragmentation** is free space split into pieces that are
individually too small or poorly placed for a requested contiguous allocation.

Paging largely avoids external fragmentation for physical-memory frames, but page granularity can
still create internal waste.

## What is a page fault?

**Answer**

A page fault occurs when an address translation cannot be completed with the current page-table
state and control transfers to the operating system. The OS may load a valid nonresident page,
create a page on demand, perform a copy-on-write operation, update permissions or mappings, or reject
the access as invalid.

Therefore, a page fault is not automatically an application error. A major fault that requires
storage I/O is generally more expensive than a minor fault resolved without it.

## How do FIFO, optimal, and LRU page replacement differ?

**Answer**

- **FIFO** evicts the page that has been resident longest. It is simple but can discard a heavily
  used page.
- **Optimal replacement** evicts the page whose next use is farthest in the future. It is useful as
  a theoretical benchmark because an online system cannot know the future reference stream.
- **Least recently used (LRU)** evicts the page that has gone unused for the longest past interval.
  Exact LRU can be expensive, so real systems commonly use approximations and additional working-set
  information.

Replacement policy is only one part of memory management; dirty-page cost, file backing, process
working sets, and memory pressure also affect eviction decisions.

## What is Belady's anomaly?

**Answer**

Belady's anomaly is the counterintuitive result that increasing the number of available page frames
can increase the number of page faults for some reference strings under FIFO replacement. Stack
algorithms, whose resident set for `n` frames is always a subset of the set for `n + 1` frames, do
not exhibit the anomaly. LRU and optimal replacement have the stack property.

## What is thrashing?

**Answer**

Thrashing occurs when a system spends so much time servicing memory faults and moving pages that it
does little useful execution. It often indicates that active working sets exceed available physical
memory or that memory allocation and admission policies are poor.

Possible responses include reducing multiprogramming, reclaiming or limiting memory consumers,
adding physical memory, and using working-set-aware policies. Simply increasing concurrency can make
thrashing worse.

## How do first fit, best fit, and worst fit allocate variable-size memory blocks?

**Answer**

- **First fit** selects the first sufficiently large free block.
- **Best fit** selects the smallest block that satisfies the request.
- **Worst fit** selects the largest available block.

Best fit does not necessarily minimize total waste because it can leave many unusably small holes.
Allocator performance depends on request patterns, splitting and coalescing rules, metadata cost,
locality, and fragmentation over time.

## What is demand paging?

**Answer**

Demand paging brings a virtual page into physical memory when it is first needed rather than loading
every possible page in advance. A fault on a valid nonresident mapping triggers the required work.

The source may be an executable or mapped file, backing storage, or a newly allocated zero-filled
page. Demand paging should not be reduced to “moving unused memory to disk”; eviction and on-demand
population are related but distinct operations.

## How do monolithic kernels and microkernels differ?

**Answer**

A **monolithic kernel** keeps most core operating-system services, such as scheduling, virtual
memory, filesystems, and many drivers, in kernel space. This allows direct internal calls but creates
a large privileged fault domain.

A **microkernel** keeps a smaller set of mechanisms in kernel space and moves more services to
separate user-space processes that communicate through messages. This can improve isolation and
replaceability at the cost of additional communication and design complexity.

Practical systems occupy a spectrum; “hybrid kernel” is commonly used for designs that combine
properties of both.

## What is reentrant code?

**Answer**

Reentrant code can be safely entered again before an earlier invocation completes, including from
another thread or a signal context permitted by the platform. It avoids shared mutable invocation
state or protects it through mechanisms valid for that context.

Reentrancy is stronger than merely sharing one read-only copy of program code. It is also different
from thread safety: a function can be thread-safe through locking but still be unsafe to reenter from
a signal handler.

## What are common magnetic-disk scheduling algorithms?

**Answer**

For workloads where seek position materially affects latency:

- **FCFS** services requests in arrival order.
- **SSTF** chooses the request nearest the current head position, which can starve distant requests.
- **SCAN** moves in one direction servicing requests, then reverses.
- **C-SCAN** services in one direction and returns to the beginning without servicing the return
  path, producing more uniform waiting times.
- **LOOK** and **C-LOOK** reverse or wrap at the last pending request instead of travelling to the
  physical end.

These textbook algorithms model rotating disks. SSDs have different costs, and modern storage
stacks also consider device queues, request merging, fairness, priorities, and controller behavior.

## What are spooling and buffering?

**Answer**

**Buffering** temporarily holds data to absorb differences in transfer size or speed between a
producer and consumer. **Spooling** places complete jobs or streams in an intermediate queue so a
shared peripheral or service can process them independently. A print spooler is the classic example.

The concepts can overlap, but a buffer usually supports data transfer within an operation, whereas a
spool manages queued work across operations or clients.

## What is RAID, and what does it not guarantee?

**Answer**

RAID combines storage devices to achieve a selected balance of capacity, performance, and tolerance
of device failures. For example, RAID 0 stripes without redundancy, RAID 1 mirrors, and parity-based
levels trade write cost and rebuild complexity for usable capacity.

RAID is not a backup. It does not inherently protect against accidental deletion, corruption,
ransomware, controller defects, or site loss. The exact failure tolerance depends on the RAID level,
layout, implementation, and which devices fail.

## References

- [Microsoft: About processes and threads](https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads)
- [Microsoft: Virtual address space](https://learn.microsoft.com/en-us/windows/win32/memory/virtual-address-space)
- [POSIX `fork()` specification](https://pubs.opengroup.org/onlinepubs/9799919799/functions/fork.html)
- [POSIX threads definitions](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)
