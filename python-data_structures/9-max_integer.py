#!/usr/bin/python3
def max_integer(my_list):
    if len(my_list) == 0:
        return None
    else:
        max = -1
        for i in my_list:
            if max < i:
                max = i
        return max
