"""
import my_module5



print(my_module5.a)
my_module5.reusable_function()
obj = my_module5.A()
obj.method1()


from my_module5 import a, reusable_function

print(a)
reusable_function()


from my_module5 import *


print(a)
reusable_function()


import my_module5 as mm

print(mm.a)

mm.reusable_function()
"""


# import my_module6

"""
Module Search Path:

The module search path in Python is a sequence of directories that the Python interpreter searches when attempting to locate and import modules. This path is stored in the sys.path variable, which is a list of strings representing directory paths.
The sys.path is initialized when Python starts, and its contents typically include:

1. The directory containing the input script: If a script is being executed, its containing directory is added to the beginning of sys.path.
2. The current working directory: If Python is run interactively (e.g., in the shell) or using the -c or -m options, the current working directory is added to sys.path.
3. Directories specified by the PYTHONPATH environment variable: If the PYTHONPATH environment variable is set, its contents (a list of directories separated by colons on Unix-like systems or semicolons on Windows) are added to sys.path.
Installation-dependent default paths: These include directories where standard Python modules and third-party packages (like site-packages) are installed.
How to inspect and modify the module search path:
To view the current module search path, you can print sys.path:
Python

    import sys
    print(sys.path)
To add a directory to the module search path at runtime, you can append it to sys.path:
Python

    import sys
    sys.path.append('/path/to/your/custom/modules')
Note that modifications made to sys.path at runtime are temporary and only affect the current Python process.
To persistently add directories, you can set the PYTHONPATH environment variable before starting Python.
Understanding the module search path is crucial for managing Python projects, resolving import errors, and ensuring that Python can find and load the modules your code depends on.
"""

"""
import sys

print(sys.path)

sys.path.append("./Folder1")

import my_module6

print(my_module6.a)


import sys

print(sys.path)

sys.path.append("./Folder1")

from my_module6 import *

print(a)
print(b)
# print(c)

func1()
func2()
# func3()


import sys

print(sys.path)

sys.path.append("./Folder1")

import my_module6


print(my_module6.a)
print(my_module6.b)
print(my_module6.c)

my_module6.func1()
my_module6.func2()
my_module6.func3()


import sys

sys.path.append("./Folder1")


from my_module6 import a, b, c, func1, func2, func3

print(a)
print(b)
print(c)

func1()
func2()
func3()


import sys

sys.path.append("./Folder1")

import my_module6 as mm

print(mm.a)
print(mm.b)
print(mm.c)

mm.func1()
mm.func2()
mm.func3()


import my_module7
print(__name__)

from MyPackage1 import my_module1

my_module1.foo()

from MyPackage1.InnerPackage import inner_module

inner_module.bar()
"""

# import MyPackage1
from MyPackage1.my_module1 import foo

foo()
