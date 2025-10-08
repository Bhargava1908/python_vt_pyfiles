"""
Comments:
1. Comments are used to explain the code.
2. They increase the readability of the program.
3. They are used to debug the program.
4. They help us and other developers to easily
   understand the program without reading the whole code.
5. Comments are ignored by the python interpreter from executing.

Single Line Comment is denoted by #
"""
# This is a Single Line Comment.

print("Hello World!!!") # This will print "Hello World" to the console.


# Multi Line Comments:
"""
This
is
a
Multi
Line
Comment
"""

# or

'''
This
is
a
Multi
Line
Comment
'''

# IO
# Input and Output:
# Output:
# Displaying the result to the user
# print()
# print(*values, sep=' ', end='\n', file=sys.stdout, flush=False)
# *values = arbitrary number of values (variable number of values).
# sep = separator. Used to separate the values inside the statement.
#       Default value is ' '(space).
# end = ending. Specifies the last character that should be
#       printed at the last of the statement.
#       Default value is '\n' (new line).
# file = used to print the output to a file.
#        Default value is sys.stdout
# flush = To forcefully flush the output from the stream.
#         Default value is False.

print("lsdjfnalefnawlieufnaewflajejfnalejn")
print('ksjnskjnwslgf slej fosle al nalek nlaswk ems')
print(12345)

print('I')
print('I', 'am')
print('I', 'am', 'Learning')
print('I','am','Learning','Python')
print('I', 'am', 'Learning', 'Python', 'I', 'am', 'Learning', 'Python', 'I', 'am', 'Learning', 'Python')
print('I','am','Learning','Python', sep='*******')
print('I', 'am', 'Learning', 'Python', end='$$$$$$')
print('I', 'am', 'Learning', 'Print', 'Function', 'in', 'Python')
print("Hello \nWorld!!!")
print("Hello World!!!")
print("Hello \tWorld!!!")

with open("output.txt", 'w') as fp:
    print("Writing Output to a file", file=fp)


# Input
# input(prompt='')
# To accept values from the user
# print("Enter Input: ")
a = input("Enter Input: ")
print(a)
print(type(a))
print("a")
