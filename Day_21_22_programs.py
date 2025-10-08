"""
Count the number of digits in a number
Ex:
Input: 12345
Output: 5

num = int(input("Enter Number: "))
count = 0
if num == 0:
    count = 1
else:
    while num != 0:
        num //= 10
        count += 1
print(count)
"""


"""
Print the sum of digits in a number
Ex:
Input: 12345
Output: 15 (1 + 2 + 3 + 4 + 5)

num = int(input("Enter a Number: "))
result = 0
while num != 0:
    rem = num % 10
    result += rem
    num //= 10
print(result)
"""


"""
3. Reverse a Number
Ex:
Input: 12345
Output: 54321

num = int(input("Enter a Number: "))
result = 0
while num != 0:
    rem = num % 10
    result = (result * 10) + rem
    num //= 10
print(result)
"""


"""
Check if a number is Palindrome or not:
Palindrome - same after reverse
Ex:
Input: 12321
Output: Yes

Input: 12345
Output: No

num = int(input("Enter a Number: "))
temp = num
reverse = 0
while num != 0:
    rem = num % 10
    reverse = (reverse * 10) + rem
    num //= 10
if reverse == temp:
    print("Given Number is a Palindrome")
else:
    print("No, Given Number is not a Palindrome.")
"""


"""
Check If a number is armstrong or not.
Ex: 
Input: 153
Output: Yes, It is an armstrong number. ((1 ** 3) + (5 ** 3) + (3 ** 3) = 153)

num = int(input("Enter Number: "))
temp = num
count = 0
if num == 0:
    count = 1
else:
    while num != 0:
        num //= 10
        count += 1

num = temp
result = 0
while num != 0:
    rem = num % 10
    result = result + (rem ** count)
    num //= 10
if result == temp:
    print("Yes, It is an armstrong number")
else:
    print("No, It is not an armstrong number")

for num in range(1, 10000):
    temp = num
    count = 0
    if num == 0:
        count = 1
    else:
        while num != 0:
            num //= 10
            count += 1

    num = temp
    result = 0
    while num != 0:
        rem = num % 10
        result = result + (rem ** count)
        num //= 10
    if result == temp:
        print(result)
"""


"""
Check if a number is Prime or not
Prime Number: A number which is divisible by only one and itself.
Ex:
2, 3, 5, 7, 11, etc

num = int(input("Enter Number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Number is Prime")
else:
    print("Number is Not a Prime Number")

num = int(input("Enter Number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
        if count > 2:
            break
if count == 2:
    print("Number is Prime")
else:
    print("Number is Not a Prime Number")

num = int(input("Enter Number: "))
flag = True
for i in range(2, num):
    if num % i == 0:
        flag = False
        break
if flag:
    print("Number is Prime")
else:
    print("Number is Not a Prime Number")
"""

num = int(input("Enter Number: "))
flag = True
if num == 2:
    print("Prime Number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
            break
    if flag:
        print("Number is Prime")
    else:
        print("Number is Not a Prime Number")


"""
Print the factors for a number
"""
num = int(input("Enter Number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, '*', num // i, '=', num)