import math
import random


def generateotp():
    otp = ''
    for i in range(1, 5):  # 4-digit number
        random_no = random.random()  # generates random no between 0 and 1
        random_int = str(math.floor(random_no * 10))  # random number between 0 and 10 excluding 10
        otp += random_int
    print(f"The random 4-digit number is: {otp}")


generateotp()
