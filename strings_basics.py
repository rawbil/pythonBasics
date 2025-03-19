"""message = "Hello"
for i in message:
    print(i)

index = 0
for i in range(index, len(message)):
    print(message[i])

"""

# isalnum
str1 = "hello"
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.islower())
print(str1.isupper())
print(str1.isspace())
print(str1.capitalize())
print(str1.strip())
print(str1.lstrip())  # leading whitespace
print(str1.rstrip())  # trailing whitespace

# id() - Returns memory address of the string
# variables with the same value are stored in the same memory location
a = 10
b = 11
print(f"value of a: {a}")
print("Memory address of a: ", id(a))

print(f"Value of b: {b}")
print(f"Memory address of b: {id(b)}")

ida = id(a)
idb = id(b)
if ida == idb:
    print("Both addresses are same")
else:
    print("Different addresses")

str1 = "Hello"
str2 = "hello"
print(f"Value of str1: {str1}")
print("Memory address of str1: ", id(str1))

print(f"Value of str2: {str2}")
print("Memory address of str2: ", id(str2))

if id(str1) == id(str2):
    print("String addresses are equal")
else:
    print("string addresses are not equal")
