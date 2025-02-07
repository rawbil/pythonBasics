#  one-line functions

# add two numbers
"""
#Regular function
def sum(x, y):
    return x + y
"""
# lambda function
"""sum = lambda x, y: x + y
print(sum(3, 4))"""
square = lambda x: x ** 2
cube = lambda x: x ** 3

print(cube(square(2)))

# use lamda function in list for map, filter and sorted
