"""
Tuple:
A Tuple is a collection of elements under a common variable name.

Characteristics:
1. Tuples are ordered.
2. Tuples are immutable.
3. Tuples allow duplicates.
4. Tuples allow values of different data types.
"""


# Creation of a tuple:
# Creation of an Empty Tuple:
# Syntax:
# <variable_name> = ()

# Example:
t1 = ()
print(type(t1))

t1 = tuple()
print(type(t1))


# Creation of elements with Tuples:
t1 = (1, 2, 3, 4, 5)
print(type(t1))
print(t1)

t1 = 1, 2, 3, 4
print(type(t1))
print(t1)


t1 = (1, 1, 2, 3, 2, 3, 4)
print(type(t1))
print(t1)

t1 = (1, 2.0, "Three", 4 + 5j, True)
print(type(t1))
print(t1)
"""
Accessing the elements in a tuple:
Indexing:
To access the individual elements from a tuple, we use indices.
1. Index in a tuple is from 0 to (length of tuple - 1).
2. We can also access the tuple elements from the end
   using negative indexing.
3. Negative indices range is from 1 to (length of tuple).
Syntax:
<tuple_variable_name>[<index>]

Example
"""
t1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("t1 data type is", type(t1))
# Positive Indexing
print(t1[0]) # 10
print(t1[9]) # 100
print(t1[4]) # 50

# Negative Indexing
print(t1[-1]) # 100
print(t1[-10]) # 10
print(t1[-4]) # 70

# print(t1[23]) # Index Error
# print(t1[-45]) # Index Error


"""
Slicing :
Extracting a portion of the tuple
Syntax:
<variable_name>[[start]:[stop]:[step]]
start is optional. Default value is 0.
stop is optional. Default value is (length of the tuple).
stop value is always excluded.
step is optional. Default value is 1.
"""
t1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(t1[:]) # (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(t1[0: 10]) # (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print(t1[0: 5]) # (10, 20, 30, 40, 50)
print(t1[: 5]) # (10, 20, 30, 40, 50)

print(t1[6: 10]) # (70, 80, 90, 100)
print(t1[6: ]) # (70, 80, 90, 100)

print(t1[3: 8]) # (40, 50, 60, 70, 80)

print(t1[1: 8: 2]) # (20, 40, 60, 80)
print(t1[3::3]) # (40, 70, 100)

# Slicing with Negative Indices
print(t1[-4:]) # (70, 80, 90, 100)
# print(t1[-4: 0]) #
print(t1[-8: -2]) # (30, 40, 50, 60, 70, 80)

print(t1[-3: -9: -1]) # (80, 70, 60, 50, 40, 30)
print(t1[-1: -9: -3]) # (100, 70, 40)

print(t1[5: 1]) # ()
print(t1[5: 1: -1]) # (60, 50, 40, 30)

print(t1[-1: -6]) # ()
print(t1[-8: -2: -1]) # ()


# Iterating over a tuple
t1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
for item in t1:
    print(item, end=' ')

print()

i = 0
while i < len(t1):
    print(t1[i], end=' ')
    i += 1
print()


# enumerate
for index, value in enumerate(t1):
    print(index, value)


t1 = (10, 20, 30, 40, 50)
t2 = (60, 70, 80, 90, 100)
print(list(zip(t1, t2)))

t1 = (10, 20, 30, 40, 50, 60, 70)
t2 = (60, 70, 80, 90, 100, 110)
t3 = (110, 120, 130, 140, 150)
print(list(zip(t1, t2, t3)))


"""
Tuple Methods:
1. index - returns the position of the first occurrence of the element
           if it is present.
           returns ValueError if the element is not present.
2. count - returns the frequency of the element.
"""
t1 = (10, 10, 20, 30, 40, 10, 10, 30, 30)
print(t1.count(10)) # 4
print(t1.count(100)) # 0

print(t1.index(20)) # 2
print(t1.index(30)) # 3

# print(t1.index(1000)) #
# in, not in
print(10 in t1) # True
print(100 in t1) # False

print(100 not in t1) # True
print(10 not in t1) # False

x = 100
if x in t1:
    print(t1.index(x))

# Identity Operators
t1 = (1, 2, 3, 4)
t2 = t1
print(id(t1))
print(id(t2))
print(t2 is t1) # True


t1 = (1, 2, 3, 4)
t2 = (1, 2, 3, 4)
print(id(t1))
print(id(t2))
print(t2 is t1) # True

t1 = (1, 2, 3, 4, 5)
t2 = (1, 2, 3, 4)
print(id(t1))
print(id(t2))
print(t2 is t1) # False

t1 = (0, 2, 3, 4)
t2 = (1, 2, 3, 4)
print(id(t1))
print(id(t2))
print(t2 is t1) # False

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
print(l1 == l2) # True
print(id(l1))
print(id(l2))
print(l1 is l2) # False


# Unpacking elements
# Assigning the items inside a tuple to individual variables.
a = (1, 2, 3)
b, c, d = a
print(b)
print(c)
print(d)

a = (10, 20, 30, 40, 50)
print(enumerate(a))
print(list(enumerate(a)))
for item in enumerate(a):
    print(item)

for index, value in enumerate(a):
    print("Index is = ", index, "Value = ", value)

a = (1, 2, 3, 4)
# b, c, d = a
# b, c, d, e, f = a
b, c, d, e = a
print(b, c, d, e)


# Create tuples using existing tuples
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)
t3 = t1 + t2
print(t3)
print(id(t1), id(t2), id(t3))

print("Before: ", id(t1), id(t2))
t1 = t1 + t2
print(t1)
print("After: ", id(t1), id(t2))

print("Before: ", id(t1), id(t2))
t1 += t2
print(t1)
print("After: ", id(t1), id(t2))

# Operators that can be used with Tuples
# + = Concatenation, * - Repetition
t1 = (1, 2, 3, 4)
t2 = t1 * 3
print(t2)


# Nested Tuples:
t1 = ((1, 2), (3, 4), (5, 6), (7, 8))
print(type(t1))

print(type(t1[0]))
print(t1[0])
a = t1[0]
print(a[1])

print(t1[0][1])
print(t1[2][0])

t1 = (1, 2, 3, 4)
t2 = (0, t1, 5, 6, 7)
print(t2)
