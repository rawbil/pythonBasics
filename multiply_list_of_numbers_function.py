def multiply_list(*numbers):
    total = 1
    for i in numbers:
        total *= i
    print(total)


multiply_list(20, 20, 20)
