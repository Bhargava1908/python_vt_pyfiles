a = 0
b = 1

def foo():
    print("Inside Module, Inside Foo")


def bar():
    print("Inside Module, Inside Bar")


class Baz:
    pass


class Qux:
    pass


__all__ = ["a", "foo"]
