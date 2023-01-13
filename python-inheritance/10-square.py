#!/usr/bin/python3
""" this is method validation """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ this is inherits from Rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
