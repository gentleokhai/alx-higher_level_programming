#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_di = sorted(a_dictionary)
    for k in a_dictionary:
        print("{}: {}".format(k, a_dictionary[k]))

