## Chapter 7: Better Living in Objectville: Planning for the Future

#### Overview
- This chapter focuses on designing classes and objects with future growth and maintenance in mind.
- It covers object-oriented design principles, including encapsulation, inheritance, polymorphism, and designing for change.

### Key Concepts

1. **Object-Oriented Design Principles**
   - **Encapsulation:** Keeping data private and providing public methods to access and modify that data.
   - **Inheritance:** Creating new classes based on existing ones, promoting code reuse.
   - **Polymorphism:** Designing objects to share behaviors, allowing different objects to be treated as instances of the same class through a common interface.
   - **Design for Change:** Writing code that can adapt to future changes with minimal modification.

### Detailed Breakdown

1. **Encapsulation**
   - **Definition:** Encapsulation is the practice of keeping fields within a class private, then providing access to them via public methods.
   - **Purpose:** Protects the internal state of an object and promotes modularity.
   - **Example:**
     ```java
     public class Dog {
         private String name;
         private int size;

         public String getName() {
             return name;
         }

         public void setName(String name) {
             this.name = name;
         }

         public int getSize() {
             return size;
         }

         public void setSize(int size) {
             this.size = size;
         }

         void bark() {
             if (size > 60) {
                 System.out.println(name + " says Woof! Woof!");
             } else if (size > 14) {
                 System.out.println(name + " says Ruff! Ruff!");
             } else {
                 System.out.println(name + " says Yip! Yip!");
             }
         }
     }
     ```

2. **Inheritance**
   - **Definition:** Inheritance allows a class to inherit fields and methods from another class.
   - **Purpose:** Promotes code reuse and establishes a natural hierarchy.
   - **Example:**
     ```java
     public class Animal {
         private String name;

         public String getName() {
             return name;
         }

         public void setName(String name) {
             this.name = name;
         }

         void eat() {
             System.out.println(name + " is eating.");
         }
     }

     public class Dog extends Animal {
         void bark() {
             System.out.println(getName() + " says Woof!");
         }
     }

     public class AnimalTestDrive {
         public static void main(String[] args) {
             Dog d = new Dog();
             d.setName("Rover");
             d.eat();
             d.bark();
         }
     }
     ```
   - **Output:**
     ```
     Rover is eating.
     Rover says Woof!
     ```

3. **Polymorphism**
   - **Definition:** Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name.
   - **Purpose:** Enables one interface to be used for a general class of actions.
   - **Example:**
     ```java
     public class Animal {
         void makeSound() {
             System.out.println("Some sound");
         }
     }

     public class Dog extends Animal {
         void makeSound() {
             System.out.println("Woof");
         }
     }

     public class Cat extends Animal {
         void makeSound() {
             System.out.println("Meow");
         }
     }

     public class AnimalTestDrive {
         public static void main(String[] args) {
             Animal[] animals = {new Dog(), new Cat()};
             for (Animal animal : animals) {
                 animal.makeSound();
             }
         }
     }
     ```
   - **Output:**
     ```
     Woof
     Meow
     ```

4. **Designing for Change**
   - **Definition:** Writing code that anticipates future changes and is flexible enough to accommodate them.
   - **Purpose:** Makes the codebase easier to maintain and extend.
   - **Example:**
     - **Initial Design:**
       ```java
       public class Book {
           private String title;
           private String author;

           public Book(String title, String author) {
               this.title = title;
               this.author = author;
           }

           // Getters and setters
       }

       public class BookTestDrive {
           public static void main(String[] args) {
               Book b = new Book("Head First Java", "Kathy Sierra");
               System.out.println(b.getTitle() + " by " + b.getAuthor());
           }
       }
       ```
     - **Extended Design with Additional Attributes:**
       ```java
       public class Book {
           private String title;
           private String author;
           private int publicationYear;
           private String genre;

           public Book(String title, String author, int publicationYear, String genre) {
               this.title = title;
               this.author = author;
               this.publicationYear = publicationYear;
               this.genre = genre;
           }

           // Getters and setters
       }

       public class BookTestDrive {
           public static void main(String[] args) {
               Book b = new Book("Head First Java", "Kathy Sierra", 2005, "Programming");
               System.out.println(b.getTitle() + " by " + b.getAuthor() + ", " + b.getPublicationYear() + " (" + b.getGenre() + ")");
           }
       }
       ```

### Practical Examples

1. **Encapsulation Example**
   - **Source Code:**
     ```java
     public class Person {
         private String name;
         private int age;

         public String getName() {
             return name;
         }

         public void setName(String name) {
             this.name = name;
         }

         public int getAge() {
             return age;
         }

         public void setAge(int age) {
             this.age = age;
         }
     }

     public class PersonTestDrive {
         public static void main(String[] args) {
             Person p = new Person();
             p.setName("Alice");
             p.setAge(30);
             System.out.println(p.getName() + " is " + p.getAge() + " years old.");
         }
     }
     ```
   - **Output:**
     ```
     Alice is 30 years old.
     ```

2. **Inheritance and Polymorphism Example**
   - **Source Code:**
     ```java
     public class Shape {
         void draw() {
             System.out.println("Drawing a shape");
         }
     }

     public class Circle extends Shape {
         void draw() {
             System.out.println("Drawing a circle");
         }
     }

     public class Square extends Shape {
         void draw() {
             System.out.println("Drawing a square");
         }
     }

     public class ShapeTestDrive {
         public static void main(String[] args) {
             Shape[] shapes = {new Circle(), new Square()};
             for (Shape shape : shapes) {
                 shape.draw();
             }
         }
     }
     ```
   - **Output:**
     ```
     Drawing a circle
     Drawing a square
     ```

3. **Designing for Change Example**
   - **Source Code:**
     ```java
     public class Vehicle {
         private String brand;
         private String model;

         public Vehicle(String brand, String model) {
             this.brand = brand;
             this.model = model;
         }

         public String getBrand() {
             return brand;
         }

         public void setBrand(String brand) {
             this.brand = brand;
         }

         public String getModel() {
             return model;
         }

         public void setModel(String model) {
             this.model = model;
         }

         void startEngine() {
             System.out.println("Engine started");
         }
     }

     public class Car extends Vehicle {
         public Car(String brand, String model) {
             super(brand, model);
         }

         void startEngine() {
             System.out.println(getBrand() + " " + getModel() + " engine started");
         }
     }

     public class Bike extends Vehicle {
         public Bike(String brand, String model) {
             super(brand, model);
         }

         void startEngine() {
             System.out.println(getBrand() + " " + getModel() + " engine started");
         }
     }

     public class VehicleTestDrive {
         public static void main(String[] args) {
             Vehicle[] vehicles = {new Car("Toyota", "Corolla"), new Bike("Honda", "CBR")};
             for (Vehicle vehicle : vehicles) {
                 vehicle.startEngine();
             }
         }
     }
     ```
   - **Output:**
     ```
     Toyota Corolla engine started
     Honda CBR engine started
     ```

### Key Points to Remember

- **Encapsulation:** Protects an object's state by keeping fields private and providing public methods for access.
- **Inheritance:** Promotes code reuse by allowing new classes to inherit fields and methods from existing classes.
- **Polymorphism:** Enables objects to be treated as instances of their parent class, facilitating flexibility and interchangeability.
- **Designing for Change:** Write code that anticipates future changes, ensuring that modifications are easy to implement.

### Summary

- **Encapsulation:** Use private fields and public methods to control access to an object's state.
- **Inheritance:** Create hierarchical class structures to promote code reuse and logical organization.
- **Polymorphism:** Design methods that can operate on objects of multiple types, promoting flexibility.
- **Designing for Change:** Develop code with future modifications in mind, making it easier to maintain and extend.

These detailed notes provide an overview and breakdown of the key concepts and examples from Chapter 7 of "Head First Java" by Kathy Sierra and Bert Bates. For more in-depth explanations and additional exercises, refer to the book directly.