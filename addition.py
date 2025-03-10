x = int(input("Enter the first number: \n"))
y = int(input("Enter the second number: \n"))
sign = input("Enter arithmetic sign(+, - , /, *): \n")
result = ''

if sign == "+":
    result = x + y
elif sign == "-":
    result = x - y
elif sign == "/":
    result = x / y
elif sign == "*":
    result = x * y
else:
    print("Invalid arithmetic sign.")

print(f'The result of {x} {sign} {y} is: {result}')
