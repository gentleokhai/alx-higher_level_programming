#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 :
        my_list = my_list
    elif idx > len(my_list):
        my_list = my_list
    else:
        my_list[idx] = element
    return my_list   

