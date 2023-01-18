#!/usr/bin/python3
"""this is module documented"""


def write_file(filename="", text=""):
    '''this is write function'''
    line = 0
    with open(filename, 'w', encoding="utf-8")as f:
        return f.write(text)
