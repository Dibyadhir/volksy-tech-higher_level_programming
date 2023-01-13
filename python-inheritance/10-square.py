#!/usr/bin/python3
""" this is method validation """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ this is inherits from Rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
