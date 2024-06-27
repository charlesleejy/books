## Chapter 3: Classes and Interfaces

#### Item 15: Minimize the accessibility of classes and members
**Explanation:**
- The principle of information hiding: make each class or member as inaccessible as possible.
- This minimizes the coupling between classes, which helps in maintaining and modifying the code.

**Guidelines:**
- Use the most restrictive access level that makes sense for a particular member.
- For top-level classes and interfaces, use package-private unless it needs to be used outside its package.
- For members of a class, use private unless they need to be accessible to other classes.

**Example:**
```java
public class Person {
    private String name;  // Private member, inaccessible outside the class

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

#### Item 16: In public classes, use accessor methods, not public fields
**Explanation:**
- Exposing fields directly can violate encapsulation, making the class harder to change in the future.

**Guidelines:**
- Always use getter and setter methods to provide access to fields.
- This approach allows you to enforce invariants and provide additional behavior.

**Example:**
```java
public class Point {
    private int x;
    private int y;

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
}
```

#### Item 17: Minimize mutability
**Explanation:**
- Immutable objects are simpler, safer, and more reliable than mutable ones.

**Guidelines:**
1. Don’t provide methods that modify the object’s state.
2. Ensure the class can’t be extended.
3. Make all fields final.
4. Make all fields private.
5. Ensure exclusive access to any mutable components.

**Example:**
```java
public final class Complex {
    private final double re;
    private final double im;

    public Complex(double re, double im) {
        this.re = re;
        this.im = im;
    }

    public double realPart() {
        return re;
    }

    public double imaginaryPart() {
        return im;
    }

    public Complex plus(Complex c) {
        return new Complex(re + c.re, im + c.im);
    }
}
```

#### Item 18: Favor composition over inheritance
**Explanation:**
- Composition provides greater flexibility by allowing the reuse of behaviors from multiple classes.

**Guidelines:**
- Use inheritance only when there is a true “is-a” relationship.
- Prefer using private fields that refer to instances of other classes (composition) and forward methods to these instances.

**Example:**
```java
public class InstrumentedHashSet<E> extends HashSet<E> {
    private int addCount = 0;

    @Override
    public boolean add(E e) {
        addCount++;
        return super.add(e);
    }

    @Override
    public boolean addAll(Collection<? extends E> c) {
        addCount += c.size();
        return super.addAll(c);
    }

    public int getAddCount() {
        return addCount;
    }
}
```
**Using Composition:**
```java
public class InstrumentedSet<E> extends ForwardingSet<E> {
    private int addCount = 0;

    public InstrumentedSet(Set<E> s) {
        super(s);
    }

    @Override
    public boolean add(E e) {
        addCount++;
        return super.add(e);
    }

    @Override
    public boolean addAll(Collection<? extends E> c) {
        addCount += c.size();
        return super.addAll(c);
    }

    public int getAddCount() {
        return addCount;
    }
}
```

#### Item 19: Design and document for inheritance or else prohibit it
**Explanation:**
- Inheritance should be designed and documented properly to avoid issues in subclasses.

**Guidelines:**
- Document precisely the self-use patterns in methods.
- Use the `final` keyword to prohibit inheritance if the class is not designed for inheritance.

**Example:**
```java
public class Super {
    public void overrideMe() { }

    public Super() {
        overrideMe();
    }
}

public class Sub extends Super {
    private final Date date;

    public Sub() {
        date = new Date();
    }

    @Override
    public void overrideMe() {
        System.out.println(date);
    }
}
```
**Prohibiting Inheritance:**
```java
public final class UtilityClass {
    private UtilityClass() {
        throw new AssertionError();
    }
}
```

#### Item 20: Prefer interfaces to abstract classes
**Explanation:**
- Interfaces are more flexible because a class can implement multiple interfaces.

**Guidelines:**
- Use interfaces to define types that can be implemented by any class.
- Abstract classes can be useful when you need to provide some default behavior.

**Example:**
```java
public interface Singer {
    void sing();
}

public interface Songwriter {
    void writeSong();
}

public class Artist implements Singer, Songwriter {
    @Override
    public void sing() {
        System.out.println("Singing a song.");
    }

    @Override
    public void writeSong() {
        System.out.println("Writing a song.");
    }
}
```

#### Item 21: Use interfaces only to define types
**Explanation:**
- Interfaces should only be used to define types, not to define constants.

**Guidelines:**
- Avoid using interfaces to define constants. Instead, use `enum` or constant classes.

**Example:**
```java
public interface PhysicalConstants {
    static final double AVOGADROS_NUMBER = 6.022_140_857e23;
    static final double BOLTZMANN_CONSTANT = 1.380_648_52e-23;
    static final double ELECTRON_MASS = 9.109_383_56e-31;
}
```
**Preferred:**
```java
public class PhysicalConstants {
    private PhysicalConstants() { } // Prevents instantiation

    public static final double AVOGADROS_NUMBER = 6.022_140_857e23;
    public static final double BOLTZMANN_CONSTANT = 1.380_648_52e-23;
    public static final double ELECTRON_MASS = 9.109_383_56e-31;
}
```

#### Item 22: Use static member classes instead of nonstatic
**Explanation:**
- Static member classes do not hold an implicit reference to the enclosing instance, which can avoid memory leaks.

**Example:**
```java
public class MyClass {
    private int outerField;

    public static class StaticNestedClass {
        // No implicit reference to MyClass
    }

    public class NonStaticNestedClass {
        // Holds an implicit reference to MyClass
    }
}
```

These detailed notes with examples provide a thorough understanding of best practices for working with classes and interfaces in Java as outlined in Chapter 3 of "Effective Java" by Joshua Bloch. For more in-depth reading, refer to the book itself.