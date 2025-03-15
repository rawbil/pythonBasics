# Unordered collections of items with no duplicates(unique)
# Defined by curly brackets
# Duplicates will be removed when creating a set or operation on existing set.
# Sets can be used instead of lists when we know that each element is unique and immutable.

set1 = {1, 2, 2, 0, 4}
set1.add(4)  # if you add an element that is already there, it will not be added.
# Also, it adds the element at the beginning of the set, not the end
set1.pop()  # removes the first element, and does not allow any values in the brackets
print(set1)

#  Convert a list to a set
list1 = set([30, 38, 32])
print(20 in list1)
print(list1)
