"""
1. Accept a number from user and
   print all the numbers from 1 upto that number
Ex:
Input: 10
Output: 1 2 3 4 5 6 7 8 9 10

num = int(input("Enter N: "))
for i in range(1, num + 1):
    print(i, end=' ')
"""


"""
2. Accept a number from user and
   print all the Even numbers from 0 upto that number
Ex:
Input: 10
Output: 0 2 4 6 8 10

num = int(input("Enter N: "))
for i in range(num + 1):
    if (i % 2) == 0:
        print(i, end=' ')

for i in range(0, num + 1, 2):
    print(i, end=' ')
"""


"""
3. Accept a number from user and
   print all the Odd numbers from 1 upto that number
Ex:
Input: 10
Output: 1 3 5 7 9

num = int(input("Enter N: "))
for i in range(num + 1):
    if (i % 2) == 1:
        print(i, end=' ')

for i in range(1, num + 1, 2):
    print(i, end=' ')
"""


"""
Print all the integers between n1 and n2 (n2 is inclusive)

n1 = int(input("Enter N1: "))
n2 = int(input("Enter N2: "))
for i in range(n1, n2 + 1):
    print(i, end=' ')
"""

"""
Accept 2 numbers n1 and n2 and a number x. Check if x exists in between n1 and n2.
Ex: n1 = 10, n2 = 20, x = 15
True (Since 15 is in between 10 and 20)

n1 = 30, n2 = 50, x = 100
False (Since 100 is not in between 30 and 50)

n1 = int(input("Enter N1: "))
n2 = int(input("Enter N2: "))
x = int(input("Enter X: "))

flag = False
for i in range(n1, n2 + 1):
    if i == x:
        flag = True
if flag:
    print(f"{x} is in between {n1} and {n2}")
else:
    print(f"{x} is in not between {n1} and {n2}")


if x in range(n1, n2 + 1):
    print(f"{x} is in between {n1} and {n2}")
else:
    print(f"{x} is in not between {n1} and {n2}")


if n1 <= x <= n2:
# if (x >= n1) and (x <= n2):
    print(f"{x} is in between {n1} and {n2}")
else:
    print(f"{x} is in not between {n1} and {n2}")
"""


"""
Accept 2 numbers n1 and n2 and print all the even numbers between n1 and n2

n1 = int(input("Enter N1: "))
n2 = int(input("Enter N2: "))
for i in range(n1, n2 + 1):
    if (i % 2) == 0:
        print(i, end=' ')
print()


if n1 % 2 == 1:
    n1 += 1
for i in range(n1, n2 + 1, 2):
    print(i, end=' ')
"""


"""
Accept 2 numbers n1 and n2 and print all the even numbers between n1 and n2

n1 = int(input("Enter N1: "))
n2 = int(input("Enter N2: "))
for i in range(n1, n2 + 1):
    if (i % 2) == 1:
        print(i, end=' ')
print()


if n1 % 2 == 0:
    n1 += 1
for i in range(n1, n2 + 1, 2):
    print(i, end=' ')
"""


"""
Print a Multiplication Table

n = int(input("Enter Table: "))
times = int(input("Enter times: "))
for i in range(1, times + 1):
    print(f"{n} * {i} = {n * i}")
"""


"""
Accept 2 numbers and an operator and perform the operation
"""
a = int(input("Enter a Number: "))
b = int(input("Enter another Number: "))
op = input("Enter Operator: ")
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print("b value is Zero")
elif op == '//':
    if b != 0:
        print(a // b)
    else:
        print("b value is Zero")
elif op == '%':
    print(a % b)
elif op == '**':
    print(a ** b)
else:
    print("Invalid Operator Provided.")


match op:
    case '+': print(a + b)
    case '-': print(a - b)
    case '*': print(a * b)
    case '/':
        if b != 0:
            print(a / b)
        else:
            print("b value is 0")
    case '//':
        if b != 0:
            print(a // b)
        else:
            print("b value is 0")
    case '%': print(a % b)
    case '**': print(a ** b)
    case _: print("Invalid Operator Provided.")
