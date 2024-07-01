## Chapter 20: Attribute Descriptors

#### Overview
- This chapter explains the concept of attribute descriptors in Python, a mechanism for customizing attribute access.
- Descriptors are used to manage the attributes of different classes uniformly, providing a powerful way to implement reusable attribute management patterns.

### Key Concepts

1. **Descriptors**
   - **Definition:** Objects that define how attribute access is interpreted by defining any of the methods `__get__`, `__set__`, or `__delete__`.
   - **Purpose:** To customize the access and modification of attributes.

2. **Types of Descriptors**
   - **Data Descriptors:** Implement both `__get__` and `__set__` (or `__delete__`).
   - **Non-Data Descriptors:** Implement only `__get__`.

### Basic Descriptor Example

1. **Creating a Descriptor**
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

### How Descriptors Work

1. **Method Resolution Order (MRO)**
   - **Definition:** Determines the order in which classes are looked up when searching for a method.
   - **Example:**
     ```python
     class Base:
         pass

     class Sub(Base):
         pass

     print(Sub.mro())
     ```

2. **Descriptor Methods**
   - **`__get__(self, instance, owner)`:** Retrieves the attribute value.
   - **`__set__(self, instance, value)`:** Sets the attribute value.
   - **`__delete__(self, instance)`:** Deletes the attribute.

### Data Descriptors vs. Non-Data Descriptors

1. **Data Descriptors**
   - **Definition:** Implement both `__get__` and `__set__` methods.
   - **Example:**
     ```python
     class DataDescriptor:
         def __get__(self, instance, owner):
             return instance.__dict__['value']

         def __set__(self, instance, value):
             instance.__dict__['value'] = value

     class MyClass:
         value = DataDescriptor()

         def __init__(self, value):
             self.value = value

     obj = MyClass(10)
     print(obj.value)  # Output: 10
     obj.value = 20
     print(obj.value)  # Output: 20
     ```

2. **Non-Data Descriptors**
   - **Definition:** Implement only the `__get__` method.
   - **Example:**
     ```python
     class NonDataDescriptor:
         def __get__(self, instance, owner):
             return 'This is a non-data descriptor'

     class MyClass:
         value = NonDataDescriptor()

     obj = MyClass()
     print(obj.value)  # Output: This is a non-data descriptor
     obj.value = 'Overwritten'
     print(obj.value)  # Output: Overwritten
     ```

### Practical Applications

1. **Using Descriptors for Attribute Validation**
   - **Example:**
     ```python
     class Positive:
         def __get__(self, instance, owner):
             return instance.__dict__[self.name]

         def __set__(self, instance, value):
             if value < 0:
                 raise ValueError(f"{self.name} must be positive")
             instance.__dict__[self.name] = value

         def __set_name__(self, owner, name):
             self.name = name

     class MyClass:
         value = Positive()

         def __init__(self, value):
             self.value = value

     obj = MyClass(10)
     print(obj.value)  # Output: 10
     obj.value = 20
     print(obj.value)  # Output: 20
     # obj.value = -5  # Raises ValueError
     ```

2. **Using `__set_name__` for Automatic Name Assignment**
   - **Definition:** A method called during class creation to bind the descriptor to the attribute name.
   - **Example:**
     ```python
     class Descriptor:
         def __set_name__(self, owner, name):
             self.name = name

         def __get__(self, instance, owner):
             return instance.__dict__[self.name]

         def __set__(self, instance, value):
             instance.__dict__[self.name] = value

     class MyClass:
         attr = Descriptor()

         def __init__(self, value):
             self.attr = value

     obj = MyClass(10)
     print(obj.attr)  # Output: 10
     obj.attr = 20
     print(obj.attr)  # Output: 20
     ```

### Advanced Descriptor Features

1. **Class-Level Attribute Management**
   - **Example:**
     ```python
     class ClassLevelDescriptor:
         def __get__(self, instance, owner):
             return self

         def __set__(self, instance, value):
             raise AttributeError("Cannot modify class-level descriptor")

     class MyClass:
         attr = ClassLevelDescriptor()

     obj = MyClass()
     print(obj.attr)  # Output: <__main__.ClassLevelDescriptor object at ...>
     # obj.attr = 10  # Raises AttributeError
     ```

2. **Descriptor as Property Factory**
   - **Example:**
     ```python
     class PropertyFactory:
         def __init__(self, getter=None, setter=None, deleter=None):
             self.getter = getter
             self.setter = setter
             self.deleter = deleter

         def __get__(self, instance, owner):
             if self.getter is None:
                 raise AttributeError("unreadable attribute")
             return self.getter(instance)

         def __set__(self, instance, value):
             if self.setter is None:
                 raise AttributeError("can't set attribute")
             self.setter(instance, value)

         def __delete__(self, instance):
             if self.deleter is None:
                 raise AttributeError("can't delete attribute")
             self.deleter(instance)

     class MyClass:
         def __init__(self, value):
             self._value = value

         def get_value(self):
             return self._value

         def set_value(self, value):
             self._value = value

         def del_value(self):
             del self._value

         value = PropertyFactory(get_value, set_value, del_value)

     obj = MyClass(10)
     print(obj.value)  # Output: 10
     obj.value = 20
     print(obj.value)  # Output: 20
     del obj.value
     # print(obj.value)  # Raises AttributeError
     ```

### Conclusion
- Attribute descriptors provide a powerful mechanism for managing attribute access and implementing reusable patterns for attribute validation, computed attributes, and more.
- Understanding the difference between data and non-data descriptors and how to implement them is crucial for leveraging their full potential.
- Practical applications of descriptors include attribute validation, class-level attribute management, and using descriptors as property factories.
- Descriptors offer fine-grained control over attribute access, making them a valuable tool for advanced Python programming.

These detailed notes cover the key concepts and examples from Chapter 20 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.