"""
Print the numbers from a given number n till 0 using recursion
"""


def func(n):
    if n < 0:
        return

    else:
        print(n, end='\t')
        func(n - 1)


n = int(input("Enter value of n: "))
(func(n))
