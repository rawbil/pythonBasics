# Write a python program to generate
# the prime numbers from 1 to N
import math
m = int(input("Find prime numbers up to: "))

# Loop through each number
for n in range(2, m + 1):
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
