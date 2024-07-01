## Chapter 8: Serious Polymorphism: Exploiting Abstract Classes and Interfaces

#### Overview
- This chapter focuses on advanced object-oriented concepts: abstract classes and interfaces.
- It emphasizes the power of polymorphism and how to use abstract classes and interfaces to design flexible and maintainable code.

### Key Concepts

1. **Polymorphism**
   - **Definition:** The ability of different classes to respond to the same method call in different ways.
   - **Purpose:** Promotes flexibility and reusability in code.

2. **Abstract Classes**
   - **Definition:** A class that cannot be instantiated and is intended to be subclassed. It may contain abstract methods that must be implemented by subclasses.
   - **Example:**
     ```java
     abstract class Animal {
         private String name;

         public Animal(String name) {
             this.name = name;
         }

         public String getName() {
             return name;
         }

         public abstract void makeSound(); // Abstract method
     }

     class Dog extends Animal {
         public Dog(String name) {
             super(name);
         }

         public void makeSound() {
             System.out.println(getName() + " says Woof!");
         }
     }

     class Cat extends Animal {
         public Cat(String name) {
             super(name);
         }

         public void makeSound() {
             System.out.println(getName() + " says Meow!");
         }
     }
     ```

3. **Interfaces**
   - **Definition:** A reference type in Java that can contain only constants, method signatures, default methods, static methods, and nested types. Interfaces cannot contain instance fields or constructors.
   - **Purpose:** Provides a way to achieve abstraction and multiple inheritance.
   - **Example:**
     ```java
     interface Animal {
         void makeSound(); // Interface method (does not have a body)
     }

     class Dog implements Animal {
         public void makeSound() {
             System.out.println("Woof!");
         }
     }

     class Cat implements Animal {
         public void makeSound() {
             System.out.println("Meow!");
         }
     }
     ```

### Detailed Breakdown

1. **Abstract Classes in Detail**
   - **Characteristics:**
     - Cannot be instantiated.
     - Can contain abstract methods (methods without a body).
     - Can have both abstract and concrete methods.
     - Subclasses must provide implementations for all abstract methods.
   - **Example:**
     ```java
     abstract class Shape {
         private String color;

         public Shape(String color) {
             this.color = color;
         }

         public String getColor() {
             return color;
         }

         public abstract double area();
     }

     class Circle extends Shape {
         private double radius;

         public Circle(String color, double radius) {
             super(color);
             this.radius = radius;
         }

         public double area() {
             return Math.PI * radius * radius;
         }
     }

     class Rectangle extends Shape {
         private double width;
         private double height;

         public Rectangle(String color, double width, double height) {
             super(color);
             this.width = width;
             this.height = height;
         }

         public double area() {
             return width * height;
         }
     }

     public class ShapeTest {
         public static void main(String[] args) {
             Shape circle = new Circle("Red", 2.5);
             Shape rectangle = new Rectangle("Blue", 4, 5);

             System.out.println("Circle area: " + circle.area());
             System.out.println("Rectangle area: " + rectangle.area());
         }
     }
     ```
   - **Output:**
     ```
     Circle area: 19.634954084936208
     Rectangle area: 20.0
     ```

2. **Interfaces in Detail**
   - **Characteristics:**
     - Cannot contain instance fields.
     - Can contain default methods (methods with a body) and static methods.
     - Classes can implement multiple interfaces.
   - **Example:**
     ```java
     interface Drawable {
         void draw();
     }

     interface Colorable {
         void fillColor(String color);
     }

     class Circle implements Drawable, Colorable {
         private String color;

         public void draw() {
             System.out.println("Drawing a circle");
         }

         public void fillColor(String color) {
             this.color = color;
             System.out.println("Filling circle with color " + color);
         }
     }

     public class InterfaceTest {
         public static void main(String[] args) {
             Circle circle = new Circle();
             circle.draw();
             circle.fillColor("Red");
         }
     }
     ```
   - **Output:**
     ```
     Drawing a circle
     Filling circle with color Red
     ```

### Practical Examples

1. **Abstract Class Example**
   - **Source Code:**
     ```java
     abstract class Vehicle {
         private String name;

         public Vehicle(String name) {
             this.name = name;
         }

         public String getName() {
             return name;
         }

         public abstract void startEngine();
     }

     class Car extends Vehicle {
         public Car(String name) {
             super(name);
         }

         public void startEngine() {
             System.out.println(getName() + " engine started.");
         }
     }

     class Motorcycle extends Vehicle {
         public Motorcycle(String name) {
             super(name);
         }

         public void startEngine() {
             System.out.println(getName() + " engine started.");
         }
     }

     public class VehicleTest {
         public static void main(String[] args) {
             Vehicle car = new Car("Toyota");
             Vehicle motorcycle = new Motorcycle("Harley");

             car.startEngine();
             motorcycle.startEngine();
         }
     }
     ```
   - **Output:**
     ```
     Toyota engine started.
     Harley engine started.
     ```

2. **Interface Example**
   - **Source Code:**
     ```java
     interface Playable {
         void play();
     }

     interface Recordable {
         void record();
     }

     class MediaPlayer implements Playable, Recordable {
         public void play() {
             System.out.println("Playing media");
         }

         public void record() {
             System.out.println("Recording media");
         }
     }

     public class MediaPlayerTest {
         public static void main(String[] args) {
             MediaPlayer mediaPlayer = new MediaPlayer();
             mediaPlayer.play();
             mediaPlayer.record();
         }
     }
     ```
   - **Output:**
     ```
     Playing media
     Recording media
     ```

### Key Points to Remember

- **Abstract Classes:** Used to provide a common base class for other classes. They cannot be instantiated and may contain abstract methods that must be implemented by subclasses.
- **Interfaces:** Used to define a contract that classes can implement. They allow for multiple inheritance and can contain method signatures, default methods, and static methods.
- **Polymorphism:** Allows methods to do different things based on the object it is acting upon, even if they share the same name.

### Summary

- **Abstract Classes:** Use abstract classes when you have a base class that should not be instantiated on its own and you want to provide common functionality to subclasses.
- **Interfaces:** Use interfaces to define a contract that can be implemented by any class, regardless of where it sits in the class hierarchy.
- **Polymorphism:** Utilize polymorphism to design flexible and reusable code that can work with objects of different classes through a common interface.

These detailed notes provide an overview and breakdown of the key concepts and examples from Chapter 8 of "Head First Java" by Kathy Sierra and Bert Bates. For more in-depth explanations and additional exercises, refer to the book directly.