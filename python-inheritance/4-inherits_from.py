#!/usr/bin/python3
""" This is module docuentation """


def inherits_from(obj, a_class):
    """ This is module documentation """
    if issubclass(type(obj, a_class)) and type(obj) != a_class:
        return True
    else:
        return False
