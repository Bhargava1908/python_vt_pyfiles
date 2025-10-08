"""
Closure:
Accessing the variable of the parent function
even after the parent function execution is completed.


"""
def foo():
    return "Hello"

f1 = foo()
print(f1) # Hello

f2 = foo
print(f2) # <function object>
result = f2()
print(result)


# Closure
def greet(name):
    def say_hello():
        print("Hello ", name)

    return say_hello

f_obj = greet("User")
print(f_obj) # <function greet.<locals>.say_hello at 0x000002A0D5F8B560>
f_obj()
