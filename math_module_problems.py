# calculate the square root of the sum of two numbers
"""Prompt the user to enter two numbers.

Calculate the sum of the two numbers.

Compute the square root of the sum using the math.sqrt() function.

Display the square root of the sum."""

import math

num1 = int(input("Enter first no: "))
num2 = int(input("Enter second no: "))


def Operation(x, y):
    add = x + y
    root = math.sqrt(add)
    return root


print(Operation(num1, num2))

"""Calculate the circumference and area of a circle.

Prompt the user to enter the radius of a circle.

Calculate the circumference of the circle using the formula 2 * math.pi * radius.

Calculate the area of the circle using the formula math.pi * radius ** 2.

Display the circumference and area of the circle."""

radius = int(input("Enter radius of circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Circumference of circle is: {circumference}")
print(f"Area of circle is: {area}")

"""Calculate the trigonometric functions of an angle.

Prompt the user to enter an angle in degrees.

Convert the angle to radians using the math.radians() function.

Calculate the sine, cosine, and tangent of the angle using
 the math.sin(), math.cos(),
  and math.tan() functions respectively.
"""

angle = int(input("Enter angle in degrees"))
radian = math.radians(angle)
sin = math.sin(radian)
cos = math.cos(radian)
tan = math.tan(radian)
print(sin)
print(cos)
print(tan)
