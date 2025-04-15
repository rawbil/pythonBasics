"""
syntax
[expression for item in iterable if condition]
"""

squares = [x ** 2 for x in range(10)]
print(squares)

# long format
squares = []
for x in range(10):
    x = x ** 2
    squares.append(x)
print(squares)

# list containing all even numbers from 0 to 10
my_list = [i for i in range(10) if i % 2 == 0]
print(my_list)

# square of each even number from 0 to 10
squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(squares)

# Nested lists
nested_list = [[i * j for j in range(1, 4)] for i in range(1, 4)]
"""
i: 1              2           3
j: 1, 2, 3       1, 2, 3      1,2, 3
for each i[1, 2, 3], there is a j array [1,2,3] = [1, 2, 3], [2, 4, 6], [3, 6, 9]
"""
print(nested_list)

# List comprehension to convert strings in the list to uppercase
'''names = ['alice', 'john', 'watson', 'potter']
new_names = []
for i in range(len(names)):
    new_names.append(names[i].upper())
print(new_names) '''

names = [name.upper() for name in (['alice', 'john', 'watson', 'potter'])]
print(names)

# Filtering data - Returning only values divisible by 5
filtered_values = [i for i in range(10) if i % 5 == 0]
print(filtered_values)

# Flattening a list
nestedList = [[3, 4, 5], [1, 2, 4], [30, 39, 58]]
'''flattened_list = []
for i in nested_list:
    for j in i:
        flattened_list.append(j)
print(flattened_list)'''

flattened_list = [j for i in nestedList for j in i]
print(flattened_list)

# List comprehension can get very complicated for complex code, so avoid it in that case
