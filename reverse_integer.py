n = int(input("Enter an integer: ")) # 23

rev = 0
while n != 0:
    digit = n % 10
    rev = (rev * 10) + digit
    n = rev // 10
    print(n)
# review this later