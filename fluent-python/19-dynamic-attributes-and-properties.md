## Chapter 19: Dynamic Attributes and Properties

#### Overview
- This chapter covers how Python handles attributes dynamically.
- It discusses how to use properties, attribute descriptors, and special methods to manage and customize attribute access.

### Key Concepts

1. **Dynamic Attributes**
   - **Definition:** Attributes that are not defined in the class but are created at runtime.
   - **Example:**
     ```python
     class DynamicAttributes:
         def __init__(self, attribute):
             self.attribute = attribute

     obj = DynamicAttributes('value')
     obj.new_attribute = 'new value'
     print(obj.new_attribute)  # Output: new value
     ```

2. **Using `__getattr__` and `__getattribute__`**
   - **`__getattr__(self, name)`:** Called when an attribute is not found in the usual places.
   - **`__getattribute__(self, name)`:** Called for every attribute access, even when the attribute exists.
   - **Example:**
     ```python
     class MyClass:
         def __getattr__(self, name):
             return f"{name} not found"

         def __getattribute__(self, name):
             if name == 'special':
                 return 'This is special'
             else:
                 return super().__getattribute__(name)

     obj = MyClass()
     print(obj.special)  # Output: This is special
     print(obj.missing)  # Output: missing not found
     ```

3. **Using `__setattr__` and `__delattr__`**
   - **`__setattr__(self, name, value)`:** Called when an attribute assignment is attempted.
   - **`__delattr__(self, name)`:** Called when an attribute deletion is attempted.
   - **Example:**
     ```python
     class MyClass:
         def __setattr__(self, name, value):
             print(f'Setting {name} to {value}')
             super().__setattr__(name, value)

         def __delattr__(self, name):
             print(f'Deleting {name}')
             super().__delattr__(name)

     obj = MyClass()
     obj.attr = 'value'  # Output: Setting attr to value
     del obj.attr        # Output: Deleting attr
     ```

### Properties

1. **Using `property` for Managed Attributes**
   - **Definition:** Properties allow for managed attribute access with getter, setter, and deleter methods.
   - **Example:**
     ```python
     class Circle:
         def __init__(self, radius):
             self._radius = radius

         @property
         def radius(self):
             return self._radius

         @radius.setter
         def radius(self, value):
             if value < 0:
                 raise ValueError("Radius must be positive")
             self._radius = value

         @radius.deleter
         def radius(self):
             del self._radius

     c = Circle(5)
     print(c.radius)  # Output: 5
     c.radius = 10
     print(c.radius)  # Output: 10
     # c.radius = -10  # Raises ValueError
     ```

2. **Properties Using Decorators**
   - **Using `@property`, `@<property_name>.setter`, and `@<property_name>.deleter` decorators to define properties.**
   - **Example:**
     ```python
     class Person:
         def __init__(self, first_name, last_name):
             self.first_name = first_name
             self.last_name = last_name

         @property
         def full_name(self):
             return f"{self.first_name} {self.last_name}"

         @full_name.setter
         def full_name(self, name):
             first, last = name.split()
             self.first_name = first
             self.last_name = last

     p = Person('John', 'Doe')
     print(p.full_name)  # Output: John Doe
     p.full_name = 'Jane Smith'
     print(p.first_name)  # Output: Jane
     print(p.last_name)   # Output: Smith
     ```

### Attribute Descriptors

1. **Creating and Using Descriptors**
   - **Definition:** A way to customize access to attributes using special methods `__get__`, `__set__`, and `__delete__`.
   - **Example:**
     ```python
     class Descriptor:
         def __init__(self, name):
             self.name = name

         def __get__(self, instance, owner):
             return instance.__dict__[self.name]

         def __set__(self, instance, value):
             instance.__dict__[self.name] = value

         def __delete__(self, instance):
             del instance.__dict__[self.name]

     class MyClass:
         attr = Descriptor('attr')

         def __init__(self, value):
             self.attr = value

     obj = MyClass(10)
     print(obj.attr)  # Output: 10
     obj.attr = 20
     print(obj.attr)  # Output: 20
     del obj.attr
     # print(obj.attr)  # Raises AttributeError
     ```

2. **Using `property` as a Descriptor**
   - **Properties are implemented as descriptors.**
   - **Example:**
     ```python
     class MyClass:
         def __init__(self, value):
             self._value = value

         @property
         def value(self):
             return self._value

         @value.setter
         def value(self, new_value):
             self._value = new_value

     obj = MyClass(42)
     print(obj.value)  # Output: 42
     obj.value = 100
     print(obj.value)  # Output: 100
     ```

### Practical Applications

1. **Using Properties for Validation**
   - **Example:**
     ```python
     class Account:
         def __init__(self, balance):
             self._balance = balance

         @property
         def balance(self):
             return self._balance

         @balance.setter
         def balance(self, amount):
             if amount < 0:
                 raise ValueError("Balance cannot be negative")
             self._balance = amount

     account = Account(100)
     print(account.balance)  # Output: 100
     account.balance = 150
     print(account.balance)  # Output: 150
     # account.balance = -50  # Raises ValueError
     ```

2. **Using Descriptors for Reusable Attribute Management**
   - **Example:**
     ```python
     class Positive:
         def __init__(self, name):
             self.name = name

         def __get__(self, instance, owner):
             return instance.__dict__[self.name]

         def __set__(self, instance, value):
             if value < 0:
                 raise ValueError(f"{self.name} must be positive")
             instance.__dict__[self.name] = value

     class MyClass:
         x = Positive('x')
         y = Positive('y')

         def __init__(self, x, y):
             self.x = x
             self.y = y

     obj = MyClass(5, 10)
     print(obj.x, obj.y)  # Output: 5 10
     obj.x = 15
     print(obj.x)  # Output: 15
     # obj.y = -5  # Raises ValueError
     ```

### Conclusion
- Dynamic attributes and properties provide powerful tools for managing and customizing attribute access in Python.
- The use of `__getattr__`, `__getattribute__`, `__setattr__`, and `__delattr__` allows for fine-grained control over attribute access and modification.
- Properties and descriptors offer a clean and reusable way to implement validation, computed attributes, and other managed behaviors.
- Understanding and leveraging these features can lead to more robust, maintainable, and Pythonic code.

These detailed notes cover the key concepts and examples from Chapter 19 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.