"""
1. Find the count of all the characters in a string
Ex:
Input: String
Output: S = 1, t = 1, r = 1, i = 1, n = 1, g = 1

s = input("Enter a String....")
for char in s:
    count = 0
    for i in range(len(s)):
        if char == s[i]:
            count += 1
    print(f"{char} - {count}")

Time Complexity = O (n ** 2)
Space Complexity = O (1)


s = input("Enter a String....")
counts_dict = {}
for char in s:
    if char in counts_dict.keys():
        counts_dict[char] += 1
    else:
        counts_dict[char] = 1

for char, count in counts_dict.items():
    print(char, '-', count)

Time Complexity = O(n)
Space Complexity = O (n)
"""

s = input("Enter a String....")
counts_dict = {}
for char in s:
    counts_dict[char] = counts_dict.get(char, 0) + 1

for char, count in counts_dict.items():
    print(char, '-', count)