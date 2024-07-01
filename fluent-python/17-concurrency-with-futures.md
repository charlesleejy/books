## Chapter 17: Concurrency with Futures

#### Overview
- This chapter introduces the concept of concurrency using `futures` in Python.
- `futures` are a higher-level abstraction for managing concurrency, making it easier to write concurrent programs.
- The chapter covers the `concurrent.futures` module, which provides a high-level interface for asynchronously executing functions using threads or processes.

### Key Concepts

1. **Futures**
   - **Definition:** An abstraction for a value that may be available at some point in the future.
   - **Purpose:** Simplifies the management of asynchronous execution and result retrieval.
   - **Example:**
     ```python
     from concurrent.futures import Future

     def return_after_5_secs():
         import time
         time.sleep(5)
         return "Completed"

     future = Future()
     ```

2. **`concurrent.futures` Module**
   - **ThreadPoolExecutor:** Manages a pool of threads to execute calls asynchronously.
   - **ProcessPoolExecutor:** Manages a pool of processes to execute calls asynchronously.

3. **Creating and Using Futures**

1. **Creating Futures**
   - **Example:**
     ```python
     from concurrent.futures import ThreadPoolExecutor
     import time

     def sleep_and_return(seconds):
         time.sleep(seconds)
         return f"Slept for {seconds} seconds"

     executor = ThreadPoolExecutor(max_workers=3)
     future = executor.submit(sleep_and_return, 3)

     print(future)  # Output: <Future at 0x... state=pending>
     ```

2. **Waiting for Future Results**
   - **Example:**
     ```python
     result = future.result()  # Blocks until the result is available
     print(result)  # Output: Slept for 3 seconds
     ```

3. **Using Callbacks with Futures**
   - **Example:**
     ```python
     def callback(future):
         print(future.result())

     future.add_done_callback(callback)
     ```

4. **Managing Multiple Futures**

1. **Using `as_completed`**
   - **Example:**
     ```python
     from concurrent.futures import as_completed

     futures = [executor.submit(sleep_and_return, i) for i in range(5)]
     for future in as_completed(futures):
         print(future.result())
     ```

2. **Using `wait`**
   - **Example:**
     ```python
     from concurrent.futures import wait

     futures = [executor.submit(sleep_and_return, i) for i in range(5)]
     wait(futures)  # Waits for all futures to complete
     for future in futures:
         print(future.result())
     ```

### Practical Applications

1. **Downloading with Threads**
   - **Example:**
     ```python
     from concurrent.futures import ThreadPoolExecutor
     import requests

     URLs = [
         'http://www.google.com',
         'http://www.example.com',
         'http://www.python.org',
         'http://www.github.com',
     ]

     def fetch(url):
         response = requests.get(url)
         return f"{url}: {response.status_code}"

     with ThreadPoolExecutor(max_workers=4) as executor:
         futures = [executor.submit(fetch, url) for url in URLs]
         for future in as_completed(futures):
             print(future.result())
     ```

2. **Calculations with Processes**
   - **Example:**
     ```python
     from concurrent.futures import ProcessPoolExecutor

     def compute_factorial(n):
         if n == 0:
             return 1
         else:
             return n * compute_factorial(n-1)

     with ProcessPoolExecutor(max_workers=4) as executor:
         futures = [executor.submit(compute_factorial, i) for i in range(5, 10)]
         for future in as_completed(futures):
             print(future.result())
     ```

### Handling Exceptions in Futures

1. **Handling Exceptions**
   - **Example:**
     ```python
     def faulty_function():
         raise ValueError("An error occurred")

     future = executor.submit(faulty_function)
     try:
         result = future.result()
     except ValueError as e:
         print(f"Caught an exception: {e}")
     ```

2. **Checking Future State**
   - **Example:**
     ```python
     future = executor.submit(sleep_and_return, 2)
     if future.done():
         print(future.result())
     else:
         print("Future is still running")
     ```

### Using `Executor.map`

1. **Mapping Functions to Iterables**
   - **Example:**
     ```python
     results = executor.map(sleep_and_return, [1, 2, 3, 4, 5])
     for result in results:
         print(result)
     ```

### Conclusion
- Futures provide a higher-level abstraction for managing concurrency in Python, making it easier to write, manage, and reason about asynchronous code.
- The `concurrent.futures` module offers a straightforward interface for executing functions asynchronously using threads or processes.
- Practical applications of futures include downloading data from multiple URLs concurrently, performing CPU-bound calculations in parallel, and handling asynchronous tasks with callbacks.
- Understanding how to use futures, handle exceptions, and manage multiple futures can significantly enhance the efficiency and responsiveness of Python programs.

These detailed notes cover the key concepts and examples from Chapter 17 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.