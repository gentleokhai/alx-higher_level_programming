#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = number % 10
if num > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, num))
elif num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
elif num < 6:
    print("Last digit of {} is {} and is not zero".format(number, num))