#!/usr/bin/python3
def safe_print_list(my_list, x):
    try:
        c = 0
        for i in my_list[:x]:
            print(i, end="")
            c += 1
        print()
        return c
    except:
        pass
