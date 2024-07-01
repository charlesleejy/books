## Chapter 7: Function Decorators and Closures

#### Overview
- This chapter explains the concept of decorators and closures in Python, showing how they can be used to enhance and extend the behavior of functions and methods without modifying their actual code.
- Decorators provide a way to wrap another function to extend its behavior.
- Closures allow functions to capture and carry some of the scope in which they were created.

### Key Concepts

1. **Decorators**
   - **Definition:** A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
   - **Syntax:** Using the `@decorator_name` syntax above a function definition.

2. **Basic Decorator Example**
   - **Example:**
     ```python
     def my_decorator(func):
         def wrapper():
             print("Something is happening before the function is called.")
             func()
             print("Something is happening after the function is called.")
         return wrapper

     @my_decorator
     def say_hello():
         print("Hello!")

     say_hello()
     # Output:
     # Something is happening before the function is called.
     # Hello!
     # Something is happening after the function is called.
     ```

3. **Decorator Functions in Detail**
   - **Wrapper Functions:** The inner function that wraps the original function.
   - **Returning the Wrapper:** The decorator function must return the wrapper function.
   - **Example:**
     ```python
     def my_decorator(func):
         def wrapper():
             print("Before calling the function.")
             func()
             print("After calling the function.")
         return wrapper
     ```

4. **Applying Multiple Decorators**
   - **Example:**
     ```python
     def bold_decorator(func):
         def wrapper():
             return "<b>" + func() + "</b>"
         return wrapper

     def italic_decorator(func):
         def wrapper():
             return "<i>" + func() + "</i>"
         return wrapper

     @bold_decorator
     @italic_decorator
     def text():
         return "Hello"

     print(text())  # Output: <b><i>Hello</i></b>
     ```

5. **Function Arguments in Decorators**
   - **Example:**
     ```python
     def my_decorator(func):
         def wrapper(*args, **kwargs):
             print("Before calling the function.")
             result = func(*args, **kwargs)
             print("After calling the function.")
             return result
         return wrapper

     @my_decorator
     def greet(name):
         return f"Hello, {name}!"

     print(greet("Alice"))
     # Output:
     # Before calling the function.
     # After calling the function.
     # Hello, Alice!
     ```

6. **Preserving Function Metadata**
   - **Using `functools.wraps`:** Preserves the original function’s metadata.
   - **Example:**
     ```python
     import functools

     def my_decorator(func):
         @functools.wraps(func)
         def wrapper(*args, **kwargs):
             print("Before calling the function.")
             result = func(*args, **kwargs)
             print("After calling the function.")
             return result
         return wrapper

     @my_decorator
     def greet(name):
         return f"Hello, {name}!"

     print(greet.__name__)  # Output: greet
     ```

### Closures

1. **Definition of Closures**
   - **Closure:** A function with an extended scope that encompasses non-global variables referenced in the body of the function but not defined there.

2. **Creating a Closure**
   - **Example:**
     ```python
     def make_multiplier(n):
         def multiplier(x):
             return x * n
         return multiplier

     times3 = make_multiplier(3)
     print(times3(10))  # Output: 30
     ```

3. **Inspecting a Closure**
   - **Attributes:**
     - `__code__.co_freevars`: Variables referenced in the closure.
     - `__closure__`: Data structure holding the bindings for the free variables.
   - **Example:**
     ```python
     def make_multiplier(n):
         def multiplier(x):
             return x * n
         return multiplier

     times3 = make_multiplier(3)
     print(times3.__code__.co_freevars)  # Output: ('n',)
     print(times3.__closure__[0].cell_contents)  # Output: 3
     ```

### Practical Examples of Decorators and Closures

1. **Logging Decorator**
   - **Example:**
     ```python
     import functools

     def log_decorator(func):
         @functools.wraps(func)
         def wrapper(*args, **kwargs):
             print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
             result = func(*args, **kwargs)
             print(f"{func.__name__} returned {result}")
             return result
         return wrapper

     @log_decorator
     def add(a, b):
         return a + b

     print(add(2, 3))
     # Output:
     # Calling add with args=(2, 3), kwargs={}
     # add returned 5
     # 5
     ```

2. **Timing Decorator**
   - **Example:**
     ```python
     import time
     import functools

     def timer_decorator(func):
         @functools.wraps(func)
         def wrapper(*args, **kwargs):
             start = time.time()
             result = func(*args, **kwargs)
             end = time.time()
             print(f"{func.__name__} took {end - start:.4f} seconds")
             return result
         return wrapper

     @timer_decorator
     def slow_function(seconds):
         time.sleep(seconds)
         return "Done"

     print(slow_function(2))
     # Output:
     # slow_function took 2.0001 seconds
     # Done
     ```

3. **Access Control with Closures**
   - **Example:**
     ```python
     def make_averager():
         series = []

         def averager(new_value):
             series.append(new_value)
             total = sum(series)
             return total / len(series)

         return averager

     avg = make_averager()
     print(avg(10))  # Output: 10.0
     print(avg(20))  # Output: 15.0
     print(avg(30))  # Output: 20.0
     ```

### Conclusion
- Decorators and closures are powerful tools in Python that enable the extension and customization of function behavior.
- Decorators provide a clean and readable way to apply reusable patterns to functions and methods.
- Closures allow for the creation of functions that retain access to the scope in which they were created, enabling flexible and dynamic behavior.
- Understanding and using these features can lead to more modular, maintainable, and readable code.

These detailed notes cover the key concepts and examples from Chapter 7 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.