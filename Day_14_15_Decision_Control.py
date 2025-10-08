# Decision Control
# 1. Simple If
"""
Syntax:
if <condition>:
    Body
"""
"""
num = 10
if num > 0:
    print("Number is Greater than Zero")
    print("Inside If 1")
    print("Inside If 2")
    print("Inside If 3")
print("Line 14")


# Example:

age = 20
if age > 18:
    print("Candidate is eligible for voting")

available_balance = 300
minimum_balance = 500
if available_balance < minimum_balance:
    print("Warning: Low Funds")
"""


# 2. If Else
"""
Syntax:
if <condition>:
    Body if condition is True
else:
    Body if condition is False
"""

# Example:
"""
num = 10
if num >= 0:
    print("Number is Positive")
else:
    print("Number is Negative")
print("Line 46")


age = 20
if age >= 18:
    print("Candidate is Eligible to Vote")
else:
    print("Candidate is not Eligible to Vote")

withdrawl_amount = 500
current_balance = 1000
# if current_balance >= withdrawl_amount:
if withdrawl_amount <= current_balance:
    print("Funds Transferred Successfully")
    current_balance -= withdrawl_amount # current_balance = current_balance - withdrawl_amount
    print("Current Balance is : ", current_balance)
else:
    print("Insufficient Funds!!!")
"""


# 3. elif Ladder
# Else Block is Optional
# Syntax:
# if <condition 1>:
#     Statements 1
# elif <condition 2>:
#     Statements 2
# elif <condition 3>:
#     Statements 3
# .....
# .....
# .....
# else:
#     Statements X

# Example:
"""
num = 10
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

num = 10
if num == 10:
    print("Number is Equal to 10")
elif num == 20:
    print("Number is Equal to 20")
elif num > 0:
    print("Number is Greater than 0")
elif num == 0:
    print("Number is Equal to 0")
elif num > 5:
    print("Number is Greater than 5")
print("Line 103")

num = 100
if num == 10:
    print("Number is Equal to 10")
elif num == 20:
    print("Number is Equal to 20")
elif num == 30:
    print("Number is Equal to 30")
elif num == 40:
    print("Number is Equal to 40")
else:
    print("None of the above conditions are True")
"""


# 4. Match (Switch) Statement
# 1. Match statement is used for code readability.
# 2. There is an optional _ case which will execute if the
#    value doesn't match with any of the above values.
# Syntax:
"""
match <variable_name>:
    case value1: 
        # Statement Set1
    case value2: 
        # Statement Set2
    case value3:
        # Statement Set3
    ....
    ....
    case _:
        # Statement Setn

a = 50
match a:
    case 1:
        print("a value is 1")
    case 2:
        print("a value is 2")
    case 3:
        print("a value is 3")
    case 4:
        print("a value is 4")
    case 5:
        print("a value is 5")
    case _:
        print("a value is either less than 1 or greater than 5")
"""


# Pass Statement
# 1. Pass Statement is an empty statement used to avoid the
# indentation errors.
# 2. In real world, sometimes we may want to skip the block of code
#    or may want to write the block after some time.
#    So, in such cases, to prevent the indentation error,
#    we use the pass statement
# 3. Pass statement can be used with Decision Control, loops,
#    functions, classes, Exceptions, etc.,
if True:
    pass
print("Line below the if block")

a = 8 + 5 * 3
print(a) # 23
# In the above case, multiplication will be executed first.
# But, If we want addition to be executed first,
# We modify the above statement as:
a = (8 + 5) * 3
print(a)

# Operator Precedence
#1. When there are multiple operators in an expression,
# the operators with the highest precedence will be executed first.
# This is called operator precedence.

a = 8 * 4 + 5 - 1 >> 2
# 1. Left to right
a = (((8 * 4) + 5) - 1) >> 2
# Evaluation:
# a = ((32 + 5) - 1) >> 2
# a = (37 -1) >> 2
# a = 36 >> 2
# a = 9
print(a)


# Nested Decision Control
# 1. Decision Control inside Decision Control is known as Nested Decision Control
# Syntax:
"""
if <condition1>:
    if <condition2>:
        # Statements 1
    else:
        # Statements 2
else:
    if <condition3>:
        # Statements 3
    else:
        # Statements 4
"""

"""
a = 10
if a > 0:
    if a == 10:
        print("a value is 10")
    else:
        print("a is positive but not equal to 10")
    print("Line 213")
elif a < 0:
    if a == -10:
        print("a value is -10")
    else:
        print("a is negative but not equal to -10")
    print("Line 219")
else:
    print("a value is 0")
    print("Line 222")
print("Statement outside elif")


num = 10
if num == 10:
    print("Number is equal to 10")
    print("Line 2")
    print("Line 3")
    print("Line 4")
    print("Line 5")
    print("Line 6")
else:
    print("Number is not equal to 10")
    print("Line 2")
    print("Line 3")
    print("Line 4")
    print("Line 5")
    print("Line 6")
"""

nationality = "Indian"
locality = "KPHB"
age = 25
if nationality == "Indian":
    if locality == "KPHB":
        if age >= 18:
            print("Candidate is eligible to vote")
        else:
            print("Candidate is minor")
    else:
        print("Candidate locality is different")
else:
    print("Only Indians can vote or (NRI's) can vote")


if (nationality == "Indian") and (locality == "KPHB") and (age >= 18):
    print("Candidate is eligible to vote")
else:
    print("Candidate is not eligible to vote")
