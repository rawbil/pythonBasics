my_list = []
length = int(input("Enter number of elements in list: "))
num = int(input("Enter number to search in the list: "))

for i in range(length):
    item = int(input(f"Enter index {i} value: "))
    if item == num:
        print(f"{item} found in index {i}")
        break
