## Chapter 10: Numbers Matter: Math, Formatting, Wrappers, and Statics

#### Overview
- This chapter delves into Java's handling of numbers, including arithmetic operations, number formatting, wrapper classes, and static members.
- It explains how to perform mathematical calculations, format numbers, and use static methods and fields.

### Key Concepts

1. **Arithmetic Operations**
   - **Basic Operations:** Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and modulus (`%`).
   - **Order of Operations:** Follows standard mathematical precedence (PEMDAS/BODMAS).

2. **Math Class**
   - **Purpose:** Provides methods for performing basic numeric operations such as exponentiation, square root, and trigonometric functions.
   - **Common Methods:**
     - `Math.abs()`: Returns the absolute value.
     - `Math.max()`: Returns the maximum of two values.
     - `Math.min()`: Returns the minimum of two values.
     - `Math.pow()`: Returns the value of the first argument raised to the power of the second argument.
     - `Math.sqrt()`: Returns the square root of a value.
     - `Math.random()`: Returns a random double value between 0.0 and 1.0.
   - **Example:**
     ```java
     public class MathExample {
         public static void main(String[] args) {
             double a = 25;
             double b = 3;

             System.out.println("Max: " + Math.max(a, b));
             System.out.println("Min: " + Math.min(a, b));
             System.out.println("Absolute: " + Math.abs(-a));
             System.out.println("Power: " + Math.pow(a, b));
             System.out.println("Square Root: " + Math.sqrt(a));
             System.out.println("Random: " + Math.random());
         }
     }
     ```

3. **Number Formatting**
   - **Purpose:** To display numbers in a specific format, such as currency or percentage.
   - **Using `DecimalFormat`:**
     - **Example:**
       ```java
       import java.text.DecimalFormat;

       public class FormattingExample {
           public static void main(String[] args) {
               double number = 12345.6789;
               DecimalFormat df = new DecimalFormat("#,###.00");
               System.out.println("Formatted: " + df.format(number));
           }
       }
       ```
   - **Using `NumberFormat`:**
     - **Example:**
       ```java
       import java.text.NumberFormat;
       import java.util.Locale;

       public class NumberFormatExample {
           public static void main(String[] args) {
               double currency = 12345.6789;
               NumberFormat currencyFormatter = NumberFormat.getCurrencyInstance(Locale.US);
               System.out.println("Currency: " + currencyFormatter.format(currency));

               double percentage = 0.75;
               NumberFormat percentFormatter = NumberFormat.getPercentInstance();
               percentFormatter.setMinimumFractionDigits(2);
               System.out.println("Percentage: " + percentFormatter.format(percentage));
           }
       }
       ```

4. **Wrapper Classes**
   - **Purpose:** Provide a way to use primitive data types as objects.
   - **Common Wrapper Classes:** `Integer`, `Double`, `Float`, `Long`, `Short`, `Byte`, `Character`, `Boolean`.
   - **Boxing and Unboxing:**
     - **Boxing:** Converting a primitive type into a corresponding wrapper object.
     - **Unboxing:** Converting a wrapper object back into a primitive type.
   - **Example:**
     ```java
     public class WrapperExample {
         public static void main(String[] args) {
             int a = 10;
             Integer aWrapper = Integer.valueOf(a); // Boxing
             int b = aWrapper.intValue(); // Unboxing

             System.out.println("Primitive: " + a);
             System.out.println("Wrapper: " + aWrapper);
             System.out.println("Unboxed: " + b);
         }
     }
     ```

5. **Static Members**
   - **Definition:** Static methods and fields belong to the class rather than any instance of the class.
   - **Purpose:** Useful for defining utility methods and constants.
   - **Static Methods:**
     - Can be called without creating an instance of the class.
     - Cannot access instance variables or methods directly.
   - **Static Fields:**
     - Shared among all instances of the class.
     - Example of a static utility class:
       ```java
       public class MathUtils {
           public static final double PI = 3.14159;

           public static int add(int a, int b) {
               return a + b;
           }

           public static double circumference(double radius) {
               return 2 * PI * radius;
           }
       }

       public class StaticExample {
           public static void main(String[] args) {
               System.out.println("PI: " + MathUtils.PI);
               System.out.println("Addition: " + MathUtils.add(5, 10));
               System.out.println("Circumference: " + MathUtils.circumference(7));
           }
       }
       ```

### Practical Examples

1. **Using Math Class**
   - **Source Code:**
     ```java
     public class MathDemo {
         public static void main(String[] args) {
             double value1 = -4.5;
             double value2 = 16.0;
             double value3 = 2.0;
             double value4 = 3.0;

             System.out.println("Absolute: " + Math.abs(value1));
             System.out.println("Square Root: " + Math.sqrt(value2));
             System.out.println("Power: " + Math.pow(value3, value4));
             System.out.println("Random: " + Math.random());
         }
     }
     ```
   - **Output:**
     ```
     Absolute: 4.5
     Square Root: 4.0
     Power: 8.0
     Random: 0.123456789 (example output, will vary)
     ```

2. **Number Formatting Example**
   - **Source Code:**
     ```java
     import java.text.DecimalFormat;

     public class DecimalFormatExample {
         public static void main(String[] args) {
             double num = 1234567.89;
             DecimalFormat formatter = new DecimalFormat("#,###.00");
             System.out.println("Formatted number: " + formatter.format(num));
         }
     }
     ```
   - **Output:**
     ```
     Formatted number: 1,234,567.89
     ```

3. **Wrapper Class Example**
   - **Source Code:**
     ```java
     public class WrapperClassDemo {
         public static void main(String[] args) {
             int primitiveInt = 42;
             Integer wrappedInt = Integer.valueOf(primitiveInt); // Boxing
             int unwrappedInt = wrappedInt.intValue(); // Unboxing

             System.out.println("Primitive: " + primitiveInt);
             System.out.println("Wrapped: " + wrappedInt);
             System.out.println("Unwrapped: " + unwrappedInt);
         }
     }
     ```
   - **Output:**
     ```
     Primitive: 42
     Wrapped: 42
     Unwrapped: 42
     ```

4. **Static Members Example**
   - **Source Code:**
     ```java
     public class Calculator {
         public static final double PI = 3.14159;

         public static int add(int a, int b) {
             return a + b;
         }

         public static double calculateCircleArea(double radius) {
             return PI * radius * radius;
         }
     }

     public class StaticMembersExample {
         public static void main(String[] args) {
             System.out.println("PI: " + Calculator.PI);
             System.out.println("Addition: " + Calculator.add(10, 20));
             System.out.println("Circle Area: " + Calculator.calculateCircleArea(5));
         }
     }
     ```
   - **Output:**
     ```
     PI: 3.14159
     Addition: 30
     Circle Area: 78.53975
     ```

### Key Points to Remember

- **Arithmetic Operations:** Understand basic operations and their precedence.
- **Math Class:** Utilize static methods for mathematical calculations.
- **Number Formatting:** Use `DecimalFormat` and `NumberFormat` for custom number displays.
- **Wrapper Classes:** Convert between primitives and objects for more flexible operations.
- **Static Members:** Use static fields and methods for shared constants and utility functions.

### Summary

- **Arithmetic Operations:** Essential for performing calculations.
- **Math Class:** Provides useful methods for advanced mathematical operations.
- **Number Formatting:** Crucial for displaying numbers in a readable and meaningful format.
- **Wrapper Classes:** Bridge the gap between primitive types and object-oriented programming.
- **Static Members:** Offer a way to define constants and utility methods that do not depend on instance variables.

These detailed notes provide an overview and breakdown of the key concepts and examples from Chapter 10 of "Head First Java" by Kathy Sierra and Bert Bates. For more in-depth explanations and additional exercises, refer to the book directly.