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

"""# Write a program that accepts user input to create a list of integers.
# Then compute the sum of all the integers in the list.

my_list = []
list_length = int(input("Enter length of list: "))
total = 0
for i in range(list_length):
    n = int(input(f"Enter element in index {i}: "))
    my_list.append(n)
    # sum += n
total = sum(my_list)
print("New List: ",my_list)
print("Sum of items is: ", total)"""

"""my_tuple = "Harry Potter", "Goosebumps", "Lord of the Rings",

for i in my_tuple:
    print(i, end="\n")"""
"""# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
my_dict = {"name": "", "age": "", "fav_color": ""}
print(my_dict["name"])
for key, value in my_dict.items():
    n = input(f"Enter value for {key}: ")
    my_dict[key] = n
print(my_dict)"""

"""# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

set1 = set()
set2 = set()
n1 = int(input("Enter length of set 1: "))
n2 = int(input("Enter length of set 2: "))

for i in range(n1):
    n = input(f"Set1: Enter element number {i + 1}: ")
    set1.add(n)
print(set1)

for i in range(n2):
    n = input(f"Set2: Enter element number {i + 1}: ")
    set2.add(n)
print(set2)

print(set1 & set2)"""

# Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
my_list = ["item1", "item2", "item3", "item4", "item5", 'whoever', 'whatever']
int_list = []
"""
for i in my_list:
    for j in i:
        if j.isdigit():
            int(j)
            int_list.append(j)
print(int_list)"""

for word in my_list:
    for letter in word:
        if letter.isdigit():
            int_list.append(word)
# print(int_list)

# List comprehension


new_list = [word for word in my_list if any(letter.isdigit() for letter in word)]
print(new_list)
