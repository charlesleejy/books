## Chapter 18: Concurrency with `asyncio`

#### Overview
- This chapter introduces the `asyncio` library in Python, which is used for writing concurrent code using the `async`/`await` syntax.
- `asyncio` provides a framework for asynchronous programming by enabling concurrent execution of I/O-bound tasks, event loops, coroutines, tasks, and futures.

### Key Concepts

1. **Event Loop**
   - **Definition:** The core of `asyncio`, managing and dispatching events and tasks.
   - **Purpose:** Continuously runs, executing tasks, and handling I/O operations asynchronously.
   - **Example:**
     ```python
     import asyncio

     async def main():
         print("Hello")
         await asyncio.sleep(1)
         print("World")

     asyncio.run(main())
     ```

2. **Coroutines**
   - **Definition:** Functions defined with `async def`, which can use `await` to pause their execution until the awaited task completes.
   - **Example:**
     ```python
     async def coroutine_example():
         print("Start coroutine")
         await asyncio.sleep(1)
         print("End coroutine")

     asyncio.run(coroutine_example())
     ```

3. **Tasks**
   - **Definition:** A way to schedule coroutines concurrently.
   - **Purpose:** Allow multiple coroutines to run simultaneously.
   - **Example:**
     ```python
     async def task_example(name, delay):
         await asyncio.sleep(delay)
         print(f"Task {name} completed")

     async def main():
         task1 = asyncio.create_task(task_example("A", 2))
         task2 = asyncio.create_task(task_example("B", 1))
         await task1
         await task2

     asyncio.run(main())
     ```

### Asyncio Fundamentals

1. **Creating and Running Coroutines**
   - **Example:**
     ```python
     async def say_hello():
         print("Hello, Asyncio!")

     asyncio.run(say_hello())
     ```

2. **Using `await`**
   - **Purpose:** Pauses the coroutine until the awaited task completes.
   - **Example:**
     ```python
     async def count_down(n):
         while n > 0:
             print(n)
             await asyncio.sleep(1)
             n -= 1

     asyncio.run(count_down(3))
     ```

3. **Scheduling Tasks with `asyncio.create_task`**
   - **Purpose:** Schedule the execution of a coroutine concurrently.
   - **Example:**
     ```python
     async def count(name, n):
         for i in range(n):
             print(f"{name} - {i}")
             await asyncio.sleep(1)

     async def main():
         task1 = asyncio.create_task(count("Task1", 3))
         task2 = asyncio.create_task(count("Task2", 2))
         await task1
         await task2

     asyncio.run(main())
     ```

### Practical Examples

1. **Concurrent Web Requests**
   - **Example:**
     ```python
     import asyncio
     import aiohttp

     async def fetch(url):
         async with aiohttp.ClientSession() as session:
             async with session.get(url) as response:
                 return await response.text()

     async def main():
         urls = [
             'http://www.google.com',
             'http://www.example.com',
             'http://www.python.org',
             'http://www.github.com',
         ]
         tasks = [asyncio.create_task(fetch(url)) for url in urls]
         results = await asyncio.gather(*tasks)
         for result in results:
             print(result)

     asyncio.run(main())
     ```

2. **Producer-Consumer Pattern**
   - **Example:**
     ```python
     import asyncio
     import random

     async def producer(queue, n):
         for _ in range(n):
             item = random.randint(0, 10)
             await queue.put(item)
             print(f'Produced {item}')
             await asyncio.sleep(random.random())

     async def consumer(queue):
         while True:
             item = await queue.get()
             print(f'Consumed {item}')
             queue.task_done()

     async def main():
         queue = asyncio.Queue()
         producer_task = asyncio.create_task(producer(queue, 5))
         consumer_task = asyncio.create_task(consumer(queue))
         await producer_task
         await queue.join()
         consumer_task.cancel()

     asyncio.run(main())
     ```

### Error Handling in Asyncio

1. **Handling Exceptions in Coroutines**
   - **Example:**
     ```python
     async def faulty_coroutine():
         raise ValueError("Something went wrong")

     async def main():
         try:
             await faulty_coroutine()
         except ValueError as e:
             print(f"Caught an exception: {e}")

     asyncio.run(main())
     ```

2. **Handling Exceptions in Tasks**
   - **Example:**
     ```python
     async def faulty_task():
         raise ValueError("Something went wrong")

     async def main():
         task = asyncio.create_task(faulty_task())
         try:
             await task
         except ValueError as e:
             print(f"Caught an exception: {e}")

     asyncio.run(main())
     ```

### Advanced Asyncio Features

1. **Timeouts with `asyncio.wait_for`**
   - **Example:**
     ```python
     async def long_running_task():
         await asyncio.sleep(10)

     async def main():
         try:
             await asyncio.wait_for(long_running_task(), timeout=5)
         except asyncio.TimeoutError:
             print("Task timed out")

     asyncio.run(main())
     ```

2. **Using `asyncio.gather` for Parallel Execution**
   - **Example:**
     ```python
     async def task(name, delay):
         await asyncio.sleep(delay)
         return f"Task {name} completed"

     async def main():
         results = await asyncio.gather(
             task("A", 2),
             task("B", 1),
             task("C", 3)
         )
         print(results)

     asyncio.run(main())
     # Output: ['Task A completed', 'Task B completed', 'Task C completed']
     ```

3. **Using `asyncio.shield` to Prevent Cancellation**
   - **Example:**
     ```python
     async def protected_task():
         await asyncio.sleep(2)
         return "Protected task completed"

     async def main():
         task = asyncio.create_task(protected_task())
         try:
             result = await asyncio.shield(task)
             print(result)
         except asyncio.CancelledError:
             print("Task was cancelled")

     asyncio.run(main())
     ```

### Conclusion
- `asyncio` provides a powerful framework for writing concurrent code using the `async`/`await` syntax.
- Understanding the event loop, coroutines, tasks, and futures is essential for effectively using `asyncio`.
- Practical applications of `asyncio` include handling concurrent web requests, implementing producer-consumer patterns, and managing timeouts and cancellations.
- Leveraging `asyncio` can significantly improve the efficiency and responsiveness of I/O-bound applications in Python.

These detailed notes cover the key concepts and examples from Chapter 18 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.