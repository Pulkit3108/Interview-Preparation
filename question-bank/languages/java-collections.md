# Java Generics and Collections

Generics, collection interfaces, iteration, maps, ordering, and concurrent collections.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## What are generics in Java?

**Answer**

- **Generics:** Allow you to define classes, interfaces, and methods with type parameters.
Provide compile-time type safety and eliminate the need for casting.
- **Generic Class:** public class Box<T>
- **Generic Methods:** public static <T> void printArray(T[] array)
- **Bounded Type Parameters:** public static <T extends Number> void printNumber(T number)
Restrict the types that can be used as type parameters.
- **Wildcards:** public static void printList(List<?> list)
Represent an unknown type.

## Tell a bit about collection API, Collection and Collections?

**Answer**

- **Collection API:** A unified architecture for representing and manipulating collections in Java. It includes interfaces, implementations, and algorithms.
- **Collection Interface:** The root interface of the Collection Framework, representing a group of objects. It is extended by other interfaces like List, Set, and Queue.
- **Collections Class:** A utility class that provides static methods to operate on or return collections. It includes methods for sorting, searching, reversing,
and more.

## What is the difference between `Arrays.sort()` and `Collections.sort()`?

**Answer**

- **Data Structures:** Arrays.sort(): Used for sorting arrays.
Collections.sort(): Used for sorting lists.
- **Method Signatures:** Arrays.sort():
- **For primitive types:** public static void sort(int[] a), public static void sort(char[] a), etc.
- **For objects:** public static <T extends Comparable<? super T>> void sort(T[] a), public static <T> void sort(T[] a, Comparator<? super T> c).
Collections.sort():
- **For lists:** public static <T extends Comparable<? super T>> void sort(List<T> list), public static <T> void sort(List<T> list, Comparator<? super T> c).
- **Performance:** Arrays.sort(): Uses dual-pivot Quicksort for primitive types and a modified mergesort for objects.
`Collections.sort(list)` delegates to `List.sort`, and the list implementation controls how elements
are rearranged. Algorithm details are implementation notes, not API contracts.

## Can you tell me about the internal implementation of ArrayList & LinkedList?

**Answer**

- **ArrayList:** Underlying Data Structure: Dynamically resizable array.
- **Capacity and Size:** Capacity is the size of the underlying array; size is the number of elements stored.
- **Growth policy:** capacity grows automatically; the exact factor is an implementation detail.
- **Random Access:** O(1) time complexity.
- **Insertion/Deletion:** O(1) at the end, O(n) at arbitrary positions.
- **LinkedList:** Underlying Data Structure: Doubly linked list.
- **Nodes:** Each node contains references to the previous and next nodes and the element itself.
- **Sequential Access:** O(n) time complexity for random access.
- **Insertion/deletion:** relinking is O(1) when a node or iterator position is already known, but
  finding an arbitrary index is O(n).

## What is the difference between Array and ArrayList?

**Answer**

- **Size:** Array: Fixed size. Once created, the size cannot be changed.
- **ArrayList:** Dynamic size. Can grow and shrink as needed.
- **Type:** Array: Can hold both primitive types and objects.
- **ArrayList:** Can only hold objects (no primitive types directly).
- **Performance:** Array: Generally faster for fixed-size collections due to less overhead.
- **ArrayList:** Slightly slower due to dynamic resizing and additional methods.
- **Flexibility:** Array: Less flexible, requires manual resizing and copying.
- **ArrayList:** More flexible, provides built-in methods for resizing, adding, and removing elements.
- **Syntax:** array: `int[] values = new int[10]`
- **ArrayList:** `List<Integer> values = new ArrayList<>()`
- **Methods:** Array: Limited to basic operations (length, indexing).
- **ArrayList:** Rich set of methods (add, remove, get, size, etc.).

## What are the performance differences when using Arrays.sort() on primitive types and objects?

**Answer**

- **Primitive Types:** Algorithm: Dual-Pivot Quicksort
- **Time Complexity:** O(n log n) on average, O(n^2) in the worst case (rare)
- **Space Complexity:** O(log n)
- **Performance:** Highly efficient for large datasets, low memory overhead
- **Objects:** Algorithm: Timsort (hybrid of Merge Sort and Insertion Sort)
- **Time Complexity:** O(n log n) in both average and worst cases
- **Space Complexity:** O(n)
- **Performance:** Stable sorting, optimized for real-world data, consistent performance

## Which collection will you use for no duplicates and insertion order is maintained?

**Answer**

- **Collection:** LinkedHashSet
- **No Duplicates:** Ensures that no duplicate elements are allowed.
- **Insertion Order:** Maintains the order in which elements are inserted.
- **Performance:** Provides constant-time performance for basic operations like add, remove, and contains.

## Which collection will you use if you want elements to be sorted?

**Answer**

- **TreeSet:** Description: Implements NavigableSet and stores elements in a sorted order.
- **Key Characteristics:** No duplicates, O(log n) time complexity for basic operations.
- **TreeMap:** Description: Implements NavigableMap and stores key-value pairs in a sorted order based on the keys.
- **Key Characteristics:** No duplicate keys, O(log n) time complexity for basic operations.
- **PriorityQueue:** exposes the least element at its head according to its ordering, but iteration is
  not sorted. It suits repeated priority removal, not a generally sorted collection.

## How does TreeSet maintain sort order?

**Answer**

- **Underlying Data Structure:** TreeSet is backed by a TreeMap, which is implemented as a Red-Black tree.
- **Natural Ordering and Comparators:** Natural Ordering: Uses the natural ordering of elements (elements must implement Comparable).
- **Custom Comparator:** Allows for a custom sort order by providing a Comparator.
- **Insertion:** Elements are added in the correct position to maintain the sorted order.
The Red-Black tree rebalances if necessary.
- **Balancing:** The Red-Black tree ensures balance by maintaining the longest path from the root to a leaf to be no more than twice as long as the shortest path.
Achieved through rotations and color changes during insertions and deletions.
- **Lookup:** Efficient lookup by traversing the tree from the root to the leaf, following the binary search property.

## Tell me any use cases of TreeMap?

**Answer**

- **Use Case:** Implementing a Leaderboard
Consider a scenario where you need to implement a leaderboard for a game. The leaderboard should maintain the scores of players in sorted order, allowing you to quickly retrieve the top players and their scores.

## Does TreeSet allow null values? Why and Why not?

**Answer**

With natural ordering, adding `null` throws `NullPointerException`. A custom comparator can
technically define an order for `null`, in which case a `TreeSet` backed by that comparator may accept
it. Most APIs should avoid nullable sorted elements because every comparison path must support them.

## What are cursors in Java?

**Answer**

In Java, the term "cursor" generally refers to an object that allows traversal over the elements of a collection. Cursors are used to iterate through the elements of a collection, such as a list, set, or map. The most common types of cursors in Java are Iterator, ListIterator, and Enumeration.
- **Iterator:** Purpose: Forward traversal of a collection.
- **Methods:** hasNext(), next(), remove().
- **Example:** Iterating through a list.
- **ListIterator:** Purpose: Bidirectional traversal of a list.
- **Methods:** Inherits from Iterator, plus hasPrevious(), previous(), add(E e), set(E e).
- **Example:** Iterating forward and backward through a list.
- **Enumeration:** Purpose: Legacy interface for traversing collections like Vector and Hashtable.
- **Methods:** hasMoreElements(), nextElement().
- **Example:** Iterating through a Vector.

## What are the different types of iterators in Java?

**Answer**

- **Iterator:** Purpose: Forward traversal of a collection.
- **Methods:** hasNext(), next(), remove().
- **Applicable Collections:** All collections implementing Collection.
- **ListIterator:** Purpose: Bidirectional traversal of a list.
- **Methods:** Inherits from Iterator, plus hasPrevious(), previous(), nextIndex(), previousIndex(), set(E e), add(E e).
- **Applicable Collections:** Lists.
- **Enumeration:** Purpose: Legacy interface for traversing collections.
- **Methods:** hasMoreElements(), nextElement().
- **Applicable Collections:** Legacy collections like Vector and Hashtable.
- **Spliterator:** Purpose: Designed for parallel processing and partitioning elements.
- **Methods:** tryAdvance(Consumer<? super T> action), trySplit(), estimateSize(), characteristics().
- **Applicable Collections:** All collections implementing Collection.

## What is the difference between Iterator and ListIterator?

**Answer**

- **Supported Collections:** Iterator: Can be used with any collection that implements the Collection interface.
- **ListIterator:** Can be used only with lists.
- **Traversal Direction:** Iterator: Supports only forward traversal.
- **ListIterator:** Supports both forward and backward traversal.
- **Methods:** Iterator: hasNext(), next(), remove().
- **ListIterator:** hasNext(), next(), hasPrevious(), previous(), nextIndex(), previousIndex(), remove(), set(E e), add(E e).
- **Capabilities:** Iterator: Does not support bidirectional traversal or adding elements during iteration. Can remove elements during iteration.
- **ListIterator:** Supports bidirectional traversal, adding elements, removing elements, and replacing elements during iteration.

## In what situations will you prefer a ListIterator over Iterator?

**Answer**

- **Bidirectional Traversal:** Use ListIterator when you need to traverse the list in both forward and backward directions.
- **Modifying the List During Iteration:** Use ListIterator when you need to add, remove, or replace elements in the list while iterating.
- **Accessing Index Information:** Use ListIterator when you need to know the index of the elements while iterating.
- **Navigating Subsections of a List:** Use ListIterator when you need to navigate and manipulate specific subsections of a list.

## How does a Hashmap internally work?

**Answer**

- **Hashing:** Converts a key into an integer value (hash code) to determine the index in the bucket array.
- **Buckets:** Array elements that store linked lists (or trees) of entries with the same hash code.
- **Entries:** Key-value pairs stored in the HashMap, each containing a reference to the next entry in the same bucket.
- **Collision Handling:** Uses separate chaining (linked lists) and tree-based structures (in Java 8 and later) to handle collisions.
- **Initialization:** records sizing parameters; current implementations allocate the bucket table
  lazily on first insertion.
- **Adding an Entry:** Calculates the hash code, determines the bucket index, and adds the entry to the bucket.
- **Retrieving an Entry:** Calculates the hash code, determines the bucket index, and retrieves the entry from the bucket.
- **Resizing:** Doubles the capacity and rehashes all entries when the load factor threshold is exceeded.

## What is Load Factor in HashMap?

**Answer**

- **Load Factor:** A measure that determines when to resize the HashMap. The default load factor is 0.75.
- **Default Initial Capacity:** The initial number of buckets in the HashMap. The default initial capacity is 16.
- **Resizing:** When the number of entries exceeds the product of the load factor and the current capacity, the HashMap is resized to maintain performance.

## What would happened if I reduce the value of load factor

**Answer**

- **Increased Space Usage:** A lower load factor means that the HashMap will have more empty slots, leading to increased memory usage.
For example, if you set the load factor to 0.5, the HashMap will resize when it is half full, resulting in more frequent resizing and more empty slots.
- **Reduced Collisions:** With a lower load factor, the HashMap will have fewer entries per bucket, reducing the likelihood of collisions.
This can improve the performance of get, put, and remove operations, as there will be fewer entries to search through in each bucket.
- **More Frequent Resizing:** A lower load factor will cause the HashMap to resize more frequently, as it will reach its threshold more quickly.
Resizing involves rehashing all the entries, which is a time-consuming operation. Frequent resizing can degrade performance, especially if the HashMap is large.
- **Improved Lookup Performance:** With fewer collisions, the average time complexity for get, put, and remove operations can approach O(1) more closely.
This can lead to improved performance for applications with high read/write operations.

## Explain the internal working of hashmap.

**Answer**

- **Hashing:** Converts keys into hash codes to index into an array.
- **Buckets:** Array of linked lists or trees to store key-value pairs.
- **Collision Handling:** Uses separate chaining and treeification to handle collisions.
- **Insertion:** Calculates hash, determines index, and inserts the node.
- **Retrieval:** Calculates hash, determines index, and searches for the node.
- **Deletion:** Calculates hash, determines index, and removes the node.
- **Resizing:** Doubles the array size and rehashes entries when the load factor is exceeded.

## How do you implement `hashCode` for an employee?

**Answer**

Use the same fields used by `equals`, and do not include mutable fields when the object may be used as
a hash-map key while those fields can change.

```java
@Override
public int hashCode() {
    return Objects.hash(id, name, department, salary);
}
```

## What is the difference between treemap and hashmap?

**Answer**

- **Ordering:** TreeMap: Maintains sorted order of keys.
- **HashMap:** No order of entries.
- **Performance:** TreeMap: O(log n) for get, put, remove operations.
- **HashMap:** O(1) average for get, put, remove operations (O(n) in worst case).
- **Null Keys:** TreeMap: Does not allow null keys.
- **HashMap:** Allows one null key.
- **Use Case:** TreeMap: Suitable for scenarios where sorted order of keys is required.
- **HashMap:** Suitable for scenarios where fast access and insertion are required, and ordering is not important.

## What is the return Type of put method?

**Answer**

The put method is commonly used in Java's Map interface to insert a key-value pair into the map.
The return type of the put method is V, which represents the type of the values stored in the map.
- **Return Type:** V: The previous value associated with the key, or null if there was no mapping for the key.

## What was the enhancement done in Hashmap in Java 8

**Answer**

Improved Collision Handling with Balanced Trees:
Linked lists are converted to red-black trees when the number of entries in a bucket exceeds a threshold (default is 8).
This improves the worst-case time complexity for operations from O(n) to O(log n).
- **Threshold for Treeification:** Treeify Threshold: The threshold at which a bucket's linked list is converted to a red-black tree (default is 8).
- **Untreeify Threshold:** The threshold at which a bucket's red-black tree is converted back to a linked list when the number of entries decreases (default is 6).
- **Improved Hash Function:** An improved hash function provides better distribution of keys across the hash table, reducing the likelihood of hash collisions.
- **Performance Improvements:** The combination of these enhancements results in significant performance improvements for HashMap operations, especially in scenarios with a high number of hash collisions.

## What is a synchronized Hashmap?

**Answer**

- **Synchronized HashMap:** A thread-safe version of HashMap that ensures safe concurrent access by synchronizing method calls.
- **Creation:** Use Collections.synchronizedMap() to create a synchronized map backed by a HashMap.
- **Synchronized Blocks for Iteration:** Synchronize on the map when iterating to prevent concurrent modification exceptions.
- **Performance Overhead:** Synchronization introduces performance overhead. For high-concurrency scenarios, consider using ConcurrentHashMap.
- **ConcurrentHashMap:** An alternative to Synchronized HashMap that provides better performance through finer-grained locking and concurrency optimizations.

## What is the difference between Synchronized HashMap and ConcurrentHashMap?

**Answer**

ConcurrentHashMap
- **Concurrency:** Allows concurrent read and write operations without locking the entire map.
- **Implementation:** current implementations combine volatile reads, CAS, and short synchronized
  bin-level updates. Fixed segment lock striping describes older Java releases.
- **Performance:** Higher performance in multi-threaded environments due to reduced contention.
- **Null Values:** Does not allow null keys or values.
- **Use Case:** Suitable for high-concurrency scenarios where multiple threads frequently read and write to the map.
Synchronized HashMap
- **Concurrency:** each wrapper method synchronizes on one mutex. Compound operations and iteration
  still require documented external synchronization unless one method supplies the required atomicity.
- **Locking Mechanism:** Uses a single lock for the entire map, leading to higher contention.
- **Performance:** Lower performance in multi-threaded environments due to the single lock.
- **Null Values:** Allows null keys and values.
- **Use Case:** Suitable for low-concurrency scenarios where thread safety is required but high performance is not critical.

## What is concurrentHashMap and HashTable?

**Answer**

Hashtable is a legacy class from the original Java 1.0 release that provides thread-safe operations by synchronizing all its methods. This means that only one thread can access the map at a time, ensuring thread safety but leading to significant contention and poor performance in highly concurrent environments. Due to its coarse-grained locking mechanism, Hashtable is generally suitable for single-threaded or lightly multi-threaded applications where the overhead of synchronization is minimal.
In contrast, `ConcurrentHashMap` is designed for scalable concurrent access. Current implementations
combine volatile reads, CAS, and short synchronized bin-level updates; the old segmented design
describes Java 7-era implementations. Its iterators are weakly consistent, it rejects null keys and
values, and compound updates should use `compute`, `merge`, or `putIfAbsent`.

## What is the difference between Hashmap vs ConcurrentHashMap?

**Answer**

HashMap
- **Thread Safety:** HashMap is not thread-safe. Concurrent access by multiple threads without external synchronization can lead to unpredictable behavior.
- **Performance:** Generally offers better performance in single-threaded scenarios because it does not have the overhead of synchronization.
- **Null Values:** Allows one null key and multiple null values.
- **Internal Structure:** Uses an array of linked lists (buckets) to store entries. In Java 8 and later, it uses a balanced tree (red-black tree) for buckets with a high collision rate to improve performance.
- **Use Case:** Suitable for single-threaded scenarios or when external synchronization is used to manage concurrent access.
ConcurrentHashMap
- **Thread Safety:** ConcurrentHashMap is thread-safe and designed for concurrent access. It allows multiple threads to read and write without external synchronization.
- **Performance:** optimized for concurrent access with nonblocking reads and finer-grained updates;
  current implementations do not use the old fixed segment-lock architecture.
- **Null Values:** Does not allow null keys or values. Attempting to insert a null key or value will result in a NullPointerException.
- **Internal Structure:** Uses a more complex internal structure with segments and fine-grained locking to allow concurrent access. In Java 8 and later, it uses a combination of CAS (Compare-And-Swap) operations and synchronized blocks to achieve thread safety.
- **Use Case:** Suitable for multi-threaded scenarios requiring concurrent access without the need for external synchronization

## What is the difference between identity hashmap and weak hashmap?

**Answer**

- **Comparison Method:** IdentityHashMap: Uses reference equality (==) to compare keys.
- **WeakHashMap:** Uses object equality (equals()) to compare keys.
- **Garbage Collection:** IdentityHashMap: Keys and values are strongly referenced and not affected by garbage collection.
- **WeakHashMap:** Keys are weakly referenced and can be garbage collected, leading to automatic removal of entries.
- **Use Cases:** IdentityHashMap: Suitable when you need to distinguish between different instances of the same object and use reference able equality for key comparison.
- **WeakHashMap:** Suitable when you want to manage memory more efficiently by allowing keys to be garbage collected and automatically removing entries with keys that are no longer in use.

## What would happen if 2 threads tried to update the same key in a ConcurrentHashMap?

**Answer**

Each `put` is thread-safe, but if two threads put different values for the same key, the final value
depends on which update wins; both are not merged automatically. Per-key compound operations such as
`compute`, `merge`, `replace`, and `putIfAbsent` provide documented atomic behavior.

## Why should we use immutable objects as keys in Hashmap?

**Answer**

- **Consistency of hashCode() and equals():** Immutable objects ensure that the hash code and equality comparisons remain consistent, preventing issues with key lookups in HashMap.
- **Concurrency:** immutability keeps a key's equality state stable, but it does not make an ordinary
  `HashMap` safe for concurrent access.
- **Reliable Behavior:** Using immutable objects as keys ensures predictable and reliable behavior in hash-based collections.

## How does the performance of a Hashmap change when Hash Collision increases and what can be done to handle it?

**Answer**

- **Performance Impact:** Increased hash collisions can degrade the performance of a HashMap by increasing the time complexity of search, insert, and delete operations.
- **Handling Collisions:** Separate Chaining: Uses linked lists or trees to handle collisions within buckets.
- **Treeify Bins:** Converts linked lists to balanced trees when the number of entries in a bucket exceeds a threshold.
- **Resizing:** Increases the number of buckets and rehashes entries when the load factor exceeds a threshold.
- **Best Practices:** Use a good hash function.
Choose an appropriate initial capacity.
Monitor and adjust the load factor.
Use immutable keys.
Measure before changing the load factor; correct, well-distributed `hashCode` implementations and
immutable equality fields matter more than arbitrary tuning.
