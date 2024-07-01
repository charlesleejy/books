## Chapter 2: An Array of Sequences

#### Overview
- This chapter delves into Python's sequence types, which include lists, tuples, and range objects. It explores the common behaviors and operations applicable to all sequence types, emphasizing their flexibility and power in Python programming.

### Key Concepts

1. **Common Sequence Operations**
   - **Indexing:** Accessing elements by their position.
     ```python
     my_list = [1, 2, 3]
     print(my_list[0])  # Output: 1
     ```
   - **Slicing:** Extracting a part of the sequence.
     ```python
     my_list = [1, 2, 3, 4, 5]
     print(my_list[1:3])  # Output: [2, 3]
     ```
   - **Concatenation:** Combining sequences.
     ```python
     print([1, 2] + [3, 4])  # Output: [1, 2, 3, 4]
     ```
   - **Repetition:** Repeating sequences.
     ```python
     print([1, 2] * 3)  # Output: [1, 2, 1, 2, 1, 2]
     ```
   - **Membership:** Checking if an element exists in a sequence.
     ```python
     print(3 in [1, 2, 3])  # Output: True
     ```
   - **Length:** Getting the number of elements.
     ```python
     print(len([1, 2, 3]))  # Output: 3
     ```

2. **List Comprehensions and Generator Expressions**
   - **List Comprehensions:** A concise way to create lists.
     ```python
     squares = [x * x for x in range(10)]
     print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
     ```
   - **Generator Expressions:** Similar to list comprehensions but produce items one at a time using lazy evaluation.
     ```python
     squares_gen = (x * x for x in range(10))
     print(list(squares_gen))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
     ```

3. **Tuples: Immutable Sequences**
   - **Definition:** Immutable sequences typically used to store heterogeneous data.
   - **Packing and Unpacking:**
     ```python
     t = (1, 2, 3)
     a, b, c = t
     print(a, b, c)  # Output: 1 2 3
     ```

4. **Named Tuples**
   - **Definition:** Tuples with named fields, providing a readable and self-documenting way to handle data.
   - **Example:**
     ```python
     from collections import namedtuple
     Point = namedtuple('Point', ['x', 'y'])
     p = Point(1, 2)
     print(p.x, p.y)  # Output: 1 2
     ```

5. **Slicing**
   - **Basic Slicing:**
     ```python
     my_list = [1, 2, 3, 4, 5]
     print(my_list[1:3])  # Output: [2, 3]
     ```
   - **Advanced Slicing:**
     ```python
     my_list = [1, 2, 3, 4, 5]
     print(my_list[::2])  # Output: [1, 3, 5]
     ```

6. **Assigning to Slices**
   - **Example:**
     ```python
     my_list = [1, 2, 3, 4, 5]
     my_list[1:3] = [20, 30]
     print(my_list)  # Output: [1, 20, 30, 4, 5]
     ```

7. **Using + and * with Sequences**
   - **Concatenation with `+`:**
     ```python
     print([1, 2] + [3, 4])  # Output: [1, 2, 3, 4]
     ```
   - **Repetition with `*`:**
     ```python
     print([1, 2] * 3)  # Output: [1, 2, 1, 2, 1, 2]
     ```

8. **Augmented Assignment with Sequences**
   - **Example:**
     ```python
     l = [1, 2, 3]
     l += [4, 5]
     print(l)  # Output: [1, 2, 3, 4, 5]
     ```

9. **Building Lists of Lists**
   - **Pitfall with Mutable Default Arguments:**
     ```python
     def make_list(value, size=3):
         result = []
         for _ in range(size):
             result.append(value)
         return result
     l = make_list([])
     l[0].append(10)
     print(l)  # Output: [[10], [], []]
     ```

### List Comprehensions and Generator Expressions

1. **List Comprehensions**
   - **Example:**
     ```python
     squares = [x * x for x in range(10)]
     print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
     ```

2. **Generator Expressions**
   - **Example:**
     ```python
     squares_gen = (x * x for x in range(10))
     print(list(squares_gen))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
     ```

### Tuples

1. **Tuples as Records**
   - **Definition:** Tuples can be used as immutable records to store heterogeneous data.
   - **Example:**
     ```python
     traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
     for passport in sorted(traveler_ids):
         print('%s/%s' % passport)
     # Output: BRA/CE342567 ESP/XDA205856 USA/31195855
     ```

2. **Tuple Unpacking**
   - **Example:**
     ```python
     t = (20, 8)
     latitude, longitude = t
     print(latitude, longitude)  # Output: 20 8
     ```

3. **Named Tuples**
   - **Example:**
     ```python
     from collections import namedtuple
     City = namedtuple('City', 'name country population coordinates')
     tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
     print(tokyo.population)  # Output: 36.933
     print(tokyo.coordinates)  # Output: (35.689722, 139.691667)
     ```

### Slicing

1. **Basic Slicing**
   - **Example:**
     ```python
     l = [10, 20, 30, 40, 50, 60]
     print(l[:2])  # Output: [10, 20]
     print(l[2:])  # Output: [30, 40, 50, 60]
     print(l[:3:2])  # Output: [10, 30]
     ```

2. **Assigning to Slices**
   - **Example:**
     ```python
     l = list(range(10))
     l[2:5] = [20, 30]
     print(l)  # Output: [0, 1, 20, 30, 5, 6, 7, 8, 9]
     l[2:5] = [100]
     print(l)  # Output: [0, 1, 100, 6, 7, 8, 9]
     ```

### Stride in Slicing

1. **Using Stride**
   - **Example:**
     ```python
     s = 'bicycle'
     print(s[::3])  # Output: 'bye'
     print(s[::-1])  # Output: 'elcycib'
     print(s[::-2])  # Output: 'eccb'
     ```

### Assigning to Slices

1. **List Identity and Slices**
   - **Example:**
     ```python
     l = [1, 2, 3, 4, 5]
     l[1:3] = [10, 20]
     print(l)  # Output: [1, 10, 20, 4, 5]
     ```

### Multiplying Sequences

1. **Repetition of Immutable Sequences**
   - **Example:**
     ```python
     my_list = [1, 2, 3]
     print(my_list * 3)  # Output: [1, 2, 3, 1, 2, 3