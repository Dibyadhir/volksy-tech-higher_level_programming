#!/usr/bin/python3
def safe_print_list_integers(my_list, x):
    try:
        c = 0
        for i in range(x):
            if type(my_list[i]) == int:
                print(my_list[i], end="")
                c += 1
        return c
    except Exception :
        pass
