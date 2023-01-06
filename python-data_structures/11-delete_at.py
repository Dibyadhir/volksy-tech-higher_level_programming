#!/usr/bin/python3
def delete_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        a = my_list[idx]
        my_list.remove(a)
        return my_list
