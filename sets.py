# Unordered collections of items with no duplicates(unique)
# Defined by curly brackets
# Duplicates will be removed when creating a set or operation on existing set.
# Sets can be used instead of lists when we know that each element is unique and immutable.

set1 = {1, 2, 2, 0, 4}
set1.add(4)  # if you add an element that is already there, it will not be added.
# Also, it adds the element at the beginning of the set, not the end
set1.pop()  # removes the first element, and does not allow any values in the brackets
print(set1)

# set
# mutable, unordered and unique
set1 = {20, 34, 39, 20}
set1.add(32)
list1 = [100, 200, 300]
set1.update(list1)  # Adding elements from other collections, such as lists, tuples, dicts to a set
set1.copy()  # creates a copy of the set
set1.remove(100)  # removes an element from the set

set1.discard(34)  # removing an element from a set
print(type(set1))
print(set1)  # Prints the items in random order

#  Convert a list to a set
list1 = set([30, 38, 32])
print(20 in list1)
print(list1)

# Union of two sets
# The union of two sets A and B includes all the elements of set A and B.
# We use the | operator or the union() method to perform the set union operation

# first set
A = {10, 20, 30}
B = {100, 200, 300}
A.union(B)
print(A.union(B))
print(A | B)

# Set Intersection
# The intersection of two sets A and B includes the common elements between sets A and B.
# We use the & operator or the intersection() method to perform set intersection

A = {1, 2, 3}
B = {10, 20, 30, 2}
print("Set intersection using &: ", A & B)
print("Set intersection using intersection(): ", A.intersection(B))

# Set Difference
# The difference between two sets A and B include elements of set A not present in set B
# We use the - operator or the difference() method to perform the difference operation

A = {10, 30, 40, 20}
B = {10, 50, 30, 80, 57}
print("Difference using - operator: ", A - B)
print("Difference using difference(): ", A.difference(B))

# Checking if 2 sets are equal
if A == B:
    print(A)
