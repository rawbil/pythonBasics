a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

if a == 0:
    print("The value of coefficient a cannot be '0'")
else:
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + discriminant ** 0.5) / 2 * c
    root2 = (-b - discriminant ** 0.5) / 2 * c
    print(f"The roots are {root1} and {root2}")
    print("The roots are: " + str(root1) + " and " + str(root2))

