#!/usr/bin/python3
"""this documention"""


def append_write(filename="", text=""):
    '''this is write function'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
