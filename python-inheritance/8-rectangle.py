#!/usr/bin/python3
""" here module is documented """


class Rectangle(BaseGeometry):
    """ here documented  a rectangle class using BaseGeometry."""

    def __init__(self, width, height):
        """ here method is documented """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
