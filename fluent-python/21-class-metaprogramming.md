## Chapter 21: Class Metaprogramming

#### Overview
- This chapter covers the advanced concept of metaprogramming in Python, focusing on class-level metaprogramming techniques.
- Metaprogramming involves writing code that manipulates other code, such as dynamically creating classes or modifying class definitions.

### Key Concepts

1. **Metaclasses**
   - **Definition:** A metaclass is a class of a class that defines how a class behaves. A class is an instance of a metaclass.
   - **Purpose:** To control class creation, modify class attributes, enforce coding standards, or automatically register classes.

2. **Custom Metaclasses**
   - **Definition:** Custom metaclasses are created by subclassing the `type` class.
   - **Example:**
     ```python
     class MyMeta(type):
         def __new__(cls, name, bases, class_dict):
             print(f'Creating class {name}')
             return super().__new__(cls, name, bases, class_dict)

     class MyClass(metaclass=MyMeta):
         pass

     # Output: Creating class MyClass
     ```

### Using Metaclasses

1. **Basic Metaclass Example**
   - **Example:**
     ```python
     class UpperCaseMeta(type):
         def __new__(cls, name, bases, class_dict):
             uppercase_attr = {
                 name.upper(): value
                 for name, value in class_dict.items()
                 if not name.startswith('__')
             }
             return super().__new__(cls, name, bases, uppercase_attr)

     class MyClass(metaclass=UpperCaseMeta):
         x = 10
         y = 20

     print(MyClass.X)  # Output: 10
     print(MyClass.Y)  # Output: 20
     ```

2. **Enforcing Coding Standards**
   - **Example:**
     ```python
     class NoMixedCaseMeta(type):
         def __new__(cls, name, bases, class_dict):
             for attr_name in class_dict:
                 if attr_name.lower() != attr_name:
                     raise ValueError("Attribute names must be all lowercase")
             return super().__new__(cls, name, bases, class_dict)

     class MyClass(metaclass=NoMixedCaseMeta):
         x = 10
         # Y = 20  # Raises ValueError
     ```

3. **Automatic Class Registration**
   - **Example:**
     ```python
     registry = {}

     class AutoRegisterMeta(type):
         def __new__(cls, name, bases, class_dict):
             new_class = super().__new__(cls, name, bases, class_dict)
             registry[name] = new_class
             return new_class

     class Base(metaclass=AutoRegisterMeta):
         pass

     class MyClass(Base):
         pass

     print(registry)
     # Output: {'Base': <class '__main__.Base'>, 'MyClass': <class '__main__.MyClass'>}
     ```

### Advanced Metaclass Techniques

1. **Overriding `__init__` in Metaclasses**
   - **Example:**
     ```python
     class InitMeta(type):
         def __init__(cls, name, bases, class_dict):
             print(f'Initializing class {name}')
             super().__init__(name, bases, class_dict)

     class MyClass(metaclass=InitMeta):
         pass

     # Output: Initializing class MyClass
     ```

2. **Using Metaclasses for Singleton Pattern**
   - **Example:**
     ```python
     class SingletonMeta(type):
         _instances = {}

         def __call__(cls, *args, **kwargs):
             if cls not in cls._instances:
                 cls._instances[cls] = super().__call__(*args, **kwargs)
             return cls._instances[cls]

     class Singleton(metaclass=SingletonMeta):
         def __init__(self, value):
             self.value = value

     s1 = Singleton(10)
     s2 = Singleton(20)
     print(s1.value)  # Output: 10
     print(s2.value)  # Output: 10
     print(s1 is s2)  # Output: True
     ```

### Practical Applications

1. **Validating Class Attributes**
   - **Example:**
     ```python
     class ValidateAttrsMeta(type):
         def __new__(cls, name, bases, class_dict):
             for attr_name, attr_value in class_dict.items():
                 if isinstance(attr_value, (int, float)) and attr_value < 0:
                     raise ValueError(f"Attribute {attr_name} must be non-negative")
             return super().__new__(cls, name, bases, class_dict)

     class MyClass(metaclass=ValidateAttrsMeta):
         x = 10
         y = -5  # Raises ValueError

     # Output: ValueError: Attribute y must be non-negative
     ```

2. **Automatic Method Binding**
   - **Example:**
     ```python
     class BindMethodsMeta(type):
         def __new__(cls, name, bases, class_dict):
             for attr_name, attr_value in class_dict.items():
                 if callable(attr_value):
                     setattr(cls, attr_name, cls.wrap_method(attr_value))
             return super().__new__(cls, name, bases, class_dict)

         @staticmethod
         def wrap_method(method):
             def wrapped(*args, **kwargs):
                 print(f"Calling {method.__name__}")
                 return method(*args, **kwargs)
             return wrapped

     class MyClass(metaclass=BindMethodsMeta):
         def foo(self):
             print("foo")

         def bar(self):
             print("bar")

     obj = MyClass()
     obj.foo()  # Output: Calling foo \n foo
     obj.bar()  # Output: Calling bar \n bar
     ```

### Dynamic Class Creation

1. **Using `type` to Dynamically Create Classes**
   - **Example:**
     ```python
     attributes = {'x': 5, 'y': 10}

     DynamicClass = type('DynamicClass', (object,), attributes)
     obj = DynamicClass()
     print(obj.x)  # Output: 5
     print(obj.y)  # Output: 10
     ```

2. **Modifying Class Attributes Dynamically**
   - **Example:**
     ```python
     def modify_class(cls):
         cls.new_attr = 'This is a new attribute'
         return cls

     @modify_class
     class MyClass:
         pass

     obj = MyClass()
     print(obj.new_attr)  # Output: This is a new attribute
     ```

### Conclusion
- Metaprogramming in Python, especially using metaclasses, provides powerful tools for customizing class creation and behavior.
- Metaclasses can be used for enforcing coding standards, implementing design patterns, automatic registration, and more.
- Understanding and leveraging metaclasses and dynamic class creation can lead to more flexible, maintainable, and expressive code.

These detailed notes cover the key concepts and examples from Chapter 21 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.