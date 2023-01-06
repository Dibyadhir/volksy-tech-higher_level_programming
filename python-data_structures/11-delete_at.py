#!/usr/bin/python3
def delete_at(my_list, idx):
    a = my_list.index(idx)
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list.remove(a)
        return my_list
