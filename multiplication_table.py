"""
Write a program to display the multiplication table of a give integer
Input the number(Table to be calculated): 15
Expected output:
15 * 1 = 15
...
...
15 * 10 = 150
"""
number = int(input("Input the number to be calculated: "))
multiplier = int(input("Input multiplier: "))

for i in range(1, multiplier + 1):
    output = int(number * i)
    print(f"{number} x {i} = {output}")
