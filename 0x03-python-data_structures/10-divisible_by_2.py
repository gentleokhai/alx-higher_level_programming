#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for my in my_list:
        if my % 2 == 0:
            va = True
        else:
            va = False
        new_list = []
        new_list.append(va)
    return new_list
