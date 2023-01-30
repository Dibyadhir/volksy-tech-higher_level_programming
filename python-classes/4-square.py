#!/usr/bin/python3
""" This is classes and object. """


class Square:
    """ this is square. """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

 def area(self):
        return self.__size ** 2
