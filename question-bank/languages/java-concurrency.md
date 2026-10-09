# Java Concurrency

Threads, synchronization, locks, visibility, atomicity, and concurrent programming.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## Tell a bit about mutex, semaphores, threads, processes, and program

**Answer**

- **Mutex (Mutual Exclusion):** Ensures that only one thread can access a resource at a time, preventing race conditions.
- **Semaphores:** Controls access to a shared resource through a counter, allowing a specified number of threads to access the resource simultaneously.
- **Threads:** The smallest unit of execution within a process, sharing the same memory space but executing independently.
Process is an instance of a program that is being executed. Each process has its own memory space. A program in execution.
Program is a sequence of instructions and data  that a CPU needs to accomplish a specific task. It is simply an executable file.

## What are different ways to create a Thread?

**Answer**

- **Extending the Thread Class:** Create a new thread by extending the Thread class and overriding the run() method.
- **Implementing the Runnable Interface:** Create a new thread by implementing the Runnable interface and passing an instance to a Thread object.
- **Using the Callable Interface and FutureTask:** Create a new thread using the Callable interface, which can return a result and throw a checked exception, and manage it with FutureTask.
- **Using the ExecutorService Framework:** Use the ExecutorService framework to manage a pool of threads and their lifecycle.

## In which scenarios you will see concurrent modification exception?

**Answer**

- **Single-Threaded Iteration with Modification:** Occurs when a collection is modified during iteration without using the iterator's methods.
- **Solution:** Use the iterator's remove method to modify the collection during iteration.
- **Concurrent access:** a fail-fast iterator may detect structural modification from another thread,
  but detection is best-effort and `ConcurrentModificationException` is not a concurrency guarantee.
  Choose a concurrent collection with the required iterator semantics, or synchronize both iteration
  and mutation on the same lock. A synchronized wrapper alone is insufficient unless traversal also
  follows its locking contract.

## Explain Multithreading and Asynchronous Programming.

**Answer**

Multithreading A form of concurrency that involves running multiple threads simultaneously on a multi-core processor. Multithreading is good for parallelizing CPU-bound tasks and managing user interfaces. However, managing multithreaded applications can be complex because of issues like deadlocks, race conditions, and the need for synchronization.
Asynchronous programming is a programming paradigm that allows a unit of work to run separately from the main application thread. When the work is complete, it notifies the main thread about its completion or failure. This approach is often used to handle I/O-bound operations, such as network requests, file I/O, or database queries, without blocking the main thread.
Multitasking is the ability of an operating system or a computing environment to execute multiple tasks or processes simultaneously. It allows a computer to perform several operations at the same time, improving efficiency and resource utilization. Multitasking can be achieved through various techniques, including time-sharing, parallel processing, and concurrency.
Preemptive Multitasking the operating system controls the allocation of CPU time to various tasks. The OS can interrupt a running task to allocate CPU time to another task, ensuring that all tasks get a fair share of the CPU.
- **Cooperative Multitasking:** each task is responsible for yielding control to other tasks. If a task does not yield control, it can monopolize the CPU, leading to poor system responsiveness.
- **Multiprocessing:** involves the use of two or more CPUs within a single computer system. Each CPU can execute its own process independently, allowing true parallel execution of tasks.

## What is the synchronized keyword?

**Answer**

synchronized keyword in Java is used to control access to a block of code or an object by multiple threads. It ensures that only one thread can execute a synchronized block or method at a time, which helps in achieving thread safety by preventing concurrent access to shared resources.
- **Synchronized Methods:** Can be instance methods or static methods. Instance methods lock the object, while static methods lock the class object.
- **Synchronized Blocks:** Allow more fine-grained control over synchronization by synchronizing only a portion of a method.

## What are some of the lock-less mechanisms?

**Answer**

- **Atomic Variables:** Lock-free, thread-safe operations on single variables.
- **Examples:** AtomicInteger, AtomicLong, AtomicBoolean, AtomicReference.
- **Concurrent Collections:** Thread-safe collections without explicit synchronization.
- **Examples:** ConcurrentHashMap, ConcurrentLinkedQueue, ConcurrentSkipListMap, CopyOnWriteArrayList.
- **Compare-And-Swap (CAS):** Atomic instruction for synchronization without locking.
`ReentrantReadWriteLock` and the read/write modes of `StampedLock` are locks, not lock-free
mechanisms. Lock-free examples include suitable atomic-variable algorithms and some concurrent queue
operations, but “uses a concurrent collection” does not imply every operation is lock-free.

## What is ReentrantLock?

**Answer**

- **ReentrantLock:** A flexible and powerful alternative to the synchronized keyword for thread synchronization.
- **Reentrant:** Allows a thread to re-acquire the lock it already holds.
- **Explicit Locking:** Requires explicit calls to lock() and unlock().
- **Fairness:** Can be configured to be fair, ensuring the longest-waiting thread acquires the lock first.
- **Condition Variables:** Supports multiple condition variables for complex thread coordination.

## What are mutations?

**Answer**

- **Mutations:** Changes or modifications made to the state of an object or data structure

When multiple threads mutate shared state without a correct happens-before relationship, a race can
make the outcome depend on execution timing. Avoid shared mutable state where possible; otherwise
use the appropriate lock, atomic type, concurrent collection, immutability, or message-passing model.

## What are different Thread states?

**Answer**

- **NEW:** The thread is created but not yet started. When a thread is created using the new keyword.
- **RUNNABLE:** the JVM state covering both executing and ready-to-run threads.
- **BLOCKED:** The thread is blocked waiting for a monitor lock. When a thread tries to enter a synchronized block or method but another thread holds the lock
- **WAITING:** The thread is waiting indefinitely for another thread to perform a particular action. When a thread calls Object.wait(), Thread.join(), or LockSupport.park()
TIMED_WAITING: The thread is waiting for another thread to perform a particular action for a specified waiting time. When a thread calls Thread.sleep(), Object.wait(long), Thread.join(long), or LockSupport.parkNanos()/parkUntil().
- **TERMINATED:** the `Thread.run()` method completed normally or abruptly. `Callable.call()` is a
  task method and is not itself a thread lifecycle state.

## What happens when thread.start() method is called on a method more than once?

**Answer**

- **First Call to start():** Transitions the thread from the "new" state to the "runnable" state.
The run() method is invoked in a new thread of execution.
- **Subsequent Calls to start():** Throws an IllegalThreadStateException.
A thread can only be started once. Once it has completed execution, it cannot be restarted.
Best Practices
- **Create a New Thread Object:** If you need to run the same task again, create a new instance of the Thread class or implement the Runnable interface and create a new Thread object.
- **Use ExecutorService:** For managing a pool of threads and reusing them, consider using the ExecutorService framework provided by the java.util.concurrent package.

## Suppose you are working on a high performance Financial Trading Application that frequently updates prices and sorts them. Which Java Collection is best suited for this scenario?

**Answer**

No collection is best without access-pattern requirements. If prices are keyed by an instrument and
must support concurrent ordered/range queries, `ConcurrentSkipListMap` is a reasonable candidate with
expected logarithmic updates and navigation. If sorting is only an occasional snapshot, a
`ConcurrentHashMap` plus a copied-and-sorted view may be cheaper. A real trading path also needs
atomic update semantics, latency measurements, ordering requirements, and allocation analysis.

## What is the difference between fail safe and fail fast collection?

**Answer**

- **Fail-Fast Collections:** Behavior: Throw ConcurrentModificationException if modified during iteration.
- **Detection:** Use a modification count (modCount) to detect concurrent modifications.
- **Examples:** ArrayList, HashMap, HashSet, LinkedList.
“Fail-safe” is informal terminology. `CopyOnWriteArrayList` iterators traverse an immutable snapshot.
`ConcurrentHashMap` iterators are weakly consistent: they do not throw
`ConcurrentModificationException`, may reflect some concurrent updates, and do not freeze a full
snapshot. State the actual iterator contract instead of grouping all concurrent collections under
one behavior.

## Suppose you are developing an application that allows multiple users to modify a shared list of tasks concurrently. In this scenario what causes Concurrent Modification Exception and what can you do to prevent this?

**Answer**

- **Causes of ConcurrentModificationException:** Modifying the list during iteration by another thread.
- **Preventing ConcurrentModificationException:** Synchronized Collections: Use Collections.synchronizedList() to synchronize access.
- **Concurrent Collections:** Use CopyOnWriteArrayList for concurrent access and modifications.
- **Explicit Synchronization:** Manually synchronize access using synchronized blocks or locks.

## What are some of the locking mechanisms?

**Answer**

Intrinsic monitors (`synchronized`), `ReentrantLock`, read/write locks, and `StampedLock` are locking
mechanisms. `Semaphore` controls permits and can model bounded access but does not require ownership.
`CountDownLatch`, `CyclicBarrier`, and `Phaser` are coordination primitives, not locks.

## Does Java support multithreading by default? If so, is it Synchronous or Asynchronous?

**Answer**

- **Java Supports Multithreading:** Java has built-in support for multithreading through the Thread class, Runnable interface, and Executors framework.
- **Synchronous Execution:** Tasks are executed one after another in a sequential manner.
- **Asynchronous Execution:** Tasks can be executed concurrently, allowing multiple tasks to run in parallel.
Java supports both blocking/synchronous coordination and asynchronous task composition. Creating
threads does not make an API inherently asynchronous; that depends on whether the caller waits for
completion and how results are communicated.

## Why is implementing Runnable better than extending Thread for Multithreading?

**Answer**

- **Separation of Concerns:** Runnable: Separates the task from the thread execution mechanism.
- **Thread:** Combines the task with the thread execution mechanism.
- **Reusability:** Runnable: The same Runnable instance can be reused by multiple threads.
- **Thread:** Each instance is tightly coupled to a specific thread.
- **Flexibility:** Runnable: Allows the class to extend another class if needed.
- **Thread:** Limits the class to extend only Thread.
- **Decoupling:** Runnable: Decouples the task from thread management.
- **Thread:** Couples the task with thread management.
- **Executor compatibility:** executors accept `Runnable` and `Callable` tasks. `Thread` implements
  `Runnable`, so it can technically be submitted, but doing so invokes its `run` method on a pool
  worker and does not start that `Thread`; using a plain task avoids this misleading design.

## How Multithreading improves Application performance and what are some challenges in it?

**Answer**

Multithreading Improves Application Performance:
- **Parallelism:** Multithreading allows multiple threads to run concurrently, making better use of multi-core processors and improving performance for CPU-bound tasks.
- **Responsiveness:** By offloading long-running tasks to separate threads, the main thread can remain responsive to user interactions, enhancing the user experience.
- **Resource Utilization:** Multithreading can improve resource utilization by allowing threads to perform I/O operations while other threads continue processing, reducing idle time.
- **Throughput:** By processing multiple tasks simultaneously, multithreading can increase the overall throughput of the application.
- **Challenges in Multithreading:** Synchronization Issues: Ensuring that shared resources are accessed in a thread-safe manner can be complex and error-prone, leading to issues like race conditions, deadlocks, and data corruption.
- **Deadlocks:** Deadlocks occur when two or more threads are waiting indefinitely for each other to release resources, causing the application to hang.
- **Race Conditions:** Race conditions happen when the outcome of a program depends on the timing of thread execution, leading to unpredictable and incorrect results.
- **Complexity:** Writing, debugging, and maintaining multithreaded code is more complex than single-threaded code, increasing the risk of bugs and errors.
- **Context Switching Overhead:** Frequent context switching between threads can introduce overhead, reducing the performance gains from multithreading.
- **Resource Contention:** Multiple threads competing for the same resources (e.g., CPU, memory, I/O) can lead to contention, reducing the efficiency of the application.
- **Memory Consistency Errors:** Ensuring that changes made by one thread are visible to other threads can be challenging, leading to memory consistency errors.
- **Testing and Debugging:** Multithreaded applications are harder to test and debug due to non-deterministic behavior and timing issues.

## What are Thread Leakages?

**Answer**

- **Thread Leakage:** Occurs when threads are created but not properly managed, leading to inactive or "leaked" threads that consume system resources.
- **Causes:** tasks that never finish, unbounded blocking without timeouts, lost interruption,
  unclosed executors, long-lived thread-local values, or repeated unmanaged thread creation. An
  uncaught exception normally terminates a thread rather than leaking it.
Improper thread pool management.
Resource leaks.
Blocking operations.
- **Consequences:** Resource exhaustion.
Increased latency.
Unpredictable behavior.
- **Prevention and Detection:** Proper thread management and termination.
Use thread pools and properly shut them down.
Use timeouts and handle interruptions.
Monitor and profile threads using tools like VisualVM, JConsole, and Java Mission Control.

## How would you make sure the update to a field of object is safe in a Multi Threaded Environment?

**Answer**

- **Synchronized Methods or Blocks:** Use synchronized keyword to ensure mutual exclusion.
- **Example:** `public synchronized void increment() { count++; }`
- **Atomic Variables:** Use atomic variables from java.util.concurrent.atomic package.
- **Example:** `private final AtomicInteger count = new AtomicInteger()`
`volatile` is enough only for an independent read/write such as publishing a flag or immutable
snapshot. It does not make `count++` atomic. Use an atomic type or a lock when an update depends on
the previous value or must preserve a multi-field invariant.
java.util.concurrent Locks:
Use explicit locks from java.util.concurrent.locks package.
- **Example:** `private final Lock lock = new ReentrantLock()`
java.util.concurrent Collections:
Use thread-safe collections from java.util.concurrent package.
- **Example:** `private final ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>()`
java.util.concurrent Utilities:
Use higher-level concurrency utilities from java.util.concurrent package.
- **Example:** ExecutorService, CountDownLatch, CyclicBarrier, Semaphore.

## What are different ways to make code Thread Safe?

**Answer**

- **Synchronized Methods/Blocks:** Use the synchronized keyword to control access to critical sections of code.
- **Volatile Keyword:** Use the volatile keyword to ensure visibility of changes to variables across threads.
- **Atomic Variables:** Use classes from the java.util.concurrent.atomic package for atomic operations.
- **Locks:** Use explicit locks provided by java.util.concurrent.locks.Lock.
- **Concurrent Collections:** Use thread-safe collections from the java.util.concurrent package.
- **ThreadLocal Variables:** Use ThreadLocal to ensure that each thread has its own instance of a variable.
- **Immutable Objects:** Design objects to be immutable so that their state cannot be changed after creation.
- **Using Executors:** Use the ExecutorService to manage and control thread execution.

## Can you explain synchronization for thread safety?

**Answer**

- **Synchronization:** Ensures that multiple threads can access shared resources in a controlled manner, preventing data inconsistency and ensuring thread safety.
- **Synchronized Methods:** Only one thread can execute a synchronized method at a time for a given object.
- **Synchronized Blocks:** Allows more fine-grained control over synchronization by locking only a specific section of code.
- **Intrinsic Locks (Monitors):** Every object in Java has an intrinsic lock. When a thread enters a synchronized method or block, it acquires the lock. When it exits, it releases the lock.
- **Reentrant Locks:** Java's intrinsic locks are reentrant, meaning that if a thread already holds the lock, it can re-enter the synchronized method or block without blocking itself.

## What is the difference between synchronized vs Reentrant Locks

**Answer**

Synchronized Block
- **Basic Concept:** A synchronized block is a built-in mechanism in Java for achieving thread synchronization.
- **Syntax:** Uses the synchronized keyword.
- **Locking:** Implicitly acquires and releases the lock on the specified object.
- **Reentrancy:** Supports reentrant locking, allowing a thread to re-enter a synchronized block it already holds the lock for.
- **Fairness:** Does not provide fairness options; threads acquire locks in an unspecified order.
- **Condition Variables:** Limited to using wait(), notify(), and notifyAll() for thread communication.
- **Performance:** Simpler and generally faster for basic synchronization needs.
ReentrantLock
- **Basic Concept:** A ReentrantLock is a class in java.util.concurrent.locks package that provides more advanced locking mechanisms.
- **Syntax:** Uses the ReentrantLock class.
- **Locking:** Explicitly acquires and releases the lock using lock() and unlock() methods.
- **Reentrancy:** Supports reentrant locking, similar to synchronized blocks.
- **Fairness:** Can be configured for fairness, ensuring threads acquire locks in the order they requested them.
- **Condition Variables:** Provides multiple Condition objects for more flexible thread communication.
- **Performance:** More flexible and powerful, but slightly more complex and may have a performance overhead for simple use cases.

## What are the different methods used in multithreading?

**Answer**

Locking and Unlocking
synchronized (object): Acquires the intrinsic lock on the specified object.
ReentrantLock.lock(): Acquires the lock, blocking if necessary until it is available.
ReentrantLock.unlock(): Releases the lock.
Waiting and Notification
Object.wait(): Causes the current thread to wait until another thread invokes notify() or notifyAll() on the same object.
Object.notify(): Wakes up a single thread that is waiting on the object's monitor.
Object.notifyAll(): Wakes up all threads that are waiting on the object's monitor.
Condition Variables (ReentrantLock)
Condition.await(): Causes the current thread to wait until it is signaled or interrupted.
Condition.signal(): Wakes up one waiting thread.
Condition.signalAll(): Wakes up all waiting threads.
Thread Management
Thread.start(): Begins execution of a new thread.
Thread.join(): Waits for the thread to die.
Thread.sleep(milliseconds): Causes the current thread to sleep for the specified number of milliseconds.
Thread.yield(): Hints to the scheduler that the current thread is willing to yield its current use of a processor.
Atomic Operations
AtomicInteger.incrementAndGet(): Atomically increments the current value by one and returns the updated value.
AtomicInteger.compareAndSet(expectedValue, newValue): Atomically sets the value to the given updated value if the current value equals the expected value.
Executors and Thread Pools
Executors.newFixedThreadPool(n): Creates a thread pool that reuses a fixed number of threads.
ExecutorService.submit(task): Submits a task for execution and returns a Future representing the task.
ExecutorService.shutdown(): Initiates an orderly shutdown in which previously submitted tasks are executed, but no new tasks will be accepted.
Summary

## Can a deadlock occur with a single thread?

**Answer**

A classic lock-order deadlock involves two or more threads in a wait cycle. A single thread can still
self-deadlock on a non-reentrant primitive or block forever after consuming all permits and waiting
for another permit that only it could release. Java intrinsic locks and `ReentrantLock` are reentrant,
so reacquiring those particular locks in the same thread does not self-deadlock. Answer from the
specific synchronization primitive rather than asserting that every deadlock requires two threads.

## Which concurrency utilities were added or significantly enhanced in Java 8?

**Answer**

Java 8 added `CompletionStage` and `CompletableFuture` for composing asynchronous stages,
`StampedLock` with write, read, and optimistic-read modes, and contention-friendly counters such as
`LongAdder`, `DoubleAdder`, `LongAccumulator`, and `DoubleAccumulator`. It also exposed the common
`ForkJoinPool` and expanded `ConcurrentHashMap` operations.

These are library and runtime-library additions, not a replacement for the Java Memory Model.
`LongAdder`, for example, improves throughput for contended statistics but does not provide an atomic
snapshot suitable for coordinating other state.

## What is the difference between volatile and Atomic variables?

**Answer**

- **Visibility:** Both volatile and atomic variables ensure visibility of changes across threads.
- **Atomicity:** volatile provides atomicity only for individual read/write operations.
Atomic variables provide atomicity for compound actions (e.g., incrementing, updating).
- **Usage:** Use volatile for simple flags and state variables where only individual read/write operations are needed.
Use atomic variables for counters, sequence numbers, and other variables where atomic operations are required.

## References

- [Java SE 8 concurrency utilities enhancements](https://docs.oracle.com/javase/8/docs/technotes/guides/concurrency/changes8.html)
- [`CompletableFuture` API](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html)
- [`StampedLock` API](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/locks/StampedLock.html)
- [`LongAdder` API](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/LongAdder.html)
