# Circumference of a circle
"""
s= (a + b + c) /2
Area= math.sqrt(s×(s−a)×(s−b)×(s−c))
if !(a + b <= c)
"""
from math import sqrt

a = int(input("Enter side a: \n"))
b = int(input("Enter side b: \n"))
c = int(input("Enter side c: \n"))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    compute = (s * (s - a) * (s - b) * (s - c))
    area = sqrt(compute)

    print("Area of the triangle(Heron's formula) is: " + str(round(area, 2)))
else:
    print("❌Invalid inputs. The sum of 2 sides must be greater than the third one")
