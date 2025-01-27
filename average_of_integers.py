# write a python program to find out the average
# of a set of integers

count = int(input("Enter the integer count: "))
total = 0
for i in range(1, count + 1):
    integer = int(input("Enter an integer: "))
    total += integer
    if i == count:
        avg = total / count
        print(f"Average is: {avg}")
