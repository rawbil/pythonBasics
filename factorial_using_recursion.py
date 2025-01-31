def fun(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fun(n - 1)


n = int(input("Enter value of n\n"))
print(fun(n))

#  the function keeps going back like a loop, until the condition is no longer met
