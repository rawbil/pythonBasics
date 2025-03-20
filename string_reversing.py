n = input("Enter a string: ")

reversed_string = ''
index = len(n) - 1
while index >= 0:
    reversed_string += n[index]
    index -= 1
print(reversed_string)
if n == reversed_string:
    print("This is a palindrome, it does not change")
