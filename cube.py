"""
Write a program to display cube of a number up to a given integer.
Input number of terms: 5
Expected output:
Number is: 1 and cube is : 1
Number is: 2 and cube is : 8
Number is: 3 and cube is : 27
Number is: 4 and cube is : 64
Number is: 5 and cube is : 125
"""
import math
n = int(input("Input number of terms: "))

for i in range(1, n + 1):
    cube = math.pow(i, 3)
    print(f"Number is: {i} and cube is : {int(cube)}")
