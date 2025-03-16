"""
Assignment:
 Write a Python program to display the sum of n numbers
 using a list
"""

numbers = []
length = int(input("Enter length of list: "))
for i in range(length):
    x = int(input(f"Insert value [{i}] into the list: "))
    numbers.append(x)
print(numbers)
print(f"The sum of the {length} numbers is: {sum(numbers)}")
