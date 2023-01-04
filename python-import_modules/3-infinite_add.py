#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lst = argv[1:]
    sum = 0
    for i in lst:
        sum = sum + int(i)
    print(sum)
