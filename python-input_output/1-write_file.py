#!/usr/bin/python3
"""this is module documented"""


def write_file(filename="", text=""):
    '''this is write function'''
    with open(filename, 'w', encoding="utf-8")as f:
        print(len(f.read()))
