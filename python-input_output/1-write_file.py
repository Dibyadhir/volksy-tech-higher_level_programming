#!/usr/bin/python3
"""this is module documented"""


def write_file(filename="", text=""):
    '''this is write function'''
    line = 0
    with open(filename, 'r', encoding="utf-8")as f:
        for i in f:
            line = line + 1
    return line
