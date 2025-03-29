my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
print(my_list.index(30))

# Add values in an array
list2 = [20, 10, 30, 80, 50, 60]
total = 0
for i in range(len(list2)):
    total += list2[i]
print(total)


# Highest value in an array
def highest_value():
    highest = list2[0]
    for x in list2:
        if x > highest:
            highest = x
    return highest


print(highest_value())


# Lowest value
def lowest_value():
    lowest = list2[0]
    for y in list2:
        if y < lowest:
            lowest = y
    return lowest


print(lowest_value())
