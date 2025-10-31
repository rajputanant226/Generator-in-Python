### Python Generators

A generator in Python is a special type of iterator that allows you to iterate over a sequence of values lazily, i.e., one at a time, on demand, without storing the entire sequence in memory.
Generators are especially useful for large datasets or infinite sequences, because they produce items one by one and save memory.

Creating Generators
There are two main ways to create a generator in Python:

### 1. Generator Functions

Use the yield keyword instead of return to produce values one at a time.

def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
for value in simple_generator():
    print(value)


Output:

1
2
3


Explanation:

yield pauses the function and sends a value back to the caller.

The next call resumes from where it left off.

### 2. Generator Expressions

Similar to list comprehensions but use parentheses () instead of square brackets [].

squares = (x**2 for x in range(5))

for num in squares:
    print(num)


Output:

0
1
4
9
16

Benefits

Reduce memory usage compared to lists for large sequences.

Useful for streaming data, reading files line by line, or generating infinite sequences.

Cleaner and more Pythonic than manually creating iterators.

Best Practices

Use generator expressions for simple sequences.

Use generator functions for complex logic or multiple yield statements.

Avoid converting large generators to lists unless necessary (list(generator)).

Combine with itertools module for advanced generator operations.
