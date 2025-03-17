squares = [x ** 2 for x in range(10)]
print(squares)

# long format
squares = []
for x in range(10):
    x = x ** 2
    squares.append(x)
print(squares)

# list of squares for even numbers
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)
