n = int(input("Enter value of n: "))
if n < 0:
    print(f"{n} should be greater than 0")
else:
    f = 1
    for i in range(1, n + 1):
        f = f*i
    print(f"Factorial of {n} is: ", f)


