#!/usr/bin/python3
"""This is classes and object"""


class Square:
    """this is square"""
    def __init__(self, size=0):

        try:
            if type(size) != int:
                raise TypeError
            elif size < 0:
                raise ValueError('size must be an integer')
            else:
                self.__size = size
        finally:
            pass
