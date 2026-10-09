# Java Coding Exercises

Stream, collection, object-model, exception, and concurrency exercises.

[Back to Java topics](java.md)

[Back to the question-bank index](../README.md)

## Create a list of Employees object from a hashmap whose key is string id and value is an basicinfo object

**Answer**

```java
Map<String, BasicInfo> basicInfoMap = new HashMap<>();
basicInfoMap.put("E001", new BasicInfo("Alice", 70000, "HR"));
basicInfoMap.put("E002", new BasicInfo("Bob", 85000, "Engineering"));
basicInfoMap.put("E003", new BasicInfo("Charlie", 60000, "Marketing"));
List<Employee> employees = new ArrayList<>();
for (Map.Entry<String, BasicInfo> entry : basicInfoMap.entrySet()) {
    String id = entry.getKey();
    BasicInfo basicInfo = entry.getValue();
    Employee employee = new Employee(id, basicInfo.getName(), basicInfo.getSalary(), basicInfo.getDepartment());
    employees.add(employee);
}
employees.forEach(System.out::println);
```

## How to find the highest salary employee?

**Answer**

```java
Optional<Employee> maxSalaryEmployee = employees.stream()
    .max((e1, e2) -> Double.compare(e1.getSalary(), e2.getSalary()));
maxSalaryEmployee.ifPresent(employee ->
    System.out.println("Employee with the highest salary: " + employee.getName())
);
```

## Create a map object from a list of salesperson object, the key of map is city and value is the count of employees in that city the map should be sorted by key in ascending order

**Answer**

```java
List<Salesperson> salespeople = Arrays.asList(
        new Salesperson("Alice", "New York"),
        new Salesperson("Bob", "Los Angeles"),
        new Salesperson("Charlie", "New York"),
        new Salesperson("David", "Chicago"),
        new Salesperson("Eve", "Los Angeles")
);
Map<String, Long> cityCountMap = salespeople.stream()
        .collect(Collectors.groupingBy(Salesperson::getCity, Collectors.counting()))
        .entrySet().stream()
        .sorted(Map.Entry.comparingByKey())
        .collect(Collectors.toMap(
                Map.Entry::getKey,
                Map.Entry::getValue,
                (oldValue, newValue) -> oldValue, LinkedHashMap::new));
cityCountMap.forEach((city, count) -> System.out.println(city + ": " + count));
```

## Create a map from the list of Integer where key is MAX and MIN String and value is max and min value of the list

**Answer**

```java
Integer max = numbers.stream().max(Integer::compareTo).orElse(null);
Integer min = numbers.stream().min(Integer::compareTo).orElse(null);
Map<String, Integer> resultMap = new HashMap<>();
resultMap.put("MAX", max);
resultMap.put("MIN", min);
resultMap.forEach((key, value) -> System.out.println(key + ": " + value));
```

## How will I sort a list of employees by age?

**Answer**

```java
List<Employee> employees = Arrays.asList(
    new Employee("Alice", 30),
    new Employee("Bob", 25),
    new Employee("Charlie", 35),
    new Employee("David", 28)
);
List<Employee> sortedEmployees = employees.stream()
    .sorted((e1, e2) -> Integer.compare(e1.getAge(), e2.getAge()))
    .collect(Collectors.toList());
sortedEmployees.forEach(System.out::println);
```

## Write a stream api code to remove duplicates from list of strings

**Answer**

```java
List<String> strings = Arrays.asList("apple", "banana", "apple", "orange", "banana", "grape");
List<String> uniqueStrings = strings.stream()
                                            .distinct()
                                            .collect(Collectors.toList());
```

You are given an array String scores[][] where each element scores[i] represents a student's name and their scores in various subjects. Specifically:
1. scores[i][0] is the student's name.
2. scores[i][1] to scores[i][n] are the scores , where each student may have a different number of scores.
3. Scores may be positive or negative integers.
- **Additionally:** 4. The same student may appear multiple times in the array with different scores.
5. You may assume names contain only alphabetic characters.
Write a function to find the student with the highest average score. If multiple students have the same average score, return the name that appears first in lexicographical (alphabetical) order.

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
        if (average > highestAverage || (average == highestAverage && (topStudent == null || name.compareTo(topStudent) < 0))) {
            highestAverage = average;
            topStudent = name;
        }
    }
    return topStudent;
}
```

## Write code to encode the string?

**Answer**

```java
public static String encodeString(String input) {
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
    // Append the last character and its count
    encoded.append(input.charAt(input.length() - 1)).append(count[0]);
    return encoded.toString();
}
```

## Write a program to find the top 3 most occuring words in a list of strings?

**Answer**

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

## Find the sum of first n prime numbers?

**Answer**

```java
int n = 10; // Change this value to find the sum of the first n prime numbers
int sum = IntStream.iterate(2, i -> i + 1) // Start with 2 and generate an infinite stream of integers
                .filter(number -> IntStream.rangeClosed(2, (int) Math.sqrt(number))
                .allMatch(divisor -> number % divisor != 0)) // Filter to include only prime numbers
                .limit(n) // Limit to the first n prime numbers
                .sum(); // Sum the prime numbers
```

## Find the factorial of a number using Stream API?

**Answer**

IntStream.rangeClosed(1, number) // Create a stream of integers from 1 to the given number
         .reduce(1, (a, b) -> a * b); // Reduce the stream to calculate the product

## Merge 2 sorted arrays into 1 sorted array using Stream API?

**Answer**

IntStream.concat(Arrays.stream(array1), Arrays.stream(array2))
                        .sorted()
                        .toArray();

## Using Stream API find sum of squares of n numbers?

**Answer**

IntStream.rangeClosed(1, n) // Create a stream of numbers from 1 to n
               .map(x -> x * x)   // Map each number to its square
               .sum();

## Write a code in Stream API to find the name of the employee with the second highest salary?

**Answer**

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

Generate the first `n` Fibonacci numbers, remove duplicates, keep the even values, and sum them.

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

- **Creating Generic Objects:** Generic<?> g1 = new Generic<>(10); creates a generic object with an Integer value.
Generic<?> g2 = new Generic<>("Hello"); creates a generic object with a String value.
- **Adding to ArrayList:** Both g1 and g2 are added to the ArrayList<Generic>.
- **Retrieving Values:** int i = g.get(0).getValue(); will cause a compile-time error because getValue() returns an Object, and it cannot be directly assigned to an int.
String s = g.get(1).getValue(); will cause a compile-time error for the same reason.

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

## Which access modifiers can the overriding `display()` method use?

**Answer**

```java
public class Shape {
    protected void display() {
        System.out.println("Display-base");
    }
}
public class Circle extends Shape {
    @Override
    public void display() {
        System.out.println("Display-derived");
    }
}
```

public and protected both can be used.
In Java, when you override a method in a subclass, you can only use an access modifier that is less restrictive or the same as the access modifier of the method in the superclass.

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

Base
Derived
DeriDerived
In Java, the constructor of the base class is called first, followed by the constructor of the derived class, and so on up the inheritance hierarchy.

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

Removing Stmt-1 will make the program compilable and it will print the following: Base: Hello Derived.
Removing Stmt-2 will make the program compilable and it will print the following: Base Derived.
Removing both Stmt-1 and Stmt-2 will make the program compilable and it will print the following: Base Derived.
No, the program will not be compilable if you don't remove any statement. The reason is that a constructor in Java can only call one superclass constructor, and it must be the first statement in the constructor. Having both super(); and super(s); in the constructor of the Derived class violates this rule and will result in a compilation error.
## How do you check whether a string is a palindrome?

**Answer**

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

## Write a Java Program to reverse each individual word of a given String.

**Answer**

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

- **There are two threads:** one has to print odd numbers, one has to print even numbers. It should be sequential from the common list.

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
                        lock.notify();
                    } else {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
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
                        lock.notify();
                    } else {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
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

```java
public class DeadlockExample {
    public static void main(String[] args) {
        final Object lock1 = new Object();
        final Object lock2 = new Object();
        Thread thread1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1: Holding lock 1...");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                System.out.println("Thread 1: Waiting for lock 2...");
                synchronized (lock2) {
                    System.out.println("Thread 1: Holding lock 1 & 2...");
                }
            }
        });
        Thread thread2 = new Thread(() -> {
            synchronized (lock2) {
                System.out.println("Thread 2: Holding lock 2...");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                System.out.println("Thread 2: Waiting for lock 1...");
                synchronized (lock1) {
                    System.out.println("Thread 2: Holding lock 1 & 2...");
                }
            }
        });
        thread1.start();
        thread2.start();
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
        String ip = logLine.split(",")[3];
        ipCountMap.put(ip, ipCountMap.getOrDefault(ip, 0) + 1);
}
// Step 2: Sort the IP addresses by count in descending order
List<Entry<String, Integer>> sortedIPList = new ArrayList<>(ipCountMap.entrySet());
sortedIPList.sort((entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue()));
// Step 3: Output the top ten IP addresses
System.out.println("RANK, IP, COUNT");
for (int i = 0; i < Math.min(10, sortedIPList.size()); i++) {
    Entry<String, Integer> entry = sortedIPList.get(i);
    System.out.println((i + 1) + ", " + entry.getKey() + ", " + entry.getValue());
}
```

## Write a short code for a counter that is increment and decremented by multiple threads?

**Answer**

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

## Write a short code using stream API to update the list of employees in which if salary is less than 5000 give them 10% increment?

**Answer**

employees.stream()
            .filter(employee -> employee.getSalary() < 5000)
            .forEach(employee -> employee.setSalary(employee.getSalary() * 1.10));

Use flatMap to convert an ‘n’ nested list into a single list.

```java
List<Integer> flatList = nestedList.stream()
            .flatMap(List::stream)
            .collect(Collectors.toList());
public static List<Integer> flatten(List<?> nestedList) {
    return nestedList.stream()
        .flatMap(element -> {
            if (element instanceof List) {
                return flatten((List<?>) element).stream();
            } else {
                return Arrays.asList((Integer) element).stream();
            }
        })
        .collect(Collectors.toList());
}
```

## Find Output?

**Answer**

Class A {
    AB(String)
    AB(Integer)
}
Class B {
    BA(String)
    BA(Object)
}
AB(null)
BA(null)
Calling AB(null)
When you call AB(null), the compiler cannot determine whether to call AB(String) or AB(Integer) because both are equally specific in this context. This results in a compilation error due to ambiguity.
Calling BA(null)

**When you call BA(null), the compiler chooses BA(String) over BA(Object) because String is a subclass of Object, making BA(String) more specific.**

The term "more specific" refers to the method whose parameter type is a subclass of the other possible parameter types.
