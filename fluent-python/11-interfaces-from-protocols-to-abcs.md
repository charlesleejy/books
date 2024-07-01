## Chapter 11: Interfaces: From Protocols to ABCs

#### Overview
- This chapter explores interfaces in Python, focusing on protocols and Abstract Base Classes (ABCs).
- It discusses the benefits of using interfaces, how to define and use protocols, and how ABCs can provide a formal structure for creating consistent APIs.

### Key Concepts

1. **Protocols**
   - **Definition:** Informal interfaces defined by convention rather than explicit declarations.
   - **Purpose:** Allow different objects to be used interchangeably if they implement the same set of methods and properties.

2. **Duck Typing**
   - **Definition:** A concept where the type or class of an object is less important than the methods it defines.
   - **Example:**
     ```python
     class Duck:
         def quack(self):
             print("Quack!")

     class Person:
         def quack(self):
             print("I can quack too!")

     def make_quack(duck):
         duck.quack()

     make_quack(Duck())    # Output: Quack!
     make_quack(Person())  # Output: I can quack too!
     ```

### Protocols as Interfaces

1. **Implicit Protocols**
   - **Definition:** Protocols that are followed by convention, without formal declarations.
   - **Example:**
     ```python
     class Dog:
         def bark(self):
             return "Woof!"

     class Cat:
         def meow(self):
             return "Meow!"

     class LoudDog(Dog):
         def bark(self):
             return super().bark().upper()

     def interact_with_pet(pet):
         if hasattr(pet, 'bark'):
             print(pet.bark())
         elif hasattr(pet, 'meow'):
             print(pet.meow())

     interact_with_pet(Dog())     # Output: Woof!
     interact_with_pet(Cat())     # Output: Meow!
     interact_with_pet(LoudDog()) # Output: WOOF!
     ```

2. **Explicit Protocols with `collections.abc`**
   - **Definition:** Using `collections.abc` to formally define protocols.
   - **Example:**
     ```python
     from collections.abc import Sized

     class MyCollection(Sized):
         def __init__(self, items):
             self._items = items

         def __len__(self):
             return len(self._items)

     c = MyCollection([1, 2, 3])
     print(len(c))  # Output: 3
     ```

### Abstract Base Classes (ABCs)

1. **Definition**
   - **Definition:** Abstract Base Classes provide a way to define interfaces in a formal, structured manner.
   - **Purpose:** Ensure that derived classes implement certain methods.

2. **Creating ABCs**
   - **Using `abc` Module:**
     ```python
     from abc import ABC, abstractmethod

     class MyABC(ABC):
         @abstractmethod
         def my_method(self):
             pass

     class ConcreteClass(MyABC):
         def my_method(self):
             return "Implemented!"

     obj = ConcreteClass()
     print(obj.my_method())  # Output: Implemented!
     ```

3. **Registering Virtual Subclasses**
   - **Definition:** Allows classes to be registered as implementing an ABC without inheritance.
   - **Example:**
     ```python
     from abc import ABC

     class MyABC(ABC):
         pass

     class AnotherClass:
         def method(self):
             return "Working!"

     MyABC.register(AnotherClass)

     obj = AnotherClass()
     print(isinstance(obj, MyABC))  # Output: True
     ```

4. **Common ABCs in `collections.abc`**
   - **Example:**
     - `Container`: Requires `__contains__` method.
     - `Iterable`: Requires `__iter__` method.
     - `Sized`: Requires `__len__` method.
     - `Sequence`: Requires `__getitem__` and `__len__` methods.

### Implementing and Using ABCs

1. **Creating a Custom ABC**
   - **Example:**
     ```python
     from abc import ABC, abstractmethod

     class Shape(ABC):
         @abstractmethod
         def area(self):
             pass

         @abstractmethod
         def perimeter(self):
             pass

     class Rectangle(Shape):
         def __init__(self, width, height):
             self.width = width
             self.height = height

         def area(self):
             return self.width * self.height

         def perimeter(self):
             return 2 * (self.width + self.height)

     r = Rectangle(10, 20)
     print(r.area())       # Output: 200
     print(r.perimeter())  # Output: 60
     ```

2. **Using ABCs for Type Checking**
   - **Example:**
     ```python
     from collections.abc import MutableSequence

     class MyList(MutableSequence):
         def __init__(self):
             self._items = []

         def __len__(self):
             return len(self._items)

         def __getitem__(self, index):
             return self._items[index]

         def __setitem__(self, index, value):
             self._items[index] = value

         def __delitem__(self, index):
             del self._items[index]

         def insert(self, index, value):
             self._items.insert(index, value)

     m = MyList()
     m.insert(0, 'a')
     print(m[0])  # Output: a
     ```

### Practical Applications

1. **Defining Protocols for APIs**
   - **Example:**
     ```python
     class PaymentProcessor(ABC):
         @abstractmethod
         def process_payment(self, amount):
             pass

     class StripePaymentProcessor(PaymentProcessor):
         def process_payment(self, amount):
             print(f"Processing payment of {amount} through Stripe")

     processor = StripePaymentProcessor()
     processor.process_payment(100)  # Output: Processing payment of 100 through Stripe
     ```

2. **Using ABCs in Frameworks and Libraries**
   - **Example:**
     ```python
     from collections.abc import MutableMapping

     class MyDict(MutableMapping):
         def __init__(self):
             self._data = {}

         def __getitem__(self, key):
             return self._data[key]

         def __setitem__(self, key, value):
             self._data[key] = value

         def __delitem__(self, key):
             del self._data[key]

         def __iter__(self):
             return iter(self._data)

         def __len__(self):
             return len(self._data)

     d = MyDict()
     d['key'] = 'value'
     print(d['key'])  # Output: value
     ```

### Conclusion
- Protocols and ABCs provide powerful mechanisms for defining and enforcing interfaces in Python.
- While protocols offer flexibility through convention, ABCs provide a formal structure that can be enforced and checked.
- Understanding and using these concepts can lead to more robust, maintainable, and reusable code, especially in larger projects and frameworks.

These detailed notes cover the key concepts and examples from Chapter 11 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.