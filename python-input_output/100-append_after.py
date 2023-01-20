#!/usr/bin/python3
"""here module is documented"""


def append_after(filename="", search_string="", new_string=""):
    """ here function is documented"""
    text = ""
    with open(filename, 'r') as fp:
        for i in fp:
            text = text + i
            if search_string in i:
                text = text + new_string
    with open(filename, 'w') as w:
        w.write(text)
