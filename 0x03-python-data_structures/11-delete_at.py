def delete_at(my_list=[], idx=0):
    if idx < 0:
        new_list = my_list
        return new_list
    if idx > len(my_list):
        new_list = my_list
        return new_list
    else:
        new_list = my_list
        del(new_list[idx])
        return new_list
