## 3rd edition of "Effective Java" by Joshua Bloch

### Introduction

### Chapter 1: Creating and Destroying Objects
- **Item 1**: Consider static factory methods instead of constructors
- **Item 2**: Consider a builder when faced with many constructor parameters
- **Item 3**: Enforce the singleton property with a private constructor or an enum type
- **Item 4**: Enforce noninstantiability with a private constructor
- **Item 5**: Prefer dependency injection to hardwiring resources
- **Item 6**: Avoid creating unnecessary objects
- **Item 7**: Eliminate obsolete object references
- **Item 8**: Avoid finalizers and cleaners
- **Item 9**: Prefer try-with-resources to try-finally

### Chapter 2: Methods Common to All Objects
- **Item 10**: Obey the general contract when overriding equals
- **Item 11**: Always override hashCode when you override equals
- **Item 12**: Always override toString
- **Item 13**: Override clone judiciously
- **Item 14**: Consider implementing Comparable

### Chapter 3: Classes and Interfaces
- **Item 15**: Minimize the accessibility of classes and members
- **Item 16**: In public classes, use accessor methods, not public fields
- **Item 17**: Minimize mutability
- **Item 18**: Favor composition over inheritance
- **Item 19**: Design and document for inheritance or else prohibit it
- **Item 20**: Prefer interfaces to abstract classes
- **Item 21**: Define interfaces only for type definitions
- **Item 22**: Use interfaces only to define types
- **Item 23**: Prefer class hierarchies to tagged classes
- **Item 24**: Favor static member classes over nonstatic
- **Item 25**: Limit source files to a single top-level class

### Chapter 4: Generics
- **Item 26**: Don't use raw types in new code
- **Item 27**: Eliminate unchecked warnings
- **Item 28**: Prefer lists to arrays
- **Item 29**: Favor generic types
- **Item 30**: Favor generic methods
- **Item 31**: Use bounded wildcards to increase API flexibility
- **Item 32**: Prefer generic methods
- **Item 33**: Consider typesafe heterogeneous containers

### Chapter 5: Enums and Annotations
- **Item 34**: Use enums instead of int constants
- **Item 35**: Use instance fields instead of ordinals
- **Item 36**: Use EnumSet instead of bit fields
- **Item 37**: Use EnumMap instead of ordinal indexing
- **Item 38**: Emulate extensible enums with interfaces
- **Item 39**: Prefer annotations to naming patterns
- **Item 40**: Consistently use the Override annotation
- **Item 41**: Use marker interfaces to define types

### Chapter 6: Lambdas and Streams
- **Item 42**: Prefer lambdas to anonymous classes
- **Item 43**: Prefer method references to lambdas
- **Item 44**: Use streams judiciously
- **Item 45**: Prefer Collection to Stream as a return type
- **Item 46**: Prefer side-effect-free functions in streams
- **Item 47**: Prefer method references to lambdas
- **Item 48**: Use caution when making streams parallel

### Chapter 7: Methods
- **Item 49**: Check parameters for validity
- **Item 50**: Make defensive copies when needed
- **Item 51**: Design method signatures carefully
- **Item 52**: Use overloading judiciously
- **Item 53**: Use varargs judiciously
- **Item 54**: Return empty collections or arrays, not nulls
- **Item 55**: Avoid unnecessary use of checked exceptions
- **Item 56**: Favor the use of standard exceptions
- **Item 57**: Use exceptions only for exceptional conditions
- **Item 58**: Favor the use of standard exceptions
- **Item 59**: Avoid unnecessary use of checked exceptions

### Chapter 8: General Programming
- **Item 60**: Avoid float and double if exact answers are required
- **Item 61**: Prefer primitive types to boxed primitives
- **Item 62**: Avoid strings where other types are more appropriate
- **Item 63**: Beware the performance of string concatenation
- **Item 64**: Refer to objects by their interfaces
- **Item 65**: Prefer interfaces to reflection
- **Item 66**: Use native methods judiciously
- **Item 67**: Optimize judiciously
- **Item 68**: Adhere to generally accepted naming conventions

### Chapter 9: Exceptions
- **Item 69**: Use exceptions only for exceptional conditions
- **Item 70**: Use checked exceptions for recoverable conditions and runtime exceptions for programming errors
- **Item 71**: Avoid unnecessary use of checked exceptions
- **Item 72**: Favor the use of standard exceptions
- **Item 73**: Throw exceptions appropriate to the abstraction
- **Item 74**: Document all exceptions thrown by each method
- **Item 75**: Include failure-capture information in detail messages

### Chapter 10: Concurrency
- **Item 76**: Synchronize access to shared mutable data
- **Item 77**: Avoid excessive synchronization
- **Item 78**: Prefer executors and tasks to threads
- **Item 79**: Prefer concurrency utilities to wait and notify
- **Item 80**: Document thread safety
- **Item 81**: Use lazy initialization judiciously
- **Item 82**: Don't depend on the thread scheduler

### Chapter 11: Serialization
- **Item 83**: Implement Serializable with great caution
- **Item 84**: Use a custom serialized form
- **Item 85**: Write readObject methods defensively
- **Item 86**: For instance control, prefer enum types to readResolve
- **Item 87**: Consider serialization proxies instead of serialized instances

### References

### Index

For more detailed information, you can refer to the official book page on [Pearson](https://www.pearson.com/en-us/subject-catalog/p/effective-java/P200000000138/9780134686042) and [O'Reilly](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/contents.xhtml) [oai_citation:1,Contents - Effective Java, 3rd Edition [Book]](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/contents.xhtml) [oai_citation:2,Effective Java](https://www.pearson.com/en-us/subject-catalog/p/effective-java/P200000000138/9780134686042).