# while loop
"""number = 0
while number <= 10:
    number += 1
    print(number)
else:
    print("End")
"""

"""number = 1
total = 0
while number <= 10:
    total += number
    number += 1
print(total)"""

# Write a program to display the count of digits in a a given number,
# eg "185", "3 digits"
'''
a = input("Enter an integer: ")
digits = 0
if a.isdigit():
    while digits < (len(a)):
        digits += 1
else:
    print("Invalid input")
print(digits)
'''
"""a = int(input("Enter any number: "))
count = 0

while a > 0:
    count += 1
    a //= 10
print(count)"""

# for loop
"""total = 0
for i in range(10):
    total += i
print(total)"""

'''students = ["John", "Harry", "Ron"]
for i in students:
    print(f"My name is {i}")
    
'''
n = int(input("Enter value n\n"))

for i in range(1, n + 1):
    print(i, end='\t')
