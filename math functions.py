import math

# print(math.floor(10 / 3))

# factorial
n = int(input("Enter an integer\n"))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i
    i += 1
print(factorial)
