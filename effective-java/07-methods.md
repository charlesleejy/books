## Chapter 7: Methods

#### Item 49: Check parameters for validity
**Explanation:**
- It’s important to validate the parameters of a method to ensure they meet the requirements. This helps catch errors early and provides clear feedback to the caller.

**Guidelines:**
- Use `IllegalArgumentException` for invalid arguments.
- Use `NullPointerException` for null arguments when null values are not permitted.
- Validate the parameters as close to the method entry as possible.

**Example:**
```java
public void setAge(int age) {
    if (age < 0) {
        throw new IllegalArgumentException("Age cannot be negative: " + age);
    }
    this.age = age;
}
```

#### Item 50: Make defensive copies when needed
**Explanation:**
- When accepting mutable objects as parameters or returning them, make defensive copies to prevent unexpected modifications.

**Guidelines:**
- Make a copy of the object before storing it if it’s mutable.
- Return a copy of the object if the internal state should not be modified.

**Example:**
```java
public class Period {
    private final Date start;
    private final Date end;

    public Period(Date start, Date end) {
        this.start = new Date(start.getTime());
        this.end = new Date(end.getTime());

        if (this.start.after(this.end)) {
            throw new IllegalArgumentException(start + " after " + end);
        }
    }

    public Date getStart() {
        return new Date(start.getTime());
    }

    public Date getEnd() {
        return new Date(end.getTime());
    }
}
```

#### Item 51: Design method signatures carefully
**Explanation:**
- Careful design of method signatures improves code readability, usability, and maintainability.

**Guidelines:**
- Avoid long parameter lists.
- Prefer using multiple methods instead of using boolean flags as parameters.
- Choose parameter types carefully to provide the correct level of abstraction.

**Example:**
```java
// Avoid boolean parameters
public void setAttributes(boolean visible, boolean enabled);

// Prefer separate methods
public void setVisible(boolean visible);
public void setEnabled(boolean enabled);
```

#### Item 52: Use overloading judiciously
**Explanation:**
- Overloading can make code more readable but can be confusing if not used properly. Overload methods only when their behavior is essentially identical.

**Guidelines:**
- Avoid using overloaded methods with the same number of parameters but different types.
- Prefer using different method names if the behavior differs significantly.

**Example:**
```java
// Overloading can be confusing
public boolean contains(int value);
public boolean contains(Object value);

// Prefer different method names
public boolean containsInt(int value);
public boolean containsObject(Object value);
```

#### Item 53: Use varargs judiciously
**Explanation:**
- Varargs (variable-length argument lists) are useful for methods that need to accept a flexible number of arguments. However, they should be used judiciously to avoid issues with type safety and performance.

**Guidelines:**
- Use varargs when the number of arguments is unknown and potentially large.
- Be cautious of methods that combine varargs with other parameters.

**Example:**
```java
public static void printNumbers(int... numbers) {
    for (int number : numbers) {
        System.out.println(number);
    }
}
```

#### Item 54: Return empty collections or arrays, not nulls
**Explanation:**
- Returning null instead of an empty collection or array can lead to NullPointerExceptions and complicates client code.

**Guidelines:**
- Always return empty collections or arrays to simplify client code and reduce the likelihood of null checks.

**Example:**
```java
public List<String> getNames() {
    return names != null ? names : Collections.emptyList();
}
```

#### Item 55: Include failure-capture information in detail messages
**Explanation:**
- Providing detailed information in exception messages helps diagnose issues more effectively.

**Guidelines:**
- Include the values of all parameters and other relevant data in the exception message.

**Example:**
```java
public void setBalance(double balance) {
    if (balance < 0) {
        throw new IllegalArgumentException("Negative balance: " + balance);
    }
    this.balance = balance;
}
```

#### Item 56: Avoid unnecessary use of checked exceptions
**Explanation:**
- Checked exceptions force callers to handle exceptions, which can lead to cumbersome code. Use checked exceptions only when the caller can reasonably recover from the exception.

**Guidelines:**
- Use unchecked exceptions for programming errors.
- Use checked exceptions for recoverable conditions.

**Example:**
```java
// Use unchecked exception for programming errors
public void setIndex(int index) {
    if (index < 0) {
        throw new IndexOutOfBoundsException("Index: " + index);
    }
    this.index = index;
}
```

#### Item 57: Use standard exceptions
**Explanation:**
- Java provides a rich set of standard exceptions that are well-understood and documented. Prefer using these exceptions over creating custom ones.

**Guidelines:**
- Use standard exceptions like IllegalArgumentException, IllegalStateException, NullPointerException, and IndexOutOfBoundsException.

**Example:**
```java
public void setValue(Object value) {
    if (value == null) {
        throw new NullPointerException("Value cannot be null");
    }
    this.value = value;
}
```

#### Item 58: Document all exceptions thrown by each method
**Explanation:**
- Documenting exceptions in the method's Javadoc helps the users of the API understand how to handle them.

**Guidelines:**
- Use the @throws Javadoc tag to document all exceptions that a method can throw.

**Example:**
```java
/**
 * Sets the age of the person.
 *
 * @param age the age to set
 * @throws IllegalArgumentException if age is negative
 */
public void setAge(int age) {
    if (age < 0) {
        throw new IllegalArgumentException("Age cannot be negative: " + age);
    }
    this.age = age;
}
```

#### Item 59: Use runtime exceptions for programming errors
**Explanation:**
- Runtime exceptions (unchecked exceptions) are suitable for programming errors that cannot be reasonably expected to be recovered from at runtime.

**Guidelines:**
- Use runtime exceptions for violations of preconditions that are not supposed to be violated by the client.

**Example:**
```java
public void withdraw(double amount) {
    if (amount > balance) {
        throw new IllegalArgumentException("Withdrawal amount exceeds balance");
    }
    balance -= amount;
}
```

#### Item 60: Avoid unnecessary use of checked exceptions
**Explanation:**
- Overuse of checked exceptions can clutter the client code. Use them only when the client can recover from the exception.

**Guidelines:**
- Prefer unchecked exceptions for errors that the client cannot be expected to recover from.

**Example:**
```java
// Use checked exception for recoverable condition
public void readFile(String path) throws IOException {
    BufferedReader reader = new BufferedReader(new FileReader(path));
    // ...
}

// Use unchecked exception for programming error
public void setIndex(int index) {
    if (index < 0) {
        throw new IndexOutOfBoundsException("Index: " + index);
    }
    this.index = index;
}
```

These detailed notes with examples provide a comprehensive understanding of best practices for designing and implementing methods in Java as outlined in Chapter 7 of "Effective Java" by Joshua Bloch. For more in-depth reading and additional details, refer to the book itself.