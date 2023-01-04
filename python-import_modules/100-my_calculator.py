#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    lst = argv[1:]
    if len(lst) == 3:
        a, b, c = lst
        if b == "+":
            re = add(int(a), int(c))
        elif b == "-":
            re = sub(int(a), int(c))
        elif b == "*":
            re = mul(int(a), int(c))
        elif b == "/":
            re = div(int(a), int(c))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {}".format(a, b, c, re))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
