n = int(input("Enter an integer: "))
if n == 0:
    print("Number cannot be 0")
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(f"factorial of {n}: {factorial}")