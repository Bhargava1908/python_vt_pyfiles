# Comments
"""
1. Comments are lines that we use for explaining the program.
   Comments are pieces in a program that we use for documentation.
   Comments increase the readability of the program
   Comments are ignored by the interpreter.

Uses of Comments:
Code Explanation: Clarifying the purpose and logic of code sections.
Readability: Enhancing the overall readability of the code.
Debugging/Testing: Temporarily disabling code sections for testing or debugging.
Documentation: Providing notes, references, or context for future reference.

Syntax:
Single Line Comments:
#
Ex:
# This is a Single Line Comment
"""

# Multi Line Comments:
"""Opening and Closing"""
# or
'''Opening and Closing'''
"""
This
is
a
Multi
Line
Comment
"""

'''
This
is
a
Multi
Line
Comment
'''


"""
Output:
We use print function to display the output to the user.
print do not consider the meaning.
Syntax:
print(*<objects>, sep, end, file, flush)
sep => Separator. It is the character by which the objects will be separated.
       By Default, it will print ' '(space)
end => ending. It is the character which will be printed after all the objects are printed.
       By Default, it will print '\n' (new line).   
file => File argument is used to print the text to a file.
        By Default, It will print to sys.stdout
flush => To flush the text from the stream.
"""
print("I am Learning Python")
print("I am Learning", "Python")
print("I am", "Learning", "Python")
print("I", "am", "Learning", "Python")

print(1, 2)
print(1, 2, 3, 4, 5)

print("skerfaliserfnuelrfnhseroliufnhesorliu ealiru hseliueaoirlu aelcanerlcaiuezh vawiesurhv")

# With Separator
print("I","am","Learning","Python")
print("I","am","Learning","Python", sep='*********************')

print("I","am","Learning","Python", end='$$$$$$$$$$$$$$$$$$$$')
print("I","am","Learning","Python")

with open("output.txt", "w") as fp:
    print("Write the text to a file", file=fp)


# Input
# input(<prompt>)
# Input by default will return the value as a string
# Input will print the prompt message that is provided to the console.
# Default value for prompt is ""
# print("Enter Input: ")
a = input("Enter Input: ")
print(a)
print(type(a))
