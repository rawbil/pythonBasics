unit = input("Choose unit of temperature: (F) for Fahrenheit, (C) for Centigrade: ")
measurement = ""
if unit.upper() == "F":
    final_unit = "Degrees Centigrade"
    measurement = final_unit
elif unit.upper() == "C":
    final_unit = "Fahrenheit"
    measurement = final_unit
else:
    print("Invalid input")

temp = float(input(f"Convert temperature to {measurement}: "))
result = 0

if unit.upper() == "F":
    centigrade = (temp - 32) / 1.8
    result = centigrade
elif unit.upper() == "C":
    fahrenheit = 1.8 * temp + 32
    result = fahrenheit
else:
    print("Invalid input")


# print final result
print(f"Temperature: {result}({measurement})")

"""
n = float(input("Enter temperature: \n"))
unit = input("Enter unit\n('c' for centigrade, 'f' for fahrenheit): \n")
result_unit = ''
result = ''
if unit.lower() == "f":
    result = float(((n - 32) * 5) / 9)
    result_unit = "centigrade"
elif unit.lower() == "c":
    result = float(((9 * n) + 160) / 5)
    result_unit = 'fahrenheit'
else:
    result = "oops...Invalid unit!"
    result_unit = 'invalid unit'

print("Temperature in " + result_unit + " is: " + str(result))
"""
