#!/usr/bin/python3
""" here module is documented """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ here documented  a rectangle class using BaseGeometry."""

    def __init__(self, width, height):
        """ here method is documented """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
