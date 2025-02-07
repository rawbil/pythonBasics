"""def outer_func():
    var = 10

    def inner_func():
        var = 20
        print("Inner variable is: " + str(var))
    inner_func()
    print("Outer variable is: " + str(var))


outer_func()"""


def cube(x):
    def square(x):
        s = x * x
        return s

    c = square(n) * x
    print(c)


n = int(input("Enter a value: "))
(cube(n))
