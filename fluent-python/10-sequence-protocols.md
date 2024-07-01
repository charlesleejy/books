## Chapter 10: Sequence Protocols

#### Overview
- This chapter delves into the sequence protocol in Python, exploring how to implement and extend sequence-like behavior in custom classes.
- It covers the essentials of making objects iterable, indexable, and sliceable, while adhering to Pythonic conventions.

### Key Concepts

1. **Sequence Protocol**
   - **Definition:** A protocol that allows objects to be indexed and iterated over, just like lists, tuples, and strings.
   - **Key Methods:** `__getitem__`, `__len__`, and `__contains__`.

2. **The `__getitem__` Method**
   - **Definition:** Allows an object to be indexed using square brackets.
   - **Example:**
     ```python
     class MySeq:
         def __getitem__(self, index):
             return index

     s = MySeq()
     print(s[0])  # Output: 0
     print(s[1:4])  # Output: slice(1, 4, None)
     ```

3. **The `__len__` Method**
   - **Definition:** Returns the length of the sequence.
   - **Example:**
     ```python
     class MySeq:
         def __len__(self):
             return 5

     s = MySeq()
     print(len(s))  # Output: 5
     ```

4. **The `__contains__` Method**
   - **Definition:** Implements membership test operations (`in` and `not in`).
   - **Example:**
     ```python
     class MySeq:
         def __contains__(self, item):
             return item == 1

     s = MySeq()
     print(1 in s)  # Output: True
     print(2 in s)  # Output: False
     ```

### Making a Custom Sequence

1. **Implementing a Basic Sequence**
   - **Example:**
     ```python
     import collections.abc

     class MySeq(collections.abc.Sequence):
         def __init__(self, start, stop):
             self._start = start
             self._stop = stop

         def __getitem__(self, index):
             if isinstance(index, slice):
                 return [self._start + i for i in range(*index.indices(len(self)))]
             elif isinstance(index, int):
                 if index < 0:
                     index += len(self)
                 if index < 0 or index >= len(self):
                     raise IndexError('Index out of range')
                 return self._start + index
             else:
                 raise TypeError('Invalid argument type')

         def __len__(self):
             return self._stop - self._start

     s = MySeq(0, 10)
     print(s[2:5])  # Output: [2, 3, 4]
     print(len(s))  # Output: 10
     ```

2. **Supporting Iterable Protocol**
   - **Example:**
     ```python
     class MySeq:
         def __init__(self, start, stop):
             self._start = start
             self._stop = stop

         def __getitem__(self, index):
             if isinstance(index, slice):
                 return [self._start + i for i in range(*index.indices(len(self)))]
             elif isinstance(index, int):
                 if index < 0:
                     index += len(self)
                 if index < 0 or index >= len(self):
                     raise IndexError('Index out of range')
                 return self._start + index
             else:
                 raise TypeError('Invalid argument type')

         def __len__(self):
             return self._stop - self._start

         def __iter__(self):
             return (self._start + i for i in range(len(self)))

     s = MySeq(0, 10)
     for item in s:
         print(item, end=' ')  # Output: 0 1 2 3 4 5 6 7 8 9
     ```

3. **Indexing and Slicing**
   - **Example:**
     ```python
     class MySeq:
         def __init__(self, start, stop):
             self._start = start
             self._stop = stop

         def __getitem__(self, index):
             if isinstance(index, slice):
                 return [self._start + i for i in range(*index.indices(len(self)))]
             elif isinstance(index, int):
                 if index < 0:
                     index += len(self)
                 if index < 0 or index >= len(self):
                     raise IndexError('Index out of range')
                 return self._start + index
             else:
                 raise TypeError('Invalid argument type')

         def __len__(self):
             return self._stop - self._start

     s = MySeq(0, 10)
     print(s[2:5])  # Output: [2, 3, 4]
     print(s[-1])  # Output: 9
     ```

### Special Methods for Sequence Emulation

1. **`__reversed__` Method**
   - **Definition:** Returns an iterator that yields items in reverse order.
   - **Example:**
     ```python
     class MySeq:
         def __init__(self, start, stop):
             self._start = start
             self._stop = stop

         def __getitem__(self, index):
             if isinstance(index, slice):
                 return [self._start + i for i in range(*index.indices(len(self)))]
             elif isinstance(index, int):
                 if index < 0:
                     index += len(self)
                 if index < 0 or index >= len(self):
                     raise IndexError('Index out of range')
                 return self._start + index
             else:
                 raise TypeError('Invalid argument type')

         def __len__(self):
             return self._stop - self._start

         def __reversed__(self):
             return (self._start + i for i in range(len(self) - 1, -1, -1))

     s = MySeq(0, 10)
     print(list(reversed(s)))  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
     ```

2. **`__contains__` Method**
   - **Definition:** Checks for membership.
   - **Example:**
     ```python
     class MySeq:
         def __init__(self, start, stop):
             self._start = start
             self._stop = stop

         def __getitem__(self, index):
             if isinstance(index, slice):
                 return [self._start + i for i in range(*index.indices(len(self)))]
             elif isinstance(index, int):
                 if index < 0:
                     index += len(self)
                 if index < 0 or index >= len(self):
                     raise IndexError('Index out of range')
                 return self._start + index
             else:
                 raise TypeError('Invalid argument type')

         def __len__(self):
             return self._stop - self._start

         def __contains__(self, item):
             return self._start <= item < self._stop

     s = MySeq(0, 10)
     print(5 in s)  # Output: True
     print(15 in s)  # Output: False
     ```

### Practical Applications

1. **Custom Sequence Example: Range-like Object**
   - **Example:**
     ```python
     class CustomRange:
         def __init__(self, start, stop, step=1):
             self._start = start
             self._stop = stop
             self._step = step

         def __getitem__(self, index):
             if isinstance(index, slice):
                 return [self._start + i * self._step for i in range(*index.indices(len(self)))]
             elif isinstance(index, int):
                 if index < 0:
                     index += len(self)
                 if index < 0 or index >= len(self):
                     raise IndexError('Index out of range')
                 return self._start + index * self._step
             else:
                 raise TypeError('Invalid argument type')

         def __len__(self):
             return max(0, (self._stop - self._start + self._step - 1) // self._step)

         def __iter__(self):
             return (self._start + i * self._step for i in range(len(self)))

     cr = CustomRange(0, 10, 2)
     print(list(cr))  # Output: [0, 2, 4, 6, 8]
     ```

### Conclusion
- Understanding and implementing the sequence protocol in Python enables the creation of custom objects that behave like built-in sequences.
- Key methods like `__getitem__`, `__len__`, and `__contains__` are essential for supporting indexing, slicing, iteration, and membership tests.
- By adhering to the sequence protocol, custom objects can seamlessly integrate with Python’s idiomatic usage patterns, providing a consistent and intuitive interface.

These detailed notes cover the key concepts and examples from Chapter 10 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.