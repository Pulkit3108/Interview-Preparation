# Java Coding Exercises

Stream, collection, object-model, exception, and concurrency exercises.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## How do you create employees from a map of IDs to basic information?

**Answer**

Iterate over the entries so both the employee ID and its associated information are available.

```java
Map<String, BasicInfo> basicInfoMap = new HashMap<>();
basicInfoMap.put("E001", new BasicInfo("Alice", 70000, "HR"));
basicInfoMap.put("E002", new BasicInfo("Bob", 85000, "Engineering"));
basicInfoMap.put("E003", new BasicInfo("Charlie", 60000, "Marketing"));
List<Employee> employees = new ArrayList<>();
for (Map.Entry<String, BasicInfo> entry : basicInfoMap.entrySet()) {
    String id = entry.getKey();
    BasicInfo basicInfo = entry.getValue();
    Employee employee = new Employee(
        id,
        basicInfo.getName(),
        basicInfo.getSalary(),
        basicInfo.getDepartment()
    );
    employees.add(employee);
}
employees.forEach(System.out::println);
```

## How do you find the employee with the highest salary?

**Answer**

`max` returns an `Optional` because the source list may be empty.

```java
Optional<Employee> maxSalaryEmployee = employees.stream()
    .max(Comparator.comparingDouble(Employee::getSalary));
maxSalaryEmployee.ifPresent(employee ->
    System.out.println("Employee with the highest salary: " + employee.getName())
);
```

## How do you count salespeople by city and sort the result by city?

**Answer**

Supply `TreeMap::new` to `groupingBy` so the collected keys remain in ascending order.

```java
List<Salesperson> salespeople = Arrays.asList(
        new Salesperson("Alice", "New York"),
        new Salesperson("Bob", "Los Angeles"),
        new Salesperson("Charlie", "New York"),
        new Salesperson("David", "Chicago"),
        new Salesperson("Eve", "Los Angeles")
);
Map<String, Long> cityCountMap = salespeople.stream()
    .collect(Collectors.groupingBy(
        Salesperson::getCity,
        TreeMap::new,
        Collectors.counting()
    ));
cityCountMap.forEach((city, count) -> System.out.println(city + ": " + count));
```

## How do you create a map containing the minimum and maximum integers?

**Answer**

The following form represents an empty input with `null`. In production code, returning an
`Optional`, rejecting an empty list, or using a result type is usually clearer.

```java
Integer max = numbers.stream().max(Integer::compareTo).orElse(null);
Integer min = numbers.stream().min(Integer::compareTo).orElse(null);
Map<String, Integer> resultMap = new HashMap<>();
resultMap.put("MAX", max);
resultMap.put("MIN", min);
resultMap.forEach((key, value) -> System.out.println(key + ": " + value));
```

## How do you sort employees by age?

**Answer**

Use a comparator that expresses the field being sorted.

```java
List<Employee> employees = Arrays.asList(
    new Employee("Alice", 30),
    new Employee("Bob", 25),
    new Employee("Charlie", 35),
    new Employee("David", 28)
);
List<Employee> sortedEmployees = employees.stream()
    .sorted(Comparator.comparingInt(Employee::getAge))
    .toList();
sortedEmployees.forEach(System.out::println);
```

## How do you remove duplicate strings with the Stream API?

**Answer**

`distinct` keeps the first occurrence of each value according to `equals` and preserves encounter
order for an ordered stream.

```java
List<String> strings = Arrays.asList("apple", "banana", "apple", "orange", "banana", "grape");
List<String> uniqueStrings = strings.stream()
    .distinct()
    .toList();
```

## How do you find the student with the highest average score?

**Answer**

Each row contains a name followed by one or more integer scores. A student may appear in multiple
rows. Accumulate the total and count per student, then choose the highest average and use the name as
the tie-breaker.

```java
public static String findStudentWithHighestAverage(String[][] scores) {
    Map<String, int[]> studentScores = new HashMap<>();
    for (String[] scoreEntry : scores) {
        String name = scoreEntry[0];
        int[] scoreData = studentScores.getOrDefault(name, new int[2]);
        for (int i = 1; i < scoreEntry.length; i++) {
            scoreData[0] += Integer.parseInt(scoreEntry[i]);
            scoreData[1]++;
        }
        studentScores.put(name, scoreData);
    }
    String topStudent = null;
    double highestAverage = Double.NEGATIVE_INFINITY;
    for (Map.Entry<String, int[]> entry : studentScores.entrySet()) {
        String name = entry.getKey();
        int[] scoreData = entry.getValue();
        double average = (double) scoreData[0] / scoreData[1];
        if (average > highestAverage
                || (Double.compare(average, highestAverage) == 0
                    && (topStudent == null || name.compareTo(topStudent) < 0))) {
            highestAverage = average;
            topStudent = name;
        }
    }
    return topStudent;
}
```

## How do you run-length encode a string?

**Answer**

Count consecutive equal characters and emit each character followed by its run length. Define the
empty-input behavior explicitly.

```java
public static String encodeString(String input) {
    Objects.requireNonNull(input, "input");
    if (input.isEmpty()) {
        return "";
    }

    StringBuilder encoded = new StringBuilder();
    int[] count = {1};
    IntStream.range(1, input.length())
             .forEach(i -> {
                 if (input.charAt(i) == input.charAt(i - 1)) {
                     count[0]++;
                 } else {
                     encoded.append(input.charAt(i - 1)).append(count[0]);
                     count[0] = 1;
                 }
             });
    // The loop emits completed runs; append the final run here.
    encoded.append(input.charAt(input.length() - 1)).append(count[0]);
    return encoded.toString();
}
```

## How do you find the three most frequently occurring words?

**Answer**

Count each word, then sort by descending frequency and ascending word for deterministic ties.

```java
List<String> words = Arrays.asList(
    "apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "banana", "kiwi", "kiwi", "kiwi"
);
List<Map.Entry<String, Long>> topWords = words.stream()
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
    .entrySet()
    .stream()
    .sorted(Map.Entry.<String, Long>comparingByValue().reversed()
        .thenComparing(Map.Entry.comparingByKey()))
    .limit(3)
    .toList();
```

## How do you sum the first `n` prime numbers?

**Answer**

Generate candidate integers, keep primes, limit the stream to `n`, and sum it. Validate that `n` is
non-negative before using this snippet.

```java
int n = 10;
int sum = IntStream.iterate(2, candidate -> candidate + 1)
    .filter(candidate -> IntStream.rangeClosed(2, (int) Math.sqrt(candidate))
        .allMatch(divisor -> candidate % divisor != 0))
    .limit(n)
    .sum();
```

## How do you calculate a factorial with the Stream API?

**Answer**

For a non-negative `number`, multiply the integers from 1 through that value. `long` only delays
overflow, so use `BigInteger` for larger inputs.

```java
IntStream.rangeClosed(1, number) // Create a stream of integers from 1 to the given number
         .reduce(1, (a, b) -> a * b); // Reduce the stream to calculate the product
```

## How do you merge two sorted arrays with the Stream API?

**Answer**

This concise solution sorts all values and costs `O((n + m) log(n + m))`. A two-pointer merge can
preserve the existing order in `O(n + m)` time.

```java
IntStream.concat(Arrays.stream(array1), Arrays.stream(array2))
    .sorted()
    .toArray();
```

## How do you sum the squares of the integers from 1 through `n`?

**Answer**

Map each integer to its square before applying the terminal sum operation. Use `LongStream` or
`BigInteger` when the result may exceed the `int` range.

```java
IntStream.rangeClosed(1, n) // Create a stream of numbers from 1 to n
    .map(x -> x * x)
    .sum();
```

## How do you find employees with the second-highest distinct salary?

**Answer**

First find the second-highest distinct salary, then return every employee tied at that salary.

```java
OptionalDouble secondHighestSalary = employees.stream()
    .mapToDouble(Employee::getSalary)
    .distinct()
    .boxed()
    .sorted(Comparator.reverseOrder())
    .mapToDouble(Double::doubleValue)
    .skip(1)
    .findFirst();

List<String> employeesAtThatSalary = secondHighestSalary.isEmpty()
    ? List.of()
    : employees.stream()
        .filter(e -> Double.compare(e.getSalary(), secondHighestSalary.getAsDouble()) == 0)
        .map(Employee::getName)
        .toList();
```

## Perform the following set of operations on an array.

**Answer**

1. Select even numbers
2. Multiply each of them by 2
3. Subtract 1 from each
4. Select all the numbers that are greater than 4

```java
List<Integer> result = Arrays.stream(array)
    .filter(n -> n % 2 == 0) // Select even numbers
    .map(n -> n * 2)         // Multiply each by 2
    .map(n -> n - 1)         // Subtract 1 from each
    .filter(n -> n > 4)      // Select numbers greater than 4
    .boxed()                 // Convert IntStream to Stream<Integer>
    .collect(Collectors.toList());
```

## How do you sum the distinct even values among the first `n` Fibonacci numbers?

**Answer**

The stream carries each pair of consecutive Fibonacci numbers. Mapping to the first value produces
the sequence before filtering and summing it.

```java
int sum = Stream.iterate(new int[]{0, 1}, x -> new int[] {x[1], x[0] + x[1]})
    .limit(n)
    .map(x -> x[0])
    .distinct()
    .filter(x -> x % 2 == 0)
    .mapToInt(x -> x)
    .sum();
```

## Does the raw `ArrayList<Generic>` example compile, and why?

**Answer**

No. The raw list erases the element type, so `getValue()` is seen as returning `Object`; assigning
that result directly to `int` or `String` fails. The snippet intentionally contains those errors.

```java
class Generic<T> {
    private T value;
    public Generic(T value) {
        this.value = value;
    }
    public T getValue() {
        return value;
    }
}
ArrayList<Generic> g = new ArrayList<>();
Generic<?> g1 = new Generic<>(10);
Generic<?> g2 = new Generic<>("Hello");
g.add(g1);
g.add(g2);
int i = g.get(0).getValue();
String s = g.get(1).getValue();
System.out.println(s);
System.err.println(i);
```

Use a typed collection when all elements share a type. If heterogeneous values are intentional,
model that explicitly and inspect the runtime type before casting.

## Which `drive()` implementation is invoked through the `Car` reference?

**Answer**

```java
class Automobile {
    private String drive() {
        return "Driving vehicle";
    }
}
class Car extends Automobile {
    protected String drive() {
        return "Driving car";
    }
}
public class ElectricCar extends Car {
    @Override
    public final String drive() {
        return "Driving an electric car";
    }
    public static void main(String[] wheels) {
        final Car car = new ElectricCar();
        System.out.print(car.drive());
    }
}
```

Driving an electric car.

The private method in `Automobile` is not inherited or overridden. The accessible `drive` method
declared by `Car` is overridden by `ElectricCar`, so normal dynamic dispatch selects the latter.

## Which access modifiers can the overriding `display()` method use?

**Answer**

```java
class Shape {
    protected void display() {
        System.out.println("Display-base");
    }
}
class Circle extends Shape {
    @Override
    public void display() {
        System.out.println("Display-derived");
    }
}
```

The overriding method can be `protected` or `public`; it cannot reduce the inherited method's
visibility.

## In what order do the constructors execute?

**Answer**

```java
class Base {
    public Base() {
        System.out.println("Base");
    }
}
class Derived extends Base {
    public Derived() {
        System.out.println("Derived");
    }
}
class DeriDerived extends Derived {
    public DeriDerived() {
        System.out.println("DeriDerived");
    }
}
public class Test {
    public static void main(String[] args) {
        Derived b = new DeriDerived();
    }
}
```

```text
Base
Derived
DeriDerived
```

Construction initializes the superclass portion before the subclass portion.

## Why does the constructor with two `super` calls fail to compile?

**Answer**

```java
class Base {
    public Base() {
        System.out.print("Base ");
    }
    public Base(String s) {
        System.out.print("Base: " + s);
    }
}
class Derived extends Base {
    public Derived(String s) {
        super(); // Stmt-1
        super(s); // Stmt-2
        System.out.print("Derived ");
    }
}
class Test {
    public static void main(String[] args) {
        Base base = new Derived("Hello ");
    }
}
```

The constructor does not compile because it may invoke exactly one superclass constructor and that
invocation must be its first statement. Keep `super()` for `Base Derived`, keep `super(s)` for
`Base: Hello Derived`, or remove both and let the compiler insert `super()`.

## How do you check whether a string is a palindrome?

**Answer**

Normalize the input, then compare it with its reverse. This version ignores case and non-alphanumeric
characters; decide whether that matches the interviewer's definition of a palindrome.

```java
public boolean isPalindrome(String s) {
    // Normalize the string: convert to lowercase and remove non-alphanumeric characters
    StringBuilder normalized = new StringBuilder();
    for (char c : s.toCharArray()) {
        if (Character.isLetterOrDigit(c)) {
            normalized.append(Character.toLowerCase(c));
        }
    }
    // Check if the normalized string is a palindrome
    String normalizedStr = normalized.toString();
    String reversedStr = normalized.reverse().toString();
    return normalizedStr.equals(reversedStr);
}
```

## How do you reverse each word in a string?

**Answer**

Split on whitespace, reverse each word, and join the result. The simple version below normalizes
multiple spaces to one space.

```java
public static String reverseWords(String str) {
    String[] words = str.split(" ");
    StringBuilder reversedString = new StringBuilder();
    for (String word : words) {
        StringBuilder reverseWord = new StringBuilder(word);
        reversedString.append(reverseWord.reverse().toString()).append(" ");
    }
    return reversedString.toString().trim();
}
```

## Write code to throw your own custom exception in Java.

**Answer**

```java
public class MyCustomException extends Exception {
    public MyCustomException(String message) {
        super(message);
    }
}
```

Throw the exception at the point where the violated domain condition is detected, and either handle
it or declare it to the caller.

## How can two threads print odd and even numbers in sequence?

**Answer**

Both threads share an index and wait while the next value belongs to the other thread. Every state
change calls `notifyAll` so a waiting thread can re-check the condition.

```java
public class OddEvenPrinter {
    private static final List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
    private static final Object lock = new Object();
    private static int index = 0;
    public static void main(String[] args) {
        Thread oddThread = new Thread(new OddPrinter());
        Thread evenThread = new Thread(new EvenPrinter());
        oddThread.start();
        evenThread.start();
    }
    static class OddPrinter implements Runnable {
        @Override
        public void run() {
            while (true) {
                synchronized (lock) {
                    if (index >= numbers.size()) break;
                    if (numbers.get(index) % 2 != 0) {
                        System.out.println("Odd: " + numbers.get(index));
                        index++;
                        lock.notifyAll();
                    } else {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                            return;
                        }
                    }
                }
            }
        }
    }
    static class EvenPrinter implements Runnable {
        @Override
        public void run() {
            while (true) {
                synchronized (lock) {
                    if (index >= numbers.size()) break;
                    if (numbers.get(index) % 2 == 0) {
                        System.out.println("Even: " + numbers.get(index));
                        index++;
                        lock.notifyAll();
                    } else {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                            return;
                        }
                    }
                }
            }
        }
    }
}
```

## Write a short code for a deadlock situation?

**Answer**

The two threads deliberately acquire the locks in opposite orders. Each can hold one lock while
waiting forever for the other; production code should enforce one global lock order.

```java
public class DeadlockExample {
    public static void main(String[] args) {
        final Object lock1 = new Object();
        final Object lock2 = new Object();
        Thread thread1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1: Holding lock 1...");
                pauseBriefly();
                System.out.println("Thread 1: Waiting for lock 2...");
                synchronized (lock2) {
                    System.out.println("Thread 1: Holding lock 1 & 2...");
                }
            }
        });
        Thread thread2 = new Thread(() -> {
            synchronized (lock2) {
                System.out.println("Thread 2: Holding lock 2...");
                pauseBriefly();
                System.out.println("Thread 2: Waiting for lock 1...");
                synchronized (lock1) {
                    System.out.println("Thread 2: Holding lock 1 & 2...");
                }
            }
        });
        thread1.start();
        thread2.start();
    }

    private static void pauseBriefly() {
        try {
            Thread.sleep(100);
        } catch (InterruptedException exception) {
            Thread.currentThread().interrupt();
        }
    }
}
```

## Find the top ten IP addresses from a web server log file.

**Answer**

- **A sample line from the log file:** 14716104719,GET,/index.html,10.10.10.1
- **Sample output:** RANK, IP, COUNT
1, 127.10.24.1, 18975
2, 239.19.5.1, 17497
...
10, 94.104.1.100, 2945

```java
Map<String, Integer> ipCountMap = new HashMap<>();
for (String logLine : logFile) {
    String[] fields = logLine.split(",", -1);
    if (fields.length >= 4) {
        String ip = fields[3];
        ipCountMap.merge(ip, 1, Integer::sum);
    }
}
List<Map.Entry<String, Integer>> sortedIPList = new ArrayList<>(ipCountMap.entrySet());
sortedIPList.sort((entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue()));

System.out.println("RANK, IP, COUNT");
for (int i = 0; i < Math.min(10, sortedIPList.size()); i++) {
    Map.Entry<String, Integer> entry = sortedIPList.get(i);
    System.out.println((i + 1) + ", " + entry.getKey() + ", " + entry.getValue());
}
```

Real log formats require a proper parser, malformed-line handling, and a tie-breaker if output must
be deterministic. For files larger than memory, aggregate in partitions or an external store.

## Write a short code for a counter that is increment and decremented by multiple threads?

**Answer**

Guard every read and update with the same lock. An `AtomicInteger` is shorter for this single-value
case, while a lock becomes useful when several values must change under one invariant.

```java
public class Counter {
    private int count = 0;
    private final ReentrantLock lock = new ReentrantLock();
    public void increment() {
        lock.lock();
        try {
            count++;
            System.out.println("Incremented to: " + count);
        } finally {
            lock.unlock();
        }
    }
    public void decrement() {
        lock.lock();
        try {
            count--;
            System.out.println("Decremented to: " + count);
        } finally {
            lock.unlock();
        }
    }
    public int getCount() {
        lock.lock();
        try {
            return count;
        } finally {
            lock.unlock();
        }
    }
    public static void main(String[] args) {
        Counter counter = new Counter();
        Runnable incrementTask = () -> {
            for (int i = 0; i < 10; i++) {
                counter.increment();
                try {
                    Thread.sleep(50); // Simulate some work
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        };
        Runnable decrementTask = () -> {
            for (int i = 0; i < 10; i++) {
                counter.decrement();
                try {
                    Thread.sleep(50); // Simulate some work
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        };
        Thread incrementThread1 = new Thread(incrementTask);
        Thread incrementThread2 = new Thread(incrementTask);
        Thread decrementThread1 = new Thread(decrementTask);
        Thread decrementThread2 = new Thread(decrementTask);
        incrementThread1.start();
        incrementThread2.start();
        decrementThread1.start();
        decrementThread2.start();
        try {
            incrementThread1.join();
            incrementThread2.join();
            decrementThread1.join();
            decrementThread2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Final count: " + counter.getCount());
    }
}
```

## How do you give employees earning less than 5,000 a 10% raise?

**Answer**

This mutates the existing employee objects. For immutable domain objects, map qualifying employees
to updated copies instead.

```java
employees.stream()
    .filter(employee -> employee.getSalary() < 5_000)
    .forEach(employee -> employee.setSalary(employee.getSalary() * 1.10));
```

## How do you flatten a list by one level?

**Answer**

`flatMap` replaces each nested list with its stream of elements.


```java
List<Integer> flatList = nestedList.stream()
    .flatMap(List::stream)
    .toList();
```

## How do you recursively flatten an arbitrarily nested list?

**Answer**

Use recursion when elements may themselves contain lists. This returns `Object` values because a
heterogeneous nested input has no more specific safe element type.

```java
public static List<Object> flatten(List<?> nestedList) {
    return nestedList.stream()
        .flatMap(element -> element instanceof List<?> nested
            ? flatten(nested).stream()
            : Stream.of(element))
        .toList();
}
```

## Which overloaded method is selected for a `null` argument?

**Answer**

```java
static void choose(String value) {}
static void choose(Integer value) {}

static void select(String value) {}
static void select(Object value) {}

choose(null); // Does not compile: String and Integer are unrelated.
select(null); // Calls select(String), the more specific overload.
```

`null` can match any reference type. Overload resolution selects the most specific applicable method;
if two applicable parameter types are unrelated, the call is ambiguous.
