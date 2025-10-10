"""
Generators:
Generators are an easy way to create Iterators.
Generator is a function that returns an iterator object
that produces a sequence of values when iterated over.

In simple terms, Generators are normal functions with yield keyword
instead of return keyword

Syntax:
def <function_name>:
    # body
    yield value

Note:
When the generator function is called, it does not execute the body immediately.
Instead, it will return a generator object.

Yield Keyword:
The yield keyword is used to produce one value from the generator and
pause the generator function's execution until the next value is
requested.

Uses of Generators:
1. Easy to Implement Iterators
2. Memory Efficient
3. Creation of Infinite Streams
4. Pipelining Generators


Generators in Python are a powerful and memory-efficient way to create iterators. They are functions that, instead of returning a single value and terminating, yield a sequence of values one at a time, pausing their execution state between each yielded value. This makes them particularly useful for working with large datasets or infinite sequences where loading all data into memory simultaneously would be impractical or impossible.
Here's a breakdown of key aspects:
1. Generator Functions:
A function becomes a generator function when it contains at least one yield statement.
When a generator function is called, it doesn't execute the function body immediately. Instead, it returns a generator object.
2. The yield Keyword:
The yield keyword is central to generators. When yield is encountered, the function pauses its execution, returns the value specified after yield, and saves its local state.
When the generator is iterated over again (e.g., in a for loop or using next()), the function resumes execution from where it left off, continuing until the next yield or the end of the function.
3. Generator Objects:
Generator objects are iterators, meaning they can be used in for loops and with functions like next().
Each call to next() on a generator object resumes the generator function and retrieves the next yielded value.
4. Generator Expressions:
Similar to list comprehensions, generator expressions provide a concise way to create generators. They use parentheses instead of square brackets.
Python

# Generator function example
def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i += 1

# Using the generator function
counter = count_up_to(5)
for num in counter:
    print(num)

# Generator expression example
squares = (x*x for x in range(10))
for sq in squares:
    print(sq)
Benefits of Generators:
Memory Efficiency: They generate values on demand, avoiding the need to store entire sequences in memory, which is crucial for large datasets.
Lazy Evaluation: Values are computed only when requested, improving performance in scenarios where not all values in a sequence might be needed.
Infinite Sequences: Generators can easily represent infinite sequences, as they only produce values as needed.
Cleaner Code: They can often lead to more readable and concise code compared to managing state explicitly in traditional iterators.


Generators in Python
Last Updated : 29 Jul, 2025
A generator function is a special type of function that returns an iterator object. Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. This allows the function to generate values and pause its execution after each yield, maintaining its state between iterations.

Example:




def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1
​
ctr = fun(5)
for n in ctr:
    print(n)

Output
1
2
3
4
5
Explanation: This generator function fun yields numbers from 1 up to a specified max. Each call to next() on the generator object resumes execution right after the yield statement, where it last left off.

Why Do We Need Generators?
Memory Efficient : Handle large or infinite data without loading everything into memory.
No List Overhead : Yield items one by one, avoiding full list creation.
Lazy Evaluation : Compute values only when needed, improving performance.
Support Infinite Sequences : Ideal for generating unbounded data like Fibonacci series.
Pipeline Processing : Chain generators to process data in stages efficiently.
Let's take a deep dive in python generators:

Creating Generators
Creating a generator in Python is as simple as defining a function with at least one yield statement. When called, this function doesn’t return a single value; instead, it returns a generator object that supports the iterator protocol. The generator has the following syntax in Python:

def generator_function_name(parameters):
    # Your code here
    yield expression
    # Additional code can follow

Example: we will create a simple generator that will yield three integers. Then we will print these integers by using Python for loop.




def fun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for val in fun():
    print(val)

Output
1
2
3
Yield vs Return
Yield: is used in generator functions to provide a sequence of values over time. When yield is executed, it pauses the function, returns the current value and retains the state of the function. This allows the function to continue from same point when called again, making it ideal for generating large or complex sequences efficiently.
Return: is used to exit a function and return a final value. Once return is executed, function is terminated immediately and no state is retained. This is suitable for cases where a single result is needed from a function.
Example with return:




def fun():
    return 1 + 2 + 3
​
res = fun()
print(res)

Output
6
Generator Expression
Generator expressions are a concise way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets and are more memory efficient.

Syntax:

(expression for item in iterable)

Example: We will create a generator object that will print the squares of integers between the range of 1 to 6 (exclusive).




sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)

Output
1
4
9
16
25
Applications of Generators in Python
Suppose we need to create a stream of Fibonacci numbers. Using a generator makes this easy, you just call next() to get the next number without worrying about the stream ending.

Generators are especially useful for processing large data files, like logs, because:
They handle data in small parts, saving memory
They don’t load the entire file at once
While iterators can do similar tasks, generators are quicker to write since you don’t need to define __next__ and __iter__ methods manually.

"""
def my_custom_generator(num):
    cur_value = 0

    while cur_value <= num:
        yield cur_value
        cur_value += 1


mcg = my_custom_generator(10)
print(mcg)

for value in my_custom_generator(5):
    print(value, end=' ')
print()


"""
Generator Expressions:
Generator Expressions are an easy way to create Generators.

Syntax:
(expression / value for <variable_name> in iterable / range([start,]stop[,step]))
"""
squares_generator = (i * i for i in range(10))
print(squares_generator)

for value in squares_generator:
    print(value, end=' ')
print()


"""
Pipelining Generators
Multiple Generators can be used to pipeline a series of operations.
"""
def even_numbers(num):
    for i in range(0, num, 2):
        yield i

"""
for i in even_numbers(10):
    print(i)
"""
def square(nums):
    for num in nums:
        yield num ** 2


print(square(even_numbers(10)))
# print(list(square(even_numbers(30))))
for value in square(even_numbers(40)):
    print(value, end=' ')
print()
