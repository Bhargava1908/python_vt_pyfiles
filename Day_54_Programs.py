import math



"""
l = [83, 45, 90, 12, 67, 89, 45, 32, 21, 4]
print(type(l))


import array

a = array.array('i', [1, 2, 3, 4, 5, 6, "Seven"])
print(type(a))
print(a)
"""


"""
1. Find the largest number in the list.
"""
def find_maximum_number(l: list[int]) -> int:
    """
    This Function will find the maximum number in the given list
    :param l: list of integers
    :return: largest number in the list
    """
    # print(max(l))
    # l.sort()
    # return l[-1]
    # max_num = 0
    # max_num = -math.inf
    # max_num = float("-inf")
    max_num = l[0]
    for cur_num in l:
        if cur_num > max_num:
            max_num = cur_num
    return max_num

l = [83, 45, 90, 12, 67, 89, 45, 32, 21, 4]
print(find_maximum_number(l))


"""
1. Find the largest number in the list.
"""
def find_minimum_number(l: list[int]) -> int:
    """
    This Function will find the maximum number in the given list
    :param l: list of integers
    :return: largest number in the list
    """
    # print(min(l))
    # l.sort()
    # return l[0]
    # max_num = 0
    # max_num = math.inf
    # max_num = float("inf")
    max_num = l[0]
    for cur_num in l:
        if cur_num < max_num:
            max_num = cur_num
    return max_num

l = [83, 45, 90, 12, 67, 89, 45, 32, 21, 4]
print(find_maximum_number(l))


"""
Input: l = ["The sun rises in the east", "program", "Rama killed Ravana"]
Output: Thesunrisesintheeastprogramramakilledravana
"""
def combine_characters(my_list):
    result = ''
    for sentence in my_list:
        """
        words_list = sentence.split(' ')
        combined_words = ''.join(words_list)
        result += combined_words
        """
        result += sentence.replace(' ', '')
    return result

l = ["The sun rises in the east", "program", "Rama killed Ravana"]
print(combine_characters(l))


"""
Search for an element in the list
If found, return the index
If not found, return -1
Input: l = [83, 90, 12, 67, 89, 45, 32, 21, 4], 45
Output: 5
"""
def linear_search(l: list[int], key: int) -> int:
    """
    This function will search for an element in the list.
    If the element is found, it will return the index value where it is found.
    If the element is not found, it will return -1.
    :param l: list of intergers
    :param key: element which has to be searched in the list
    :return: index value of the key if it is found, -1 if it is not found.
    """
    index: int
    for index in range(len(l)):
        if l[index] == key:
            return index
    return -1

l = [83, 90, 12, 67, 89, 45, 32, 21, 4]
print(linear_search(l, 45))
print(linear_search(l, 90))
print(linear_search([1, 2, 3, 4, 5], 4))


def foo():
    return 1, 2

a = foo()
print(type(a)) # <class tuple>
print(a)

b, c = foo()
print(b)
print(c)

a = 1, 2, 3, 4, 5, 6
print(type(a))
print(a)


def foo():
    return [1, 2]

a = foo()
print(type(a))
print(a)


def foo():
    return [1, 2, 3], 4

a = foo()
print(type(a))
print(a)
