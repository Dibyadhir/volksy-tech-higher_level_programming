#!/usr/bin/python3
"""this is documented"""


def read_file(filename=""):
    """here function is documented"""
    with open(filename,'r', encoding="utf-8") as f:
        print(f.read(), end='')
