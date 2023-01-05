#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lst = my_list.reverse()
    for i in lst:
        print("{:d}".format(i))
