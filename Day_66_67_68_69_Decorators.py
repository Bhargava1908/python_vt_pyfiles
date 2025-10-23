"""
Higher-Order Functions: Functions that can take other functions as arguments
                        or return functions as results.
"""

"""
First Class Objects:
1. Those that can be assigned to variables
2. They can be passed as parameters to functions.
3. They can be returned from functions.
4. They can be stored in data structures such as lists, dictionaries etc
5. They can have attributes.

In Python, Functions are known as First Class Objects
"""


def foo():
    print("Hello World!!!")
    return 1

f1 = foo()
print(f1)

f2 = foo
print(f2)
f2()


def bar(my_func):
    print("Inside Function, Before Calling Function...")
    my_func()
    print("Inside Function, After Calling Function...")

def baz():
    print("Inside Baz Function, Hello World!!!")


bar(baz)


def outer_function():
    print("Inside Outer Function...")
    def inner_function():
        print("Inside Inner Function...")
    return inner_function


f = outer_function()
f()


def my_func():
    pass


my_func.description = "This is a sample function."
print(my_func.description)


def foo():
    print("Hello World!")
    fun()

# foo()

def fun():
    print("Its working...")

# foo()


def foo():
    return

print(foo())


def foo():
    print("Hello World!!!")


a = foo()
print("Value of a is", a)


"""
Decorators:
Python decorators are a powerful and elegant feature that allow modification or extension of the behavior of functions or 
methods without altering their source code.
Decorators are used to add extra functionality to the functions 
without modifying them.


Python decorators are a powerful and elegant feature that allow modification or extension of the behavior of functions or methods without altering their source code. They are essentially functions that take another function as an argument, add some functionality, and return a new function.
Key Concepts:
Functions as First-Class Objects: In Python, functions are treated as first-class objects, meaning they can be passed as arguments to other functions, returned from functions, and assigned to variables. This fundamental concept enables decorators.
Higher-Order Functions: Decorators are a type of higher-order function, which are functions that either take one or more functions as arguments or return a function as a result.
The @ Syntax: Python provides syntactic sugar for applying decorators using the @ symbol placed directly above the function definition to be decorated. 
How Decorators Work:
A decorator typically involves:
An outer function (the decorator itself): This function takes the function to be decorated as an argument.
An inner function (often called wrapper): This function is defined inside the decorator and is responsible for executing the original function and adding any extra logic (before or after the original function's execution).
Returning the wrapper function: The decorator returns this inner wrapper function, effectively replacing the original function with the enhanced version.
Example:
Python

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
Output:
Code

Something is happening before the function is called.
Hello, Alice!
Something is happening after the function is called.
Common Use Cases:
Logging: Adding logging statements before or after function execution.
Authentication/Authorization: Checking user permissions before allowing access to a function.
Timing/Benchmarking: Measuring the execution time of a function.
Caching: Storing the results of expensive function calls to avoid recalculation.
Input Validation: Validating arguments passed to a function.
Error Handling: Wrapping functions with try-except blocks for consistent error management.
"""


"""
def foo():
    print("Inside Foo...")

def wrapper(func):
    print("Before Calling the Function...")
    func()
    print("After Calling the Function...")

wrapper(foo)
"""

"""
def foo():
    print("Inside Foo...")

def decorator_function(func):
    def wrapper():
        print("Before Calling the Function...")
        func()
        print("After Calling the Function...")
    return wrapper

wrapper_function_obj = decorator_function(foo)
wrapper_function_obj()
"""


def decorator_function(func):
    def wrapper():
        print("Before Calling the Function...")
        func()
        print("After Calling the Function...")
    return wrapper


@decorator_function
def bar():
    print("Inside Bar Function...")

bar()


@decorator_function
def baz():
    print("Inside Baz Function...")

baz()


# Examples
import time


"""
def fun1():
    t1 = time.time()
    print("Inside Fun1")
    t2 = time.time()
    print("Time Taken to Execute fun1 is ", (t2 - t1))

def fun2():
    t1 = time.time()
    print("Inside Fun2")
    t2 = time.time()
    print("Time Taken to Execute fun2 is ", (t2 - t1))

def fun3():
    t1 = time.time()
    print("Inside Fun3")
    t2 = time.time()
    print("Time Taken to Execute fun3 is ", (t2 - t1))

fun1()
fun2()
fun3()
"""


def measure_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print("Time Taken to Execute fun is ", (t2 - t1))
    return wrapper

@measure_time
def fun1():
    print("Inside Fun1")

@measure_time
def fun2():
    print("Inside Fun2")

@measure_time
def fun3():
    print("Inside Fun3")

fun1()
fun2()
fun3()


# Decorator with Arguments
def decorator_function(func):
    def wrapper(a, b):
        print("Before Executing Function...")
        func(a, b)
        print("After Executing Function...")
    return wrapper

@decorator_function
def add(a, b):
    print(a + b)

add(10, 20)


def decorator_function(func):
    def wrapper(*args):
        print("Before Executing Function...")
        func(*args)
        print("After Executing Function...")
    return wrapper

@decorator_function
def add(a, b):
    print(a + b)

add(10, 20)



print('-' * 50)
"""
def decorator_function(func):
    def wrapper():
        print("Before Calling Foo Function...")
        func()
        print("After Calling Foo Function...")
    return wrapper


def foo():
    print("Inside Foo Function")

wrapper_function_obj = decorator_function(foo)
wrapper_function_obj()
"""

def decorator_function(func):
    def wrapper():
        print("Before Calling Foo Function...")
        func()
        print("After Calling Foo Function...")
    return wrapper

@decorator_function
def foo():
    print("Inside Foo Function")

foo()


def decorator_function(func):
    def wrapper(a, b):
        print("Before calling the Function...")
        func(a, b)
        print("After calling the Function...")
    return wrapper

@decorator_function
def add(a, b):
    print(f"Sum of {a} and {b} is {a + b}")

add(10, 20)


import time


"""
def fun1():
    t1 = time.time()
    print("Inside Funtion 1")
    t2 = time.time()
    print("Total Time Taken to execute is ", (t2 - t1))


def fun2():
    t1 = time.time()
    print("Inside Funtion 2")
    t2 = time.time()
    print("Total Time Taken to execute is ", (t2 - t1))

def fun3():
    t1 = time.time()
    print("Inside Funtion 3")
    t2 = time.time()
    print("Total Time Taken to execute is ", (t2 - t1))
"""

def measure_time_decorator(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print("Total Time taken to execute is ", (t2 - t1))
    return wrapper


@measure_time_decorator
def fun1():
    print("Inside Funtion 1")

@measure_time_decorator
def fun2():
    print("Inside Funtion 2")

@measure_time_decorator
def fun3():
    print("Inside Funtion 3")


fun1()
fun2()
fun3()


def decorator_with_variable_number_of_arguments(func):
    def wrapper(*args, **kwargs):
        print("Before Calling Function...")
        func(*args, **kwargs)
        print("After Calling Function...")
    return wrapper

@decorator_with_variable_number_of_arguments
def foo():
    print("This Function accepts no arguments")

@decorator_with_variable_number_of_arguments
def greet(name):
    print("Hello ", name)
    print("This Function accepts one argument")

@decorator_with_variable_number_of_arguments
def add(a, b):
    print(a + b)

foo()
greet("User")
add(100, 200)


"""
Types of Decorators
1. Function Decorators:
   These Decorators add extra functionality to the functions.

2. Method Decorators:
   These Decorators add extra functionality to the methods.

3. Class Decorators:
   These Decorators add extra functionality to the classes.
"""
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before Calling Function...")
        func(self, *args, **kwargs)
        print("After Calling Function...")
    return wrapper

class Foo:
    @method_decorator
    def add(self, a, b):
        print(f"Addition of {a} and {b} is {a + b}")


f = Foo()
f.add(50, 150)


def square_decorator(func):
    def wrapper(num):
        num **= 2
        func(num)
    return wrapper


def multiply_with_10(func):
    def wrapper(num):
        num *= 10
        func(num)
    return wrapper


@square_decorator
@multiply_with_10
def print_number(num):
    print("The Value of Number is: ", num)


print_number(2)


@multiply_with_10
@square_decorator
def print_number(num):
    print("The Value of Number is: ", num)


print_number(2)


# Preserving Function Data
def add(a: int, b: int) -> None:
    """
    This Function prints the result of addition of a and b
    :param a: integer
    :param b: integer
    :return: None
    """
    print(a + b)


print(add.__name__)
print(add.__doc__)


def greet_decorator(func):
    def wrapper(name):
        message = "Hello, " + name
        func(message)
    return wrapper


@greet_decorator
def print_name(name: str) -> None:
    """
    This function prints the name
    :param name: string
    :return: None
    """
    print(name)


print(print_name.__name__)
print(print_name.__doc__)


from functools import wraps

def greet_decorator(func):
    @wraps(func)
    def wrapper(name):
        message = "Hello, " + name
        func(message)
    return wrapper


@greet_decorator
def print_name(name: str) -> None:
    """
    This function prints the name
    :param name: string
    :return: None
    """
    print(name)


print(print_name.__name__)
print(print_name.__doc__)