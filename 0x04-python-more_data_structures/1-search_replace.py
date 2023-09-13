#!/usr/bin/python3
def search_replace(my_list, search, replace):
    myne = []
    for ny in my_list:
        if ny == search:
            ny = replace
        else:
            ny = ny
        myne.append(ny)
    return myne
