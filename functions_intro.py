"""def my_function(fname, lname):
    print("Hello World")
    print(f"My name is {fname}, {lname}")


my_function("Bildad", "Simiyu")"""


# ____________________________
"""
# Multiple Arguments
def my_function(*students):
    print("The second student is: " + students[1])


my_function("one", "two", "three")"""


'''def fun():
    for i in range(1, 11):
        print("Hello World")

fun()'''

'''def fun():
    print("Hello World")

for i in range(1, 11):
    fun()
'''

'''def fun(i):
    for j in range(1, i + 1):
        print(j, end='\t')

fun(5)'''

def add_fun(a, b):
    c = a + b
    return c

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
print(add_fun(a, b))
