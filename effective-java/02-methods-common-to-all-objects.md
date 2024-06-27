## Chapter 2: Methods Common to All Objects

#### Item 10: Obey the general contract when overriding equals
**Explanation:**
- The `equals` method must adhere to its general contract, which includes properties like reflexivity, symmetry, transitivity, consistency, and non-nullity.

**Guidelines:**
1. **Reflexive:** For any non-null reference value `x`, `x.equals(x)` should return `true`.
2. **Symmetric:** For any non-null reference values `x` and `y`, `x.equals(y)` should return `true` if and only if `y.equals(x)` returns `true`.
3. **Transitive:** For any non-null reference values `x`, `y`, and `z`, if `x.equals(y)` returns `true` and `y.equals(z)` returns `true`, then `x.equals(z)` should return `true`.
4. **Consistent:** For any non-null reference values `x` and `y`, multiple invocations of `x.equals(y)` consistently return `true` or consistently return `false`, provided no information used in `equals` comparisons is modified.
5. **Non-nullity:** For any non-null reference value `x`, `x.equals(null)` should return `false`.

**Example:**
```java
public class PhoneNumber {
    private final short areaCode;
    private final short prefix;
    private final short lineNumber;

    public PhoneNumber(int areaCode, int prefix, int lineNumber) {
        this.areaCode = rangeCheck(areaCode, 999, "area code");
        this.prefix = rangeCheck(prefix, 999, "prefix");
        this.lineNumber = rangeCheck(lineNumber, 9999, "line number");
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof PhoneNumber)) return false;
        PhoneNumber pn = (PhoneNumber) o;
        return areaCode == pn.areaCode && prefix == pn.prefix && lineNumber == pn.lineNumber;
    }

    @Override
    public int hashCode() {
        return 31 * (31 * areaCode + prefix) + lineNumber;
    }

    private static short rangeCheck(int val, int max, String arg) {
        if (val < 0 || val > max)
            throw new IllegalArgumentException(arg + ": " + val);
        return (short) val;
    }
}
```

#### Item 11: Always override hashCode when you override equals
**Explanation:**
- If two objects are equal according to the `equals(Object)` method, then calling the `hashCode` method on each of the two objects must produce the same integer result.

**Guidelines:**
1. **Consistent with equals:** If `x.equals(y)` is true, then `x.hashCode() == y.hashCode()` must also be true.
2. **Consistent:** The `hashCode` method must consistently return the same integer, provided no information used in `equals` comparisons is modified.
3. **Performance:** The hash code should evenly distribute across the entire integer range for better performance in hash-based collections.

**Example:**
```java
@Override
public int hashCode() {
    int result = Short.hashCode(areaCode);
    result = 31 * result + Short.hashCode(prefix);
    result = 31 * result + Short.hashCode(lineNumber);
    return result;
}
```

#### Item 12: Always override toString
**Explanation:**
- Providing a good `toString` implementation makes your class much more user-friendly. It’s particularly important for debugging.

**Guidelines:**
- Provide a succinct yet informative representation that is easy for a person to read.
- Include all of the object's important information.

**Example:**
```java
@Override
public String toString() {
    return String.format("(%03d) %03d-%04d", areaCode, prefix, lineNumber);
}
```

#### Item 13: Override clone judiciously
**Explanation:**
- The `clone` method is intended to produce a copy of an object, but it can be tricky to implement correctly, especially for classes with mutable fields or complex structures.

**Guidelines:**
1. **Implements Cloneable:** A class should implement the `Cloneable` interface and override `clone` method.
2. **Return type:** The `clone` method should return an object obtained by calling `super.clone`.
3. **Field copies:** Any mutable fields must be deeply cloned.

**Example:**
```java
public class Stack implements Cloneable {
    private Object[] elements;
    private int size = 0;

    public Stack clone() {
        try {
            Stack result = (Stack) super.clone();
            result.elements = elements.clone();
            return result;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
```

#### Item 14: Consider implementing Comparable
**Explanation:**
- Implementing `Comparable` allows a class to be used in sorted collections and makes it easier to sort arrays of the class.

**Guidelines:**
1. **Natural ordering:** Implement the `compareTo` method to provide a natural ordering for instances of the class.
2. **Consistency with equals:** The `compareTo` method should be consistent with `equals`.

**Example:**
```java
public class PhoneNumber implements Comparable<PhoneNumber> {
    @Override
    public int compareTo(PhoneNumber pn) {
        int areaCodeDiff = Short.compare(areaCode, pn.areaCode);
        if (areaCodeDiff != 0) return areaCodeDiff;

        int prefixDiff = Short.compare(prefix, pn.prefix);
        if (prefixDiff != 0) return prefixDiff;

        return Short.compare(lineNumber, pn.lineNumber);
    }
}
```

These detailed notes and examples from Chapter 2 of "Effective Java" provide a thorough understanding of best practices for methods common to all objects. For more in-depth reading and additional details, refer to the book itself.