## Appendix C: Java 8: Lambdas and Streams

#### Overview
- This appendix introduces the new features introduced in Java 8, specifically lambdas and streams.
- It covers the basics of lambda expressions, functional interfaces, method references, and the Stream API for processing collections of data.

### Key Concepts

1. **Lambda Expressions**
   - **Definition:** A concise way to represent anonymous functions (methods without a name).
   - **Syntax:** `(parameters) -> expression` or `(parameters) -> { statements }`
   - **Purpose:** Simplifies the use of single-method interfaces (functional interfaces) and enables functional programming style.

2. **Functional Interfaces**
   - **Definition:** An interface with a single abstract method (SAM).
   - **Common Functional Interfaces:** `Runnable`, `Callable`, `Comparator`, `Function`, `Predicate`, `Consumer`, `Supplier`.
   - **Example:**
     ```java
     @FunctionalInterface
     public interface MyFunctionalInterface {
         void myMethod();
     }

     public class LambdaExample {
         public static void main(String[] args) {
             MyFunctionalInterface myFunc = () -> System.out.println("Hello, Lambda!");
             myFunc.myMethod();
         }
     }
     ```

3. **Method References**
   - **Definition:** A shorthand notation for calling a method by referring to it with the help of its name directly.
   - **Types:** 
     - Reference to a static method: `ClassName::methodName`
     - Reference to an instance method: `instance::methodName`
     - Reference to a constructor: `ClassName::new`
   - **Example:**
     ```java
     public class MethodReferenceExample {
         public static void main(String[] args) {
             // Static method reference
             Consumer<String> print = System.out::println;
             print.accept("Hello, Method Reference!");

             // Instance method reference
             String str = "Hello";
             Supplier<Integer> lengthSupplier = str::length;
             System.out.println("Length: " + lengthSupplier.get());
         }
     }
     ```

4. **Stream API**
   - **Definition:** A sequence of elements supporting sequential and parallel aggregate operations.
   - **Purpose:** Simplifies the processing of collections with a functional programming approach.
   - **Key Stream Operations:**
     - **Intermediate Operations:** Transform a stream into another stream. Examples: `filter()`, `map()`, `sorted()`.
     - **Terminal Operations:** Produce a result or side-effect. Examples: `forEach()`, `collect()`, `reduce()`.
   - **Example:**
     ```java
     import java.util.*;
     import java.util.stream.*;

     public class StreamExample {
         public static void main(String[] args) {
             List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Edward");

             // Intermediate operations: filter and map
             List<String> result = names.stream()
                 .filter(name -> name.startsWith("D"))
                 .map(String::toUpperCase)
                 .collect(Collectors.toList());

             // Terminal operation: forEach
             result.forEach(System.out::println);
         }
     }
     ```

### Detailed Breakdown

1. **Lambda Expressions in Detail**
   - **Syntax Variations:**
     ```java
     // No parameters
     () -> System.out.println("Hello, World!");

     // Single parameter
     x -> x * x;

     // Multiple parameters
     (x, y) -> x + y;

     // Multiple statements
     (x, y) -> {
         int sum = x + y;
         return sum;
     };
     ```
   - **Example with Comparator:**
     ```java
     List<String> names = Arrays.asList("Charlie", "Alice", "Bob");
     Collections.sort(names, (a, b) -> a.compareTo(b));
     System.out.println(names);
     ```

2. **Functional Interfaces and Lambda Expressions**
   - **Built-in Functional Interfaces:**
     ```java
     import java.util.function.*;

     public class FunctionalInterfacesExample {
         public static void main(String[] args) {
             // Predicate
             Predicate<String> isEmpty = String::isEmpty;
             System.out.println(isEmpty.test(""));

             // Function
             Function<String, Integer> length = String::length;
             System.out.println(length.apply("Hello"));

             // Consumer
             Consumer<String> printer = System.out::println;
             printer.accept("Hello, Consumer!");

             // Supplier
             Supplier<String> supplier = () -> "Hello, Supplier!";
             System.out.println(supplier.get());
         }
     }
     ```

3. **Using Method References**
   - **Static Method Reference:**
     ```java
     Consumer<String> print = System.out::println;
     print.accept("Hello, Method Reference!");
     ```

   - **Instance Method Reference:**
     ```java
     String str = "Hello";
     Supplier<Integer> lengthSupplier = str::length;
     System.out.println("Length: " + lengthSupplier.get());
     ```

   - **Constructor Reference:**
     ```java
     Supplier<List<String>> listSupplier = ArrayList::new;
     List<String> list = listSupplier.get();
     list.add("Hello");
     System.out.println(list);
     ```

4. **Stream API in Detail**
   - **Creating Streams:**
     ```java
     List<String> list = Arrays.asList("a", "b", "c");
     Stream<String> stream = list.stream();
     ```

   - **Intermediate Operations:**
     ```java
     List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Edward");

     List<String> result = names.stream()
         .filter(name -> name.startsWith("D"))
         .map(String::toUpperCase)
         .collect(Collectors.toList());
     ```

   - **Terminal Operations:**
     ```java
     names.stream().forEach(System.out::println);

     long count = names.stream().filter(name -> name.length() > 3).count();
     System.out.println("Count: " + count);
     ```

### Practical Examples

1. **Filtering and Mapping a List**
   - **Source Code:**
     ```java
     import java.util.*;
     import java.util.stream.*;

     public class FilterMapExample {
         public static void main(String[] args) {
             List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Edward");

             List<String> result = names.stream()
                 .filter(name -> name.startsWith("D"))
                 .map(String::toUpperCase)
                 .collect(Collectors.toList());

             result.forEach(System.out::println);
         }
     }
     ```

2. **Using Collectors**
   - **Source Code:**
     ```java
     import java.util.*;
     import java.util.stream.*;
     import java.util.function.*;

     public class CollectorsExample {
         public static void main(String[] args) {
             List<Person> people = Arrays.asList(
                 new Person("John", 25),
                 new Person("Jane", 30),
                 new Person("Jack", 20)
             );

             // Collect names to a list
             List<String> names = people.stream()
                 .map(Person::getName)
                 .collect(Collectors.toList());
             System.out.println(names);

             // Group by age
             Map<Integer, List<Person>> peopleByAge = people.stream()
                 .collect(Collectors.groupingBy(Person::getAge));
             System.out.println(peopleByAge);

             // Summarizing age
             IntSummaryStatistics ageSummary = people.stream()
                 .collect(Collectors.summarizingInt(Person::getAge));
             System.out.println(ageSummary);
         }
     }

     class Person {
         private String name;
         private int age;

         public Person(String name, int age) {
             this.name = name;
             this.age = age;
         }

         public String getName() {
             return name;
         }

         public int getAge() {
             return age;
         }

         @Override
         public String toString() {
             return name + " (" + age + ")";
         }
     }
     ```

### Key Points to Remember

- **Lambdas:** Provide a concise way to represent anonymous functions and are used extensively in functional programming.
- **Functional Interfaces:** Interfaces with a single abstract method, which can be implemented using lambda expressions or method references.
- **Method References:** Provide a shorthand way to refer to methods and constructors.
- **Stream API:** Simplifies the processing of collections using a functional programming approach, with powerful operations like `filter`, `map`, and `collect`.

### Summary

- **Java 8 Enhancements:** Introduces lambdas and the Stream API, bringing functional programming capabilities to Java.
- **Lambdas and Functional Interfaces:** Enable concise and readable code for single-method implementations.
- **Stream API:** Provides a powerful and flexible way to process collections, making data manipulation easier and more intuitive.

These detailed notes provide an overview and breakdown of the key concepts and examples from Appendix C of "Head First Java" by Kathy Sierra and Bert Bates. For more in-depth explanations and additional exercises, refer to the book directly.