"""
Sets:
A Set is a collection of unique elements.

Characteristics:
1. Sets are mutable.
2. Sets allow different data types.
3. Sets only allow immutable data types as members.
4. Sets only allow unique values.
5. Sets are unordered.
"""

# Creation of Sets
# Empty Set
a = set()
print(type(a))

# Set with Elements
a = {1, 2, 3, 4, 5}
print(type(a))

a = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(a)

a = {1, "Two", 3.0}
print(a)

a = {1, "Two", 3.0}
print(a)

# a = {{1, 2, 3}, 4, 5, 6}
# a = {[1, 2, 3], 4, 5, 6}

# Set Methods
"""
1. add() - Add new members to a set
2. remove() - remove existing elements from a set if the element is present.
              If the element is not present, raises a KeyError.
3. pop() - removes an arbitrary element from a set if the set is non empty.
           if the set is empty, raises error.
3. discard() - removes if the element exists and 
               ignores if the element doesn't exist in the set.
4. clear() - removes all the elements and makes the set empty.
4. union() - Performs Union of two sets. (A U B)
5. intersection() - Performs the intersection of two sets. (A ∩ B)
6. intersection_update() - Performs the intersection of two sets and
                           updates the original set. (A ∩ B)
7. difference() - Performs the set difference between two sets. (A - B)
8. difference_update() - Performs the set difference between two sets and
                           updates the original set. (A - B)
9. symmetric_difference() - Performs the symmetric difference between
                            two sets. (A U B) - (A ∩ B)
10. symmetric_difference_update() - Performs the symmetric difference
                                    between two sets and
                                    updates the original set.
                                    (A U B) - (A ∩ B)
11. update() - adds the elements from an iterable
12. isdisjoint() - 
13. issuperset() - 
14. issubset() - 

Subset and superset - If all the elements in the set a are members of set b, 
         then set a is called sub set of b.
         set b is called super set of a.

disjoint - If there are no common elements between both the sets,
           then the sets are disjoint.
"""
a = {1, 2, 3, 4}
a.add(5)
print(a)

a.add(1)
print(a)

a.remove(5)
print(a)

x = 100
if x in a:
    a.remove(100)
print(a)

b = a.discard(4)
a.discard(100)
print(a)

removed_element = a.pop()
print("Removed Element is ", removed_element)
print(a)

a.clear()
print(a)

# a.pop()


a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9, 10}
c = a.union(b)
print(c)


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9, 10}
c = a.union(b)
print(c)
print(a)

c = a.intersection(b)
print(c)

c = a.difference(b)
print(c)

c = a.symmetric_difference(b)
print(c)

print(a)
print(b)


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9, 10}
a.intersection_update(b)
print(a)


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9, 10}
a.difference_update(b)
print(a)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9, 10}
a.symmetric_difference_update(b)
print(a)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9, 10}
a.update(b)
print(a)

a = {1, 2, 3, 4, 5}
b = [4, 5, 6, 7, 8]
a.update(b)
print(a)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = a.issubset(b)
print(c)

a = {1, 2, 3, 10}
b = {1, 2, 3, 4, 5}
c = a.issubset(b)
print(c)


a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = b.issuperset(a)
print(c)

a = {1, 2, 3, 10}
b = {1, 2, 3, 4, 5}
c = b.issuperset(a)
print(c)

a = {1, 2, 3, 4}
b = {5, 6, 7, 8}
c = a.isdisjoint(b)
print(c)

a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8}
c = a.isdisjoint(b)
print(c)

a = {1, 2, 3, 4}
b = a
b.add(5)
print("a = ", a) # {1, 2, 3, 4, 5}
print("b = ", b) # {1, 2, 3, 4, 5}
print(id(a))
print(id(b))
print(a is b) # True

a = {1, 2, 3, 4}
b = a.copy()
b.add(5)
print(id(a))
print(id(b))
print(a is b) # False
# print(a == b)
print("a = ", a) # {1, 2, 3, 4}
print("b = ", b) # {1, 2, 3, 4, 5}


# Iterating over a set
a = {1, 2, 3, 4, 5}
for item in a:
    print(item, end=' ')
print()


"""
Operators that can be used with sets
| => Union, 
& - Intersection
- => difference
^ => symmetric difference,
> => proper superset
< => proper subset
>= => superset
<= => subset
== => Equality
!= => Not Equality
"""
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a | b
print(c) # {1, 2, 3, 4, 5, 6, 7, 8}
c = a & b
print(c) # {4, 5}
c = a - b
print(c) # {1, 2, 3}
c = a ^ b
print(c) # {1, 2, 3, 6, 7, 8}
a = {1, 2, 3}
b = {1, 2, 3}
c = (b <= a)
print(c) # True
c = (a <= b)
print(c) # True
c = (b < a)
print(c) # False
c = (a < b)
print(c) # False
c = (a >= b)
print(c) # True
c = (b >= a)
print(c) # True
c = (a > b)
print(c) # False
c = (b > a)
print(c) # False
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = (b <= a)
print(c) # True
c = (b < a)
print(c) # True
c = (a >= b)
print(c) # True
c = (a > b)
print(c) # True
a = {1, 2, 3, 4}
b = {1, 2, 3, 4}
c = (a == b)
print(c) # True
c = (a != b)
print(c) # False
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {1, 2, 3, 7, 8, 9, 10, 11}
d = a | b & c
print(d) # {1, 2, 3, 4, 5, 7, 8}


"""
Frozen Sets:
1. Frozen sets are immutable.

Uses:
1. Since they are immutable, they can be included as members in a set.
2. Since they are immutable, they can be used as keys for a dictionary.
"""

# Creation:
# Empty frozen set
# <set_variable_name> = frozenset()
a = frozenset()
print(type(a))
print(a)


# <set_variable_name> = frozenset(<iterable>)
a = frozenset([1, 2, 3, 4, 5])
print(type(a))
print(a)

a = frozenset((1, 2, 3, 4, 5))
print(type(a))
print(a)

a = frozenset({1, 2, 3, 4, 5})
print(type(a))
print(a)

a = frozenset({1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"})
print(type(a))
print(a)

"""
Methods for a frozen set
1. union() - Performs Union of two sets. (A U B)
2. intersection() - Performs the intersection of two sets. (A ∩ B)
3. difference() - Performs the set difference between two sets. (A - B)
4. symmetric_difference() - Performs the symmetric difference between
                            two sets. (A U B) - (A ∩ B)
5. isdisjoint() - 
6. issuperset() - 
7. issubset() - 
"""

a = frozenset({1, 2, 3, 4, 5})
b = frozenset({4, 5, 6, 7, 8})
c = a.union(b) # frozenset({1, 2, 3, 4, 5, 6, 7, 8})
print(c)
c = a.intersection(b)
print(c)

a = frozenset([1, 2, 3])
b = {1, 2, a, 3, 4, 5}
print(b)

a = [1, 2, 3]
b = frozenset(a)

c = (1, 2, 3)
d = frozenset(c)

print(b)
print(d)
print(id(b))
print(id(d))
print(b is d) #
