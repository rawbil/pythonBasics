"""
w-write
r-read
x-create
"""

"""file = open("File1.txt", "w")
file.write("Hi, my name is Bildad,"
           "and I am a pro at what I do"
           )

file.close()
print("File written successfully")"""

file = open("File1.txt", "r")
"""print(file.read()) # read the whole file
print(file.read(5)) # read characters-- in this case, 5"""
print(file.readline())  # read a single line
print(file.readline())
# When you add to readline() statements, it prints the first 2 lines

"""for x in file:
    print(x) # prints each line
"""
