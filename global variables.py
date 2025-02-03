x = "Cool"


def myFunc():
    global x
    x = "awesome"
    print("I am " + x)


myFunc()

print("I am " + x)
