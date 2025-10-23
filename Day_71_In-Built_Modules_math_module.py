# Math Module
import math


sqrt_100 = math.sqrt(100)
print(sqrt_100) # 10.0

pow_10 = math.pow(10, 3)
print(pow_10)

num = 10
abs_num = abs(num)
print(abs_num)
num = -10
abs_minus_num = abs(num)
print(abs_minus_num)

print(math.floor(17.3)) # 17
print(math.floor(18.9)) # 18
print(math.floor(20)) # 20
print(math.floor(-45.45)) # -46
print(math.floor(-32.254)) # -33

print(math.ceil(69.75)) # 70
print(math.ceil(134.45)) # 135
print(math.ceil(50)) # 50
print(math.ceil(-37.89)) # -37
print(math.ceil(-54.45)) # -54

print(math.sin(10))
print(math.log(8, 2)) # 3

print(math.log10(100)) # 2.0
print(math.factorial(5)) # 120
print(math.pi) # 3.141592653589793

infinity = float("inf")
print(infinity)

infinity = math.inf
print(infinity)

negative_infinity = float("-inf")
print(negative_infinity)

negative_infinity = -math.inf
print(negative_infinity)

a = 15
b = 5
print ("The gcd of 5 and 15 is : ", end="")
print (math.gcd(b, a))
