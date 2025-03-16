# Containers where items are accessed by a key
# To generate a dictionary, enclose a sequence of key-value pairs, separated by commas, in curly brackets
# The key can be any immutable object- a number, string or tuple
# New dictionary elements can be added, and existing ones can be changed, by using an assignment statement
# Order is not preserved in a dictionary, so printing will not necessarily print the items in the order they were added

dict1 = {1: 1, 2: 2, 'x': 10}
dict1['x'] = 0
dict1.pop(1)
print(dict1['x'])
print(dict1.items())

# get returns None if the key does not exist, else returns the value of the key
print(dict1.get(1))

###
dict2 = {
    'name': "He Who Must Not be Named",
    'age': 21,
    'salary': 104_000
}

for key, value in dict2.items():
    print(f'{key}: {value}')
