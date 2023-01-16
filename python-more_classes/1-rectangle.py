#!/usr/bin/python3
""" this is documented """


class Rectangle:
    """ this is documented """
    def __init__(self, width=0, height=0):
        """ this is constructore """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ this is property """
        return self.__width

    @width.setter
    def width(self, value):
        """ this is setter """
        if value != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value != int:
            return TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
