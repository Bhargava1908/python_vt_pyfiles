"""
1. Reverse a string

a = "Python"
b = ""
for i in a:
    b = i + b
print(b)

print(a[::-1])

a = list(a)
a.reverse()
b = ''.join(a)
print(b)
"""


"""
2. count the number of occurrences of a character in a string
   without using count method.

a = "Python Program"
key = input("Enter a Character")
count = 0
for char in a:
    if char == key:
        count += 1
print(count)
"""

"""
3. find the index position of a character in a string without using
  in-built methods.

a = "Strings in Python"
char = input("Enter a Character")
index = -1
for i in a:
    index += 1
    if i == char:
        break
print(f"{char} found at index: {index}")

a = "Strings in Python"
char = input("Enter a Character: ")
for i in range(len(a)):
    if a[i] == char:
        print(f"{char} is found at {i}")
        break
else:
    print(f"{char} is not found...")

a = "Strings in Python"
key = input("Enter a Character: ")
for index, char in enumerate(a):
    if char == key:
        print(f"{key} is found at {index}")
        break
else:
    print(f"{key} is not found...")
"""


"""
4. Find the count of vowels(a, e, i, o, u) and consonants in a string.

a = "PythonProgramOnStrings"
vowels = 0
consonants = 0
b = "AEIOUaeiou"
for i in a:
    # if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    if i in b:
        vowels += 1
    else:
        consonants += 1
print("Vowels count = ", vowels)
print("Consonants Count = ", consonants)

a = "PythonProgramOnStrings"
vowels = 0
b = "AEIOUaeiou"
for i in a:
    # if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    if i in b:
        vowels += 1
print("Vowels count = ", vowels)
print("Consonants Count = ", len(a) - vowels)
"""


"""
5. Reverse all the words in a string.
   Ex:
   Input: The Sun Rises in the East
   Output: East the in Rises Sun The

a = "The Sun Rises in the East"
b = a.split()
b.reverse()
a = ' '.join(b)
print(a)
"""


"""
6. Find all the words in a string with even length.
   Ex:
   Input: The Sun Rises in the East
   Output: 2 (in, East are the words with even length)
"""
a = "The Sun Rises in the East"
b = a.split()
count = 0
for word in b:
    if len(word) % 2 == 0:
        count += 1
print(count)
