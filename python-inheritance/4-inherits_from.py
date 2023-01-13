#!/usr/bin/python3
""" here module is documented """


def inherits_from(obj, a_class):
    """ method is documented """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
