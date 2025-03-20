"""
Assignment: Python Program to Count the Number of matching characters in a pair of string
"""
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

count = 0
for letter in str1:
    if letter in str2:
        count += 1

print(f"The number of matching characters are: {count}")

# If you want the characters to be unique, that is, let's say the first string is 'find' and the second string is a long string with 'find',
# even if there are other letters with 'ind' or 'd', it will only show the one with 'find'
# To do this, use set() to wrap the strings
"""for letter in set(str1):
    if letter in set(str2):"""
