# Part C — Interview Ready

## Q1: Explain the Output

**1. `print(type(True))`**  
Output: `<class 'bool'>`  
Explanation: `True` is a boolean value, so its type is `bool`.

---

**2. `print(isinstance(True, int))`**  
Output: `True`  
Explanation: In Python, `bool` is a subclass of `int`. So `True` is considered an integer internally.

---

**3. `print(True + True + False)`**  
Output: `2`  
Explanation: `True` behaves like `1` and `False` behaves like `0`. So the calculation becomes `1 + 1 + 0 = 2`.

---

**4. `print(int(3.99))`**  
Output: `3`  
Explanation: `int()` removes the decimal part. It truncates, it does not round.

---

**5. `print(bool("False"))`**  
Output: `True`  
Explanation: Any non-empty string is considered `True` in Python, even if the text says "False".

---

**6. `print(bool(""))`**  
Output: `False`  
Explanation: An empty string evaluates to `False`.

---

**7. `print(0.1 + 0.2 == 0.3)`**  
Output: `False`  
Explanation: Floating-point numbers are stored in binary, which causes small precision errors. So `0.1 + 0.2` is not exactly `0.3`.

---

**8. `print("5" + "3")`**  
Output: `"53"`  
Explanation: These are strings, so Python joins them together (concatenation).

---

**9. `print(5 + 3)`**  
Output: `8`  
Explanation: These are integers, so Python performs normal addition.

---

## Q2: Coding — Build a Type Analyzer Function

### Question

Write a function `analyze_value(value)` that takes any Python value and returns a formatted string containing:

- The value itself  
- Its type  
- Its truthiness (True/False)  
- Its length (if applicable, otherwise "N/A")

---

### Implementation

```python
def analyze_value(value):
    """Analyze a value and return its type, truthiness, and length."""

    value_type = type(value).__name__
    truthy = bool(value)

    try:
        length = len(value)
    except TypeError:
        length = "N/A"

    return (
        f"Value: {value} | "
        f"Type: {value_type} | "
        f"Truthy: {truthy} | "
        f"Length: {length}"
    )
### Function Implementation

```python
def analyze_value(value):
    """Analyze a value and return its type, truthiness, and length."""

    value_type = type(value).__name__
    truthy = bool(value)

    try:
        length = len(value)
    except TypeError:
        length = "N/A"

    return (
        f"Value: {value} | "
        f"Type: {value_type} | "
        f"Truthy: {truthy} | "
        f"Length: {length}"
    )
### Evaluation

This function is designed to handle any Python data type safely and generically.

- `type(value).__name__` extracts the readable name of the data type.
- `bool(value)` evaluates whether the value is truthy or falsy according to Python’s truth rules.
- `len(value)` is attempted inside a `try` block to prevent runtime errors.
- If the object does not support length (such as integers, floats, or booleans), the function gracefully returns `"N/A"` instead of crashing.

This approach ensures robustness, avoids type errors, and works for strings, lists, tuples, dictionaries, numbers, and more. The function demonstrates understanding of Python’s dynamic typing system and safe error handling.


## Q3: Debug — Find and Fix 4 Bugs

### Question

The following code contains multiple bugs. Identify and fix all of them.

---

### Original Buggy Code

```python
name = input("Name: ")
age = input("Age: ")

if age >= 18:
status = "Adult"
else:
status = "Minor"

print(f"name is {age} years old and is a {status}")
print(f"In 5 years: {age + 5}")

score = 85.5
print(f"Score: {score:.0}")
```

---

### Corrected Code

```python
name = input("Name: ")
age = int(input("Age: "))

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"{name} is {age} years old and is a {status}")
print(f"In 5 years: {age + 5}")

score = 85.5
print(f"Score: {score:.0f}")
```

---

### Evaluation

The original code had several issues:

1. `age` was stored as a string but compared to an integer, causing a type error.
2. The `if` and `else` blocks were incorrectly indented, causing a syntax error.
3. The formatted string printed the literal word `"name"` instead of the variable.
4. Adding `5` to `age` would fail because it was a string.
5. The float formatting specifier `:.0` was incorrect and needed to be `:.0f`.

After converting `age` to an integer, correcting indentation, properly referencing variables, and fixing the format specifier, the program runs correctly and produces the expected output.