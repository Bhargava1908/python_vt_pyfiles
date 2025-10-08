"""
def add(x, y):
    print(x + y)


add(10, 20)
add(100, 300)


def reverse_number(num):
    result = 0
    while num != 0:
        rem = num % 10
        result = (result * 10) + rem
        num //= 10
    return result


reverse_number(12345)
reverse_number(3456)


def is_palindrome(num):
    if reverse_number(num) == num:
        return True
    else:
        return False


num = int(input("Enter a Number: "))
if is_palindrome(num):
    print("The Given Number is a Palindrome...")
else:
    print("The Given Number is not a Palindrome...")
"""


# Print all the prime numbers between n1 and n2
def is_prime(num):
    if num == 1:
        return False

    flag = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
            break
    return flag


def print_primes_between_range(num1, num2):
    prime_numbers = []
    for i in range(num1, num2 + 1):
        if is_prime(i):
            # print(i, end=' ')
            prime_numbers.append(i)
    return prime_numbers

n1 = int(input("Enter N1: "))
n2 = int(input("Enter N2: "))
prime_numbers = print_primes_between_range(n1, n2)
print(prime_numbers)

