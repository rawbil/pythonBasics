def range_fun(x, y):
    n = int(input("Enter number: "))
    if n in range(x, y + 1):
        print(f"{n} is in the range ({x}, {y})")
    else:
        print(f"{n} is not in the range({x}, {y})")


range_fun(5, 10)
