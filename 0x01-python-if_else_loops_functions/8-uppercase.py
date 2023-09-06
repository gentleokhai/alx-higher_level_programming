#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            upp = chr(ord(char) - 32)
        else:
            upp = char
        new_str += upp
    print("{}".format(new_str))
