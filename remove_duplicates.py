"""
Write a program to remove all duplicates
 from a given string in python
"""


def remove_duplicates(str1):
    mySet = set()
    myList = []

    for letter in str1:
        if letter not in mySet:
            mySet.add(letter)
            myList.append(letter)
    return ''.join(myList)


n = input("Enter a string with duplicate values: ")
print(remove_duplicates(n))
