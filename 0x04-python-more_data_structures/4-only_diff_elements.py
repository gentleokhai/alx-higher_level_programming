#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for s in set_1:
        if s in set_2:
            my_list.append(s)
        else:
            continue
    return my_list
