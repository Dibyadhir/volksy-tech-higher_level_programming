#!/usr/bin/python3
def weight_average(my_list):
    if len(my_list) == 0:
        return 0
    else:
        mul_add = 0
        add = 0
        for i in range(len(my_list)):
            a, b = my_list[i]
            mul = a * b
            add = add + b
            mul_add = mul_add + mul
        return mul_add / add
