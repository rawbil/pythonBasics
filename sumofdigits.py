"""
Write a program to display sum of digits in a given number
Input:
    Enter any number: 125
Output:
    Sum of digits: 8
"""
n = int(input("Enter any number: "))
total = 0
digits = 0
while n > 0:
    lastDigit = n % 10
    total += lastDigit
    n = n // 10
print(f"Sum of digits: {total}")
