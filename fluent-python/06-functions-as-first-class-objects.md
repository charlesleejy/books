## Chapter 6: Functions as First-Class Objects

#### Overview
- This chapter explores the concept of functions as first-class objects in Python.
- It discusses how functions can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures.

### Key Concepts

1. **First-Class Functions**
   - **Definition:** Functions in Python are first-class objects, meaning they can be used as any other object (assigned to variables, passed as arguments, etc.).
   - **Example:**
     ```python
     def greet(name):
         return f"Hello, {name}!"
     
     greet_function = greet
     print(greet_function("Alice"))  # Output: Hello, Alice!
     ```

2. **Higher-Order Functions**
   - **Definition:** A function that takes one or more functions as arguments or returns a function as its result.
   - **Example:**
     ```python
     def loud(func):
         def wrapper(*args, **kwargs):
             return func(*args, **kwargs).upper()
         return wrapper
     
     def greet(name):
         return f"Hello, {name}!"
     
     loud_greet = loud(greet)
     print(loud_greet("Alice"))  # Output: HELLO, ALICE!
     ```

3. **Map, Filter, and Reduce**
   - **Map:** Applies a function to all items in an input list.
     ```python
     numbers = [1, 2, 3, 4]
     doubled = list(map(lambda x: x * 2, numbers))
     print(doubled)  # Output: [2, 4, 6, 8]
     ```
   - **Filter:** Filters items out of an input list based on a function that returns a boolean.
     ```python
     numbers = [1, 2, 3, 4]
     evens = list(filter(lambda x: x % 2 == 0, numbers))
     print(evens)  # Output: [2, 4]
     ```
   - **Reduce:** Applies a rolling computation to sequential pairs of values in a list.
     ```python
     from functools import reduce
     
     numbers = [1, 2, 3, 4]
     product = reduce(lambda x, y: x * y, numbers)
     print(product)  # Output: 24
     ```

4. **Anonymous Functions: The Lambda Syntax**
   - **Definition:** Small anonymous functions can be created with the lambda keyword.
   - **Example:**
     ```python
     add = lambda x, y: x + y
     print(add(3, 5))  # Output: 8
     ```

5. **Function Annotations**
   - **Definition:** Python provides a way to attach metadata to function arguments and return values using annotations.
   - **Example:**
     ```python
     def greet(name: str) -> str:
         return f"Hello, {name}!"
     
     print(greet.__annotations__)  # Output: {'name': <class 'str'>, 'return': <class 'str'>}
     ```

### Detailed Examples

1. **Assigning Functions to Variables**
   - **Example:**
     ```python
     def greet(name):
         return f"Hello, {name}!"
     
     greet_function = greet
     print(greet_function("Alice"))  # Output: Hello, Alice!
     ```

2. **Passing Functions as Arguments**
   - **Example:**
     ```python
     def loud(func):
         def wrapper(*args, **kwargs):
             return func(*args, **kwargs).upper()
         return wrapper
     
     def greet(name):
         return f"Hello, {name}!"
     
     loud_greet = loud(greet)
     print(loud_greet("Alice"))  # Output: HELLO, ALICE!
     ```

3. **Returning Functions from Functions**
   - **Example:**
     ```python
     def make_adder(n):
         def adder(x):
             return x + n
         return adder
     
     add_5 = make_adder(5)
     print(add_5(10))  # Output: 15
     ```

4. **Storing Functions in Data Structures**
   - **Example:**
     ```python
     def greet(name):
         return f"Hello, {name}!"
     
     def farewell(name):
         return f"Goodbye, {name}!"
     
     actions = {
         'greet': greet,
         'farewell': farewell
     }
     
     print(actions['greet']('Alice'))  # Output: Hello, Alice!
     print(actions['farewell']('Bob'))  # Output: Goodbye, Bob!
     ```

### Higher-Order Functions

1. **Using `map`**
   - **Example:**
     ```python
     numbers = [1, 2, 3, 4]
     doubled = list(map(lambda x: x * 2, numbers))
     print(doubled)  # Output: [2, 4, 6, 8]
     ```

2. **Using `filter`**
   - **Example:**
     ```python
     numbers = [1, 2, 3, 4]
     evens = list(filter(lambda x: x % 2 == 0, numbers))
     print(evens)  # Output: [2, 4]
     ```

3. **Using `reduce`**
   - **Example:**
     ```python
     from functools import reduce
     
     numbers = [1, 2, 3, 4]
     product = reduce(lambda x, y: x * y, numbers)
     print(product)  # Output: 24
     ```

### Lambda Functions

1. **Basic Lambda Function**
   - **Example:**
     ```python
     add = lambda x, y: x + y
     print(add(3, 5))  # Output: 8
     ```

2. **Using Lambdas with `map`, `filter`, `reduce`**
   - **Example:**
     ```python
     numbers = [1, 2, 3, 4]
     
     doubled = list(map(lambda x: x * 2, numbers))
     evens = list(filter(lambda x: x % 2 == 0, numbers))
     product = reduce(lambda x, y: x * y, numbers)
     
     print(doubled)  # Output: [2, 4, 6, 8]
     print(evens)  # Output: [2, 4]
     print(product)  # Output: 24
     ```

### Function Annotations

1. **Defining Function Annotations**
   - **Example:**
     ```python
     def greet(name: str) -> str:
         return f"Hello, {name}!"
     
     print(greet.__annotations__)  # Output: {'name': <class 'str'>, 'return': <class 'str'>}
     ```

2. **Using Annotations for Type Hints**
   - **Example:**
     ```python
     def add(x: int, y: int) -> int:
         return x + y
     
     print(add(3, 5))  # Output: 8
     print(add.__annotations__)  # Output: {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
     ```

### Practical Applications

1. **Decorator Functions**
   - **Example:**
     ```python
     def decorator(func):
         def wrapper(*args, **kwargs):
             print("Before the function call")
             result = func(*args, **kwargs)
             print("After the function call")
             return result
         return wrapper
     
     @decorator
     def say_hello():
         print("Hello!")
     
     say_hello()
     # Output:
     # Before the function call
     # Hello!
     # After the function call
     ```

2. **Callback Functions**
   - **Example:**
     ```python
     def process_data(data, callback):
         result = [item * 2 for item in data]
         callback(result)
     
     def print_result(result):
         print(f"Result: {result}")
     
     process_data([1, 2, 3, 4], print_result)
     # Output: Result: [2, 4, 6, 8]
     ```

### Conclusion
- Functions as first-class objects in Python provide powerful capabilities for functional programming and code reuse.
- Understanding how to leverage first-class functions, higher-order functions, lambda functions, and function annotations can lead to more concise, readable, and maintainable code.
- Decorators and callbacks are practical applications of first-class functions that enable flexible and dynamic behavior in programs.

These detailed notes cover the key concepts and examples from Chapter 6 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.