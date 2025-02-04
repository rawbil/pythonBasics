# in fibonacci series, the sum of 2 numbers is equal to the third number
# formula: F(n) = F(n - 1) * F(n - 2) if n >= 2
# if n == 0, F(0) = 0 and if n == 1, F(1) = 1
# Assignment: Python program to find the Nth term in a Fibonacci series using recursion


def fib(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer"
    elif n == 1:  # first term
        return 0
    elif n == 2:  # second term
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input("Enter the value of n: "))
print(f'The {n}th Fibonacci number is: {fib(n)}')
