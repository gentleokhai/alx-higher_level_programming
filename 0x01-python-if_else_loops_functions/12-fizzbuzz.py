#!/usr/bin/python3
def fizzbuzz():
    for v in range(1, 101):
        if v % 3 == 0:
            v = "Fizz"
        elif v % 5 == 0:
            v = "Buzz"
        elif v % 15 == 0:
            v = "FizzBuzz"
        else:
            v = v
        print(f"{v}", end = ' ')
